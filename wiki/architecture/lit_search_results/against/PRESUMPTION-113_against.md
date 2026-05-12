SEARCH-AGAINST-PRESUMPTION-113:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-113
  Original statement: "Off-cadence specialist proposal filings presumed same baseline expectations as on-cadence filings"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-113
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 specialist-proposal disposition
      15b: Searched for counter-evidence on off-cadence work-product variance
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. Newport (2016); Csikszentmihalyi (1997) — off-cadence work has documented attention-state difference; baseline expectations should reflect this rather than presume identity.
    2. Williams (2010); Stol & Fitzgerald (2014) — empirical agile-quality literature shows cadence-induced quality variance is small but observable; baseline-identity presumption is conservative-toward-noise but inaccurate.
    3. Mark et al. (2014) "Bored Mondays and Focused Afternoons" — circadian / weekly-cadence variance in work-product quality is documented; baseline-identity flattens this signal.
    4. Statistical-process-control literature (Wheeler 2000) — uniform baseline across variable-cadence streams biases approval-rate metrics; documented as noise-introduction.
    5. C2A2-internal: ASSUMPTION-091 / PRESUMPTION-112 — companion items in the uniform-treatment-without-character-differentiation cluster.

  Strength of challenge: Moderate

  Summary: Same-baseline-expectations is canonical default but is challenged when cadence-induced variance is observable. The literature uniformly endorses cadence-tagging for downstream metrics rather than baseline-identity. The challenge is moderate because the variance is small in steady state but non-zero; the presumption is precision-overstated, not category-mistake.

  Specific risks: (a) Approval-rate metric bias; (b) cadence-induced variance hidden; (c) compounds with ASSUMPTION-091 / PRESUMPTION-112 — uniform-treatment cluster.

  Mitigations available: (a) Cadence flag on filings; (b) cadence-sliced baseline expectations; (c) variance test on existing data.

  Recommendation: PARTIALLY-CHALLENGED (cadence-independence is canonical default; observable variance is the standard guard, currently absent)

  STEELMAN:
    Item: PRESUMPTION-113
    Strongest counterargument: Cadence-induced quality variance is documented in agile / knowledge-work / circadian literatures. Same-baseline-expectations across variable cadence biases downstream metrics. The presumption pairs with ASSUMPTION-091 in the uniform-treatment cluster — both inherit the same gap (no cadence flag, no variance test).
    What would need to be true for C2A2 to be safe: (a) cadence flag; (b) variance test; (c) cadence-sliced metrics.
    How to test: Tag past filings with cadence; compare variance pooled vs. sliced; if sliced reveals systematic difference, presumption is empirically refuted.
