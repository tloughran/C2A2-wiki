SEARCH-FOR-PRESUMPTION-520:
  Date searched: 2026-07-23
  Original item: PRESUMPTION-520
  Original statement: [inferred] The daily run caught three of its own errors and reads this as the falsifiability contract working, presuming the errors caught are representative of the errors present. The self-catch rate is reported with no denominator.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-520
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the self-catch framing without an undetected-error estimate
      15a: Searched for supporting literature on defect-detection completeness, capture-recapture for undetected error, and fault seeding
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Eick, S.G., Loader, C.R., Long, M.D., Votta, L.G., Vander Wiel, S. (1992). "Estimating software fault content before coding." / capture-recapture inspection literature. — Establishes the standard method: the number of defects *found* is uninformative about defects *present* unless combined with an estimator (overlap between independent reviewers) that yields the unseen remainder. A raw catch count has no denominator, exactly as the presumption states.
    2. Mills, H.D. (1972). "On the statistical validation of computer programs" (fault seeding / error seeding). — Seeding known faults and measuring the fraction re-caught is the classical way to convert a catch count into a detection *rate*; without seeding or capture-recapture, "caught three" cannot be read as "few remain."
    3. Petersson, H., Thelin, T., Runeson, P., Wohlin, C. (2004). "Capture-recapture in software inspections after 10 years research." J. Systems and Software 72(3). — Reviews a decade of evidence that inspection effectiveness must be *estimated*, not read off the found-count; supports the demand for a denominator before any completeness claim.

  Strength of support: Strong

  Summary: The presumption restates a well-established result from software inspection science: the count of defects found is not an estimate of defects present. Two standard remedies exist — capture-recapture (overlap of independent detectors) and fault seeding (inject known errors, measure the re-catch fraction) — and both exist precisely because a bare catch count is known to be uninformative about the remainder. C2A2 reporting "caught three" as evidence the contract works, with no denominator, is the exact gap this literature was built to close.

  Caveats: The estimators require independence assumptions (correlated detectors inflate apparent completeness) — which links this item to the 15a/15b correlation concern (ASSUMPTION-499, REVISE-233); the fix is not free.

  Recommendation: SUPPORTED
