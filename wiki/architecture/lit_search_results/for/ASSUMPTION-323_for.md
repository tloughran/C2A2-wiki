SEARCH-FOR-ASSUMPTION-323:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-323
  Original statement: "A commit-message self-report ('+38 PRS triplets') is an adequate cross-check that verifies the derived yield series."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-323
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the verification step grounding confidence in the yield series
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Triangulation / convergent validation (Campbell & Fiske 1959; Denzin) — agreement between an independently-produced figure (the commit author's contemporaneous count) and a derived figure is a genuine convergence signal; two different operations pointing at the same number raises confidence above either alone.
    2. Software-process measurement — using a contemporaneous developer self-report as a sanity check on an automated extraction is a recognized lightweight validation; a matching independent witness is real corroborating evidence.

  Strength of support: Weak-Moderate

  Summary: A commit-message count is an independent witness produced at the time of the work, so a match with the derived series is a legitimate convergence/triangulation signal that does raise confidence locally. Where the self-report and the pipeline agree on a specific day's delta, that day is corroborated by two independent operations. The honest support is "a matching contemporaneous self-report is real corroboration for the point it touches" — not "it verifies the whole series."

  Caveats: The corroboration is point-local, not series-wide (the "+38" touches one window); commit messages are known to be unreliable narrators (aspirational, rounded, batched, or referring to prior work). Support is conditional on the self-report being independent of the pipeline and on coverage being more than a single point (see PRESUMPTION-356 on single-confirmation induction; ASSUMPTION-322).

  Search scope: triangulation/convergent validation; software self-report as sanity check; commit-message reliability. Comprehensive.

  Recommendation: PARTIALLY-SUPPORTED
