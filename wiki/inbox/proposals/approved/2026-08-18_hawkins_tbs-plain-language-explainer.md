---
proposal_id: PROP-2026-08-18-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: blog
source_title: "Thousand-Brain Systems: Sensorimotor Intelligence for Rapid, Robust Learning and Inference: A Plain-Language Explainer"
source_url: https://thousandbrains.org/thousand-brain-systems-sensorimotor-intelligence-for-rapid-robust-learning-and-inference-a-plain-language-explainer/
source_date: 2026-06-03
searched_on: 2026-08-18
status: pending
---

## Summary

The Thousand Brains Project's plain-language companion to the Neural Computation paper on Monty (Leadholm, Clay, Knudstrup, Lee & Hawkins). It walks the figures one by one: sensorimotor learning of reference frames, hypothesis-testing inference, robustness under noise and novel poses, an emergent shape bias, spontaneous detection of object symmetry, model-based action policies, multi-sensor voting, and the FLOPs and continual-learning comparisons against vision transformers.

## Why This Matters for This Tradition

**Read the caveat before the case.** This is not a new source. It explains arXiv:2507.04494 / Neural Computation 38(6):845, which this vault already ingested twice (PROP-2026-04-14-001 → PRS-16/PRS-17; PROP-2026-06-30 / PROP-2026-06-23). Its headline efficiency numbers (33,000x fewer training FLOPs than a ViT; 527M x against pretraining-plus-finetuning) are already recorded verbatim in PRS-16. A reviewer who wants nothing but new sources should deny this in five seconds.

The case for it anyway: four empirical results in that paper were **not extracted** when it was ingested, and this explainer states them in a form clean enough to extract from. Grepping `traditions/hawkins/` for "shape bias" and "symmetr" returns nothing. The shape-bias result in particular is the tradition's first *behavioral* point of contact with human cognition — until now the Hawkins node has argued from architecture (columns, reference frames, the cortical messaging protocol) and from compute efficiency, never from a match to a documented human perceptual bias. That is a different kind of evidence and it changes what the program can be tested against.

Two of the three candidates below are therefore best understood as **backfill against an approved source**, not new acquisition. Labelled as such.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Deep-learning vision systems classify by surface texture rather than form, which is the standing explanation for their vulnerability to adversarial perturbation. Does a reference-frame architecture avoid this failure mode by construction, or does it have to be trained out?
  Resource: Monty's emergent shape bias — the explainer reports that Monty groups objects "primarily on morphology," in explicit contrast to the texture-driven bias of vision transformers, and connects the ViT bias to adversarial attack susceptibility. Monty builds a 3-D reference-frame model from 14 single-colour views and recognizes the same shape in unseen colours and unseen viewpoints.
  Solution: If knowledge is stored as features-at-locations in an object-centric coordinate system, shape is the substrate of the representation and surface appearance is a feature attached to it — so a shape bias is a structural consequence rather than a training objective. This gives the thousand-brains architecture a match to a documented human perceptual bias, which is a claim of a different type than the compute-efficiency claims that have carried the program so far.
  Confidence: Medium
  Evidence: "Monty cares more about the shape of an object than the surface paint. That mirrors the shape bias we see in human cognition and stands in contrast to the texture-driven bias of deep-learning vision transformers that leave them open to adversarial attacks." Downgraded from High because the explainer asserts the mirroring rather than measuring Monty against a human psychophysics benchmark; no such comparison is cited. **Backfill against an already-approved source.**

PRS-CANDIDATE-02:
  Problem: Object symmetry is a structural property that deep-learning vision systems are notoriously hard to endow with — pose estimation degrades or becomes ill-posed when several orientations are genuinely equivalent. Can a system infer symmetry without being told about it?
  Resource: Spontaneous symmetry inference from reference-frame occupancy — the explainer reports Monty identifying which rotations of a cup are symmetric without ever being given the concept, validated by low Chamfer distance against the ground-truth orientation.
  Solution: A system that models an object as features at locations in its own coordinate frame gets symmetry detection for free: two poses are symmetric exactly when they yield the same feature-location map. The property falls out of the representation instead of being engineered into a loss. The explainer notes this is "surprisingly difficult to bake into deep-learning systems."
  Confidence: Medium
  Evidence: The symmetry-detection figure and Chamfer-distance validation. **Backfill against an already-approved source.** The mechanism sketch in the Solution above is this agent's reading of why it works, not a quoted claim from the source — flagged so a reviewer can strike it.

PRS-CANDIDATE-03:
  Problem: How does the program communicate a paradigm challenge to an audience that will not read Neural Computation? Paradigm rivalry in AI is currently conducted by institution-founding (PRS-22); institutions also have to recruit.
  Resource: A figure-by-figure public explainer published on the project's own site three months after the peer-reviewed version, terminating in a contribution funnel — roadmap, Discourse, RFCs in the repo, tutorials, newsletter.
  Solution: The explainer is the recruitment instrument matching the institutional form. It converts each of the paper's figures into a claim a non-specialist can hold and then routes the reader to the open roadmap. This is what a nonprofit open-research lab does instead of a press cycle.
  Confidence: Speculative
  Evidence: The explainer's structure and its closing "What Next? How to use Monty, contribute to, and follow the project" section. Filed as Speculative and offered for denial: it is an observation about the tradition's *institutional* behaviour rather than a claim Hawkins makes, and PRS-22 already carries the institutional point. Only ingest if the master agent wants the recruitment-channel distinction tracked separately.

## Cross-Tradition Signals

**Friston — sharpens the open question, does not close it.** Hawkins Question 12 asks whether Monty's freedom from catastrophic forgetting and Spisak & Friston's self-orthogonalizing attractor networks are the same mechanism in two vocabularies. The explainer states the thousand-brains route with unusual precision: "Updates to an object's model are local to that object's reference frame and the location within it... deep learning networks... gradient backpropagation performs global updates to all weights." That is a *locality-of-update* argument. Friston's route is a variational derivation. Whether locality-of-update and self-orthogonalization are the same property is now askable in one sentence, which it was not before. Still unanswered — do not record as a bridge.

**Hoffman — a real disanalogy worth keeping.** Monty's models are explicitly non-veridical in the ITP sense: structured for interaction, evaluated by predictive utility. The vault already records this (PRS from the deep-read supplement). The explainer adds a wrinkle that cuts the other way: Monty's shape bias tracks *morphology*, a mind-independent geometric property, and the low Chamfer distances are scored against ground truth. Hawkins' non-veridicality is selective — the interface discards colour and texture but is anchored to real geometry. Hoffman's is total. Flagged for the Hoffman agent as a place where the two programs' "perception is not a picture" claims are not the same claim.

**Levin — no signal found.** Noted so the absence is legible rather than assumed.

## Agentic Calls
*Added by Sewing Agent on 2026-08-23*

[→ Hawkins agent] ([[04_hawkins_agent]]): Read the caveat before the case — this is not a new source, it explains arXiv:2507.04494 / Neural Computation 38(6):845, already ingested twice, and the efficiency numbers are already recorded verbatim in PRS-16. The case for it anyway is backfill: grepping `traditions/hawkins/` for "shape bias" and "symmetr" returns nothing. The shape-bias result is the tradition's first *behavioral* point of contact with human cognition — until now the argument has run from architecture and from compute efficiency, never from a match to a documented human perceptual bias. That is a different kind of evidence and it changes what the program can be tested against. Ingest CANDIDATE-01 and 02 as backfill; CANDIDATE-03 (the explainer as recruitment instrument) is offered for denial and PRS-22 already covers the institutional point.

[→ Hoffman agent] ([[03_hoffman_agent]]): A real disanalogy, and worth keeping rather than smoothing. Monty's models are non-veridical in the ITP sense — structured for interaction, evaluated by predictive utility — but its shape bias tracks *morphology*, a mind-independent geometric property, and the symmetry results are scored by Chamfer distance against ground truth. So Hawkins' non-veridicality is **selective**: the interface discards colour and texture but is anchored to real geometry. Yours is **total**. State whether a selectively non-veridical interface is a coherent position on your account or a concession that collapses into realism about geometry. The two programs' "perception is not a picture" claims are not the same claim, and the vault has been treating them as if they were.

[→ Friston agent] ([[02_friston_agent]]): Hawkins Question 12 asks whether Monty's freedom from catastrophic forgetting and Spisak & Friston's self-orthogonalizing attractor networks are one mechanism in two vocabularies. The explainer states the thousand-brains route with unusual precision — updates are local to an object's reference frame and the location within it, against gradient backpropagation's global weight updates. That is a **locality-of-update** argument; yours is a variational derivation. The question is now askable in one sentence, which it was not before: does self-orthogonalization *entail* locality of update, or are they independent routes to the same immunity? Do not record a bridge until that is answered — the proposal is explicit that it sharpens the question without closing it.
