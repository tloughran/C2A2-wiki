---
proposal_id: PROP-2026-07-27-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Intelligence from Learnable Novelty"
source_url: https://arxiv.org/abs/2607.18433
source_date: 2026-07-20
searched_on: 2026-07-27
status: pending
---

## Summary
Zhang & Levin propose "learnable novelty" as a single quantity underlying the many faces of intelligence (data compression in ML, universal computation in dynamical systems, adaptive behavior in agents). They diagnose two opposite failure modes as sharing one root error: novelty search (seek surprise) gets "transfixed by a noisy television screen," while the free-energy principle (avoid surprise) is "most content in a dark room." Both conflate the surprise a learner *can* convert into knowledge with the surprise it never can. Isolating the learnable part of information — learnable novelty — recovers the disparate projections of intelligence from one objective.

## Why This Matters for This Tradition
This is a formal, substrate-independent intelligence metric from Levin's group, directly in line with his search-efficiency and diverse-intelligence measures (cf. Chis-Ciure & Levin, "Cognition all the way down 2.0"). It gives the C2A2 program a candidate quantitative handle on "progress" that is neither pure exploration nor pure surprise-minimization.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Why do the two leading formal objectives for intelligence — novelty search and free-energy minimization — each fail (noisy-TV problem vs. dark-room problem)?
  Resource: The distinction between surprise that is *learnable* (convertible into knowledge) and surprise that is irreducibly unlearnable (noise).
  Solution: "Learnable novelty" — the learnable component of information — as a single objective that avoids both the noisy-TV trap and the dark-room trap, and from which compression, computation, and adaptive behavior all fall out as projections.
  Confidence: High
  Evidence: Abstract identifies the shared cause of both failures ("each objective treats as one quantity the surprise a learner can convert into knowledge and the surprise it never can") and claims learnable novelty "yields the seemingly disparate projections of intelligence."

PRS-CANDIDATE-02:
  Problem: Is there a substrate-agnostic measure of intelligence usable across biological, artificial, and hybrid agents?
  Resource: Learnable-novelty formalism (with accompanying implementation; code released).
  Solution: A unifying quantity that reconciles statistics/ML, dynamical-systems, and agent-based definitions of intelligence under one measure.
  Confidence: Medium
  Evidence: Abstract frames intelligence's "different names in different fields" as projections of one quantity; Levin-group program on diverse-intelligence metrics.

## Cross-Tradition Signals
- **Friston (FEP) — flag explicitly:** This paper is a direct, named critique-and-repair of the free-energy principle's dark-room problem. It proposes that FEP's surprise-avoidance is incomplete and that intelligence requires seeking *learnable* surprise. Highest-priority dispatch to the Friston Agent — a genuine cross-tradition tension/advance (does FEP already contain this via expected free energy / epistemic value, or is learnable novelty a real amendment?).
- **Hoffman / Hawkins:** "Learnable vs. unlearnable surprise" bears on interface-theory fitness payoffs and on cortical prediction-error prioritization.
- **C2A2 relevance:** Candidate metric for quantifying inter-tradition learning — a mature member entering a second tradition is maximizing learnable novelty, not raw surprise.
