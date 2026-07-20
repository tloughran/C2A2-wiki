---
proposal_id: PROP-2026-07-20-003
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Neural cellular automata: Applications to biology and beyond classical AI"
source_url: https://doi.org/10.1016/j.plrev.2025.11.010
source_date: 2026
searched_on: 2026-07-20
status: pending
---

## Summary
Hartl, Levin and Pio-Lopez review neural cellular automata (NCA) — cellular automata whose local update rule is a learned neural network — as a modelling substrate for morphogenesis, regeneration, and forms of intelligence that classical AI architectures do not capture. The review positions NCA as the computational counterpart of Levin's bioelectric collectives: many identical local agents, no central controller, robust large-scale target morphology.

## Why This Matters for This Tradition
This is the methodological spine of Levin's computational work, stated as a review rather than a single result. It matters for the wiki because it names *why* NCA and not standard deep learning: NCA natively exhibit the regenerative, anatomy-homeostatic behaviour Levin studies empirically, which makes them a candidate in-silico testbed for bioelectric hypotheses rather than a mere illustration.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Classical AI architectures (feedforward nets, transformers) have no natural account of regeneration, anatomical homeostasis, or goal-directed repair — the phenomena central to Levin's program.
  Resource: Neural cellular automata — learned local update rules over a lattice of identical agents, with no global controller.
  Solution: NCA as the appropriate computational model class for morphogenetic intelligence, supporting in-silico experiments on target-morphology setpoints.
  Confidence: High
  Evidence: The review is explicitly framed as applications "to biology and beyond classical AI."

PRS-CANDIDATE-02:
  Problem: Is Levin's "collective intelligence of cells" a substantive computational claim or a metaphor?
  Resource: The demonstrated ability of NCA to regenerate damaged target patterns from purely local rules.
  Solution: A constructive existence proof — local-rule collectives *do* exhibit repair toward a setpoint without a homunculus, discharging the objection that goal-directedness requires a central planner.
  Confidence: Medium
  Evidence: NCA regenerative behaviour is the review's central biological application.

## Cross-Tradition Signals
**Wolfram (Strong):** NCA is literally Wolfram's cellular-automata substrate with a learned rule. This is the tightest formal contact point between the Levin and Wolfram programs in the wiki so far — Wolfram asks what CA rules *can* generate; Levin asks which rules a living system *selects and maintains*. A bridge essay on "rule discovery vs. rule maintenance" looks well motivated.

**Hawkins (Medium):** many identical local units, no central controller, converging on a coherent global model — the structural parallel to cortical columns and the Thousand Brains thesis is close enough to be worth testing rather than merely noting.

**Friston (Medium):** an NCA converging on a target morphology is a candidate minimal instance of active inference in a non-neural substrate, which the Friston agent's watch-list names as a major cross-tradition signal.

**Note for dedup:** distinct from the already-captured "BraiNCA: brain-inspired neural cellular automata" (arXiv:2604.01932) — that is a primary result, this is the field-level review.
