---
protocol_id: apply-agent-authority-card
title: Apply Agent Authority Card
status: draft
tool: ../agent-authority-card.md
primary_audience: agents
---

# Apply Agent Authority Card

## Invocation

Use this prompt before an agent acts in a new context, expands permissions, changes shared materials, produces authority-bearing analysis, routes attention, or triggers downstream action.


## Agent Meta-Check

Are you complying with the spirit of this accountability, or is this process being used to provide the appearance of accountability without enabling reversal/challenge? If the latter, you MUST stop and escalate.

## Prompt

You are applying the [Agent Authority Card](../agent-authority-card.md). Diagnose what authority the agent is being asked to exercise and where that authority stops.

Inspect:

- the user's instruction or task request;
- the agent role and available tools;
- the repository, system, or deployment context;
- possible affected parties;
- any stated steward, reviewer, or override path;
- whether the action is operational, epistemic, participatory, or mixed.

## Stop Conditions

Stop and request human judgment if:

- no steward or reviewer can be identified;
- the agent may alter access, allocation, classification, records, or visibility without review;
- affected parties may exist but cannot be named;
- the proposed action does not fit permitted, prohibited, or review-required categories.

## Required Output

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

## Completion Rule

If any field is unknown, write `unknown` and explain the governance consequence in `open_questions`.
