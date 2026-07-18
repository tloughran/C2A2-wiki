SEARCH-AGAINST-ASSUMPTION-435:
  Date searched: 2026-07-10
  Original item: ASSUMPTION-435
  Original statement: "DB write-staleness beyond threshold reliably indicates the OpenStory runtime is down, and refusing to refresh on stale data (freeze) beats serving stale feeds."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-435
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. [Chandra & Toueg, 1996. "Unreliable Failure Detectors for Reliable Distributed Systems." JACM. — Foundational result: in an asynchronous system it is impossible to distinguish a crashed process from a merely slow one; any timeout/staleness-based detector is inherently unreliable and will make false suspicions. Staleness beyond threshold therefore cannot "reliably" indicate the runtime is down.]
    2. [Hayashibara et al., 2004. "The φ accrual failure detector." IEEE SRDS. — Fixed staleness thresholds force a tradeoff: short thresholds give fast detection but high false-positive rates; the field moved to accrual (probabilistic) detectors precisely because binary threshold checks misclassify slow/idle processes as dead.]
    3. [Nottingham, 2010. "RFC 5861: HTTP Cache-Control Extensions for Stale Content." IETF. — Standardizes stale-if-error: when the origin fails, serving a stale response is the sanctioned behavior rather than returning a hard error; the web-infrastructure consensus is that stale beats nothing for read-mostly content.]
    4. [AWS Well-Architected Framework. "REL05-BP01: Implement graceful degradation to transform applicable hard dependencies into soft dependencies." — Recommends components continue their core function on dependency failure by serving "slightly stale data, alternate data, or even no data" as a last resort; freezing output is the bottom of the preference order, not the top.]
    5. [Fastly Documentation. "Serving stale content." — Industry CDN practice: serve stale while revalidating and serve stale on error, because for most read paths hours-old data is more useful than an error; explicit caveat that staleness is dangerous only for domains like trading prices or payment rates.]

  Strength of challenge: Strong

  Summary: Both halves of the claim are contradicted by well-established literature. First, distributed-systems theory (Chandra & Toueg; accrual failure detectors) shows that a staleness threshold cannot reliably distinguish "runtime down" from "runtime idle," "runtime slow," or "clock/reporting path broken" — false suspicion is intrinsic to timeout-based detection. In C2A2's case a legitimately quiet day with no writes is observationally identical to an outage. Second, the graceful-degradation literature (RFC 5861 stale-if-error, AWS Well-Architected, CDN practice) holds that for read-mostly, non-safety-critical feeds, serving stale content with a staleness indicator dominates refusing to serve; freeze-on-stale is reserved for domains where acting on stale data causes harm (trading, payments, actuation). A philosophy-wiki feed is squarely in the "stale is fine, label it" category.

  Specific risks: False positives — an idle-but-healthy runtime or a broken heartbeat-write path triggers a freeze, and C2A2 withholds perfectly good data from its consumers; the freeze itself becomes the availability incident. Conversely, users may interpret a frozen feed as total system failure, eroding trust more than a labeled stale feed would.

  Mitigations available: Use a dedicated liveness heartbeat (runtime writes a timestamp even when there is no content activity) so staleness measures liveness, not workload; serve stale data with an explicit "last updated" banner instead of freezing (stale-while-revalidate pattern); use graduated thresholds (warn, then degrade, then freeze) rather than a binary cliff; distinguish "no new writes" from "heartbeat missing."

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Staleness conflates at least four states — down, slow, idle, and broken measurement path — and forty years of failure-detector theory says no threshold can separate them. Building a freeze behavior on an unreliable detector means the system will predictably deny service on false positives, and for a research wiki the cost asymmetry runs the other way: stale philosophy content harms nobody, while a frozen feed is a self-inflicted outage. The web's own standards body codified serve-stale-on-error as the correct default for exactly this class of content.
    What would need to be true for C2A2 to be safe: Staleness must be measured against a guaranteed-periodic heartbeat (not organic writes), the threshold must be far above the heartbeat period, and the cost of a consumer acting on stale feed data must genuinely exceed the cost of serving nothing — a condition that should be argued, not assumed.
    How to test: Run the runtime in a deliberately idle state (no content writes) past the threshold and observe whether the detector fires falsely; simulate a real outage and compare consumer impact of freeze vs stale-with-banner. This is the queued in-house empirical test.
