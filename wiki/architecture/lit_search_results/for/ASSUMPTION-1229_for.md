SEARCH-FOR-ASSUMPTION-1229:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1229
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: A disclosed constraint violation that improved the outcome warrants revising the
    constraint; and finding-yield-per-unit-budget is the measure by which that warrant is assessed.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1229
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from two transcripts; distinguished from ASSUMPTION-1221 because the warrant shifted
        from disclosure to defence-on-results.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED (measurement limb only)

  Search scope: WebSearch, 2026-08-28, one dedicated query on defect-detection yield per unit of inspection
    effort and diminishing returns. Literature reached: arXiv defect-management papers (1209.5573,
    1203.6439, 1402.5267, 2005.09217), practitioner defect-rate material, and secondary reporting of the
    IBM inspection-yield figures. NOT COVERED and material: (i) the cost-of-quality literature in primary
    form; (ii) any literature at all on the normative limb — whether a good outcome licenses revising the
    rule that was broken — which this direction did not find a supportive treatment of anywhere.
    All sources SNIPPET-ONLY. Search confidence: MODERATE on the measurement limb, NONE on the normative limb.

  Supporting evidence found: Partial

  Sources:
    1. Secondary reporting of the IBM inspection study, via Anon., "Defect Management Strategies in Software
       Development" (arXiv:1209.5573) and related [SNIPPET-ONLY; authors and primary citation unverified] —
       38 defects/KLOC found by inspection vs 8/KLOC by unit test, inspection accounting for 82% of total
       defects found. Establishes that yield-per-unit-of-review-effort is a measured quantity with a real
       literature, which is the assumption's second limb.
    2. Axify, "Defect Rate: Metrics, Tools, and Strategies to Improve Quality" [SNIPPET-ONLY]
       https://axify.io/blog/defect-rate — Reports formal inspections detecting ~60% of defects vs under
       50% for informal review; i.e. yield is a function of process formality and is routinely compared.
    3. Anon., "Simulation-Based Risk Reduction for Planning Inspections" (arXiv:1402.5267) [SNIPPET-ONLY;
       authors unverified] — Compares inspection policies (none / all / density-threshold), which is the
       decision-theoretic frame the assumption gestures at: choose the inspection budget by expected yield.

  Strength of support: Weak-Moderate

  Summary: Only half of this assumption found support, and it is the uncontroversial half. Finding-yield-
    per-unit-of-inspection-effort is a genuine, measured, comparable quantity, and choosing an inspection
    budget by expected yield is a recognised decision problem with a modelling literature behind it. That
    much of the assumption is sound. The load-bearing half — that a violation which produced good findings
    thereby earns a revision of the limit it violated — found no supporting literature from this direction
    at all. Nothing was located that treats a favourable outcome as evidence about the correctness of the
    constraint that was breached to obtain it. The supportive result is therefore narrow and should not be
    read as endorsing the inference the item actually makes.

  Caveats: The IBM figures are 1970s-80s software inspection data reaching me third-hand at snippet level,
    with the primary citation unverified; their transfer to token budgets in a review pipeline is assumed,
    not shown. The absence of support on the normative limb is a finding, not an omission.

  Recommendation: PARTIALLY-SUPPORTED
