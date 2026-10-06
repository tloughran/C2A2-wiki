SEARCH-AGAINST-PRESUMPTION-004:
  Date searched: 2026-09-04
  Original item: PRESUMPTION-004 (MONITOR-009)
  Original statement: "2/3 threshold optimal" - a 2-of-3 agreement threshold is the right decision
    rule for the system's tripled-agent checks. This cycle's focus: the CONTEXT question -
    context-specific error costs, and comparison of thresholds across decision contexts.
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15b (cycle 5)]
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Inferred from the system's use of a fixed 2-of-3 rule across tripled checks without a
           stated justification for the fraction or its uniformity.
      15b: Searched for challenging literature (cycle 5 re-check), scoped to CONTEXT-INVARIANCE
           rather than ensemble independence, which ASSUMPTION-008 already dispositioned REVISE on
           2026-09-02 (REVISE-426). This scoping was instructed, to avoid re-deriving REVISE-426.
    Current status: CHALLENGED

  Queries run this cycle:
    1. "correlated errors Condorcet jury theorem dependence voters fails majority rule"
    2. "optimal voting threshold asymmetric error costs decision context safety-critical"
    3. "LLM multi-agent majority voting consensus collapse sycophancy 2026"
    4. "common cause failure N-version programming triple modular redundancy independence assumption violated"
    5. "'Nine Judges, Two Effective Votes' correlated errors LLM evaluation panels"
    6. "optimal decision threshold depends on prevalence base rate not transferable across contexts recalibration"
    7. "adaptive self-consistency sampling budget task difficulty fixed number samples suboptimal LLM"
    8. "risk-tiered human oversight escalation policy AI agents one-size-fits-all threshold inappropriate"
    9. "Neyman-Pearson classification asymmetric error control type I error priority threshold selection"
   10. "'Blind to the Pivotal Vote' aggregate independence metrics verification"

  Challenging evidence found: Yes

  Sources:
    1. Shu, Y. 2026. "Blind to the Pivotal Vote: Aggregate Independence Metrics Miss Where
       Verification Actually Helps." arXiv:2608.06940 (Zhejiang University, August 2026).
       [VERIFIED BY 15c 2026-09-04 - author, affiliation, month and both figures confirmed.]
       - Directly on the context question. The entire accuracy benefit of an additional evidence
       source concentrates on PIVOTAL decisions (one-vote margin): +10.4 to +23.3pp there and
       "exactly zero" elsewhere. A single fixed threshold applied uniformly is therefore mispriced.
       Also reports that an independent verification signal (test-suite execution) produced no
       measurable change in effective-vote count at scale (-0.04, 95% CI [-0.10, +0.02]).
    2. Kohli, G. 2026. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation
       Panels." arXiv:2605.29800 (search results date it 2026-05-28). - Nine frontier judges across
       seven model families supply approximately two independent votes' worth of information; panel
       accuracy falls 8-22pp short of independent voting and the best single judge matches the
       panel. Already cited in REVISE-426; carried here for the fraction-is-meaningless implication.
    3. Neyman-Pearson classification literature (Tong 2016, WIREs Computational Statistics survey;
       Tong et al., Science Advances, "Neyman-Pearson classification algorithms and NP receiver
       operating characteristics"). - When Type I and Type II errors carry different costs, the
       correct rule is set by a user-specified alpha; the oracle threshold is determined by the
       error-cost priority, not by a universal fraction.
    4. Cost-sensitive threshold literature via arXiv:2601.04486 ("Decision-Aware Trust Signal
       Alignment for SOC Alert Triage") and arXiv:2604.27282 ("The Likelihood Ratio Wall"). -
       Closed form t* = C_FP/(C_FP + C_FN); cost-blind threshold choice is "arbitrarily suboptimal
       as cost asymmetry increases." A constant 2/3 is Bayes-optimal only under one specific and
       unstated cost/base-rate configuration.
    5. Ladha, K. "Information pooling through majority-rule voting: Condorcet's jury theorem with
       correlated votes," JEBO (ScienceDirect 016726819400068P); Boland, "Condorcet's jury theorem,
       dependency among jurors," Social Choice and Welfare (Springer BF00187435); Bottcher &
       Kernell 2022, "Examining the limits of the Condorcet Jury Theorem," SAGE
       10.1177/26339137221133401. - Positive correlation among voters degrades majority-rule
       competence and can reverse the Condorcet effect; monotonicity in voter count is not
       guaranteed under strong pairwise dependency.
    6. Aggarwal et al. 2023. "Let's Sample Step by Step: Adaptive-Consistency for Efficient
       Reasoning and Coding with LLMs." EMNLP 2023 (2023.emnlp-main.761; arXiv:2305.11860). Plus
       arXiv:2601.02970 and arXiv:2608.24590. - A FIXED agreement/sample regime is dominated by an
       instance-adaptive one: up to 7.9x budget reduction at <0.1% accuracy cost. The fixed rule is
       not optimal even holding the task family constant.
    7. arXiv:2604.17139 ("The Consensus Trap"); arXiv:2606.29270 ("Minority Sentinel");
       arXiv:2605.00914 ("The Cost of Consensus"). - Majority-vote failure on ~24% of disputed
       questions; ~23.9% of initially-disagreed questions converging to UNANIMOUS WRONG consensus by
       round three; sycophantic conformity up to 85.5%; consensus collapse with oracle gaps up to
       32.3pp. Unanimity does not rescue the rule here - it is the failure mode.
    8. arXiv:1801.06897, "The Optimal Majority Threshold as a Function of the Variation Coefficient
       of the Environment"; arXiv:1901.09233, "Optimal majority threshold in a stochastic
       environment." - Titles/abstracts encountered this run establish that the optimal majority
       threshold is an explicit FUNCTION of environmental parameters. Full texts not read.
    9. Risk-tiered oversight literature: arXiv:2506.12482 ("Tiered Agentic Oversight");
       arXiv:2606.22484 ("Governed AI-Assisted Engineering: Graduated Human Oversight"); plus vendor
       frameworks (Galileo, Arthur, MintMCP, MindStudio) treated as direction, not evidence. -
       Converges on the claim that uniform gates are wrong; oversight intensity should scale with
       reversibility and impact.
   10. NSF-SHREC / IEEE, "Modeling Common Cause Failures in Systems with Triple Modular Redundancy
       and Repair" (IEEE Xplore 9153662). - Common-cause failure caps TMR's reliability gain at
       ~51x versus simplex in the worked example. The TMR literature's own remedy is PLATFORM
       DIVERSITY, not threshold tuning - an argument that the fraction is the wrong control
       variable altogether.

  NEW SINCE LAST CYCLE: arXiv:2608.06940 (Aug 2026) is the single most decision-relevant new result
    and did not exist in April; it is the first source found that empirically localises WHERE an
    extra vote helps, which is exactly the CONTEXT question. arXiv:2606.29270, arXiv:2608.24590 and
    arXiv:2606.20158 also postdate April. arXiv:2605.29800 and arXiv:2605.00914 are May 2026. The
    Condorcet-dependency, Neyman-Pearson and TMR/CCF material is long-standing and was searched to
    establish that the classical result is unchanged, which it is.

  Strength of challenge: Strong (on the context-invariance question specifically)

  Summary: The literature is close to unanimous that an optimal agreement/decision threshold is a
    function of error costs, base rate and instance difficulty - never a constant. The
    Neyman-Pearson framework and the cost-sensitive form t* = C_FP/(C_FP + C_FN) make this analytic
    rather than empirical: a single fraction can be optimal for at most one cost/prevalence
    configuration, so applying 2/3 to both a safety-critical gate and an exploratory scan is optimal
    for at most one of them. The strongest new evidence, arXiv:2608.06940, shows the marginal value
    of an additional vote is zero except on one-vote-margin decisions and large there. Adaptive
    consistency results show fixed regimes are dominated by instance-adaptive ones even within a
    single task family. Nothing found argues a fixed fraction is context-robust.

  Specific risks: C2A2 is systematically over-gating cheap reversible decisions (throughput cost
    plus approval habituation downstream) and simultaneously under-gating irreversible or
    safety-critical ones, where the correct rule is probably unanimity or a 1-of-3 VETO rather than
    2-of-3 concurrence. Worse, because 2-of-3 among correlated same-model instances is close to
    1-of-1 with extra steps, the system may be recording "checked" for decisions that received no
    real independent check. The failure is silent: agreement rates stay high and look like
    confirmation.

  Mitigations available:
    (a) Replace the single fraction with a two-parameter rule per decision class - a concurrence
        threshold and a veto threshold, e.g. safety-critical = 3/3 concurrence with 1/3 veto;
        exploratory = 1/3 sufficient to proceed. With N=3 the admissible thresholds are only
        {1/3, 2/3, 3/3}, so this is a three-way choice, not a tuning problem.
    (b) Log disagreement margin on every tripled check and report accuracy conditional on
        disagreement, per the explicit recommendation in arXiv:2608.06940.
    (c) Adaptive escalation: spend a 4th/5th check only when the first three split.
    (d) Force genuine diversity (different base model, different scaffold, or a tool-grounded
        check) rather than tuning the fraction.

  STEELMAN:
    Strongest counterargument: With N=3 the threshold space is discrete and tiny - {1/3, 2/3, 3/3} -
      so "optimal" is a coarse claim, and 2/3 is the unique choice that is neither trivially
      permissive nor requires perfect agreement, which is a defensible default under uncertainty
      about the cost ratio. The cost-sensitive t* is a PROBABILITY threshold on a calibrated score,
      not a vote fraction, so mapping it onto 2-of-3 is an analogy rather than a theorem.
      Furthermore, if the three agents are highly correlated then 1/3, 2/3 and 3/3 all behave nearly
      identically and the choice of fraction is close to irrelevant - which paradoxically makes 2/3
      "not wrong." Finally, arXiv:2606.20158 ("N-Version Programming with Coding Agents") indicates
      N-version units can still improve reliability under fault correlation, so partial dependence
      does not void the scheme.
    What would need to be true for C2A2 to be safe: (i) the error-cost ratio C_FP/C_FN is roughly
      similar across all decision types the tripled check is applied to - i.e. C2A2 is not in fact
      mixing safety-critical with exploratory under one gate; (ii) the disagreement rate is high
      enough that the choice among {1/3, 2/3, 3/3} changes outcomes on a non-trivial fraction of
      decisions; and (iii) the tripled agents are diverse enough that a 2-1 split is informative
      rather than noise.
    How to test: Cheap and decisive. Instrument every tripled check to record the raw 3-vote tally
      (not just pass/fail), the decision class, and - where ground truth later exists - correctness.
      Then compute (1) the empirical distribution of 3-0 / 2-1 / 1-2 / 0-3 splits per decision
      class; if >90% are unanimous, the threshold is near-inert and this item is low-priority
      regardless of theory. (2) Accuracy conditional on a 2-1 split, per class. (3) For any class
      where 2-1 splits are common AND conditional accuracy on 2-1 splits is near chance, the 2/3
      rule is provably not doing work there. Logging changes only; no new agents.

  15c NOTE APPENDED 2026-09-04: condition (ii) of the steelman was answered by 15c's own
    verification of arXiv:2606.29270, which 15a had cited in the opposite direction. That paper
    reports 39.1% of samples exhibiting 2:1 splits, with the minority correct in 25.5% of them. The
    disagreement rate is NOT low, so the threshold is not near-inert, and the steelman's most
    plausible escape route is closed by measurement rather than by argument. See DISPOSITION-893.

  Recommendation: CHALLENGED
