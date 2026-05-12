SEARCH-AGAINST-PRESUMPTION-135:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-135
  Original statement: "Morning chat-scrape 3rd consecutive day reaches three-recurrence canonization threshold per ASSUMPTION-098 but presumed absorbed under PRESUMPTION-121 cluster without explicit subsumption rule"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-135
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD cluster-absorption without subsumption rule
      15b: Searched for counter-evidence on cluster-absorption of recurrence-counts
    Current status: CHALLENGED

  Sources:
    1. Beyer (2016) SRE Ch. 14 — explicit subsumption rules are required to prevent recurrence-counter dilution; absorption without rule is documented anti-pattern.
    2. ITIL v4 Problem Management — cluster-membership-as-subsumption is permitted only when membership criteria are canonically defined; absent the rule, default is per-incident counting.
    3. Nygard (2018) — runbook entries grow by accretion when subsumption rules are absent; cluster identity drift is the canonical risk.
    4. PRESUMPTION-134 (this cycle) — substrate-decomposition concern; cluster-membership presumption depends on substrate being shared, which is itself unverified.
    5. C2A2-internal: ASSUMPTION-098 (MONITOR-101) is the governance protocol; consistency requires subsumption-rule specification.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. The literature uniformly requires explicit subsumption rules for cluster-membership absorption of recurrence-counts. The C2A2 case lacks the rule; default ITIL practice would count morning chat-scrape independently. Cluster-absorption-without-rule undermines ASSUMPTION-098 governance protocol consistency. PRESUMPTION-134 substrate-decomposition concern is the paired issue.

  Specific risks: (a) Governance protocol inconsistency: rule applied case-by-case; (b) recurrence-counter dilution; (c) cluster identity drift; (d) canonization threshold satisfaction obscured.

  Mitigations available: (a) Explicit subsumption rule in cluster definition; (b) substrate-decomposition (PRESUMPTION-134) before cluster-membership absorption; (c) parallel-track per-incident counter alongside cluster counter.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-135
    Strongest counterargument: Cluster-absorption without an explicit subsumption rule is documented anti-pattern across SRE (Beyer), ITIL Problem Management, and Nygard's release-engineering literature. The C2A2 case lacks the rule. Default ITIL practice would count morning chat-scrape as an independent recurrence — which would itself meet the three-recurrence canonization threshold for a distinct DECISION. Cluster-absorption is the discretionary move; without rule, the discretion is exercised case-by-case, which corrupts ASSUMPTION-098 governance protocol consistency.
    What would need to be true for C2A2 to be safe: (a) Explicit subsumption rule; (b) substrate-decomposition; (c) parallel-track counters.
    How to test: Audit whether subsumption rule exists in PRESUMPTION-121 cluster definition; check whether morning chat-scrape is counted separately or absorbed; whether the decision is rule-based or discretionary.
