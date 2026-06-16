SEARCH-FOR-PRESUMPTION-327:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-327
  Original statement: Making the agent swarm legible/comparable/rankable is itself benign or good (observability treated as normatively neutral).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-327
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference — the Explorer treats legibility/ranking of the swarm as an unexamined good (cycle 0, priority LOW-MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Forsgren, N., Humble, J., Kim, G., 2018. "Accelerate: The Science of Lean Software and DevOps." IT Revolution; and DORA "State of DevOps" reports (2024: 39,000+ respondents). — Strongest empirical case that measurement/visibility of delivery processes correlates with dramatically better outcomes (elite teams recover ~2,000x faster); legibility of systems is repeatedly associated with performance.
    2. Hubbard, D., 2014. "How to Measure Anything" (3rd ed.). Wiley. — Theoretical grounding for measurement-as-good: reduced uncertainty improves decisions; refusing to measure has its own (usually larger) costs.
    3. Splunk/New Relic observability outcome reports (e.g., "organizations with complete observability practice see 64% fewer customer-affecting incidents"). — Industry-scale (vendor) evidence that making systems legible yields concrete reliability benefits.
    4. Muller, J.Z., 2018. "The Tyranny of Metrics." Princeton UP; Strathern, M., 1997. "'Improving ratings': audit in the British university system." — Boundary literature: the documented harms attach mainly to *ranking and incentive-coupling*, less to legibility per se; this carves out the defensible part of the presumption.
  Strength of support: Moderate
  Summary: For the legibility/observability component, support is real and reasonably strong: a large empirical literature (DORA/Accelerate) and decision-theory tradition (Hubbard) associate making systems measurable and visible with better outcomes, and for non-human software agents the classic surveillance harms (privacy, autonomy, observer effects on workers) largely do not apply in their original form. The *rankable* component is where neutrality fails: metric-fixation literature (Muller, Strathern/Goodhart) shows that converting visibility into rankings changes behavior of whoever optimizes against them — here, the humans curating agents, and potentially agents themselves if metrics feed back into prompts/selection. So the presumption is supported for legible/comparable, unsupported as a blanket claim covering ranking.
  Caveats: Vendor-published observability statistics are promotional and self-selected. The benign-for-agents argument weakens as agent outputs become consequential or as displayed metrics start steering curation decisions (Goodhart coupling — 15b's territory). Normative neutrality should be claimed only for the descriptive layer, with ranking treated as a separate, justified design decision.
  Search scope: 1 query — "benefits of observability dashboards transparency improves team performance you can't manage what you don't measure evidence". Plus established literature (Forsgren et al. 2018; Hubbard 2014; Muller 2018).
  Recommendation: PARTIALLY-SUPPORTED
