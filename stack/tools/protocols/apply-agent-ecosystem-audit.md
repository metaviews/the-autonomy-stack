---
protocol_id: apply-agent-ecosystem-audit
title: Apply Agent Ecosystem Audit
status: draft
tool: ../agent-ecosystem-audit.md
primary_audience: agents
---

# Apply Agent Ecosystem Audit

## Invocation

Use this prompt when a workflow involves multiple agents, models, tools, providers, memory stores, human review roles, or downstream systems. Use it before expanding an agent deployment or relying on an agent ecology for governance-relevant work.

## Prompt

You are applying the [Agent Ecosystem Audit](../agent-ecosystem-audit.md). Map the ecosystem as a system of relationships, dependencies, data flows, authority flows, and contestability paths.

Inspect:

- every agent or model that participates in the workflow;
- providers, platforms, compute dependencies, and infrastructure control points;
- tools, APIs, databases, memory stores, and external systems;
- human stewards, reviewers, operators, and affected parties;
- data flows, instruction flows, authority flows, and downstream actions;
- existing authority cards, reasoning traces, reversibility maps, and contestability protocols;
- where authority may have emerged through repeated use rather than explicit delegation.

## Stop Conditions

Stop and request governance review if:

- no steward is accountable for the ecosystem as a whole;
- authority flows cannot be reconstructed across agents or tools;
- affected parties cannot discover that an agent ecosystem shaped the outcome;
- no contestability path exists for ecosystem-level failure;
- a single provider, model, memory store, or steward can alter outcomes without review;
- human reviewers are accountable for outcomes they cannot inspect or override.

## Required Output

```yaml
ecosystem_name:
purpose:
agents:
  - name:
    role:
    authority_type:
    tools_or_permissions:
    steward:
providers_and_infrastructure:
  - name:
    dependency_type:
    control_points:
tools_and_memory_stores:
  - name:
    function:
    data_or_state_held:
    access_rules:
humans:
  - role:
    authority:
    review_or_override_capacity:
affected_parties:
data_flows:
instruction_flows:
authority_flows:
downstream_actions:
contestability_paths:
reversibility_dependencies:
reasoning_trace_requirements:
emergent_authority_risks:
single_points_of_failure:
stewardship_gaps:
required_constraints:
open_questions:
```

## Completion Rule

If the ecosystem cannot be mapped end to end, mark the audit `incomplete` in `open_questions` and identify which missing relationships block accountability.
