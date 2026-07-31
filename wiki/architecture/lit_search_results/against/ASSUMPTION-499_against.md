SEARCH-AGAINST-ASSUMPTION-499:
  Date searched: 2026-07-22
  Original item: ASSUMPTION-499
  Original statement: 15a and 15b, under full blocking, retrieved the same key sources on >=5 items — the first quantitative datum on 15a/15b correlation; independence is asserted, not engineered.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-499
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-21 evening sync (15c in-run self-measurement)
      15b: Searched for reasons the datum may not mean what it is taken to mean
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Condorcet / independence baseline reasoning (per arXiv:2605.29800). — High source overlap is only diagnostic of lost independence against an expected-overlap baseline for genuinely independent retrieval on the *same* claim; on a well-specified factual claim, independent searchers *should* converge on the same canonical sources. Overlap alone does not prove dependence.
    2. "When the Judge Changes, So Does the Measurement," arXiv:2607.08535. — Measurement of judge reliability is itself instrument-dependent; a self-measurement taken by the pipeline it evaluates inherits that instrument's biases.
    3. Metrology / self-flagged-instrument principle (cf. C2A2's own PRESUMPTION-508). — A datum produced by the same apparatus whose independence it evaluates has no external referent.

  Strength of challenge: Moderate (against the *interpretation*, not against the underlying concern)

  Summary: The challenge is not that correlated searchers are fine — the FOR evidence is strong that they are not — but that C2A2's specific datum ("same sources on >=5 items") is uncalibrated and possibly misread. On a sharply-specified claim, independent high-quality retrieval is *expected* to converge on the same authoritative sources; overlap is then a sign of quality, not of dependence. Without an expected-overlap baseline (PRESUMPTION-518, same batch), the >=5 figure cannot be classified as high or low, and it was measured by the very pipeline whose blocking it evaluates.

  Specific risks: If C2A2 treats raw source overlap as the independence metric without a baseline, it may either (a) falsely alarm on well-posed claims where convergence is correct, or (b) falsely reassure when overlap is low for spurious reasons.

  Mitigations available: Establish an expected-overlap baseline for genuinely independent retrieval before interpreting the figure; have overlap measured by an instrument external to 15a/15b; combine overlap with error-correlation (do they make the *same mistakes*, per the Nine-Judges construction) rather than source-identity alone.

  STEELMAN:
    Item: ASSUMPTION-499
    Strongest counterargument: "Same sources on >=5 items" is exactly what two competent independent searchers *should* produce for well-specified claims — the primary literature on a question is finite and canonical. Reading shared retrieval as lost independence conflates "converged because dependent" with "converged because correct." The load-bearing quantity is correlated *error* (same wrong conclusions), which source overlap does not measure.
    What would need to be true for C2A2 to be safe: An expected-overlap baseline and an error-correlation measure, both produced by an instrument external to 15a/15b.
    How to test: Compute source overlap AND conclusion-agreement-on-known-hard-items against a baseline of deliberately diversified retrieval.

  Recommendation: PARTIALLY-CHALLENGED
