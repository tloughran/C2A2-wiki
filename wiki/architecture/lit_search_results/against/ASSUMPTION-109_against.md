SEARCH-AGAINST-ASSUMPTION-109:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-109
  Original statement: "PRESUMPTION-125 4th-recurrence cowork-to-chat sync requires standalone DECISION canonization distinct from DECISION-027 scope"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-109
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD standalone-DECISION-vs-DECISION-027-scope distinction
      15b: Searched for counter-evidence on cluster-distinction without substrate-decomposition
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Vesely (1981) "Fault Tree Handbook" — common-cause failure analysis requires substrate-decomposition before treating clusters as independent; splitting without substrate decomposition inflates apparent reliability and corrupts mitigation design.
    2. Allspaw / Cook "How Complex Systems Fail" (2000) — naming-the-cluster substitutes for understanding-the-cluster; standalone-DECISION canonization based on cluster-naming alone is anti-pattern.
    3. Nygard (2018) — DECISION proliferation without substrate-discipline produces ADR sprawl; ADR sprawl is documented maintainability burden.
    4. PRESUMPTION-134 (this cycle) — explicit substrate-decomposition challenge to ASSUMPTION-109's basis for treating cowork-to-chat sync as substrate-independent of Chrome MCP cluster.
    5. PRESUMPTION-136 (this cycle) — week-carrying-capacity challenge: two HIGH-urgency canonizations same week is over-commitment by ADR / Kotter / Goldratt standards.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. Standalone DECISION canonization is canonical when substrate-decomposition supports independence, but the substrate-decomposition has not been done — and PRESUMPTION-134 explicitly raises this as the missing prerequisite. The cowork-to-chat-sync cluster shares Chrome MCP + claude.ai login state substrate with PRESUMPTION-121 cluster. Calendar-paced URGENT canonization compounds the concern (same anti-pattern as ASSUMPTION-108). Week-carrying-capacity (PRESUMPTION-136) is the operator-availability constraint not consulted.

  Specific risks: (a) Substrate-decomposition gap means standalone-DECISION may bake in cluster-naming that does not survive substrate analysis; (b) DECISION proliferation without substrate-discipline produces ADR sprawl; (c) two HIGH-urgency canonizations same week overloads operator; (d) "URGENT" framing is calendar-paced.

  Mitigations available: (a) Substrate-decomposition before standalone-DECISION canonization; (b) consider combined-DECISION if substrate is shared (reducing carrying-capacity demand from 2 to 1); (c) implementation-paced rather than calendar-paced commitment; (d) week-carrying-capacity consultation with Tom.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-109
    Strongest counterargument: Standalone DECISION canonization is appropriate only when the cluster has been substrate-decomposed and the independence claim is supported. PRESUMPTION-134 explicitly raises that the cowork-to-chat-sync cluster shares Chrome MCP + claude.ai login state substrate with PRESUMPTION-121 — making independence questionable. By Vesely common-cause-failure analysis, splitting two substrate-coupled failure modes inflates apparent reliability. By Nygard ADR discipline, the standalone-DECISION canonization without substrate-discipline produces ADR sprawl. By Kotter/Goldratt, two HIGH-urgency canonizations same week is over-commitment.
    What would need to be true for C2A2 to be safe: (a) Substrate-decomposition documents independence; (b) carrying-capacity consulted; (c) implementation-paced.
    How to test: Audit whether substrate-decomposition is performed; check whether DECISION-027 and standalone-DECISION end up referring to overlapping infrastructure components (revealing the substrate-shared pattern post-canonization).
