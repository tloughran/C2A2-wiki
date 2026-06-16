SEARCH-FOR-ASSUMPTION-303:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-303
  Original statement: Agent actors are cumulative telemetry, not single-dated events; exempting them from the time-slider date cut is the correct temporal semantics.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-303
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Al-Fedaghi, S., 2012. "Conceptual Modelling and The Quality of Ontologies: Endurantism Vs. Perdurantism." arXiv:1207.2619. — Grounds the distinction the assumption relies on: endurants (objects/actors) exist wholly at each moment, perdurants (events) exist only at their dates; different temporal-filter treatment for the two kinds is ontologically principled.
    2. Wang, T.D., Plaisant, C., Shneiderman, B. et al., 2009. "Temporal Summaries: Supporting Temporal Categorical Searching, Aggregation and Comparison." IEEE TVCG (InfoVis). — Precedent for treating aggregated/rollup temporal entities differently from raw events in interactive temporal filtering.
    3. Guizzardi, G. et al. (UFO foundational ontology line, e.g. "Conceptual Modeling Applied to Data Semantics," arXiv:2210.01335). — Foundational-ontology practice of typing model elements as endurant vs perdurant and assigning different temporal semantics accordingly.
  Strength of support: Moderate
  Summary: The assumption maps cleanly onto the endurant/perdurant distinction in formal ontology: an agent actor that accumulates telemetry is an endurant (wholly present whenever it exists), whereas wiki-file creation events are perdurants pinned to dates. Ontology-driven modeling literature supports giving the two kinds different temporal semantics, and temporal-visualization work treats derived/aggregate entities differently from raw events under time filters. No source addresses the exact design (exempting one node class from a time-slider cut), but the theoretical grounding is solid and the analogous precedent in temporal aggregation is real.
  Caveats: Support is for the distinction, not for full exemption — an alternative consistent semantics would clip the actor's cumulative counts to the slider date (showing telemetry-as-of-t) rather than exempting it entirely; literature on temporal summaries arguably favors that as-of treatment when the data permits. Exemption is correct only while per-date decomposition of the telemetry is unavailable.
  Search scope: 1 WebSearch ("temporal filtering semantics aggregate entities vs events visualization endurant perdurant data modeling time slider").
  Recommendation: PARTIALLY-SUPPORTED
