---
tool_id: authority-migration-check
title: Authority Migration Check
status: draft
primary_question: Has authority moved through repeated use, dependency, defaults, or workflow centrality rather than explicit delegation?
applies_to:
  - agent ecosystems
  - recurring agent workflows
  - provider and model dependencies
  - memory and evaluation systems
related_layers:
  - L2 Commons & Institutions
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
  - L5 Knowledge & Intelligence
related_requirements:
  - Emergent authority must be monitored and redistributed.
  - Delegation must be explicit and bounded.
  - Stewardship is authority and must be accountable.
related_docs:
  - ../agentic-governance-annex.md
  - agent-ecosystem-audit.md
  - stewardship-accountability-register.md
  - reasoning-trace-standard.md
  - authority-graph-schema.md
---

# Authority Migration Check

## Purpose

Use this tool to identify authority that has migrated to an agent, provider, model, prompt, memory store, metric, evaluator, or workflow default without being formally delegated. Migration is often visible through reliance, centrality, convenience, or loss of alternative capacity.

## When To Use

Use after an [Agent Ecosystem Audit](agent-ecosystem-audit.md), during recurring system reviews, before renewing or expanding agent deployments, or when a component has become difficult to replace, challenge, or ignore.

## Inputs

- Agent ecosystem audit
- Stewardship accountability register
- Usage patterns and dependency records
- Default prompts, routing rules, and evaluation criteria
- Human review logs and override records
- Known alternatives or fallback paths
- Affected parties and contestation records

## Migration Signals

**Reliance:** People or agents increasingly defer to one component because it is available, fast, familiar, or treated as normal.

**Default capture:** A prompt, model, metric, provider, or route becomes authoritative because changing it requires effort or permission.

**Capacity loss:** Human or institutional capacity degrades because the agent now performs the work.

**Epistemic centrality:** One agent, corpus, memory store, or evaluator becomes the main source of what counts as known, relevant, safe, or high quality.

**Provider leverage:** A provider can alter access, cost, behavior, policy, or availability in ways that reshape the ecosystem.

**Contestability drift:** Challenge paths exist on paper but become too slow, obscure, costly, or weak to affect outcomes.

## Diagnostic Questions

- Which component is consulted most often, trusted most quickly, or used as the default?
- Which decisions now depend on an agent output even if humans formally decide?
- Which human capacities, review practices, or institutional memories have weakened through substitution?
- Which provider, model, memory store, prompt, metric, or evaluator would be hard to replace?
- Who can change the component that now shapes outcomes?
- Was this authority formally delegated, or did it emerge through use?
- Can affected parties identify and challenge the migrated authority?
- Are there viable fallback paths or plural alternatives?
- Has the steward updated authority cards, contestability paths, or review obligations to reflect the migration?
- Does the migration concentrate authority across operational, epistemic, and participatory layers?

## Output Format

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

## Agent Use Protocol

Look for where practical reliance has outrun formal authorization. Do not treat the absence of a formal decision as evidence that no authority has moved. If a component shapes what is seen, trusted, ranked, routed, remembered, or acted on, it may be exercising authority. Use `migrated_authority_to` edges from the [Authority Graph Schema](authority-graph-schema.md) when representing migration relationships.

## Stop Conditions

- A component has high migrated authority and no accountable steward.
- A provider or model can reshape outcomes without notice or contestability.
- Affected parties cannot know that migrated authority shaped an outcome.
- Human review depends on a component reviewers cannot inspect or override.
- No viable fallback exists for a component that now mediates binding or authority-bearing decisions.

## Related Stack Concepts

Authority can migrate without announcement. The governance task is to notice when dependence has become power and update accountability before that power becomes invisible infrastructure.
