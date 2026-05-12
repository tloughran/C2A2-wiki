SEARCH-AGAINST-PRESUMPTION-041:
  Date searched: 2026-04-17
  Original item: PRESUMPTION-041
  Original statement: "Afternoon-session architectural commitments do not require same-day DECISION-NNN entries (the 'implicit decision' workflow pattern is adequate)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-041
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — architectural commitments made without same-day DECISION records
      15b: Searched for challenging literature
    Current status: STRONGLY CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Nygard (2011) "Documenting Architecture Decisions": ADRs must be written synchronously with the decision; retroactive reconstruction loses rationale and fidelity.
    2. Kruchten et al. (2019) survey on ADR practices: implicit / undocumented decisions show high decay; reconstruction costs rise with delay; often impossible after team turnover or even context shift.
    3. Tyree & Akerman (2005) "Architectural Decisions: Demystifying Architecture": explicit, synchronous capture is the minimum discipline; implicit decisions accumulate into "architectural debt."
    4. C2A2's own PROVENANCE protocol: every inter-agent claim requires a chain-of-custody; architectural commitments are exactly the class that requires provenance.
    5. Rationale-capture decay literature (Burge & Brown 2000): intent and rationale for design decisions decay rapidly — days, not weeks — without explicit capture.

  Strength of challenge: Strong

  Summary: The literature is essentially unanimous. Architecture decisions require synchronous capture; implicit decisions are the specific anti-pattern ADRs were invented to address. More importantly, this presumption directly conflicts with C2A2's own PROVENANCE protocol, which requires chain-of-custody for all architectural claims. An implicit-decision workflow for architectural commitments is both externally-unsupported and internally-inconsistent with the system's stated values.

  Specific risks: Architectural commitments accumulate without rationale; future reversal is high-cost because the "why" is lost; provenance chain breaks at exactly the decision-commitment step that matters; other pipeline components (15d monitor, 16 deferred action) can't reason about decisions that weren't recorded.

  Mitigations available:
    - Standing rule: any afternoon-session architectural commitment creates a same-day DECISION-NNN entry
    - Lightweight template (short-form ADR) reduces friction
    - Automated reminder in afternoon-session close

  Recommendation: STRONGLY CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-041
    Strongest counterargument: Implicit decision-making is the named anti-pattern ADR practice was invented to address. Worse, this presumption directly contradicts C2A2's own PROVENANCE protocol, which requires chain-of-custody for architectural claims. The system cannot simultaneously mandate provenance for inter-agent claims and accept provenance-free commitments at the architectural level — this is internal inconsistency, not just an external weakness.
    What would need to be true for C2A2 to be safe: Same-day DECISION-NNN entries for all architectural commitments; explicit short-form ADR template available to reduce friction.
    How to test: Audit of today's afternoon-session architectural commitments — are they captured in decisions.md? If not, the presumption is actively violating the PROVENANCE protocol.
