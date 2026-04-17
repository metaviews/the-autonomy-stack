---
tool_id: human-in-the-loop-adequacy-test
title: Human-in-the-Loop Adequacy Test
status: draft
primary_question: Is human oversight substantive, or only formal?
applies_to:
  - review workflows
  - agent supervision
  - override design
related_layers:
  - L4 Decision Systems & Authority
  - L6 Human Capacity & Care
related_requirements:
  - Human-in-the-loop must be substantive.
  - Stewardship is authority and must be accountable.
related_docs:
  - ../agentic-governance-annex.md
  - ../modules/care-based-infrastructure.md
---

# Human-in-the-Loop Adequacy Test

## Purpose

Use this tool to determine whether a human review role has real authority, capacity, and information, or whether it only provides the appearance of accountability.

## When To Use

Use whenever an agentic system claims human oversight, human approval, human review, human escalation, or human accountability.

## Inputs

- Human reviewer role
- Agent output or action
- Review timing
- Information available to reviewer
- Override mechanism
- Workload and time constraints
- Consequences of missed review

## Diagnostic Questions

- Does the human review before irreversible effects occur?
- Does the human have enough time to review?
- Does the human have enough context to understand the output?
- Can the human inspect the reasoning trace?
- Can the human override, halt, or redirect the agent?
- Is override respected by the system?
- Is the human penalized or overburdened for overriding?
- Does the reviewer have the domain competence required?
- Is the review role resourced as governance work?

## Output Format

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

## Agent Use Protocol

Do not treat human involvement as a safeguard unless the reviewer has time, information, competence, and genuine authority to change the outcome.

## Stop Conditions

- The human reviews only after practical harm has occurred.
- The reviewer cannot inspect the reasoning trace.
- The reviewer cannot override the agent.
- The reviewer is expected to ratify outputs at a volume or speed that prevents judgment.

## Related Stack Concepts

Human-in-the-loop can become accountability theater. Care capacity is part of governance capacity.
