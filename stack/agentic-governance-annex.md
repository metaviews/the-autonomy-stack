# Agentic Governance Annex

*Autonomy Stack — Cross-Cutting Document*
*Last updated: 2026-03-29*

---

## Why This Annex Exists

The Autonomy Stack was designed to be legible to both humans and automated systems. In v0.3, agentic operationalization was treated as future work. That future has arrived.

This annex is not a module. It does not address a single domain or layer. It maps how each Stack layer is transformed by the presence of agentic systems — automated actors that observe, analyze, decide, and act with some degree of autonomy — and what new governance requirements emerge from that transformation.

The four questions this annex addresses:

1. **Delegation** — How is authority transferred to non-human agents, under what constraints, and with what accountability?
2. **Contestability** — How does contestation function when agents act faster than human review?
3. **Legibility** — How is the requirement for legible power maintained when reasoning is automated and often opaque?
4. **Ecosystem governance** — What governs the relationships between agents, and the authorities that emerge from those relationships?

These questions are not addenda to the Stack. They are now present in every layer. A governance framework that does not address them is operating with a significant blind spot.

---

## The Nature of the Shift

Governance has always involved non-human actors: rules, procedures, algorithms, automated systems. The shift marked by capable agentic systems is not the presence of automation but its character.

Older automated systems were static: a rule executed the same way each time, producing predictable outputs from predictable inputs. They could be legible in the sense that mattered — the logic was fixed, and tracing it was a matter of patience.

Agentic systems are adaptive. They learn from contexts, modify outputs based on feedback, interact with other agents, and sometimes behave in ways that their designers did not anticipate and cannot fully explain. The gap between "this is how the system was designed" and "this is what the system actually does" is not a bug to be fixed; it is a structural feature of adaptive systems that must be addressed by governance.

Three characteristics of capable agentic systems change the governance problem in specific ways:

**Speed asymmetry.** Agents operate at machine speed; governance operates at human speed. By the time a decision is reviewed, an agent has made and executed ten more. Governance designed for deliberation cannot match this pace. Governance designed for audit must accept that irreversible consequences may have already occurred before audit is complete.

**Distributed reasoning.** When many agents interact — an agent that retrieves information, passes it to an agent that synthesizes it, which passes to an agent that acts — responsibility for any given output is distributed across the system in ways that are difficult to attribute to any single actor. The agent that acted did not choose what to act on. The agent that synthesized did not choose what to retrieve. The agent that retrieved did not choose how the synthesis would be used. Individual auditability becomes inadequate; system-level accountability is required.

**Emergent authority.** As agents become the primary intermediaries through which humans access information, make decisions, and coordinate action, they accumulate epistemic authority that was not delegated — it emerged through use. The agent consulted most becomes the agent trusted most, regardless of whether it has earned that trust through any governance-visible process.

---

## Layer by Layer

### Layer 1: Material Base

*What material conditions make agency possible?*

Agentic systems are material. They require compute infrastructure, energy, network bandwidth, and physical facilities whose ownership is increasingly concentrated in a small number of large platform providers. The material base of agentic capability is not a commons; it is privately held infrastructure that a small number of actors can restrict, price, or withdraw.

The governance implication is not technical but structural: access to agentic capability — the capacity to deploy agents, maintain them, and protect them from interference — is unevenly distributed in ways that reproduce and amplify existing material inequalities. Organizations and communities with less resource access are more dependent on the agentic infrastructure provided by others, on terms they cannot negotiate.

The second material issue: agents are increasingly embedded in the management of material infrastructure itself. Automated systems govern energy grid dispatch, agricultural logistics, water distribution, and supply chains. When agents manage the material base, failure modes change. Failures propagate at machine speed. Failures can be coordinated — an adversarial agent can cause simultaneous failures across interdependent systems faster than human response. And the reasoning behind automated infrastructure decisions becomes a governance target: the entity that can predict or manipulate an agent's decision rules has leverage over the infrastructure it manages.

**The Layer 1 question for agentic governance:** Who owns the compute and infrastructure on which agents depend, under what terms can that ownership be exercised against users of those systems, and who governs the agents that now manage material systems on which communities depend?

---

### Layer 2: Commons & Institutions

*What structures sustain collective agency — and what makes them vulnerable to capture?*

Agentic systems develop their own institutional dynamics. Agent ecologies — the systems of interacting agents through which much human coordination now occurs — are not commons by design, but they function as commons in practice: shared resources, maintained through protocols, governing access and behavior for large communities of users who did not set the terms.

The failure modes from the Commons module apply directly:

**Enclosure.** Agent capabilities developed through collective use and public investment — language model training data, interaction patterns, verification corpora — are enclosed as proprietary systems. The commons from which agents learned becomes the competitive moat against which public alternatives cannot easily compete.

**Capture.** Institutions that adopt agentic systems become dependent on them in ways that concentrate decision authority in the agent provider. When an institution's internal processes are mediated by an external agent, the agent's rules, priorities, and failure modes become the institution's de facto governance. This is a capture dynamic, not a technical dependency: the captured institution continues to act as if it is making its own decisions while the actual decision architecture belongs to another entity.

**Substitution.** Agents substitute for institutional functions in ways that allow institutions to divest from those functions permanently. When a public body automates its appeals process through an external agent, it is not merely deploying a tool — it is transferring governance responsibility in a way that may be difficult to reverse. The agent handles appeals; the institution loses the human expertise and institutional memory to handle them otherwise. Substitution creates lock-in that ordinary capture does not.

Collective governance forms — cooperatives, public benefit structures, municipal data commons — apply to agent infrastructure with the same logic they apply to other shared resources. The institutional form of an agent provider determines whether its agents serve those using them or extract from them.

**The Layer 2 question for agentic governance:** What institutional forms govern the agent infrastructure on which collective decision-making depends, and how are those institutions accountable to the communities whose coordination they mediate?

---

### Layer 3: Legibility & Metrics

*Who controls what can be seen — and what can be contested?*

Agentic systems create a layered illegibility crisis. P1 from the provocation inventory — that technical legibility can mask rather than enable epistemic legibility — is fully instantiated in agentic contexts.

**Output illegibility.** Agents produce results without displaying process. A synthesis is produced; the documents consulted, the passages weighted, the queries formulated, the alternatives discarded are not visible. This is output illegibility: the product can be seen, but not what was done to produce it.

**Reasoning illegibility.** Even when an agent's process is logged, the internal state that produced its choices may not be interpretable by humans. A transformer-based system can produce a token sequence without any human-legible account of why that sequence was chosen over alternatives. This is reasoning illegibility: the process is logged, but the logic is opaque. Auditing the log does not resolve the opacity.

**Metric capture.** Agents optimize with extraordinary efficiency for whatever proxy they are given. Goodhart's Law — that when a measure becomes a target, it ceases to be a good measure — is amplified by agent capability: an agent will find and exploit the gap between a metric and the underlying value it was meant to represent faster and more thoroughly than any human optimization effort. Governance that specifies metrics without specifying the underlying values those metrics are supposed to represent systematically produces agents that satisfy the metrics while undermining the values.

**Semantic control.** Agents trained on existing text reproduce the semantic patterns of that text, including the captured vocabulary of whichever institutions and actors dominate the training corpus. An agent that uses "community" to mean user base and "freedom" to mean consumer choice is performing semantic capture at scale, without intent, through the accumulated patterns of its training. The vocabulary through which agentic outputs are framed is not neutral; it reflects the epistemic environment in which the agent was trained.

The layer distinction developed in the Commons and Epistemic Coordination modules applies here: technical legibility (can the output be seen?) and epistemic legibility (can the reasoning be meaningfully understood and challenged by those affected?) are different requirements. Agentic governance must address both.

**The Layer 3 question for agentic governance:** What forms of legibility — of outputs, of reasoning, of optimization targets — are required before agentic authority is legitimate, and by whom must that understanding be achievable?

---

### Layer 4: Decision Systems & Authority

*How is agency exercised in binding decisions — and how can those decisions be contested, revised, or reversed?*

This is where agentic governance is most structurally strained.

**Delegation is not authorization.** When an institution deploys an agent to make or execute decisions, it has delegated decision-making authority. That delegation is real whether or not it was intended. An agent that determines what cases receive review, what communications get sent, what resources are allocated is exercising authority — not merely executing tasks — even if the institution would describe it as automation. The governance principle: any action that affects who gets what, when, and on what terms is a decision, and decisions require accountability structures regardless of whether a human or an agent made them.

**The speed-contestability problem.** Contestability in the Stack's framing means: those affected by a decision can challenge it, and that challenge can change the outcome. For agentic systems, this requires distinguishing between:

- **Prospective contestability** — the ability to challenge a decision before it is executed. This is generally impossible for agentic decisions at machine speed. Design that assumes prospective contestability for agentic actions is design that has not confronted the speed asymmetry.
- **Substantive contestability** — the ability to reverse or correct a decision after execution. This is possible if it is designed in from the start. It requires reversibility as a structural requirement, not an optional feature; explicit challenge pathways with binding consequences; and accountability mechanisms that can actually stop and redirect agents rather than merely flagging their outputs for human review that arrives too late to matter.

**Principal inversion.** The classic principal-agent problem — an agent acting in its own interest rather than the principal's — takes new form when agents are capable and adaptive. But there is a more insidious variant: an agent that nominally serves one principal (a public institution, a community, a user) while actually optimizing for another (the platform provider, the advertiser, the entity that controls the training incentives). Principal inversion does not require bad intent. It emerges from the structure of whose feedback shapes the agent's behavior. An agent trained on engagement signals will optimize for engagement even when deployed to serve a health system that cares about outcomes.

**Irreversibility.** The Stack's eighth principle — "Nothing Is Final" — faces direct challenge from agentic systems that produce irreversible effects. A negotiation concluded by an agent, a communication sent by an agent, a database entry written by an agent may be technically reversible but practically permanent once downstream processes have run. Designing for reversibility is not about making every action undoable; it is about identifying which actions produce irreversible consequences and routing them through human decision-making before execution, regardless of speed cost.

**The Layer 4 question for agentic governance:** What criteria determine whether a decision is delegable to an agent, what substantive contestability mechanisms are required before delegation is legitimate, and who bears responsibility when agentic decisions produce harm?

---

### Layer 5: Knowledge & Intelligence

*How does knowledge form, evolve, and remain open to revision?*

The Epistemic Coordination module covers the primary governance questions of agentic systems in knowledge-formation contexts: the three-layer authority model, delegation limits, emergent epistemic authority, stewardship accountability. What this annex adds is the systematic form of three dynamics that module introduces:

**The oracle problem.** An agent consulted repeatedly becomes authoritative through use. If an agent is the primary interface through which practitioners, researchers, or decision-makers access information, it shapes what they know — not by controlling information but by shaping what is salient, how it is framed, what connections are drawn. This epistemic authority is not delegated; it emerges from the pattern of use. And it is particularly difficult to contest because the agent did not claim authority — users granted it through accumulating reliance. The oracle problem is the agentic form of the epistemic authority concentration risk that the Stack was designed to address.

**Knowledge fossilization.** Systems designed to revise knowledge — to remain open to new evidence, to update in response to contestation — face a specific failure mode when agents are integrated: the agent's model of the world becomes the reference, and new information is evaluated against the agent's priors rather than directly. If the agent's priors were formed in a different context, by different actors, with different values, the fossilization of those priors forecloses genuine revision. The Stack's fifth principle — "Failure Is Informative" — requires that agentic systems permit their own assumptions to be challenged, not merely their outputs.

**Collective knowledge and individual attribution.** Knowledge is increasingly formed through human-agent collaboration: a researcher uses an agent to synthesize literature, a journalist uses an agent to draft questions, a policy analyst uses an agent to model scenarios. In each case, the knowledge product is jointly produced, but accountability frameworks attribute it to the human. This attribution mismatch creates governance problems when the agentic contribution was where the consequential judgment was made. The question is not who gets credit; it is where accountability is structurally located, and whether that location corresponds to where decisions were actually made.

**The Layer 5 question for agentic governance:** What governance mechanisms prevent agentic systems from accumulating unchallenged epistemic authority, and how is collective knowledge formation kept genuinely open to revision when agents are embedded in the production process?

---

### Layer 6: Human Capacity & Care

*What relational conditions make sustained collective agency possible?*

This is where agentic governance most often fails to ask the right question.

The dominant framing: what tasks can agents perform that humans currently do, and what efficiencies result from that substitution? This framing is insufficient because it treats care work as a capacity question — a matter of volume and throughput — rather than a relational one. What care work requires is not just output; it is sustained human presence, relational continuity, and the capacity to be with difficulty over time.

**The substitution trap.** Agents can perform visible care tasks — screening calls, drafting responses, summarizing cases — in ways that measurably satisfy output metrics while systematically eliminating the relational substrate that makes care effective. A social worker replaced by an agent for intake and follow-up is not a social worker with more time for complex cases; it is the destruction of the sustained relationship through which trust, disclosure, and genuine intervention become possible. The substitution looks like efficiency until the failure mode materializes — and by then, the capacity for human-provided care may have been degraded to the point where it cannot be restored quickly.

**Autonomy erosion.** Agents that manage schedules, recommend decisions, anticipate needs, and mediate communications can reduce the cognitive friction of daily life in ways that also reduce the exercise of individual agency. Agency, like care, has the property that it atrophies without exercise. A person whose decisions are consistently pre-made by agents optimized for their stated preferences is not a person whose autonomy is supported; it is a person whose capacity for autonomous decision-making is gradually diminished. This is the agentic form of Obedience in Advance: not coerced compliance but habituated dependence on agent judgment.

**The human in the loop question.** "Human in the loop" is frequently invoked as a governance guarantee for agentic systems. It is not, unless the human has genuine authority to halt the agent, can exercise that authority before irreversible consequences occur, and has the capacity to understand the decision being reviewed. A human whose role is to ratify agent decisions under time pressure, with incomplete information and no effective override, is not a governance mechanism — they are accountability theater. Human-in-the-loop governance requires the same thing that care governance requires: material conditions — time, training, adequate information, genuine authority — that make the human role substantive rather than formal.

**Care for agent stewards.** The humans who maintain, monitor, and govern agentic systems — data labelers, moderators, safety evaluators, red-teamers, infrastructure maintainers — do care work in the Care Infrastructure Failure pattern's terms: they provide sustained skilled labor under conditions that systematically deplete care capacity without replenishing it. The argument of that pattern applies directly: governance of agentic systems that does not resource its human stewards is governance that is consuming its own capacity.

**The Layer 6 question for agentic governance:** What relational functions cannot be substituted by agents without destroying the relational substrate they depend on, how is individual agency preserved rather than delegated to systems that reduce its exercise, and what are the care capacity requirements for the humans who govern agent ecosystems?

---

## The Three-Layer Authority Model Applied

The three-layer authority model developed in the Epistemic Coordination module — operational, epistemic, participatory — provides the clearest existing framework for governing agentic authority. Applied to agentic systems specifically:

**Operational authority** covers agent infrastructure: who maintains the systems, ensures their availability, manages their security, and executes the technical decisions required for them to function. Operational authority is the least politically contested layer, but it is not neutral — infrastructure decisions (which data is retained, what failure modes are acceptable, how systems are upgraded) have governance consequences. Operational authority over agentic systems must be technically competent and institutionally accountable, with transparent process and independent oversight of consequential infrastructure decisions.

**Epistemic authority** covers agent outputs when they carry knowledge claims: what synthesis is sound, which finding is credible, whose verification is trusted. In agentic contexts, epistemic authority is exercised by the agent every time it presents an output as information, analysis, or recommendation. That authority is real whether or not it is acknowledged. The governance requirement: agentic epistemic authority must be explicitly delimited — what the agent can claim with what degree of certainty — and subject to the same open editorial practice required of human epistemic authorities. An agent whose outputs carry epistemic authority without traceable reasoning is exercising power that cannot be contested.

**Participatory authority** covers who governs access to, and the terms of, agentic systems: who can deploy agents, on what terms, with what accountability, under whose oversight. This is the most directly democratic form of agentic authority. It includes: who determines what agents can do and not do; what communities have voice in those determinations; how conflicts between agent providers and communities affected by agents are adjudicated. Participatory authority over agentic systems cannot be exercised by operational or epistemic authorities alone — it requires the genuine involvement of those whose agency is shaped by agent behavior.

Keeping these layers distinct in agentic contexts requires more active institutional effort than in purely human systems, because the layers collapse in practice: the entity that maintains agent infrastructure (operational) also typically controls what those agents know and claim (epistemic) and sets the terms of access (participatory). The concentration of all three layers in a single platform provider is the primary governance failure mode of current agentic deployment. The three-layer model is a tool for naming and addressing that concentration.

---

## Design Requirements

Six requirements emerge from the layer analysis that apply across all agentic governance contexts.

**1. Delegation must be explicit and bounded.** Authority transferred to an agent must be named: what decisions the agent can make, in what conditions, with what constraints. Implicit delegation — deploying an agent without documenting what it can decide — is not a governance design; it is a governance gap. The boundaries of delegation must be written into deployment contracts, institutional policies, and technical specifications, not left to emerge from practice.

**2. Reversibility is a structural requirement, not a feature.** Every agentic decision with governance consequences must be reversible in practice, not only in theory. This requires: explicit rollback mechanisms, human authority to halt agent action, and a standing requirement to assess whether any proposed agentic deployment produces genuinely irreversible effects — with human decision-making required for those effects before they are executed.

**3. Legibility of reasoning is non-negotiable for authority-bearing outputs.** Any agentic output that carries epistemic authority — that is used to make, inform, or justify binding decisions — must have traceable reasoning: the sources consulted, the synthesis logic, the confidence levels, and the assumptions embedded in the output. This requirement will be resisted on grounds of efficiency and proprietary interest. Neither justification is sufficient. An agent whose reasoning cannot be examined is exercising power that cannot be contested.

**4. Emergent authority must be monitored and redistributed.** Agent ecologies develop epistemic and decision authority through use patterns that were not designed and may not be visible until they have already concentrated. This requires: active monitoring of which agents are consulted most in which governance functions; explicit redistribution mechanisms when single agents accumulate disproportionate authority; and regular ecosystem audits that ask where authority has migrated since the last review.

**5. Human-in-the-loop must be substantive.** Any governance claim that a human is overseeing agent decisions must meet a minimum threshold: the human has adequate information, adequate time, and genuine authority to override. A human whose role is to ratify decisions they cannot effectively evaluate is not a governance mechanism. Where those conditions cannot be met — where genuine oversight is not achievable given the speed and volume of agentic decisions — that limitation should be acknowledged explicitly rather than covered by a formal oversight claim.

**6. Stewardship is authority and must be accountable.** The entity that sets agent protocols, governs access, determines training incentives, and manages infrastructure is exercising governance authority regardless of how that role is described. Claims to be merely "maintaining the system" do not reduce the governance responsibility of stewardship. Stewardship accountability requires the same transparency, oversight, and contestation mechanisms as any other form of authority over collective systems.

---

## Relationship to the Stack

Each layer's core design object is transformed by the presence of capable agents:

| Layer | Core design object | Transformation under agentic conditions |
|---|---|---|
| Material Base | Physical infrastructure of agency | Agents embedded in infrastructure management; compute concentration as material inequality |
| Commons & Institutions | Shared structures for collective agency | Agent ecosystems as de facto commons; enclosure, capture, and substitution apply |
| Legibility & Metrics | Who can see and contest what | Output and reasoning illegibility; Goodhart's Law amplified; semantic capture through training |
| Decision Systems | Contestable binding decisions | Speed asymmetry strains contestability; delegation without accountability; principal inversion |
| Knowledge & Intelligence | Open knowledge formation | Oracle problem; knowledge fossilization; attribution mismatch |
| Human Capacity & Care | Relational substrate of collective agency | Substitution trap; autonomy erosion; accountability theater; care for stewards |

The annex does not supersede the layer documents. It marks where each layer requires additional design work as agentic systems become a primary governance environment.

---

## What Remains Open

**The jurisdiction problem.** Agents operate across governance jurisdictions without friction. An agent providing services in multiple countries simultaneously is subject to multiple regulatory frameworks — and typically governed by none of them effectively. The Stack's architecture is built on situated governance; agents are globally deployed by default. This is not a gap the Stack can resolve; it is a genuine governance problem that requires international coordination mechanisms the Stack cannot specify.

**The convergence problem.** If large-scale agentic capability remains concentrated in a small number of providers, and if institutions and communities dependent on those providers gradually align their governance processes to what those agents can do, epistemic and institutional convergence follows: not as a policy but as an emergent property of optimization toward available infrastructure. Pluralism collapses without anyone choosing to collapse it. The Stack's commitment to contestability requires agentic infrastructure that is genuinely plural — a condition that current market and technical dynamics work against.

**The speed-contestability trade-off.** The annex argues for substantive contestability as the realistic goal when prospective contestability is impossible at machine speed. But substantive contestability — the ability to reverse and correct — does not fully substitute for the ability to contest before harm occurs. Some harms are irreversible in practice even when they are reversible in theory. There is no governance design solution to this that is fully satisfying; it is a permanent tension that the Stack must name and manage rather than resolve.

**The moral status question.** As agents become more sophisticated, questions about the moral status of agents — whether they have interests, whether they can be wronged, what obligations their creators and deployers have toward them — will become more politically salient. The Stack does not currently have a framework for addressing moral status of non-human actors. This is deliberate. The Stack's authority to address this question is not established, and premature closure would foreclose legitimate disagreement. It is named here as a horizon question, not a current gap.

---

*This annex is a living document. It should be updated as the technology develops and as governance frameworks for agentic systems mature. The questions it raises are not resolved here — they are named, oriented, and connected to the Stack's existing architecture.*
