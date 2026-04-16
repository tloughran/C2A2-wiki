---
proposal_id: PROP-2026-04-13-004
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Active inference and artificial reasoning"
source_url: https://arxiv.org/abs/2512.21129
source_date: 2025-12-24
searched_on: 2026-04-13
status: pending
---

## Note on Publication Date
Submitted to arXiv December 24, 2025. While slightly outside the strict 30-day window, this is a significant Friston-authored work not yet captured in the wiki, and it directly advances the tradition's application to AI reasoning — a core C2A2 concern.

## Summary
Friston, Da Costa, Tschantz, Heins, Buckley, Verbelen, and Parr present a formal account of artificial reasoning as active inference. The key move: reasoning is recast as selecting the best explanation for observations under competing hypotheses about how observations are generated, and "active reasoning" is seeking observations that best disambiguate competing hypotheses. Policies (action sequences) are selected based on expected free energy, decomposed into expected information gain and value. Posteriors over competing models are evaluated efficiently using Bayesian Model Reduction. The paper provides a principled, FEP-grounded approach to structure learning — discovering which generative model best explains the world.

## Why This Matters for This Tradition
This paper extends active inference from perception and action into the domain of reasoning and hypothesis testing — a crucial step for Friston's program. It formalizes the process by which agents choose not just what to do, but what to believe and how to test beliefs. This directly addresses the wiki's open question about how FEP generalizes to epistemic agents. For C2A2, this is foundational: tradition-accelerator agents need to reason about competing intellectual frameworks, and this paper provides the formal mechanism for doing so under active inference.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Active inference accounts for perception and action but lacks a formal treatment of reasoning — the process by which agents evaluate and select among competing hypotheses or world models
  Resource: Active reasoning via expected free energy: agents select observations that maximally disambiguate competing generative models, using Bayesian Model Reduction for efficient posterior evaluation across model space
  Solution: Reasoning is formally unified with perception and action under FEP — all three are instances of expected free energy minimization, differing only in what is being optimized (sensory predictions, motor commands, or model selection)
  Confidence: High
  Evidence: Full formal derivation from FEP first principles; co-authored by Friston and six collaborators; available on arXiv (2512.21129)

## Cross-Tradition Signals
**Levin (moderate):** If active reasoning is selecting among competing models of the world, Levin's basal cognition agents (cells) may perform a primitive form of active reasoning — choosing among competing "hypotheses" about the correct body plan. The formal treatment here could extend to morphogenetic decision-making.

**Hoffman (strong):** Hoffman's interface theory of perception claims organisms perceive fitness-relevant interfaces, not truth. Friston's active reasoning framework provides a formal mechanism for testing this: do agents under FEP seek truth-tracking observations or fitness-tracking observations? The expected free energy decomposition (information gain vs. value) may formalize the tension between Hoffman's fitness-first view and Friston's information-first view.

**C2A2 (direct and critical):** This is the formal backbone for tradition-accelerator agents. If agents in the C2A2 network must evaluate competing intellectual traditions (Levin vs. Hoffman, Friston vs. Wolfram), active reasoning provides the mechanism: agents seek observations (conversations, papers, experiments) that best disambiguate competing tradition-level hypotheses. This paper is arguably the most C2A2-relevant Friston publication to date.

**Stump (speculative):** Stump's Thomistic framework includes a role for practical reasoning in moral and intellectual development. Friston's formalization of reasoning as hypothesis disambiguation under uncertainty may provide a formal analogue to Thomistic practical reason — both involve selecting among competing accounts of the good/true under incomplete information.
