SEARCH-AGAINST-PRESUMPTION-085:
  Date searched: 2026-04-28
  Original item: PRESUMPTION-085
  Original statement: "PREMISE-012 N-day threshold not examined; surface-and-proceed has no upper bound"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-085
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Sources:
    1. Shewhart (1931); Wheeler (1995) — staleness-floor design is core to statistical process control; absence of explicit threshold is a calibration gap.
    2. Jennex (2007) "Knowledge Management in Modern Organizations" — staleness thresholds are load-bearing; the absence of one is a documented failure mode.
    3. Reason (1990) — principle-scope-extension errors when a premise ratified at small-N is applied at large-N is a canonical accident-causation pattern.
    4. C2A2-internal: PREMISE-012 was ratified at 4-day staleness; PRESUMPTION-077 / MONITOR-069 already flagged the scaling-floor concern.

  Strength of challenge: Strong

  Summary: The literature is consistent: explicit thresholds are necessary for surface-and-proceed patterns. The absence of an upper bound — the precise content of PRESUMPTION-085 — is the documented failure mode. C2A2's own prior cycle already flagged this concern as PRESUMPTION-077 / MONITOR-069.

  Specific risks: (a) Silent breakdown at N>4 days; (b) PREMISE-012 is applied at scales it was never validated for; (c) accumulating staleness goes undetected.

  Mitigations available: (a) Specify an explicit N-day upper bound on PREMISE-012; (b) tie the bound to PRESUMPTION-077 / MONITOR-069 monitor cadence; (c) trigger explicit re-evaluation at N+1.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE

  STEELMAN:
    Item: PRESUMPTION-085
    Strongest counterargument: PREMISE-012 was ratified at 4-day staleness with no upper bound; this is the literal scope-extension failure mode. The principle is being applied at staleness scales it was never validated for, and the absence of a threshold means the failure (if it happens) will be silent.
    What would need to be true for C2A2 to be safe: Specify an explicit upper bound on PREMISE-012 (e.g., 7-day reapply-with-caveat, 14-day re-derive-from-scratch).
    How to test: Identify the longest-staleness gap in the C2A2 record so far; verify whether PREMISE-012 was applied at that scale; if yes, sample for silent breakdown.
