SEARCH-AGAINST-ASSUMPTION-1702:
  Date searched: 2026-09-30
  Original item: ASSUMPTION-1702
  Original statement: A frozen artifact and a quiet upstream are indistinguishable without a standing rebuild/heartbeat.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1702
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from fef2bbcb task text.
      15b: Searched for challenging literature (scheduled run 2026-09-30; depth: web search + selective fetch)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Wilkinson, J. (2016). "Practical Alerting from Time-Series Data." Ch. 10 in Beyer, Jones,
       Petoff & Murphy (eds.), Site Reliability Engineering, O'Reilly/Google. [Fetched: full
       chapter.] Borgmon records "synthetic" variables for each target: whether the name resolved,
       whether the target responded to a collection, and when the collection finished. Engineers use
       "the collection failure itself as a signal". Prober checks the payload from outside. Both
       separate "no new data because the collector or artifact is broken" from "no new data
       because the source is quiet" without a standing rebuild. You record whether the check ran
       and whether it reached the source, independently of the data volume.
    2. Data-observability practitioner literature (e.g., Acceldata, Sifflet, Bruin blog posts on
       data freshness, 2025-2026). [Search-result level; vendor/practitioner, not peer-reviewed.]
       Freshness is judged against learned arrival patterns and combined with volume monitoring and
       lineage. Source-side freshness shows whether the upstream is quiet. Downstream freshness
       shows whether the artifact is frozen. Comparing the two distinguishes the cases.
    3. Heartbeat-monitoring practitioner sources (e.g., drumbeats.io "Heartbeat Monitoring";
       crontap.com "Dead man's switch, explained"; lennney.com "Silent Jobs: Designing Health Checks
       Without False Positives"). [Search-result level; practitioner.] These sources point the
       other way on sufficiency. A liveness heartbeat can keep firing while the worker is stuck,
       and an untested dead man's switch "gives false confidence". A heartbeat or rebuild is not
       enough unless it checks progress (new content), not just that the process ran.

  Strength of challenge: Moderate

  Summary: The literature challenges the strong form ("indistinguishable ... only a standing rebuild
    closes it") in two directions. On necessity, established monitoring practice separates the two
    states cheaply. It probes the upstream directly for its latest timestamp or item, records
    whether each collection succeeded, and compares source-side with artifact-side freshness. On
    sufficiency, a heartbeat or rebuild that runs successfully while re-emitting stale input
    reproduces the ambiguity, which is the stuck-but-alive failure. The core intuition is not
    refuted: freshness alone cannot tell the cases apart, and some independent second signal is
    needed. The literature disputes the claim that the rebuild is the only such signal, and that it
    is sufficient.

  Specific risks: C2A2 invests in a standing rebuild that mirrors the pipeline. If the rebuild reads
    the same frozen intermediate, it reports "fresh" (for example, 1611 signals, span to 09-23)
    while the upstream has moved on. Meanwhile the direct test (ask the upstream for its newest
    item) is never built. The 21-day warning threshold also exceeds normal cadence, so a frozen
    artifact can go undetected for up to three weeks.

  Mitigations available: Add an upstream probe that records the latest upstream timestamp or ID
    independently of the artifact, and alert when upstream_latest > artifact_latest. Log collection
    success separately from content count. Make the heartbeat carry a progress value (newest item
    ID), not just "ran". Periodically test the switch by freezing a copy on purpose.

  Search scope: Preliminary: 2 searches, 1 fetch (the fetch is shared with PRESUMPTION-1096). No
    peer-reviewed study on this exact distinction was found; the evidence is engineering practice.
  Excluded results: product landing pages (oneuptime, nurbak, updog), used only as corroboration
    and not cited individually.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1702
  Strongest counterargument: The two states are only indistinguishable if you look at the artifact.
    Production monitoring solved this long ago by observing the source and the collector
    separately. Prober checks the source from outside, and synthetic "did the collection succeed"
    variables track the collector. A standing rebuild is neither necessary nor sufficient. If it
    reads the same stale intermediate, it succeeds while re-emitting a frozen state, the
    stuck-but-alive failure that heartbeat practitioners warn about. Framing the rebuild as the only
    fix sends effort toward redundancy instead of an independent observation of the upstream.
  What would need to be true for C2A2 to be safe: The rebuild re-reads the true upstream (not a
    cached intermediate) and asserts progress (a new max ID or date), or the upstream cannot be
    queried directly.
  How to test: Freeze the artifact's input on purpose for one cycle and check whether the rebuild,
    and separately a direct upstream probe, detect it.
