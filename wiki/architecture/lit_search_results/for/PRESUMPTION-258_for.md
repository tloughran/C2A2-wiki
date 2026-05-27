SEARCH-FOR-PRESUMPTION-258:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-258
  Original statement: The "approval backlog is cleared" headline presumes approval, by itself, is a real network contribution; today network counts (222/90/35) moved by zero — intake-pipeline state advanced but network state did not. The headline silently re-instantiates the approved-vs-ingested decoupling (PRESUMPTION-252).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-258
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — headline-framing obscures next bottleneck.
      15a: Searched for supporting literature on intake-pipeline metrics as legitimate progress indicators.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Sources:
    1. Pirolli & Card (1999) information-foraging — intake-stage progress IS a meaningful proxy for downstream throughput when downstream is reliably exercised.
    2. Lean software / Kanban literature — stage-throughput metrics are legitimate even when end-to-end metrics lag; lead-time tracking respects this distinction.
    3. SRE / observability literature — measuring at each pipeline stage is the recommended pattern; intake-state metrics are valid in their own right.
    4. C2A2-internal: approval IS a real act with downstream commitment; reporting it is not invalid per se.

  Strength of support: Weak

  Summary: Stage-throughput metrics are legitimate in their own right (Lean, SRE), and intake-progress is a real signal. The supportive case is that the headline is not *false*, only *incomplete*. Where this gets weak is the *headline-framing* aspect — Goodhart concerns dominate when a stage-metric is used as the project-level summary.

  Caveats: (a) Support is for "intake metrics have value"; the presumption's challenge is "headline framing obscures downstream stall" — and the support does not address that; (b) the supportive case is bounded by whether downstream IS reliably exercised — which PRESUMPTION-248 says it currently is not.

  Recommendation: PARTIALLY-SUPPORTED (Weak)
