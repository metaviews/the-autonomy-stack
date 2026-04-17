# QWEN.md — The Autonomy Stack

## Project Overview

The Autonomy Stack is a **documentation-first governance framework** — a living reference architecture that maps the conditions under which individual and collective agency is possible, sustainable, and contestable. It is not a software project, startup, or political platform. Most content is Markdown, with lightweight YAML indexes for agent-readable navigation.

The current operational audience now includes agents as primary readers and actors. Agent-facing artifacts should remain diagnostic and contestable, not compliance certificates.

The framework treats governance as an **operating system** composed of six interconnected layers, each understood as a dimension of agency:

1. **Material Base** — What material conditions make agency possible?
2. **Commons & Institutions** — What structures sustain collective agency, and what makes them vulnerable to capture?
3. **Legibility & Metrics** — Who controls what can be seen and contested?
4. **Decision Systems & Authority** — How is agency exercised in binding decisions — and can those decisions be contested, revised, or reversed?
5. **Knowledge & Intelligence** — How does knowledge form, evolve, and remain open to revision?
6. **Human Capacity & Care** — What relational conditions make sustained collective agency possible?

The current architecture is **v0.3**, which reframes layers as dimensions of agency rather than merely domains of governance.

## Repository Structure

| Path | Description |
|---|---|
| `stack/00-overview.md` | Primary architecture document (v0.3) |
| `stack/STATE.md` | Living orientation snapshot — what is stable, active, unresolved |
| `stack/entry.md` | 2,000-word orientation for first-time readers |
| `stack/LEXICON.md` | ~80 core terms with definitions and cross-references |
| `stack/PROVOCATIONS.md` | Eight unresolved tensions that challenge Stack assumptions |
| `stack/design-toolkit.md` | Diagnostic questions by layer for practitioners |
| `stack/pattern-quick-reference.md` | All 20 patterns in 1–2 sentences with layer mappings |
| `stack/agentic-governance-annex.md` | How each layer applies to agentic systems |
| `stack/ROADMAP-AGENTIC-GOVERNANCE-TOOLS.md` | Current vNext roadmap for agent-legible governance tooling |
| `stack/tools/` | Agentic Governance Toolkit: five diagnostic instruments, vocabulary, metadata conventions, and example |
| `stack/tools/index.yaml` | Agent-readable tool index with use cases, inputs, and outputs |
| `stack/indexes/` | Lightweight YAML indexes for layers, patterns, and provocations |
| `stack/modules/` | Five completed domain modules (Food Power, Care Infrastructure, Epistemic Coordination, Commons & Institutional Governance, Distributed Resistance) |
| `stack/cases/` | Completed case studies + candidate review file (`candidates.md`) |
| `patterns/` | 20 recurring governance dynamics with 7-section structure |
| `signals/` | Short orientation artifacts (<200 words), timestamped |
| `sources/` | Source material including Metaviews newsletter archive and structured extractions |
| `scripts/` | Processing pipeline: extraction, pattern generation, case study discovery and generation |
| `PRINCIPLES.md` | 8 design constraints that bound all work |
| `VISION.md` | Origin document (v0.1) |
| `CHANGELOG.md` | Version history |

## Key Principles

All work is constrained by the eight principles in `PRINCIPLES.md`. They are **limits**, not aspirations:

1. Authority must be contestable
2. Power without legibility is unacceptable
3. Disagreement is a design condition
4. Resilience takes priority over elegance
5. Legibility takes priority over expertise
6. Opaque mechanisms require extraordinary justification
7. Failure is informative
8. Nothing is final

Before proposing major structural changes, read `PROVOCATIONS.md` — many apparent gaps are already named as unresolved tensions.

## Content Flow

The project follows a directional (but non-linear) content pipeline:

```
narrative (newsletter) → extraction → signal → pattern → stack layer → module
                                                    ↓
                                              case study → applied testing
```

- **Extractions** are produced by `scripts/extract.py` from the Metaviews newsletter archive
- **Patterns** are synthesized from the extraction corpus via `scripts/generate_patterns.py`
- **Case study candidates** are discovered from the corpus via `scripts/find_cases.py`
- **Case studies** are generated from approved candidates via `scripts/write_cases.py`
- Movement between stages happens through editorial judgment, not automation

## Scripts

All scripts use the OpenRouter API via the `openai` SDK. Configuration is in `.env` at the repo root (`OPENROUTER_API_KEY`, `OPENROUTER_MODEL`). Progress is checkpointed after each item — safe to interrupt and resume.

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Extract from newsletter (test batch or full run)
python scripts/extract.py --limit 10
python scripts/extract.py

# Generate patterns (all or single)
python scripts/generate_patterns.py
python scripts/generate_patterns.py --pattern "Pattern Name"

# Find case study candidates from corpus (or user-directed query)
python scripts/find_cases.py
python scripts/find_cases.py --limit 10
python scripts/find_cases.py --query "platform governance failures"
python scripts/find_cases.py --sources path/to/text.md  # add user-provided sources

# Generate case studies from approved candidates
python scripts/write_cases.py                            # all approved
python scripts/write_cases.py --case "Case Name"         # one specific
python scripts/write_cases.py --cases "A" "B"            # multiple
python scripts/write_cases.py --limit 2                  # next 2 approved only
```

Dependencies: `openai>=1.0.0`, `python-dotenv>=1.0.0`

## Artifact Conventions

- **Patterns** follow a 7-section structure: Summary / Core Dynamic / Signals / What It Targets / Why It Works / Common Misreadings / Related Patterns
- **Signals** are named `YYYY-MM-DD--kebab-case-title.md` and surface tension rather than resolve it
- **Extractions** are named `YYYY-MM-DD--slug.md` with YAML frontmatter, categorized as SIGNAL / PATTERN CANDIDATE / STACK MATERIAL / CONCEPT / PROVOCATION / OTHER
- **Agentic governance tools** use YAML frontmatter, diagnostic sections, and explicit stop conditions; see `stack/tools/metadata-conventions.md`
- **Indexes** route agents to source documents and should not be treated as replacements for the source material
- Voice is analytic but not clinical — names things directly without performing certainty

## How to Engage

- Read `stack/entry.md` for a first-time orientation
- Read `stack/STATE.md` for current posture and open tensions
- Use `stack/tools/README.md` and `stack/tools/index.yaml` when applying the agentic governance toolkit
- Use `stack/indexes/` for agent navigation across layers, patterns, and provocations
- Read `PRINCIPLES.md` and `PROVOCATIONS.md` before proposing significant additions or changes
- Treat uncertainty as a feature, not a flaw
- All design choices must surface their assumptions and trade-offs explicitly
