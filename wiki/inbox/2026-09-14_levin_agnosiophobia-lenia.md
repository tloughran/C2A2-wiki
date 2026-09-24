---
proposal_id: PROP-2026-09-14-003
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Agnosiophobia in a virtual agent: behavioral and dynamical architecture in Lenia"
source_url: https://arxiv.org/abs/2605.30708
source_date: 2026-05-29
searched_on: 2026-09-14
status: pending
---

## Summary
Cool, Hartl, Levin and Petti place regions into a Lenia creature's environment from which no sensory information can be obtained — informational blind spots — and find that the creatures steer away from them. The authors name the behavior "agnosiophobia": avoidance of the unknowable. Nothing in the creature was designed to detect or avoid such regions. The authors argue the avoidance falls out of a more basic imperative: the creature changes heading in order to preserve its own morphology, and entering an information-void threatens that.

## Why This Matters for This Tradition
This is the Levin program's central move — read a goal off a system's behavior rather than off its architecture — applied to a substrate with no genome, no neurons, and no designed objective function. It also gives the "multi-scale competency" thesis a clean minimal case: a preference appears at the level of the whole creature that is present nowhere in the update rule.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Can a system exhibit an apparently epistemic preference — avoiding the unknowable — without any mechanism designed for that task?
  Resource: Lenia creatures plus experimentally introduced regions from which no sensory information is available.
  Solution: Yes. Creatures reliably avoid occluded regions despite having no explicit mechanism for the task; the behavior is emergent rather than engineered.
  Confidence: High
  Evidence: The authors introduce regions from which no sensory information is available and report that creatures tend to avoid them, terming this "agnosiophobia."

PRS-CANDIDATE-02:
  Problem: When a system displays a behavior, at what level does its actual goal sit?
  Resource: Dynamical analysis of the creature's heading changes and attractor structure under occlusion.
  Solution: The apparent goal (avoid the unknown) is subordinate to a deeper one (preserve morphology). Attributed goals should be read at the level where the attractor lives, not at the level of the observed behavior — a methodological result for the whole diverse-intelligence program.
  Confidence: Medium
  Evidence: The authors argue creatures take advantage of their freedom to change heading in order to achieve "a more fundamental goal: the preservation of their morphology."

## Cross-Tradition Signals
- **Friston / active inference** — strongest signal in this batch. Avoiding regions that yield no observations is, in active-inference terms, avoiding states with no epistemic affordance; but a strict FEP reading would predict the opposite pull, since uncertainty is what an epistemic agent is drawn to reduce. The paper's resolution — morphological self-preservation dominates — is a live test case where the two programs make *different* predictions about the same behavior. Recommend this to the Master agent as a candidate bridge, not a mere resonance.
- **Hoffman**: a creature whose behavior is organized around what it cannot perceive is a direct probe of interface theory — the "blind spot" is a property of the interface, and it has causal consequences for action.
- **Wolfram**: emergent goal-like structure in a continuous CA is computational irreducibility producing something we have no shorter description for than "it wants to keep its shape."

## Provenance Note
Confirmed by two independent searches. Also in the ALIFE 2026 proceedings (doi 10.1162/ISAL.a.1012) and listed on Levin's publications page. Note the title varies between sources: the arXiv listing has "behavioral," the proceedings listing has "behavioural" — same paper. Submitted to arXiv 2026-05-29; outside the 30-day window but not previously captured in the wiki, so proposed under the "significant work not yet captured" clause. Abstract-level reading only.
