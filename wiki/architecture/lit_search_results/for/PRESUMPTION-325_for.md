SEARCH-FOR-PRESUMPTION-325:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-325
  Original statement: The agent population is a clean one-cron-task-per-agent roster (contradicted by multi-fire agents + unmapped interactive sessions).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-325
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference — roster design presumed one cron task per agent; already contradicted in-session by multi-fire agents and unmapped interactive sessions (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (only weak support for singleton mapping as a provisional starting heuristic)
  Sources:
    1. Talburt, J.R., 2011. "Entity Resolution and Information Quality." Morgan Kaufmann. — The "unique reference assumption" (each reference denotes exactly one entity) is a standard *simplifying baseline* in entity resolution — but the field exists because real populations violate clean one-to-one mappings, requiring explicit resolution machinery.
    2. Christen, P., 2012. "Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection." Springer. — Treats one-to-one record↔entity cardinality as an assumption to be tested and usually relaxed (one-to-many and many-to-many linkage are core cases), not a property to be presumed.
    3. Wang, R.Y., Strong, D.M., 1996. "Beyond Accuracy: What Data Quality Means to Data Consumers." JMIS 12(4). — Completeness/representational-consistency framework: a roster that excludes a known activity class (interactive sessions) fails completeness by definition.
  Strength of support: None (for the claim as stated); Weak (for singleton mapping as a deliberate provisional simplification)
  Summary: No literature was found asserting that real activity populations cleanly satisfy a one-source-per-entity taxonomy; the entity-resolution and record-linkage fields are premised on the opposite — cardinality assumptions are hypotheses that routinely fail and require explicit handling. The most charitable support available is procedural: starting from a unique-reference baseline is accepted practice *as a labeled, testable simplification*. Here the presumption was held implicitly and is already empirically contradicted in-session (multi-fire agents; unmapped interactive sessions), so even the procedural defense applies only retroactively.
  Caveats: This is a search over an already-falsified presumption; the FOR case can at best rehabilitate the *method* (start simple, then resolve), not the claim. Any residual use should recast the roster as an entity-resolution problem with explicit one-to-many handling and an "unmapped" residual category.
  Search scope: 1 query — "entity resolution registry design one-to-one identity mapping assumption scheduled jobs cron as unit of identity inventory roster". Plus established literature (Talburt 2011; Christen 2012). Preliminary search — broader search recommended.
  Recommendation: NO-SUPPORT-FOUND
