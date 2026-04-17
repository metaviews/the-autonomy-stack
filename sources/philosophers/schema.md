# Philosopher Autonomy Corpus Schema

This schema governs how agents maintain `sources/philosophers/`.

## Purpose

The corpus is not a general philosophy encyclopedia. It is a source-derived knowledge base for autonomy-related thought and its relevance to the Autonomy Stack.

## Canonical Correction

Because autonomy-centered anti-authoritarian traditions are often marginalized by state-centered academic canons, the corpus intentionally includes anarchist, anarchist-adjacent, abolitionist, Indigenous, feminist, and stateless governance thinkers where they clarify autonomy, mutual aid, self-organization, or anti-domination.

## Layers

### Raw Sources

Raw source records live in `raw/`. They may include:

- bibliographic records
- source links
- short public-domain excerpts
- notes about source availability
- acquisition or reading status

Agents should not rewrite raw source records except to correct metadata, add source links, or append new source notes.

### Compiled Wiki

Compiled wiki pages live in `wiki/`. Agents may update these pages when new source material changes the synthesis, adds a cross-reference, creates a contradiction, or reveals a Stack-relevant tension.

### Schema and Index

`schema.md` defines conventions. `index.yaml` routes agents to current pages and source records. The index does not replace the pages.

## Page Types

### Thinker Page

Use `wiki/thinkers/kebab-case-name.md`.

Required sections:

- Core Relevance to Autonomy
- Key Works and Source Records
- Source Claims
- Interpretive Synthesis
- Stack Application
- Tensions and Cautions
- Cross-References

### Concept Page

Use `wiki/concepts/kebab-case-concept.md`.

Required sections:

- Working Definition
- Associated Thinkers
- Source Claims
- Interpretive Synthesis
- Stack Application
- Tensions and Cautions
- Cross-References

### Tension Page

Use `wiki/tensions/kebab-case-tension.md`.

Required sections:

- Tension
- Thinkers Who Illuminate It
- Source Claims
- Interpretive Synthesis
- Stack Application
- Open Questions
- Cross-References

## Ingest Workflow

1. Add or update a source record in `raw/`.
2. Identify affected thinker, concept, and tension pages.
3. Update compiled pages with explicit separation of source claim, interpretive synthesis, and Stack application.
4. Update `index.yaml`.
5. Flag contradictions, unresolved interpretive questions, or weak source coverage.

## Agent Rules

- Do not treat a compiled page as a source.
- Do not quote copyrighted material at length.
- Do not infer a thinker endorses the Autonomy Stack.
- Distinguish influence, resonance, contrast, and challenge.
- Prefer "illuminates," "complicates," or "challenges" over "supports" unless the source directly supports the claim.
- If source coverage is thin, mark the page as incomplete.
- Do not drop a candidate thinker because they are outside state-centered or academic canons; mark them as candidate or later-wave if source coverage is not yet ready.
