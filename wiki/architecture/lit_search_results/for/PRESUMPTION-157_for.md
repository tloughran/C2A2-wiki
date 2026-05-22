SEARCH-FOR-PRESUMPTION-157:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-157
  Original statement: "Generative-canvas library set (D3 + three.js + Plotly + WebGL) presumed right catalog without comparison against Observable Plot / deck.gl / regl / vega-lite / P5.js / Mapbox GL JS / ECharts"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-157
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-124 closed-enumeration of library set
      15a: Searched for visualization-library comparison literature for generative AI workflows
    Current status: SUPPORTED

  Sources:
    1. State of JS 2024 / State of Frontend 2024 — visualization library landscape includes Observable Plot, deck.gl, vega-lite, ECharts as first-tier; explicit comparison is standard.
    2. Heer et al. (2010) "A tour through the visualization zoo" — library-comparison-by-use-case is endorsed methodology.
    3. Vis Atelier / Vis 2024 surveys — library-set selection for generative workflows is an active research area; closed enumeration is widely flagged.
    4. Observable Plot (Bostock 2022) — explicit successor to D3 for common cases; may subsume D3 for typical plots.

  Strength of support: Strong

  Summary: The library landscape is well-documented and the alternatives named (Observable Plot, deck.gl, vega-lite, ECharts) are first-tier. Library-set-selection-by-comparison is endorsed methodology. The presumption correctly identifies that ASSUMPTION-124 closes the enumeration without comparison. Strong support for the inference; the presumption tracks a recognized closed-enumeration concern.

  Caveats: (a) Library-set sizing is a real concern — fewer libraries reduce LLM-codegen surface; (b) The chosen libraries are widely-used and not wrong; the comparison may confirm the choice; (c) deck.gl is geo-and-large-data specific — may not be needed for C2A2's whiteboard plots; vega-lite may be too prescriptive for generative use.

  Recommendation: SUPPORTED — library-comparison gap is real; the inference identifies a recognized closed-enumeration concern
