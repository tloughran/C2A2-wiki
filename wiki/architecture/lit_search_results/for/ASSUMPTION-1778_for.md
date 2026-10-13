SEARCH-FOR-ASSUMPTION-1778:
  Date searched: 2026-10-13
  Original item: ASSUMPTION-1778
  Original statement: Do health checks that verify "a record exists" rather than "the record is fresh" systematically
    miss silent failures, and what liveness/heartbeat designs (dead-man switches, watchdog-of-watchdog) prevent it?

  Premise tested: Existence checks miss silent failures (a stale record still "exists"), so C2A2 monitoring needs
    freshness/liveness checks, i.e. alerting on the ABSENCE of a recent signal, plus an independent check on the
    monitor itself.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1778
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-10-12 transcripts, where a health check confirmed a record was present but not that it
        was recent; queued 2026-10-12
      15a (2026-10-13): 4 web searches (dead-man switch / heartbeat monitoring; SRE freshness monitoring for data
        pipelines; gray failure / differential observability; Prometheus Watchdog meta-monitoring) plus 1 on failure
        detector theory. No fetches for this item; all evidence from search-result summaries (abstract level or lower).
    Current status: SUPPORTED (Moderate-to-Strong)

  Search scope: PRELIMINARY. Practitioner SRE material, one distributed-systems position paper, one foundational
    theory paper. No peer-reviewed empirical study comparing existence vs freshness checks was found.

  Supporting evidence found: Yes

  Sources:
    1. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M., Yao, R., 2017. "Gray Failure: The
       Achilles' Heel of Cloud-Scale Systems." HotOS XVI (Microsoft Research). [search-result summary] Defines gray
       failure as "differential observability": the system's own failure detector reports healthy while clients see
       failure. Relevance: theoretical grounding. A check that tests a weaker property (record exists) than the one
       consumers depend on (record is current) is a textbook way to produce this gap.
    2. Skorikov, A. (Google), 2021. "Horizontal Data Freshness Monitoring in Complex Pipelines." SREcon21 talk and
       slides. [search-result summary] Calls data staleness one of the outage classes teams are least prepared for,
       and proposes explicit freshness monitoring across the dependency graph to catch "slow bleeds". Relevance:
       direct practitioner support that freshness, not presence, is the property to monitor.
    3. Prometheus-operator / kube-prometheus "Watchdog" runbook; PromLabs training "End-to-End Watchdog Alerts".
       [search-result summary] An always-firing alert is routed to an external dead-man service (e.g. Dead Man's
       Snitch); silence triggers a page. The rationale given: a monitoring system cannot reliably report its own
       failure, so the checker must not depend on the monitored stack. Relevance: established watchdog-of-watchdog
       pattern, matching the second half of the item.
    4. Healthchecks.io / Cronitor-style cron heartbeat monitoring (several vendor guides, e.g. onlineornot.com,
       notifier.so). [search-result summary] A job that never runs leaves nothing to log; only alerting on a missing
       ping (expected interval + grace period) catches it. Guidance includes one heartbeat per pipeline step. Relevance:
       empirical practice; vendor sources, so not independent evidence.
    5. Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed Systems." JACM 43(2):
       225-267. [search-result summary] Frames failure detection by completeness (crashed processes are eventually
       suspected) and accuracy. Heartbeat/timeout detectors are the usual way to get completeness. A presence-only
       check gives no completeness for a process that stops updating. Relevance: theoretical framing. The specific
       heartbeat mechanics were not checked in the paper itself.

  Strength of support: Moderate-to-Strong (strong practitioner consensus plus a theoretical framing; weak
    peer-reviewed empirical base)

  Summary: SRE and distributed-systems sources agree on the premise. Silent failures, such as a job that never runs
    or data that stops updating, are invisible to checks that test only for presence. The standard remedies are
    heartbeat / dead-man-switch monitoring (alert on a missing signal within a deadline) and external meta-monitoring
    (an always-firing Watchdog alert whose silence pages someone). Gray-failure research gives the general principle:
    detectors that observe a different or weaker property than consumers rely on will report healthy during failure.
    C2A2's move from "record exists" to "record is fresh" fits standard practice.

  Caveats: (i) Most evidence is practitioner or vendor guidance, not controlled study. (ii) Heartbeats show liveness,
    not correctness. A job can ping on schedule while producing bad output (gray failure again), so freshness is
    necessary but not sufficient. (iii) Sources stress that the watchdog must be independent of the watched system,
    and a co-located watchdog inherits common-mode failure (see PRESUMPTION-1125). (iv) Timeout/grace settings trade
    false alarms against detection latency (see PRESUMPTION-1127).

  NOVELTY flag: None. The pattern is well established.

  Recommendation: SUPPORTED (Moderate-to-Strong). Preliminary search. A broader search could cover the SRE Workbook
    "Data Processing Pipelines" chapter (not retrieved) and Panorama (Huang et al., OSDI 2018).
