SEARCH-FOR-PRESUMPTION-285:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-285
  Original statement: [inferred] '16/16 logic validation' presumes the 16 cases cover the parser's input space; coverage adequacy undefended, and the fade bug shows logic-pass != visually working.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-285
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched test-count vs coverage adequacy and parser test design.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Zhu, Hall & May (1997) 'Software unit test coverage and adequacy' — a curated suite *can* be adequate if cases are chosen to cover the input partitions.
    2. Equivalence-partitioning / boundary-value literature — a small number of well-chosen cases can cover a parser's classes.
    3. C2A2-internal: 16 cases may have been chosen to cover the parser's known input classes.

  Strength of support: Weak

  Summary: A small, well-designed suite can be adequate if the 16 cases map onto the parser's input partitions. Support is weak because no coverage argument was given; adequacy is asserted by count, not demonstrated.

  Caveats: Conditional on the 16 cases being partition-designed, which is undefended.

  Recommendation: PARTIALLY-SUPPORTED
