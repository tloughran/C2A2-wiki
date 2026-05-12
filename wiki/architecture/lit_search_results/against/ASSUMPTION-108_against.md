SEARCH-AGAINST-ASSUMPTION-108:
  Date searched: 2026-05-11
  Original item: ASSUMPTION-108
  Original statement: "ASSUMPTION-098 three-recurrence governance threshold satisfied URGENT-this-week for DECISION-027 scope extension to external-tool-review layer (PRESUMPTION-121 N=5/30 days)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-108
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-10 EOD URGENT-this-week canonization trigger
      15b: Searched for counter-evidence on three-recurrence thresholds and URGENT-calendar-paced canonization
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Bryar & Carr (2021) "Working Backwards" Amazon ADR practice — calendar-paced URGENT canonization is documented anti-pattern; document quality is the load-bearing variable, not week boundary.
    2. Nygard (2011) blog "ADR" — explicit warning against calendar-paced ADR commitment; ADR maturation requires deliberation, not deadline.
    3. Pearl (2000) "Causality" — recurrence-counter satisfaction is not a sufficient causal claim; substrate-decomposition must precede canonization.
    4. PRESUMPTION-134 (this cycle, paired) — substrate-decomposition challenge: PRESUMPTION-121 and PRESUMPTION-125 may share substrate, undermining the recurrence-counter independence assumption.
    5. PRESUMPTION-106 (prior cycle, unresolved) — canonization criterion not self-evident; canonizing without resolving the upstream criterion is structural circularity.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. The recurrence-threshold pattern is canonical but the URGENT-this-week framing is calendar-paced rather than implementation-paced — a documented ADR anti-pattern. The substrate-decomposition challenge (PRESUMPTION-134) is the more serious gap: if PRESUMPTION-121 and PRESUMPTION-125 share substrate, the recurrence count is inflated by treating common-cause failures as independent. Additionally, the upstream ASSUMPTION-098 (governance threshold itself) is MONITOR-101, not INCORPORATE — canonizing under an un-validated governance rule is circular.

  Specific risks: (a) Calendar-paced canonization corrupts deliberation quality; (b) substrate-decomposition gap means recurrence-counter may be inflated by common-cause failure; (c) two HIGH-urgency canonizations same week (PRESUMPTION-136) overloads operator (Tom) capacity; (d) circular dependency on un-validated ASSUMPTION-098 governance rule.

  Mitigations available: (a) Defer URGENT-this-week framing in favor of implementation-paced commitment; (b) substrate-decomposition before recurrence-counter satisfaction claim; (c) ASSUMPTION-098 INCORPORATE before relying on threshold; (d) week-carrying-capacity consultation with Tom before parallel HIGH-urgency canonizations.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-108
    Strongest counterargument: The three-recurrence pattern is canonical but does not by itself authorize URGENT-this-week canonization. The Bryar-Carr Amazon practice and Nygard ADR literature both explicitly warn against calendar-paced commitment — quality of deliberation is the load-bearing variable. The substrate-decomposition challenge (PRESUMPTION-134) means the recurrence-counter may be inflated: if PRESUMPTION-121 and PRESUMPTION-125 share Chrome MCP + claude.ai login state substrate, the apparent independent recurrence is a common-cause-failure artifact rather than a substrate-validated trigger. The upstream ASSUMPTION-098 threshold itself remains MONITOR — relying on it before it is INCORPORATEd is circular.
    What would need to be true for C2A2 to be safe: (a) Substrate-decomposition completed; (b) ASSUMPTION-098 INCORPORATEd; (c) week-carrying-capacity consultation with Tom; (d) calendar-pace replaced with implementation-pace.
    How to test: Check whether substrate-decomposition is documented; whether ASSUMPTION-098 status changes from MONITOR to INCORPORATE; whether Tom is consulted about week-carrying-capacity.
