SEARCH-AGAINST-PRESUMPTION-520:
  Date searched: 2026-07-23
  Original item: PRESUMPTION-520
  Original statement: [inferred] Catching three of its own errors is read as the contract working, presuming the errors caught are representative of the errors present. No denominator.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-520
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the self-catch framing without an undetected-error estimate
      15b: Searched for challenging literature — arguments that self-catch is nonetheless informative
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No (weak boundary only)

  Sources:
    1. Boundary observation: Catching three errors is not *zero* information — it establishes a non-zero detection capability and rules out "the process never self-corrects." So "no denominator" overstates slightly; the count bounds detection from below even without an estimate of the remainder.
    2. Reliability-growth / defect-discovery models (e.g. Musa, software reliability engineering). — One could argue trend in catches over time is informative even without seeding. But these models still require *multiple periods and an assumed discovery distribution* to estimate remaining faults — they do not rescue a single day's "caught three."

  Strength of challenge: None to Weak

  Summary: 15b found no source contradicting the presumption. The only qualification is that a positive catch count is weak positive evidence of *some* detection capability — but it remains true that it says nothing about the undetected remainder, which is exactly the presumption's point. The demand for a denominator (via seeding or capture-recapture) stands unchallenged.

  Specific risks: None against the claim.

  Mitigations available: Fault seeding (inject known errors, measure re-catch fraction) converts "caught three" into a detection rate; this is the named in-house test.

  STEELMAN:
    Item: PRESUMPTION-520
    Strongest counterargument (against the presumption): If the *class* of caught errors is the same class as most errors produced (e.g. the recurring slug-prefix defect), then catching them is representative by construction, and the denominator worry is moot. But this requires knowing the error-class distribution — which is itself the missing denominator — so the counterargument presupposes what it needs to prove.
    What would need to be true for C2A2 to be safe: A seeded-error catch rate, or a capture-recapture overlap between two independent checkers.
    How to test: Seed N known errors of varied classes; report the fraction re-caught.

  Recommendation: NO-CHALLENGE-FOUND
