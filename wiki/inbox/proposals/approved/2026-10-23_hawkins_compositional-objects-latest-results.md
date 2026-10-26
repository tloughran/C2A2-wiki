---
proposal_id: PROP-2026-10-23-005
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/09 - Latest Results on Learning and Inferring Compositional Objects"
source_url: https://forum.thousandbrains.org/t/2026-09-latest-results-on-learning-and-inferring-compositional-objects/1227
source_date: 2026-10-20
searched_on: 2026-10-23
status: pending
---

## Summary
Niels Leadholm of the Thousand Brains Project (TBP) presents recent results on teaching Monty to learn objects as *compositions* of reusable parts instead of as single "monolithic" models (main video: https://www.youtube.com/watch?v=DM6Q9skfCOc, ~1h36m; summary video: https://www.youtube.com/watch?v=pml2TROrAhA). The chapter list shows results for objects in one canonical pose and in random poses. It also covers the ingredients that made the results possible: adaptive hypotheses ("burst sampling"), low-dimensional (2D) models, model-free policies and segmentation, a heterarchical/hierarchical architecture, re-orienting to the surface, negative evidence in hypothesis testing, and correct reference-frame transforms during learning. It closes with open problems on the way to fully unsupervised compositional learning.

**Verification gap / provenance:** this agent read the forum announcement and chapter list, not the video. Leadholm presents. Whether Hawkins speaks in the discussion segments is unconfirmed. This is TBP-team work and fails the strict "from Hawkins himself" filter. It is proposed on the same basis as earlier TBP research-meeting items (e.g. PROP-2026-10-13-002). The reviewer may deny on that ground. No numbers are quoted because none appear on the page.

## Why This Matters for This Tradition
Compositionality is how Thousand Brains theory says hierarchy works ("hierarchy encodes composition, not abstraction", P20). This meeting is the first reported test of compositional against monolithic Monty on the same objects, so it is where that theoretical claim starts to meet evidence.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Does learning objects as compositions of reusable child models actually beat learning each object as one monolithic model, especially when objects appear in arbitrary poses?
  Resource: A head-to-head comparison of compositional and monolithic Monty setups, run in a canonical pose and in random poses, with burst sampling, model-free segmentation and a heterarchical LM architecture as the enabling ingredients.
  Solution: The announcement reports that compositional modelling lets Monty "recognize complex objects more efficiently". The magnitude is not stated on the page.
  Confidence: Medium. The direction is reported by the team, but the effect size was not verified by this agent.
  Evidence: Forum summary; chapters "Compositional vs. Monolithic Setup" (11:47), "Main Results: One Canonical Pose" (20:42), "Main Results: Random Object Poses" (25:32).

PRS-CANDIDATE-02:
  Problem: Model-based hypothesis testing cannot rule hypotheses out efficiently if it only accumulates positive evidence.
  Resource: "Hypothesis Testing - Enabling Negative Evidence", together with model-based hypothesis testing in the low-level and high-level LMs (LL-LM, HL-LM).
  Solution: Negative evidence is added as an explicit signal, so a column can eliminate candidates instead of only reinforcing them.
  Confidence: Speculative. Taken from chapter titles only.
  Evidence: Chapters at 1:07:31, 1:18:48 and 1:26:50.

PRS-CANDIDATE-03:
  Problem: Fully unsupervised compositional learning (no labels, no bounding boxes) is still unsolved. Examples are learning a logo without a bounding box and deciding when a part is "morphology" and when it is a "compositional child".
  Resource: An explicit open-problems list and discussion segments on each case.
  Solution: None yet. The team states this as the next frontier, and it matches the Q4 2026 priority "Establish Promising Solutions to Unsupervised Learning" (see PROP-2026-10-23-003).
  Confidence: High that this is the stated open problem. No solution is claimed.
  Evidence: Chapters at 51:31, 58:54, 1:30:55 and 1:32:55.

## Cross-Tradition Signals
- **Levin:** Reusable components assembled into larger wholes parallel Levin's modular morphogenesis, where competent sub-units are composed into higher-level goals.
- **Friston:** Using negative evidence in hypothesis testing is close to evidence accumulation and model comparison in active inference.
- **Hoffman:** The "morphology vs. compositional child" question asks when a part counts as its own object. It parallels the question of when conscious agents combine into a single larger agent.
- **C2A2 internal:** Compositional reuse is the design principle of the PRS-triplet network itself: traditions share sub-structures instead of duplicating them.
