SEARCH-AGAINST-PRESUMPTION-337:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-337
  Original statement: The single-human attended commit gate scales with parallel-session output (local-only queues can accumulate indefinitely without integration risk).

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-337
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference (parallel sessions producing local queues; no stated plan for gate throughput or queue-age risk)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Forsgren, Humble & Kim, 2018. "Accelerate" (DORA research program). — Empirically, high performance associates with <=3 active branches and merging to mainline at least daily; long-accumulating unintegrated work is one of the strongest measured anti-patterns.
    2. Fowler, 2024 (rev.). "Continuous Integration." martinfowler.com. — Integration risk grows with time-since-last-integration: "the longer you wait, the bigger that risk"; queued local work is precisely deferred integration, and conflicts compound nonlinearly on shared artifacts.
    3. Reinertsen, 2009. "The Principles of Product Development Flow." Celeritas. — Batch-size economics: large batches raise defect-feedback delay, review quality collapse, and variability superlinearly; an unbounded queue in front of a fixed-capacity single server (the attending human) has unbounded wait growth once arrival rate exceeds service rate (Little's Law).
    4. Hyrum/practice literature on review fatigue and single-approver bottlenecks (e.g., Graphite, "How merge queues can reduce CI/CD pipeline bottlenecks"). — Single-approver gates become both throughput ceiling and quality ceiling: as queue depth rises, approval becomes rubber-stamping, defeating the gate's purpose (interacts with PRESUMPTION-335's human-detector limits).
  Strength of challenge: Strong
  Summary: The CI and flow literatures directly contradict both halves of the presumption. First, "without integration risk": conflict probability on shared artifacts (the wiki vault, the generated HTML, shared scripts) rises with queue age and with the number of parallel producers; deferred integration does not park risk, it compounds it, and semantic conflicts (two sessions editing related wiki content) are worse than textual ones because no merge tool flags them. Second, "scales": a single human is a fixed-capacity server; with parallel agent sessions the arrival rate is elastic while service rate is not, so queue depth grows without bound, and the documented response is degraded review (rubber-stamping) — meaning the gate's anomaly-detection function (already challenged in 335) decays exactly when load rises. The gate's safety and its scalability are inversely related.
  Specific risks: Two parallel sessions touch the same wiki pages or generator scripts and the late-merged one silently reverts or contradicts the earlier; queue age makes the human's review context stale ("why did I make this?"); a burst of agent productivity converts directly into either a review backlog (blocking) or unreviewed integration (unsafe); commit-yield metrics (307/339) then incentivize more arrivals into the saturated gate.
  Mitigations available: WIP limit on unintegrated sessions (e.g., max N local queues before integration pause); daily integration cadence regardless of batch completeness; partition parallel sessions by vault region to make conflicts structurally impossible; lightweight pre-merge conflict scan (file-overlap report across queues) so queue risk is visible, not presumed absent.
  STEELMAN:
    Strongest counterargument: This is not a multi-developer trunk: one human owns the canon, sessions are mostly additive (new wiki notes, new result files) with naturally disjoint file sets, and git handles additive merges trivially. For append-heavy knowledge work, queue age carries little conflict risk, and the attended gate's value is judgment, not throughput — a backlog is an acceptable buffer, not a failure.
    What would need to be true for C2A2 to be safe: Parallel sessions write to disjoint paths (enforced, not assumed); shared artifacts (generator, for_lit_search.md, narration HTML) are single-writer; gate arrival rate stays within the human's sustainable review capacity; queue age is bounded by a cadence rule.
    How to test: Measure file-set overlap across the current parallel queues; track median queue age and gate throughput for two weeks — rising age with constant throughput confirms the saturation dynamic.
  Search scope: 1 WebSearch ("delayed integration batch size risk merge conflicts increase with branch age continuous integration small batches evidence").
  Recommendation: CHALLENGED
