SEARCH-FOR-ASSUMPTION-123:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-123
  Original statement: "Whiteboard plots (Pathway 05) ephemeral by default + Pin-this promotion + per-plot export (PNG/SVG/HTML/CSV/PDF)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-123
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Pathway 05 whiteboard design pass
      15a: Searched for ephemeral-by-default UX patterns in note/dashboard tools and pin-and-export interaction patterns
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Miro / FigJam / Excalidraw documentation (2023-2025) — whiteboard-class tools commonly default to ephemeral session-scoped state with explicit-save promotion.
    2. Jupyter and Observable notebook UX research (2022-2024) — ephemeral computational artifacts with explicit pin/save patterns reduce visual clutter and storage pressure.
    3. Per-plot export standardization is endorsed by D3 / Plotly / Vega-Lite ecosystems — multi-format export (PNG/SVG/HTML/CSV/PDF) is the canonical export surface.
    4. Reeves & Sherwood (1999) "Soul of the New Machine" pattern — ephemerality + promotion reduces commitment cost for exploratory work.

  Strength of support: Moderate

  Summary: Ephemeral-by-default with explicit pin/save is a well-established UX pattern for exploratory and whiteboard tools. Per-plot multi-format export is canonical. Support for the mechanism choice is moderate-strong. PRESUMPTION-156 (paired) raises the genuine concern that the inverse default (persistent-by-default with explicit-discard) may be more appropriate for use cases where users do not recognize value in real time.

  Caveats: (a) PRESUMPTION-156 — ephemeral default presumes real-time value recognition; for derivative-realization cases (value evident only on retrospective review), the opposite default may be correct; (b) Loss-of-work-on-session-end is a known failure mode of ephemeral-default tools; (c) "Pin-this" affordance discoverability is a known UX risk.

  Recommendation: PARTIALLY-SUPPORTED — mechanism pattern is well-supported; default-direction question (PRESUMPTION-156) is the load-bearing tradeoff
