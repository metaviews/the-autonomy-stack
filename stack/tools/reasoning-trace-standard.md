---
tool_id: reasoning-trace-standard
title: Reasoning Trace Standard
status: draft
primary_question: What must be preserved so an authority-bearing agent output can be examined and challenged?
applies_to:
  - synthesis outputs
  - recommendations
  - classifications
  - agent tool use
related_layers:
  - L3 Legibility & Metrics
  - L5 Knowledge & Intelligence
related_requirements:
  - Legibility of reasoning is non-negotiable for authority-bearing outputs.
  - Emergent authority must be monitored and redistributed.
related_docs:
  - ../agentic-governance-annex.md
  - ../modules/epistemic-coordination.md
---

# Reasoning Trace Standard

## Purpose

Use this tool to preserve the minimum review record for an agent output that may carry epistemic or decision authority. The goal is not full model interpretability. The goal is enough traceability for meaningful challenge.

## When To Use

Use for outputs that summarize evidence, recommend action, classify risk, prioritize work, justify decisions, or trigger downstream tools.

## Inputs

- Task instruction
- Sources or data consulted
- Tools used
- Intermediate outputs
- Final output
- Downstream action

## Diagnostic Questions

- What instruction shaped the output?
- What sources, files, records, or tools were used?
- What was excluded or unavailable?
- What assumptions shaped the synthesis?
- What uncertainty remains?
- What confidence or status should be attached to the output?
- What downstream action did the output inform or trigger?
- What would a reviewer need to challenge the output?

## Output Format

```yaml
output_id:
task_instruction:
sources_consulted:
sources_unavailable_or_excluded:
tools_used:
intermediate_steps:
assumptions:
uncertainty:
confidence_or_status:
final_output:
downstream_effects:
review_needs:
open_questions:
```

## Agent Use Protocol

Produce a trace when the output may be used as information, analysis, recommendation, or justification. If a trace cannot be produced, mark the output as unsuitable for authority-bearing use.

## Stop Conditions

- The output will justify a binding decision but sources cannot be identified.
- The agent cannot distinguish evidence from assumption.
- The output routes downstream action without preserving the instruction and source context.
- The output is likely to be treated as verified when its status is uncertain.

## Related Stack Concepts

Technical logs are not enough. Epistemic legibility requires a reviewer to understand what was consulted, assumed, excluded, and triggered.
