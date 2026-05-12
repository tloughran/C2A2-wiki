SEARCH-FOR-ASSUMPTION-068:
  Date searched: 2026-04-27
  Original item: ASSUMPTION-068
  Original statement: "Master-wiki-narrative-gap is to be surfaced rather than fabricated (re-affirmation of PREMISE-006 against today's 4-day gap)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-068
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 morning walk handoff — re-affirmation of flag-don't-fabricate stance under a 4-day gap
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. SRE / operational-monitoring literature (Beyer et al. 2016 "Site Reliability Engineering"; Limoncelli et al. 2014 "The Practice of Cloud System Administration") — surface-don't-fabricate is the canonical pattern: missing data is itself a signal, not a problem to paper over.
    2. Incident-response literature (Allspaw 2009; Adkins et al. "Building Secure & Reliable Systems") — fabricating data to fill gaps in audit logs or post-mortems is an explicit anti-pattern; honest gaps preserve epistemic integrity.
    3. PREMISE-006 (validated_premises.md) — already-incorporated C2A2 premise that flag-over-reconcile is correct on master-wiki staleness; this assumption is a re-affirmation, not a new claim.
    4. Statistical-process-control literature (Shewhart 1931; Wheeler 1995): out-of-spec values are flagged, not interpolated; same principle applies to narrative gaps.
    5. Knowledge-management literature on staleness (Jennex 2007; Maier 2007) — explicit acknowledgment of gaps preserves trust; silent interpolation degrades user calibration.

  Strength of support: Strong

  Summary: The flag-don't-fabricate stance is canonical across SRE, incident response, statistical-process control, and knowledge-management literatures. Re-affirming PREMISE-006 in a 4-day-gap case is consistent with all five and inherits the prior validation. The literature treats this as a robust principle that does not weaken with longer gaps; if anything, longer gaps make surfacing more important, not less.

  Caveats: (a) The 4-day gap is the largest the principle has handled in C2A2; whether the principle scales to weeks or months is not separately tested (PRESUMPTION-077); (b) "surface" must be operationalized — silent gaps that aren't surfaced anywhere are not surfaced.

  Recommendation: SUPPORTED (re-affirmation of an already-validated principle; literature consensus is strong)
