SEARCH-FOR-ASSUMPTION-435:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-435
  Original statement: "DB write-staleness beyond threshold reliably indicates the OpenStory runtime is down, and refusing to refresh on stale data (freeze) beats serving stale feeds."
  QUEUED-EMPIRICAL: literature clause only searched; in-house empirical test out of scope for 15a.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-435
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Aguilera, Chen & Toueg, 1997/1998. "Heartbeat: A Timeout-Free Failure Detector for Quiescent Reliable Communication." Cornell TR 97-1631 / Springer LNCS. — Canonical distributed-systems result: a counter that stops increasing (i.e., goes stale) is the defining signal that the remote process has crashed. Directly supports using write-staleness as a liveness/failure signal.
    2. Bhayani, A., 2023–2024. "Heartbeats in Distributed Systems." arpitbhayani.me. — Practitioner treatment of heartbeat/timeout failure detection: absence of expected periodic writes within a timeout is the standard operational indicator that a component is down; also documents the false-positive/detection-latency tradeoff in choosing the threshold.
    3. Monte Carlo Data, 2023–2025. "Data Freshness Explained." montecarlodata.com; and Sifflet, 2024–2025. "What Is Data Freshness in Data Observability?" — Data-observability literature: freshness checks ("max timestamp newer than now minus SLA") are a first-class, widely deployed detection mechanism because stale data "introduces silent failure modes"; treating staleness as an actionable failure signal is industry standard.
    4. Tacnode, 2025–2026. "Data Freshness vs Latency: Why Fast Queries Still Return Stale Results." tacnode.io. — Identifies "fast + stale" as the dangerous quadrant: no errors, no timeouts, but every answer is outdated. Supports the claim's preference for refusing to refresh (making staleness loud) over silently serving stale feeds.
    5. AWS Well-Architected, current. "REL05-BP01: Implement graceful degradation." docs.aws.amazon.com. — Included for balance within FOR scope: mainstream guidance often prefers serving "slightly stale data" as graceful degradation, but explicitly conditions this on cases where stale data is acceptable to the business function — implying freeze is correct where stale data would mislead consumers.

  Strength of support: Moderate

  Summary: The two halves of the claim receive different levels of support. The first half — staleness of expected periodic writes as a down-detector — is strongly grounded: heartbeat/timeout failure detection is foundational distributed-systems theory (Aguilera et al.'s heartbeat counter that "stops increasing" on crash), and modern data-observability practice deploys freshness-SLA checks as primary failure detectors. The second half — freeze beats serving stale feeds — finds support in the observability literature's warning that the "fast + stale" state is the most dangerous failure mode precisely because it is silent; refusing to refresh converts a silent failure into a visible one, which is a recognized fail-loud design virtue. Circuit-breaker literature likewise endorses fail-fast rejection of requests to an unhealthy dependency rather than pretending health.

  Caveats: "Reliably indicates" overstates what the theory grants: timeout-based detectors are inherently imperfect in asynchronous systems (a too-short threshold yields false positives from slow-but-alive runtimes, network partitions, or paused schedulers — the runtime may be up while writes are stalled for other reasons). And the freeze-vs-serve-stale preference is context-dependent: a large body of resilience guidance (AWS graceful degradation, circuit breaker with cached fallback) prefers serving last-known-good data when consumers tolerate it. Support for freeze is strongest when stale feeds would silently mislead, which is the wiki's stated context.

  Search scope confidence: comprehensive for failure-detection and freshness-monitoring angles; the freeze-vs-stale tradeoff is genuinely contested in the literature

  Recommendation: PARTIALLY-SUPPORTED
