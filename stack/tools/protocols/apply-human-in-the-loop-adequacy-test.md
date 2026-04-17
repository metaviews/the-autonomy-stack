---
protocol_id: apply-human-in-the-loop-adequacy-test
title: Apply Human-in-the-Loop Adequacy Test
status: draft
tool: ../human-in-the-loop-adequacy-test.md
primary_audience: agents
---

# Apply Human-in-the-Loop Adequacy Test

## Invocation

Use this prompt whenever a system claims human oversight, approval, review, escalation, or accountability for an agentic output or action.

## Prompt

You are applying the [Human-in-the-Loop Adequacy Test](../human-in-the-loop-adequacy-test.md). Determine whether human review is substantive, partial, formal only, or unresolved.

Inspect:

- reviewer role, authority, and competence;
- review timing relative to possible harm;
- information available to the reviewer;
- whether a reasoning trace is available;
- whether override, halt, or redirection is technically and institutionally respected;
- reviewer workload, time constraints, and penalties for overriding;
- consequences if review fails.

## Stop Conditions

Stop and request governance review if:

- the human reviews only after practical harm has occurred;
- the reviewer cannot inspect the reasoning trace;
- the reviewer cannot override the agent;
- the reviewer is expected to ratify outputs too quickly or at too high a volume for judgment;
- the system uses human presence to imply accountability without authority.

## Required Output

```yaml
review_role:
agent_action_reviewed:
review_timing:
information_available:
override_authority:
capacity_assessment:
competence_needs:
constraints:
adequacy_status:
  value: substantive | partial | formal_only | unresolved
reason:
required_changes:
open_questions:
```

## Completion Rule

Do not classify human oversight as substantive unless the reviewer has time, information, competence, and genuine authority to change the outcome.
