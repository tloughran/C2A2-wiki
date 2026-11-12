---
proposal_id: PROP-2026-11-10-001
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/09 - Averaging Pose Vectors Inside a Voxel"
source_url: https://github.com/thousandbrainsproject/tbp.monty/pull/1174
source_date: 2026-09-09
searched_on: 2026-11-10
status: pending
---

## Summary
At a Thousand Brains Project research meeting on 2026-09-09 (recording now posted to the TBP Brainstorming playlist as "2026/09 - Averaging Pose Vectors Inside a Voxel"), the team named an open problem: how to merge the pose information (surface normal plus two curvature directions) that Monty stores at each point of a learned object model, when several observations land in the same small cube of space (a "voxel"). The trigger was a bug found in the Monty code: two pose readings were being averaged number by number, which does not give a valid rotation. The linked pull request (#1174, "fix!: correctly merge new and previous pose vectors") records the stopgap the team agreed at that meeting and the open questions that remain.

## Why This Matters for This Tradition
In Hawkins' theory every cortical column stores objects as features at locations in a reference frame, with orientation attached. This item shows that storing orientation is not a solved detail: when a thin surface passes through one voxel its two sides point in opposite directions, and when the voxel is too coarse the stored orientation becomes undefined. That is a concrete limit on the "reference frame" resource the whole program rests on.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: When several pose observations fall in one voxel of a learned object model, how should they be combined so the result is still a valid orientation?
  Resource: The bug report in PR #1174: element-wise averaging `(next + prev) / 2` of rotation matrices does not preserve orthonormality. A histogram in the PR thread (one test run, `surf_agent_unsupervised_10simobj`) shows hypothesis-pose determinants spread from about 0 to 1, with some negative values, before the fix; a valid rotation has determinant exactly 1.
  Solution: Interim fix agreed at the 2026-09-09 research meeting: replace the faulty merge with a weighted `Rotation.mean()` (SciPy), weighted by how many observations each side represents. After the fix, the same run's determinants sit at 1.0 throughout. The PR states this is "no worse than the bug" and "leaves open the question of what we should be doing in the long term."
  Confidence: High (for the bug and the interim fix; stated directly in the PR thread)
  Evidence: PR #1174 comment by tristanls-tbp: "In today's (September 9, 2026) research meeting, we highlighted the open problem of how to correctly merge pose vectors inside a voxel."

PRS-CANDIDATE-02:
  Problem: Two different situations make the stored orientation in a voxel ambiguous: (a) a thin surface whose two faces pass through one voxel, giving opposite surface normals that cancel; (b) a voxel that is too large for the local curvature.
  Resource: Team discussion in the PR thread (Mounir): the existing "majority" trick handles case (a) only if the voxel is correctly sized; case (b) "relates more to the problem of how to scale the voxels, similar to the other problem of how to size the attention voxels dynamically (the one you identified in Rome)."
  Solution: None yet. The team separates the two cases and links (b) to the open problem of dynamic voxel sizing already raised for attention regions at the Rome Focus Week.
  Confidence: Medium (team discussion, not a stated result)
  Evidence: PR #1174 review comment on `orthonormal_pose_vectors` in `object_model_utils.py`.

PRS-CANDIDATE-03:
  Problem: What should the representation of pose prioritize when combining readings?
  Resource: A comparison in the thread (Lee): Monty's own method gives the surface normal priority, fits the first curvature direction to it, and derives the second by cross product; `Rotation.mean()` weights all three axes equally, so the two give slightly different answers (e.g. averaging identity with a 90-degree rotation).
  Solution: Proposed but not adopted: normalize how pose is represented everywhere in Monty (the flattened 9-number vector in object models versus the stacked 3x3 form in the Cortical Messaging Protocol), as a separate cleanup. A related latent bug was flagged: the boolean `pose_fully_defined` is also averaged, so False and True average to 0.5 and convert back to True.
  Confidence: Medium
  Evidence: PR #1174 comments by hlee9212 and nielsleadholm.

## Notes for the reviewer
- **Authorship:** this is Thousand Brains Project team work (GitHub handles ramyamounir, nielsleadholm, hlee9212, tristanls-tbp, jeremyshoemaker), not a statement by Jeff Hawkins himself. It fails the task's strict "FROM Hawkins himself" filter, but matches the precedent of earlier approved TBP forum and research-meeting proposals (e.g. PROP-2026-10-23-006). Deny if the filter should be read strictly.
- **Date:** the meeting was 2026-09-09, over 30 days ago; the recording appeared on the TBP Brainstorming playlist later (exact upload date not found). Admitted under "significant work not yet captured": no wiki file mentions it.
- **Video not watched.** The recording's content is inferred from the PR thread, which cites the meeting. The YouTube URL for the video was not found by search.
- **Two sibling recordings on the same playlist, not proposed (titles only, no retrievable content):** "2026/09 - Latency Mismatches" (likely related to the Q4 roadmap item "Inner LM Loop to Address Temporal Mismatches", already captured from PROP-2026-10-23-003) and "2026/09 - Exploring How Cortical Columns Handle Variations in Learned Object Models". Good targets for next week's run.

## Cross-Tradition Signals
- **Friston:** averaging conflicting observations into a single estimate is the precision-weighting problem of predictive processing; Monty's weighting by observation count is a crude precision weight. Whether orientation evidence should be combined on the rotation manifold rather than in flat coordinates is a shared technical question.
- **Wolfram:** the voxel-size dependence (what counts as "one place" depends on resolution) parallels coarse-graining choices in Wolfram's models, where observed structure depends on the observer's grain.
- **Hoffman:** a mild signal only. The stored orientation is a property of the model's chosen grain, not read off the object directly; one could read this as an interface-style point about representation. This is this agent's reading, not a claim in the source.

> [TRACKED-16: 2026-11-12] CHECK disposition recorded 2026-11-11 (no note supplied). Tracked by Agent 16 as WATCH-007. Status: AWAITING-HUMAN — Tom to state what the CHECK is for (see watch list for candidate readings). PR #1174 not verifiable this run (fetch refused; search found nothing).
