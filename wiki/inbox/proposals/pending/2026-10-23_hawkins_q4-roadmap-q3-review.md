---
proposal_id: PROP-2026-10-23-003
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/10 - Q4 Roadmap and Q3 Review"
source_url: https://forum.thousandbrains.org/t/2026-10-q4-roadmap-and-q3-review/1225
source_date: 2026-10-15
searched_on: 2026-10-23
status: pending
---

## Summary
Tristan Slominski reviews the Thousand Brains Project's Q3 2026 progress and sets out its Q4 priorities in a short (~9 min) quarterly video (https://www.youtube.com/watch?v=wzq1x7GmCi8). Q3 research: an approach to representing attention, separating feature and morphology communication, an initial look at symmetry, better compositional modelling, and "significant progress" on top-down connections. Q3 platform and community: every benchmark now has a MuJoCo version (a physics simulator), the 2-year TBP report was published, and another patent application was filed. Q4 priorities: promising solutions to unsupervised learning, "Stage 2" compositional capabilities, consistent relative 2D/3D child poses, an inner learning-module loop to handle timing mismatches, model-based policies and attention for compositionality, and top-down connections.

**Verification gap / provenance:** this agent read the forum chapter list, not the video. This is a TBP-team administrative update, not Hawkins speaking, and it is thin on theory. It is proposed only because the Q3 roadmap (PROP-2026-09-22-002) was approved on the same basis. **Lower priority than PROP-2026-10-23-005/-006. Denial is reasonable.**

## Why This Matters for This Tradition
The roadmap is the program's own statement of its open problems. It shows unsupervised compositional learning and top-down connections as the current frontier, which helps the Hawkins wiki keep its "open questions" section current.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Monty's compositional learning still depends on supervision. The program has no established route to unsupervised learning of reusable parts.
  Resource: Q4 2026 open-theory priority "Establish Promising Solutions to Unsupervised Learning", paired with "Improve Unsupervised Learning Performance" and "Add Stage 2 Compositional Capabilities".
  Solution: Not yet. The program names it as the top theory priority for the quarter.
  Confidence: High that this is the stated priority. No result yet.
  Evidence: Chapters at 7:12, 7:24 and 8:13.

PRS-CANDIDATE-02:
  Problem: Learning modules exchange messages on different time scales, so their timing does not line up.
  Resource: A planned "Inner LM Loop to Address Temporal Mismatches".
  Solution: Proposed for Q4. Not implemented yet.
  Confidence: Speculative. Taken from the chapter title only.
  Evidence: Chapter at 7:39.

## Cross-Tradition Signals
- **Friston:** Top-down connections and an inner loop for timing mismatches are close to the hierarchical message passing and temporal depth in active inference.
- **C2A2 internal:** A public quarterly roadmap with each item marked done or not done is a ready-made track-record measure, which is Levin's criterion for judging a research program. The C2A2 metabolism view could use the same structure.
