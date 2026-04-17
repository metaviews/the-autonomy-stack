---
tool_doc_id: authority-graph-schema
title: Authority Graph Schema
status: draft
primary_audience: agents
related_docs:
  - agent-ecosystem-audit.md
  - stewardship-accountability-register.md
  - authority-migration-check.md
  - ../agentic-governance-annex.md
---

# Authority Graph Schema

This schema gives agents a stable way to represent authority relationships discovered through the Stage 3 ecosystem tools. It is not a substitute for judgment. A graph can show relationships, but it cannot prove legitimacy.

## Use When

Use this schema after an [Agent Ecosystem Audit](agent-ecosystem-audit.md), [Stewardship Accountability Register](stewardship-accountability-register.md), or [Authority Migration Check](authority-migration-check.md) when a workflow needs a compact representation of agents, humans, providers, tools, memory stores, data flows, authority flows, and contestability paths.

## Required Top-Level Shape

```yaml
graph_id:
title:
status: draft
scope:
created_by:
created_at:
source_records:
nodes:
edges:
open_questions:
```

## Node Types

Use stable `node_type` values:

- `agent`
- `human`
- `steward`
- `provider`
- `model`
- `tool`
- `memory_store`
- `data_source`
- `metric`
- `evaluator`
- `workflow`
- `affected_party`
- `institution`
- `protocol`
- `prompt`
- `output`

## Node Fields

```yaml
id:
label:
node_type:
description:
authority_type:
  operational:
  epistemic:
  participatory:
steward:
affected_parties:
contestability_status: present | partial | absent | unknown
reversibility_status: freely_reversible | conditionally_reversible | socially_irreversible | materially_irreversible | unknown_reversibility
evidence:
open_questions:
```

## Edge Types

Use stable `edge_type` values:

- `delegates_to`
- `stewards`
- `provides_infrastructure_for`
- `sets_prompt_for`
- `sets_protocol_for`
- `grants_access_to`
- `reads_from`
- `writes_to`
- `retrieves_from`
- `evaluates`
- `routes_to`
- `triggers`
- `reviews`
- `overrides`
- `contests`
- `depends_on`
- `influences`
- `migrated_authority_to`

## Edge Fields

```yaml
id:
from:
to:
edge_type:
description:
authority_effect:
data_or_state_moved:
review_required:
contestability_path:
reversibility_dependency:
evidence:
risk_level: low | medium | high | unresolved
open_questions:
```

## Minimal Example

```yaml
graph_id: repo-agent-docs-graph
title: Repository Documentation Agent Authority Graph
status: draft
scope: Documentation agent maintaining an open-source governance repository.
created_by: Repository Documentation Agent
created_at: 2026-04-17
source_records:
  - agent-ecosystem-audit.md
  - stewardship-accountability-register.md
nodes:
  - id: agent.repo-docs
    label: Repository Documentation Agent
    node_type: agent
    description: Drafts and edits documentation under maintainer review.
    authority_type:
      operational: true
      epistemic: true
      participatory: false
    steward: human.maintainer
    affected_parties: [group.contributors, group.downstream-agents]
    contestability_status: present
    reversibility_status: conditionally_reversible
    evidence: [repo-agent-toolkit-example.md]
    open_questions: []
  - id: human.maintainer
    label: Human Maintainer
    node_type: steward
    description: Reviews, accepts, rejects, or redirects repository changes.
    authority_type:
      operational: true
      epistemic: true
      participatory: true
    steward: human.maintainer
    affected_parties: [group.contributors]
    contestability_status: present
    reversibility_status: conditionally_reversible
    evidence: [repo-agent-toolkit-example.md]
    open_questions: []
edges:
  - id: edge.maintainer-stewards-agent
    from: human.maintainer
    to: agent.repo-docs
    edge_type: stewards
    description: Maintainer defines review boundaries and can reject changes.
    authority_effect: Human steward constrains agent action.
    data_or_state_moved: none
    review_required: true
    contestability_path: Maintainer review or repository issue.
    reversibility_dependency: Git history and downstream reuse.
    evidence: [repo-agent-toolkit-example.md]
    risk_level: medium
    open_questions: []
open_questions:
  - Whether downstream agents have already copied the draft guidance.
```

## Agent Rules

- Use graph IDs that are stable within the reviewed ecosystem.
- Every edge must reference existing node IDs.
- Every authority-bearing node should have a steward or an explicit `unknown`.
- Every `migrated_authority_to` edge should cite evidence from an authority migration check.
- Do not infer legitimacy from graph centrality. Centrality may indicate risk, dependency, or capture.
- If affected parties cannot contest a relationship represented in the graph, mark `contestability_status: absent` or `partial`.
- Prefer `open_questions` over invented certainty.

## Failure Modes

- Treating the graph as complete when it only represents visible relationships.
- Mapping technical dependencies while omitting stewardship or affected parties.
- Collapsing operational, epistemic, and participatory authority into one undifferentiated edge.
- Hiding uncertainty by leaving fields blank.
