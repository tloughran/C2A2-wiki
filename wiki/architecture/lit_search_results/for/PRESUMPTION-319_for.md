SEARCH-FOR-PRESUMPTION-319:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-319
  Original statement: [inferred] The data/code guard presumes PRS-data regeneration is deterministic/safe enough to publish unreviewed (data treated as review-exempt).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-319
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that regenerated data needs no human review.
      15a: Searched for support that deterministic, schema-validated derived data can be safely auto-published.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Deterministic-build / reproducible-pipeline practice (reproducible builds; deterministic data transforms). — If a generator is genuinely deterministic and its inputs are already approved, the output is a pure function of approved inputs, which supports treating it as lower-risk than arbitrary code change.
    2. Automated data-validation gates (schema checks, Great Expectations-style assertions, constraint tests). — The recognized way to make data auto-publishable is to replace HUMAN review with AUTOMATED data tests; where such gates exist, "unreviewed by a human" can be safe because it is not "unchecked."
    3. Risk-asymmetry / blast-radius (shared with ASSUMPTION-284). — Appending already-approved data within a fixed schema is lower-variance than changing rendering logic.

  Strength of support: Weak-Moderate

  Summary: There is genuine support for treating deterministic, already-approved data as lower-risk than code — BUT the literature converts "no human review" into "automated validation," not "no checking at all." The supportable version of the presumption is "data may bypass HUMAN visual review IF it passes automated data-quality gates and the generator is verified deterministic." Bare "data is review-exempt" is supported only under those substituted controls.

  Caveats: The support is conditional on (a) verified determinism and (b) automated data-quality gates standing in for the human. Absent those, the presumption overclaims; the AGAINST search shows that silent data-quality regressions are the harder, less-visible failure mode precisely because no one is looking.

  Recommendation: PARTIALLY-SUPPORTED
