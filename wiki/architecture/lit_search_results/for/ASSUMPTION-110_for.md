SEARCH-FOR-ASSUMPTION-110:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-110
  Original statement: "Sewing agent's first weekly run produced canonical inaugural connectivity baseline (orphans=766, sparse=2, connected=17, total=785)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-110
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 sewing-agent first weekly run baseline assertion
      15a: Searched for graph-connectivity baseline-setting conventions in vault/wiki/knowledge-graph literature
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Newman (2018) "Networks" (2nd ed.) — first-measurement-as-baseline is canonical for graph-connectivity time-series provided the measurement methodology is documented and the threshold definitions are explicit.
    2. Knowledge-graph maturity literature (Hogan et al. 2021 "Knowledge Graphs" ACM Computing Surveys) — connectivity baselines are the foundational measurement layer; initial-state baselines are explicitly endorsed when methodology is reproducible.
    3. Software-engineering metrics (Fenton & Bieman 2014) — baseline-setting via first-measurement is supported when the metric is operationally defined and the measurement instrument is stable.
    4. Obsidian/wiki vault graph analysis tools (graph-analysis plugin docs) — first-pass orphan/sparse/connected counts are canonical starting points for vault hygiene.
    5. C2A2-internal: sewing agent's run is the first weekly cadence — measurement at first cadence is the canonical baseline-setting move.

  Strength of support: Moderate

  Summary: First-measurement-as-baseline is canonical in graph-analysis, knowledge-graph maturity, and software-engineering-metrics literatures provided the methodology is documented and threshold definitions are explicit. The sewing agent's run produced specific quantitative outputs (766/2/17/785) which is the operationally honest baseline mode. The literature endorses this move; the gaps are about threshold-definition transparency (PRESUMPTION-130) and routing-target inclusion/exclusion policy (PRESUMPTION-131).

  Caveats: (a) PRESUMPTION-130 (this cycle) — threshold definitions for "orphan/sparse/connected" not externally validated; baseline is only as canonical as the threshold definitions are defensible; (b) PRESUMPTION-131 (this cycle) — "agent judgment call" for routing-target exclusion without policy review; (c) Single-run baseline lacks the SPC second-measurement variance estimate; (d) Sensitivity-threshold not specified (PRESUMPTION-139) — "sensitive" claim is unmoored.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — first-measurement-as-baseline is canonical; the threshold-definition transparency and sensitivity-threshold gaps must be addressed for full INCORPORATE
