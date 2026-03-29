# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

The Autonomy Stack is a **documentation-first governance framework** — no build system, no tests. All content is markdown. The project maps the conditions under which individual and collective agency is possible, sustainable, and contestable, organized as a reference architecture across six interconnected layers.

It has a dual-use audience: human readers and automated systems. Artifacts are written to be legible to both without implying hierarchy or command.

## Repository Structure

**`/stack/`** — The conceptual core.
- `00-overview.md` — Primary architecture document (currently v0.3). The foundational claim: layers are dimensions of agency, not merely domains of governance.
- `STATE.md` — Living orientation snapshot: what is stable, what is active, what is unresolved.
- `MODULE-CANDIDATES.md` — Five areas mature enough for structured experimentation, with recommended sequencing.
- `PROVOCATIONS.md` — Eight unresolved tensions that challenge Stack assumptions; essential reading before proposing major additions.

**`/patterns/`** — Recurring governance dynamics distilled from practice. 15 patterns currently in the library. They describe recurrent phenomena, not rules.

**`/signals/`** — Short orientation artifacts (<200 words). Timestamped. Capture shifts in attention and emerging tensions before they are ready to become patterns.

**`/sources/`** — Source material. `metaviews.substack.com/` contains the full Metaviews: Future of Authority newsletter archive (296 issues, Oct 2024–Mar 2026). `extractions/` contains structured per-issue extractions and `AUDIT.md` — a full corpus analysis.

**`/scripts/`** — Processing pipeline.
- `extract.py` — Processes newsletter HTML → structured extractions (signals, pattern candidates, stack material, concepts, provocations). Uses OpenRouter via `openai` SDK. Config in `.env`.
- `generate_patterns.py` — Synthesizes patterns from extraction corpus. Same infrastructure as extract.py.
- `requirements.txt` — `openai`, `python-dotenv`.

Supporting root documents: `PRINCIPLES.md` (8 design constraints), `VISION.md` (v0.1 origin), `CHANGELOG.md`.

## The Six Layers (v0.3 framing)

Each layer is a dimension of agency — a question about what makes autonomy possible:

1. **Material Base** — *What material conditions make agency possible?*
2. **Commons & Institutions** — *What structures sustain collective agency, and what makes them vulnerable to capture?*
3. **Legibility & Metrics** — *Who controls what can be seen and contested?*
4. **Decision Systems & Authority** — *How is agency exercised in binding decisions — and can those decisions be contested, revised, or reversed?*
5. **Knowledge & Intelligence** — *How does knowledge form, evolve, and remain open to revision?*
6. **Human Capacity & Care** — *What relational conditions make sustained collective agency possible?*

## Artifact Conventions

**Patterns** follow a consistent 7-section structure: Summary / Core Dynamic / Signals / What It Targets / Why It Works / Common Misreadings / Related Patterns. Voice is analytic but not clinical — names things directly without performing certainty.

**Signals** are named `YYYY-MM-DD--kebab-case-title.md`. They do not resolve tension — they surface it.

**Extractions** (in `sources/extractions/`) are named `YYYY-MM-DD--slug.md` with YAML frontmatter. Organized by category: SIGNAL / PATTERN CANDIDATE / STACK MATERIAL / CONCEPT / PROVOCATION / OTHER.

**STATE.md** is revised when orientation changes, not on a schedule.

## Scripts

Both scripts load `.env` from repo root for `OPENROUTER_API_KEY` and `OPENROUTER_MODEL`. Progress is checkpointed after each item — safe to interrupt and resume.

```bash
pip install -r scripts/requirements.txt
python scripts/extract.py --limit 10      # test batch
python scripts/extract.py                 # full run
python scripts/generate_patterns.py       # generate all patterns
python scripts/generate_patterns.py --pattern "Pattern Name"  # single pattern
```

## Content Principles

All work is constrained by `PRINCIPLES.md`. The proceeding constraint: new work belongs in the Autonomy Stack only when it clarifies how autonomy — understood as the conditions for individual and collective agency — is sustained, constrained, or lost under complex and contested conditions.

Before proposing major structural changes, read `PROVOCATIONS.md`. Many apparent gaps are already named as unresolved tensions requiring framework development, not quick fixes.

## Content Flow

**narrative (newsletter) → extraction → signal → pattern → stack layer → module**

Movement is directional but non-linear. The corpus pipeline (extract.py) handles the newsletter → extraction step. From there, extractions inform signals, patterns, and layer revisions through editorial judgment, not automation.
