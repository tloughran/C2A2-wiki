SEARCH-AGAINST-PRESUMPTION-1121:
  Date searched: 2026-10-11
  Original item: PRESUMPTION-1121
  Original statement: [inferred] The pipeline presumes its flags have a reader. Outputs to Tom pile
    up (some recommendations repeated 25-35 times) while little reviewer action is visible. Question:
    should an unattended pipeline measure reviewer uptake (flags actioned / flags raised) and
    throttle or escalate when uptake drops?
  Under test: the implied remedy, measuring uptake and throttling or escalating on low uptake. I
    searched for uptake/acknowledgment metrics being gamed or misleading, and for throttling or
    suppression on low engagement hiding real signals.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1121
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-10): Inferred from repeated, unactioned recommendations (25-35 repeats) that the
        pipeline presumes it has a reader. Queued with the uptake-metric and throttle/escalate
        question.
      15b (2026-10-11): Searched for challenging literature. 3 searches: gaming of alert
        acknowledgment/override metrics; consequences of suppressing high-override CDS alerts;
        Goodhart's and Campbell's laws. 1 fetch: New Relic "Manage your alert quality" doc (full
        text).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One full-text fetch (vendor documentation); the rest are snippets or
    search summaries.
  Search scope: preliminary (3 searches, 1 fetch).

  Challenging evidence found: Partial
  Strength of challenge: Moderate on uptake as a throttle signal. Weak on measuring uptake at all.

  Sources:
    1. New Relic. "Manage your alert quality" (AQM tutorial documentation). [fetched, full text]
       Supports uptake measurement: "The amount of engagement an individual alert receives is a
       direct measurement of its value... less (or zero) engagement implies an alert may simply be
       noisy and should be modified or disabled." It also documents the gaming risk: fatigued
       responders "begin to simply close unresolved alert events to stay within response time
       targets", and the doc warns against manual closes and "mass acknowledgement exercises".
       Bearing: low engagement is read as a sign of low alert value, which is the opposite inference
       to "the reader is overloaded, so escalate". The same metric can support either action. Once
       uptake is measured, it can be satisfied by closing flags without acting on them.
    2. Rootly, "Alert management metrics: 18 KPIs"; Ray Wilson et al. 2026 systematic review of
       alert fatigue (MetroHealth PDF). [snippet] "An acknowledgment alone should not classify an
       alert as actionable." A disposition taxonomy is needed (action taken / duplicate / false
       positive / no action). The 2026 review finds alert-fatigue measures (override rate,
       acceptance rate) "not clearly or consistently defined". Bearing: "flags actioned / flags
       raised" is under-specified. A flag can rightly go unactioned, so a raw uptake ratio
       conflates noise with neglect.
    3. JMIR Med Inform 2020;8(7):e15653, systematic review of CDS alert overrides (23 articles).
       [snippet] Override rates ran from 46.2% to 96.2%. The appropriateness of overrides varied
       widely (drug-drug 0-95%). Inappropriate overrides were associated with more potential adverse
       drug events. Bearing: low uptake does not mean low value. Some ignored alerts were the ones
       that mattered, so throttling a channel because uptake is low can remove the rare true signal.
       The search found no controlled study measuring missed critical events after suppression
       rules; this is a literature gap.
    4. Goodhart's law / Campbell's law (Campbell 1976; Strathern's phrasing; Manheim & Garrabrant
       taxonomy). [snippet, secondary] The more a quantitative indicator drives decisions, the more
       it is subject to corruption pressure and the more it distorts the process it monitors.
       Bearing: if uptake drives throttling or escalation, both the pipeline (agents that phrase
       flags to get them actioned) and the reviewer (batch-closing to stop escalations) acquire
       incentives to move the ratio rather than the substance.

  Summary: The literature supports the core diagnosis. Unread, repeated flags are the classic
    alert-fatigue pattern, and measuring engagement is standard alert-quality practice. It challenges
    the proposed control loop. An uptake ratio is ambiguous: low uptake can mean noisy flags or an
    overloaded reader. It is easy to game: close without acting, or batch-acknowledge. When used to
    throttle, it can suppress the low-frequency, high-value flags that clinical override data show
    are among the most often ignored. Escalation on low uptake can also backfire. In a one-reviewer
    system, escalation adds volume to the channel that is already saturated.

  Specific risks: (a) Throttling hides a real systemic flag that Tom never read. (b) Escalation
    increases the volume of the output that is already being ignored. (c) Tom or the agents learn to
    move the metric. (d) A single-reader system has no alternative escalation path, so "escalate"
    has nowhere to go.

  Mitigations available: Record disposition (actioned / declined / deferred / duplicate), not just
    actioned. Deduplicate repeated recommendations into a single item with a counter, and do not
    re-emit it. Exempt a small severity tier from throttling. Throttle by quality (dedup, merge), not
    by engagement alone. Audit a sample of dropped flags periodically.

  STEELMAN:
    Item: PRESUMPTION-1121
    Strongest counterargument: Uptake is the most gameable and most ambiguous metric in the alerting
      toolkit. Vendor guidance that recommends it also documents responders closing alerts to hit
      targets. Clinical evidence shows that the most-ignored alerts include genuinely dangerous ones.
      A control loop that throttles on low uptake treats reviewer neglect as evidence of low signal
      value. It will therefore silence exactly the flags an absent reviewer most needed. Escalation
      has nowhere to go when there is one reviewer. By Goodhart/Campbell, the loop will soon measure
      how flags are handled, not whether they are heeded.
    What would need to be true for C2A2 to be safe: Uptake is recorded by disposition, not as a
      binary. It informs deduplication and summarisation, not suppression. A protected severity tier
      is never throttled. Escalation means a change of format (a digest) or a secondary channel, not
      more volume.
    How to test: Replay the last 30 days of flags under the proposed throttle rule. Check whether any
      flag later judged important (e.g. systemic-risk flags) would have been suppressed.

  Boundary conditions identified:
    - The alert-fatigue literature mostly involves high-frequency operational alerts with many
      responders. C2A2 has one reviewer and low-frequency, deliberative flags. The gaming and
      ambiguity mechanisms transfer, but the volume numbers do not.
    - No source found measures the harm of throttling directly. The suppression risk is inferred
      from override-appropriateness data.

  Recommendation: PARTIALLY-CHALLENGED

SYSTEMIC-RISK-FLAG:
  Date: 2026-10-11
  Affected items: ASSUMPTION-1766, ASSUMPTION-1769, PRESUMPTION-1120, PRESUMPTION-1121
  Common vulnerability: Every proposed fix sends verification through a proxy that the pipeline
    defines and scores itself, with a single human reviewer as the only external check:
    consolidated premises (compliance judged by the agents themselves), planted canaries
    (calibration judged on the system's own plants), a house threshold with deferral to the reviewer
    (verification handed to the reviewer), and an uptake ratio (attention judged by a gameable
    count). In each case the literature shows the proxy can be satisfied while the target is not:
    broad principles leave compliance ambiguous (Black), gold sets get detected and fail to
    transfer (Checco et al.; Ovadia et al.), reviewers rubber-stamp (Skitka; Cologne 2023), and
    engagement metrics are gamed (New Relic; Goodhart/Campbell). Each relies on the same scarce
    resource, Tom's attention, which PRESUMPTION-1121 suggests is already saturated.
  Literature basis: Black 2008; Checco, Bates & Demartini 2019; Ovadia et al. 2019; Skitka et al.
    1999; New Relic AQM doc; Campbell 1976 / Goodhart.
  Risk level: High
  Recommendation: The system should consider at least one check that is independent of both the
    pipeline's own proxies and Tom's queue, for example a periodic blind audit sample adjudicated
    outside the normal reviewer flow. It should also treat "the reviewer will check" as a capacity
    claim to be measured, not assumed. This continues the earlier High flag (PRESUMPTION-1117
    family: binary corrections plus added meta-process).
