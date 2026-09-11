SEARCH-FOR-PRESUMPTION-948:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-948
  Original statement: "[inferred] That an item already answered by an ACTIVE premise should not be
    searched — that the register is an answer-set to be consulted rather than a set of claims to be
    re-exposed."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-948
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an absent alternative in a run proposing a change to this register's own
        routing. Declared interest: 14b is the party the change would constrain.
      15a: Searched for supporting literature; found a well-developed literature that supports stopping
        re-search of a settled question, and found that *every* branch of it pairs stopping with a
        named re-entry trigger.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-174 (ACTIVE) — "A REGISTER WITH EXPANSION AND NO CONTRACTION CANNOT REVISE... belief
      revision is DEFINED as contraction followed by expansion; a knowledge base that can add but not
      retract cannot perform revision." This bears directly and is the formal core of the item. It does
      not by itself rule on the *routing* question (whether to search), only on the *lifecycle*
      question (whether a premise can move). The two are separable and 14b separated them correctly.
    - PREMISE-183 (ACTIVE) — a filed flag is a live obligation with a closure test; a repeat filing is
      a reopening, not a new filing. Supplies the re-entry shape the register lacks.
    - PREMISE-184 (ACTIVE) — a novelty flag must be retracted explicitly when the literature is found;
      retraction is affirmative, not passive. This is a worked precedent for a status that *does* move.
      Note: this is evidence against the factual claim that no status has ever moved.
    - ASSUMPTION-1309, PREMISE-107 as named in the entry.
    Recording the hit per OPEN-192; searched anyway, which is the disposition OPEN-192 asks about.

  LIMB SPLIT:
    Limb A (STOPPING IS LEGITIMATE): a question whose answer is settled may rationally be exempted from
      further search, and the exemption is a saving rather than a defect.
    Limb B (STOPPING IS PERMANENT): the exemption needs no re-entry condition; consultation of the
      answer-set is the whole of the operation.

  Supporting evidence found: Yes (Limb A), No (Limb B)

  Sources:
    1. Cochrane / Living Evidence Network, 2023. "Proposed triggers for retiring a living systematic
       review." J Clin Epidemiol (PMID 36889900). — SECONDARY (PubMed page blocked by reCAPTCHA on
       retrieval; content via search summary) — Formalises the position that a continuously-updated
       evidence synthesis *should* stop: retire when evidence becomes conclusive for decision-relevant
       outcomes (judged by GRADE certainty), when the question ceases to be decision-relevant, when new
       studies are not anticipated, or when resources end. Directly supports Limb A: exempting a settled
       question from re-search is codified best practice in the most methodologically self-conscious
       evidence discipline there is.
    2. Elliott, J. et al., 2017. "Living systematic review: 1. Introduction — the why, what, when, and
       how." J Clin Epidemiol. — SECONDARY — "Knowing when to stop" is an explicit feature of the design
       and the stopping criteria must be stated *in the protocol*. Supports Limb A and constrains it:
       the stopping rule is pre-declared, not discovered at consultation time.
    3. Bastian, H. et al., 2019. "Enough evidence and other endings: a descriptive study of stable
       Cochrane systematic reviews in 2019." medRxiv 10.1101/19013912. — **VERIFIED** (retrieved full
       text; abstract and Conclusion read directly) — Conclusion, read in the source: reviews "were more
       likely to end because important future primary research activity was believed to be unlikely,
       than because there was enough evidence. Judgments about the strength of evidence and need for
       research were often inconsistent with the declaration that conclusions were unlikely to change."
       This is the single most important finding for this item and it cuts both ways: it confirms that
       organisations do close questions (Limb A), and it measures the closing judgment as *unreliable*
       — which is precisely the failure mode Limb B has no mechanism to catch.
       (The per-reason percentages circulating in search summaries — 18% "last search found nothing
       likely to change conclusions," 16% "research area no longer active," 7.5% superseded, 6.4%
       "evidence is conclusive," 6.2% intervention no longer in use — are SECONDARY; I read the
       abstract and conclusion in the retrieved text but did not locate these figures in the body, so
       they carry no weight in the rating.)
    4. Babić, A. et al., 2020. "How to decide whether a systematic review is stable and not in need of
       updating: Analysis of Cochrane reviews." Research Synthesis Methods 11(6) (doi 10.1002/jrsm.1451).
       — UNVERIFIED — Wiley returned an empty body on fetch and PubMed was CAPTCHA-blocked. The title
       states the item's exact question. Named here so a later run can retrieve it; no figure from it is
       used.
    5. Alchourrón, Gärdenfors & Makinson, 1985, and the AGM literature (survey material retrieved via
       arXiv:2104.14512, arXiv:0912.5511). — SECONDARY — Contraction is treated as the *more basic*
       operation than revision, since in contraction beliefs can only decrease. A belief set closed
       under consequence with expansion but no contraction has no revision operator at all. This is the
       formal statement of why Limb B is not merely risky but incoherent as a design — and PREMISE-174
       already carries it.
    6. Semantic-caching / memoization literature for LLM question answering (arXiv:2505.11271;
       arXiv:2603.26557). — SECONDARY — Reported savings: memoization cutting mean inference 19.11s →
       13.57s (29.0%); semantic cache reducing 903 inference calls to 527 (41.6%). Supports Limb A's
       efficiency claim by analogy and, more usefully, names the exact two-sided error: "a false hit can
       directly harm correctness (returning an answer for a different but similar-looking question),
       while a false miss loses potential savings." Every production cache design in this literature
       carries an invalidation/refresh path; none is write-once.

  Strength of support: Moderate (Limb A), None (Limb B)

  Summary: Limb A is well supported and should be conceded without reservation — the 82% pre-answered
    rate is a real saving, and evidence synthesis, belief revision and caching all independently license
    declining to re-open a settled question. Limb B has no support anywhere I searched. In living
    systematic reviews the retirement decision is explicitly reversible and the triggers are
    pre-declared; in AGM, contraction is the primitive and a contraction-free base cannot revise; in
    caching, invalidation is part of the design and false hits are the named correctness risk. The
    strongest finding is Bastian et al., which measured the *closing judgment itself* and found it
    frequently inconsistent with the evidence offered for it — meaning that an exemption granted at
    consultation time, with no re-entry, will inherit an error rate nobody is measuring. The pre-route
    grep 14a proposes is therefore defensible as a saving and indefensible as a terminal state; the
    literature says the grep should be paired with a declared re-exposure trigger, and that the trigger
    should be written into the protocol rather than discovered later.

  Caveats: Living systematic reviews retire *questions*, not *claims*, and they retire them with a named
    adjudicator and a public justification — neither of which the estate's register has. AGM is a
    normative logic of ideal agents and imposes no cost model, so it says nothing about whether the
    saving is worth taking. The caching analogy is the weakest of the three: a cache's contents are
    cheap to recompute and a premise's are not, which cuts in favour of caching premises harder, but
    also means a stale premise persists longer than a stale cache entry.

  Search scope: comprehensive — searched living systematic review retirement/stopping triggers, Cochrane
    review stabilisation and updating decisions, AGM contraction and monotonic belief base revision,
    answer-set-programming belief change, and semantic caching/memoization invalidation. Did not search
    truth-maintenance systems (de Kleer ATMS) or non-monotonic default logic, which would add formal
    depth but no new direction.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on the split: Limb A is SUPPORTED and
    the efficiency finding survives; Limb B is NO-SUPPORT-FOUND and is the limb that carries the High
    risk 14b assigned. Concretely, the literature answers OPEN-192 in a form neither option offered: do
    not choose between "exclude pre-answered items" and "search them anyway" — exclude them, and write
    the re-exposure trigger into the protocol at the same time. The in-house count 14b specifies (how
    many of 158 premises have ever changed status) remains the decisive measurement; note that
    PREMISE-184's affirmative-retraction clause is itself evidence that at least one status-movement
    mechanism was designed, so the count may not be zero.
