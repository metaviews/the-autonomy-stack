# Roadmap Session Brief

*Read this at the start of a new session before beginning roadmap work.*

---

## What We're Building

A development roadmap for the Autonomy Stack — a governance operating system that maps the conditions under which individual and collective agency is possible, sustainable, and contestable.

The roadmap should take the project from its current state (v0.3, reference architecture with integrated corpus) toward a framework that is operational and usable by practitioners, institutions, and automated systems.

---

## What Has Been Done (Do Not Redo)

### Architecture — v0.3 complete

The Stack's six layers have been reframed as **dimensions of agency**:

1. Material Base — *What material conditions make agency possible?*
2. Commons & Institutions — *What structures sustain collective agency, and what makes them vulnerable to capture?*
3. Legibility & Metrics — *Who controls what can be seen and contested?*
4. Decision Systems & Authority — *How is agency exercised in binding decisions — and can those decisions be contested, revised, or reversed?*
5. Knowledge & Intelligence — *How does knowledge form, evolve, and remain open to revision?*
6. Human Capacity & Care — *What relational conditions make sustained collective agency possible?*

Read `stack/00-overview.md` for the full architecture.

### Corpus — fully integrated

296 issues of the *Metaviews: Future of Authority* newsletter (Oct 2024–Mar 2026) have been extracted, audited, and used to ground the architecture. The extraction corpus is in `sources/extractions/`. The corpus audit is at `sources/extractions/AUDIT.md`.

Key finding from the corpus: a clear three-stage arc — Crisis Detection → Institutional Failure → Alternative Construction. The Stack's next phase should reflect this trajectory.

### Pattern library — 15 patterns

Located in `patterns/`. Three tiers:
- Tier 1: Algorithmic Authority, Epistemic Warfare, Legitimacy Drift
- Tier 2: Care vs. Coercion, Platform Capture, Obedience in Advance, Institutional Weaponization
- Tier 3: Manufactured Ambiguity, Strategic Ambiguity, Commons Destruction, Material Base Sovereignty, Distributed Resistance
- Established: Temporal Capture, Internalized Policing, Hybrid War

### Foundational documents for the roadmap

Read these before writing a single roadmap item:

**`stack/MODULE-CANDIDATES.md`** — Five areas identified as ready for structured experimentation, with recommended sequencing:
- Phase 1 (immediate): Food Power & Agricultural Sovereignty, Care-Based Infrastructure Design
- Phase 2 (~6 months): Epistemic Coordination & Distributed Intelligence, Commons & Institutional Governance
- Phase 3 (~12 months): Distributed Resistance & Tactical Coordination

**`stack/PROVOCATIONS.md`** — Eight unresolved tensions that challenge Stack assumptions. These are not problems to route around — they are the conditions the roadmap must be honest about. Any roadmap item that touches one of these provocations should acknowledge it explicitly.

The eight provocations:
1. Technical opacity masking power (legibility is necessary but insufficient)
2. Care-based authority resisting contestation (the moralization trap)
3. Expertise forbidden yet required (the knowledge authority paradox)
4. Distributed systems too slow for crises (resilience-speed trade-off)
5. Language itself as contested terrain (semantic collapse)
6. Private authority beyond formal contestation
7. Material base as authority mechanism, not just precondition
8. Care capacity depleted by the system that demands it

---

## The Task

Build a roadmap that moves the Autonomy Stack from reference architecture toward operational framework.

### What a good roadmap for this project looks like

This is not a software product roadmap. It should not be structured around sprints, features, or releases. It should be structured around **maturation stages** — each stage deepening the Stack's grounding, extending its reach, or operationalizing its architecture.

The roadmap should address:

1. **Module development** — which modules, in what sequence, toward what concrete outputs (frameworks, design patterns, toolkits, case studies)
2. **Pattern maturation** — which patterns need deepening, which need stress-testing, which point toward patterns not yet written (the existing patterns reference several: Proceduralism as Shield, Legitimacy Drift already written but Procedural Entombment, Collective Leadership Architecture not yet written)
3. **Provocation work** — which unresolved tensions are addressable in the near term, which require sustained framework development, which should be named as permanent design conditions
4. **Vocabulary/lexicon** — the corpus produced 330+ concept entries; a Stack lexicon would make the framework self-contained and accessible
5. **Agentic operationalization** — how agentic computing enters explicitly (deferred in v0.3, but belongs in the roadmap's later stages)
6. **Public and practitioner interface** — what would make the Stack usable by people outside the project

### What the roadmap is NOT

- A complete build plan with timelines and owners
- A content calendar for a newsletter
- A feature list
- A document that resolves the provocations (it shouldn't — it should sit with or expand them)

### Tone and posture

The roadmap should reflect the Stack's own principles. Particularly:
- **Nothing is final** — the roadmap is itself a living document
- **Disagreement is a design condition** — the roadmap should acknowledge genuine uncertainty about sequencing and priority
- **Failure is informative** — build in explicit checkpoints and review moments, not just milestones
- **Legibility over expertise** — write it so a careful first-time reader of the Stack could understand what the work is and why it matters

---

## Files to Read Before Starting

In order of priority:

1. `stack/00-overview.md` — the current architecture (v0.3)
2. `stack/MODULE-CANDIDATES.md` — the five module candidates with sequencing
3. `stack/PROVOCATIONS.md` — the eight unresolved tensions
4. `stack/STATE.md` — current orientation
5. `PRINCIPLES.md` — the eight design constraints
6. `sources/extractions/AUDIT.md` — corpus shape and temporal arc

Pattern library (`patterns/`) is worth skimming for the vocabulary.

---

## Output

Write the roadmap to: `stack/ROADMAP.md`

It should be a document that a new collaborator could read and understand where the project is going and why — and that the project itself could return to and revise as conditions change.
