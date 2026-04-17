---
protocol_id: apply-stewardship-accountability-register
title: Apply Stewardship Accountability Register
status: draft
tool: ../stewardship-accountability-register.md
primary_audience: agents
---

# Apply Stewardship Accountability Register

## Invocation

Use this prompt after an ecosystem audit, before expanding agent permissions, when responsibility for an agentic system is unclear, or when a system claims accountability without naming who can change its rules.

## Prompt

You are applying the [Stewardship Accountability Register](../stewardship-accountability-register.md). Identify who governs the conditions under which agents act and whether those stewardship roles are accountable.

Inspect:

- the agent ecosystem or deployment;
- prompts, protocols, policies, and evaluation criteria;
- access, permission, memory, model, provider, and update rules;
- human review and escalation responsibilities;
- affected parties and contestation channels;
- which actors can alter behavior, data access, memory, evaluation, or review paths;
- where stewardship is concentrated, externalized, or unowned.

## Stop Conditions

Stop and request governance review if:

- no steward can be identified for prompts, protocols, access rules, memory, model choice, or escalation;
- a provider can change material behavior without notice, review, or contestability;
- affected parties cannot identify who is accountable for a contested outcome;
- human stewards are responsible for decisions they cannot inspect, halt, or reverse;
- stewardship is concentrated in one actor without review or separation of powers.

## Required Output

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

## Completion Rule

If a stewardship domain is unnamed or controlled only by an external provider, mark it explicitly in `unowned_decisions` or `externalized_stewardship_risks`.
