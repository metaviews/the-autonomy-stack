---
tool_id: agent-ecosystem-audit
title: Agent Ecosystem Audit
status: draft
primary_question: What agents, humans, providers, tools, memory stores, and affected parties form this ecosystem, and where has authority accumulated?
applies_to:
  - multi-agent systems
  - agent deployments
  - platform-mediated workflows
  - agent infrastructure reviews
related_layers:
  - L1 Material Base
  - L2 Commons & Institutions
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
  - L5 Knowledge & Intelligence
  - L6 Human Capacity & Care
related_requirements:
  - Emergent authority must be monitored and redistributed.
  - Stewardship is authority and must be accountable.
  - Legibility must run both ways.
related_docs:
  - ../agentic-governance-annex.md
  - agent-authority-card.md
  - contestability-protocol.md
  - reasoning-trace-standard.md
---

# Agent Ecosystem Audit

## Purpose

Use this tool to map a system of interacting agents, tools, providers, memory stores, humans, and affected parties. The goal is to identify where authority, dependency, data, and contestability actually reside across the ecosystem.

## When To Use

Use when more than one agent, model, provider, tool, workflow, or human review role participates in producing an output or action. Use before expanding an agent deployment, connecting agents to shared infrastructure, or relying on an agent ecology for governance-relevant work.

## Inputs

- Agents and agent roles
- Providers, models, platforms, and infrastructure dependencies
- Tools, APIs, databases, memory stores, and external systems
- Human stewards, reviewers, operators, and affected parties
- Data flows, instruction flows, authority flows, and escalation paths
- Existing authority cards, reasoning traces, contestability paths, and reversibility maps

## Diagnostic Questions

- Which agents participate in the workflow, and what does each contribute?
- Which human actors set goals, permissions, prompts, review standards, or escalation rules?
- Which providers or platforms control access, compute, model behavior, storage, or policy enforcement?
- What data enters, moves through, or leaves the ecosystem?
- Which agents or systems can trigger downstream action?
- Which outputs are likely to be treated as authoritative?
- Where can authority migrate through repeated use rather than explicit delegation?
- Where does the ecosystem depend on a single provider, model, memory store, or steward?
- Can affected parties know which agents shaped an output or action?
- Can affected parties challenge the ecosystem-level outcome, not only one component's output?
- What evidence is preserved across component boundaries?
- What functions would degrade if one agent, provider, or human steward failed?

## Output Format

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

## Agent Use Protocol

Audit the ecosystem as a system, not as a list of isolated agents. If a component's output cannot be understood without another component's retrieval, synthesis, memory, or action, treat accountability as distributed. Use the audit to determine where more specific tools are needed: [Agent Authority Card](agent-authority-card.md), [Reasoning Trace Standard](reasoning-trace-standard.md), [Reversibility Map](reversibility-map.md), and [Contestability Protocol](contestability-protocol.md).

## Stop Conditions

- No steward is accountable for the ecosystem as a whole.
- Authority flows cannot be reconstructed across agents or tools.
- Affected parties cannot discover that an agent ecosystem shaped the outcome.
- No contestability path exists for ecosystem-level failure.
- A single provider, model, memory store, or steward can alter outcomes without review.
- Human reviewers are accountable for outcomes they cannot inspect or override.

## Related Stack Concepts

Agent ecosystems create authority through relationships, dependencies, and repeated use. Ecosystem governance asks where power has accumulated, not only where authority was formally delegated.
