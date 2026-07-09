SEARCH-FOR-ASSUMPTION-422:
  Date searched: 2026-07-07
  Original item: ASSUMPTION-422
  Original statement: "A second same-week data point from a slightly different resolver would add methodological noise to the trend line."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-422
    Item type: ASSUMPTION (stated); Priority MEDIUM
    Transform at each step:
      14a: Extracted from the 2026-07-06 autonomous-Monday EOD sources (sewing bootstrap verification report / sync-agent transcripts) comparing an older bootstrap resolver against the newer weekly connectivity resolver
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Scottish Government, "Long term survey strategy: mixed mode research report," Ch. 8 (Impacts of changing or mixing modes on trends and time series). gov.scot. — Concludes that once an instrument/mode transition occurs there is "an effective break in the time series," and calibration to remove the discontinuity is "widely viewed as practically infeasible," directly supporting the claim that a different resolver injects a discontinuity/noise into a trend.
    2. De Leeuw et al., "Mixing Modes: Tradeoffs Among Coverage, Nonresponse, and Measurement Error." — Establishes that a change of measurement instrument introduces a mode/method effect: systematic bias on parameter estimates confounded with true change, precisely the mechanism by which a second resolver contaminates a trend line.
    3. Klausch, Hox & Schouten (measurement equivalence in mixed-mode surveys), Frontiers in Psychology, 2015 / PMC4318282. — Shows that instruments must demonstrate measurement equivalence before their outputs can be pooled; absent equivalence, mixed-instrument comparisons reflect method variance rather than true change.
    4. Van de Schoot et al. / longitudinal measurement-invariance literature (e.g., PMC12987755 "Estimating Trends With Differential Item Functioning"). — Demonstrates that noninvariant measurement across occasions biases growth/trend parameters "in a difficult-to-predict direction," reinforcing that an unvalidated resolver swap corrupts trend inference.

  Strength of support: Strong

  Summary: The longitudinal-measurement and survey-methodology literatures strongly support the claim. A change of instrument (here, resolver) introduces a "mode effect"/method variance that is confounded with true change, producing a break or discontinuity in the time series; calibrating it away after the fact is regarded as practically infeasible. Measurement-invariance/DIF theory is explicit that pooling instruments that are not demonstrably equivalent biases trend estimates in unpredictable directions. Thus a second, slightly different resolver in the same week would indeed add methodological noise unless equivalence were first established.

  Caveats: The same literature offers a competing prescription: rather than EXCLUDE the discordant instrument, one can MODEL the mode effect (overlap/bridge samples, alignment, DIF-adjusted estimation) and recover comparability — so "excluding beats modeling" is not established, only "naive pooling is harmful." Support is strongest when the two resolvers genuinely differ in measurement properties; if they are near-equivalent, added noise is minimal and the second point could instead improve precision. Sources are from human-survey research; transfer to automated graph-connectivity resolvers is analogical.

  Recommendation: SUPPORTED
