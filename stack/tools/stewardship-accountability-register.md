---
tool_id: stewardship-accountability-register
title: Stewardship Accountability Register
status: draft
primary_question: Who sets, changes, reviews, and is accountable for the rules under which agents act?
applies_to:
  - agent stewardship
  - multi-agent governance
  - protocol ownership
  - access and update governance
related_layers:
  - L2 Commons & Institutions
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
  - L5 Knowledge & Intelligence
  - L6 Human Capacity & Care
related_requirements:
  - Stewardship is authority and must be accountable.
  - Delegation must be explicit and bounded.
  - Emergent authority must be monitored and redistributed.
related_docs:
  - ../agentic-governance-annex.md
  - agent-ecosystem-audit.md
  - agent-authority-card.md
  - human-in-the-loop-adequacy-test.md
  - authority-graph-schema.md
---

# Stewardship Accountability Register

## Purpose

Use this tool to identify the people, teams, institutions, or providers who govern the conditions under which agents act. Stewardship includes setting prompts, protocols, access rules, model choices, memory policies, evaluation criteria, escalation rules, and update practices.

## When To Use

Use after an [Agent Ecosystem Audit](agent-ecosystem-audit.md), before expanding agent permissions, when responsibility for an agentic system is unclear, or when a system claims accountability but does not name who can change the rules.

## Inputs

- Agent ecosystem or deployment
- Steward roles and institutions
- Protocols, prompts, policies, and evaluation criteria
- Access, permission, memory, and update rules
- Human review and escalation responsibilities
- Affected parties and contestation channels
- Known providers or external dependencies

## Stewardship Domains

**Protocol stewardship:** Who defines how agents should act, stop, escalate, and document reasoning.

**Prompt stewardship:** Who writes, approves, changes, and audits system or workflow prompts.

**Access stewardship:** Who grants, removes, or constrains access to tools, data, memory, users, or external systems.

**Model and provider stewardship:** Who chooses models, providers, hosting terms, fallback systems, and infrastructure dependencies.

**Memory stewardship:** Who governs what is stored, forgotten, corrected, retrieved, or shared across agents.

**Evaluation stewardship:** Who defines success, safety, quality, legitimacy, and failure criteria.

**Update stewardship:** Who changes agent behavior over time and how those changes are reviewed, announced, and reversed.

**Contestability stewardship:** Who receives challenges, preserves evidence, reviews disputes, and can alter outcomes.

## Diagnostic Questions

- Who can change the rules under which the agent acts?
- Who approves prompts, protocols, access rules, memory policies, and evaluation criteria?
- Who can halt, roll back, or narrow the system?
- Who is accountable when a provider, model, memory store, or tool changes behavior?
- Which stewardship roles are held by the same actor, and does that concentrate authority?
- Which stewardship roles are externalized to a provider or platform?
- Can affected parties identify the steward responsible for a contested outcome?
- Are stewards resourced with time, competence, and authority?
- How are stewardship decisions logged and reviewed?
- What happens when stewards disagree?

## Output Format

```yaml
system_or_ecosystem:
stewardship_scope:
stewards:
  - name_or_role:
    institution_or_provider:
    stewardship_domains:
    decisions_controlled:
    authority_limits:
    review_obligations:
    escalation_path:
    affected_party_contact:
protocol_stewardship:
prompt_stewardship:
access_stewardship:
model_and_provider_stewardship:
memory_stewardship:
evaluation_stewardship:
update_stewardship:
contestability_stewardship:
concentrated_authority_risks:
externalized_stewardship_risks:
unowned_decisions:
required_logs:
required_reviews:
open_questions:
```

## Agent Use Protocol

Treat stewardship as governance authority. Do not describe a role as merely technical maintenance if it can change what agents see, do, remember, optimize, or escalate. If a stewardship role is unowned, record it as an accountability gap.

## Stop Conditions

- No steward can be identified for prompts, protocols, access rules, memory, model choice, or escalation.
- A provider can change material behavior without notice, review, or contestability.
- Affected parties cannot identify who is accountable for a contested outcome.
- Human stewards are responsible for decisions they cannot inspect, halt, or reverse.
- Stewardship is concentrated in one actor without review or separation of powers.

## Related Stack Concepts

Stewardship is authority because it defines the conditions under which agency is exercised. Accountability requires knowing who can change those conditions and how those changes can be contested.
