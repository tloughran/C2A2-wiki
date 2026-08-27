SEARCH-FOR-PRESUMPTION-849:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-849
  Original statement: "[inferred] That a zero from a blocked channel and a zero from a searched channel are the same register entry."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-849
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by placing three same-day zeros of different provenance against one
        register slot; continues OPEN-158 into a new domain.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web search, 2026-08-25. Queries run: (1) missing-data mechanisms —
    MCAR/MAR/MNAR, complete-case analysis, ignorability conditions; (2) impact of
    unretrieved records on meta-analytic conclusions; (3) the Egger et al. empirical study
    of search comprehensiveness; (4) Schmucker et al. on unpublished and grey-literature
    data; (5) PRISMA 2020 accounting for records not retrieved vs. records excluded;
    (6) dual independent screening and reviewer error rates. Venues reached: PMC/NCBI
    Bookshelf, PLOS ONE, Health Technology Assessment (NIHR), Journal of Clinical
    Epidemiology listings, Columbia Mailman methods pages, PRISMA implementation guides.
    Status: ADEQUATE for the missing-data-mechanism limb; ADEQUATE for the
    does-it-change-conclusions limb; PRELIMINARY for negative-result registries, which I
    did not reach — broader search recommended. Session web-search budget was exhausted
    before that query could be run. I could not retrieve the Egger et al. abstract (PubMed
    fetch returned no body), so its findings are not relied on here.

  Supporting evidence found: Partial

  Sources:
    1. "Types of Missing Data," in Managing Missing Data in Patient Registries. NCBI
       Bookshelf NBK493614, https://www.ncbi.nlm.nih.gov/books/NBK493614/ — Supplies the
       only clean warrant for the presumption. Under MCAR, "the probability of missing data
       is entirely independent of both observed and unobserved variables"; MCAR "is
       sufficient to guarantee that the missingness mechanism is ignorable," and a
       complete-case analysis under MCAR yields unbiased estimates. If a channel's
       blockage is genuinely independent of what the channel would have contained, then a
       blocked-channel zero and a searched-channel zero are exchangeable and the presumption
       holds exactly. (search-snippet-only)
    2. Missing-data methodology, extended condition. Reported in the same body of work: "the
       complete case analysis will be unbiased due to missing data if the missingness is
       independent of the outcome under study, a condition that can be present whether the
       data are MAR or MNAR." — Widens the supporting condition: strict MCAR is not required,
       only independence of missingness from the outcome. This is a meaningfully weaker and
       more attainable premise than full MCAR. (search-snippet-only; primary source not
       isolated)
    3. Schmucker, C. et al., 2017. "Systematic review finds that study data not published in
       full text articles have unclear impact on meta-analyses results in medical research."
       PLOS ONE, 12(4):e0176210.
       https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0176210 —
       Supports the presumption in its consequentialist form: the review found it is "not
       possible for a meta-analyst to judge beforehand whether the addition of unpublished
       and grey literature study data impacts the pooled effect estimates and leads to a
       change in overall conclusions," and that even where included studies would have been
       impacted, "it is still possible that this would not affect the conclusions." If the
       distinction between retrieved and unretrieved material does not systematically move
       conclusions, then collapsing the two zeros into one register entry is defensible in
       practice even if not in principle. (search-snippet-only)
    4. Egger, M., Juni, P., Bartlett, C., Holenstein, F. & Sterne, J., 2003. "How important
       are comprehensive literature searches and the assessment of trial quality in
       systematic reviews? Empirical study." Health Technology Assessment, 7(1). PubMed
       12583822. — The canonical empirical test of whether unretrieved material changes
       conclusions, and the natural home for evidence on this presumption. Bibliographic
       details verified from search results; the abstract could not be retrieved, so its
       direction and magnitude are NOT verified and are NOT relied on here. Listed as a
       search lead, not as evidence. (bibliographic details verified; content unverified)
    5. Dual-screening evidence. Reported in the screening-methodology literature: single
       screeners missed a median of 5% of studies that two independent reviewers would have
       included, and even experienced reviewers missed a median of 3% [primary citation not
       isolated; encountered via DistillerSR and Queen's University Library screening
       guidance]. — Weakly supportive by scale: the magnitude of loss from an incomplete
       ascertainment process is small in the median case, which makes register-level
       collapsing of the two zero types a low-consequence simplification most of the time.
       (search-snippet-only, secondary reports)

  Strength of support: Weak

  Summary: Support for this presumption exists but is entirely conditional and is
    consequentialist rather than principled. The missing-data literature identifies the
    exact condition under which the presumption is exactly true: if the mechanism that
    blocked the channel is independent of what the channel would have contained — MCAR, or
    more weakly, missingness independent of the outcome — then the missingness is ignorable,
    complete-case analysis is unbiased, and a blocked zero carries the same information as
    a searched zero. Separately, Schmucker et al. found that the impact of unretrieved and
    unpublished material on meta-analytic conclusions is unpredictable rather than reliably
    conclusion-changing, and the dual-screening literature puts the median loss from an
    incomplete ascertainment process in the low single-digit percentages. Taken together
    these license a practical, not an epistemic, equivalence: collapsing the two zeros is
    usually low-consequence. What no source supports is the presumption in its unconditional
    form, and the missing-data literature that supplies the supporting condition is also the
    literature that says the condition is rarely met.

  Caveats:
    - The supporting condition is self-undermining in this case. MCAR requires that
      missingness be independent of the underlying value. A channel that is blocked
      *because of what it contains* — access controls, paywalls, robots directives,
      institutional gating, rate limiting triggered by query specificity — is close to a
      textbook MNAR mechanism. The very fact that the channel was identified as primary
      suggests its content is not exchangeable with the substitute's.
    - The same source that supplies the MCAR warrant states plainly that "MCAR is generally
      unrealistic." The support here is a conditional whose antecedent the literature
      expects to be false.
    - Schmucker et al.'s finding is that the impact is *unclear*, not that it is *null*.
      Reading "unclear" as "safe to collapse" is an inference the authors do not make; their
      framing is that even the most comprehensive search "will not allow a final judgment
      whether the identified sample is in fact complete and representative."
    - The 3–5% dual-screening figures are secondary reports whose primary source I did not
      isolate, and they concern human screener error, not channel blockage — a different
      mechanism.
    - Encountered incidentally rather than sought, and recorded for scope honesty: PRISMA
      2020 maintains "reports not retrieved" as a separate line item from "records screened
      and excluded," with "reports assessed for eligibility" defined as sought-for-retrieval
      minus not-retrieved. The reporting standard in the field therefore explicitly declines
      to make the two the same entry. This is not offered as supporting evidence; it is
      noted so the scope of this search is not overread.
    - Three same-day zeros of different provenance (per 14b's transform) is a very small n,
      and none of the retrieved literature addresses register design for agentic evidence
      pipelines.
    - I did not reach the negative-result-registry literature, which is where any positive
      case for recording nulls without provenance distinction would most likely live.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: PRESUMPTION-849, register-design limb.
    Searched: six queries across missing-data methodology, meta-research on unretrieved
      studies, and reporting-standard guidance, for any treatment of whether a null arising
      from an inaccessible channel should be recorded identically to a null arising from a
      successful search.
    Finding: the *statistical* structure of the question is thoroughly addressed —
      MCAR/MAR/MNAR is exactly the right frame and the field has worked it out in detail, so
      the general question is not novel. What is not addressed anywhere I reached is the
      register-design question: whether a provenance-blind null entry is defensible in an
      evidence system that will later be queried as if all its zeros were equivalent.
    Unaddressed sub-claim, precisely: "a null record that does not carry its own provenance
      (blocked vs. searched) supports the same downstream inferences as one that does."
    Implication: the presumption should be re-expressed as a conditional on the missingness
      mechanism rather than adopted flat. Whether the register can carry that conditional is
      an open design question the literature does not answer.
    Recommended status: NOVEL (register-design limb only; the statistical limb is not novel).
