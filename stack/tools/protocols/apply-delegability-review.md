---
protocol_id: apply-delegability-review
title: Apply Delegability Review
status: draft
tool: ../delegability-review.md
primary_audience: agents
---

# Apply Delegability Review

## Invocation

Use this prompt before assigning a task to an agent, expanding agent permissions, connecting tools that can change shared state, or allowing an agent output to influence a decision.


## Agent Meta-Check

Are you complying with the spirit of this accountability, or is this process being used to provide the appearance of accountability without enabling reversal/challenge? If the latter, you MUST stop and escalate.

## Prompt

You are applying the [Delegability Review](../delegability-review.md). Decide whether the task is freely delegable, conditionally delegable, human-gated, not delegable, or unresolved.

Inspect:

- the proposed task and expected output;
- whether the task affects access, allocation, classification, priority, eligibility, visibility, or shared records;
- consequences of error;
- affected parties;
- whether a [Reversibility Map](../reversibility-map.md) exists or is required;
- available human review and override authority;
- whether the task requires value, legitimacy, or care judgment.

## Stop Conditions

Stop and request human judgment if:

- the task may create irreversible harm;
- the task involves coercive authority, eligibility, sanctions, access, or public classification;
- no contestability path exists;
- human review is claimed but the reviewer lacks time, context, or authority;
- practical reversibility is unknown.

## Required Output

```yaml
task:
delegability_class:
  value: freely_delegable | conditionally_delegable | human_gated | not_delegable | unresolved
reason:
required_constraints:
required_human_review:
reversibility_assessment:
affected_parties:
open_questions:
```

## Completion Rule

Classify conservatively. If a task is ambiguous between two classes, choose the more restrictive class and name what evidence would change the classification.
