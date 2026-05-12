SEARCH-AGAINST-PRESUMPTION-093:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-093
  Original statement: "Same-day catch-up structurally equivalent to spread-across-week"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-093
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated counterpart of ASSUMPTION-079
      15b: Searched for challenging literature on temporal-clustering effects on cross-source signal independence
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Time-series literature (Box, Jenkins & Reinsel 2015) — temporal-clustering effects on cross-source signal independence are well-documented and material; same-window runs lose autocorrelation structure.
    2. Multi-agent-system literature (Wooldridge 2009; Stone & Veloso 2000) — same-window runs share environmental conditions; outputs are correlated in ways that spread runs would not produce.
    3. Sampling theory (Kish 1965) — within-cluster correlation reduces effective sample size in batch sampling; equivalence-by-default is unsupported.
    4. C2A2-internal: ASSUMPTION-079 PARTIALLY-CHALLENGED — same evidence applies; PRESUMPTION-status compounds.
    5. 2026-04-27 SYSTEMIC-RISK (PRESUMPTION-074) — shared-context bias is the operational form of this concern.

  Strength of challenge: Strong

  Summary: Structural equivalence is broken by temporal-clustering effects, shared-context bias, and within-cluster correlation. As an unstated presumption (PRESUMPTION-status), the equivalence is operating without precondition checks; literature is unambiguous that the preconditions matter and are routinely violated. The challenge is strong because the unstated form removes the prompt to test the preconditions.

  Specific risks: (a) Shared-context bias inflates apparent signal-convergence; (b) within-cluster correlation reduces signal-detection power; (c) compounds 2026-04-27 SYSTEMIC-RISK on specialist-recognition reliability.

  Mitigations available: (a) Surface the equivalence claim as testable; (b) randomize per-specialist prompt context within the catch-up window; (c) measure within-cluster correlation across catch-up cycles.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-093
    Strongest counterargument: The structural-equivalence claim is exactly the kind of presumption that quietly extends a stated assumption beyond its scope. ASSUMPTION-079 at least surfaces the claim for testing; PRESUMPTION-093 absorbs it as default. Same-day batches share environmental conditions in ways that spread distribution does not, and the literature consistently shows this matters. Treating the equivalence as unstated default removes the prompt to test the preconditions.
    What would need to be true for C2A2 to be safe: Surface the equivalence claim as a stated assumption (it then inherits ASSUMPTION-079's MONITOR cadence); test stationarity preconditions explicitly.
    How to test: Compare specialist outputs across catch-up vs. spread cycles; measure within-cluster correlation. If correlation > spread baseline, equivalence is operationally broken.
