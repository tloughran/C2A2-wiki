SEARCH-FOR-PRESUMPTION-326:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-326
  Original statement: Recent/available activity is representative; bounded-window + sparse-old-data ingest under-renders low-frequency agents.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-326
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference — windowed ingest treats recent activity as representative, systematically under-rendering low-frequency agents (cycle 0, priority MEDIUM-HIGH)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (recency-priority is supported for *current-state* questions, not for population coverage)
  Sources:
    1. Gama, J., Žliobaitė, I., Bifet, A., Pechenizkiy, M., Bouchachia, A., 2014. "A survey on concept drift adaptation." ACM Computing Surveys 46(4). — Canonical support for recency-weighting: under non-stationarity, recent observations are the most informative about current behavior, and sliding windows that "forget" old data are the standard remedy.
    2. Bifet, A., Gavaldà, R., 2007. "Learning from Time-Changing Data with Adaptive Windowing (ADWIN)." SDM 2007. — Formal grounding that bounded recent windows are not just convenient but optimal-ish for estimating the *current* state of a drifting process.
    3. "Handling Concept Drift in Global Time Series Forecasting," 2023. arXiv:2304.01512. — Empirical: recency-weighting schemes (ECW/GDW) improve forecast accuracy, supporting the premise that recent data better reflects present dynamics.
  Strength of support: Moderate (for the recency-priority half only)
  Summary: The concept-drift literature gives real support to the design instinct behind the presumption: if the question is "what is this agent population doing *now*," recent windows are the right basis, and stale data can actively mislead. That legitimizes bounded-window ingest as a default for a live explorer. However, the support is for *temporal estimation of active entities*, not for *population representativeness*: nothing found supports the inference that a recency window adequately renders low-frequency or dormant entities — the same windowing literature acknowledges that infrequent events are exactly what fixed windows miss (motivating adaptive windows like ADWIN). So the FOR case covers "recent data is the best signal for what's current," not "recent data is representative of the roster."
  Caveats: Transfer requires separating two uses: state-estimation (windowing supported) vs roster coverage/comparison (windowing biased — low-frequency agents get sparse or zero representation, a survivorship-style undercount; that side is 15b's territory but bounds this one). Mitigation consistent with the supporting literature: per-entity adaptive windows or explicit "insufficient data in window" rendering rather than implicit near-zero rendering.
  Search scope: 1 query — "concept drift recent data more predictive sliding window recency weighting forecasting". Plus established literature (Gama et al. 2014; Bifet & Gavaldà 2007).
  Recommendation: PARTIALLY-SUPPORTED
