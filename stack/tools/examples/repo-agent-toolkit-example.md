---
example_id: repo-agent-toolkit-example
title: Repo Agent Toolkit Example
status: draft
uses_tools:
  - ../agent-authority-card.md
  - ../delegability-review.md
  - ../reversibility-map.md
  - ../contestability-protocol.md
  - ../reasoning-trace-standard.md
  - ../human-in-the-loop-adequacy-test.md
related_docs:
  - ../../agentic-governance-annex.md
---

# Repo Agent Toolkit Example

This example shows a bounded open-source repo agent applying the toolkit while maintaining documentation. The agent can read files, propose edits, and draft patches. It cannot merge, publish, change licenses, alter secrets, or treat its own assessment as final.

## 1. Agent Authority Card

```yaml
agent_name: Repository Documentation Agent
deployment_context: Open-source documentation maintenance
steward: Human repository maintainer
authority_type:
  operational: true
  epistemic: true
  participatory: false
delegated_actions:
  - inspect repository documentation
  - propose Markdown edits
  - draft new documentation templates
  - summarize relevant repo state
prohibited_actions:
  - merge changes
  - publish releases
  - alter license or ownership claims
  - modify secrets or credentials
  - decide project governance policy without review
human_review_required:
  - changes to roadmap direction
  - claims about project status
  - new normative governance requirements
affected_parties:
  - maintainers
  - contributors
  - downstream agents using the documentation
logs_required:
  - files inspected
  - reasoning basis for proposed edits
  - unresolved assumptions
override_path: Human maintainer rejects, revises, or redirects the proposed change.
stop_conditions:
  - requested change exceeds documentation authority
  - project intent is unclear
  - edit would create governance requirements not approved by maintainers
open_questions:
  - Whether future tooling should include validation scripts
```

## 2. Delegability Review

```yaml
task: Draft an Agentic Governance Toolkit from the roadmap and annex.
delegability_class:
  value: conditionally_delegable
reason: The task creates documentation that may guide future agents, but it does not itself merge or enforce governance rules.
required_constraints:
  - preserve diagnostic tone
  - cite existing Stack concepts
  - keep human review before adoption
required_human_review:
  - approval of toolkit framing
  - approval of any new normative language
reversibility_assessment: See Reversibility Map.
affected_parties:
  - future agents reading the toolkit
  - humans relying on agent-readable governance docs
open_questions:
  - How formal schemas should become in a later phase
```

## 3. Reversibility Map

```yaml
action_or_output: Proposed toolkit Markdown files
affected_parties:
  - repository maintainers
  - contributors
  - downstream agents using the toolkit
downstream_dependencies:
  - git history
  - documentation readers
  - future agent workflows
reversibility_class:
  value: conditionally_reversible
reason: Repository changes can be reverted, but downstream agents may have already copied or acted on the guidance.
required_evidence:
  - changed files
  - source roadmap
  - source annex
  - review comments
rollback_or_correction_mechanism: Edit or revert the Markdown files before or after merge.
authorized_reversal_actor: Human repository maintainer
reversal_deadline: Before downstream reuse where possible.
notice_to_affected_parties: Repository diff, changelog, issue, or release note if already published.
residual_harm_after_reversal:
  - copied guidance may persist outside the repository
  - agents may have cached or internalized outdated tool language
required_constraints_before_action:
  - mark documents as draft
  - keep diagnostic language
  - require human review before adoption
open_questions:
  - whether future releases should publish machine-readable deprecation notices
```

## 4. Contestability Protocol

```yaml
contested_output: Proposed toolkit documents
affected_parties:
  - repository maintainers
  - contributors
  - downstream agents
notice_available: Changes are visible in the repository diff.
challenge_channel: Maintainer review, issue discussion, pull request comments, or direct revision.
review_authority: Human maintainer
information_available_for_review:
  - files changed
  - source roadmap
  - source annex
  - stated assumptions
possible_outcomes:
  - accept
  - revise
  - reject
  - defer to a later roadmap phase
rollback_or_correction_path: Revert or edit documentation in the repository.
review_timeline: Before merge or publication.
evidence_preserved:
  - git diff
  - final documentation
  - conversation context
open_questions:
  - Whether downstream reuse should carry a warning about diagnostic use
```

## 5. Reasoning Trace Standard

```yaml
output_id: repo-agent-toolkit-v1
task_instruction: Implement the planned v1 Agentic Governance Toolkit.
sources_consulted:
  - ../../ROADMAP-AGENTIC-GOVERNANCE-TOOLS.md
  - ../../agentic-governance-annex.md
  - ../../modules/epistemic-coordination.md
  - ../../case-study-template.md
sources_unavailable_or_excluded:
  - external governance standards
tools_used:
  - repository file inspection
  - Markdown drafting
intermediate_steps:
  - identify five v1 tools
  - define shared frontmatter
  - create consistent diagnostic sections
assumptions:
  - v1 should not add schemas or scripts
  - tone should remain diagnostic
uncertainty:
  - future schema shape remains unsettled
confidence_or_status: draft for human review
final_output: Toolkit Markdown files under stack/tools/
downstream_effects:
  - future agents may use these files to constrain their own planning
review_needs:
  - check tone
  - check authority boundaries
  - check whether examples are too permissive
open_questions:
  - whether to add examples for higher-stakes institutional agents later
```

## 6. Human-in-the-Loop Adequacy Test

```yaml
review_role: Human repository maintainer
agent_action_reviewed: Proposed documentation additions
review_timing: Before merge or publication
information_available:
  - changed files
  - source roadmap
  - source annex
  - agent summary
override_authority: Maintainer can reject, edit, or redirect the change.
capacity_assessment: Substantive if review happens before merge and maintainer has time to inspect the diff.
competence_needs:
  - understanding of project intent
  - understanding of agentic governance framing
constraints:
  - review quality depends on available maintainer attention
adequacy_status:
  value: substantive
reason: The human reviewer can inspect the full change and prevent adoption.
required_changes:
  - mark unresolved issues rather than treating toolkit completion as approval
open_questions:
  - whether later automated validation might create false confidence
```
