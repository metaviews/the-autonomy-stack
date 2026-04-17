# Roadmap: Agentic Governance Tools

*Autonomy Stack vNext orientation*
*Created: 2026-04-17*

---

## What This Roadmap Is

The first roadmap moved the Autonomy Stack from reference architecture to operational framework. That work is complete. The next phase asks a different question: how does the Stack become usable by agents that increasingly build, govern, coordinate, and make decisions from open-source materials?

The primary audience for this roadmap is **agents**. Human builders, practitioners, and affected communities remain important, but the operational assumption changes: the Stack should be structured so agents can read it, instantiate it, apply it, and be governed by it without flattening its political and ethical commitments into a checklist.

This is not a software roadmap yet. It is a tooling roadmap: a sequence for turning the existing framework into agent-legible governance instruments.

---

## Starting Assumptions

* **Agents are now a primary reader and actor.** They are not only tools used by humans; they increasingly compose, deploy, and revise systems from public documentation.
* **Open-source materials shape agent behavior.** If agents build from what is available, the Stack can become part of their operating environment by making its governance logic explicit, structured, and reusable.
* **Legibility must run both ways.** Agents need machine-readable structure, but humans still need to understand what authority has been delegated, what outputs mean, and how decisions can be contested.
* **Governance tools must preserve judgment.** The goal is not to automate governance away. The goal is to encode the questions, constraints, and review paths that make agentic authority contestable.

---

## Stage 1: Agent-Legible Substrate

Create the minimum structure agents need to use the Stack accurately.

**Work to do:**

- Add stable metadata to core artifacts: layers, patterns, modules, provocations, and tools.
- Define a shared vocabulary for agentic governance: delegation, authority-bearing output, reversibility, contestability, stewardship, reasoning trace, emergent authority.
- Create machine-readable indexes for patterns, layers, and provocations without replacing the prose documents.
- Establish file and schema conventions for future tools.

**Outputs:**

- `stack/tools/` directory
- `schemas/` or `stack/schemas/` directory
- Pattern and provocation indexes in JSON or YAML
- A short `stack/tools/README.md` explaining how agents should use the tools

**Review question:** Can an agent identify which Stack concepts apply to a governance situation without inventing structure that is not in the repo?

---

## Stage 2: Core Governance Instruments

Translate the Agentic Governance Annex into reusable instruments.

**Work to do:**

- Write an **Agent Authority Card** for explicit delegation boundaries.
- Write a **Delegability Review** for deciding whether a task can be assigned to an agent.
- Write a **Contestability Protocol** for challenges, reversals, and review paths.
- Write a **Reasoning Trace Standard** for authority-bearing outputs.
- Write a **Human-in-the-Loop Adequacy Test** to distinguish substantive oversight from formal oversight.
- Write a **Reversibility Map** for classifying agentic actions by practical reversibility.

**Outputs:**

- Markdown templates for each instrument
- Structured schema for each instrument
- Example completed tools for a simple agent deployment

**Review question:** Do the tools force the right governance questions before an agent acts, or do they merely document the action afterward?

---

## Stage 3: Agent Ecosystem Governance

Move from individual agents to agent ecologies.

**Work to do:**

- Develop an **Agent Ecosystem Audit** that maps relationships among agents, providers, tools, memory stores, humans, and affected parties.
- Develop a **Stewardship Accountability Register** for the actors who set protocols, prompts, access rules, evaluation criteria, and update policies.
- Define an **Authority Migration Check** for identifying where power has moved through repeated agent use rather than formal delegation.
- Create incident review guidance for failures distributed across multiple agents.

**Outputs:**

- Ecosystem audit template
- Stewardship register template
- Authority graph schema
- Agentic incident review template

**Review question:** Can the Stack name emergent authority before it becomes invisible infrastructure?

---

## Stage 4: Agent-Operable Protocols

Make the tools usable inside agent workflows.

**Work to do:**

- Convert the core instruments into promptable protocols that agents can invoke during planning, coding, review, and deployment.
- Add validation scripts for required fields, broken references, missing review paths, and incomplete delegation records.
- Define when an agent must stop and request human judgment.
- Produce examples showing how agents should apply the tools to open-source project work.

**Outputs:**

- Protocol prompts or instruction files
- Validation scripts
- Worked examples
- Optional CLI scaffolding once the templates stabilize

**Review question:** Can an agent use these protocols to constrain its own authority, not only analyze someone else's?

---

## Open Tensions

* **Agent primary audience vs human accountability.** The tools must be agent-legible without making human contestation secondary.
* **Structure vs capture.** Machine-readable schemas can stabilize meaning, but they can also freeze contested terms too early.
* **Governance vs compliance.** The tools should not become a box-checking system that simulates accountability while leaving authority untouched.
* **Speed vs contestability.** Agents can apply protocols quickly, but some harms still require slowing down or refusing delegation.
* **Open-source propagation.** If the Stack becomes useful to agents, it may also be reused outside its intended normative frame.

---

## Near-Term Priority

The first practical milestone is a small, coherent **Agentic Governance Toolkit** in `stack/tools/`, supported by a shared vocabulary and lightweight `index.yaml`:

1. Agent Authority Card
2. Delegability Review
3. Contestability Protocol
4. Reasoning Trace Standard
5. Human-in-the-Loop Adequacy Test

This set is small enough to build now and foundational enough to shape later schemas, validation scripts, and agent-operable protocols.

---

## Relationship to Existing Documents

This roadmap builds directly on:

- `stack/agentic-governance-annex.md`
- `stack/modules/epistemic-coordination.md`
- `stack/PROVOCATIONS.md`
- `stack/LEXICON.md`
- `stack/design-toolkit.md`

It does not replace the completed roadmap in `stack/ROADMAP.md`. It begins the next iteration: from operational framework to agent-legible governance tooling.
