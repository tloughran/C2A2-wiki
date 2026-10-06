SEARCH-FOR-ASSUMPTION-1315:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1315
  Original statement: "the C2A2 wiki took its largest single-night ingest of the series at 22:00 (85 new
    PRS entries across ten registers, plus CROSS-132 through CROSS-135), **which re-opens 147
    absence-declinations across 74 syntheses as unverified**; two were hand-checked and both still hold."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1315
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim. Cross-project (Summa), and therefore within PRESUMPTION-945's open scope
        question. Recorded because it is the one place in the estate where the ingest was treated as
        *invalidating* rather than as accretion — 85 triplets in, 147 prior claims out of verified
        status. No C2A2-side run drew that consequence.
      15a: Searched for supporting literature; the sampling limb is settled arithmetically and against
        the assumption; the invalidation limb is supported.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check: PREMISE-182 settles the sampling limb outright and the intake said so.
    - PREMISE-182: "A CORROBORATION COUNT LICENSES FAR LESS THAN IT APPEARS TO, AND THE EXACT AMOUNT IS A
      CLOSED-FORM IDENTITY. Under n-for-n agreement with zero observed failures, the one-sided lower
      confidence bound on the underlying success rate is R_L = (1 − C)^(1/n) — the Clopper–Pearson exact
      limit specialised to zero failures." This is directly applicable and gives a number. The search was
      run anyway per OPEN-192, and the search's contribution is to confirm the premise's formula against
      the external literature and to supply the exact finite-population version, which the premise's
      binomial form does not.
    - PREMISE-126: a staleness-triggered re-check that only advances the date certifies "not-yet-expired,"
      which is categorically weaker than "re-tested against current state." Supports the invalidation
      limb.
    - PREMISE-049: an unverified cross-tradition lead must never be treated as true until a targeted
      confirmation search promotes it. Supports the invalidation limb's conservatism.
    - PREMISE-189: absence claims require an independently maintained expectation about what should be
      present — governs what an "absence-declination" can mean at all.

  Supporting evidence found: Yes (invalidation limb); No (sampling limb — the arithmetic runs against it)

  Sources:
    1. Clopper C.J. & Pearson E.S. 1934. "The use of confidence or fiducial limits illustrated in the
       case of the binomial." Biometrika 26:404-413. — SECONDARY (the exact-limit formula is standard and
       was confirmed across multiple retrieved expositions; the 1934 paper was not fetched) — Gives the
       exact one-sided limit. For n=2 successes with zero failures at 95% confidence, the lower bound on
       the success rate is 0.05^(1/2) = 0.2236. Computed and checked: 22.4%.
    2. "Rule of three (statistics)" — the 3/n approximation for the upper bound on an event rate after
       zero observations in n trials, derived from solving (1−p)^n = 0.05. — SECONDARY (multiple
       retrieved statistical expositions, incl. Triola's textbook treatment and pmean.com's zero-events
       note) — Explicitly documented as a good approximation only for n > 30. At n=2 the rule returns
       3/2 = 1.5, i.e. an upper bound above 1, which is the approximation announcing that the sample
       carries no information. This is the cleanest way to state the finding.
    3. Exact hypergeometric bound for this specific case. — VERIFIED (computed here; arithmetic shown) —
       Sampling 2 of 147 without replacement, observing zero failures. P(0 failures | D defective) =
       C(147−D,2)/C(147,2). This exceeds 5% for all D ≤ 113 (at D=113, P = 5.23%) and falls below at
       D=114 (P = 4.92%). So the 95% upper confidence bound on the number of invalid declinations is 113.
       The two hand-checks are consistent, at the 5% level, with up to 113 of the 147 absence-declinations
       being wrong — i.e. they exclude essentially nothing.
    4. Acceptance sampling practice (MIL-STD-105 / ANSI-ASQ Z1.4 lineage; zero-acceptance-number plans). —
       SECONDARY — Standard sampling plans for a lot of ~150 at even modest AQLs call for sample sizes in
       the tens, not 2. n=2 does not appear in any standard plan for a lot of this size, which is the
       practitioner's way of saying the same thing the arithmetic says.
    5. Re-verification-after-change practice: regression testing and impact analysis; ISO/IEC/IEEE 29119
       and the change-based-retest principle; PREMISE-126's certification analogue. — SECONDARY — The
       standard position is that a change within a claim's scope invalidates prior verification of that
       claim and obliges re-test of the affected set, with the affected set determined by impact
       analysis rather than by sampling. Supports the invalidation limb and, notably, does NOT support
       discharging the obligation by sampling.

  Strength of support: Strong (limb a: an absence claim is invalidated by later ingest into its scope);
                       None (limb b: that 2 of 147 hand-checks license the remaining 145).

  Summary: The run did the hard part right and the easy part wrong. Limb (a) — treating an ingest into an
    absence claim's scope as invalidating that claim's verified status — is the conservative and correct
    standard; it matches change-based retest practice, is supported by PREMISE-126's distinction between
    "not-yet-expired" and "re-tested," and is notable as the one place in the estate where an ingest was
    treated as invalidating rather than accretive. Limb (b) is arithmetically hopeless and does not need
    a literature to settle it. Under the Clopper-Pearson identity that PREMISE-182 already supplies, 2
    for 2 with zero failures gives a 95% lower bound on the success rate of 22.4%. Under the exact
    hypergeometric calculation for this finite population, the observation excludes only D ≥ 114: the
    data are consistent with 113 of the 147 declinations being invalid. The rule of three announces the
    same thing by returning an upper bound greater than 1. Two hand-checks are a spot check, and the run
    was right to report them as "two were hand-checked and both still hold" rather than as clearance —
    but the sentence sits inside a claim structure that reads as licensing, and it should not be allowed
    to.

  Caveats:
    - The confidence bounds assume the two checked items were selected in a way uninformative about the
      rest. If they were the two easiest or the two most recently touched, the bound is optimistic and
      the true position is worse, not better. No selection rule is recorded.
    - The bounds also assume exchangeability across the 147. They are almost certainly not exchangeable:
      a declination's exposure to invalidation depends on whether the 85 new triplets fall in its scope,
      which is checkable directly. Impact analysis — enumerate which of the 147 have scope overlap with
      the 85 — is both cheaper and strictly more informative than any sampling plan, and is what the
      re-verification literature actually prescribes. This is the operative recommendation.
    - Limb (a) has a cost the item does not price. If every ingest invalidates every in-scope absence
      claim, and ingests are nightly, then absence claims are never in a verified state for long and the
      status becomes uninformative. PREMISE-095's arrival-vs-service argument applies: 147 re-checks
      re-opened by one night's ingest, against an unstated re-check rate, is a queue-stability question
      and nobody has computed it.
    - Cross-project scope: this is a Summa finding inside PRESUMPTION-945's open scope question. Whether
      C2A2 premises govern it is unruled, and this search takes no position on that.
    - Computation note: the hypergeometric figures above were computed during this search and are marked
      VERIFIED in the sense that the arithmetic was executed and checked, not in the sense that a source
      publishes them. The underlying identity is standard.

  Search scope: comprehensive search — Clopper-Pearson exact binomial limits and zero-failure bounds, the
    rule of three and its stated n>30 validity condition, acceptance sampling plans for small lots,
    confidence intervals with zero events, re-verification and change-based retest obligations. Exact
    hypergeometric bound computed directly rather than searched.

  Recommendation: PARTIALLY-SUPPORTED — the recommendation rests on limb (a). Limb (b) is
    NO-SUPPORT-FOUND and is refuted arithmetically by this estate's own PREMISE-182: the correct statement
    is that 2 of 147 hand-checks license nothing, and the 95% upper bound on invalid declinations is 113.
    Recommend the 147 be dispositioned by scope-overlap impact analysis against the 85 new triplets, not
    by sampling; and that the phrase "two were hand-checked and both still hold" be carried with the
    bound attached wherever it is quoted (PREMISE-188).
