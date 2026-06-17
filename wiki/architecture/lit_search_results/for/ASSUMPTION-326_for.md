SEARCH-FOR-ASSUMPTION-326:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-326
  Original statement: "Build the metric before iterating the view layer that depends on it ('cart-before-horse' sequencing)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-326
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the sequencing decision — define the metric before building its visualization
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Measure first" / data-before-dashboard practice in analytics & BI — defining and validating the metric before designing the view that depends on it is standard guidance; building visualization against placeholder/undefined data is a recognized anti-pattern that bakes in rework.
    2. Requirements/data-model-first design (software engineering) — depend on the stable layer before the volatile one; UI built atop an unsettled data definition incurs churn when the definition changes. Supports building the metric (the dependency) before the dependent view.
    3. "Garbage in, gospel out" cautions — designing the presentation around data whose definition is unsettled risks hardening an artifact on a moving foundation; settling the measure first reduces this risk.

  Strength of support: Moderate-Strong

  Summary: The metric-before-view sequencing is directly supported by analytics/BI and software-design practice: the view depends on the metric, so the metric is the stable layer that should be defined and validated first; building a visualization against placeholder or undefined data is a known anti-pattern that guarantees rework. As a dependency-ordering decision the sequencing is sound and conventional. Support is for the SEQUENCING choice specifically.

  Caveats: Support for "build the metric first" does NOT extend to "once built, the metric is trustworthy enough to build on" — that is the separate, weaker claim in PRESUMPTION-360 (provenance != validity). Iterative/prototyping schools also note value in cheap throwaway views that pressure-test the metric definition; "metric first" should not preclude using a rough view to surface metric problems early.

  Search scope: metric/data-before-visualization sequencing; dependency-first design; measure-first vs iterative prototyping. Comprehensive.

  Recommendation: SUPPORTED
