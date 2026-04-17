---
tool_doc_id: agentic-governance-vocabulary
title: Agentic Governance Vocabulary
status: draft
primary_audience: agents
related_docs:
  - ../agentic-governance-annex.md
  - ../LEXICON.md
  - README.md
---

# Agentic Governance Vocabulary

This vocabulary defines terms the toolkit uses repeatedly. It is narrower than the main Stack lexicon: its purpose is to help agents apply the tools consistently while preserving the political and ethical meaning of the terms.

## Authority-Bearing Output

An agent output that is likely to shape a decision, justify action, classify a person or claim, route attention, allocate priority, or be treated as reliable knowledge. An output can be authority-bearing even if it is framed as a draft, summary, recommendation, or technical artifact.

*Use when:* deciding whether a reasoning trace, contestability path, or human review is required.

## Delegation

The transfer of action, judgment, or decision capacity to an agent. Delegation is real when the agent's output changes what happens next, even if no one formally names it as authority.

*Use when:* filling an Agent Authority Card or reviewing whether a task can be assigned to an agent.

## Delegability

The degree to which a task can be assigned to an agent under current governance conditions. Delegability depends on consequence, reversibility, contestability, review capacity, and whether the task requires value, care, or legitimacy judgment.

*Use when:* classifying a task as freely delegable, conditionally delegable, human-gated, not delegable, or unresolved.

## Contestability

The ability to challenge an output or decision in a way that can change the outcome. Feedback, comments, or advisory review are not contestability unless they can alter, halt, reverse, or correct the action.

*Use when:* deciding whether an affected party or reviewer has a meaningful challenge path.

## Prospective Contestability

The ability to challenge a decision before it is executed. Agentic systems often strain or eliminate this because they operate at machine speed.

*Use when:* identifying whether review must happen before an action, especially when harm may be irreversible.

## Substantive Contestability

The ability to reverse, correct, or otherwise change an outcome after an agentic action has occurred. It is weaker than prospective contestability, but often the realistic minimum for fast agentic systems.

*Use when:* designing rollback, correction, appeal, or escalation paths.

## Reasoning Trace

The review record for an agent output: task instruction, sources consulted, unavailable or excluded sources, tools used, assumptions, uncertainty, confidence or status, final output, and downstream effects.

*Use when:* an output may carry epistemic or decision authority.

## Stewardship

The authority exercised by those who maintain agent infrastructure, set prompts or protocols, choose models, govern access, define evaluation criteria, manage memory, or determine update policies. Stewardship is governance, not neutral maintenance.

*Use when:* identifying who can alter the conditions under which agents act.

## Emergent Authority

Authority that develops through repeated use, dependency, or centrality in an agent ecosystem rather than through formal delegation. The agent most consulted can become the agent most trusted without a governance-visible process.

*Use when:* auditing agent ecologies, dependency patterns, or authority migration.

## Practical Reversibility

The degree to which an action can be undone in the world, not only in a system record. A database edit may be technically reversible while its social, legal, financial, or relational consequences remain difficult or impossible to repair.

*Use when:* evaluating whether delegation is acceptable or whether human review must happen before action.

## Human-in-the-Loop

A claimed oversight arrangement in which a human reviews, approves, or can intervene in agentic action. It is substantive only when the human has adequate time, information, competence, and authority to change the outcome.

*Use when:* testing whether human review is real or only formal.

## Accountability Theater

The appearance of accountability without the capacity to alter outcomes, inspect reasoning, assign responsibility, or repair harm. Human-in-the-loop processes, dashboards, and review queues can become accountability theater when they lack authority or consequence.

*Use when:* a process documents activity but does not preserve contestability.

## Stop Condition

A condition under which an agent should halt, refuse delegation, request human judgment, or narrow its action. Stop conditions make limits operational before harm occurs.

*Use when:* converting governance principles into agent-operable constraints.
