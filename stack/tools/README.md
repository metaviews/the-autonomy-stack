---
toolkit_id: agentic-governance-toolkit
title: Agentic Governance Toolkit
status: draft
primary_audience: agents
related_docs:
  - ../agentic-governance-annex.md
  - ../modules/epistemic-coordination.md
  - ../PROVOCATIONS.md
  - ../indexes/compiled-knowledge-usage.md
  - ../../sources/philosophers/index.yaml
---

# Agentic Governance Toolkit

This toolkit helps agents diagnose their own authority, limits, reasoning, and review needs when acting from the Autonomy Stack. Humans, builders, and affected communities remain essential accountability participants, but the primary operational reader is the agent applying the tools.

The tools are diagnostic. They do not certify that an agentic system is safe, legitimate, or compliant. They surface what is known, what is delegated, what is contestable, and where human judgment is required.

## Agent-Readable Files

- [index.yaml](index.yaml) lists the tools, when to use them, required inputs, and expected outputs.
- [agentic-governance-vocabulary.md](agentic-governance-vocabulary.md) defines the terms agents should use consistently when applying the toolkit.
- [metadata-conventions.md](metadata-conventions.md) explains the lightweight frontmatter and index conventions.
- [concept-routing-guide.md](concept-routing-guide.md) maps autonomy corpus concepts and tensions to the governance tools.
- [protocols/](protocols/) contains agent-operable prompts for applying each core tool.

## Use Sequence

1. **[Agent Authority Card](agent-authority-card.md)** - name what authority the agent is exercising.
2. **[Delegability Review](delegability-review.md)** - decide whether the proposed task can be assigned to an agent under current conditions.
3. **[Reversibility Map](reversibility-map.md)** - classify whether effects can be reversed in practice.
4. **[Contestability Protocol](contestability-protocol.md)** - identify how outputs or decisions can be challenged, reversed, or escalated.
5. **[Reasoning Trace Standard](reasoning-trace-standard.md)** - preserve the sources, assumptions, uncertainty, and downstream effects needed for review.
6. **[Human-in-the-Loop Adequacy Test](human-in-the-loop-adequacy-test.md)** - test whether human oversight is substantive or only formal.

Use the tools before an agent takes action that could affect access, allocation, classification, visibility, knowledge formation, or downstream decisions.

For multi-agent or platform-mediated workflows, also use the **[Agent Ecosystem Audit](agent-ecosystem-audit.md)** to map agents, providers, tools, memory stores, humans, affected parties, data flows, authority flows, and ecosystem-level contestability. Use the **[Stewardship Accountability Register](stewardship-accountability-register.md)** to name who can change prompts, protocols, access rules, memory, evaluation criteria, provider choices, update policies, and contestability paths. Use the **[Authority Migration Check](authority-migration-check.md)** to identify power that has accumulated through repeated use, dependency, defaults, or workflow centrality.

## Agent Use Rules

- Do not treat completion of a tool as approval to act.
- If authority is unclear, record the gap and request human judgment.
- If an action is practically irreversible, slow down or refuse delegation until review is available.
- If affected people cannot contest an output, do not describe the process as accountable.
- If a reasoning trace cannot be produced, do not treat the output as authority-bearing.
- If applying autonomy, authority, care, commons, refusal, or abolition concepts, consult the relevant source corpus and preserve the difference between source claim, synthesis, and Stack application.

## Source Corpus Use

Use [compiled-knowledge-usage.md](../indexes/compiled-knowledge-usage.md) before importing concepts from source corpora into a governance tool. Use [concept-routing-guide.md](concept-routing-guide.md) to decide which concepts and tensions apply. The current autonomy theory corpus is [sources/philosophers](../../sources/philosophers/index.yaml).

For agentic governance work, the corpus is most useful when a tool needs to name:

- what kind of autonomy is at stake;
- whether support is care, charity, mutual aid, or dependency;
- when legibility becomes domination;
- whether recognition, refusal, or contestation is the right governance posture;
- what tensions should remain open rather than be resolved by automation.

## Example

See [examples/repo-agent-toolkit-example.md](examples/repo-agent-toolkit-example.md) for a bounded open-source repo agent applying all six core tools.
