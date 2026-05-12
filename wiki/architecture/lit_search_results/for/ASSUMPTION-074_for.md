SEARCH-FOR-ASSUMPTION-074:
  Date searched: 2026-04-28
  Original item: ASSUMPTION-074
  Original statement: "No-new-evidence carry-forward (refresh-cycle MONITOR re-disposition with 'no new literature this cycle') is a PREMISE-006-extension to the refresh case"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-074
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — 39 refresh items dispositioned with "no new evidence" carry-forward
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (with conditions)

  Sources:
    1. C2A2-internal: PREMISE-006 (flag-don't-fabricate) — established as the master principle for surfacing-rather-than-confabulating in master-wiki narratives. The carry-forward pattern is structurally parallel: "no evidence found" reported honestly rather than re-dispositioning silently.
    2. Cochrane Collaboration "Living Systematic Reviews" methodology (Elliott et al. 2017) — endorses "no change since last update" as a valid review outcome when the searched database has not added new sources, *with the explicit condition* that search depth is documented.
    3. Brookes (1980) "The foundations of information science" — refresh-cycle null reporting is treated as informational; the absence of new evidence is a signal, not a non-signal, for ongoing surveillance systems.
    4. SRE/operational-monitoring (Beyer et al. 2016 "Site Reliability Engineering") — heartbeat / no-change events are first-class signals that the monitoring system itself is functioning.
    5. ISO/IEC 25024 Data Quality Measurement — endorses the documentation of null-evidence cycles as part of the audit trail; carry-forward without documentation is the failure mode, carry-forward with documentation is the supported pattern.

  Strength of support: Moderate

  Summary: Carry-forward with explicit "no new evidence found" reporting is well-established in living systematic reviews, SRE monitoring, and ISO data-quality standards. PREMISE-006 already encodes the parallel principle (flag-don't-fabricate); extending it to the refresh case is a structurally consistent move. Support is moderate because the literature uniformly conditions the pattern on documented search depth — a condition that ASSUMPTION-074's framing does not yet make explicit.

  Caveats: (a) Carry-forward is supported when search depth is documented and reproducible; ASSUMPTION-074 does not specify depth. (b) PRESUMPTION-082 surfaces the same concern from the disconfirmatory side. The two should be reconciled.

  Recommendation: PARTIALLY-SUPPORTED (the carry-forward pattern is supported when paired with documented search depth; the un-paired version surfaced as ASSUMPTION-074 inherits the search-depth-asymmetric concern)
