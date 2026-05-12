---
proposal_id: PROP-2026-05-04-001
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Active Inference: A method for Phenotyping Agency in AI systems?"
source_url: https://arxiv.org/abs/2604.23278
source_date: 2026-04-25
searched_on: 2026-05-04
status: pending
---

## Summary
A new arxiv paper (April 25, 2026) by Wilson, Constant, Albarracin, Hinrichs, Moore, Polani, and Friston proposing active inference as a framework for "phenotyping" agency in AI systems. The paper offers a minimal definition of agency built from three criteria — intentionality (action grounded in beliefs and desires), rationality (normatively coherent action entailed by a world model), and explainability (action causally traceable to internal states) — and instantiates these as a partially observable Markov decision process under variational free-energy minimization. Using a canonical T-maze paradigm, they show how empowerment (channel capacity between actions and anticipated observations) serves as an operational metric distinguishing zero-, intermediate-, and high-agency phenotypes.

## Why This Matters for This Tradition
This is the freshest Friston-co-authored extension of active inference into the AI agency / alignment territory since the "Active Inference and Artificial Reasoning" paper (already in the wiki). It reframes the alignment-relevant question "is this AI system an agent?" as a *measurable phenotypic question* rather than a definitional one. The paper directly bridges Friston's clinical "computational phenotyping" tradition (used in computational psychiatry to characterize humans) with the AI agency debate — making this a methodologically reflexive use of active inference. It strengthens the wiki's account of how Friston's program is migrating from neuroscience into AI characterization without losing its variational core.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The proliferation of agentic AI has outpaced the conceptual tools needed to characterize agency in computational systems. Existing definitions (autonomy, goal-directedness) are too coarse to distinguish degrees or kinds of agency, and don't yield operational metrics.
  Resource: A three-criterion minimal definition of agency (intentionality, rationality, explainability) instantiated as a POMDP under expected-free-energy minimization, with empowerment (action–observation channel capacity) as the operational metric.
  Solution: A "computational phenotyping" methodology for AI agency — agency becomes a measurable, graded property along a spectrum (zero, intermediate, high) rather than a binary or discursive label, and the same variational framework that phenotypes humans in computational psychiatry phenotypes AI systems.
  Confidence: High
  Evidence: arxiv 2604.23278, T-maze experimental section showing empowerment-graded agency phenotypes.

PRS-CANDIDATE-02:
  Problem: AI systems can be trained on objectives that imitate goal-directed behavior without satisfying the structural conditions that would warrant calling them agents (i.e. without intentional-rational-explainable structure). How do we tell apart "behaviorally agent-like" systems from "structurally agent-like" systems?
  Resource: Empowerment as a structural-rather-than-behavioral metric — it measures the capacity of the agent's action policies to causally constrain anticipated observations, regardless of whether external behavior looks goal-directed.
  Solution: A way to dissolve the "looks like an agent" / "is an agent" ambiguity in AI systems by grounding the answer in the geometry of the agent's generative model, not in its behavioral output.
  Confidence: Medium-High
  Evidence: T-maze structural-manipulation experiments distinguishing behaviorally similar systems with different empowerment profiles.

## Cross-Tradition Signals

- **Hawkins (Thousand Brains / sensorimotor agency):** Phenotyping agency by structural conditions of the generative model maps directly onto Hawkins' "intelligence requires sensorimotor reference frames" thesis (FINDING-018a). Both programs converge on a structural rather than behavioral definition of agency. New CROSS candidate.
- **Levin (multi-scale agency):** Levin's "competent subunits making decisions" framework already invites a Friston-style phenotyping. The Wilson et al. method could be applied to bioelectrically-mediated cellular collectives — a testable bridge.
- **Wolfram (rulial-space cognition):** Wolfram's "AI's final form" as non-humanlike rulial-space exploration (PROP-2026-04-27-003) and Friston's empowerment metric are complementary — Friston gives the metric, Wolfram gives the substrate. A possible joint operationalization.
- **Stump / McGilchrist (agency and narrative):** Empowerment-as-channel-capacity is silent on whether the agency phenotype is narratively coherent, which is what Stump (PRS on biblical narratives) and McGilchrist (right-hemisphere participatory engagement) treat as essential. A useful contrast point.
