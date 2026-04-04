#!/usr/bin/env python3
"""
write_cases.py

Generates full case study documents for the Autonomy Stack from approved
candidates. Each case study applies the six-layer framework, matches
patterns, identifies active provocations, and surfaces gaps.

Candidates are approved in stack/cases/candidates.md by marking them
with [APPROVED]. Then this tool generates the full analysis.

Usage:
    python write_cases.py                              # Write all approved cases
    python write_cases.py --case "Platform X moderation crisis"  # One specific case
    python write_cases.py --cases "Case A" "Case B"    # Multiple specific cases
    python write_cases.py --limit 2                    # Next 2 approved only
    python write_cases.py --reset                      # Regenerate all approved
    python write_cases.py --model <openrouter-id>      # Override model

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
CHECKPOINT_FILE  = CASES_DIR / ".write-checkpoint.json"

# ---------------------------------------------------------------------------
# Model configuration
# ---------------------------------------------------------------------------
load_dotenv(REPO_ROOT / ".env")
DEFAULT_MODEL       = os.environ.get("OPENROUTER_MODEL", "google/gemini-flash-1.5")
MAX_TOKENS          = 8192
DELAY               = 0.5
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MAX_EVIDENCE_CHARS  = 30000

# ---------------------------------------------------------------------------
# Reference documents
# ---------------------------------------------------------------------------
def load_layer_descriptions():
    return """\
1. Material Base — What material conditions make agency possible?
   Food, energy, housing, logistics, environmental systems. Control over material
   inputs is a direct lever of power and a terrain of contest.

2. Commons & Institutions — What structures sustain collective agency, and what
   makes them vulnerable to capture?
   Cooperatives, unions, public agencies, mutual aid networks, standards bodies.
   Shared responsibility vs. evaporated obligation.

3. Legibility & Metrics — Who controls what can be seen and contested?
   What gets measured shapes what gets defended. Technical legibility (seeing
   the output) vs. epistemic legibility (understanding and challenging it).

4. Decision Systems & Authority — How is agency exercised in binding decisions
   and can those decisions be contested, revised, or reversed?
   Law, algorithms, norms, procedure. Authority without legitimate process is
   force wearing governance's clothing.

5. Knowledge & Intelligence — How does knowledge form, evolve, and remain open
   to revision?
   Research, media, shared situational awareness. Epistemic warfare degrades
   the conditions under which truth and falsehood can be distinguished together.

6. Human Capacity & Care — What relational conditions make sustained collective
   agency possible?
   Care networks, trust, capacity for engagement. Burnout and precarity
   eliminate the relational substrate on which everything else depends.\
"""


def load_principles():
    return """\
1. Authority must be contestable
2. Power without legibility is unacceptable
3. Disagreement is a design condition
4. Resilience takes priority over elegance
5. Legibility takes priority over expertise
6. Opaque mechanisms require extraordinary justification
7. Failure is informative
8. Nothing is final\
"""


def load_patterns_index():
    """Load brief pattern descriptions for reference in the generation prompt."""
    patterns_dir = REPO_ROOT / "patterns"
    patterns = []
    for f in sorted(patterns_dir.glob("*.md")):
        if f.name.lower() == "readme.md":
            continue
        text = f.read_text(encoding='utf-8', errors='replace')
        # Extract name from first heading
        name_match = re.search(r'# Pattern:\s*(.+)', text)
        if not name_match:
            name_match = re.search(r'#\s*(.+)', text)
        name = name_match.group(1).strip() if name_match else f.stem

        # Extract summary
        summary_match = re.search(r'## Summary\n+(.+?)(?:\n\n|\n##)', text, re.DOTALL)
        summary = summary_match.group(1).strip() if summary_match else ""

        patterns.append(f"- {name}: {summary}")

    return "\n".join(patterns)


def load_provocations_index():
    """Load the eight provocations as brief names."""
    return """\
P1: Authority Without Legibility — Technical opacity masking power
P2: Care-Based Authority vs. Contestability — The moralization trap
P3: The Knowledge Authority Paradox — Expertise forbidden yet required
P4: The Resilience-Speed Trade-Off — Distributed systems cannot move fast enough in crises
P5: Language as Contested Medium — Semantic collapse of governance
P6: Private Authority Beyond the State — Sovereignty without territory
P7: Material Base as Authority Determinant — You cannot govern without food
P8: The Care-Capacity Inversion — The system demands care it cannot provide\
"""


# ---------------------------------------------------------------------------
# Evidence gathering
# ---------------------------------------------------------------------------
def gather_evidence(case_name, case_description):
    """
    Search extractions for material relevant to this case.
    Uses the case name and key terms from the description.
    """
    # Build search terms from the case metadata
    search_terms = []
    search_terms.append(case_name.lower())
    # Add meaningful words from the description
    desc_words = re.findall(r'\b[a-zA-Z]{4,}\b', case_description)
    search_terms.extend([w.lower() for w in desc_words if w.lower() not in
        ('the', 'and', 'for', 'from', 'with', 'that', 'this', 'what', 'when',
         'where', 'which', 'who', 'their', 'there', 'these', 'those', 'under',
         'about', 'after', 'before', 'between', 'through', 'during', 'without',
         'each', 'some', 'such', 'than', 'then', 'been', 'being', 'have',
         'has', 'had', 'does', 'did', 'will', 'would', 'could', 'should',
         'may', 'might', 'must', 'can', 'into', 'more', 'most', 'other',
         'only', 'very', 'just', 'over', 'also')])

    evidence_parts = []
    files = sorted(
        [f for f in EXTRACTIONS_DIR.glob("*.md") if not f.name.startswith('.')],
        key=lambda f: f.name
    )

    for path in files:
        text = path.read_text(encoding='utf-8', errors='replace')
        text_lower = text.lower()

        if not any(term in text_lower for term in search_terms if len(term) >= 4):
            continue

        # Extract all non-frontmatter content
        content = re.sub(r'^---.*?---\n\n', '', text, flags=re.DOTALL)
        date_match = re.search(r'^date:\s*(\S+)', text, re.MULTILINE)
        title_match = re.search(r'^title:\s*"([^"]+)"', text, re.MULTILINE)
        date = date_match.group(1) if date_match else path.stem[:10]
        title = title_match.group(1) if title_match else path.stem

        # Get relevant sections
        sections = re.split(r'\n### ', content)
        relevant = []
        for section in sections:
            sec_lower = section.lower()
            if any(term in sec_lower for term in search_terms if len(term) >= 4):
                relevant.append(f"### {section.strip()}")

        if relevant:
            evidence_parts.append(
                f"[{date}] {title}\n" + "\n".join(relevant[:3])
            )

    combined = "\n\n---\n\n".join(evidence_parts)

    if len(combined) > MAX_EVIDENCE_CHARS:
        combined = combined[:MAX_EVIDENCE_CHARS] + "\n\n[... evidence truncated at budget limit ...]"

    return combined if combined else "(No direct corpus matches — synthesize from general knowledge of this type of situation.)"


# ---------------------------------------------------------------------------
# Generation prompt
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are writing a case study for the Autonomy Stack — a governance operating \
system that maps the conditions under which individual and collective agency \
is possible, sustainable, and contestable.

Case studies apply the Stack's six-layer framework to a specific real-world \
situation. They are analytical, not prescriptive. They do not argue for a \
specific intervention or outcome. Their function is to make the Stack's \
diagnostic capacity visible by applying it to a concrete situation.

The case study must follow the template structure precisely:
- Situation (factual, concrete, no Stack vocabulary yet)
- Layer Analysis (all six layers, weighted by relevance)
- Patterns Present (name, how it appeared, confirms/strains/extends)
- Provocations Alive (which of the eight provocations are active)
- What This Case Illuminates (what the Stack handles well and struggles with)
- What Remains Open (questions the Stack cannot currently answer)

The voice is analytic but not clinical — it names things directly without \
performing certainty. Use precise language. Every sentence should earn its place.\
"""

CASE_STUDY_PROMPT = """\
Write a full case study for the Autonomy Stack based on the situation \
described below and the evidence from the research corpus.

## Case metadata

**Title:** {case_name}
**Description:** {case_description}
**Timeframe:** {timeframe}
**Domain:** {domain}
**Primary layer:** {primary_layer}

## Stack reference

### Layer descriptions

{layer_descriptions}

### Principles

{principles}

### Pattern library (for pattern matching)

{patterns_index}

### Provocations

{provocations_index}

## Evidence from the research corpus

{evidence}

## Additional context

{additional_context}

---

Write the case study using the template structure below. Be concrete and \
specific. Ground the analysis in the situation and evidence provided. When \
matching patterns, indicate whether this case confirms, strains, or extends \
each pattern — don't just confirm everything. Be honest about where the Stack \
struggles.

## Template

### [Case Title]

*One sentence describing the situation.*

**Date / timeframe:** {timeframe}
**Domain / context:** {domain}
**Primary Stack entry point:** {primary_layer}

---

#### Situation

2–4 paragraphs describing what happened. Factual and concrete. No Stack \
vocabulary yet.

---

#### Layer Analysis

**L1 — Material Base:** What material conditions shaped this situation? \
Who controlled what?

**L2 — Commons & Institutions:** What governance structures were present? \
How did they function or fail?

**L3 — Legibility & Metrics:** What could be seen? By whom? What was \
invisible, contested, or misrepresented?

**L4 — Decision Systems & Authority:** How were binding decisions made? \
Were they contestable? What was irreversible?

**L5 — Knowledge & Intelligence:** How did collective understanding form? \
Was it reliable, fragmented, or adversarially disrupted?

**L6 — Human Capacity & Care:** What relational conditions were present? \
What sustained or depleted them?

---

#### Patterns Present

**[Pattern Name]** — How it appeared in this situation. \
*Confirms / Strains / Extends* the pattern description. \
(Strain or extension notes if applicable.)

---

#### Provocations Alive in This Situation

Name each active provocation and note specifically how it manifests.

---

#### What This Case Illuminates

What does this case reveal that the Stack's current architecture handles well? \
What does it reveal that the architecture struggles with?

---

#### What Remains Open

What questions does this case raise that the Stack cannot currently answer? \
What would the Stack need to develop in order to address them?

---

Write only the case study content. No preamble, no meta-commentary.\
"""


# ---------------------------------------------------------------------------
# Candidate parsing
# ---------------------------------------------------------------------------
def load_approved_candidates():
    """Parse candidates.md for [APPROVED] entries."""
    if not CANDIDATES_FILE.exists():
        return []

    text = CANDIDATES_FILE.read_text(encoding='utf-8', errors='replace')

    # Split by ## headings
    sections = re.split(r'\n## ', text)
    approved = []

    for section in sections:
        if '[APPROVED]' not in section:
            continue

        # Parse the section
        lines = section.strip().split('\n')
        heading = lines[0]
        name = heading.replace('[APPROVED]', '').strip().rstrip(' \n')

        candidate = {
            'name': name,
            'description': '',
            'timeframe': '',
            'domain': '',
            'primary_layer': '',
            'relevant_patterns': '',
            'evidence_summary': '',
            'why_this_case': '',
        }

        for line in lines[1:]:
            line = line.strip()
            if line.startswith('**Description:**'):
                candidate['description'] = line.replace('**Description:**', '').strip()
            elif line.startswith('**Timeframe:**'):
                candidate['timeframe'] = line.replace('**Timeframe:**', '').strip()
            elif line.startswith('**Domain:**'):
                candidate['domain'] = line.replace('**Domain:**', '').strip()
            elif line.startswith('**Primary layer:**'):
                candidate['primary_layer'] = line.replace('**Primary layer:**', '').strip()
            elif line.startswith('**Relevant patterns:**'):
                candidate['relevant_patterns'] = line.replace('**Relevant patterns:**', '').strip()
            elif line.startswith('**Evidence:**'):
                candidate['evidence_summary'] = line.replace('**Evidence:**', '').strip()
            elif line.startswith('**Why this case:**'):
                candidate['why_this_case'] = line.replace('**Why this case:**', '').strip()

        if candidate['name']:
            approved.append(candidate)

    return approved


def slugify(name):
    """Convert a case name to a filename-safe slug."""
    s = name.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    s = re.sub(r'-{2,}', '-', s)
    return s[:80].strip('-')


# ---------------------------------------------------------------------------
# Checkpoint
# ---------------------------------------------------------------------------
def load_checkpoint() -> set[str]:
    if CHECKPOINT_FILE.exists():
        data = json.loads(CHECKPOINT_FILE.read_text(encoding='utf-8'))
        return set(data.get("written", []))
    return set()


def save_checkpoint(written: set[str]):
    CHECKPOINT_FILE.write_text(
        json.dumps({"written": sorted(written)}, indent=2),
        encoding='utf-8'
    )


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------
def generate_case_study(candidate, client, model):
    """Returns (content, error)."""
    evidence = gather_evidence(candidate['name'], candidate['description'])

    layers = load_layer_descriptions()
    principles = load_principles()
    patterns = load_patterns_index()
    provos = load_provocations_index()

    prompt = CASE_STUDY_PROMPT.format(
        case_name=candidate['name'],
        case_description=candidate['description'],
        timeframe=candidate.get('timeframe', 'Not specified'),
        domain=candidate.get('domain', 'Not specified'),
        primary_layer=candidate.get('primary_layer', 'Not specified'),
        layer_descriptions=layers,
        principles=principles,
        patterns_index=patterns,
        provocations_index=provos,
        evidence=evidence,
        additional_context=candidate.get('why_this_case', ''),
    )

    response = client.chat.completions.create(
        model=model,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
    )

    # Clean up: remove any markdown code fences the model might add
    content = response.choices[0].message.content
    content = re.sub(r'^```\s*markdown?\n?', '', content)
    content = re.sub(r'\n?```\s*$', '', content)

    # Add the title wrapper
    output = f"# Case Study: {candidate['name']}\n\n*{candidate['description']}*\n\n{content}\n"

    return output, None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate Autonomy Stack case studies from approved candidates")
    parser.add_argument("--case",   type=str, default="",    help="Generate one specific case by name")
    parser.add_argument("--cases",  type=str, nargs='+',     help="Generate multiple specific cases by name")
    parser.add_argument("--limit",  type=int, default=0,     help="Max cases to generate this run (0 = all approved)")
    parser.add_argument("--reset",  action="store_true",     help="Clear checkpoint and regenerate all approved")
    parser.add_argument("--model",  default=DEFAULT_MODEL,   help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not set")

    CASES_DIR.mkdir(parents=True, exist_ok=True)

    client    = OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)
    written   = set() if args.reset else load_checkpoint()
    approved  = load_approved_candidates()

    if not approved:
        print("No approved candidates found.")
        print(f"Edit {CANDIDATES_FILE.relative_to(REPO_ROOT)} and mark candidates with [APPROVED].")
        return

    # Filter to specific cases if requested
    if args.case:
        candidates = [c for c in approved if c['name'].lower() == args.case.lower()]
        if not candidates:
            raise SystemExit(f"Approved case not found: {args.case}")
    elif args.cases:
        candidates = [c for c in approved if c['name'].lower() in [x.lower() for x in args.cases]]
        if not candidates:
            raise SystemExit(f"None of the specified cases found in approved list.")
    else:
        # Skip already written
        candidates = [c for c in approved if c['name'] not in written]
        if args.limit:
            candidates = candidates[:args.limit]

    print(f"Approved candidates: {len(approved)}")
    print(f"Already written:     {len(written)}")
    print(f"This run:            {len(candidates)}")
    print(f"Model:               {args.model}")
    print()

    done = 0
    for i, candidate in enumerate(candidates):
        print(f"[{i+1}/{len(candidates)}] {candidate['name']}")

        content, err = generate_case_study(candidate, client, args.model)

        if err:
            print(f"         SKIP -- {err}")
        else:
            slug = slugify(candidate['name'])
            out_path = CASES_DIR / f"{slug}.md"
            out_path.write_text(content, encoding='utf-8')
            print(f"         -> {out_path.relative_to(CASES_DIR)}")
            done += 1

        written.add(candidate['name'])
        save_checkpoint(written)

        if i < len(candidates) - 1:
            time.sleep(DELAY)

    print(f"\nDone. {done} case studies written to {CASES_DIR}")


if __name__ == "__main__":
    main()
