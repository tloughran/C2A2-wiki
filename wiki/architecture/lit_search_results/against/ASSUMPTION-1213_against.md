SEARCH-AGAINST-ASSUMPTION-1213:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1213
  Queue ref: LIT-QUEUE — 2026-08-25 (14a + 14b end-of-day intake cohort), Priority Medium
  Original statement: "the citation repairs cost +196 and +216 words, pushing both files past +25% on
    anchoring alone with no new argument added." — with the register's derived reading that the length
    clause "presumes length tracks argument size" while "three same-day counter-instances say it tracks
    citation density instead."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1213
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa commentary reviewer (Days 24 and 20) and corroborated against the
           QC sweep's Day 130 escalation. Two independent frames, same night, same conclusion —
           recorded as convergence, not as a single report. Marked CHALLENGED (of the length clause) on
           internal evidence, no literature consulted.
      15b: Searched for challenging literature. Four WebSearch queries covering document length as a
           quality/content proxy, the empirical relationship between article length and reference
           count, metric gaming and Goodhart effects under length targets, and the argumentation-theory
           status of citation as backing.
    Current status: PARTIALLY-CHALLENGED

  Search scope: Four WebSearch queries, executed 2026-08-26. Coverage reached: the bibliometric
    literature on article length and reference count (economics, medicine, ecology, general
    scientometrics); the readability and text-metrics literature on construct validity of
    length-derived proxies; the 2024–2026 LLM-evaluation literature on verbosity bias and
    length-controlled metrics; the Goodhart / metric-gaming literature including one recent formal
    treatment; and argumentation theory (Toulmin) on the status of backing. All sources read as
    search-result snippets only — **no full text or abstract was fetched**; all marked SNIPPET-ONLY.
    NOT COVERED, and each is a real limb of the queue's question: (a) the technical-writing and
    editorial literature on how word limits are actually administered when apparatus grows (style
    guides distinguishing body text from reference apparatus in word counts) — this is the direct
    practitioner answer to "how do length-control rules behave when growth comes from citation
    apparatus" and I did not reach it; (b) any empirical study of length-control rules specifically
    excluding or including citations, which is the exact question and which I could not find; (c) the
    legal-brief page-limit literature, where the question of whether citations count toward the limit
    has been litigated and formalised in court rules, and which is probably the single most relevant
    body of practice; (d) systematic-review reporting-length guidance (PRISMA and journal word caps).
    This search is adequate on the general construct-validity point and thin on the specific
    apparatus-versus-body question.

  Challenging evidence found: Partial

  Sources:
    1. Toulmin, S. 1958. "The Uses of Argument." [primary text not retrieved; framework summarised via
       multiple teaching sources, e.g. https://www.blinn.edu/writing-centers/wide/toulmin-argument.html
       and https://academics.umw.edu/speaking/resources/handouts/toulmin-argument-model/] — Directly
       challenges the assumption's load-bearing phrase, "with no new argument added." In the Toulmin
       scheme, *grounds* and *backing* are constituents of the argument, not ornament: backing is "the
       support, justification, and reasons that back up the warrant," and grounds are among the three
       *essential* components alongside claim and warrant. On this account a citation repair that
       replaces an unanchored assertion with an anchored one is not padding — it converts a claim into
       an argument. The +196 and +216 words are argument, newly present, in the standard analytic
       vocabulary for what an argument is made of. SNIPPET-ONLY, and note these are pedagogical
       summaries, not the primary text.
    2. [authors unverified] 2018. "Citations increase with manuscript length, author number, and
       references cited in ecology journals." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6093155/ —
       Reports that longer papers, papers with more authors, and papers citing more references are
       cited more, "and an increase in each independently predicts an increase in citations received."
       This bears on the assumption's implicit devaluation of anchoring-driven growth: in the one
       large-scale setting where the question has been studied, growth in citation apparatus is
       associated with *more* downstream impact, not with dilution. It does not show the apparatus is
       argument, but it does show it is not inert. SNIPPET-ONLY.
    3. [authors unverified] 2021. "Article length and citation outcomes." Scientometrics.
       https://link.springer.com/article/10.1007/s11192-021-04083-x ; and [authors unverified] 2012,
       "The Impact of Article Length on the Number of Future Citations: A Bibliometric Analysis of
       General Medicine Journals," PLOS ONE,
       https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0049476 — Together these
       supply the boundary condition rather than a refutation: "a 1% increase in page length is
       associated with a 0.56% increase in the number of citations" in economics journals, but "there
       is a relation between article length and impact at the shorter side of the length distribution
       [and] no significant relation was found for longer papers," and some studies find no
       relationship at all. So length is a weak and *regime-dependent* correlate of anything worth
       having, which cuts against the length clause but equally against any confident inference from a
       length ratio in either direction — including 14a's. SNIPPET-ONLY.
    4. [authors unverified] scientometric summary via
       https://arxiv.org/pdf/1804.10436 and related sources — Citation *density* (references per
       normalised page) "has remained fairly constant," meaning the absolute number of references, not
       their density, has grown historically. This is the closest thing I found to a base rate for the
       assumption's central claim. If density is normally near-constant across a literature, then a
       document whose density jumps sharply after repair is anomalous relative to the norm, which
       weakly supports the length clause's premise that density and length ordinarily move together —
       and therefore weakly challenges the claim that a length ratio "is not wrong" only because
       anchoring grew. SNIPPET-ONLY and this is my inference from a base rate, not a finding in the
       source; flagged as such.
    5. [authors unverified] 2026. "PRAIB: Peer Review AI Benchmark of Behaviour of LLM-Assisted
       Reviewing." arXiv:2605.29815. https://arxiv.org/pdf/2605.29815 ; and rubric-evaluation summary
       at https://medium.com/@adnanmasood/... [practitioner source, low grade] — Documents *verbosity
       bias*: judges "consistently give higher scores to longer outputs regardless of whether that extra
       length adds informational value, conflating word count with thoroughness." The recommended
       remedies are length-controlled metrics that "mathematically strip out the length advantage" or
       explicit concision criteria. Read against the assumption, this is a challenge to abandoning the
       length clause rather than to the clause itself: verbosity bias is exactly the failure a length
       cap exists to prevent, and the fact that repair-driven growth is a false positive for the cap
       does not mean the cap is protecting nothing. SNIPPET-ONLY.
    6. [authors unverified] 2022. "Challenges in Explanation Quality Evaluation." arXiv:2210.07126 ;
       and readability-corpus work at
       https://link.springer.com/article/10.3758/s13428-022-01802-x — The general construct-validity
       objection to length-derived proxies: traditional readability formulas "often lack strong
       construct validity since their features are solely based on statistical correlations rather than
       being theoretically oriented," and "many estimates of lexical diversity are not invariant as text
       length changes." SNIPPET-ONLY. Note: this source supports rather than challenges 14a. Recorded
       here for completeness and because it constrains what the *replacement* metric can be.
    7. [authors unverified] 2025. "Take Goodhart Seriously: Principled Limit on General-Purpose AI
       Optimization." arXiv:2510.02840. https://arxiv.org/pdf/2510.02840 ; and general treatments at
       https://www.keypup.io/blog/goodharts-law-in-action-why-your-dev-metrics-are-being-gamed-and-how-to-fix-it/
       — "When the proxy objective misspecifies the true goal and omits goal-relevant features,
       optimization pressures trade off arbitrarily large degradation of these unconstrained features
       for arbitrarily small gains in the proxy." Applied *against* the assumption's implied remedy:
       whatever replaces the word-count rule will be a proxy too, and if the replacement is citation
       density it will be gamed by adding citations, exactly as the current one is triggered by adding
       them. The challenge is that "the tier is not wrong" is not an argument for any particular
       successor metric. SNIPPET-ONLY.

  Strength of challenge: Moderate

  Summary: The literature does not defend word count as a measure of argument size — on that the
  assumption is on solid ground, and the construct-validity literature agrees with it. The challenges
  are three, and they are to the surrounding inferences rather than to the measurement. First and
  strongest: the phrase "with no new argument added" is contestable on the standard analysis of what an
  argument is. In the Toulmin scheme grounds and backing are constituents, so replacing an unanchored
  assertion with an anchored one adds argument in the only sense that has an established technical
  meaning. The +196 and +216 words may be exactly the thing the length budget exists to purchase.
  Second, the empirical relationship between length, references and value is real but weak and
  regime-dependent — 0.56% citations per 1% page length in economics, present at the short end and
  absent at the long end, absent entirely in some studies — which undercuts confident inference from
  length ratios in *either* direction, including the inference that a +25% overrun is benign because of
  its composition. Third, the Goodhart literature warns that the natural successor metric inherits the
  problem: a rule keyed to citation density is gamed by citations, and verbosity bias in LLM-produced
  and LLM-judged text is a documented failure that some length discipline exists to restrain. Rated
  Moderate: the assumption's diagnosis of the clause is not refuted, but its characterisation of the
  added words, and the implied remedy, both face substantive objections that the internal evidence
  cannot settle.

  Specific risks: (a) If anchoring text is argument, then the register has recorded three
  "counter-instances" that are not counter-instances but correct firings of a rule working as intended
  on files that genuinely grew — and the clause would be retired on the basis of its successes. (b) The
  verbosity-bias result means a system that generates and reviews its own prose has a documented drift
  toward length; removing the length discipline without a replacement removes the only restraint named
  in the record. (c) A successor metric keyed to citation density inherits Goodhart directly and would
  make the anchoring repair — currently the corpus's main quality intervention — the thing that trips
  the new rule. (d) The internal evidence base is three instances on three days from two frames, and
  while 14a is right to record it as convergence, both frames observed the same repair campaign, so the
  independence is of observers, not of the phenomenon. (e) Shares a failure mode with ASSUMPTION-1206
  and PRESUMPTION-877: a reliable automated proxy standing in for an unmeasured construct, with the
  proxy's vocabulary ("length ratio," "tier") the only vocabulary available for the discussion.

  Mitigations available:
    - Separate body text from citation apparatus in the count. This is the standard editorial and legal
      practice for exactly this problem and would resolve the observed instances without abandoning any
      discipline. I did not reach the literature that documents it and flag the recommendation as
      practitioner-standard-by-reputation rather than cited.
    - Report the ratio with its composition attached — words added as body, words added as anchoring —
      so that the length note carries the information needed to judge it. This is cheap and makes
      "repair-driven overrun" visible as a category rather than as an anomaly discovered per-instance.
    - Resist replacing one scalar with another. The Goodhart result argues for a *pair* of measures
      that trade against each other (length and anchoring density), not for a better single one.
    - Retain a concision criterion of some kind, given documented verbosity bias in generated and
      LLM-judged text (arXiv:2605.29815). The instances say the current rule mis-fires; nothing in the
      record says no rule is needed.
    - Before retiring the clause, count how often it has fired on *non*-repair growth. The register has
      226 length items and 205 carrying a length_note (per ASSUMPTION-1207); three repair-driven
      instances out of that population is a false-positive rate of ~1.5%, not a broken rule.

  STEELMAN:
    Item: ASSUMPTION-1213
    Strongest counterargument: The clause is not presuming that length tracks argument size. It is
    presuming that length tracks *reader cost*, which is a different construct and one for which word
    count is close to a direct measurement rather than a proxy at all. A commentary that grows 25%
    costs its reader 25% more time whether the growth is argument or apparatus, and a tier rule that
    caps growth is protecting the reader's budget, not adjudicating argumentative content. On that
    reading the three "counter-instances" are the rule working perfectly: it detected real growth,
    correctly, and the human judgement that the growth was worth it is exactly the judgement the flag
    exists to prompt. Furthermore, "no new argument added" is doing heavy work in the original sentence
    and it is the weakest link: on the standard analysis of argument structure, backing is argument, so
    the claim that 412 words of anchoring added nothing argumentative is not obviously true and was
    asserted, not shown. And the empirical literature that would license replacing length with citation
    density does not exist in usable form — the length/reference/impact relationships are weak, mixed
    in sign across studies, and regime-dependent.
    What would need to be true for C2A2 to be safe: (i) the tier rule's purpose must actually be
    argument-size control rather than reader-cost control — this is checkable in the rule's own
    definition and has not been checked in the record; (ii) if the rule is retired or amended, some
    restraint on generated verbosity must replace it, since verbosity bias is documented and the
    system both writes and reviews; (iii) the anchoring words must be genuinely non-argumentative,
    which requires inspecting them rather than classifying them by their origin in a repair; (iv) the
    three instances must not be a selected sample — they were surfaced *because* they overran, so they
    are conditioned on the outcome; (v) any successor metric must be paired rather than scalar, or the
    Goodhart failure recurs one level over.
    How to test: Two tests, both in-house. First, composition: for the two affected files, classify
    each of the +196 and +216 words as (a) reference apparatus — ids, paths, source lines; (b)
    connective prose asserting what the source supports; (c) new claim. Category (b) is backing and is
    argument on the standard analysis; if (b) is a large share, "no new argument added" is false as
    stated and the assumption needs restating. Second, base rate: over the 226 length items, count how
    many overruns are attributable to repair-driven anchoring growth versus other causes. If the share
    is small, the clause has a low false-positive rate and should be amended (exclude apparatus from the
    count) rather than doubted. Both tests use files already on disk and neither needs literature.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: ASSUMPTION-1213, ASSUMPTION-1206, PRESUMPTION-877
    Common vulnerability: **Construct-validity failure in automated proxies — a cheap, perfectly
    reliable measure reported under the name of the construct it was standing in for, with the proxy's
    vocabulary crowding out any term for what it misses.** Here: words counted, argument size reported.
    In 1206/877: ids resolved, citation health reported. The register's available terms — "length
    ratio," "tier," "dead citation" — are all proxy-shaped, so the constructs they miss cannot be named
    or trended. The Goodhart literature gives the general form: optimisation of, and reporting on, a
    compressed measure discards the goal-relevant features the compression omits (arXiv:2510.02840),
    and the LLM-evaluation literature gives the specific instance in verbosity bias, where length is
    substituted for thoroughness by judges (arXiv:2605.29815).
    Literature basis: arXiv:2510.02840; arXiv:2605.29815; arXiv:2210.07126 and
    link.springer.com/article/10.3758/s13428-022-01802-x (construct validity of length-derived
    features); PMC12285159 and arXiv:2511.16198 for the citation limb.
    Risk level: High
    Recommendation: Require every automated figure promoted to a register headline to carry a named
    statement of what it cannot measure, and prefer paired measures to scalar ones when replacing a
    proxy that has been shown to mis-fire.

  Recommendation: CHALLENGED
