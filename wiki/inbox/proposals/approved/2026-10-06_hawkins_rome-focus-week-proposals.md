---
proposal_id: PROP-2026-10-06-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "08/2026 - Project Proposals for the Rome Focus Week"
source_url: https://thousandbrains.org/learn/videos-and-podcasts/
source_date: 2026-09 (approx; video posted to TBP Brainstorming playlist after 2026-08-30; focus week reported as late September 2026)
searched_on: 2026-10-06
status: pending
---

## Summary
The Thousand Brains Project posted a research-meeting video laying out the team's project proposals for its Rome Focus Week, a week-long in-person hackathon. Per the project's own summary (quoted in search snippets of the TBP X account), the proposals were (a) unsupervised learning of unfamiliar objects, (b) connecting Monty to the ARC-AGI-3 benchmark, and (c) using symmetry and attention to improve recognition and exploration. Three teams then delivered: an ARC-AGI-3 integration, a brand-new attention-system prototype in Monty, and new methods to merge object models or split them into reusable parts.

**Provenance caveats (read before approving):** (1) The video itself was not watched; content comes from the TBP site's playlist listing plus search-result snippets of the TBP X account, which could not be fetched directly. (2) Hawkins' personal participation in this meeting is not verified — the source is the TBP team channel, accepted in past runs (e.g. PROP-2026-09-01-001, ARC-AGI-3 review) as material from Hawkins' research program. (3) No forum discussion thread exists yet, and no direct YouTube URL was retrievable, so `source_url` points to the TBP Videos page where the title is listed. A companion video, "Ideas on Implementing Attention in Monty" (listed as "2027/08", almost certainly a typo for 2026/08), was also found but is not proposed separately because its content could not be read; it continues the attention arc already in the wiki (PROP-2026-09-15-001, -09-22-001).

## Why This Matters for This Tradition
This is the first point at which three threads already in the wiki — the ARC-AGI-3 gap analysis (PROP-2026-09-01-001), the attention/saliency arc, and compositional object models — move from brainstorming to built prototypes. It marks the program's shift from "what Monty would need" to "what Monty now has," which is the kind of track-record evidence a research program is judged on.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The July ARC-AGI-3 review identified what Monty would need to tackle abstract, interactive reasoning tasks, but Monty had no connection to the benchmark, so the gap could not be measured.
  Resource: An ARC-AGI-3 integration built by one Rome Focus Week team.
  Solution: Monty can now be run against ARC-AGI-3, turning a theoretical gap analysis into an empirical test bed for sensorimotor-first reasoning.
  Confidence: Medium
  Evidence: TBP summary reports "an ARC-AGI-3 integration" as one of three focus-week results. No scores reported in what was readable.

PRS-CANDIDATE-02:
  Problem: Monty's attention infrastructure (the DefaultAttentionSystem: VoxelGrid, weight decay/merge, GoalFilter, WeightPooler) was functionally a no-op because nothing generated attention regions.
  Resource: A new attention-system prototype built during the focus week, alongside the docs' framing of attention as gating votes and inputs ("covert" attention via top-down feedback and lateral competition).
  Solution: A first working prototype of region-based attention in Monty, closing the gap between the attention theory sessions (June-July 2026) and running code.
  Confidence: Speculative
  Evidence: TBP summary: "a brand-new attention system prototype in Monty"; GitHub PR #1199 description notes the prior implementation was a no-op pending a generator of AttentionRegions. Whether the prototype is that generator is not confirmed.

PRS-CANDIDATE-03:
  Problem: Compositional objects require models that can be combined into wholes or decomposed into reusable parts, and Monty's per-object reference-frame models had no mechanism for either.
  Resource: New methods to merge object models or split them into reusable parts.
  Solution: A step toward the program's first milestone (unsupervised compositional models at scale) by making object models recombinable.
  Confidence: Speculative
  Evidence: TBP summary: "new ways to merge object models or split them into reusable parts." Method details not readable.

## Cross-Tradition Signals
- **Friston (active inference):** Attention as gating of votes and inputs by top-down feedback parallels precision-weighting of prediction errors in predictive coding. The earlier TBP session framing model-free policies via prediction error makes this link explicit.
- **Levin (substrate independence / collective intelligence):** Merging and splitting object models across learning modules is a modular-composition problem, analogous to how cell collectives merge and partition goal states.
- **Hoffman (interface theory):** Symmetry-aware recognition, where Monty learns that some orientations are indistinguishable, is a small worked case of a perceiver tracking only fitness-relevant distinctions rather than full structure.
