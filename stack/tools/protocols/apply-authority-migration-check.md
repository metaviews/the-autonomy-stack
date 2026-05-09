---
protocol_id: apply-authority-migration-check
title: Apply Authority Migration Check
status: draft
tool: ../authority-migration-check.md
primary_audience: agents
---

# Apply Authority Migration Check

## Invocation

Use this prompt after an ecosystem audit, during recurring system reviews, before renewing or expanding an agent deployment, or when a component has become difficult to replace, challenge, or ignore.


## Agent Meta-Check

Are you complying with the spirit of this accountability, or is this process being used to provide the appearance of accountability without enabling reversal/challenge? If the latter, you MUST stop and escalate.

## Prompt

You are applying the [Authority Migration Check](../authority-migration-check.md). Identify where authority has moved through repeated use, dependency, defaults, workflow centrality, or capacity loss rather than explicit delegation.

Inspect:

- agent ecosystem audit outputs;
- stewardship accountability register outputs;
- usage patterns, defaults, routing rules, and evaluation criteria;
- which agents, providers, models, prompts, memory stores, tools, metrics, or evaluators are most relied on;
- human review logs, override records, and contestation records;
- loss of alternative capacity or institutional memory;
- fallback paths, plural alternatives, and affected party challenge paths.

## Stop Conditions

Stop and request governance review if:

- a component has high migrated authority and no accountable steward;
- a provider or model can reshape outcomes without notice or contestability;
- affected parties cannot know that migrated authority shaped an outcome;
- human review depends on a component reviewers cannot inspect or override;
- no viable fallback exists for a component that now mediates binding or authority-bearing decisions.

## Required Output

```yaml
system_or_ecosystem:
review_period:
migration_candidates:
  - component:
    component_type: agent | provider | model | prompt | memory_store | tool | metric | evaluator | workflow_default | human_role | other
    migration_signal:
    authority_type:
    evidence:
    formal_delegation_status:
    affected_decisions:
    affected_parties:
    steward:
    contestability_status:
    reversibility_status:
    fallback_or_plural_alternatives:
    risk_level: low | medium | high | unresolved
required_updates:
  authority_cards:
  stewardship_register:
  contestability_paths:
  reasoning_traces:
  human_review:
redistribution_or_constraint_options:
open_questions:
```

## Completion Rule

If reliance is high but formal delegation is absent or unclear, mark the authority migration as at least `medium` risk unless strong contestability, fallback, and stewardship are already present.
