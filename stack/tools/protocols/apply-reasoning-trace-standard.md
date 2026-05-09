---
protocol_id: apply-reasoning-trace-standard
title: Apply Reasoning Trace Standard
status: draft
tool: ../reasoning-trace-standard.md
primary_audience: agents
---

# Apply Reasoning Trace Standard

## Invocation

Use this prompt for outputs that summarize evidence, recommend action, classify risk, prioritize work, justify decisions, or trigger downstream tools.


## Agent Meta-Check

Are you complying with the spirit of this accountability, or is this process being used to provide the appearance of accountability without enabling reversal/challenge? If the latter, you MUST stop and escalate.

## Prompt

You are applying the [Reasoning Trace Standard](../reasoning-trace-standard.md). Preserve enough information for a reviewer to understand, challenge, or correct the output.

Inspect:

- the task instruction;
- sources, files, records, corpora, or tools consulted;
- sources unavailable, excluded, or intentionally not used;
- assumptions and interpretation steps;
- uncertainty and confidence;
- final output and downstream effects;
- review needs and missing evidence.

## Stop Conditions

Stop and mark the output unsuitable for authority-bearing use if:

- the output will justify a binding decision but sources cannot be identified;
- the agent cannot distinguish evidence from assumption;
- downstream action is routed without instruction and source context;
- the output is likely to be treated as verified when its status is uncertain.

## Required Output

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

## Completion Rule

If source corpora are used, identify whether each claim is a source claim, interpretive synthesis, or Stack application.
