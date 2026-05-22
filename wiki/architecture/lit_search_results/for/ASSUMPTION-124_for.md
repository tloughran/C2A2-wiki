SEARCH-FOR-ASSUMPTION-124:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-124
  Original statement: "Generative-canvas library set is D3 + three.js + Plotly + bare canvas/WebGL"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-124
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from generative-canvas library catalog decision
      15a: Searched for visualization-library landscape in 2026 and combination patterns for generative AI workflows
    Current status: SUPPORTED

  Sources:
    1. Bostock (2011-2024) D3.js documentation and case studies — D3 is the canonical low-level web visualization grammar.
    2. three.js documentation and WebGL community (2010-2025) — three.js is the dominant high-level WebGL library.
    3. Plotly community and benchmarks (2023-2025) — Plotly is widely used for analytics dashboards; declarative API is appropriate for AI-generated plots.
    4. State of JS / State of Frontend 2024-2025 surveys — D3 + Plotly + three.js together cover the bulk of production data-visualization needs.
    5. C2A2-internal: parallel pattern with wiki_narration.html (D3 v7) already in production.

  Strength of support: Strong

  Summary: D3 + three.js + Plotly + WebGL covers the canonical landscape — declarative analytics (Plotly), low-level web (D3), 3D/WebGL (three.js), and bare metal (canvas/WebGL) for performance edge cases. The library set is well-supported by production practice and ecosystem maturity. The C2A2-internal wiki_narration.html precedent confirms D3 is operating well. PRESUMPTION-157 (paired) flags that alternatives (Observable Plot, deck.gl, vega-lite, ECharts) were not explicitly compared — this is a closed-enumeration concern, not a wrong-library concern.

  Caveats: (a) PRESUMPTION-157 — closed enumeration; alternatives not compared; (b) Library set sizing concern — four libraries is heavy if any could be eliminated; (c) Observable Plot (built on D3) may subsume D3 for typical plots and reduce LLM-codegen surface; (d) deck.gl is the canonical choice for geo / large-data WebGL — not covered.

  Recommendation: SUPPORTED — library set is well-justified; the comparison-against-alternatives audit (PRESUMPTION-157) would strengthen the choice
