#!/usr/bin/env python3
"""
extract.py

Processes the Metaviews: Future of Authority newsletter archive and extracts
signals, pattern candidates, stack material, and concepts for the Autonomy Stack.

Usage:
    python extract.py                  # Process all unprocessed issues
    python extract.py --limit 10       # Process next 10 issues only
    python extract.py --reset          # Clear checkpoint and reprocess all
    python extract.py --model <model>  # Override model (default: google/gemini-flash-1.5)

Requires:
    .env file (or environment) with OPENROUTER_API_KEY and optionally OPENROUTER_MODEL
    pip install openai python-dotenv
"""

import os
import csv
import json
import time
import re
import argparse
from pathlib import Path
from html.parser import HTMLParser

from dotenv import load_dotenv
from openai import OpenAI

# Ensure stdout handles full Unicode on Windows
import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Load .env from repo root (two levels up from this script)
load_dotenv(Path(__file__).parent.parent / ".env")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT      = Path(__file__).parent.parent
SOURCES_DIR    = REPO_ROOT / "sources" / "metaviews.substack.com"
POSTS_DIR      = SOURCES_DIR / "posts"
POSTS_CSV      = SOURCES_DIR / "posts.csv"
EXTRACTIONS_DIR = REPO_ROOT / "sources" / "extractions"
CHECKPOINT_FILE = EXTRACTIONS_DIR / ".checkpoint.json"

# ---------------------------------------------------------------------------
# Model configuration
# ---------------------------------------------------------------------------
DEFAULT_MODEL = os.environ.get("OPENROUTER_MODEL", "nvidia/nemotron-3-super-120b-a12b:free")
MAX_TOKENS    = 2048
DELAY         = 0.3   # seconds between requests

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# ---------------------------------------------------------------------------
# Extraction prompt
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are a careful analyst building the Autonomy Stack — a governance operating \
system that provides a reference architecture for understanding how authority \
forms, holds, and breaks down across interconnected systems.

The Stack is organized into six layers (reference axes):
  1. Material Base — food, energy, housing, logistics, environmental systems
  2. Commons & Institutions — co-ops, unions, municipalities, mutual aid, public agencies
  3. Legibility & Metrics — what systems can see, measure, and respond to
  4. Decision Systems & Authority — law, norms, algorithms, administrative processes
  5. Knowledge & Intelligence — research, media, shared situational awareness
  6. Human Capacity & Care — care systems, labor, disability inclusion, education

The Stack's core principles: authority must be contestable, power without \
legibility is unacceptable, disagreement is a design condition, resilience \
over elegance, legibility over expertise, failure is informative, nothing is final.

## Extraction methodology

Every issue is relevant — whether primarily journalistic or conceptual. \
Journalistic issues contain data, cases, and observations that inform the Stack \
even when they don't theorize directly. Extract accordingly.

When an insight spans multiple categories, include it in each relevant category \
and note the cross-reference explicitly (e.g. "Also logged as PATTERN CANDIDATE: \
Algorithmic Authority as Legitimacy Bypass"). This duplication is intentional — \
it preserves future opportunities for correlation and synthesis across the corpus.

Never assume a referenced framework, model, or concept is well-known or \
self-explanatory. Log every named framework or analytical lens as a CONCEPT entry, \
even if it appears in common discourse. The Stack's lexicon should be self-contained.\
"""

EXTRACTION_PROMPT = """\
Analyze this newsletter issue and extract relevant material into the following categories.

For each item, provide:
- A short descriptive title (5–8 words)
- The synthesized content (not a direct quote — distill the insight)
- A brief source note (paraphrase of the originating passage)
- Cross-reference note if the item is also logged under another category

---

## Categories

### SIGNAL
A shift in attention, emerging tension, newly visible assumption, or pattern \
beginning to take shape. Should be concise — under 150 words. A good signal \
illuminates context without resolving it.

### PATTERN CANDIDATE
A recurring dynamic that could be abstracted into a reusable governance pattern. \
Describe: the phenomenon, the context in which it appears, the forces that produce it, \
and the consequences of engaging with or ignoring it.

### STACK MATERIAL
Analysis that maps to a specific layer, challenges a layer's current framing, \
or introduces a concept the Stack's architecture should incorporate. \
Always note which layer(s) are relevant and whether this extends, complicates, \
or contradicts the existing framing.

### CONCEPT
A term, framework, method, or vocabulary item introduced that might belong \
in the Stack's lexicon. Include a proposed definition and note where it \
connects to existing Stack language. Log every named framework — do not \
assume prior familiarity.

### PROVOCATION
Something that directly challenges or complicates an existing Stack assumption \
or principle. Do not resolve it — surface it clearly so it can be sat with.

### OTHER
Anything important that doesn't fit the above. Suggest what category it might \
warrant and why it resists the existing taxonomy.

---

## Issue

Title: {title}
Subtitle: {subtitle}
Date: {date}

Content:
{content}

---

Return only the extracted material, organized by category. \
Omit any category that yields nothing worth extracting from this issue. \
Even for primarily journalistic issues, extract the data points, cases, and \
observations most relevant to governance, authority, and coordination.\
"""

# ---------------------------------------------------------------------------
# HTML stripping
# ---------------------------------------------------------------------------
class _HTMLStripper(HTMLParser):
    BLOCK_TAGS = {'p', 'div', 'br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'li', 'tr', 'blockquote', 'article', 'section', 'header', 'footer'}
    SKIP_TAGS  = {'script', 'style', 'noscript', 'iframe'}

    def __init__(self):
        super().__init__()
        self._parts   = []
        self._skip    = 0

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t in self.SKIP_TAGS:
            self._skip += 1
        elif t in self.BLOCK_TAGS:
            self._parts.append('\n')

    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.SKIP_TAGS:
            self._skip = max(0, self._skip - 1)
        elif t in self.BLOCK_TAGS:
            self._parts.append('\n')

    def handle_data(self, data):
        if self._skip == 0:
            self._parts.append(data)

    def get_text(self):
        raw = ''.join(self._parts)
        raw = re.sub(r'[ \t]+', ' ', raw)
        raw = re.sub(r'\n{3,}', '\n\n', raw)
        return raw.strip()


def strip_html(html: str) -> str:
    stripper = _HTMLStripper()
    stripper.feed(html)
    return stripper.get_text()

# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_posts() -> list[dict]:
    """Load posts.csv sorted oldest → newest. Undated posts sort to the end."""
    posts = []
    with open(POSTS_CSV, encoding='utf-8') as f:
        for row in csv.DictReader(f):
            posts.append(row)
    posts.sort(key=lambda r: r['post_date'] if r['post_date'] else '9999')
    return posts


def find_html(post_id: str) -> Path | None:
    """Locate the HTML file for a given post_id (numeric prefix match)."""
    numeric = post_id.split('.')[0]
    matches = list(POSTS_DIR.glob(f"{numeric}.*.html"))
    return matches[0] if matches else None


def numeric_id(post_id: str) -> str:
    return post_id.split('.')[0]

# ---------------------------------------------------------------------------
# Checkpoint
# ---------------------------------------------------------------------------
def load_checkpoint() -> set[str]:
    if CHECKPOINT_FILE.exists():
        data = json.loads(CHECKPOINT_FILE.read_text(encoding='utf-8'))
        return set(data.get('processed', []))
    return set()


def save_checkpoint(processed: set[str]):
    CHECKPOINT_FILE.write_text(
        json.dumps({'processed': sorted(processed)}, indent=2),
        encoding='utf-8'
    )

# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------
def extract(post: dict, client: OpenAI, model: str) -> tuple[str | None, str | None]:
    """
    Returns (extraction_markdown, error_message).
    One will always be None.
    """
    html_file = find_html(post['post_id'])
    if not html_file:
        return None, f"no HTML file for {post['post_id']}"

    html   = html_file.read_text(encoding='utf-8', errors='replace')
    text   = strip_html(html)

    if len(text) < 200:
        return None, "content too short after stripping"

    date     = post.get('post_date', '')[:10]
    title    = post.get('title', '(untitled)')
    subtitle = post.get('subtitle', '')

    prompt = EXTRACTION_PROMPT.format(
        title=title,
        subtitle=subtitle,
        date=date,
        content=text,
    )

    response = client.chat.completions.create(
        model=model,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
    )

    extraction = response.choices[0].message.content

    output = (
        f"---\n"
        f"title: {json.dumps(title)}\n"
        f"subtitle: {json.dumps(subtitle)}\n"
        f"date: {date}\n"
        f"source: {html_file.name}\n"
        f"---\n\n"
        f"# {title}\n\n"
        f"**{subtitle}**  \n"
        f"*{date}*\n\n"
        f"---\n\n"
        f"{extraction}\n"
    )
    return output, None

# ---------------------------------------------------------------------------
# Output filename
# ---------------------------------------------------------------------------
def output_path(post: dict) -> Path:
    date  = post.get('post_date', '')[:10]
    pid   = post['post_id']
    slug  = pid.split('.', 1)[1] if '.' in pid else pid
    slug  = re.sub(r'[^\w\-]', '-', slug)[:80]
    return EXTRACTIONS_DIR / f"{date}--{slug}.md"

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Extract Autonomy Stack material from newsletter archive')
    parser.add_argument('--limit', type=int, default=0,          help='Max issues to process this run (0 = all)')
    parser.add_argument('--reset', action='store_true',           help='Clear checkpoint and reprocess everything')
    parser.add_argument('--model', default=DEFAULT_MODEL,         help=f'OpenRouter model to use (default: {DEFAULT_MODEL})')
    args = parser.parse_args()

    api_key = os.environ.get('OPENROUTER_API_KEY')
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY environment variable is not set")

    EXTRACTIONS_DIR.mkdir(parents=True, exist_ok=True)

    client = OpenAI(
        api_key=api_key,
        base_url=OPENROUTER_BASE_URL,
    )
    posts  = load_posts()
    processed = set() if args.reset else load_checkpoint()

    remaining = [p for p in posts if numeric_id(p['post_id']) not in processed]
    to_process = remaining[:args.limit] if args.limit else remaining

    print(f"Total posts:      {len(posts)}")
    print(f"Already done:     {len(processed)}")
    print(f"This run:         {len(to_process)}")
    print(f"Model:            {args.model}")
    print()

    done = 0
    for i, post in enumerate(to_process):
        title = post.get('title', post['post_id'])
        print(f"[{i+1}/{len(to_process)}] {title[:70]}")

        extraction, err = extract(post, client, args.model)
        nid = numeric_id(post['post_id'])

        if err:
            print(f"         SKIP — {err}")
        else:
            path = output_path(post)
            path.write_text(extraction, encoding='utf-8')
            print(f"         -> {path.name}")
            done += 1

        processed.add(nid)
        save_checkpoint(processed)

        if i < len(to_process) - 1:
            time.sleep(DELAY)

    print(f"\nDone. {done} extractions written to {EXTRACTIONS_DIR}")


if __name__ == '__main__':
    main()
