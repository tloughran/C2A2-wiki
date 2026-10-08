SEARCH-AGAINST-PRESUMPTION-865 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-865
  Original statement (per MONITOR-552): Reducing collection breadth is low-cost when the collected items
    are not being consumed.
  Owed this cycle: the RECOVERABILITY limb only — whether non-uniform coverage produced by an adaptive
    collection policy into a not-yet-consumed corpus is recoverable once consumption begins. Named
    venues: adaptive/sequential sampling bias and inverse-probability weighting (IPW), including
    positivity violations; systematic-review database-coverage bias; file-drawer of the never-searched.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Cycle-0 15a is known to me only via MONITOR-552's
    one-line summary (which names Halladay 2015 and Bramer 2017 as 15a's breadth-limb sources).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-865
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the asymmetry between the stated cost (queue depth) and the unstated cost
        (coverage).
      15b (2026-08-25): PARTIALLY-CHALLENGED (Moderate); NO targeted query executed (budget exhausted);
        one analogical SOC-alert-screening source inverting the cost ordering.
      15c: DISPOSITION-812 → MONITOR-552 (HIGH; narrowing decision live and irreversible).
      15d (2026-09-13): Re-triggered; owed = recoverability-limb literatures.
      15b (re-trigger cycle 1, 2026-10-08): 2 searches (IPW positivity; database-coverage bias); 1
        full-text fetch (Zhu/Mitra et al. 2021 positivity review). First targeted search on this item.
    Current status: CHALLENGED

  EVIDENCE GRADE: one full-text fetch (positivity review); two search-result-level empirical studies.
    Moderate scope on the IPW limb; preliminary on the systematic-review limb; the file-drawer-of-the-
    never-searched venue was NOT separately searched (folded into the coverage-bias query).

  Challenging evidence found: Yes (on recoverability-by-correction); Partial (on recoverability-by-
    back-fill)

  Sources:
    1. Zhu, Y., Hubbard, R. A., Chubak, J., Roy, J. & Mitra, N. 2021. "Core Concepts in
       Pharmacoepidemiology: Violations of the Positivity Assumption in the Causal Analysis of
       Observational Data: Consequences and Statistical Approaches." Pharmacoepidemiology and Drug
       Safety 30:1471ff. doi:10.1002/pds.5338, PMC8492528. [fetched — full text; author list beyond
       N. Mitra taken from background knowledge, page metadata showed Mitra only] Key passages:
       "Consider an example in which a subgroup ... never receives the treatment of interest. In such a
       subgroup, the treatment effect cannot be estimated directly because outcomes ... are never
       observed." Structural violations "occur when it is impossible for a subject to receive a certain
       treatment ... Increasing sample size does not ameliorate this problem." IPW weights there are
       "undefined because the denominator is 0 which results in an infinite weight." The available
       remedies (trimming, overlap/matching weights) "change the target of inference" to the overlap
       population; the alternative, extrapolation, "relies on extrapolation ... leading to possibly
       inaccurate and imprecise estimates if trends in nonoverlap regions are not well captured."
       Bearing: an adaptive policy that stops collecting a stratum creates, for that stratum, a
       selection probability of zero. That is a STRUCTURAL positivity violation. The statistics
       literature is unambiguous that it is not recoverable by reweighting what was collected; it is
       recoverable only by (a) redefining the question to exclude the stratum, (b) extrapolating on
       untestable assumptions, or (c) going back and collecting.
    2. Konno, K. & Pullin, A. S. 2020. "Assessing the risk of bias in choice of search sources for
       environmental meta-analyses." Research Synthesis Methods. [search-result — abstract-level via
       Bangor University repository listing; author names and venue from background knowledge, not
       verified on the page] 137 meta-analyses: single-platform and multi-platform restricted searches
       missed studies in 100 and 80 of them; missed studies produced larger, smaller, or
       opposite-direction effects; "the proportion of studies missed was positively related on a
       log-linear scale to the deviation of mean effect sizes"; restricted searches "are likely to lead
       to unrepresentative samples of studies and biased estimates." Bearing: direct empirical evidence
       that coverage narrowing produces bias that scales with what was missed, in the field closest to a
       literature-collecting system.
    3. Bramer, W. M. et al. 2017. "Optimal database combinations for literature searches in systematic
       reviews: a prospective exploratory study." Systematic Reviews 6:245, PMC5718002. [search-result]
       16% of included references were found in only ONE database; an estimated 60% of published
       reviews fail to retrieve 95% of relevant references. HONEST NOTE: 15a reportedly cited Bramer for
       the breadth limb; my reading of the same paper is that its unique-to-one-source figure is
       evidence that dropping a source loses items no other source recovers.
    COUNTER-EVIDENCE REPORTED FOR BALANCE: Cochrane-based analyses (incl. Halladay et al. 2015, as
       summarised in the search result) found point-estimate changes in 13/33 meta-analyses, mostly
       <20%, and "not ... in a systematic manner." So in well-indexed clinical literatures, restriction
       often costs precision rather than direction. This is a genuine boundary condition.

  Strength of challenge: Moderate-to-Strong (Strong on "recoverable by statistical correction";
    Moderate on "costly in practice", since the empirical evidence is field-dependent)

  Summary: The literature splits the recoverability question in two and answers each half against the
    presumption's cheap reading. Recovery by correction — reweighting the collected corpus at
    consumption time — is impossible for any stratum the adaptive policy stopped collecting: that is a
    structural positivity violation, and the causal-inference literature says more data of the same
    kind does not help and every workaround changes the question or extrapolates. Recovery by back-fill
    is possible only if the source still exists AND the consumer knows which strata are missing; an
    adaptive policy that stopped collecting a stratum has, by design, no observations telling it that
    the stratum later mattered. Empirically, restricted search coverage biases synthesis in proportion
    to what was missed in at least one large field (Konno & Pullin), though in Cochrane-indexed
    clinical literature the damage is usually small and non-directional.

  Specific risks: (i) narrowing becomes self-confirming — the strata dropped are never observed again, so
    no evidence ever arrives that they were valuable; (ii) consumption-time reweighting gives a false
    sense of repair (weights on the overlap region silently redefine the population); (iii) for
    time-bound sources (feeds, preprint versions, snapshots) back-fill may be impossible, making the
    loss permanent; (iv) the irreversibility flagged in MONITOR-552 is confirmed by theory.

  Mitigations available: keep a small non-zero exploration rate on every stratum (restores positivity,
    enabling IPW later — the standard bandit/surveillance remedy); log the policy's inclusion
    probabilities so consumption-time weighting is possible; maintain an explicit register of
    de-prioritised strata with date dropped; run MONITOR-552's back-fill experiment on one dropped
    stratum to measure what was lost.

  Recommendation: CHALLENGED — "recoverable once consumption begins" is false for zero-probability
    strata as a matter of established statistical theory; recoverable-by-back-fill survives only as a
    conditional (source persistent + missing strata known), which is itself a cost the presumption omits.

STEELMAN:
  Item: PRESUMPTION-865 (recoverability limb)
  Strongest counterargument: "Not yet consumed" sounds like "nothing lost yet," but the loss happens at
    collection, not at consumption. The moment an adaptive policy assigns a stratum zero collection
    probability, that stratum leaves the support of the data, and the causal-inference literature is
    explicit that no weighting of what remains can bring it back — more volume of the same kind does
    not help. The only remedy is to go back and collect, and the adaptive policy is the one component
    guaranteed not to know what to go back for, because it stopped looking precisely where it formed
    the belief that looking was not worth it. So the claimed low cost is the cost of a decision whose
    downside is invisible to the instrument that made it.
  What would need to be true for C2A2 to be safe: every de-prioritised stratum retains a non-zero
    collection probability; or the sources are persistent and the dropped strata are logged so a
    targeted back-fill is possible; and the corpus's eventual consumers do not need the dropped strata.
  How to test: pick one stratum dropped by the narrowing; back-fill it from source for the dropped
    window; measure how many back-filled items would have changed any downstream verdict.
