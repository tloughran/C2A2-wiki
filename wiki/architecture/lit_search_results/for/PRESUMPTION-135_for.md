SEARCH-FOR-PRESUMPTION-135:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-135
  Original statement: "Morning chat-scrape 3rd consecutive day reaches three-recurrence canonization threshold per ASSUMPTION-098 but presumed absorbed under PRESUMPTION-121 cluster without explicit subsumption rule"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-135
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 EOD cluster-absorption-without-subsumption-rule observation
      15a: Searched for governance-subsumption rules for cluster-membership in problem-management
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. ITIL v4 Problem Management — cluster-membership-as-subsumption is permitted when the cluster is canonically defined; otherwise per-incident recurrence counts independently.
    2. Beyer (2016) SRE Ch. 14 — explicit subsumption rules are required to prevent recurrence-counter dilution; absorption without rule is documented anti-pattern.
    3. Nygard (2018) "Release It!" — runbook entries grow by accretion when subsumption rules are absent; cluster identity drift is the canonical risk.
    4. C2A2-internal: PRESUMPTION-121 is the cluster identifier; ASSUMPTION-098 is the governance threshold (MONITOR-101); subsumption rule is not specified.
    5. PRESUMPTION-134 (this cycle) is the related substrate-decomposition concern — both surface the same cluster-naming-without-substrate-spec gap.

  Strength of support: Moderate

  Summary: Cluster-membership as a subsumption rule is supported by ITIL when the cluster is canonically defined with explicit membership criteria. The C2A2 case lacks an explicit subsumption rule — PRESUMPTION-121 was named cluster but not specified as a recurrence-counter aggregation rule. The literature endorses both options (subsume or count separately) provided the rule is explicit; the gap is the absent rule. Partial support for the practice contingent on the rule being made explicit.

  Caveats: (a) Absent subsumption rule, default ITIL practice is per-incident counting (would mean morning chat-scrape recurrence triggers separate canonization); (b) PRESUMPTION-134 raises the substrate-decomposition concern; (c) Governance-protocol consistency (ASSUMPTION-098) is undermined when subsumption rules are silently elective.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — subsumption is legitimate practice when rule is explicit; the C2A2 case lacks the rule and therefore falls back on per-incident counting per default ITIL practice
