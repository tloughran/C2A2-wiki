---
proposal_id: PROP-2026-09-01-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "07/2026 - ARC-AGI 3 Review and What Monty Would Need to Solve it"
source_url: https://forum.thousandbrains.org/t/07-2026-arc-agi-3-review-and-what-monty-would-need-to-solve-it/1181
source_date: 2026-08-26
searched_on: 2026-09-01
status: pending
---

## Summary
A Thousand Brains Project research session, presented by Viviane Clay with the TBP team, reviewing ARC-AGI-3 — an interactive benchmark that tests whether an agent can adapt to an unfamiliar task without language, external knowledge, or pre-trained solutions. The team audits Monty (the project's thousand-brains system) against the four components ARC-AGI-3 targets: exploration, modeling, goal-setting, and planning/execution. The session ends with an explicit list of what Monty is missing — causality, object segmentation, compositionality, goal inference — and a decision about whether ARC-AGI-3 is a useful prototyping environment for those features.

Note on provenance: this is a TBP team session led by Clay, not a solo Hawkins piece. The wiki has treated TBP research meetings as tradition-primary material before (PROP-2026-08-17-011/012, PROP-2026-08-26-005); this proposal follows that precedent.

## Why This Matters for This Tradition
This is the first source in the wiki where the thousand-brains program states, against an external benchmark it did not design, the specific capability gaps between its own system and general fluid intelligence. It converts an internal roadmap into a falsifiable scorecard.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The thousand-brains program has lacked an external, unsaturated benchmark that tests skill *acquisition* rather than accumulated skill, so claims about its advantage over deep learning have had no shared yardstick.
  Resource: ARC-AGI-3, an interactive benchmark scoring efficiency of adaptation to unseen environments across four components — exploration, modeling, goal-setting, planning/execution — with no language or pre-training permitted.
  Solution: The team adopts ARC-AGI-3 as a candidate prototyping environment and maps Monty's current capabilities onto its four required components, making the program's remaining gap explicit and measurable.
  Confidence: High
  Evidence: Session segments "ARC-AGI-3 Tests These Four Core Components," "How Does Monty Do on the Skills Required to Solve ARC-AGI-3?" (39:06) and "Is ARC-AGI 3 a Good Benchmark for Monty?" (1:18:50).

PRS-CANDIDATE-02:
  Problem: Monty models concrete 3D objects through sensorimotor exploration, but ARC-AGI-3 requires reasoning about abstract objects — what a key does, what counts as winning — inside a concrete 2D grid.
  Resource: The claim, internal to the thousand brains theory, that the same cortical algorithm over reference frames should apply to abstract as well as physical spaces.
  Solution: The team treats ARC-AGI-3 as a forcing function for the concrete-to-abstract transfer, and scopes prototyping around causality, dynamic compositionality, and forgetting mechanisms rather than around the benchmark score itself.
  Confidence: Medium
  Evidence: Segments "Discussion: 2D vs 3D Modeling" (58:11), "What's Missing in Monty to Solve ARC-AGI-3" (1:04:35), "Dynamic Compositionality & Forgetting Mechanisms" (1:38:44); forum reply by W_Foxalike (2026-08-28) naming the concrete-to-abstract leap as the theory's untested step.

PRS-CANDIDATE-03:
  Problem: A sensorimotor system that only recognizes objects cannot set its own goals; ARC-AGI-3 scores goal inference and curiosity-driven exploration.
  Resource: Learned reference-frame models used for planning, plus a discussion of goals, rewards, and curiosity as drivers of exploration policy.
  Solution: Proposes using Monty's learned models directly for planning and goal inference, i.e. treating the object model as a substrate for action selection rather than only for classification.
  Confidence: Medium
  Evidence: Segments "Using Learned Models for Planning & Goal Inference" (43:54) and "Goals, Rewards & Curiosity" (1:28:58).

## Cross-Tradition Signals
Strong contact with Friston: ARC-AGI-3's exploration/modeling/goal-setting decomposition is close to active inference's expected-free-energy split between epistemic and pragmatic value, and the "curiosity" discussion is the same quantity under a different name — a place where the two programs could be made to disagree rather than merely coexist. Contact with Levin in the goal-inference thread: both programs are pressing on where goal-directedness comes from in a system with no designer-specified reward. Contact with Wolfram in the 2D-vs-3D modeling debate, which is a question about what the substrate's native reference frame is. Also a C2A2-internal signal: the forum replies argue that the theory's real constraint is not evidence but resource concentration in the transformer lineage — a live case of a research program's track record being shaped by which paradigm holds the capital.
