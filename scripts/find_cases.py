#!/usr/bin/env python3
"""
find_cases.py

Scans the Metaviews extraction corpus (and optionally user-provided text)
to identify candidate situations for case study generation.

Each candidate is a concrete, real-world event or situation with visible
governance dynamics that would benefit from full Stack analysis.

Usage:
    python find_cases.py                         # Scan corpus for all candidates
    python find_cases.py --limit 10              # Top 10 candidates
    python find_cases.py --query "platform moderation failures"  # User-directed search
    python find_cases.py --sources path/to/text.md path2/   # User-provided sources
    python find_cases.py --reset                 # Regenerate candidates from scratch

Requires:
    OPENROUTER_API_KEY (and optionally OPENROUTER_MODEL) in .env
    pip install openai python-dotenv
"""

import os
import re
import json
import time
import argparse
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT        = Path(__file__).parent.parent
EXTRACTIONS_DIR  = REPO_ROOT / "sources" / "extractions"
CASES_DIR        = REPO_ROOT / "stack" / "cases"
CANDIDATES_FILE  = CASES_DIR / "candidates.md"
CHECKPOINT_FILE  = CASES_DIR / ".find-checkpoint.json"

# ---------------------------------------------------------------------------
# Model configuration
# ---------------------------------------------------------------------------
load_dotenv(REPO_ROOT / ".env")
DEFAULT_MODEL       = os.environ.get("OPENROUTER_MODEL", "google/gemini-flash-1.5")
DEFAULT_MODEL_FALLBACK = os.environ.get("OPENROUTER_MODEL_FALLBACK", "")
MAX_TOKENS          = 4096
DELAY               = 0.3
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
CORPUS_SAMPLE_CHARS = 40000  # how much corpus text to include as evidence

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are an analyst helping to identify case study candidates for the \
Autonomy Stack — a governance operating system that maps the conditions \
under which individual and collective agency is possible, sustainable, and \
contestable.

The Stack has six layers (dimensions of agency):
  1. Material Base — what material conditions make agency possible?
  2. Commons & Institutions — what structures sustain collective agency, and what makes them vulnerable to capture?
  3. Legibility & Metrics — who controls what can be seen and contested?
  4. Decision Systems & Authority — how is agency exercised in binding decisions, and can those decisions be contested, revised, or reversed?
  5. Knowledge & Intelligence — how does knowledge form, evolve, and remain open to revision?
  6. Human Capacity & Care — what relational conditions make sustained collective agency possible?

A good case study candidate is:
- A concrete, real-world situation (not a hypothetical or theoretical scenario)
- Rich in governance dynamics — authority, legitimacy, contestation, and coordination are visible
- Engages multiple Stack layers
- Has sufficient documentation or description in the source material to support analysis
- Either confirms existing patterns/predictions OR strains/contradicts them (both are useful)

You are working from a research corpus of newsletter issues about authority, \
governance, and coordination. Identify situations within this corpus that would \
make strong case studies.\
"""

CORPUS_SCAN_PROMPT = """\
Analyze the following excerpts from a research corpus and identify 8–12 concrete \
situations that would make strong case study candidates for the Autonomy Stack.

A case study candidate is a specific, real-world situation — not a general trend \
or abstract pattern. It should be a situation where governance dynamics (authority, \
legitimacy, contestation, coordination) are clearly visible and analyzable.

For each candidate, provide:
- **name** — A concise, descriptive title (under 8 words)
- **description** — One sentence describing the situation
- **timeframe** — When it occurred (if determinable from the text)
- **domain** — The context (e.g., disaster response, platform governance, municipal policy)
- **primary_layer** — Which Stack layer is the most natural entry point (L1–L6)
- **relevant_patterns** — 3–5 existing pattern names that seem relevant
- **evidence_summary** — What in the source material supports this as a candidate (2–3 sentences)
- **why_this_case** — What would this case illuminate that existing case studies don't? (1–2 sentences)

## Existing patterns for reference

Algorithmic Authority, Epistemic Warfare, Legitimacy Drift, Care vs. Coercion, \
Platform Capture, Obedience in Advance, Institutional Weaponization, \
Manufactured Ambiguity, Strategic Ambiguity, Commons Destruction, \
Material Base Sovereignty, Distributed Resistance, \
Proceduralism as Shield, Procedural Entombment, \
Collective Leadership Architecture, Semantic Capture, \
Care Infrastructure Failure, Temporal Capture, \
Internalized Policing, Hybrid War

## Existing case study (already done — don't re-propose)

- LA Wildfires Mutual Aid (January 2025, disaster response / mutual aid)

## Source material

The following are excerpts from 18 months of newsletter issues. \
They contain signals, events, analyses, and observations.

{corpus}

---

Return ONLY the candidates as a structured list. No preamble. No conclusion.\
"""

USER_QUERY_PROMPT = """\
Identify 5–8 concrete, real-world situations that would make strong case study \
candidates for the Autonomy Stack, based on the following user query and the \
supporting research corpus.

User query: {query}

A case study candidate is a specific situation — not a general trend. \
It should be a situation where governance dynamics (authority, legitimacy, \
contestability, coordination) are visible and analyzable.

For each candidate, provide:
- **name** — A concise, descriptive title (under 8 words)
- **description** — One sentence describing the situation
- **timeframe** — When it occurred (if determinable)
- **domain** — The context
- **primary_layer** — Which Stack layer is the most natural entry point (L1–L6)
- **relevant_patterns** — 3–5 existing pattern names
- **evidence_summary** — What supports this as a candidate (2–3 sentences)
- **why_this_case** — What would this case illuminate? (1–2 sentences)

## Existing patterns for reference

Algorithmic Authority, Epistemic Warfare, Legitimacy Drift, Care vs. Coercion, \
Platform Capture, Obedience in Advance, Institutional Weaponization, \
Manufactured Ambiguity, Strategic Ambiguity, Commons Destruction, \
Material Base Sovereignty, Distributed Resistance, \
Proceduralism as Shield, Procedural Entombment, \
Collective Leadership Architecture, Semantic Capture, \
Care Infrastructure Failure, Temporal Capture, \
Internalized Policing, Hybrid War

## Existing case study (already done — don't re-propose)

- LA Wildfires Mutual Aid (January 2025, disaster response / mutual aid)

{corpus_context}

---

Return ONLY the candidates as a structured list. No preamble. No conclusion.\
"""

# ---------------------------------------------------------------------------
# Corpus loading
# ---------------------------------------------------------------------------
def load_corpus_excerpts(limit_chars=CORPUS_SAMPLE_CHARS):
    """
    Load a representative sample from the extraction corpus.
    Prioritizes STACK MATERIAL and PATTERN CANDIDATE sections
    since those are most likely to contain concrete situations.
    """
    files = sorted(
        [f for f in EXTRACTIONS_DIR.glob("*.md") if not f.name.startswith('.')],
        key=lambda f: f.name
    )

    excerpts = []
    total = 0

    for path in files:
        text = path.read_text(encoding='utf-8', errors='replace')

        # Extract date and title from frontmatter
        date_match = re.search(r'^date:\s*(\S+)', text, re.MULTILINE)
        title_match = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
        date = date_match.group(1) if date_match else path.stem[:10]
        title = title_match.group(1) if title_match else path.stem

        # Extract relevant sections
        sections = re.split(r'\n### ', text)
        for section in sections:
            if any(kw in section[:60].upper() for kw in ['STACK MATERIAL', 'PATTERN CANDIDATE', 'SIGNAL', 'PROVOCATION']):
                # Get first 500 chars of each relevant section
                excerpt = section[:500]
                excerpts.append(f"[{date}] {title}\n{excerpt}")
                total += len(excerpt)

        if total >= limit_chars:
            break

    combined = "\n\n---\n\n".join(excerpts)
    if len(combined) > limit_chars:
        combined = combined[:limit_chars] + "\n\n[... additional corpus material ...]"

    return combined, len(files)


def load_user_sources(source_paths: list[str]) -> str:
    """Load text from user-provided source files or directories."""
    parts = []
    for sp in source_paths:
        p = Path(sp)
        if p.is_file() and p.suffix in ('.md', '.txt', '.html'):
            content = p.read_text(encoding='utf-8', errors='replace')
            parts.append(f"## Source: {p.name}\n\n{content[:5000]}")
        elif p.is_dir():
            for f in sorted(p.glob("*.md"))[:10]:
                content = f.read_text(encoding='utf-8', errors='replace')
                parts.append(f"## Source: {f.name}\n\n{content[:3000]}")
    return "\n\n".join(parts)


def load_existing_cases() -> set[str]:
    """Get names of already-written case studies to avoid duplication."""
    if not CASES_DIR.exists():
        return set()
    cases = set()
    for f in CASES_DIR.glob("*.md"):
        if f.name == "candidates.md":
            continue
        text = f.read_text(encoding='utf-8', errors='replace')
        # Try to get title from first line
        first_line = text.strip().split('\n')[0] if text.strip() else ''
        cases.add(first_line.lstrip('# ').strip())
    return cases


# ---------------------------------------------------------------------------
# Candidate generation
# ---------------------------------------------------------------------------
def find_candidates(client, model, query=None, user_sources=None):
    """Run the LLM to identify case study candidates."""
    corpus, file_count = load_corpus_excerpts()

    if user_sources:
        source_text = load_user_sources(user_sources)
        corpus_context = f"\n\n## Additional source material provided by user\n\n{source_text[:10000]}\n\n## Corpus excerpts\n\n{corpus}"
    else:
        corpus_context = f"\n\n## Corpus excerpts\n\n{corpus}"

    if query:
        prompt = USER_QUERY_PROMPT.format(
            query=query,
            corpus_context=corpus_context,
        )
    else:
        prompt = CORPUS_SCAN_PROMPT.format(corpus=corpus)

    response = client.chat.completions.create(
        model=model,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
    )

    return response.choices[0].message.content


def parse_candidates(raw_text):
    """
    Parse the LLM's output into structured candidate dicts.
    Handles three common formats:

    Format A (key-value, lowercase):
        **name** — Title
        **description** — One sentence

    Format B (numbered list):
        1. **Name**
        - **description** — One sentence

    Format C (bold heading, dashed fields):
        **Name**
        - **Description:** One sentence
    """
    FIELD_KEYS = ['description', 'timeframe', 'domain', 'primary_layer',
                  'relevant_patterns', 'evidence_summary', 'why_this_case']

    candidates = []
    current = {}
    in_fields = False  # tracks if we're inside a candidate's field block

    for line in raw_text.split('\n'):
        stripped = line.strip()
        if not stripped:
            if current.get('name'):
                candidates.append(current)
                current = {}
                in_fields = False
            continue

        # Format A: **name** — Title  or  - **name:** Title
        name_match = re.match(r'^(?:-\s+)?\*\*name\*\*\s*[—:–-]\s*(.+)', stripped, re.IGNORECASE)
        if name_match:
            if current.get('name'):
                candidates.append(current)
            current = {'name': name_match.group(1).strip().strip('*# ')}
            in_fields = True
            continue

        # Format B: numbered heading
        num_match = re.match(r'^\d+\.\s*\*\*(.+?)\*\*', stripped)
        if num_match:
            if current.get('name'):
                candidates.append(current)
            current = {'name': num_match.group(1).strip()}
            in_fields = True
            continue

        # Format C: bare **Name** — a line that is ONLY bold text (no field label)
        # Must be at start of a block (not in_fields), and followed by field lines
        bare_bold = re.match(r'^\*\*(.+?)\*\*\s*$', stripped)
        if bare_bold and not in_fields:
            name_text = bare_bold.group(1).strip()
            # Skip if it looks like a field key (short word like "name")
            if name_text.lower() not in ('name',) and len(name_text) > 3:
                if current.get('name'):
                    candidates.append(current)
                current = {'name': name_text}
                in_fields = True
                continue

        # Field lines: "**field** — value" or "- **field** — value" or "- **Field:** value"
        if in_fields:
            for field in FIELD_KEYS:
                # Replace underscores with [_\s]? to match "Primary Layer" or "primary_layer"
                field_pat = re.escape(field).replace('_', '[_\\s]?')
                pat = rf'(?:-\s+)?\*\*{field_pat}[*:]*\*\s*[—:–-]?\s*(.+)'
                m = re.match(pat, stripped, re.IGNORECASE)
                if m:
                    current[field] = m.group(1).strip().strip('"')
                    break

    if current.get('name'):
        candidates.append(current)

    # Deduplicate by name
    seen = set()
    unique = []
    for cand in candidates:
        key = cand['name'].lower()
        if key not in seen:
            seen.add(key)
            unique.append(cand)

    return unique


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def write_candidates_file(candidates):
    """Write candidates to the candidates.md file with review markup."""
    existing = load_existing_cases()

    header = """# Case Study Candidates

*Generated by find_cases.py. Review candidates below and mark them as approved \
by adding `[APPROVED]` after the name. Then run `write_cases.py` to generate \
the full case studies.*

*To approve: change `## [Candidate Name]` to `## [Candidate Name] [APPROVED]`*

---

"""
    parts = [header]

    for i, c in enumerate(candidates, 1):
        already_done = c['name'] in existing
        status = "⚠️ Already exists" if already_done else "⬜ Pending review"

        parts.append(f"## {c['name']}  \n*{status}*\n")
        parts.append(f"**Description:** {c.get('description', 'N/A')}")
        parts.append(f"**Timeframe:** {c.get('timeframe', 'N/A')}")
        parts.append(f"**Domain:** {c.get('domain', 'N/A')}")
        parts.append(f"**Primary layer:** {c.get('primary_layer', 'N/A')}")
        parts.append(f"**Relevant patterns:** {c.get('relevant_patterns', 'N/A')}")
        parts.append(f"**Evidence:** {c.get('evidence_summary', 'N/A')}")
        parts.append(f"**Why this case:** {c.get('why_this_case', 'N/A')}")
        parts.append("")

        if already_done:
            parts.append("*A case study with this name already exists. Skipping or rename needed.*")
            parts.append("")

    content = "\n".join(parts)
    CANDIDATES_FILE.write_text(content, encoding='utf-8')
    return content


def print_candidates(candidates):
    """Print a concise summary to console."""
    existing = load_existing_cases()

    print(f"{'='*60}")
    print(f"CASE STUDY CANDIDATES")
    print(f"{'='*60}")
    print()

    for i, c in enumerate(candidates, 1):
        already = c['name'] in existing
        marker = "⚠️ EXISTS" if already else ""
        print(f"  {i}. {c['name']} {marker}")
        print(f"     {c.get('description', 'N/A')}")
        print(f"     Layer: {c.get('primary_layer', '?')} | Domain: {c.get('domain', '?')}")
        if c.get('why_this_case'):
            print(f"     → {c['why_this_case']}")
        print()

    print(f"{'='*60}")
    new_count = sum(1 for c in candidates if c['name'] not in existing)
    print(f"Total: {len(candidates)} candidates  |  New: {new_count}  |  Already exists: {len(candidates) - new_count}")
    print(f"{'='*60}")
    print()
    print(f"Full details written to: {CANDIDATES_FILE.relative_to(REPO_ROOT)}")
    print("To approve: mark with [APPROVED] in the file, then run write_cases.py")


# ---------------------------------------------------------------------------
# Checkpoint
# ---------------------------------------------------------------------------
def load_checkpoint() -> str:
    """Return the last query/checkpoint state to avoid re-scanning."""
    if CHECKPOINT_FILE.exists():
        data = json.loads(CHECKPOINT_FILE.read_text(encoding='utf-8'))
        return data.get('last_query', '')
    return ''


def save_checkpoint(query):
    CHECKPOINT_FILE.write_text(
        json.dumps({'last_query': query}, indent=2),
        encoding='utf-8'
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Find case study candidates from the Autonomy Stack corpus")
    parser.add_argument("--limit",       type=int, default=0,   help="Max candidates to return (0 = all)")
    parser.add_argument("--query",       type=str, default="",  help="User-directed search query for candidates")
    parser.add_argument("--sources",     type=str, nargs='+',   help="User-provided source files/directories")
    parser.add_argument("--reset",       action="store_true",   help="Regenerate from scratch")
    parser.add_argument("--model",       default=DEFAULT_MODEL, help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not set")

    CASES_DIR.mkdir(parents=True, exist_ok=True)

    client = OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)

    query_key = args.query or ("__corpus_scan__" + (','.join(args.sources) if args.sources else "__default__"))
    if args.reset:
        save_checkpoint("")

    print(f"Model:          {args.model}")
    print(f"Mode:           {'user query' if args.query else 'corpus scan'}")
    if args.query:
        print(f"Query:          {args.query}")
    if args.sources:
        print(f"User sources:   {', '.join(args.sources)}")
    print()

    # Check if we already have candidates from this query
    existing_text = ''
    if CANDIDATES_FILE.exists() and load_checkpoint() == query_key:
        existing_text = CANDIDATES_FILE.read_text(encoding='utf-8')
        print(f"Using cached candidates from: {CANDIDATES_FILE.relative_to(REPO_ROOT)}")
        print("Use --reset to regenerate.\n")

    if not existing_text:
        print("Scanning for candidates...")
        raw = find_candidates(client, args.model, query=args.query or None, user_sources=args.sources)
        candidates = parse_candidates(raw)

        if not candidates:
            print("No candidates identified. Try --query with a specific topic.")
            print(f"Raw model output:\n{raw}")
            return

        if args.limit:
            candidates = candidates[:args.limit]

        write_candidates_file(candidates)
        save_checkpoint(query_key)
    else:
        # Re-parse existing file
        candidates = parse_candidates(existing_text)

    print_candidates(candidates)


if __name__ == "__main__":
    main()
