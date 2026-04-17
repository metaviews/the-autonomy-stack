---
protocol_id: apply-reversibility-map
title: Apply Reversibility Map
status: draft
tool: ../reversibility-map.md
primary_audience: agents
---

# Apply Reversibility Map

## Invocation

Use this prompt before an agent changes shared state, publishes or routes an authority-bearing output, classifies a person or group, triggers downstream tools, alters access, affects resource allocation, or makes a recommendation likely to be followed.

## Prompt

You are applying the [Reversibility Map](../reversibility-map.md). Classify whether the action can be reversed in practice, not only in theory.

Inspect:

- what exact action, output, or effect would need reversal;
- downstream systems, actors, caches, copies, or decisions;
- affected parties and notice requirements;
- logs, evidence, and reasoning traces needed for reversal;
- who has authority and technical ability to reverse;
- the deadline for reversal before harm becomes durable;
- residual reputational, relational, legal, material, or care harms.

## Stop Conditions

Stop and request human judgment if:

- reversibility is unknown and the action may affect access, allocation, classification, safety, visibility, or rights;
- the reversal actor lacks authority, time, evidence, or technical ability;
- affected parties cannot be notified of correction;
- the action may create materially irreversible harm;
- rollback only removes one record while downstream effects remain.

## Required Output

```yaml
action_or_output:
affected_parties:
downstream_dependencies:
reversibility_class:
  value: freely_reversible | conditionally_reversible | socially_irreversible | materially_irreversible | unknown_reversibility
reason:
required_evidence:
rollback_or_correction_mechanism:
authorized_reversal_actor:
reversal_deadline:
notice_to_affected_parties:
residual_harm_after_reversal:
required_constraints_before_action:
open_questions:
```

## Completion Rule

If an action is ambiguous between two reversibility classes, choose the less reversible class.
