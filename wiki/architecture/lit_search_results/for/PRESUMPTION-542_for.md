SEARCH-FOR-PRESUMPTION-542:
  Date searched: 2026-07-25
  Original item: PRESUMPTION-542
  Original statement: [inferred] A 15d monthly re-check returning "ACTIVE, no change" is presumed to be genuine re-validation, but a staleness-triggered re-stamp may certify only "not-yet-expired," not "re-tested against current state" — recency conflated with re-confirmation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-542
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a time-triggered re-check read as re-confirmation
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. ISO/IEC 17021 & the ISO 9001 audit-cadence literature. — Standards explicitly distinguish a SURVEILLANCE re-check (sampled, confirms the certificate has not lapsed) from a RECERTIFICATION audit (comprehensive re-assessment against current state). The distinction exists precisely because a lapse-check is not a re-test; conflating them is a recognized failure of audit design.
    2. FAA CFI recency rule (post-expiration-date removal). — Removing the printed expiry did not remove the substantive requirement: a 24-month RECENCY-OF-EXPERIENCE re-exercise is still mandated. Recency ("not expired") and demonstrated current competence are treated as different certifications — direct analogue.
    3. Software-testing practice on flaky/decaying tests and "assertion-free" green tests (cf. project Rule 9: tests verify intent, not recency). — A test that passes without re-exercising the asserted business logic gives a green signal that is uninformative about current correctness; a re-stamp that does not re-run the underlying measurement is the same anti-pattern.

  Strength of support: Strong

  Summary: The presumption is well-supported: a time-triggered re-stamp certifies "not-yet-expired," which is categorically weaker than "re-tested against current state." Certification regimes that take re-validation seriously separate the lapse-check from the substantive re-assessment for exactly this reason. Applied to 15d, a monthly re-check that only advances the date without re-computing the underlying measurement is recency theatre, not re-confirmation — structurally identical to the project's own Rule-9 concern about tests that cannot fail.

  Caveats: A well-designed periodic re-check CAN re-exercise the assertion (the recertification audit does). The premise is about whether THIS re-check re-computes — an implementation question (see the in-house test and 15b boundary).

  Recommendation: SUPPORTED
