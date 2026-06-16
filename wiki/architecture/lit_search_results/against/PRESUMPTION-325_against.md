SEARCH-AGAINST-PRESUMPTION-325:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-325
  Original statement: The agent population is a clean one-cron-task-per-agent roster (contradicted by multi-fire agents + unmapped interactive sessions).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-325
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (roster design presumed 1:1 task↔agent; in-session evidence already contradicted it)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Binette & Steorts, 2022. "(Almost) All of Entity Resolution." Science Advances 8(12). — Modern ER explicitly rejects the clean-roster premise: real linkage problems have duplicates within sources, many-to-one and one-to-many mappings, and unmatchable residue; methods assuming no within-source duplication (classic Fellegi-Sunter) produce impossible linkage configurations when the assumption fails.
    2. Fellegi & Sunter, 1969 + critiques (see Steorts et al. microclustering line, "Theoretical Limits of Record Linkage and Microclustering," 2017). — One-to-one linkage assumptions violate independence and bias error estimates when entity cardinality is actually variable; cluster sizes in real registries follow skewed (microclustering) distributions, not singletons.
    3. Christen, P., 2012. "Data Matching." Springer. — Standard reference: registry/roster designs must model entity:record cardinality explicitly; systems that hard-code 1:1 require schema surgery, not parameter tweaks, when many:many data arrives.
    4. Kimball & Ross, 2013. "The Data Warehouse Toolkit" (3rd ed.). — Dimensional-modeling treatment of the same trap: conflating a recurring process (cron task) with an entity (agent) creates a fact/dimension confusion; recurring vs ad-hoc executions need a separate event grain from the entity dimension.
  Strength of challenge: Strong
  Summary: This presumption was already contradicted by the system's own data (multi-fire agents, unmapped interactive sessions), and the literature explains why that contradiction is the expected case, not an anomaly. Entity-resolution research treats variable cardinality and within-source duplication as the default condition of real registries; one-to-one rosters are a degenerate special case whose violation breaks both the mapping and the error estimates built on it. Dimensional modeling adds the deeper diagnosis: "cron task" is an *event template* and "agent" is an *entity*, and collapsing the two grains means interactive sessions (events with no template) and multi-fire tasks (templates with many events) both have nowhere to live. The roster doesn't need patching; its cardinality model needs to be agent(1) — task(0..n) — session(0..n), with an explicit unmapped-residue bucket.
  Specific risks: Unmapped interactive sessions silently dropped from the explorer (population undercount); multi-fire agents either double-counted or merged wrongly; every per-agent metric (volume, eval/apply, edges) computed over a mis-specified denominator, contaminating ASSUMPTIONS 287/291/292 outputs.
  Mitigations available: Explicit three-level schema (agent / task-definition / session) with declared cardinalities; an "unassigned" residue class that is rendered, not dropped; reconciliation report each ingest (sessions in = sessions mapped + sessions residual); revisit after reseed when residue share is measurable.
  STEELMAN:
    Strongest counterargument: For a small, locally-known population, a 1:1 roster is a deliberate simplification, not an error — the owner can name every agent, the multi-fire cases are enumerable by hand, and a full ER machinery is overkill. Schema simplicity bought a working explorer in one day; the known exceptions can be carried as a short manual exception list.
    What would need to be true for C2A2 to be safe: The residue (unmapped sessions + multi-fire spillover) stays small and visible; the exception list is actually maintained; no downstream metric assumes the denominator is complete.
    How to test: Compute the share of total sessions that fail the 1:1 mapping today (multi-fire + interactive). If it exceeds a few percent — and 14b's evidence suggests it does — the "clean roster" is quantitatively falsified on the system's own data.
  Search scope: 1 search — "entity resolution one-to-many cardinality assumption failure record linkage duplicate entities registry". Plus established ER/dimensional-modeling literature.
  Recommendation: CHALLENGED
