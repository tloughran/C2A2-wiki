---
proposal_id: PROP-2026-08-26-005
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/06 - Brainstorming Around How Columns Work Together During Learning and Inference"
source_url: https://www.youtube.com/watch?v=9r3nOjWSKco
source_date: 2026-07-02
searched_on: 2026-08-26
status: pending
---

## Summary
In this recorded Thousand Brains Project research meeting, Jeff Hawkins presents a set of unsolved problems that appear the moment the theory moves from a single cortical column to many columns modeling the same object at once. He names four: the shared learning problem (how separate columns come to agree on one model), sharing pose during inference, columns moving on and off an object as the sensor travels, and combining permanent object models with temporary, situation-specific features. The team then works through candidate mechanisms, including whether object identity itself could anchor grid cells and whether an attentional area could be used to determine relative pose.

## Why This Matters for This Tradition
The Thousand Brains Theory's central claim is that intelligence arises from thousands of semi-independent columns voting, so the mechanics of how columns coordinate is the load-bearing joint of the whole program rather than an implementation detail. This session is Hawkins naming, out loud and unresolved, the specific coordination problems the theory has not yet solved — which makes it unusually useful evidence about where the research program actually stands.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: When many cortical columns sense the same object at once, how do they build and share a single coherent model rather than many disconnected ones — the "shared learning problem"?
  Resource: A four-part decomposition of multi-column coordination: shared learning, pose sharing during inference, columns moving on and off the object, and the combination of permanent models with temporary features.
  Solution: Hawkins proposes treating these as distinct problems with potentially distinct mechanisms rather than as one voting problem, and the team explores object identity as a possible anchoring signal for grid cells across columns.
  Confidence: Medium
  Evidence: Video description and chapter markers: "Jeff presents several problems that arise when we start going from one to multiple columns. They include the shared learning problem, sharing pose during inference, columns moving on and off the object, and combining permanent models with temporary features." Chapter at 3:33, "Problems Related to Multiple Columns Modeling The Same Object."

PRS-CANDIDATE-02:
  Problem: How does a column establish the pose of an object relative to itself during inference, when pose must be consistent across columns for voting to work?
  Resource: The proposal that an attentional area — a spatial region rather than a discrete sensed point — could supply the reference needed to determine relative pose.
  Solution: An attention-area-based route to relative pose, offered as a candidate mechanism under active discussion rather than a settled result.
  Confidence: Speculative
  Evidence: Chapter marker at 48:09, "Could Attention Area Be Used to Determine Relative Pose?" This is framed as an open question in a brainstorming session; no experimental result is reported. Assessed from the video's own description and chapter list — the full session audio was not transcribed for this proposal.

PRS-CANDIDATE-03:
  Problem: When should the system fork a new model rather than continue updating an existing one — the question of how object classes and model boundaries arise?
  Resource: The framing of class formation as a "forking" decision about when to create a new model.
  Solution: Identified as an open problem tied to the permanent-versus-temporary model distinction; no mechanism is settled in this session.
  Confidence: Speculative
  Evidence: Chapter marker at 1:12:57, "Problems Related to Classes and Forking Models (When Do We Create A New Model?)". Named as a problem, not resolved.

## Cross-Tradition Signals
- **Friston:** The pose-sharing and model-forking problems are recognizably the same questions active inference asks about how a generative model partitions the world and when it should expand its state space. Hawkins arrives at them from cortical anatomy rather than from a free-energy objective, so the two programs converge on shared problems from opposite starting points.
- **Levin:** The shared learning problem — many semi-independent units converging on one coherent model without a central controller — is structurally the same coordination question Levin asks of cells forming a body plan. Both traditions locate intelligence in the coordination layer rather than in the individual unit.
