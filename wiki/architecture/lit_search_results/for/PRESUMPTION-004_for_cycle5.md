SEARCH-FOR-PRESUMPTION-004:
  Date searched: 2026-09-04
  Original item: PRESUMPTION-004 (MONITOR-009)
  Original statement: "2/3 threshold optimal" - a 2-of-3 agreement threshold is the right decision
    rule for the system's tripled-agent checks. Cycle-5 sub-question, taken from MONITOR-009's
    "what would change disposition": is a SINGLE FIXED threshold appropriate across heterogeneous
    decision types (safety-critical vs. exploratory)?
  Cycle: monthly re-check cycle 5 (15d re-trigger of 2026-07-05)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (cycle 5)]
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Inferred from the system's use of tripled-agent checks that a 2-of-3 rule was being
           treated as optimal without that optimality ever being argued.
      15a: Searched for supporting literature (cycle 5 re-check)
    Current status: PARTIALLY-SUPPORTED

  Queries run this cycle:
    1. "May's theorem majority rule optimal decision rule axiomatic characterization"
    2. "triple modular redundancy 2-of-3 voting safety-critical systems reliability optimal"
    3. "cost-sensitive threshold selection ROC decision threshold depends on misclassification costs"
    4. "Condorcet jury theorem optimal majority threshold competence heterogeneous"
    5. "IEC 61508 voting architecture 1oo2 2oo3 selection safety integrity level trade-off spurious trip"
    6. "ensemble majority voting optimality Bayes decision rule weighted voting versus simple majority classifiers"
    7. "signal detection theory optimal decision criterion depends on prior probability and payoff matrix"
    8. "LLM multi-agent majority voting agreement threshold verification 2026 how many agents optimal"
    9. "uniform decision threshold across decision types justification robustness simple rules ecological rationality"
   10. "majority rule robust default aggregation rule when competences unknown no calibration data"
   11. "2-of-3 agreement rule verification LLM outputs false positive false negative cost asymmetry safety critical"

  Supporting evidence found: Partial

  Sources:
    1. May's theorem, via en.wikipedia.org/wiki/May's_theorem and the extension paper "An extension
       and an alternative characterization of May's theorem," Annals of Operations Research
       (link.springer.com/article/10.1007/s10479-021-03999-0). - Majority rule is the UNIQUE binary
       social choice function satisfying anonymity, neutrality, positive responsiveness and
       decisiveness. At n=3, 2-of-3 IS simple majority, so this is a genuine uniqueness result for
       the rule in use. NOTE: the primary 1952 Econometrica paper was NOT opened this run; the
       axiom list comes from the secondary sources named.
    2. Fey, M. "A Note on the Condorcet Jury Theorem with Supermajority Voting Rules."
       (PDF at rochester.edu/college/faculty/markfey/papers/FeySCWFinal.pdf. Filename suggests
       Social Choice and Welfare; volume/year/DOI NOT VERIFIED this run - do not cite with a year.)
       - A group seeking correct collective decisions is better off with simple majority than with a
       raised supermajority fraction. Direct support against raising the threshold above 2-of-3.
    3. "A Comprehensive Survey of Redundancy Systems with a Focus on Triple Modular Redundancy
       (TMR)." arXiv:2603.14411. - Surfaced this run. Establishes TMR/2oo3 as the standard
       fault-masking architecture; the reliability identity R = 3R_M^2 - 2R_M^3 (corroborated in
       nature.com/articles/s41598-023-41363-3) means 2-of-3 strictly improves on a single channel
       whenever per-module reliability exceeds 0.5.
    4. He, C., Chen, Z., Yang, Z., Qiao, S., Ju, M., Liu, J., Wen, D. & Liu, G. 2026.
       "Minority Sentinel: When to Overturn Majority Voting in Multi-Agent LLM Debates."
       arXiv:2606.29270 (AgentSearch Workshop @ SIGIR 2026).
       *** 15a's reading of this paper was CHECKED BY 15c ON 2026-09-04 AND DOES NOT HOLD. ***
       15a cited it as reporting that stricter-than-majority thresholds give no accuracy benefit
       and that gains are stable across a wide band tau in [0.61, 0.95], and treated the width of
       that band as the strongest available support for context-invariance. That band is the
       operating range of the paper's LightGBM meta-classifier's FLIP threshold, not a vote
       threshold. The paper's headline result runs the other way: 39.1% of samples exhibit 2:1
       splits and in 25.5% of those the MINORITY is correct, a 10.0pp recovery margin that majority
       voting forfeits; its stated thesis is a shift from "counting heads" to "auditing evidence."
       This citation is retained in the record with its correction rather than deleted.
    5. "Collective decision efficiency and optimal voting mechanisms: A comprehensive overview for
       multi-classifier models." arXiv:1502.02191. - Majority rule coincides with the Bayes
       classifier under equiprobable classes and equal, independent competences.
    6. Preprint on LLM output verification (preprints.org manuscript
       004bea68f2366c15c5d1445daccf85ca). AUTHOR AND TITLE NOT VERIFIABLE from search results;
       recorded as unrefereed and given no weight.

  NEW SINCE LAST CYCLE: arXiv:2606.29270 (June 2026) and arXiv:2603.14411 (March 2026) postdate an
    April-2026 baseline. Everything else (May, Condorcet, TMR, SDT) was available in April. After
    15c's verification, the only genuinely new SUPPORTIVE material is the TMR survey, which speaks
    to the fraction and not to context-invariance.

  Strength of support: Moderate for "2-of-3 is a reasonable robust default";
                       None for "one fixed threshold is optimal across decision types".

  Summary: The half of this presumption nobody disputes is well supported. May's theorem gives
    majority rule a uniqueness characterisation on binary choices; the TMR reliability identity
    shows 2oo3 dominates a single channel for any module better than a coin flip; supermajority
    analysis says raising the fraction hurts rather than helps correctness. The half cycle 5
    actually asked about - whether ONE threshold can serve heterogeneous decision types - is not
    supported, and the literature encountered points the other way. Signal detection theory gives
    an explicit optimum that is a function of prior odds and the payoff matrix; cost-sensitive
    thresholding is an entire subfield premised on the threshold moving with misclassification
    costs; and IEC 61508 practice deliberately selects DIFFERENT voting architectures (1oo2, 2oo2,
    2oo3) for different safety/availability profiles. The honest reading is that 2-of-3 is a
    defensible robust default, not a context-invariant optimum.

  Caveats:
    - FLAGGED AGAINST OWN BRIEF by 15a. Three independent literatures contradict the
      context-invariance half. (a) SDT: beta_opt = [P(N)/P(S)] x [(V(CR)+C(FA))/(V(H)+C(M))], an
      explicit function of context (Landy SDT chapter, cns.nyu.edu; "Optimal metacognitive decision
      strategies in signal detection theory," Psychonomic Bulletin & Review,
      doi 10.3758/s13423-024-02510-7). (b) Cost-sensitive thresholding (scikit-learn
      "Post-tuning the decision threshold for cost-sensitive learning"; Dmochowski et al., JMLR 11).
      (c) Safety engineering: the 1oo2-vs-2oo3 choice IS the context-specific threshold decision,
      made per loop.
    - The ensemble literature is consistent that the OPTIMAL rule is weighted majority with log-odds
      weights; plain majority is optimal only under equal competence, independence and equiprobable
      classes. Tripled instances of one base model are the paradigm case where independence fails
      (arXiv:2604.17139, "The Consensus Trap").
    - Mitigating: majority rule is defensible precisely BECAUSE competences are uncalibrated;
      weighted voting requires calibration data C2A2 does not have.

  METHODOLOGICAL NOTE: venue/year/DOI could not be verified for the Fey supermajority note or for
    "The Robust Beauty of Majority Rules"; both are recorded only as encountered PDFs. The
    preprints.org manuscript has no verifiable author or title. See the correction on source 4 -
    15a's strongest claimed new support did not survive 15c's verification.

  Recommendation: PARTIALLY-SUPPORTED
    (Support for "2-of-3 is a reasonable robust default." No support, and active contradiction, for
    "one fixed threshold is optimal across heterogeneous decision types." The presumption as
    literally stated should be narrowed.)

  NOTE TO 15c (verbatim from 15a): "My brief was to find support and I did find real support - but
    only for the half of the presumption that nobody was disputing. The cycle-5 question was
    specifically about context-invariance, and signal detection theory, cost-sensitive
    thresholding, and IEC 61508 voting-architecture practice all independently say the optimal
    threshold is a function of error costs and priors. I would rather flag this than let a
    PARTIALLY-SUPPORTED verdict launder it. The defensible narrowed claim is: 2-of-3 is a good
    robust default when per-agent competences are uncalibrated and error costs are unknown or
    roughly symmetric - which is a conditional, and the conditions are checkable."
