SEARCH-AGAINST-PRESUMPTION-846:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-846
  Original statement: [inferred] That a pipeline's absence is self-announcing — that monitoring
    scoped to artifact freshness can detect a job that never started.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-846
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by asking which instrument in the fleet takes a non-event as its subject.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive. Queries: "Alpern Schneider 1985 defining liveness safety
    property finite trace cannot falsify liveness"; "alerting on absence of events negative
    alerting cron job monitoring push-based heartbeat limitations"; "freshness SLO staleness
    monitoring data pipeline cannot detect job never scheduled scheduler down missing expected
    run"; "gray failure differential observability"; "Chandra Toueg unreliable failure
    detectors". Venues: Information Processing Letters, JACM, HotOS/ACM, Datadog, Better Stack,
    data-observability vendor documentation, practitioner blogs. Date range 1985–2026.
    Gaps: the theory (liveness) and the practice (freshness monitoring) are rarely connected
    in one source; the bridge below is my synthesis, and I flag it as such rather than
    attributing it to any cited author.

  Challenging evidence found: Yes

  Sources:
    1. Alpern & Schneider, 1985. "Defining Liveness." Information Processing Letters.
       https://www.cs.cornell.edu/fbs/publications/DefLiveness.pdf
       (ScienceDirect pii 0020019085900560) [volume/pages unverified]
       — The formal result that bites here: a safety property can be definitively refuted by a
       finite prefix of a trace, whereas *no finite prefix can refute a liveness property*,
       because any finite prefix can be extended so as to satisfy it. "The job eventually
       runs" is a liveness property. No amount of observed silence logically establishes that
       the job will not run; detection is only possible by *imposing a deadline*, i.e.
       converting the liveness property into a safety property with an explicit time bound.
       FULL-TEXT (PDF available); the characterisation quoted was confirmed in search results.
    2. Chandra & Toueg, 1996. "Unreliable Failure Detectors for Reliable Distributed Systems."
       Journal of the ACM. DOI 10.1145/226643.226647. — The same problem in operational form:
       it is impossible to distinguish a failed process from a slow one in an asynchronous
       system, and accuracy can never be guaranteed. A late job and a job that never started
       are the same observation until a timeout is declared. ABSTRACT-ONLY.
    3. Huang et al., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS '17.
       DOI 10.1145/3102980.3103005. — Differential observability: the observer sees healthy
       while the system is unhealthy. Freshness monitoring that only reads artifacts is an
       observer positioned where this gap is widest. ABSTRACT-ONLY.
    4. Datadog, "Data pipeline monitoring 101: Tracking health and performance across the data
       stack." https://www.datadoghq.com/blog/data-pipeline-monitoring/
       — Recommends alerting on skipped *scheduler* heartbeats and on jobs that do not begin
       on time by comparing expected start times against actual start times. This is an
       explicit statement that artifact-level monitoring is not the instrument for a
       never-started job; you need a declared expected schedule. FULL-TEXT.
    5. Practitioner statement of the converse failure — "it's often not enough to monitor
       pipeline jobs, since a job could run successfully but produce no new data," recovered
       from the data-pipeline-monitoring result set (see Datadog and Pantomath,
       https://www.pantomath.com/guide-data-observability/data-pipeline-monitoring).
       — Establishes that job status and artifact freshness are *independent* signals: neither
       implies the other. A freshness-only monitor therefore cannot separate "ran and produced
       nothing," "ran and failed," "started and hung," and "never started." SNIPPET-ONLY.
    6. Better Stack, "Cron and heartbeat monitor" documentation.
       https://betterstack.com/docs/uptime/cron-and-heartbeat-monitor/
       — The working design requires a *declared expected interval plus grace period* held by
       an external monitor; the missing ping is the alert. The declaration is the load-bearing
       part: without an expected-set, absence has nothing to be absent from. FULL-TEXT.
    7. Cron-monitoring practitioner literature on the three background-job failure modes —
       "they don't run at all, they run but fail silently, or they run forever" — with the
       observation that external polling and log scraping each miss at least one of the three
       (recovered across the cron-monitoring result set, e.g.
       https://www.upti.my/blog/designing-heartbeat-monitoring-system,
       https://onlineornot.com/cron-job-monitoring). SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The presumption fails on both theoretical and practical grounds. Theoretically,
  "the job eventually runs" is a liveness property, and Alpern and Schneider's characterisation
  says liveness properties cannot be refuted by any finite observation — absence is never
  self-announcing; it becomes detectable only when a deadline converts it into a safety
  property that a finite trace can violate. Practically, freshness monitoring reads the wrong
  variable: a stale artifact is consistent with at least four distinct causes (never scheduled,
  scheduled but failed, ran and correctly produced nothing, still running), and the vendor
  literature is explicit that job-run status and data freshness are independent signals.
  Freshness monitoring is also downstream in time — its detection latency is bounded below by
  the freshness threshold, so it is structurally a slow instrument for the one failure mode
  where speed matters. The standard design replaces the inference with a declaration: an
  external monitor holds the expected schedule plus a grace period, and the missing check-in
  is itself the alert. Nothing in the searched literature supports the presumption as stated.

  Specific risks: If this presumption is false, the C2A2 fleet has no instrument whose subject
  is a non-event, and the class "job never started" is undetectable in principle rather than
  merely missed in practice. That class includes the highest-impact and most plausible causes:
  a dropped or paused schedule entry, a scheduler that is itself down, a credential expiry at
  startup, a host that never came back. Detection then depends on a human eventually noticing
  a missing artifact — which is exactly what the five-day review-page gap on the sibling item
  looks like. Worse, freshness thresholds are usually set generously to avoid false alarms, so
  the presumption produces a monitoring system that is quietest precisely when the pipeline
  has stopped entirely, and a stale artifact will be misattributed to "nothing to report"
  rather than "nothing ran."

  Mitigations available:
    - Declare the expected set: register each job's schedule with an external monitor holding
      an interval plus grace period, so a missed run is a positive alert (Better Stack cron
      and heartbeat docs; Datadog expected-vs-actual start-time comparison).
    - Monitor the *scheduler's* heartbeat separately from the jobs, and alert on skipped
      scheduler heartbeats (Datadog).
    - Emit a start-of-run signal, not only an end-of-run artifact, so "never started" and
      "started and died" are distinguishable (implied by the three-failure-mode taxonomy in
      the cron-monitoring literature).
    - Instrument all three of scheduler liveness, job start/finish, and artifact freshness,
      and treat them as independent — none substitutes for another (Datadog; Pantomath).
    - Accept that the deadline is a design choice, not a discovery: pick the grace period
      deliberately, because it *is* the detection latency (follows from Alpern & Schneider's
      safety/liveness split and from Chandra & Toueg's accuracy/completeness trade-off).

  STEELMAN:
    Item: PRESUMPTION-846
    Strongest counterargument: Absence has no timestamp. Every instrument that fires does so
    on receipt of something; a job that never started produces nothing to receive, so it can
    only be detected by an observer that already knew what to expect and when. Alpern and
    Schneider make this precise: no finite observation can refute "it will eventually run," so
    detection requires an externally supplied deadline that turns the liveness claim into a
    checkable safety claim. Artifact freshness cannot supply that deadline, because a stale
    artifact is equally consistent with a job that ran correctly and had nothing to write —
    the signal is ambiguous at exactly the point where it needs to be decisive. The presumption
    therefore asks a downstream, ambiguous, high-latency signal to do the work of an upstream,
    declarative, low-latency one.
    What would need to be true for C2A2 to be safe: (a) an expected-run registry exists
    outside the jobs, listing every scheduled job and its interval; (b) each job emits a
    start-of-run signal as well as an artifact; (c) the monitor alarms on a *missing* expected
    signal within a deliberately chosen grace period; (d) the pipeline genuinely cannot
    produce an empty-but-correct result — or, if it can, an explicit "ran, produced nothing"
    record distinguishes that case from silence; (e) the freshness threshold is short enough
    relative to the run interval that staleness is unambiguous.
    How to test: Delete the schedule entry for one job entirely and measure time-to-alert.
    Then, separately, let the job run normally but produce zero output, and check whether the
    monitoring reports the same thing in both cases. If the two scenarios are
    indistinguishable to the monitoring, or if the deleted-schedule case produces no alert
    within the intended window, the presumption is falsified. A third variant: stop the
    scheduler itself and see whether anything notices.

  Recommendation: CHALLENGED
