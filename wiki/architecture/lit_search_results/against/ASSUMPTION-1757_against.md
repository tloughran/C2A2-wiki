SEARCH-AGAINST-ASSUMPTION-1757:
  Date searched: 2026-10-10
  Original item: ASSUMPTION-1757
  Original statement: 15c counted 15a/15b agreement on sources fetched from a shared cache as one
    reading, not two. Question under test: is discounting correlated evidence to a single reading the
    right correction when two "independent" reviewers share retrieval?
  Under test: the implied correction "shared retrieval => collapse to n = 1". I searched for evidence
    that this is too crude (partial-correlation / effective-sample-size alternatives) or
    over-conservative (agreement on the same source still carries independent information).

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today. Worked only from the item statement
    supplied by the orchestrator plus my own searches.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1757
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-10-09): Extracted stated practice from 15c: 15a/15b agreement on shared-cache sources
        counted as one reading; queued with question on correlated-evidence correction.
      15b (2026-10-10): Searched for challenging literature. 3 searches (design effect / effective
        sample size with correlated raters; wisdom of crowds with shared information; double data
        extraction from the same source text); 2 fetches (McCoy & Prelec 2024, abstract; Buscemi et
        al. 2006, abstract). No fetch failures.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Two fetched abstracts; rest search-result. Broader search recommended.

  Search scope: preliminary (3 searches, 2 fetches).

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Buscemi N, Hartling L, Vandermeer B, Tjosvold L, Klassen TP. 2006. "Single data extraction
       generated more errors than double data extraction in systematic reviews." J Clin Epidemiol
       59(7):697-703. doi:10.1016/j.jclinepi.2005.11.010. [fetched, abstract] Single extraction gave
       21.7% more errors than double extraction (P = .019); effect estimates mostly similar.
       Bearing: in the standard evidence-synthesis practice, two reviewers reading the SAME source
       text are treated as two readings, because the independent part is the interpretation, not the
       retrieval. Shared input does not make the second reading worthless. Collapsing to one throws
       away a measurable error reduction.
    2. McCoy J & Prelec D. 2024. "A Bayesian Hierarchical Model of Crowd Wisdom Based on Predicting
       Opinions of Others." Management Science 70(9):5931-5948. doi:10.1287/mnsc.2023.4955.
       [fetched, abstract] "shared information across respondents can result in correlated errors";
       proposes modelling that dependence rather than deleting judgments. Bearing: the field corrects
       for shared information by MODELLING it. It does not collapse correlated judges to one.
    3. Palley AB & Soll JB. 2019. "Extracting the Wisdom of Crowds When Information Is Shared."
       Management Science 65(5):2291-2309. [search-result] Correlated errors from shared
       information LIMIT the accuracy gain from averaging but do not remove it. Their "pivoting"
       method separates shared and private components. Bearing: the correct quantity is somewhere
       between 1 and 2 effective readings, and you can estimate it.
    4. Design-effect / effective-sample-size literature (Statistics Canada, Survey Methodology 2020,
       "Considering interviewer and design effects when planning sample sizes"; arXiv 2601.09084
       "How Many Human Judgments Are Enough?") [search-result] Effective n = n / DEFF with
       DEFF = 1 + (m - 1)ρ. For k raters with inter-rater correlation ρ_r the variance factor is
       (1 + (k - 1)ρ_r)/k. With k = 2 this gives an effective count of 2/(1 + ρ). That equals 1
       ONLY at ρ = 1. The survey paper also warns that empirical design effects are often
       over-estimated when rater effects are mixed up with design effects. Bearing: "one reading" is
       the ρ = 1 limit and is conservative for any partial correlation.
    5. Gartlehner, SWAR28 slides (2023) [search-result] A second checker can also ADD errors by
       changing a correct entry. Bearing: this is a boundary condition in the other direction. The
       second reading is not always additive either.

  Summary: Most of the literature I found treats shared information as a reason to MODEL partial
    dependence (effective sample size, design effect, shared/private decomposition), not as a reason
    to count two judges as one. Collapsing to one reading is the ρ = 1 limit. It is right only when
    the two reviewers share both the retrieval AND the interpretive process (for example the same
    model, prompt and context). In systematic reviews, two people reading the same full text count
    as two readings and measurably reduce error, so shared retrieval alone does not justify the
    collapse. On the other side, the correction errs in the safe direction (it under-claims) and is
    cheap. That is why this is a partial challenge, not a refutation.

  Specific risks: (a) Systematic under-weighting of genuine convergence, so items stay
    "UNTESTED/CONTESTED" when interpretation-level agreement was informative. (b) A binary rule hides
    where the real dependence sits. 15a and 15b may share much more than the cache (same base model,
    similar prompts), in which case even "different sources" readings are correlated and the rule
    under-corrects elsewhere.

  Mitigations available: Record the dependence channels (retrieval, model, prompt) per agreement.
    Report an effective-count range (1 to 2) instead of a point. Keep the "as extracted" readings
    separately from any consensus (Cochrane Handbook 7.6.5 practice).

  STEELMAN:
    Item: ASSUMPTION-1757
    Strongest counterargument: Independence is not binary, and the statistics of correlated judges
      is well developed. Two reviewers who read the same document but reason separately give an
      effective sample size of 2/(1 + ρ), which lies strictly between 1 and 2 unless their
      interpretations are perfectly correlated. Evidence synthesis has relied on double reading of
      the same text for decades precisely because it catches about a fifth more errors. Counting
      that as one reading discards real information. It also lends false precision to the rule's
      "conservatism", because it ignores the deeper shared channel (same model family) that the
      cache rule does not touch.
    What would need to be true for C2A2 to be safe: The 15a/15b interpretive processes are so
      similar (same model, near-identical prompts) that ρ is close to 1 anyway, OR the
      collapse-to-one rule is applied only where both retrieval and interpretation are shared.
    How to test: On a sample of shared-cache items, compare 15a and 15b's extracted claims and
      gradings from the same source (not just the verdicts). Estimate ρ. If the verdicts diverge
      materially on the same text, the readings are not one reading.

  Boundary conditions identified:
    - Collapse-to-one is correct only at ρ ≈ 1 (shared retrieval AND shared interpretation).
    - Where the error being guarded against is retrieval error (a bad or stale cached copy), shared
      retrieval does make the readings fully dependent for that error class. The rule is apt for
      source-validity claims and too crude for interpretation claims.
    - A second reader can introduce errors (Gartlehner), so "two readings" is not automatically
      better than one either.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: shared with PRESUMPTION-1115, PRESUMPTION-1117, PRESUMPTION-1118,
    PRESUMPTION-1119. Common vulnerability: binary corrections (here: 2 readings → 1) plus added
    meta-process, where the literature favours graded, documented handling. Risk level: High. Full
    flag text in PRESUMPTION-1117_against.md.
