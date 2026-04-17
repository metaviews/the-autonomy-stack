---
tool_id: agent-authority-card
title: Agent Authority Card
status: draft
primary_question: What authority is this agent exercising, and where are its limits?
applies_to:
  - agent deployment
  - agent task planning
  - delegated action review
related_layers:
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
  - L5 Knowledge & Intelligence
related_requirements:
  - Delegation must be explicit and bounded.
  - Stewardship is authority and must be accountable.
related_docs:
  - ../agentic-governance-annex.md
  - ../modules/epistemic-coordination.md
---

# Agent Authority Card

## Purpose

Use this tool to make delegated authority visible before an agent acts. It distinguishes permitted actions, prohibited actions, review needs, and accountability paths.

## When To Use

Use before an agent performs work that could shape decisions, alter shared materials, produce authoritative analysis, route attention, classify people or content, or trigger downstream action.

## Inputs

- Agent name or role
- Deployment context
- Proposed actions
- Available tools and permissions
- Human steward or reviewer
- Known affected parties

## Diagnostic Questions

- What is the agent being asked to do?
- Which actions are operational, epistemic, or participatory?
- What can the agent do without review?
- What requires human review before action?
- What is explicitly outside the agent's authority?
- What outputs may be mistaken for authoritative decisions?
- Who can halt, revise, or override the agent?
- What must be logged so authority can be examined later?

## Output Format

```yaml
agent_name:
deployment_context:
steward:
authority_type:
  operational:
  epistemic:
  participatory:
delegated_actions:
prohibited_actions:
human_review_required:
affected_parties:
logs_required:
override_path:
stop_conditions:
open_questions:
```

## Agent Use Protocol

Fill the card before acting. If a proposed action does not fit the delegated actions, prohibited actions, or human review categories, classify it as an open question and request review.

## Stop Conditions

- No steward or reviewer is identifiable.
- The agent can alter access, allocation, classification, or records without review.
- Affected parties are unclear but may exist.
- The agent cannot explain whether its action is operational, epistemic, or participatory.

## Related Stack Concepts

Delegation is not authorization. Stewardship is authority. Authority-bearing outputs require contestability and legibility.
