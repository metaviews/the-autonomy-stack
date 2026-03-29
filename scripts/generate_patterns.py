#!/usr/bin/env python3
"""
generate_patterns.py

Synthesizes patterns for the Autonomy Stack from the extraction corpus.
Each pattern is grounded in evidence drawn from the Metaviews newsletter extractions.

Usage:
    python generate_patterns.py                             # Generate all ungenerated patterns
    python generate_patterns.py --limit 3                  # Generate next 3 only
    python generate_patterns.py --pattern "Epistemic Warfare"  # One specific pattern
    python generate_patterns.py --reset                    # Clear checkpoint and regenerate all
    python generate_patterns.py --model <openrouter-id>    # Override model

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
PATTERNS_DIR     = REPO_ROOT / "patterns"
CHECKPOINT_FILE  = PATTERNS_DIR / ".checkpoint.json"

# ---------------------------------------------------------------------------
# Model configuration
# ---------------------------------------------------------------------------
load_dotenv(REPO_ROOT / ".env")
DEFAULT_MODEL       = os.environ.get("OPENROUTER_MODEL", "google/gemini-flash-1.5")
MAX_TOKENS          = 2048
DELAY               = 0.5
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MAX_EVIDENCE_CHARS  = 24000  # cap evidence per pattern to manage token budget

# ---------------------------------------------------------------------------
# Pattern definitions
# ---------------------------------------------------------------------------
PATTERNS = [
    {
        "name": "Algorithmic Authority",
        "filename": "algorithmic-authority.md",
        "description": "Automated systems accumulate decision-making power by mimicking institutional authority without inheriting its accountability structures.",
        "search_terms": ["algorithmic", "algorithm", "automated decision", "algorithmic authority"],
        "related": ["Platform Capture", "Legitimacy Drift", "Manufactured Ambiguity"],
        "tier": 1,
    },
    {
        "name": "Epistemic Warfare",
        "filename": "epistemic-warfare.md",
        "description": "The deliberate degradation of shared factual baselines and knowledge-forming conditions as a governance attack.",
        "search_terms": ["epistemic", "factual baseline", "disinformation", "epistemic warfare", "linguistic colonization", "information warfare", "shared reality"],
        "related": ["Algorithmic Authority", "Manufactured Ambiguity", "Hybrid War"],
        "tier": 1,
    },
    {
        "name": "Legitimacy Drift",
        "filename": "legitimacy-drift.md",
        "description": "Authority gradually decouples from legitimacy through accumulated small departures from accountable process, until force replaces consent as the operative mechanism.",
        "search_terms": ["legitimacy drift", "legitimacy", "authority decoupled", "authority without legitimacy", "decoupled from legitimacy"],
        "related": ["Hybrid War", "Institutional Weaponization", "Temporal Capture"],
        "tier": 1,
    },
    {
        "name": "Care vs. Coercion",
        "filename": "care-vs-coercion.md",
        "description": "The foundational choice between care and coercion as organizing modes of relation — and the ways coercion disguises itself as care.",
        "search_terms": ["care", "coercion", "transactional", "care vs coercion", "relational", "caretaker"],
        "related": ["Internalized Policing", "Commons Destruction", "Distributed Resistance"],
        "tier": 2,
    },
    {
        "name": "Platform Capture",
        "filename": "platform-capture.md",
        "description": "Infrastructure platforms accumulate governance functions without acquiring governance accountability.",
        "search_terms": ["platform capture", "platform", "infrastructure", "tech platform", "social media platform"],
        "related": ["Algorithmic Authority", "Institutional Weaponization", "Legitimacy Drift"],
        "tier": 2,
    },
    {
        "name": "Obedience in Advance",
        "filename": "obedience-in-advance.md",
        "description": "People preemptively comply with anticipated demands before any explicit coercion occurs, internalizing and enforcing limits on their own agency.",
        "search_terms": ["obedience in advance", "pre-emptive", "self-censorship", "anticipatory compliance", "chilling effect", "preemptive compliance"],
        "related": ["Internalized Policing", "Hybrid War", "Manufactured Ambiguity"],
        "tier": 2,
    },
    {
        "name": "Institutional Weaponization",
        "filename": "institutional-weaponization.md",
        "description": "Public institutions are repurposed from neutral arbitration into offensive capabilities deployed against designated opponents.",
        "search_terms": ["institutional weaponization", "weaponization", "civil service", "personal loyalty", "institutions as weapons", "weaponized"],
        "related": ["Legitimacy Drift", "Platform Capture", "Hybrid War"],
        "tier": 2,
    },
    {
        "name": "Manufactured Ambiguity",
        "filename": "manufactured-ambiguity.md",
        "description": "Ambiguity is deliberately produced to prevent coordinated response, dissolve accountability, and exhaust those seeking clarity.",
        "search_terms": ["manufactured ambiguity", "deliberate ambiguity", "manufactured confusion", "strategic confusion", "plausible deniability"],
        "related": ["Hybrid War", "Strategic Ambiguity", "Legitimacy Drift"],
        "tier": 3,
    },
    {
        "name": "Strategic Ambiguity",
        "filename": "strategic-ambiguity.md",
        "description": "Deliberate maintenance of unclear intent to preserve optionality, prevent commitment, and force opponents to overextend on incomplete information.",
        "search_terms": ["strategic ambiguity", "strategic uncertainty", "unclear intent", "deliberate vagueness"],
        "related": ["Manufactured Ambiguity", "Hybrid War", "Obedience in Advance"],
        "tier": 3,
    },
    {
        "name": "Commons Destruction",
        "filename": "commons-destruction.md",
        "description": "Shared resources, institutions, and relational infrastructure are systematically enclosed, privatized, or degraded to concentrate agency.",
        "search_terms": ["commons destruction", "commons", "enclosure", "privatization", "commons erosion", "shared resources"],
        "related": ["Platform Capture", "Institutional Weaponization", "Material Base Sovereignty"],
        "tier": 3,
    },
    {
        "name": "Material Base Sovereignty",
        "filename": "material-base-sovereignty.md",
        "description": "Control over food, energy, and logistics functions as governance — whoever controls the material base shapes the conditions for all other agency.",
        "search_terms": ["material base", "food sovereignty", "food power", "material sovereignty", "supply chain", "food system"],
        "related": ["Commons Destruction", "Platform Capture", "Legitimacy Drift"],
        "tier": 3,
    },
    {
        "name": "Distributed Resistance",
        "filename": "distributed-resistance.md",
        "description": "Resilient opposition to concentrated power through decentralized, mutual, and peer-based structures that cannot be decapitated.",
        "search_terms": ["mutual aid", "distributed resistance", "decentralized", "collective action", "solidarity", "peer-to-peer"],
        "related": ["Care vs. Coercion", "Commons Destruction", "Internalized Policing"],
        "tier": 3,
    },
]

# ---------------------------------------------------------------------------
# Reference examples (used in synthesis prompt)
# ---------------------------------------------------------------------------
PATTERN_EXAMPLES = """\
## Example pattern 1

# Pattern: Temporal Capture

## Summary
The future is endlessly promised while present conditions deteriorate, delaying accountability and suppressing action.

## Core Dynamic
Attention is redirected from present failure to speculative futures, keeping authority insulated from evaluation.

## Signals
- Grand future-oriented narratives amid worsening current conditions
- Calls for patience framed as responsibility
- Permanent pilots, transitions, or "early stages"
- Criticism dismissed as premature or anti-progress

## What It Targets
Accountability, urgency, and collective capacity to act in the present.

## Why It Works
People are culturally trained to tolerate present harm in exchange for promised future benefit.

## Common Misreadings
- "This is just long-term planning"
- "Change takes time"
- "You don't understand the roadmap"

## Related Patterns
- Legitimacy Drift
- Algorithmic Authority
- Proceduralism as Shield

---

## Example pattern 2

# Pattern: Internalized Policing

## Summary
Social norms and enforcement are crowdsourced to peers, reducing the need for overt institutional coercion.

## Core Dynamic
Power operates by encouraging people to monitor, correct, and punish one another.

## Signals
- Public shaming replacing formal enforcement
- Rules enforced unevenly through social pressure
- Fear of reputational damage outweighing legal risk
- Communities fragmenting over norm compliance

## What It Targets
Solidarity, dissent, and the ability to coordinate resistance.

## Why It Works
It converts social belonging into a mechanism of control and distributes enforcement costs.

## Common Misreadings
- "This is just accountability"
- "People are choosing to enforce norms"
- "There's no coercion involved"

## Related Patterns
- Obedience in Advance
- Platform Capture
- Manufactured Ambiguity\
"""

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = """\
You are writing patterns for the Autonomy Stack — a governance operating system \
that maps the conditions under which individual and collective agency is possible, \
sustainable, and contestable.

Patterns describe recurring governance dynamics that have been observed across \
contexts. They are not rules or prescriptions. They are recognitions — distilled \
from practice and stress-tested in the open.

The Stack's core principles constrain all pattern work:
- Authority must be contestable
- Power without legibility is unacceptable
- Disagreement is a design condition
- Resilience over elegance
- Legibility over expertise
- Failure is informative
- Nothing is final

The Stack is organized into six layers (dimensions of agency):
  1. Material Base — what material conditions make agency possible?
  2. Commons & Institutions — what structures sustain collective agency, and what makes them vulnerable to capture?
  3. Legibility & Metrics — who controls what can be seen and contested?
  4. Decision Systems & Authority — how is agency exercised in binding decisions, and can those decisions be contested, revised, or reversed?
  5. Knowledge & Intelligence — how does knowledge form, evolve, and remain open to revision?
  6. Human Capacity & Care — what relational conditions make sustained collective agency possible?

Write with precision and economy. Every sentence should earn its place. \
The voice is analytic but not clinical — it names things directly without \
performing certainty. Avoid jargon where plain language serves.\
"""

SYNTHESIS_PROMPT = """\
Generate a pattern for the Autonomy Stack based on the following definition \
and evidence from the research corpus.

## Pattern to generate

**Name:** {name}
**Description:** {description}
**Suggested related patterns:** {related}

## Format

Use this exact structure (match the examples precisely):

# Pattern: [Name]

## Summary
[One precise sentence describing what this pattern is.]

## Core Dynamic
[One sentence describing the mechanism — how this pattern operates.]

## Signals
- [Observable indicator]
- [Observable indicator]
- [Observable indicator]
- [Observable indicator]
(4-6 signals)

## What It Targets
[One sentence: what dimension of agency, capacity, or collective function does this pattern attack or erode?]

## Why It Works
[One sentence: what makes this pattern effective or difficult to resist?]

## Common Misreadings
- "[How people dismiss or misname this pattern]"
- "[Another common misreading]"
- "[Another common misreading]"
(3-4 misreadings, written as direct quotes of the dismissal)

## Related Patterns
- [Pattern name]
- [Pattern name]
(List provided related patterns plus any others strongly suggested by the evidence)

## Reference examples

{examples}

---

## Evidence from the research corpus

The following extractions are drawn from 18 months of the Metaviews: Future of \
Authority newsletter. They represent pattern candidates, signals, stack material, \
and concepts that relate to this pattern. Use them as raw material — synthesize \
the insight, do not copy the text.

{evidence}

---

Generate only the pattern file content. No preamble, no commentary after.\
"""

# ---------------------------------------------------------------------------
# Evidence collection
# ---------------------------------------------------------------------------
def collect_evidence(pattern: dict) -> str:
    """
    Search extraction files for content relevant to this pattern.
    Returns concatenated evidence capped at MAX_EVIDENCE_CHARS.
    """
    terms = [t.lower() for t in pattern["search_terms"]]
    evidence_parts = []

    files = sorted(
        [f for f in EXTRACTIONS_DIR.glob("*.md") if not f.name.startswith('.')],
        key=lambda f: f.name
    )

    for path in files:
        text = path.read_text(encoding='utf-8', errors='replace')
        text_lower = text.lower()

        if not any(term in text_lower for term in terms):
            continue

        # Extract only sections that match
        sections = re.split(r'\n### ', text)
        matching_sections = []

        for section in sections:
            sec_lower = section.lower()
            if any(term in sec_lower for term in terms):
                # Get the date from the frontmatter
                date_match = re.search(r'^date:\s*(\S+)', text, re.MULTILINE)
                date = date_match.group(1) if date_match else path.stem[:10]
                matching_sections.append(f"[{date}]\n### {section.strip()}")

        evidence_parts.extend(matching_sections)

    combined = "\n\n---\n\n".join(evidence_parts)

    # Trim to budget
    if len(combined) > MAX_EVIDENCE_CHARS:
        combined = combined[:MAX_EVIDENCE_CHARS] + "\n\n[... evidence truncated ...]"

    return combined if combined else "(No direct matches found — synthesize from general corpus knowledge of this dynamic.)"

# ---------------------------------------------------------------------------
# Checkpoint
# ---------------------------------------------------------------------------
def load_checkpoint() -> set[str]:
    if CHECKPOINT_FILE.exists():
        data = json.loads(CHECKPOINT_FILE.read_text(encoding='utf-8'))
        return set(data.get("generated", []))
    return set()


def save_checkpoint(generated: set[str]):
    CHECKPOINT_FILE.write_text(
        json.dumps({"generated": sorted(generated)}, indent=2),
        encoding='utf-8'
    )

# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------
def generate_pattern(pattern: dict, client: OpenAI, model: str) -> tuple[str | None, str | None]:
    """Returns (content, error)."""
    evidence = collect_evidence(pattern)

    prompt = SYNTHESIS_PROMPT.format(
        name=pattern["name"],
        description=pattern["description"],
        related=", ".join(pattern["related"]),
        examples=PATTERN_EXAMPLES,
        evidence=evidence,
    )

    response = client.chat.completions.create(
        model=model,
        max_tokens=MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": prompt},
        ],
    )

    return response.choices[0].message.content, None

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Generate Autonomy Stack patterns from the extraction corpus")
    parser.add_argument("--limit",   type=int, default=0,        help="Max patterns to generate this run (0 = all)")
    parser.add_argument("--pattern", type=str, default="",       help="Generate one specific pattern by name")
    parser.add_argument("--reset",   action="store_true",        help="Clear checkpoint and regenerate all")
    parser.add_argument("--model",   default=DEFAULT_MODEL,      help=f"OpenRouter model (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("OPENROUTER_API_KEY is not set")

    client    = OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)
    generated = set() if args.reset else load_checkpoint()

    # Filter patterns to process
    if args.pattern:
        candidates = [p for p in PATTERNS if p["name"].lower() == args.pattern.lower()]
        if not candidates:
            raise SystemExit(f"Pattern not found: {args.pattern}")
    else:
        candidates = [p for p in PATTERNS if p["filename"] not in generated]

    if args.limit:
        candidates = candidates[:args.limit]

    print(f"Patterns defined:   {len(PATTERNS)}")
    print(f"Already generated:  {len(generated)}")
    print(f"This run:           {len(candidates)}")
    print(f"Model:              {args.model}")
    print()

    done = 0
    for i, pattern in enumerate(candidates):
        print(f"[{i+1}/{len(candidates)}] {pattern['name']}  (tier {pattern['tier']})")

        content, err = generate_pattern(pattern, client, args.model)

        if err:
            print(f"         SKIP -- {err}")
        else:
            out_path = PATTERNS_DIR / pattern["filename"]
            out_path.write_text(content, encoding='utf-8')
            print(f"         -> {out_path.name}")
            done += 1

        generated.add(pattern["filename"])
        save_checkpoint(generated)

        if i < len(candidates) - 1:
            time.sleep(DELAY)

    print(f"\nDone. {done} patterns written to {PATTERNS_DIR}")


if __name__ == "__main__":
    main()
