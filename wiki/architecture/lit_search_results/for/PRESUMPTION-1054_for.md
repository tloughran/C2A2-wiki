SEARCH-FOR-PRESUMPTION-1054:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1054
  Original statement: Liveness is not progress; a monitoring regime that watches for dead processes is
    blind to hung ones, and the blindness is silent by construction.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-1054
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Inferred from 15d's stated inability plus this pass's three-probe measurement.
      15a: Searched for supporting literature on liveness/progress and watchdog blind spots.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Distributed-systems liveness theory (Aeron, "Liveness Detection," distributed-systems-basics;
       and "Ensuring liveness properties of distributed systems: Open problems," *Journal of Logical and
       Algebraic Methods in Programming*, ScienceDirect S2352220817302006 / arXiv:1912.05616). —
       Makes exactly 14b's distinction formal: a liveness property states that *progress occurs*, and
       "without a progress assumption no meaningful liveness property can be established." Progress is
       the primitive; heartbeat-style liveness is a proxy for it, and the two come apart.
    2. Heartbeat/failure-detector practice literature (Aeron docs; Singh, "Heartbeat: How Distributed
       Systems Know You're Still Alive"; systemdesignhandbook heartbeat guide). — States the failure
       mode in the terms 14b used: a server can freeze while "still listening on the network, still
       responding to pings, but completely unable to process requests." The heartbeat reports healthy.
       This is the hung-vs-crashed blindness, named as a known limitation of the design.
    3. Hierarchical watchdog mechanisms for systemic fault awareness on distributed systems
       (ResearchGate 270455282). — Motivates multi-level watchdogs precisely because a single
       liveness signal at one level cannot witness stalled progress at another.

  Strength of support: Strong

  Summary: This is textbook distributed systems, and the literature states the presumption almost
    verbatim. Liveness-by-heartbeat detects crash-stop failures; it does not detect a process that is
    alive and making no progress, and the standard remedy is a *progress* witness (a monotonic counter,
    a work-completed watermark, an end-to-end probe) rather than an aliveness witness. The "silent by
    construction" clause is also supported: the failure produces no signal at all, which is why the
    literature classes it with silent/Byzantine-adjacent faults rather than with detectable crashes.

  Caveats: None material to the general claim. The one scope note: the literature's remedies assume the
    monitor can observe a progress quantity. For C2A2 the natural quantity exists and is already being
    read by hand (turn count, trailing message, last-written run section in `lit_search_returns.md`), so
    the gap is not conceptual but unimplemented. Comprehensive search on the principle.

  Recommendation: SUPPORTED
