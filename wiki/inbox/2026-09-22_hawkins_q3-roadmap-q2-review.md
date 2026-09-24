---
proposal_id: PROP-2026-09-22-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/07 - Q3 Roadmap and Q2 Review"
source_url: https://forum.thousandbrains.org/t/2026-07-q3-roadmap-and-q2-review/1159
source_date: 2026-07-14
searched_on: 2026-09-22
status: pending
---

## Summary
Viviane Clay reviews the Thousand Brains Project's Q2 2026 results against its stated open theory questions and names Q3 priorities. Q2 shipped the saliency policy and 2D Sensor Module into Monty, combined hypothesis channels, fixed compositional modeling and added a compositional-object and sticker dataset, upgraded the platform (MuJoCo, Python, simplified configuration, `tbp.teleop`), merged 180 PRs, published in *Neural Computation*, and hired a Developer Advocate. One research item — top-down connections / parent-to-child orientation — was **not started** and is carried forward. Q3 names attention and object-behavior modeling as the two open-theory priorities, and commits to a two-year TBP report.

## Why This Matters for This Tradition
This is the program's own quarterly self-audit, published openly, with a named unmet commitment left on the record rather than quietly dropped. For a tradition tracked by its track record — the MacIntyre criterion the whole C2A2 instrument is built around, and the criterion Levin states as *the* justification for a paradigm — a quarterly document that reports what the program said it would do, what it did, and what it failed to start is a higher-grade evidentiary artifact than any single result. It also dates the program's turn toward attention, which supplies the context for PROP-2026-09-22-001 and the two 2026/06 attention sessions already in the wiki.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: A research program's claim to progress is unfalsifiable if its goals are restated after the fact.
  Resource: A published quarterly review that scores the prior quarter against pre-stated open theory questions and records an unmet item explicitly — top-down connections / parent-to-child orientation "Not Started, Remains on the List for Next Quarter."
  Solution: The program supplies its own progress ledger, with failures carried forward under their original names rather than absorbed into the next quarter's framing.
  Confidence: High
  Evidence: Video chapter at 3:23; Q3 priorities list re-enters the same item at 11:43 ("Adding Top-Down Connections into Monty").

PRS-CANDIDATE-02:
  Problem: Compositional objects — objects made of other objects — were a standing gap in Monty's modeling capability.
  Resource: Compositional modeling fixes, a new compositional-object and sticker dataset integrated into the benchmark suite, and hypothesis-channel combination.
  Solution: Compositional modeling reported as "working well," with Q3 committing to V1 of compositionality-benefits figures — i.e., a quantitative claim about *what compositionality buys*, not only that it runs.
  Confidence: High
  Evidence: Chapters at 2:49, 3:00, 3:09, 3:30; Q3 priority at 11:23.

PRS-CANDIDATE-03:
  Problem: Attention had been an open theory question without a scheduled home in the roadmap.
  Resource: Q3 open-theory priorities naming attention first, with three research items attached: model-free segmentation for focus-until-recognized, model-based policies and attention for compositionality, and symmetry representations with child-parent relative orientations.
  Solution: Attention is promoted from brainstorm topic to scheduled research with defined deliverables — converting the 2026/06 sessions' open questions into dated commitments.
  Confidence: High
  Evidence: Chapters at 9:55, 10:15, 10:57, 11:15, 10:50.

PRS-CANDIDATE-04:
  Problem: An open research program that is hard to enter cannot recruit the outside contributors its progress depends on.
  Resource: Documentation brought current, future-work sections rewritten with beginner-friendly tasks explicitly labeled, `tbp.teleop` and `lazyconfigs` published, a new Developer Advocate hired, and 180 PRs merged across 17 repositories.
  Solution: Onramp construction treated as a first-class quarterly deliverable alongside theory — the program's reproduction mechanism made an explicit object of planning.
  Confidence: High
  Evidence: Chapters at 5:47, 6:30, 8:20, 8:34, 9:01, 9:09, 9:32.

## Cross-Tradition Signals
- **Levin** — The sharpest signal in this proposal, and it is methodological rather than substantive. Levin's stated criterion for a paradigm's justification is the research program it generates and that program's track record. This document is exactly that object, produced voluntarily and quarterly by a rival (non-neural-independent, resolutely biological-cortical) program. Recommend the Master agent treat it as a *template* question: which C2A2 traditions publish a comparable ledger, and which do not?
- **Wolfram** — Compositional objects built from reusable sub-objects, with parent-to-child relative orientation as the unsolved piece, is the reference-frame composition problem in the form nearest to Wolfram's spatial/rulial composition. The unmet top-down-connections item is where that bridge would have to be built.
- **Friston** — Attention promoted to top open-theory priority, carrying the prediction-error framing from PROP-2026-09-22-001 with it. The two programs now have their highest-priority theoretical work pointed at the same quantity.
- **C2A2 methodological note (→ Master agent)** — The forthcoming "Two-Year TBP Report, Summarizing the Last Two Years" (chapter 12:49) is a tradition writing its own maturity narrative at a known date. That is the artifact the accelerator/detector instrument most wants and least often gets. Flag it for monitoring; it is not yet published.
