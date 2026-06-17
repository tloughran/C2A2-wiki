SEARCH-FOR-ASSUMPTION-324:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-324
  Original statement: "Yield headline = gross cumulative production (264), reported alongside net on-disk-unique (262); retired/reused ids kept in cumulative."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-324
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the reporting convention for the yield metric (gross headline + net alongside)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Stock-vs-flow accounting (national accounts; software-metrics) — gross cumulative production (a flow that includes retired units) and net surviving stock (an on-disk census) are two legitimate, standard measures of the same system; reporting both is normal and informative, not contradictory.
    2. Scientometrics / output accounting — counting all artifacts ever produced (including later-retracted ones) as "produced," while separately reporting the surviving set, is established practice (e.g., publications-ever vs currently-in-print). Keeping retired ids in the cumulative is a defensible flow definition.
    3. Software KLOC/churn measurement — gross-added vs net-surviving lines are standard distinct measures; the discipline explicitly distinguishes cumulative production from current footprint.

  Strength of support: Moderate-Strong

  Summary: The gross-cumulative-plus-net-on-disk reporting convention is squarely supported by stock-and-flow accounting and by scientometric/software-metric practice: production-ever (a flow, retirees retained) and surviving-set (a stock census) are distinct, legitimate measures of one system, and reporting both is the recommended way to avoid conflating them. Keeping retired/reused ids in the cumulative is the correct treatment for a flow measure. The 264/262 pairing is therefore methodologically clean PROVIDED both are labeled for what they are.

  Caveats: Support is conditional on labeling discipline — the headline must not be read as a current census, and "gross" must not silently become a target (Goodhart; see PRESUMPTION-355). The convention is sound; the risk is purely presentational (which number is foregrounded). Couples PRESUMPTION-357 (whether these are one quantity or distinct constructs) and the prior 318/349 commensurability thread.

  Search scope: stock-vs-flow accounting; gross vs net output measures; retraction/retirement counting conventions. Comprehensive.

  Recommendation: SUPPORTED
