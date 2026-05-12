SEARCH-FOR-PRESUMPTION-124:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-124
  Original statement: "Today's 8-task fire-rate treated as global negative inference for daemon-link-count regression — wiki-orchestrator status today not in evidence frame"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-124
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD per-task-to-cross-task inference analysis
      15a: Searched for per-task vs. cross-task evidence-frame literature in failure-mode diagnosis
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. Failure-mode diagnosis literature (Vesely et al. 1981 "Fault Tree Handbook"; Stamatis 2003 FMEA) — per-task evidence is canonically informative only about THIS task; cross-task generalization requires explicit per-task disaggregation.
    2. Distributed-systems literature (Lamport 1978; Gray 1978 "Notes on Database Operating Systems") — selectively-affected systems are documented; per-node positive evidence does not transfer to other nodes without per-node check.
    3. Statistical inference literature on selection effects (Heckman 1979) — global inference from partial sample, where the sample is selected by the outcome being inferred, is canonical selection bias.
    4. (No literature supports global-from-partial inference for selectively-affected systems.)
    5. C2A2-internal: ASSUMPTION-080 partition (>1 fires; =1 silent skip) explicitly predicts selective-affectedness; per-task fire evidence cannot rule out other-task silent skips.

  Strength of support: None

  Summary: No literature supports global-from-partial inference for selectively-affected systems. The fault-tree, distributed-systems, and selection-effect literatures uniformly require per-node disaggregation. The presumption operates against literature consensus.

  Caveats: This is a NO-SUPPORT-FOUND for the FOR direction.

  Recommendation: NO-SUPPORT-FOUND
