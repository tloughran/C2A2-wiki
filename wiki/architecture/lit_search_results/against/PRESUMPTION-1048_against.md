SEARCH-AGAINST-PRESUMPTION-1048:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1048
  Original statement: A monitoring agent sampling at a slower rate than its source publishes has a structurally invisible coverage window whose size is determined by the two cadences, and whose failure mode is a null report indistinguishable from a quiet period.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1048
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (queue entry p1048: monitoring-agent cadence vs source publication cadence; related ASSUMPTION-1540, OPEN-243)
      15b: Searched for challenging literature; found conceptual/engineering counter-arguments but no direct empirical refutation; strength: Moderate (conceptual), thin empirical base
    Current status: PARTIALLY-CHALLENGED

  Search scope: PRELIMINARY — broader search recommended. Several primary sources (PMC full texts) were not retrievable (reCAPTCHA); claims below are limited to what was actually fetched.

  Challenging evidence found: Partial

  Sources:
    1. Yan Cui, 2025 (15 May). "Understanding push vs poll in event-driven architectures." theburningmonk.com (https://theburningmonk.com/2025/05/understanding-push-vs-poll-in-event-driven-architectures/). — Practitioner (non-peer-reviewed) argument that poll-based consumers over durable streams (Kinesis/Kafka) checkpoint progress and retry independently, so polling frequency trades latency/throughput, not completeness. Supports the objection that for persistent sources a slow sampler loses latency, not events.
    2. Authors not retrieved, c. 1999. "Detection of Aliasing in Persistent Signals." arXiv:chao-dyn/9905021 (https://arxiv.org/abs/chao-dyn/9905021). — Shows aliasing in sampled waveforms can be detected (via a stationarity concept for individual waveforms) under fairly unrestrictive constraints. Challenges "structurally invisible" even within the signal-theory home domain; the invisibility is conditional, not absolute. (Applies to signals, not directly to indexed corpora; analogy-transfer caveat cuts both ways.)
    3. Zhu D, Luo X, Chen Y (Lanzhou University), 2023. "How often should 'living' systematic reviews be updated? A cross-sectional study." Cochrane Colloquium 2023 abstract (https://abstracts.cochrane.org/2023-london/how-often-should-living-systematic-reviews-be-updated-cross-sectional-study). — Of 164 LSRs, median stated update interval 3 months (range 1 week to 18-24 months). Abstract does NOT report missed-evidence outcomes; cited only as evidence that deliberately slow cadences are accepted practice in a persistent-index domain, not as evidence of loss. Weak.
    4. Butler AR, Hartmann-Boyce J, Livingstone-Banks J, Turner T, Lindson N, 2024. "Optimizing process and methods for a living systematic review: 30 search updates and three review updates later." (Oxford PHC record: https://www.phc.ox.ac.uk/publications/publication_modal/1578413; PMC12018299 not retrievable). — Monthly automated searches against bibliographic databases are described as sufficient; cadence is framed as a workload/timeliness choice. Relevance is indirect; summary taken from the abstract-level page only.

  Not found / searched without result: no source located that directly argues the Nyquist/aliasing analogy is a category error for discrete indexed corpora; no source located that quantifies coverage loss for slow pollers of non-expiring archives. These are literature gaps for this direction, not confirmed absences. Unretrieved leads: LOCATE (PMC8056603) and MEDLINE indexing-lag material (e.g., Decullier et al., BMC Res Notes 2014;7:395) — not read, not relied upon.

  Strength of challenge: Moderate (conceptual argument plus engineering practice; Weak on direct empirical evidence)

  Summary: The presumption bundles three claims. (a) Coverage window set by two cadences: valid for expiring/rolling sources (windowed feeds, retention-limited logs) but, by the item's own framing, not for persistent, indexed, permanently retrievable corpora, where a slow sampler with a high-water mark/cursor loses latency only; the window then closes at next poll. (b) "Structurally invisible": signal literature indicates aliasing can be detectable under conditions, and in engineering practice cursors, sequence numbers, and "since last checkpoint" queries make the gap observable. (c) Null report indistinguishable from quiet: this part is largely NOT challenged; it is true when the agent reports only counts of new items without recording what range was queried. The challenge is therefore to scope (source persistence, existence of a cursor) and to "structurally", not to the existence of the failure mode.

  Specific risks: If the presumption is over-general, C2A2 may spend effort harmonizing fifteen cadences that do not matter for non-expiring sources, or may add event-driven machinery with its own failure modes (missed webhooks, ordering). Conversely, if C2A2 accepts the persistence objection wholesale, it may overlook sources that are rolling, rate-limited, index-lagged, or revised/deleted, where slow sampling does lose items.

  Mitigations available: Classify each tradition's source as persistent vs expiring; have every monitor report the query window (from/to, cursor) alongside the result so a null report is distinguishable from a quiet period; poll the index by entry/ingest date rather than by publication date; run periodic full-index reconciliation sweeps.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1048
  Strongest counterargument: Aliasing is a property of sampling a continuous signal whose information is transient: samples discarded between ticks are gone. C2A2's sources are discrete, indexed, append-mostly corpora, where each item persists with a timestamp. Sampling such a store is not sampling a signal but reading a log: a query "everything since cursor T" returns the entire inter-poll backlog, so nothing is lost regardless of the cadence ratio; the only cost is staleness, which is a latency parameter, not a coverage window. The "invisible window" exists only if the monitor queries by a fixed recent horizon or discards its cursor. That is an implementation defect in the monitor, not a structural property of cadence mismatch, and a null report is distinguishable from quiet wherever the report carries the queried range.
  What would need to be true for C2A2 to be safe: All monitored sources are persistent and queryable by ingest/entry time; the monitor stores and reports a high-water mark; index lag is bounded and shorter than the poll interval or handled by overlap windows; no source revises or deletes items silently.
  How to test: For each of the fifteen traditions, replay a retrospective comparison: run the slow monitor and an exhaustive index query over the same period and count items missed; inject items with backdated publication dates and check if the monitor catches them; check whether the null-report format contains the queried range.

SYSTEMIC-RISK-FLAG: none raised from this item alone (single item; fifteen-cadence exposure already noted in the item's own risk statement).

## RETURN BLOCK
RETURN-TO-14b:
  Original item: PRESUMPTION-1048
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate (conceptual); Weak empirically; preliminary search
  Key source: Cui, Y. 2025. "Understanding push vs poll in event-driven architectures." theburningmonk.com (supporting arXiv:chao-dyn/9905021, "Detection of Aliasing in Persistent Signals")
  Specific risk: If the presumption is over-general, effort is wasted harmonizing cadences for persistent sources; if wholly dismissed, rolling/index-lagged sources lose items silently.
  Summary: Window-from-cadences holds for expiring sources but for persistent indexed corpora with a cursor a slow poller loses latency, not coverage; the null-report-vs-quiet failure mode itself is not challenged.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1048_against.md
  Queue summary (one line): PRESUMPTION-1048 [SEARCHED-15b: 2026-10-05] PARTIALLY-CHALLENGED, Moderate/conceptual, preliminary; persistence + cursor scoping objection, null-report mode stands.
SYSTEMIC-RISK: not flagged
