SEARCH-AGAINST-ASSUMPTION-303:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-303
  Original statement: Agent actors are cumulative telemetry, not single-dated events; exempting them from the time-slider date cut is the correct temporal semantics.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (temporal-semantics design choice)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. Aigner, Miksch, Schumann & Tominski, 2011. "Visualization of Time-Oriented Data." Springer. — Standard treatment distinguishes instants vs intervals and stresses that a temporal filter must apply one coherent time model to the whole display; mixed semantics within one control is a recognized design error.
    2. Grenon & Smith, 2004. "SNAP and SPAN: Towards Dynamic Spatial Ontology." Spatial Cognition & Computation. — Endurant/perdurant distinction: enduring entities (like an agent) still have time-indexed states; the ontologically correct rendering at time t is the entity's state-as-of-t, not its full present-day state.
    3. ArcGIS Pro documentation, "Visualize temporal data using the time slider." — Industry-standard slider semantics: the slider filters the view to entities/values valid in the visible time span; layers exempted from time produce a display whose elements answer different temporal questions simultaneously.
  Strength of challenge: Moderate
  Summary: The challenge is not that agent actors are dated events — they aren't — but that "cumulative, therefore exempt" is a false dichotomy. Cumulative entities have valid-time histories: an agent actor at slider position t should appear with its activity-as-of-t (or not at all if it had no activity before t), which is the state-snapshot semantics standard in temporal visualization and ontology (SNAP/SPAN). Full exemption makes the display silently bimodal: wiki nodes answer "what existed by date t" while agent nodes answer "what exists today," and a user scrubbing to early dates sees agents connected to nodes that did not yet exist. The literature treats such mixed temporal semantics as a comprehension hazard, not a neutral choice.
  Specific risks: Users (including the project's own retrospective analyses) draw wrong inferences about when agent activity began or co-occurred with wiki growth; edges from exempted agent nodes to date-filtered nodes dangle or mislead at early slider positions; the precedent licenses future "exempt" layers, eroding the slider's invariant.
  Mitigations available: Truncate cumulative agent telemetry to the slider date (state-as-of-t) rather than exempting; if exemption is kept, visually mark exempted nodes (distinct style/legend note "not time-filtered"); hide agent edges whose endpoints are date-filtered out.
  STEELMAN:
    Strongest counterargument: Agent actors are derived rollup nodes, not first-class historical records; their per-date decomposition may not exist in the captured telemetry, so state-as-of-t is unimplementable without fabricating data. Showing them constantly, clearly styled as a distinct actor class, is more honest than an invented history, and matches dashboard conventions where reference layers ignore time brushes.
    What would need to be true for C2A2 to be safe: Users reliably perceive agent nodes as a different ontological class exempt from time; no analysis ever reads agent-wiki co-occurrence off the time-scrubbed view; per-date telemetry truly is unrecoverable.
    How to test: Scrub to the earliest date and check whether agent nodes/edges produce visibly anachronistic connections; if file-write telemetry has timestamps, a state-as-of-t cut is feasible and should be prototyped.
  Search scope: 1 WebSearch ("time slider filter semantics aggregate derived nodes exempt temporal filtering visualization pitfalls cumulative data"); plus standard temporal-visualization and ontology literature.
  Recommendation: PARTIALLY-CHALLENGED
