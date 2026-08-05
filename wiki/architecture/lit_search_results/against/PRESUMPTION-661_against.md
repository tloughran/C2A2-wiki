SEARCH-AGAINST-PRESUMPTION-661:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-661
  Original statement: That a session reported as "running" is progressing — whereas four
    scheduled sessions were unchanged in turn count across three polls, and one had been
    silent for five months.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-661
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 poll showing four scheduled sessions with
        unchanged turn counts across three polls and one silent for five months
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R.,
       2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS '17,
       Microsoft Research. — Defines differential observability: the failure detector does
       not notice the problem even while applications are afflicted by it. Gray failures
       include severe performance degradation, flaky I/O and non-fatal exceptions — states
       in which a component is nominally up and materially not working.
    2. Gunawi, H.S. et al., 2018. "Fail-Slow at Scale: Evidence of Hardware Performance
       Faults in Large Production Systems." FAST '18, USENIX. — 101 fail-slow incidents
       across 12 institutions; the defining property is hardware that is "still running and
       functional but in a degraded mode." Empirical demonstration that the running/working
       distinction is not theoretical.
    3. Do, T., Hao, M., Leesatapornwongsa, T., Patana-anake, T. & Gunawi, H.S., 2013.
       "Limplock: Understanding the Impact of Limpware on Scale-Out Cloud Systems." SoCC
       '13. — Defines limplock: a system progressing slowly due to limping components and
       unable to fail over, because no failure signal is ever emitted. Benchmarked across
       Hadoop, HDFS, ZooKeeper, Cassandra and HBase; most were not limpware tolerant.
    4. Failure-detector critique in the Kubernetes/microservice health literature, e.g.
       (2025) "Signalling Health for Improved Kubernetes Microservice Availability,"
       arXiv:2507.02158, and Aeron documentation on liveness detection. — States the
       specific defect: traditional detectors assume a process is working as long as it does
       something periodically (replies to pings, sends heartbeats, maintains a session);
       this works for fail-stop and cannot detect gray failure, partial failure, limplock,
       fail-slow or state corruption.
    5. Kubernetes probe guidance (Better Stack; web-alert.io). — "TCP probes pass on
       applications that accept connections but can't serve anything, which makes them a
       weak liveness signal for hung apps." A session that holds a status field is exactly
       this case.
    6. Bronson, N. et al., 2021. "Metastable Failures in Distributed Systems." HotOS '21. —
       Relevant secondary mechanism: a system can be stuck in a self-sustaining bad state
       that persists after the trigger is gone, so a stalled session may not resume even
       though nothing is currently wrong.

  Strength of challenge: Strong

  Summary: This is among the best-established results in systems reliability and the
    literature is uniform against the presumption. "Running" is a status field, not a
    measurement of progress, and every major failure taxonomy in cloud systems — gray
    failure, fail-slow, limplock — is defined by the gap between the two. The failure-detector
    critique is the most directly applicable: detectors that infer health from the existence
    of a session or from periodic signals are documented as unable to detect precisely the
    class of failure at issue, and the item's evidence (turn count unchanged across three
    polls; five months of silence) is a textbook progress-stall signature that no
    status-field-based detector would ever raise. The five-month case is decisive on its own
    — no plausible reading of "running" survives it. What the literature adds is the general
    prescription: progress must be measured by a monotonically advancing quantity observed
    over time, and its non-advancement must be an alarm condition in its own right, because
    the absence of a failure signal carries no information about whether work is happening.

  Specific risks: Four scheduled sessions believed to be doing work are almost certainly
    doing none, and the work they were scheduled to do has silently not happened for an
    unknown period — up to five months in one case. Everything downstream that depends on
    that work is therefore stale while appearing current, and nothing will surface this,
    because the sessions report the healthy state. This interlocks badly with PRESUMPTION-646:
    a stalled session may still appear in `list_sessions`, so the presence check and the
    progress check are both wrong in the reassuring direction. It also consumes resources — a
    hung session may hold locks, queue positions or scheduler slots — and it corrupts capacity
    accounting, since C2A2 believes four workers are busy when zero are. Because there is no
    stall detector, the mean time to discovery for this failure class is currently
    unbounded and the five-month case establishes that empirically.

  Mitigations available: (1) Replace status polling with progress polling: record turn count
    (or any monotonic counter) per session per poll and alarm on no-change across N
    consecutive polls. The item's own data shows this works — it is what surfaced the problem.
    (2) Set a maximum silent interval per scheduled session and treat exceedance as a failure,
    not a status; five months should have been impossible. (3) Distinguish three states rather
    than two: RUNNING-AND-ADVANCING, RUNNING-BUT-STALLED, and NOT-RUNNING. The current
    two-state model cannot represent the observed condition. (4) Require sessions to emit
    heartbeats that carry work evidence (a counter, a last-artifact path), not bare liveness —
    per the failure-detector critique, a content-free heartbeat is exactly what limplock
    defeats. (5) Add a reaper: stalled sessions past a threshold should be terminated and
    rescheduled rather than left, since metastable stalls do not self-clear. (6) Audit now —
    enumerate every scheduled session and its last progress timestamp; the tail of that
    distribution is the current exposure.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-661
    Strongest counterargument: Turn count is a poor progress proxy — a session may be
      legitimately in a long single turn (a large tool call, a long generation, a wait on an
      external dependency), so unchanged turn count across three closely spaced polls is
      weak evidence of a stall and aggressive stall detection would kill healthy long-running
      work. Scheduled sessions may also be idle by design between triggers, in which case
      "running" correctly describes a live, waiting process, and the five-month case may be a
      dormant scheduled entry rather than a hung one. The gray-failure and fail-slow
      literature concerns systems under load with strict latency requirements; a wiki
      maintenance session has neither, so degraded progress may be entirely acceptable.
    What would need to be true for C2A2 to be safe: (a) The polls are spaced widely enough
      that no legitimate operation spans them, or a second progress signal exists that is not
      turn-based. (b) Idle-by-design and stalled are distinguishable in the data model.
      (c) A stalled session consumes no resource that a healthy one needs. (d) Someone would
      notice within a bounded time that the scheduled work was not done — which the five-month
      case falsifies.
    How to test: Immediate and cheap. For each of the four sessions, read the transcript and
      look at the last recorded activity timestamp and the content of the final turn. A turn
      that ends mid-tool-call or with no assistant response is a hang; a turn that completed
      cleanly and simply has not been followed is a scheduling failure; the two need different
      fixes. Then instrument: log turn count per session on every poll for a week and inspect
      the deltas. Zero deltas for a session whose schedule fired during the window is a
      definitive stall.

  Search scope: Adequate. Concepts searched: liveness vs progress detection; gray failure and
    differential observability; fail-slow and limpware/limplock; heartbeat failure-detector
    limitations; hung-process and stall detection; shallow liveness probes; metastable stalls.
