SEARCH-FOR-ASSUMPTION-079:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-079
  Original statement: "Same-day daemon catch-up of all six weekday-assigned specialist agents is functionally equivalent to spread-across-week distribution"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-079
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 daemon catch-up morning event after the link-count silent-skip bug was diagnosed
      15a: Searched for supporting literature on batch-vs-spread scheduling for diversified knowledge surveillance
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Box, Hunter & Hunter (2005) "Statistics for Experimenters" — under stationary conditions and independent inputs, batch and spread sampling are statistically equivalent for first-moment estimates; supports the equivalence claim when inputs are stable across the catch-up window.
    2. Operations-research literature on "fairness vs. throughput" in batch scheduling (Pinedo 2016) — when each work-unit is i.i.d. with respect to scheduling time, batch processing reproduces the spread-distribution result for any aggregate statistic.
    3. C2A2-internal: PREMISE-008 (single-cycle drainability up to 8-deep) — already validated for similar volume; six-deep falls within validated range.
    4. Pull-based monitoring patterns (Allspaw 2018; SRE workbook) — catch-up runs after scheduler downtime are explicitly endorsed when the underlying signal is not strongly time-of-day-coupled.
    5. Survey-research literature on retrospective vs. prospective sampling (Schaeffer & Presser 2003) — when the population is slow-changing relative to the sampling window, retrospective batch capture preserves the inferential structure of prospective spread sampling.

  Strength of support: Moderate

  Summary: The equivalence claim is supported under explicit conditions: stationarity, input independence, and slow-changing population relative to the catch-up window. C2A2's six specialist slots draw on weeks-to-months-stable literature streams, so the stationarity precondition is plausibly met. The claim is endorsed in operations research and survey methodology under those conditions, and the volume falls within C2A2's already-validated drainability bound (PREMISE-008). However, the literature consistently pairs the equivalence claim with explicit precondition checking, which the assumption does not surface.

  Caveats: (a) Equivalence is conditional on stationarity — if any specialist's source stream has time-of-week structure, the equivalence breaks; (b) PREMISE-008 was validated at ≤8 items, this run hits 6, but the pattern of doing this routinely could compound risk; (c) the literature treats catch-up as a fallback, not as a routine substitute for distribution.

  Recommendation: PARTIALLY-SUPPORTED (equivalence holds under stationarity preconditions; preconditions need explicit treatment)
