SEARCH-AGAINST-ASSUMPTION-347:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-347
  Original statement: "Three columns wired to differ by reference frame (not random seed) yield robustness; identical agents at temperature measure only stochastic variance"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-347
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the central design commitment of Pathway 31
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kuncheva & Whitaker 2003. 'Measures of Diversity in Classifier Ensembles.' Machine Learning. - The diversity-accuracy relationship is weak and inconsistent; manipulating an input 'axis' does not guarantee the error decorrelation needed for robustness.
    2. 'Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels' (arXiv 2025). - Nominally distinct LLM configurations show heavily correlated errors, so the EFFECTIVE diversity is far below the nominal column count.
    3. Hidden-clone / family-bias in model ensembles (arXiv 2026). - Ensembles built on a shared base exhibit shared failure modes, undercutting expected robustness.

  Strength of challenge: Moderate

  Summary: The principle is sound but its realization for C2A2 is not guaranteed. The challenge is not that diversity helps - it does - but that wiring columns to 'differ by reference frame' does NOT ensure their ERRORS decorrelate; if all three columns share a base model, their errors can remain strongly correlated and the ensemble degenerates toward a single distribution with inflated apparent agreement. Empirically, nominal diversity routinely overstates effective diversity. So 'reference-frame variation yields robustness' is conditional on a decorrelation that must be demonstrated, not assumed.

  Specific risks: C2A2 could read three correlated columns as a robust ensemble, over-trusting consensus and under-estimating uncertainty - the opposite of the intended robustness.

  Mitigations available: Measure inter-column error correlation directly; report EFFECTIVE number of independent votes; require base-model or strong prompt diversity before treating consensus as robust.

  STEELMAN:
    Item: ASSUMPTION-347
    Strongest counterargument: Even reference-frame-distinct columns drawn from one base model can share systematic errors; if those errors dominate, the ensemble measures correlated bias, not robustness, and is no better (and falsely more confident) than a single agent.
    What would need to be true for C2A2 to be safe: The three reference frames produce measurably decorrelated errors (low pairwise error correlation) on the target task.
    How to test: Run all three columns on a labeled benchmark; compute pairwise error correlation and the effective independent-vote count; compare ensemble vs best single column.

  Search scope: Ensemble diversity-accuracy limits; correlated-error in LLM panels. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED
