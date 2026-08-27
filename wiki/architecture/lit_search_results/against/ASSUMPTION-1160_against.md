SEARCH-AGAINST-ASSUMPTION-1160:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1160
  Original statement: That a fleet of unattended scheduled jobs can be made observable by
    per-job self-reporting, when the observed failure mode is jobs that die before
    they can report — including the job whose purpose is detecting that.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1160
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from four null runs including the health check, with its own
        anti-silence clause quoted against its own silence.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive for the practitioner/SRE literature and adequate for the
    theory. Queries: "who watches the watchmen monitoring self-monitoring fails silently
    dead man's switch"; "fail-silent versus fail-stop failure model taxonomy silent failure
    detection"; "alerting on absence of events push-based heartbeat limitations";
    "gray failure differential observability HotOS 2017"; "Chandra Toueg unreliable failure
    detectors impossibility"; "Prometheus Watchdog Dead Man's Snitch end-to-end alerting
    pipeline"; "Google SRE monitoring distributed systems black box symptom versus cause".
    Venues: HotOS/ACM, JACM, Google SRE Book, PromLabs/Prometheus operator runbooks,
    PagerDuty, vendor and practitioner engineering blogs. Date range 1991–2026.
    Gaps: no controlled empirical study measuring self-report coverage rates for cron
    fleets specifically; industry claims are architectural arguments plus incident
    anecdote, not measured detection-rate data.

  Challenging evidence found: Yes

  Sources:
    1. Huang, Guo, Zhou, Lorch, Dang, Chintalapati, Yao, 2017. "Gray Failure: The Achilles'
       Heel of Cloud-Scale Systems." HotOS '17, ACM. DOI 10.1145/3102980.3103005.
       — Defines *differential observability*: the system's own failure detectors report
       healthy while the system is in fact unhealthy. This is exactly the structure of a
       self-reporting job fleet, and the paper's central claim is that this class of failure
       is the dominant one at scale, not an edge case. ABSTRACT-ONLY (plus SNIPPET of the
       differential-observability definition and gray-failure examples).
    2. Chandra & Toueg, 1996. "Unreliable Failure Detectors for Reliable Distributed
       Systems." Journal of the ACM. DOI 10.1145/226643.226647 (preliminary version PODC '91,
       DOI 10.1145/112600.112627). — Establishes that in an asynchronous system a crashed
       process cannot be reliably distinguished from a slow one; accuracy of failure
       detection can never be guaranteed. An in-band self-report is a strictly weaker
       instrument than the failure detectors this paper already proves insufficient.
       ABSTRACT-ONLY.
    3. Classical failure-model taxonomy (fail-stop vs. fail-silent / omission), as summarised
       in multiple distributed-systems course and survey materials, e.g. Savaş, CS403/534
       Fault Tolerance lecture notes, Sabancı University
       (https://people.sabanciuniv.edu/erkays/cs403/Chapter_7a.pdf). — The taxonomy's own
       distinction is that under fail-silent failure "the client cannot tell what went
       wrong", whereas fail-stop is detectable *by an external observer via heartbeat*.
       The assumption implicitly assumes a fail-stop-with-self-announcement model that the
       taxonomy says does not come for free. SNIPPET-ONLY.
    4. PromLabs, "Metrics-based meta-monitoring: end-to-end watchdog alerts."
       https://training.promlabs.com/training/monitoring-and-debugging-prometheus/metrics-based-meta-monitoring/end-to-end-watchdog-alerts/
       and kube-prometheus runbook for the `Watchdog` alert,
       https://runbooks.prometheus-operator.dev/runbooks/general/watchdog/
       — The mainstream production answer is an *always-firing* alert routed to an
       *external* service that alarms on its absence. The design explicitly refuses to let
       the monitoring stack be its own witness. FULL-TEXT (docs).
    5. Rajhi, "Never Get Caught Blind: Securing Your Monitoring Stack with a Dead Man Switch."
       https://seifrajhi.github.io/blog/securing-monitoring-stack-dead-man-switch/
       — States the requirement directly: the dead man switch must be an *independent*
       watchdog, and meta-monitoring must be hosted on isolated infrastructure, not in the
       same cluster as the stack it watches. FULL-TEXT.
    6. Beyer, Jones, Petoff, Murphy (eds.), 2016. Site Reliability Engineering, ch.
       "Monitoring Distributed Systems." https://sre.google/sre-book/monitoring-distributed-systems/
       — White-box monitoring "depends on the ability to inspect the innards of the system";
       Google pairs it with black-box monitoring precisely because white-box signals go dark
       with the system that emits them. FULL-TEXT.
    7. PagerDuty, "Who watches the watchmen?" https://pagerduty.com/blog/watches-watchmen
       — Practitioner statement of the failure mode: when the primary monitoring tool
       crashes, downtime becomes invisible; the failure is silent by construction.
       SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The literature does not merely doubt this assumption — it names the failure and
  has a standard remedy that the assumption omits. Per-job self-reporting is white-box,
  in-band instrumentation: it is co-located with, and dependent on, the thing it reports on,
  so any failure that destroys the job also destroys the report. Huang et al.'s gray-failure
  work generalises this into *differential observability* and argues it is the dominant
  availability killer at scale, while Chandra and Toueg's result shows that even purpose-built
  external failure detectors cannot be perfectly accurate in an asynchronous system — an
  in-band self-report is weaker still. The recursion the item flags (the health check being
  one of the silent jobs) is the exact case the dead-man's-switch / watchdog pattern exists to
  break, and every practitioner source insists the watchdog be externally hosted and
  absence-triggered. The claim as stated is contradicted; the correct form is "self-reporting
  observes *some* failures, and only an external absence-detector observes death."

  Specific risks: If this claim is false and C2A2 relies on it, the fleet has a systematic
  blind spot with exactly the wrong shape: the more severe the failure (process killed,
  host gone, scheduler stopped, credentials revoked at startup), the less likely it is to be
  reported, so observed reliability rises as actual reliability falls. Silence is read as
  health. The health-check job's own silence is indistinguishable from "nothing to report,"
  so the instrument certifies the fleet at exactly the moment it has stopped looking. Mean
  time to detection becomes unbounded — bounded in practice only by a human noticing a
  missing artifact days later, which is what four null runs already demonstrated.

  Mitigations available:
    - External dead-man's switch / watchdog: an always-firing signal routed to a third-party
      service that alarms on *absence*, hosted off the failing infrastructure (PromLabs
      end-to-end watchdog alerts; kube-prometheus `Watchdog` runbook; Rajhi, isolated-
      infrastructure requirement).
    - Heartbeat/cron-monitoring with declared expected interval plus grace period, so a
      missed check-in is itself the alert rather than requiring a positive error report
      (standard cron-heartbeat design; see e.g. Better Stack cron and heartbeat monitor docs,
      https://betterstack.com/docs/uptime/cron-and-heartbeat-monitor/).
    - Pair white-box self-reports with black-box symptom checks so at least one signal does
      not share a fate with the job (Beyer et al., SRE Book, monitoring chapter).
    - Accept imperfect detection explicitly and design for false suspicion rather than for a
      perfect detector (Chandra & Toueg: completeness and accuracy trade off; detectors that
      make infinite mistakes are still useful).

  STEELMAN:
    Item: ASSUMPTION-1160
    Strongest counterargument: Self-reporting is structurally incapable of covering its own
    negation. A report is an event emitted by a live process; the failure mode of interest is
    the absence of a live process; no quantity of emitted events constitutes evidence about
    an event that was never emitted. This is not an implementation shortfall that better
    per-job logging would fix — it is a category error about what an in-band instrument can
    witness, and Huang et al. show that the resulting differential observability is where
    real outages live. Worse, the assumption is self-undermining under recursion: the
    detector-of-silence is itself a job that can fall silent, so the architecture's guarantee
    is only as good as an unguarded base case that four null runs have already shown to be
    unguarded.
    What would need to be true for C2A2 to be safe: (a) at least one absence-detecting
    observer exists outside the fault domain of the jobs it watches — different process,
    different host, different credential, ideally a third-party service; (b) that observer's
    trigger is a *timeout*, not a received error; (c) the expected set of runs is declared in
    advance so "no report" is comparable against "a report was due"; (d) the outermost
    observer's own liveness is guaranteed by a party outside the system (a human-visible
    recurring signal, or a commercial uptime service whose business is being up).
    How to test: Run a chaos drill — SIGKILL a scheduled job mid-run, and separately disable
    the scheduler entry entirely, and measure time-to-alert for each. Then repeat the drill
    against the health-check job itself. Any of these three that produces no alert within the
    declared detection window falsifies the assumption directly. A cheaper offline test:
    enumerate every alerting path and ask, for each, "which process must be alive for this
    alert to fire?" — if the answer is ever the process being monitored, that path is
    self-referential.

  Recommendation: CHALLENGED
