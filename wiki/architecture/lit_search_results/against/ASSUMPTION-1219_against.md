SEARCH-AGAINST-ASSUMPTION-1219:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1219
  Queue ref: LIT-QUEUE — 2026-08-25 (14a + 14b end-of-day intake cohort), Priority High
  Original statement: "Every Summa repair today lowered confidence. Four repairs, four downward.
    Combined with yesterday's two-corrected-downward result, that's six consecutive corrections that
    made the wiki claim *less*. That is either the system working exactly as designed, or a sign the
    original synthesis pass was systematically over-confident — and which of those it is bears directly
    on OPEN-165."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1219
    Item type: ASSUMPTION (stated — quoted)
    Transform at each step:
      14a: Extracted verbatim from the evening summary ("For Morning Discussion") and deliberately left
           as a two-member disjunction, passing the exhaustiveness question to 14b rather than resolving
           it here. Recorded status: UNTESTED; whether the disjunction exhausts the space is filed as
           PRESUMPTION-880.
      15b: Searched for challenging literature. Four WebSearch queries covering intrinsic
           self-correction in language models, critic-induced confidence change, asymmetric error costs
           and conservatism in revision, and directional bias in post-hoc review.
    Current status: CHALLENGED

  Search scope: Four WebSearch queries, executed 2026-08-26. Coverage reached: the 2023–2026 literature
    on LLM self-correction and self-critique, including the canonical negative result and one paper on
    asymmetric response to opposing versus supportive advice; the sycophancy literature; and, weakly,
    the decision-theory literature on asymmetric error costs. All sources read as search-result
    snippets only — **no full text or abstract was fetched** — so all are SNIPPET-ONLY, and the one
    quantitative figure I report (69.6%) is as rendered by the search engine, not verified in the
    paper. NOT COVERED, and these are real gaps: (a) the psychometric literature on regression to the
    mean in repeated ratings, which is the null explanation for any monotone short series and which I
    did not search — this is the most important omission and I flag it as such rather than let the
    steelman carry it alone; (b) base rates for upward versus downward revision in human post-hoc
    review of scholarly text, which is the queue's second explicit limb and which I did not find any
    measurement of; (c) the peer-review literature on reviewer severity drift; (d) the small-sample
    statistics of run length — the probability of six same-direction outcomes under a fair coin is
    2×(1/2)^6 ≈ 3.1%, which is suggestive but not significant at conventional thresholds and which no
    source is needed to compute. The challenge below is strong on the mechanism limb and absent on the
    base-rate limb.

  Challenging evidence found: Yes

  Sources:
    1. Huang, J., Chen, X., et al. [remaining authors unverified] 2023/2024. "Large Language Models
       Cannot Self-Correct Reasoning Yet." arXiv:2310.01798, ICLR 2024.
       https://arxiv.org/abs/2310.01798 — The decisive source, and it supplies a *third* member the
       disjunction omits. Intrinsic self-correction — a model reviewing and revising its own answer
       with no external ground-truth signal — "consistently degrades performance," with models
       "changing correct answers to wrong ones more often than [they] fixed errors." The methodological
       finding is equally sharp: prior papers reporting gains "used oracle labels to decide when to
       stop correcting, meaning the model only corrects already-wrong answers — which is not
       self-correction but oracle-guided filtering." C2A2's repair loop has no oracle and no
       adjudicator; it is the regime the paper studies, not the one that works. SNIPPET-ONLY.
    2. Follow-on analysis reported alongside source 1 [paper and authors unverified; figure as rendered
       by search] — "For initially correct answers that become incorrect, the main cause is false
       problem identification (69.6%), where the model incorrectly critiques a correct original answer
       and revises it into a wrong one." This is the third disjunct stated precisely: the corrections
       may be neither correct-by-design nor evidence of original over-confidence, but artefacts of a
       reviewer that finds problems because it was asked to look for them. Given that every one of six
       corrections went the same way, a mechanism that produces spurious critiques at ~70% of its
       error-inducing volume is a live rival explanation. SNIPPET-ONLY, and the figure is
       second-hand — do not quote it as verified.
    3. [authors unverified] 2025. "How Overconfidence in Initial Choices and Underconfidence Under
       Criticism Modulate Change of Mind in Large Language Models." arXiv:2507.03120.
       https://arxiv.org/pdf/2507.03120 — Names the directional asymmetry the item is observing.
       Models "overweight opposing rather than supportive advice, showing strikingly asymmetric
       sensitivity to opposing and supportive advice — with overweighting of the former but not the
       latter," and "when faced with disagreement... experience a steep drop in confidence and often
       flip their position entirely, even when the criticism offered no actual evidence." A review
       process whose job is to find problems supplies opposing input by construction; if the responder
       is asymmetrically sensitive to opposing input, the correction series is *predicted* to be
       one-directional regardless of whether the original claims were over-confident. This is the
       single most direct challenge to the disjunction: it explains the observation without either
       member. SNIPPET-ONLY.
    4. [authors unverified] 2026. "Diagnosing and Mitigating Sycophancy and Skepticism in LLM Causal
       Judgment." arXiv:2601.08258. https://arxiv.org/html/2601.08258v3 — Adds the safety-tuning limb:
       "safety-tuned models reject valid causal links at alarming rates by sacrificing sensitivity,"
       and on ambiguous cases "larger models can regress by defaulting to paralysis rather than engaging
       the reasoning they demonstrably possess." Lowering a confidence claim is the cheap, safe move for
       a tuned model; a hedging gradient built into the reviewer would produce exactly six downward
       corrections in six. SNIPPET-ONLY.
    5. Sycophancy literature generally — e.g. https://arxiv.org/pdf/2412.00967 ("Linear Probe Penalties
       Reduce LLM Sycophancy") and summary at
       https://pacific.ai/detecting-and-evaluating-sycophancy-bias-an-analysis-of-llm-and-ai-solutions/
       — RLHF "may encourage models to be overly deferential to the preferences or advice of another
       user or agent." In a self-review pipeline the reviewer's implicit prompt-level expectation is
       that corrections will be found; deference to that expectation is a bias with a name and a
       measurement literature. SNIPPET-ONLY; the second source is a vendor page and is low grade.
    6. Asymmetric error costs — [authors unverified] "The evolution of distorted beliefs vs. mistaken
       choices under asymmetric error costs," Evolutionary Human Sciences,
       https://www.cambridge.org/core/journals/evolutionary-human-sciences/article/evolution-of-distorted-beliefs-vs-mistaken-choices-under-asymmetric-error-costs/90C8F91087E13A7ED903FB734252E43F
       ; and https://pmc.ncbi.nlm.nih.gov/articles/PMC9432742/ on error management in collective
       decision-making — The general result: "contemporary cost asymmetries affect choices by
       increasing the rate of cheap errors to reduce the rate of expensive errors," and agents "evolved
       a bias towards the signal decision boundary avoiding the costly error." Applied here: in a wiki
       whose reputational exposure is asymmetric — over-claiming is embarrassing, under-claiming is
       invisible — a rational reviewer will systematically shade downward, and the resulting monotone
       series is a property of the *cost structure*, not of the original claims. This is a fourth
       explanation, and it is not a bias in the pejorative sense; it may be correct behaviour producing
       an uninformative signal. SNIPPET-ONLY; the transfer from evolutionary models to this setting is
       my inference, not the sources'.

  Strength of challenge: Strong

  Summary: The challenge here is not to either member of the disjunction but to its exhaustiveness, and
  the literature supplies at least three further members with more empirical support than either of the
  two named. First and most damaging: intrinsic self-correction without an external ground-truth signal
  is a documented *degrader* — models change correct answers to wrong ones more often than they fix
  errors, and the dominant cause is false problem identification, i.e. critiquing a correct original.
  The papers that reported self-correction gains did so by using oracle labels, which the C2A2 pipeline
  does not have. Second, models are asymmetrically sensitive to opposing versus supportive input and
  drop confidence sharply under criticism "even when the criticism offered no actual evidence"; a
  process constituted to look for problems supplies criticism by construction, so a monotone downward
  series is what the setup predicts irrespective of the originals' quality. Third, the cost structure
  is asymmetric — over-claiming is visible and under-claiming is not — and the error-management
  literature says agents facing asymmetric costs shade toward the cheap error. Any of these three
  produces "six consecutive corrections that made the wiki claim less" with no over-confidence in the
  original pass and no system working as designed. Note also, and no source is required: under a fair
  coin, six same-direction outcomes has probability ~3.1% two-sided, which is interesting but not
  decisive, and n=6 with a single reviewer cannot separate these hypotheses at all. Rated Strong
  because the omitted explanations are better evidenced than the included ones and because the
  register's own downstream question — OPEN-165 — is answered differently under each.

  Specific risks: (a) The disjunction, as posed, forces a choice between two options where the true
  answer may be a third, and the register's note says this "bears directly on OPEN-165" — so a live
  decision may be taken on a false dichotomy. (b) If the corrections are artefacts of critic bias, then
  six wiki claims have been *degraded*, not improved, and the repair channel is subtracting accuracy
  while logging quality work; this is the worst case and it is consistent with all observed data. (c)
  The direction of the danger is inverted relative to the register's framing: 14a's second disjunct
  worries that the originals were over-confident, but the self-correction literature's concern is that
  the *corrections* are wrong, which no member of the disjunction contemplates. (d) A hedging gradient
  compounds: each pass that lowers confidence provides the next pass with a weaker claim to weaken
  further, and nothing in the loop can push a claim back up, so the corpus drifts monotonically toward
  vacuity at a rate set by review frequency. (e) The evidential base is six corrections by, as far as
  the record shows, a single reviewer with no adjudicator — which is the exact configuration
  PRESUMPTION-880 names and which the literature says is the configuration in which self-correction
  fails. (f) The register cannot currently distinguish "correction" from "confidence reduction," so a
  downward move is recorded as a repair by definition.

  Mitigations available:
    - Introduce an oracle or an adjudicator, even a weak one. The self-correction literature's single
      clearest finding is that the failure is specific to the no-external-signal regime; any
      independent check restores the gains that the oracle-labelled papers reported.
    - Re-review a blind sample of the six by a reader who did not make them and who is not told the
      direction of the original correction. This is what 14a already listed under Testability and it is
      the right test; the addition from the literature is that the re-reviewer must be blind to the
      correction's direction, or the same asymmetric-criticism effect operates on them.
    - Record the *counterfactual*: for each repair, log whether the reviewer considered raising
      confidence and rejected it. A process that never generates the upward hypothesis cannot produce
      an upward correction, and the absence would be visible immediately.
    - Track direction as a metric with an expected distribution, not as an anecdote. Six of six is not
      significant; sixty of sixty would be. The register should carry the running count so the question
      becomes answerable rather than recurrent.
    - Separate "correction" from "hedging" in the taxonomy. If confidence-lowering is the only move the
      pipeline can log as a repair, the direction of the series is a definitional artefact.
    - Note the asymmetric-cost point is not a bias to be eliminated: shading downward may be the
      correct policy given the corpus's exposure. But if it is policy, it should be stated as policy,
      and then the series carries no evidence about the original pass at all.

  STEELMAN:
    Item: ASSUMPTION-1219
    Strongest counterargument: The self-correction literature is about *reasoning benchmarks with
    ground truth* — arithmetic and multi-step QA, where a correct answer exists and a model talks
    itself out of it. C2A2's Summa repairs are not that. They are corrections to *confidence
    qualifiers* on interpretive syntheses, where lowering a claim from "shows" to "suggests" is not a
    flip from correct to incorrect but a calibration move, and where the reviewer often has evidence
    the original pass did not — specifically, it has read the cited record. Four of the six corrections
    on the day in question sit in a repair campaign that was *also* finding real citation defects, so
    there is a plain mechanism by which downward moves are warranted: the anchor turned out to be
    thinner than the claim built on it. Under that reading, "the system working exactly as designed" is
    not one of two guesses but the observed process, and the disjunction's second member covers the
    remaining possibility perfectly well. Adding critic-bias as a third member risks the opposite
    error — explaining away a real signal that the synthesis pass over-claims, which is the finding
    with actual consequences for OPEN-165.
    What would need to be true for C2A2 to be safe: (i) each downward correction must be traceable to
    specific new evidence the original pass lacked — if the reviewer's stated reason is evidential in
    every case, the critic-bias explanation loses most of its force, and this is checkable in the six
    transcripts today; (ii) the reviewer must have been capable of moving a claim *upward* — the
    process must admit that move, and someone must have exercised it at least once, ever; (iii) the
    corrections must not be confidence-qualifier changes only, since a series of hedges is exactly what
    the sycophancy and safety-tuning results predict and carries no information about the originals;
    (iv) the sample must not be selected — if repairs are triggered by suspicion of over-claiming, then
    conditioning on "a repair happened" guarantees downward direction and the observation is
    tautological; this is the most likely explanation of all and neither the item nor my search
    addresses it; (v) a blind re-reviewer must agree with the direction more often than chance.
    How to test: 14a's own proposal is correct and needs one addition. Take the six corrections. Present
    a reader who did not make them with the *original* claim and the *corrected* claim, unlabelled and
    in randomised order, plus the cited record, and ask which better fits the evidence. Blindness to
    which is the correction is essential — otherwise the re-reviewer inherits the same asymmetric
    sensitivity to the "opposing" version. Then, separately and more cheaply: count how many repairs in
    the entire register's history moved a claim upward. If the answer is zero over a long history, the
    channel is directional by construction and the disjunction is moot, because a process that can only
    subtract will produce a monotone series whatever the truth is. That count can be run today.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: ASSUMPTION-1219, ASSUMPTION-1218, ASSUMPTION-1221
    Common vulnerability: **All three depend on an adjudicator who is absent, and each substitutes an
    act of signalling for an act of resolution.** 1219's disjunction cannot be settled without an
    independent reviewer, and the self-correction literature says the no-adjudicator regime is
    precisely the one in which review degrades rather than improves accuracy — so the corrections
    proceed and are logged as repairs while unadjudicated. 1218 escalates to a party absent for
    fifty-plus days and treats the escalation as terminal. 1221 discloses a rule breach and continues,
    treating disclosure as discharging the rule, where the party who could rule on "raise the budget,
    lower the cap, or lower the standard" is the same absent party. The literature says this
    substitution is not neutral: self-correction without an oracle degrades (arXiv:2310.01798);
    disclosure without adjudication produces moral licensing and *more* biased behaviour, not less
    (Cain, Loewenstein & Moore); and unanswered escalation is the structure of failure to rescue rather
    than a remedy for it.
    Literature basis: arXiv:2310.01798 (Huang, Chen et al.); arXiv:2507.03120;
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=480121 (Cain, Loewenstein & Moore);
    https://pubmed.ncbi.nlm.nih.gov/24768480/ and https://pubmed.ncbi.nlm.nih.gov/25794627/
    (failure to rescue); normalisation-of-deviance literature [Vaughan attribution not verified in this
    search].
    Risk level: High
    Recommendation: Measure the adjudicator channel as a first-class system property — answer rate and
    silence duration — and define what each agent may do unilaterally when it is dead. Until then,
    "escalated," "disclosed" and "self-corrected" should be recorded as *pending*, not complete. For
    this item specifically: no unadjudicated correction series should be read as evidence about the
    quality of the original pass.

  Recommendation: CHALLENGED
