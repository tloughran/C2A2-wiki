SEARCH-FOR-ASSUMPTION-046:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-046
  Original statement: "Filtering active Pattern-Detector findings from 17 to 'most significant 11' preserves actionable signal"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-046
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from briefing-layer filter — 17→11 reduction with "most significant" as the criterion
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Miller (1956) "The Magical Number Seven, Plus or Minus Two"; Cowan (2001) revisions to working-memory limits at N=4; Rosenholtz et al. (2005) visual-clutter findings: a scannability budget of 5–12 items is empirically grounded for human cognitive surfaces.
    2. Executive briefing / dashboard design literature (Few 2013 "Information Dashboard Design"; Tufte 1990 "Envisioning Information"): information density must be bounded by cognitive-budget; selection is an unavoidable part of briefing-surface design.
    3. Ranking-and-truncation in recommender systems (Ricci et al. 2015 "Recommender Systems Handbook"; MAP@k / NDCG@k evaluation tradition): truncating a ranked list at a fixed cutoff preserves top-signal by construction when ranking is well-calibrated.
    4. Alert-fatigue literature (Ancker et al. 2017; Sasangohar et al. 2018): reducing alert volume is a documented intervention that improves rather than harms downstream action — less-is-often-more at the cognitive-surface layer.
    5. C2A2's prior PRESUMPTION-029 disposition (CRITICAL; selection-bias in multi-subagent batch case): the system has prior disposition scaffolding recognizing that selection is consequential; this assumption is the briefing-layer analog.

  Strength of support: Moderate

  Summary: The *general form* of the claim — that a cognitive-scannability budget (5–12 items) exists, and that ranked truncation is a defensible briefing-surface strategy — is well-supported by cognitive-psychology, dashboard-design, recommender-systems, and alert-fatigue literatures. The *preservation-of-actionable-signal* clause is supported if and only if the ranking function itself is well-calibrated — which is the contested territory that the paired PRESUMPTION-053 (unaudited selection criterion) directly names.

  Caveats: (a) "preservation" is a measurable claim only if there is a ground-truth notion of actionability — which is not operationalized in the briefing pipeline; (b) the 17→11 ratio is not derived from a loss-function measurement; (c) asymmetric to PRESUMPTION-029's quiet-amplification concern, the symmetric quiet-attenuation risk is not audited here.

  Recommendation: PARTIALLY-SUPPORTED (cognitive-budget rationale is strong; signal-preservation claim inherits the calibration gap of the unaudited ranking function)
