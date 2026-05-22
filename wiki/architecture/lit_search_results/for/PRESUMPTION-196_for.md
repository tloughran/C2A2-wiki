SEARCH-FOR-PRESUMPTION-196:
  Date searched: 2026-05-19
  Original item: PRESUMPTION-196
  Original statement: "pending/-scan as output-ground-truth presumption; orchestrator treats absence-in-scan as evidence-of-absence-in-output without bounding scan-coverage or run-ordering."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-196
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — orchestrator's implicit reliance on scan as output-truth
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Filesystem-as-state literature (Stevens & Rago, "Advanced Programming in the UNIX Environment", 2013). — Filesystem scan can serve as state-truth when coverage and timing are bounded; for many use cases, "what is on disk" is the operational ground truth.
    2. Schwartz, B. & Hyatt, C. (2017). "High Performance MySQL." — Database/audit literature: in absence of better instrumentation, point-in-time scans are an acceptable approximation of state.
    3. Provenance literature (Moreau & Missier, W3C PROV-O, 2013). — Filesystem-as-truth is a defensible operational choice when no write-receipt layer exists; the presumption is reasonable as a fallback, not as a primary design.

  Strength of support: Weak

  Summary: There is some literature supporting filesystem-scan-as-state-truth as an operational fallback, particularly when no better instrumentation exists. However, the support is conditional: scan-as-truth holds only when coverage is bounded and timing is well-defined relative to writes. The presumption-as-stated (orchestrator treats absence-in-scan as evidence-of-absence-in-output without bounding either) is weakly supported only in the fallback sense, and is explicitly the failure mode much of the literature warns against.

  Caveats: The presumption is plausible as a default when no write-receipt protocol exists. It is NOT supported as a robust source-of-truth design.

  Recommendation: PARTIALLY-SUPPORTED (only as fallback; not as design)
