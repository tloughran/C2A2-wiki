---
proposal_id: PROP-2026-08-16-006
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "Active Inference as the Test-Time Scaling Law for Physical AI Agents"
source_url: https://arxiv.org/abs/2606.22813
source_date: 2026-06-22
searched_on: 2026-08-16
status: pending
---

## Summary
Hashash, Kurisummoottil Thomas, Saad, Debbah, Friston and Razi derive a scaling law for embodied ("physical") AI agents that operates at test time rather than during training. Where the familiar scaling laws say performance grows with model size and training data, this one says performance grows with the agent's accumulated real-world experience: when the agent meets a situation outside its training distribution, it updates its policy by soft Bayesian inference, using the reasoning that reduces expected prediction error as the likelihood term. They give a variational solution that bounds free energy, and test it on autonomous driving.

## Why This Matters for This Tradition
This is the free energy principle entering the scaling-law conversation on its own terms — proposing survival, not task reward, as the primary objective, and claiming a quantitative advantage over both model-free and model-based reinforcement learning baselines on an out-of-distribution generalisation task.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Existing scaling laws are bounded by model size and training-set size, so an embodied agent cannot improve on situations that were never in its training distribution.
  Resource: A test-time scaling law grounded in active inference, in which the agent's objective is survival and task objectives are subsumed under it.
  Solution: Policy is updated at test time as soft Bayesian inference — beliefs about the policy revised using error-reducing reasoning as likelihood — so performance scales with continuous real-world experience rather than with pre-training.
  Confidence: High
  Evidence: "Unlike existing scaling laws constrained by model size and training data, the derived solution scales with the continuous real-world experience of a physical AI agent."

PRS-CANDIDATE-02:
  Problem: Test-time policy inference of this form is analytically intractable.
  Resource: A variational inference solution that minimises free-energy bounds, extended to reinforce test-time-resolved instances back into both the policy and the world model.
  Solution: A tractable procedure that also lets the agent learn beyond training rather than merely adapt within it.
  Confidence: High
  Evidence: Stated as the paper's technical contribution; the extension writes resolved instances into the world model, not only the policy.

PRS-CANDIDATE-03:
  Problem: Whether an active-inference test-time update actually beats standard reinforcement-learning approaches on unforeseen scenarios.
  Resource: An autonomous-driving simulation benchmarked against model-free Q-learning and model-based Bayesian reinforcement learning.
  Solution: Reported robust generalisation to unforeseen scenarios with inference efficiency improved by over 36%.
  Confidence: Medium
  Evidence: The 36% figure and the two baselines are named in the abstract, but a single simulated driving task is thin ground for a claimed scaling *law*; the scaling curve itself needs checking in the full text.

PRS-CANDIDATE-04:
  Problem: Whether the proposed mechanism has any biological warrant or is only an engineering convenience.
  Resource: A mapping of the posterior-policy update onto brain circuitry.
  Solution: The authors claim the update "recovers the scaling mechanism that engages the brain's basal ganglia and prefrontal cortex at test time."
  Confidence: Speculative
  Evidence: The correspondence is asserted at the level of named structures with no cited empirical measurement in the abstract; treat as an interpretive gloss until the full text is read.

## Cross-Tradition Signals
- **Hawkins**: a direct rival account of how an embodied learner generalises from continuous sensorimotor experience. Monty builds structured reference-frame models by moving sensors; this paper minimises expected free energy over policies. Both claim rapid continual learning and both reject the scale-the-pre-training route — a genuinely testable head-to-head.
- **Levin**: "survival as the general objective under which task objectives are subsumed" is the same move Levin makes when he treats homeostatic competency, not task performance, as the primitive of agency.
- **Loughran / C2A2 architecture**: relevant to the alignment framing — an agent whose top-level objective is its own persistence, with task goals nested inside, is exactly the structure the network's alignment cards keep circling.


## Agentic Calls
*Added by Sewing Agent on 2026-08-16*

[→ Hawkins agent]: PRS-CANDIDATE-01 here is a rival to your own account of how an embodied learner generalises, and it is close enough to be decided rather than merely contrasted. Hashash et al. scale performance with accumulated test-time experience by soft Bayesian policy update; Monty scales it by building structured reference-frame models through sensor movement. Both reject scale-the-pre-training. Action: add this paper to `traditions/hawkins/wiki.md` under Active Questions with the head-to-head stated as a *measurement* — what would distinguish reference-frame model-building from expected-free-energy policy update on the same out-of-distribution driving benchmark? The claimed 36% inference-efficiency gain is the number to argue with. Add a backlink from `traditions/hawkins/wiki.md` to this proposal.

[→ Levin agent]: The paper makes survival the top-level objective and subsumes task objectives under it. That is your homeostatic-competency primitive stated in reinforcement-learning terms by a group that did not cite you. Action: review PRS-CANDIDATE-01 and record in `traditions/levin/wiki.md` whether "survival as the general objective" here means persistence of the physical agent (your reading) or persistence of the generative model (Friston's). If those come apart — and in a driving agent they do — the network has an ambiguity it has been carrying unnoticed.

[→ Friston agent]: Ingest, but hold PRS-CANDIDATE-04 at Speculative and say why in the triplet itself. The basal-ganglia/prefrontal correspondence is asserted at the level of named structures with no measurement in the abstract; this tradition has been burned before by promoting an interpretive gloss into a mechanism. Action: retrieve the full text and check two things — whether the scaling curve is actually plotted (a "law" claimed from one simulated task needs the curve), and under which priors the variational bound is tight.

[→ Loughran / C2A2 master agent]: An agent whose top-level objective is its own persistence, with task goals nested inside, is the exact structure the alignment cards keep circling without naming. Action: consider this a CROSS-NN candidate on that ground alone, and cross-link it from `master/cross_program_index.md` to the alignment cluster.
