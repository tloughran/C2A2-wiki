SEARCH-AGAINST-PRESUMPTION-255:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-255
  Original statement: The per-tradition time model ("hour per top-3, half-hour per long-tail") presumes per-tradition processing time scales linearly with file count and is roughly uniform across traditions, but the 12 traditions span very different theoretical complexity.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-255
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on per-tradition complexity factors.
    Current status: CHALLENGED (Moderate — sustains the presumption)

  Sources:
    1. Boehm (1981) COCOMO II — software effort scales with both size AND complexity multipliers; complexity factors regularly add 2-4x to size-only estimates.
    2. Software-effort estimation meta-analysis (Jorgensen 2004) — count-based estimates have median 30-50% error; complexity factors needed for accuracy.
    3. Theoretical-complexity differences are well-documented: Wolfram (computational), Hawkins (functional/representational), Friston (mathematical), Aquinas (theological — Stump) are not commensurate complexity classes.
    4. C2A2-internal: prior tradition-ingest sessions have shown non-uniform per-file times.

  Strength of challenge: Moderate (sustains the presumption)

  Summary: The PRESUMPTION-255 challenge to ASSUMPTION-233/234 is well-supported by estimation literature. File-count-only models systematically underestimate complexity-variant batches. The 12-tradition complexity span is wide enough that uniform per-tradition time models will mis-estimate.

  Specific risks: (a) Time-budget overrun during the focused session; (b) early-tradition cadence becomes the locked-in expectation for harder later traditions; (c) wolfram-canary representativeness depends on whether wolfram is median or extreme.

  Mitigations available: (a) Add complexity multipliers per tradition; (b) re-estimate after 3 traditions, not after 1; (c) build slack into time budget.

  Recommendation: CHALLENGED (Moderate; presumption sustained)

  STEELMAN:
    Item: PRESUMPTION-255
    Strongest counterargument (to the presumption): File-count is a usable first-pass estimator and within-session learning can correct mid-stream.
    What would need to be true for C2A2 to be safe (if relying on uniform model): Mid-session re-estimation; explicit slack budget.
    How to test: After ingest, compute per-tradition actual time vs estimated; the variance quantifies the uniformity violation.
