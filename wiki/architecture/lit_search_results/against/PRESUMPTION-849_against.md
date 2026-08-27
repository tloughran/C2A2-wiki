SEARCH-AGAINST-PRESUMPTION-849:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-849
  Original statement: "[inferred] That a zero from a blocked channel and a zero from a searched
    channel are the same register entry."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-849
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by placing three same-day zeros of different provenance against one
        register slot; continues OPEN-158 into a new domain.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Queries run 2026-08-25: PRISMA 2020 flow-diagram treatment of unretrieved reports
    versus excluded records; missing-data mechanisms MCAR/MAR/MNAR and informative missingness;
    testability of MAR versus MNAR; absence-of-evidence interpretation; reporting bias from
    unrecorded nulls. Venues reached: PRISMA Statement, BMJ, Health and Quality of Life Outcomes,
    PharmacoEconomics, Springer/Elsevier missing-data methods literature, university systematic-
    review guidance (UNC, SDSU, Temple, Gonzaga), ILCOR/CoSTR. Date range: 1976–2025. Depth:
    COMPREHENSIVE for the methodological principle; PRELIMINARY for the specific three-zeros
    instance, which I did not inspect. Gaps: web-search budget exhausted before a dedicated search
    on negative-result registries; the Rubin 1976 and Little & Rubin monograph details are cited
    from secondary description rather than verified at source.

  Challenging evidence found: Yes

  Sources:
    1. PRISMA 2020 flow diagram. https://www.prisma-statement.org/prisma-2020-flow-diagram
       — Decisive on the point. The reporting standard mandates that "reports sought for retrieval"
       and "reports not retrieved" be counted separately from "records excluded," precisely because
       a record that could not be obtained is not the same object as a record that was obtained and
       found not to qualify. Reports assessed for eligibility is defined as reports sought minus
       reports not retrieved. The distinction PRESUMPTION-849 collapses is a mandatory field in the
       dominant evidence-synthesis standard. FULL-TEXT (standard plus multiple university
       implementations: UNC, SDSU, Temple, Gonzaga guides consulted 2026-08-25).
    2. Page, M. J. et al., 2021. "The PRISMA 2020 statement: an updated guideline for reporting
       systematic reviews." BMJ 372:n71. [details unverified — cited from the flow-diagram
       resource and standard practice, not verified at source in this search]
       — The parent statement for source 1.
    3. Rubin, D. B., 1976. "Inference and missing data." Biometrika. [details unverified]
       — Origin of the MCAR / MAR / MNAR taxonomy. The relevant principle: missingness is ignorable
       only if the mechanism producing it is independent of the unobserved values. A blocked channel
       is a missingness mechanism; a searched channel is an observation. Cited from secondary
       description in the sources below.
    4. Little, R. J. A. & Rubin, D. B. Statistical Analysis with Missing Data. [details unverified;
       2002 and 2019 editions both cited in the secondary sources reached]
       — Standard reference for the result that MAR versus MNAR cannot be distinguished from the
       observed data alone, i.e. one cannot certify from within the run that a blocked zero is
       equivalent to a searched zero.
    5. "Simple imputation methods were inadequate for missing not at random (MNAR) quality of life
       data." Health and Quality of Life Outcomes, 2008, 6:57. DOI 10.1186/1477-7525-6-57
       — Empirical demonstration that filling MNAR gaps with a default value produces biased
       estimates. Substituting "zero" for an unread channel is exactly a default-value imputation.
       Authors not resolved from snippet. SNIPPET-ONLY.
    6. "Every missing not at random model has got a missing at random counterpart with equal fit."
       [Molenberghs et al., attribution from the ResearchGate record; venue and year unverified]
       https://www.researchgate.net/publication/4993363
       — Formal statement of the untestability point: for any MNAR model there is an MAR model
       fitting the observed data equally well, so the observed data never license the assumption
       that missingness is benign. SNIPPET-ONLY, details unverified.
    7. "Sensitivity Analysis for Not-at-Random Missing Data in Trial-Based Cost-Effectiveness
       Analysis: A Tutorial." PharmacoEconomics, 2018. DOI 10.1007/s40273-018-0650-5
       — The accepted remedy where the mechanism cannot be identified: report a range under
       alternative missingness assumptions rather than a point value. Authors not resolved.
       SNIPPET-ONLY.
    8. Altman, D. G. & Bland, J. M., 1995. "Statistics notes: Absence of evidence is not evidence
       of absence." BMJ 311:485. PMC2550545.
       — The inferential rule: a non-finding is evidence of absence only in proportion to the
       power of the instrument. A blocked channel has zero power, so its zero carries zero
       evidential weight, whereas a searched channel's zero carries weight proportional to its
       recall. Two different quantities cannot be one entry. FULL-TEXT.
    9. Greenberg, S. A., 2009. "How citation distortions create unfounded authority: analysis of a
       citation network." BMJ 339:b2680. PMID 19622839.
       — Shows the downstream mechanism: once records that would weaken a claim drop out of the
       accounting, the claim accumulates unfounded authority through amplification. Directly models
       what happens when unretrieved-negative and searched-negative are not distinguished.
       ABSTRACT plus James Lind Library summary.

  Strength of challenge: Strong

  Summary: This presumption is contradicted by an explicit, mandatory provision of the dominant
    reporting standard in evidence synthesis. PRISMA 2020 does not merely permit the distinction
    between "reports not retrieved" and "records excluded" — it requires both to be counted and
    reported separately, because a record that could not be obtained has a different epistemic
    status from one that was obtained and rejected. The statistical literature explains why. Under
    the Rubin taxonomy a blocked channel is a missingness mechanism, and the reason a block matters
    is that blocking is very often informative: paywalls, access restrictions, and outages correlate
    with venue, recency and language, which correlate with content. That makes the missingness
    plausibly MNAR, and the Molenberghs-type result means the observed data can never certify
    otherwise from inside the run. Altman & Bland give the corresponding inferential rule: the
    weight of a zero scales with the power of the instrument that produced it, and an unread channel
    has none. Greenberg 2009 supplies the empirical consequence — 242 papers and 220,553 supporting
    citation paths generating unfounded authority, because negatives that dropped out of the
    accounting were never subtracted from the belief.

  Specific risks: If a blocked zero and a searched zero occupy one register slot, three things
    break. First, the register loses recoverability: a later reader cannot tell which zeros are
    revisitable (unblock the channel and look again) and which are settled, so blocked items are
    never retried and become permanent. Second, the bias is directional, not random — blocked
    channels skew toward paywalled, recent, non-English and non-indexed material, so the surviving
    evidence base is systematically tilted toward the accessible and the mainstream, which is
    exactly the tilt Greenberg documents producing unfounded authority. Third, confidence is
    miscomputed downstream: a slot holding three zeros of different provenance reads as
    triple-corroborated absence when it may be one weak observation plus two non-observations, so
    the pipeline's own certainty estimates inflate in proportion to how badly its channels are
    failing. The 14b transform notes three same-day zeros of different provenance against one slot
    — that is the inflation happening in the concrete case.

  Mitigations available:
    - Split the field. Adopt the PRISMA 2020 two-field structure: sought / not-retrieved recorded
      separately from screened-and-excluded (https://www.prisma-statement.org/prisma-2020-flow-diagram).
    - Attach a provenance tag and an instrument-power estimate to every zero, so downstream
      consumers can weight it (Altman & Bland 1995, BMJ 311:485).
    - Where the mechanism cannot be identified, report a range rather than a point — the
      sensitivity-analysis convention (PharmacoEconomics 2018, DOI 10.1007/s40273-018-0650-5).
    - Never default-impute. Treating an unread channel as zero is a simple-imputation move, shown
      inadequate under MNAR (Health and Quality of Life Outcomes 6:57).
    - Make blocked zeros a retry queue rather than a terminal state, so the missingness is
      recoverable rather than absorbed.

  STEELMAN:
    Item: PRESUMPTION-849
    Strongest counterargument: The two zeros are not the same measurement and should never share a
      slot. A searched-channel zero is an observation with an estimable error rate; a blocked-channel
      zero is a non-observation with no error rate at all, and the standard missing-data result is
      that you cannot tell from the observed data whether the missingness was benign. Worse, the
      blocking is likely to be informative rather than incidental — access failures track venue,
      recency and indexing, all of which track content — which makes this the MNAR case where
      substituting a default value is known to bias estimates. The reporting standard that governs
      this exact situation, PRISMA 2020, treats the distinction as mandatory rather than optional,
      which is about as clear a verdict as a methodological literature gives. And the collapse is
      self-concealing: once the provenance is dropped, no downstream reader can reconstruct which
      zeros were real, so the error cannot be caught later.
    What would need to be true for C2A2 to be safe: The collapse would be harmless only if blocking
      were demonstrably independent of content — i.e. the channel failed for reasons uncorrelated
      with what it contained (a random outage rather than an access-tier restriction) — AND the
      blocked channel were fully redundant with a channel that was successfully searched, so nothing
      unique was lost. Both conditions would have to be established affirmatively, not assumed. In
      the case at hand neither has been shown. Failing that, the minimum safe condition is that the
      register carries provenance per zero even if it continues to store them in one slot, so the
      distinction is recoverable.
    How to test: Yes, directly. For the three same-day zeros in question, retry each blocked channel
      once access is restored and record whether the zero survives. Across a sample of blocked-then-
      retried items, the proportion of zeros that flip is a direct empirical estimate of how wrong
      the collapse is — if it is near zero the presumption is benign for this pipeline, and if it is
      appreciable the register needs the split field. This is cheap, repeatable, and yields a
      calibration constant rather than a binary verdict.

  Recommendation: CHALLENGED
