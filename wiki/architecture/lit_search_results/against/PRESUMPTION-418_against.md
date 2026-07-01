SEARCH-AGAINST-PRESUMPTION-418:
  Date searched: 2026-06-29
  Original item: PRESUMPTION-418
  Original statement: "[inferred] That orphan-detection should have a single canonical owner - bootstrap-beside-weekly framed as wasteful 'double-counting' rather than useful redundant cross-check (against the project's own monitor-of-monitor principle)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-418
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: redundant orphan-detection treated as wasteful rather than as defense-in-depth
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Defense-in-depth / redundancy literature. - Independent, overlapping checks are explicitly designed to catch what any single layer misses; stacking independent monitors multiplies detection and reduces undetected-failure probability - the opposite of "wasteful double-counting."
    2. Single-ownership scope limit. - The efficiency case for deduplication/single-ownership is about FINDING tracking and remediation, not about detection coverage; collapsing two independent DETECTORS removes an independent cross-check, which dedup literature does not endorse.
    3. C2A2's own monitor-of-monitor principle (PREMISE-086 family). - The project has already validated dead-man's-switch / monitor-of-monitor / "absence is the signal" practice; framing redundant orphan-detection as waste directly contradicts an existing validated premise, an internal inconsistency.

  Strength of challenge: Strong

  Summary: The presumption mislabels redundant orphan-detection as wasteful double-counting, but defense-in-depth literature treats independent overlapping detectors as a feature, not waste - they catch failures a single owner would miss. The deduplication/single-ownership case the FOR direction cites applies to tracking findings, not to detection coverage; conflating the two is the error. Most importantly, this presumption contradicts C2A2's OWN validated monitor-of-monitor / dead-man's-switch principle (PREMISE-086), making it an internal inconsistency, not just an external risk.

  Specific risks: Collapsing to a single orphan-detector creates a single point of failure for liveness; a silent stall in the sole owner goes undetected - the exact failure the project's dead-man's-switch family was built to prevent.

  Mitigations available: Keep bootstrap + weekly as independent cross-checks; deduplicate the FINDINGS (one ticket per orphan) while preserving two independent DETECTORS; alarm on disagreement between them.

  STEELMAN:
    Item: PRESUMPTION-418
    Strongest counterargument: There is a genuine efficiency cost to running two orphan detectors and reconciling their outputs, and uncoordinated redundancy can produce duplicate tickets and confusion - so a single canonical owner with clean deduplication is simpler IF detection reliability is not the concern.
    What would need to be true for C2A2 to be safe: Orphan detection is not liveness-critical AND a single owner cannot silently stall - neither of which holds, given the project's own OPEN-086 liveness concerns.
    How to test: Check whether the two detectors ever disagree or catch different orphans; if they do, redundancy is earning its keep.

  Search scope: Defense-in-depth; dedup scope; internal consistency vs PREMISE-086. Adequate.

  Recommendation: CHALLENGED
