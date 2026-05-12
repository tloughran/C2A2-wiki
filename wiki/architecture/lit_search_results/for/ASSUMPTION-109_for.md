SEARCH-FOR-ASSUMPTION-109:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-109
  Original statement: "PRESUMPTION-125 4th-recurrence cowork-to-chat sync requires standalone DECISION canonization distinct from DECISION-027 scope"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-109
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD 4th-recurrence cowork-to-chat-sync cluster requiring distinct canonization
      15a: Searched for incident-management severity-ladder design and recurrence-counter-driven escalation patterns
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. ITIL v4 (2019) Problem Management — distinct problem records for distinct root causes is canonical; clustering by symptom rather than by root cause is documented anti-pattern.
    2. Nygard (2018) "Release It!" — failure modes with distinct substrates warrant distinct mitigation patterns even when symptoms cluster; "shared-mode failure" is a separate category from "shared-substrate failure".
    3. Allspaw (2016) "How Complex Systems Fail" (Cook) — recurrence with the same observable surface signature can have distinct underlying contributors; lumping vs. splitting is a canonical decision.
    4. C2A2-internal: PRESUMPTION-125 (REVISE 2026-05-10) — flat-severity-ladder is the documented anti-pattern; severity-ladder + recurrence-counter is the literature-endorsed remediation.
    5. ADR literature (Tyree-Akerman 2005) — standalone DECISION records preserve traceability for distinct architectural concerns even when adjacent.

  Strength of support: Moderate

  Summary: Standalone DECISION records for distinct root causes are canonical in ITIL, SRE, and ADR literature. The cowork-to-chat-sync cluster has its own substrate (chat persistence + cross-session continuity) distinct from external-tool-review (DECISION-027's scope: external-LLM uptake adjudication). The "splitting" approach is supported by problem-management literature when substrates differ. The "URGENT" framing is again calendar-paced rather than implementation-paced.

  Caveats: (a) PRESUMPTION-134 (this cycle) is the paired explicit challenge: PRESUMPTION-121 and PRESUMPTION-125 may share substrate (Chrome MCP + claude.ai login state) — substrate-decomposition before splitting is the literature-endorsed sequence; (b) Standalone DECISION canonization without implementation commitment is documentation-as-fix (PRESUMPTION-122 anti-pattern); (c) Calendar-paced URGENT canonization is not endorsed by ADR literature; (d) Two HIGH-urgency canonizations same week (PRESUMPTION-136 this cycle) raises week-carrying-capacity concern.

  Recommendation: PARTIALLY-SUPPORTED (Moderate) — splitting on substrate is canonical; the substrate-decomposition (PRESUMPTION-134) and week-capacity (PRESUMPTION-136) prerequisites must be resolved before standalone canonization
