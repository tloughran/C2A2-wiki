SEARCH-AGAINST-ASSUMPTION-074:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-074
  Original statement: "No-new-evidence carry-forward as PREMISE-006 extension to refresh case"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-074
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Knowledge-management staleness literature (Maier 2007; Jennex 2007) — carry-forward without depth specification produces silent staleness; the documented failure mode is "the system reports no change because nobody looked, not because nothing changed."
    2. Cochrane "Living Systematic Reviews" (Elliott et al. 2017) — depth-matched search is the explicit precondition for valid null-evidence reporting; un-matched depth is the documented anti-pattern.
    3. Trist (1981) "The evolution of socio-technical systems" — refresh-cycle decay studies in operational pipelines show that null-evidence reports lose reliability as cycle count grows without re-calibration.
    4. SRE alert-fatigue literature (Beyer et al. 2016) — repeated null reports lower attention to the next non-null; the carry-forward pattern itself can mask the eventual change.

  Strength of challenge: Moderate

  Summary: Carry-forward null-evidence reporting is challenged when search depth is not documented or is asymmetric to the original cycle. The literature treats this as a known failure mode (silent staleness) and recommends explicit depth-pairing. PRESUMPTION-082 surfaces the same challenge from the unstated side.

  Specific risks: (a) Silent staleness: items remain MONITOR indefinitely because the refresh cycle never matches original-cycle depth; (b) alert-fatigue: 39 carry-forwards in one day (2026-04-27) lowers attention to the next change.

  Mitigations available: (a) Document refresh-cycle search depth explicitly; (b) periodically run a depth-matched sample to verify carry-forward reliability; (c) flag items where carry-forward exceeds N cycles for explicit re-evaluation.

  Recommendation: PARTIALLY-CHALLENGED (Moderate — the conditional version is defensible; the un-paired version is challenged)

  STEELMAN:
    Item: ASSUMPTION-074
    Strongest counterargument: The carry-forward pattern is sound only when search depth is documented and matched to the original cycle. The C2A2 refresh cycles do not currently document depth, so the "no new evidence" claim cannot be distinguished from "we did not look at the same depth as the original cycle." Without that distinction, the pattern silently drifts toward staleness.
    What would need to be true for C2A2 to be safe: (a) refresh-cycle search depth is documented; (b) periodic depth-matched audits verify reliability; (c) carry-forward beyond N cycles triggers explicit re-evaluation.
    How to test: Sample 5 carry-forwarded items from the 2026-04-27 batch; run a full-depth search; check whether any new evidence is found that the carry-forward missed. >0 hits would falsify the assumption.
