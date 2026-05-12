SEARCH-FOR-PRESUMPTION-035:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-035
  Original statement: "Four Chrome-extension failures in one day meet the OPERATIONAL-DRIFT threshold defined by PRESUMPTION-032 — although PRESUMPTION-032 never specified a threshold"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-035
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — threshold-free invocation of drift alert
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. SRE literature (Beyer et al. 2016 "Site Reliability Engineering"; Google SRE Workbook 2018): explicit SLI/SLO threshold definition is a prerequisite for consistent alerting — no literature supports retrospectively declaring a threshold met without prior definition.
    2. Alert-design literature (Rosen et al. 2020 on alert fatigue): retrospective or ad hoc thresholds are treated as anti-patterns.

  Strength of support: None

  Summary: No literature supports threshold-free or retrospectively-defined drift thresholds. The SRE and alert-design literature is unanimous that consistent drift/SLO alerts require pre-defined, documented thresholds. The presumption that "four failures meets the threshold" is, by the literature, indistinguishable from "four failures feels like a lot right now" — which may be a reasonable heuristic but is not a codified threshold.

  Caveats: None — the absence of literature support is the salient finding. A clear threshold could be defined going forward (e.g., "≥2 failures in any channel in a rolling 24h window"), at which point future invocations would be supportable.

  Recommendation: NO-SUPPORT-FOUND
