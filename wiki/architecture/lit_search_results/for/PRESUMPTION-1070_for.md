SEARCH-FOR-PRESUMPTION-1070:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1070
  Original statement: Monitoring systems that report status without checking the age of the status datum
    produce stale-alarm errors at predictable rates.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1070
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the health run's timing (≈06:03) against the refresh (06:15) and the line it
        quoted.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Google SRE Workbook, "Monitoring" chapter (sre.google/workbook/monitoring). — States that data
       freshness determines how quickly monitoring detects problems and that slow data can lead
       operators to act on incorrect information or infer false cause-effect relationships. Direct
       practitioner support for the error mechanism.
    2. Brazil, B., 2017. "Staleness and Isolation in Prometheus 2.0." PromCon Munich (slides); and
       Robust Perception, "Staleness and PromQL." — Prometheus introduced explicit staleness markers and
       a 5-minute lookback because, without them, queries returned outdated samples as current (e.g.
       double-counting after target replacement). Engineering precedent: age-of-datum checks were added
       precisely because their absence produced systematic wrong answers.
    3. Nobl9, "A Guide to SRE Metrics" (vendor guide). — "An SLI reporting 99.99% availability means
       nothing if the underlying metrics haven't updated in three hours"; advanced implementations flag
       stale measurements. Practitioner corroboration, non-peer-reviewed.
    4. [unverified — from background knowledge, not confirmed by this search] Dead-man's-switch /
       heartbeat alerting as standard practice (e.g. Prometheus "Watchdog" alert) exists to catch the
       silent-staleness failure.

  Strength of support: Moderate (for the mechanism); Weak (for "predictable rates")

  Summary: SRE and observability practice treats unchecked data age as a known source of wrong status
    reports, and major tooling (Prometheus staleness handling, freshness SLIs, heartbeat alerts) exists
    specifically to prevent it. That supports the first half of the presumption well. The "predictable
    rates" clause has only logical support: if a status check and a data refresh run on fixed schedules
    with a known offset (here ≈06:03 vs 06:15), the stale-read window is deterministic, so the error
    rate is predictable from the schedule. No empirical study quantifying stale-alarm rates as a
    function of unchecked datum age was found.

  Caveats: Sources are practitioner/engineering documentation rather than peer-reviewed studies. The
    clinical-alarm literature (72–99% false alarm rates) was reviewed but concerns artifact/brief
    threshold crossings, not staleness, and was not counted as support. Predictability depends on fixed
    schedules; with jittered or event-driven refresh the rate is stochastic.

  Search scope: Preliminary — three searches (SRE staleness/freshness; clinical alarm false-alarm
    rates; Prometheus staleness handling).

  Excluded results: GitHub PR "papoveB01/EdgeGW_Project #2" and GitHub issue "LTstripes/Health-Check
    #147" (repos whose titles closely mirror the claim — stale/silent-source health checks); glama.ai
    "freshprobe" MCP listing (no venue); GitHub issues from grafana/tempo and opentelemetry-collector
    (issue threads, not evidence).

  Recommendation: PARTIALLY-SUPPORTED
