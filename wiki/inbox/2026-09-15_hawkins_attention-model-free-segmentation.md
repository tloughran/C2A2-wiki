---
proposal_id: PROP-2026-09-15-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/06 - Attention and Model-Free Segmentation"
source_url: https://forum.thousandbrains.org/t/2026-06-attention-and-model-free-segmentation/1170
source_date: 2026-07-28
searched_on: 2026-09-15
status: pending
---

## Summary
Niels Leadholm and Scott Knudstrup present attention in Monty as an **area-based constraint** on where the system spends its resources — a structure explicitly distinct from a target pose, and distinct again from salience. Knudstrup shows early results applying model-free segmentation algorithms (flood-fill interacting with salience maps) to the Thousand Brains Project's compositional dataset. The meeting closes on a deliberately radical question: if attentional regions can up- and down-weight candidate movements directly, are target poses still needed at all?

## Why This Matters for This Tradition
The thousand brains theory has always required some mechanism that decides *which* part of the world a set of columns is currently modeling; without it, compositional objects (the classic example here is a logo printed on a mug) have no principled boundary. This session is the first captured instance of the team treating attention as its own first-class data structure in the architecture rather than a side effect of the motor policy — and of the team entertaining removal of target poses, a load-bearing construct in the published Monty design.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: A sensorimotor system with no notion of an attended region has no principled way to decide where one compositional object ends and its parts begin — a logo on a mug is simultaneously "a logo," "a mug," and "a mug with a logo."
  Resource: Attention modeled as a constraint-*area* — a spatial region, structurally different from a target pose and different again from a salience map — that multiple learning modules can each contribute to and refine.
  Solution: Attention up-scales or down-scales candidate target poses according to whether they fall inside the attended region, giving segmentation a model-based influence without requiring a pre-committed object boundary.
  Confidence: High
  Evidence: Chapter markers state "Attention Is a Constraint-Area, a Different Structure than Target Poses" (1:08), "Salience Is Different Than Attention" (2:30), "Multiple Learning Modules Can Each Define Their Own Locations to Refine the Attentional Area" (25:57), and "Attention Upscales and Downscales Target Poses Based on If the Target Pose Falls within the Region" (35:28).

PRS-CANDIDATE-02:
  Problem: Model-free segmentation (flood-fill, salience) is fast but object-blind; model-based recognition is object-aware but expensive and presupposes what is to be recognized. Neither alone segments a novel compositional scene.
  Resource: A hybrid pipeline in which model-free algorithms propose regions of interest from salience maps, while model-based policies supply the initial seed location without requiring sensor movement; Gestalt grouping principles are canvassed as candidate grouping priors.
  Solution: Early empirical results on the TBP compositional dataset comparing several segmentation algorithms live in-meeting, establishing a concrete baseline for the hybrid approach.
  Confidence: Medium
  Evidence: Post states Knudstrup "presented some early results on using model-free segmentation algorithms on our compositional dataset"; chapters "Live Demo: Comparing Different Algorithms" (6:33), "Gestalt Psychology Principles and Other Ideas on How to Group Things Together as One" (19:04), "Initial Seed Location Can Be Defined Without Moving Sensors in Model-Based Policies" (22:35). Results were described as early; no published numbers.

PRS-CANDIDATE-03:
  Problem: What should make a location *interesting* enough to attend to, in a system with no external reward signal?
  Resource: Prediction error repurposed as a curiosity signal driving attentional allocation.
  Solution: Proposed — unexplained sensory input pulls attention, which is also how a narrowing attentional region would be triggered when a model fails to account for what is sensed.
  Confidence: Speculative
  Evidence: Chapters "What Makes Something Interesting" (44:01) and "Prediction Error as a Curiosity Signal" (49:49). Post notes "discussion around the difficulty of how model-based signals might influence attention, particularly when unexpected sensory input occurs" — i.e. the mechanism was flagged as unresolved, not settled.

PRS-CANDIDATE-04:
  Problem: If attentional regions can themselves bias which movements happen, the target pose may be a redundant intermediate representation.
  Resource: The "radical idea" that target poses could be dropped entirely, tested against the neuroanatomical constraint of corticospinal monosynaptic connections.
  Solution: No resolution reached; the neuroanatomical question ("what are the corticospinal monosynaptic neurons doing if there is no target pose?") is posed as the discriminating test.
  Confidence: Speculative
  Evidence: Chapters "A Radical Idea: Are Target Poses Still Needed?" (51:59) and "Question and Discussion - What are the Corticospinal Monosynaptic Neurons Doing if There Is No Target Pose?" (1:04:23). This is an open brainstorm; TBP explicitly does not human-correct transcripts for brainstorming videos because the ideas "could be incorrect or rapidly outdated."

## Cross-Tradition Signals
- **[[02_friston_agent]] — strong.** "Prediction error as a curiosity signal" is, in active-inference vocabulary, epistemic value / expected information gain driving action selection. Friston's framework treats attention as precision-weighting of prediction errors; TBP is arriving at a structurally similar role for attention from cortical-anatomy constraints rather than from a variational free-energy derivation. Whether "attention as an area" and "attention as precision" are the same mechanism under two descriptions is a sharp, answerable cross-tradition question.
- **[[03_hoffman_agent]] — moderate.** Model-free segmentation is the engineering form of Hoffman's question about what counts as an object. The mug-and-logo case is an interface-boundary problem: which carving the system commits to is determined by usefulness to the agent, not by a fact about the scene.
- **[[05_mcgilchrist_agent]] — moderate.** Leadholm's reply in thread describes attention as *starting wide* and narrowing only when something goes unexplained (novel Chinese character vs. familiar word). That is close to McGilchrist's account of a broad contextual mode that yields to narrow focused attention on demand — but with the causal ordering stated explicitly and testably.
- **[[01_levin_agent]] — weak.** Multiple learning modules each defining locations that jointly refine one attended region is a collective-agency mechanism at the level of cortical columns.

Note on provenance: the substantive claims above are from the TBP announcement post and the team's own chapter markers. The video itself was not transcribed. Two community replies in the thread (an "attention as inhibition" proposal and a free-will aside) are reader speculation, not TBP positions, and are excluded from the triplets.
