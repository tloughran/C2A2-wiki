SEARCH-AGAINST-PRESUMPTION-382:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-382
  Original statement: "That a one-night autonomous census can authoritatively reframe a standing human-tracked alarm - write-caution applied, interpretive-caution not"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-382
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: write-side caution applied, interpretive caution not
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Interpretive vs operational autonomy (HITL governance: Galileo; Famulor human-on-the-loop). - Governance frameworks separate act-caution from INTERPRET-caution; an agent may be cleared to measure yet not to authoritatively reinterpret a human-owned signal.
    2. Silent re-interpretation between attended sessions. - An autonomous reframe that changes a standing alarm's meaning without review is an unreviewed status change - the same class as silent degradation (MONITOR-296).
    3. Automation bias. - Downstream readers may treat the autonomous reframe as settled, compounding the unreviewed interpretation.

  Strength of challenge: Moderate-Strong

  Summary: Moderate-strong challenge. The audit correctly withheld WRITE action (no bulk mutation, ASSUMPTION-342) but then exercised INTERPRETIVE authority - reframing a standing, human-tracked orphan alarm as an artifact. HITL governance treats these as distinct permissions: clearance to measure is not clearance to authoritatively reinterpret a human-owned signal. An unreviewed reframe that propagates downstream is a silent status change, and automation bias means later readers may treat it as settled fact.

  Specific risks: A human-tracked alarm is effectively closed by an unattended run's interpretation; the human loses a signal they were tracking, without ever reviewing the reframe.

  Mitigations available: Let autonomous runs PROPOSE reframes flagged as provisional pending Tom's review; do not change a human-tracked alarm's status autonomously; log interpretive moves distinctly from measurements.

  STEELMAN:
    Strongest counterargument: If the reframe is recorded as a provisional proposal (not an authoritative status change) and surfaced for review, autonomous interpretation is fine - the issue is authority, not interpretation.
    What would need to be true for C2A2 to be safe: The reframe must be marked provisional and routed to human review before it alters alarm status.
    How to test: Check whether the orphan alarm's tracked status was changed without an attended review; if so, the interpretive-caution gap is real.

  Search scope: interpretive vs operational autonomy; silent re-interpretation; automation bias. Comprehensive.

  Recommendation: CHALLENGED
