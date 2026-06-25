SEARCH-AGAINST-ASSUMPTION-357:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-357
  Original statement: "Real synthesis often coins NEW vocabulary, so the shared-id test risks a false negative; an honest fix needs a contemporaneous derived_from lineage field"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-357
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; gates OPEN-091; instrument-before-trust
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: Partial

  Sources:
    1. (Weak) Much routine synthesis REUSES existing vocabulary rather than coining new terms, so shared-id tests catch a substantial share of real integration - the false-negative rate may be lower than feared.
    2. Provenance-field overhead (data-curation literature): manually maintained lineage fields are themselves error-prone and incompletely populated, adding a new failure mode.

  Strength of challenge: Weak

  Summary: Little challenges the assumption's core worry; the main counterpoints are that (a) not all synthesis coins new vocabulary, so the false-negative problem may be smaller than implied, and (b) the proposed remedy (a derived_from lineage field) introduces its own incompleteness/error as a manually maintained field. Neither refutes the assumption; they bound its magnitude and flag remedy cost.

  Specific risks: Over-investing in lineage instrumentation for a false-negative rate that may be modest; or trusting an incompletely-populated lineage field.

  Mitigations available: Measure the actual false-negative rate of the shared-id test before building heavy lineage machinery; validate lineage-field completeness.

  STEELMAN:
    Item: ASSUMPTION-357
    Strongest counterargument: If most real synthesis reuses existing identifiers, the shared-id test's false-negative rate may be low, and a costly lineage field could be premature; the worry, while valid, may be smaller than assumed.
    What would need to be true for C2A2 to be safe: The measured false-negative rate is high enough to justify the lineage field's maintenance cost.
    How to test: Hand-label a sample of known syntheses; measure how many the shared-id test misses.

  Search scope: Synthesis-vocabulary reuse; provenance-field cost. Adequate.

  Recommendation: NO-CHALLENGE-FOUND
