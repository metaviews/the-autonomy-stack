---
tool_id: delegability-review
title: Delegability Review
status: draft
primary_question: Can this task be assigned to an agent under current governance conditions?
applies_to:
  - task assignment
  - automation review
  - agent planning
related_layers:
  - L4 Decision Systems & Authority
  - L6 Human Capacity & Care
related_requirements:
  - Delegation must be explicit and bounded.
  - Reversibility is a structural requirement, not a feature.
related_docs:
  - ../agentic-governance-annex.md
  - ../PROVOCATIONS.md
---

# Delegability Review

## Purpose

Use this tool to diagnose whether a task can be delegated to an agent, requires human gating, or should not be delegated under current conditions.

## When To Use

Use before assigning a new task type, expanding an agent's permissions, connecting tools that can change shared state, or allowing an agent output to influence binding decisions.

## Inputs

- Proposed task
- Expected output or action
- Consequences of error
- Reversibility conditions
- Available human review
- Affected parties

## Diagnostic Questions

- Does the task affect who gets what, when, or on what terms?
- Does it classify a person, group, claim, risk, priority, or eligibility status?
- Is the output likely to be treated as authoritative?
- Can harm be reversed in practice, not only in theory?
- Can affected parties know the agent was involved?
- Can a human reviewer understand and override the output?
- Does the task require value judgment, care judgment, or legitimacy judgment?
- Would delegation erode human capacity that the system still needs?

## Output Format

```yaml
task:
delegability_class:
  value: freely_delegable | conditionally_delegable | human_gated | not_delegable | unresolved
reason:
required_constraints:
required_human_review:
reversibility_assessment:
affected_parties:
open_questions:
```

## Agent Use Protocol

Classify conservatively. If a task is ambiguous between two classes, choose the more restrictive class and explain what evidence would change the classification.

## Stop Conditions

- The task may create irreversible harm.
- The task involves coercive authority, eligibility, access, sanctions, or public classification.
- No contestability path exists.
- Human review is claimed but the reviewer lacks time, context, or override authority.

## Related Stack Concepts

Delegation is not authorization. Reversibility is structural. Human-in-the-loop oversight must be substantive.
