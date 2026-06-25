SEARCH-AGAINST-ASSUMPTION-354:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-354
  Original statement: "A retrospective-only confirmatory run on the pre-registering-commit ledger is ungameable-by-construction (past can't be steered by a future rule)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-354
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; coupled to REVISE-115; self-noted caveat retrospective != clean
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Garden of forking paths (Gelman & Loken 2013). - Even with fixed past data, the analyst's post-hoc choice of which test/subset to run reintroduces multiplicity and bias; 'fixed data' is not 'fixed analysis'.
    2. Selection on the dependent variable (Geddes 1990). - Retrospectively choosing what to analyze in a fixed record biases inference.
    3. Leakage/anticipation: if the logged behavior was produced by agents that anticipated future evaluation, the ledger is not exogenous.

  Strength of challenge: Moderate

  Summary: The 'ungameable-by-construction' claim is the part that is challenged. While the PAST DATA cannot be steered by a future rule, the ANALYSIS is not fixed: choosing which retrospective slice/test to run on the ledger is a live researcher degree of freedom (garden of forking paths), and selection on outcomes can bias a retrospective confirmatory run. Moreover, if the ledger's entries were generated under anticipation of audit, exogeneity fails. So the run is materially gameable through analysis-choice and anticipation, even though forward-steering of the data is closed.

  Specific risks: False confidence that a retrospective confirmatory result is bias-free, when analysis-selection or anticipation effects could be driving it.

  Mitigations available: Pre-register the retrospective analysis spec itself (which slice, which test, thresholds) BEFORE looking; pre-commit the full ledger scope; check for anticipation effects.

  STEELMAN:
    Item: ASSUMPTION-354
    Strongest counterargument: 'Ungameable-by-construction' conflates fixed data with fixed inference; the past cannot be steered, but the choice of what to test on the past can be, so a retrospective run is only as clean as its pre-committed analysis plan - which the assumption does not yet require.
    What would need to be true for C2A2 to be safe: The retrospective analysis (subset, statistic, thresholds) is itself pre-registered and the ledger scope is fixed before inspection.
    How to test: Have an independent party pre-register the analysis; compare to any analyst-chosen analysis for divergence.

  Search scope: Forking paths; selection on outcomes; exogeneity. Comprehensive.

  Recommendation: CHALLENGED
