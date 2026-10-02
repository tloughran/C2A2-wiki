SEARCH-AGAINST-PRESUMPTION-1104:
  Date searched: 2026-10-02
  Original item: PRESUMPTION-1104
  Original statement: Shared files edited by independently scheduled agents are safe without read-before-write, locks or merge.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1104
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across four 2026-10-01 sessions.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. "Language Model Teams as Distributed Systems", 2026. arXiv:2603.12229. https://arxiv.org/pdf/2603.12229 [fetched] — LLM agents on shared repos silently overwrite each other's work; decentralized teams median 19 test failures vs 4 preassigned (p<0.001), speedup 0.88x vs 1.36x.
    2. Meiklejohn, 2026. "Multi-Agent Systems Have a Distributed Systems Problem". https://christophermeiklejohn.com/ai/agents/distributed/zabriskie/2026/03/30/multi-agent-systems-have-a-distributed-systems-problem.html [search-snippet]
    3. alex_spinov, "Lost update when two AI agents edit one file". https://dev.to/alex_spinov/lost-update-when-two-ai-agents-edit-one-file-one-silently-wins-21n3 [search-snippet]
    4. Monperrus, "lost update problem humans ai agents". https://www.monperrus.net/martin/lost-update-problem-humans-ai-agents [search-snippet]

  Strength of challenge: Strong

  Summary: The lost-update problem is textbook, and the 2026 study shows it occurs empirically in LLM agent teams writing shared files. Safety without read-before-write, locks or merge holds only if writes never overlap (disjoint files, spaced schedules) or files are append-only. In-house corroboration: the 2026-10-01 concurrent lit-pipeline run overwrote the other run's eight result files.

  STEELMAN: Independently scheduled agents with no coordination are exactly where read-modify-write races occur. Failures are silent (one version wins), so they go unnoticed. Cron spacing only lowers probability because agent runs have long, variable duration. Safety needs a structural guarantee (unique-owner files, append-only logs, atomic rename, version check), not assumed non-collision.

  Caveats: Test setting was concurrent agents on code, with higher contention than a sparse cron system; if each file has a single writer the presumption could hold.

  Search scope: preliminary search — broader search recommended (no file-locking-in-cron or CRDT-adoption search); web-only; independent of 15a — 15a results were not read by the 15b searcher.

  Recommendation: CHALLENGED
