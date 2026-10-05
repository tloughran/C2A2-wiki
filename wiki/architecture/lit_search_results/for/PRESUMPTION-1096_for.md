SEARCH-FOR-PRESUMPTION-1096:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1096
  Original statement: Monitors co-located with the monitored system give adequate coverage.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1096
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 7886254b, b5f437f2, 6f1262b0.
      15a: Searched for supporting literature (scheduled run 2026-09-30; depth: web search + selective fetch; sources marked 'search-result level' were not read in full)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Ewaschuk, R., 2016. "Monitoring Distributed Systems," Ch. 6 in Beyer et al. (eds.), Site Reliability Engineering (O'Reilly). — Google "combine[s] heavy use of white-box monitoring with modest but critical uses of black-box monitoring". White-box (internal, co-located) instrumentation catches imminent problems and failures masked by retries, and "monitoring saturation and performance of subsystems such as databases often must be performed directly on the subsystem itself". The same chapter keeps black-box probing for paging on active symptoms. (fetched)
    2. Google SRE, Ch. 10 "Practical Alerting" (Prober). — Probers are pointed both at the frontend and behind the load balancer, so monitoring runs at several layers rather than being wholly external. (search-result level)
    3. Background knowledge (not fetched this run): widespread practice of on-host agents (node_exporter, collectd, cron self-checks) as the main source of host metrics such as disk, CPU and processes.

  Strength of support: Weak

  Summary: Practice does support co-located (white-box) monitoring as the main and often the only feasible source of resource-level signals such as disk, memory and process state. The leading SRE reference says such subsystem metrics often must be collected on the subsystem itself. That gives real support to co-located monitors as a necessary part of coverage. The same reference pairs them with external black-box checks, however, and no source found claims co-located monitors alone give adequate coverage.

  Caveats: The support is for co-located monitoring as necessary, not sufficient. No source addresses the failure mode in the item, where a shared resource failure (disk full) silences both the monitored tasks and the monitor. The sources describe large-scale production systems, while C2A2 is a single-sandbox agent setup, so domain transfer is limited. Preliminary search.

  Recommendation: PARTIALLY-SUPPORTED
