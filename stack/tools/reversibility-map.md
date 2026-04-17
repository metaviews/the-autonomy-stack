---
tool_id: reversibility-map
title: Reversibility Map
status: draft
primary_question: Can the effects of this agentic action be reversed in practice, on time, and by accountable actors?
applies_to:
  - agent actions
  - delegated tool use
  - authority-bearing outputs
  - rollback planning
related_layers:
  - L3 Legibility & Metrics
  - L4 Decision Systems & Authority
  - L6 Human Capacity & Care
related_requirements:
  - Reversibility is a structural requirement, not a feature.
  - Contestability must be able to change outcomes.
  - Human review must occur before irreversible harm when after-the-fact review is inadequate.
related_docs:
  - ../agentic-governance-annex.md
  - contestability-protocol.md
  - delegability-review.md
---

# Reversibility Map

## Purpose

Use this tool to classify whether an agentic action, output, or downstream effect can be reversed in practice. Reversibility is not the same as deletion, apology, or later review. A reversal must be timely, effective, authorized, and visible to affected parties.

## When To Use

Use before an agent changes shared state, publishes or routes an authority-bearing output, classifies a person or group, triggers downstream tools, alters access, affects resource allocation, or makes a recommendation likely to be followed.

## Inputs

- Proposed agent action or output
- Downstream systems or actors affected
- Affected parties
- Time sensitivity
- Error consequences
- Available logs and evidence
- Available rollback, correction, or appeal mechanism
- Human steward or reviewer with override authority

## Reversibility Classes

**Freely reversible:** The action can be undone quickly by the agent or steward, with no durable harm, no external dependency, and no loss of evidence.

**Conditionally reversible:** The action can be undone only if specified logs, permissions, timing, or human review conditions are present.

**Socially irreversible:** The technical state can be changed, but attention, reputation, trust, classification, or institutional memory may not return to the prior condition.

**Materially irreversible:** The action can produce loss, exclusion, bodily risk, resource depletion, legal exposure, or other effects that cannot be restored by rollback.

**Unknown reversibility:** The action's effects, dependencies, or affected parties are not sufficiently understood.

## Diagnostic Questions

- What exactly would need to be reversed?
- Who has authority to reverse it?
- How quickly must reversal occur to prevent harm?
- What evidence must be preserved for reversal or review?
- Which downstream systems may copy, cache, act on, or amplify the output?
- Would reversal be visible to affected parties?
- Would the affected party be restored to the prior practical condition?
- Are reputational, relational, legal, material, or care harms possible?
- Does rollback depend on a provider, platform, database, or institution outside the steward's control?
- If reversibility is unknown, what must be learned before delegation?

## Output Format

```yaml
action_or_output:
affected_parties:
downstream_dependencies:
reversibility_class:
  value: freely_reversible | conditionally_reversible | socially_irreversible | materially_irreversible | unknown_reversibility
reason:
required_evidence:
rollback_or_correction_mechanism:
authorized_reversal_actor:
reversal_deadline:
notice_to_affected_parties:
residual_harm_after_reversal:
required_constraints_before_action:
open_questions:
```

## Agent Use Protocol

Classify based on practical reversibility, not theoretical possibility. If an action is ambiguous between two classes, choose the less reversible class. Use the classification to constrain the [Delegability Review](delegability-review.md) and [Contestability Protocol](contestability-protocol.md).

## Stop Conditions

- Reversibility is unknown and the action may affect access, allocation, classification, safety, visibility, or rights.
- The reversal actor lacks authority, time, evidence, or technical ability to restore the prior condition.
- Affected parties cannot be notified that reversal or correction occurred.
- The action may create materially irreversible harm.
- The proposed rollback only removes a record while leaving downstream copies, decisions, or social effects intact.

## Related Stack Concepts

Reversibility is a condition for meaningful delegation and contestability. When an action cannot be reversed in practice, prospective review becomes more important than after-the-fact correction.
