---
tool_doc_id: metadata-conventions
title: Metadata Conventions for Agentic Governance Tools
status: draft
primary_audience: agents
related_docs:
  - README.md
  - index.yaml
  - ../indexes/README.md
---

# Metadata Conventions

These conventions keep toolkit documents readable by agents without turning the toolkit into a formal compliance schema. Frontmatter should orient agents, not replace the prose document.

## General Rules

- Use YAML frontmatter at the top of each toolkit document.
- Keep field names stable once introduced.
- Use kebab-case identifiers.
- Prefer relative links.
- Treat `status: draft` as an orientation marker, not as approval status.
- Do not infer missing authority from metadata. If a field is absent or unclear, read the source document and mark the ambiguity.

## Toolkit Document Fields

Use these fields for governance tools:

```yaml
tool_id:
title:
status:
primary_question:
applies_to:
related_layers:
related_requirements:
related_docs:
```

Use `tool_id` for a single reusable tool, such as `delegability-review`.

## Supporting Document Fields

Use these fields for vocabulary, examples, conventions, or README-like documents:

```yaml
tool_doc_id:
title:
status:
primary_audience:
related_docs:
```

Use `tool_doc_id` when the document supports the toolkit but is not itself a diagnostic instrument.

## Index Files

Index files should be YAML and should include:

```yaml
index_id:
title:
status:
```

An index should route agents to source documents. It should not summarize enough material for an agent to skip reading the source.

## Layer References

Use the stable layer codes:

- `L1` Material Base
- `L2` Commons & Institutions
- `L3` Legibility & Metrics
- `L4` Decision Systems & Authority
- `L5` Knowledge & Intelligence
- `L6` Human Capacity & Care

## Provocation References

Use the stable provocation codes `P1` through `P8` from `../PROVOCATIONS.md`.

## Status Values

Use only these status values unless the repository later defines a formal lifecycle:

- `draft` - usable but still open to revision
- `stable` - relied on by other documents
- `superseded` - kept for lineage but no longer current

## Agent Behavior

When metadata and prose appear to conflict, prefer the prose and flag the inconsistency. When an index and a source document conflict, prefer the source document and flag the index for review.
