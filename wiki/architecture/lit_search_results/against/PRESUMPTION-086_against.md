SEARCH-AGAINST-PRESUMPTION-086:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-086
  Original statement: "PREMISE-013 N-collisions threshold not examined; flag-and-roll-forward scales without breakdown"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-086
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Shapiro et al. (2011) on CRDTs — collision-merge handling has saturation point; the literature is explicit that scaling is conditional, not unconditional.
    2. Bryant et al. (2014) on persistent identifier failure — non-unique IDs cause downstream rollup corruption.
    3. Kleppmann (2017) "Designing Data-Intensive Applications" — eventual-consistency tradeoffs require explicit boundary conditions.
    4. C2A2-internal: PREMISE-013 conditions (low collision rate, durable mapping, follow-renames) are the safeguards; PRESUMPTION-086 elides them.

  Strength of challenge: Moderate

  Summary: The literature is consistent: flag-and-roll-forward scales conditionally, not unconditionally. The presumption that the pattern scales "without breakdown" elides the explicit conditions PREMISE-013 names. The conditional version is supported; the unconditional version is challenged.

  Specific risks: (a) ID-collision compound failures at N>5 cumulative-unresolved; (b) reference-rot if rename-mapping is not durably persisted; (c) audit-trail breakage.

  Mitigations available: (a) Specify an explicit N-collision upper bound; (b) audit durable mapping persistence; (c) track collision rate as metric.

  Recommendation: CHALLENGED (Moderate) — PRESUMPTION + moderate challenge → lean toward MONITOR/REVISE per 15c heuristic

  STEELMAN:
    Item: PRESUMPTION-086
    Strongest counterargument: "Without breakdown" elides PREMISE-013's explicit conditions. The presumption applies the principle at scales the conditions were never tested at. As collision count grows, downstream consumers may receive different referents under the same ID across time without a redirect mechanism.
    What would need to be true for C2A2 to be safe: Specify an explicit collision-count upper bound; audit rename-mapping persistence; add HTTP-301-style redirect entries for renamed IDs.
    How to test: Sample 5 cross-references in older wiki content; check whether each resolves to the post-rename target. Any failure falsifies the no-breakdown claim.
