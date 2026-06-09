SEARCH-FOR-PRESUMPTION-318:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-318
  Original statement: [inferred] Building the auto-push task before probing whether the sandbox could push presumed capabilities instead of checking them (violates Rules 1/8).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-318
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated build-then-discover ordering that skipped a capability check.
      15a: Searched for any support that building before probing capabilities is acceptable practice.
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Walking-skeleton / spike practice (Cockburn; "Growing Object-Oriented Software Guided by Tests," Freeman & Pryce). — Even the most permissive agile guidance says: when an end-to-end capability is uncertain, build the THINNEST end-to-end probe FIRST to prove the path works; this is the opposite of building the full task before probing.
    2. (No source supports build-before-probe as a positive pattern.)

  Strength of support: None

  Summary: No literature supports building a capability-dependent automation before confirming the capability exists. The closest adjacent practice — the walking skeleton / spike — actually prescribes a tiny end-to-end probe FIRST precisely to retire this risk, which contradicts the presumed ordering rather than supporting it.

  Caveats: This is a clean NO-SUPPORT-FOUND for the supportive direction; the methodological literature (and Tom's own Rules 1 and 8) points the other way. The AGAINST search develops the strong case.

  Recommendation: NO-SUPPORT-FOUND
