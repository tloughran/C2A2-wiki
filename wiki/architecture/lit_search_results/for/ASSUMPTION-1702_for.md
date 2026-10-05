SEARCH-FOR-ASSUMPTION-1702:
  Date searched: 2026-09-30
  Original item: ASSUMPTION-1702
  Original statement: A frozen artifact and a quiet upstream are indistinguishable without a standing rebuild/heartbeat.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1702
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from fef2bbcb task text.
      15a: Searched for supporting literature (scheduled run 2026-09-30; depth: web search + selective fetch; sources marked 'search-result level' were not read in full)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Dhandala, N., 2026. "How to Set Up Heartbeat and Dead Man's Switch Alerts." OneUptime blog. — Threshold alerting returns empty, not zero, when a series stops arriving, so silence triggers nothing; heartbeats ("I am alive") and always-firing dead man's switches routed to an external watchdog are the remedy, and should be tested periodically. Direct practitioner statement of the claim. (fetched)
    2. Practitioner literature on dead man's switches (crontap.com, dev.to "When your monitor dies, who watches the watcher?", odown.com, updog.watch, 2025-2026). — "From an outside perspective, a dead system is indistinguishable from a quiet one"; fix is to alert on absence of an expected signal, judged off-machine. (search-result level)
    3. Beyer, B. et al. (eds.), 2016. Site Reliability Engineering (O'Reilly), Ch. 6 "Monitoring Distributed Systems" (Ewaschuk). — Distinguishes black-box probing of externally visible behaviour from white-box metrics; black-box probes detect "not working right now" states that passive signals may not reveal. Supports active probing (a standing rebuild is an active probe) over passive observation. (fetched)
    4. Background knowledge (not fetched this run): Fischer, Lynch & Paterson, 1985, "Impossibility of Distributed Consensus with One Faulty Process," JACM; Chandra & Toueg, 1996, "Unreliable Failure Detectors for Reliable Distributed Systems," JACM. — In asynchronous systems a crashed process cannot be distinguished from a slow one by passive observation; failure detectors built on heartbeats/timeouts are the standard mechanism. Formal theoretical grounding for the indistinguishability claim.

  Strength of support: Strong

  Summary: Distributed-systems theory establishes that, without timing assumptions and active signals, a failed component and a slow/quiet one are observationally equivalent; heartbeat-based failure detectors are the canonical resolution. Monitoring practice converges on the same point: absence of data does not fire alerts, so a dead pipeline and a quiet one look alike unless an expected signal (heartbeat, always-firing alert, or active probe) is required. The wiki's Phase 5.6 rationale is a direct instance of this well-established principle.

  Caveats: The practitioner sources are blogs, not peer-reviewed; the formal results are cited from background knowledge. The literature supports "a heartbeat or active probe is needed", not specifically "only a standing rebuild" — lighter mechanisms (upstream freshness checks, synthetic canary inputs, external watchdog pings) also close the gap. Heartbeats themselves only give eventual, timeout-based detection and must be off-machine to avoid shared failure.

  Recommendation: SUPPORTED
