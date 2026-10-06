---
proposal_id: PROP-2026-09-22-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/06 - Attentional Regions, Policies, and Prediction Error"
source_url: https://forum.thousandbrains.org/t/2026-06-attentional-regions-policies-and-prediction-error/1155
source_date: 2026-07-07
searched_on: 2026-09-22
status: pending
---

## Summary
Viviane Clay and Niels Leadholm work through how Monty could attend to *regions* of space rather than discrete points, and how attention relates to policies, gating of sensory input, and inter-column voting. The central open question they pose is whether prediction error — on both short and long timescales — could serve as the general framing that defines model-free policies in the first place. A community reply (Alex, 9 July) pushes back that attention is driven by non-cortical systems computing importance, and that recognizing a mug involves affordance memory, not shape matching — the "wire-frame mug" case.

## Why This Matters for This Tradition
The wiki already holds the two downstream sessions in this arc (PROP-2026-09-15-001 model-free segmentation, PROP-2026-09-15-002 visual saliency), but not this one, which is where the framing question is actually raised: what *defines* a model-free policy before any model exists to define it against. Attention was subsequently named a Q3 open-theory priority (see PROP-2026-09-22-002), so this session is the origin node of the program's current highest-priority theoretical thread.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Monty attends to discrete sensed points, but biological attention selects extended regions of space — and the theory has no account of what fixes an attentional area's shape or extent.
  Resource: The proposal that attentional areas are defined by a *set of cortical columns*, considered against the rival proposal that they are initially amorphous and then narrowed to a location.
  Solution: Two competing, distinguishable structural hypotheses about the substrate of an attended region, either of which would make "attention area" a derived rather than stipulated quantity.
  Confidence: Medium
  Evidence: Video chapters at 23:42 ("Are Attentional Areas Defined by a Set of Cortical Columns?") and 34:37 ("Are Attentional Areas Amorphous Followed by Narrowing Down Location?").

PRS-CANDIDATE-02:
  Problem: Model-free policies must be specified before a model exists, so they cannot be justified by reference to what the model predicts — a bootstrapping problem at the base of the sensorimotor loop.
  Resource: Prediction error, taken at both short and long timescales, proposed as the single general framing from which model-free policies could be derived.
  Solution: A candidate unification in which the same quantity that drives model-based hypothesis testing also grounds the pre-model policies, removing the need for a separate hand-specified policy vocabulary.
  Confidence: Speculative
  Evidence: Session description: "There are high-level questions about how model-free policies are defined in the first place, and whether prediction error (both in the long and short term) could be used as a general framing."

PRS-CANDIDATE-03:
  Problem: Monty leaves objects before recognizing them, which degrades object recognition.
  Resource: A "stay on object until recognized" policy, combined with gating of sensory input to attended regions.
  Solution: Attention reframed as an operational recognition aid rather than a phenomenological add-on — a policy whose success is measured directly in recognition accuracy.
  Confidence: High
  Evidence: Chapter at 40:03, "'Stay on Object until Recognized' Policies"; described in the session summary as a way "to help with object recognition."

PRS-CANDIDATE-04:
  Problem: Voting across columns requires that the voting columns share a location reference, but columns anchor their grid cells independently.
  Resource: The session's treatment of voting and grid-cell anchoring together (1:20:05), and the question of whether modeling with multiple columns rather than one makes attention *easier* rather than harder (52:29).
  Solution: An argument that the multi-column case may be the tractable one — that shared anchoring is what supplies the reference an attentional region needs, rather than an extra cost to be paid.
  Confidence: Medium
  Evidence: Chapter structure at 52:29 and 1:20:05.

## Cross-Tradition Signals
- **Friston** — Direct and strong. Prediction error proposed as the general framing for policy definition is, in Friston's vocabulary, expected free energy selecting a policy. Two programs converging on the same quantity from opposite starting points (TBP from cortical-column architecture, Friston from a variational principle). Recommend dispatch: the claim that short- *and* long-timescale prediction error jointly define model-free policies is close enough to active inference's policy selection that the Friston tradition should be given the chance to say whether it is the same result or a rival one.
- **Levin** — "Stay on object until recognized" is a goal-directed persistence policy stated at the level of the whole agent, with no model of the object yet in hand. This is structurally the same shape as Levin's setpoint-directed competencies in non-neural systems.
- **McGilchrist** — The community reply's wire-frame-mug case (shape matches, affordance does not, producing confusion or humour) is an attention-as-mode-of-relation argument arriving inside a computational-neuroscience thread. Worth flagging: McGilchrist's claim is that *what* you attend with determines what you find, which is the same objection Alex is raising against a purely visual-recognition account of attending to a mug.
- **Hoffman** — If attentional regions turn out to be defined by which columns are recruited rather than by anything in the sensed world, the attended region is an interface construct. Weak signal, but on the productive-tension axis already logged between these two traditions.
