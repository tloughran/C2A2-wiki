SEARCH-AGAINST-ASSUMPTION-1778:
  Date searched: 2026-10-13
  Original item: ASSUMPTION-1778
  Original statement: [stated] Do health checks that verify "a record exists" rather than "the record
    is fresh" systematically miss silent failures, and what liveness/heartbeat designs (dead-man
    switches, watchdog-of-watchdog) prevent it?
  Under test: the implied design stance that existence checks miss silent failures and that
    freshness/liveness checks (heartbeats, dead-man switches, watchdog-of-watchdog) close the gap. I
    did not contest the first half, which is well supported. I searched for evidence that heartbeats
    and freshness checks are themselves proxies that miss "gray" failures, and that a liveness signal
    can be fresh while the work it vouches for is wrong.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1778
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-10-12): Extracted from 2026-10-12 transcripts (health check confirmed a record existed,
        not that it was current). Queued with the existence-vs-freshness question.
      15b (2026-10-13): Searched for challenging literature. 3 searches: gray failure / differential
        observability (Huang et al.); dead-man-switch blind spots (practitioner sources); unreliable
        failure detectors (Chandra & Toueg). 1 fetch: Huang et al. 2017 HotOS PDF (full text read).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: MIXED. Huang et al. 2017 was read in full. Huang et al. 2018 and Chandra & Toueg 1996
    are from search snippets and abstracts. Dead-man-switch material is practitioner, not peer-reviewed.
  Search scope: preliminary (3 searches, 1 fetch). Broader search recommended.

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Huang P, Guo C, Zhou L, Lorch JR, Dang Y, Chintalapati M, Yao R. 2017. "Gray Failure: The
       Achilles' Heel of Cloud-Scale Systems." HotOS '17. doi:10.1145/3102980.3103005. [fetched, full
       text] The paper defines gray failure as "differential observability": the observer judges the
       system healthy while an app judges it unhealthy. The canonical example is a heartbeat: "if a
       system's request-handling module is stuck but its heartbeat module is not, then an
       error-handling module relying on heartbeats will perceive the system as healthy." In an Azure
       incident, VM heartbeats were relayed through a host agent over local RPC, so the detector stayed
       green during a network failure inside the VM until users reported it. The authors say gray
       failure is "behind most cloud incidents". They call for moving "from singular failure detection
       (e.g., with heartbeats) to multi-dimensional health monitoring". They also show that recovery
       driven by a detector can make things worse (§2.3, a reboot loop that ended in a cascading
       failure). Bearing: a heartbeat or freshness stamp is a second proxy, one level up from "record
       exists". It catches fail-stop failures but not fail-wrong or fail-slow ones.
    2. Huang P et al. 2018. "Capturing and Enhancing In Situ System Observability for Failure
       Detection" (Panorama). OSDI '18. [snippet] The paper reproduced 15 real gray failures. Panorama,
       which uses observations made by a component's requesters, detected all 15 in under 7 s. Existing
       detectors (heartbeat-style) caught only one within 300 s. Bearing: as numbers, this is the
       strongest evidence that conventional liveness detection misses most of these failures. The fix
       is to observe from the consumer side, not to add a better heartbeat.
    3. Chandra TD & Toueg S. 1996. "Unreliable Failure Detectors for Reliable Distributed Systems."
       JACM 43(2). [abstract/snippet; the timeout argument is standard background, not quoted from the
       paper] In asynchronous systems any timeout-based detector is unreliable in both directions. It
       trades completeness against accuracy and can only be "eventually" correct. Bearing: heartbeats
       and dead-man switches give probabilistic evidence and cannot certify liveness. Thresholds that
       are too tight produce false alarms (see PRESUMPTION-1127). Thresholds that are too loose bring
       back silent windows.
    4. Practitioner dead-man-switch literature (e.g. crontap.com, dev.to "A dead man's switch for your
       monitoring stack"). [snippet, non-academic] A ping proves that the job reached the ping line,
       not that its output is correct. A heartbeat sent before output validation is "a liveness signal
       dressed up as correctness". A monitor that shares infrastructure with what it monitors inherits
       that infrastructure's blind spots. Bearing: a watchdog-of-watchdog adds coverage only if it is
       independent of the watched path, which links to PRESUMPTION-1125.

  Summary: The literature agrees that existence checks miss silent failures. It challenges the
    proposed remedy. Heartbeats and freshness checks are the textbook instrument that gray failure
    defeats. Huang et al. report that most cloud incidents are failures where the liveness signal stays
    green while the service is broken. Panorama found heartbeat-style detectors caught 1 of 15 gray
    failures in time. Distributed-systems theory says timeout detectors cannot be both complete and
    accurate. Freshness is necessary but not sufficient. What closes the gap is observing the output
    from the consumer side: end-to-end probes, validation gated before the ping, and observers that do
    not share the failure path.

  Specific risks: (a) C2A2 swaps "record exists" for "record timestamp < N hours" and declares the
    problem solved, while an agent that writes fresh but empty or malformed output passes. (b)
    Watchdog-of-watchdog chains share a scheduler or host, so one failure silences both. (c) Thresholds
    tuned for silence produce alert noise, or the reverse.

  Mitigations available: Gate every heartbeat on a content check, for example a non-empty diff, a
    schema check, or a count within the expected range. Add at least one consumer-side observation (does
    the downstream agent actually find new usable input?). Run a known-answer canary. Put the watchdog
    on a separate execution path. Log the time between failure and detection when audits find
    failures.

  STEELMAN:
    Item: ASSUMPTION-1778
    Strongest counterargument: Moving from existence to freshness moves the proxy up one level without
      changing its kind. Both checks ask the producer whether it did something, not whether the
      consumer got what it needed. The best-documented class of production failures, gray failure, is
      defined by exactly this gap. Heartbeats are its canonical victim, and the 2017 paper says it is
      behind most cloud incidents. A dead-man switch built on top of a heartbeat inherits the blind
      spot. Watchdog-of-watchdog adds layers but not independence. The remedy may give C2A2 a stronger
      feeling of coverage than the actual coverage it adds.
    What would need to be true for C2A2 to be safe: The freshness signal is emitted only after a
      content or validity check. At least one observer is on the consumer side. The watchdog does not
      share a scheduler, host, or credential with what it watches.
    How to test: Inject faults deliberately. Make an agent write fresh but empty or garbage output, and
      separately stall it while its heartbeat continues. Measure whether the proposed design detects
      each fault and how long it takes.

  Boundary conditions identified:
    - Heartbeats are adequate for fail-stop faults (crash, scheduler not firing), which may be the
      dominant failure mode in a small scheduled pipeline. Gray-failure prevalence data comes from
      cloud-scale systems.
    - The gray-failure work is from large distributed systems. The authors note that it also occurs at
      single-node scale, but they provide no prevalence data there.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see SYSTEMIC-RISK-FLAG_2026-10-13_remedy-is-another-proxy_1778-1780-1124-1125-1127.md
