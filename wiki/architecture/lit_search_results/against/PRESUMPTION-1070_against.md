SEARCH-AGAINST-PRESUMPTION-1070:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1070
  Original statement: Monitoring systems that report status without checking the age of the
    status datum produce stale-alarm errors at predictable rates.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1070
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the health run's timing (≈06:03) against the refresh (06:15) and the
           line it quoted.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (that age-unchecked status reporting produces stale
      errors is corroborated; "at predictable rates" is challenged as a boundary condition)

  Challenging evidence found: Partial

  Sources:
    1. Prometheus documentation, "Querying basics" (prometheus.io), and Brazil, B. (2017).
       "Staleness and Isolation in Prometheus 2.0." PromCon Munich (slides). Also Robust
       Perception, "Staleness and PromQL." Before stale markers, Prometheus kept returning the
       last sample for up to the 5-minute lookback window, a textbook stale-status error. This
       CORROBORATES the mechanism. It also shows that mature monitoring stacks now check datum
       age by default (stale markers, a configurable lookback delta). So the claim applies to
       hand-built or naive monitors, not to monitoring systems in general.
    2. "Update or Wait: How to Keep Your Data Fresh." (IEEE INFOCOM 2016; the title was
       confirmed by search, and the author list Sun, Uysal-Biyikoglu, Yates, Koksal & Shroff is
       [unverified — from background knowledge]). Also "Age of Information: An Introduction
       and Survey" (PDF hosted by the Ulukus group, UMD), and "Overage and
       Staleness Metrics for Status Update Systems" (arXiv:2109.14062). The Age-of-Information
       literature formally defines "stale update probability" and gives closed forms for it
       under stationary queueing models. That supports "predictable." It also shows that with
       heavy-tailed or highly random service times, simple policies fail and staleness depends
       strongly on the timing process. Rates are predictable only if the update and query
       processes are stationary and known.
    3. "An Empirical Study of Production Incidents in Generative AI Cloud Services."
       arXiv:2504.08865 (2025). Reports an 11.0% false-alarm rate for monitor-detected
       incidents and 38.3% of incidents detected by humans rather than monitors. In the causes
       reported for alert fatigue (ScienceDirect 2024, "Mitigating Alert Fatigue in Cloud
       Monitoring Systems: A Machine Learning Perspective"), threshold sensitivity and policy
       design dominate. Stale data is not singled out as a main cause of false alarms in these
       sources, which limits how much weight stale-alarm errors can carry.

  Strength of challenge: Weak

  Summary: Nothing found contradicts the core mechanism: a monitor that does not check the age
  of its status datum will sometimes report stale status. Prometheus's own design history is a
  documented case of it. The challenge concerns scope and predictability. (1) Industrial
  monitoring stacks have largely absorbed the fix, so the claim describes a known anti-pattern
  in custom monitors rather than a general property of monitoring systems. (2) Age-of-
  Information theory says the stale-error rate is predictable only when the relative timing of
  status checks and data refreshes is stationary. In C2A2's case (a health run at about 06:03
  against a refresh at 06:15), the rate would be close to deterministic, near 100% for that
  phase, not a stable probabilistic rate. It would change completely if the schedules drifted.
  (3) Empirical false-alarm studies attribute most false alarms to other causes.

  Specific risks: If C2A2 models stale alarms as a steady background rate, it may miss that a
  fixed schedule offset turns them into a systematic, every-run error. It may also miss that a
  small schedule change can remove or reintroduce them abruptly.

  Mitigations available: Record the source timestamp of each status datum and report its age.
  Fail closed or mark as UNKNOWN when the age exceeds a threshold, as with Prometheus stale
  markers or lookback limits. Order health checks after refreshes, or make them depend on the
  refresh completing.

  Search scope: Preliminary — 3 searches (Prometheus staleness; alert-fatigue causes;
  Age-of-Information staleness). No empirical study measured stale-alarm rates specifically.

  Excluded results: GitHub issues (grafana/tempo #6494, prometheus #11565, #398, discussion
  #9428, opentelemetry-collector-contrib #31016) as issue-tracker content rather than
  published sources; oneuptime.com and opensight.ch blog posts; vendor pages (torq.io, IBM,
  upwind.io).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1070
  Strongest counterargument: "Predictable rates" is the wrong model. When a status check and a
    data refresh run on fixed schedules, staleness is a phase relationship, not a rate. It is
    either always present (check before refresh) or never present (check after refresh), and
    it flips when either schedule moves. Age-of-Information theory gives predictable
    stale-update probabilities only for stochastic, stationary update processes, which cron-
    scheduled agents are not. The mature monitoring ecosystem also treats datum-age checking
    as a solved default, so the claim describes a local implementation defect rather than a
    systemic property.
  What would need to be true for the presumption to hold as stated: The check and refresh
    timings vary stochastically but stationarily (for example, jittered or queued runs), so the
    fraction of stale reads converges to a stable value. The monitor has no age check at all.
  How to test: Over the last N health runs, log the gap between each health-run timestamp and
  the most recent refresh completion. Plot the stale-read fraction. A step function
  (all-or-nothing by schedule phase) supports the challenge. A stable intermediate fraction
  supports the presumption.
