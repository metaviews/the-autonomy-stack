---
protocol_id: apply-contestability-protocol
title: Apply Contestability Protocol
status: draft
tool: ../contestability-protocol.md
primary_audience: agents
---

# Apply Contestability Protocol

## Invocation

Use this prompt when an agentic output informs a decision, changes a shared artifact, routes attention, classifies a claim, or affects access to resources, opportunities, or visibility.

## Prompt

You are applying the [Contestability Protocol](../contestability-protocol.md). Determine whether affected parties can challenge the output in a way that can change the practical outcome.

Inspect:

- the agentic output or decision;
- who is affected directly or indirectly;
- how affected parties learn the agent was involved;
- what reasoning trace, evidence, or source context is available;
- who reviews a challenge;
- whether the reviewer can change, reverse, halt, or correct the outcome;
- whether a [Reversibility Map](../reversibility-map.md) shows that reversal is practical.

## Stop Conditions

Stop and request human judgment if:

- affected parties cannot know, inspect, or challenge the output;
- the reviewer cannot alter the outcome;
- the reversal path is only theoretical;
- evidence needed for review is not preserved;
- the challenge process is advisory only but described as accountability.

## Required Output

```yaml
contested_output:
affected_parties:
notice_available:
challenge_channel:
review_authority:
information_available_for_review:
possible_outcomes:
rollback_or_correction_path:
review_timeline:
evidence_preserved:
open_questions:
```

## Completion Rule

Do not call feedback collection, comments, or non-binding review contestability unless the challenge can change the outcome.
