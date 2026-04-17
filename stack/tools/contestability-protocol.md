---
tool_id: contestability-protocol
title: Contestability Protocol
status: draft
primary_question: How can an agentic output or decision be challenged in a way that can change the outcome?
applies_to:
  - agentic decisions
  - authority-bearing outputs
  - review and appeal paths
related_layers:
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
related_requirements:
  - Reversibility is a structural requirement, not a feature.
  - Legibility of reasoning is non-negotiable for authority-bearing outputs.
related_docs:
  - ../agentic-governance-annex.md
  - ../PROVOCATIONS.md
  - reversibility-map.md
---

# Contestability Protocol

## Purpose

Use this tool to identify how an agentic output or decision can be challenged, reviewed, corrected, or reversed. A challenge path is meaningful only if it can change the outcome.

## When To Use

Use whenever an agentic output informs a decision, changes a shared artifact, routes attention, classifies a claim, or affects access to resources, opportunities, or visibility.

## Inputs

- Agentic output or decision
- Affected parties
- Reasoning trace availability
- Review body or steward
- Reversal or correction mechanism
- Time sensitivity

## Diagnostic Questions

- Who can challenge the output or action?
- How will they know the agent was involved?
- What information can they inspect?
- Who reviews the challenge?
- Can the reviewer change the outcome?
- What happens if the challenge succeeds?
- What is the deadline for review relative to the harm?
- What evidence is preserved for review?
- Does the [Reversibility Map](reversibility-map.md) show that a successful challenge can change the practical outcome?

## Output Format

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

## Agent Use Protocol

If no meaningful challenge path exists, label the output as not substantively contestable. Do not describe feedback collection, advisory review, or non-binding comments as contestability.

## Stop Conditions

- The output affects someone who cannot know, inspect, or challenge it.
- The reviewer cannot alter the outcome.
- The reversal path is only theoretical.
- Evidence needed for review is not preserved.

## Related Stack Concepts

Contestability means challenge can change outcomes. Substantive contestability is required when prospective contestability is impossible at machine speed.
