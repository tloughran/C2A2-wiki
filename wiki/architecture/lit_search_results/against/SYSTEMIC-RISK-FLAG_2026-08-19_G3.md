SYSTEMIC-RISK-FLAG:
  Date: 2026-08-19
  Filed by: 15b (Literature Search AGAINST)
  Affected items: PRESUMPTION-839, ASSUMPTION-1150, ASSUMPTION-1149, ASSUMPTION-1153, PRESUMPTION-844
  Common vulnerability: **The system reports counts without denominators, and treats agreement among non-independent observers as corroboration.**

  Statement: Five items in this cohort turn on a quantity the fleet reports but cannot compose. Six per-lineage streak counters, all correct, with no fleet denominator (839). Nine model votes worth about two, with the effective-N never measured locally (1150). Three parses of one queue giving three backlog figures, with no ground truth (1149). Four instrument retractions in a day, with no count of total findings issued that day (1153). Four independent escalations converging on one framing of a bottleneck, treated as convergent evidence (844). In every case a numerator is reported and the denominator is either absent or unmeasured, and in three of the five, concordance among observers is read as confirmation when the observers share a scaffold.

  Literature basis:
    - Ecological fallacy [established-work, Robinson 1950] and Simpson's paradox [established-work]: cross-level inference is unwarranted and can reverse in sign. Operational signature: global metric red, every local report green.
    - Gray failure / differential observability [established-work]: components degrade while detectors report health; described as the mechanism behind most cloud incidents.
    - "Security Considerations for Multi-agent Systems" (arXiv:2603.09002): per-agent thresholds are systematically evadable by distributing events beneath them; the aggregation boundary is itself the exploitable object. [authors not verified]
    - "Correlated Errors in Large Language Models" (arXiv:2506.07962; ICML 2025): ~60% agreement when both models err; correlation *rises* with capability. [authors not verified]
    - "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels" (arXiv:2605.29800): no panel exceeds ~2.6 effective independent votes. [**Title and arXiv ID verified; the "Kohli 2026" attribution used elsewhere in the register is NOT verified and should be checked or dropped.**]
    - Kish design effect [established-work] and its documented limits: exact only for exchangeable Bernoulli votes with common pairwise correlation; a variance-matching approximation otherwise, with bias direction not established under heterogeneous dependence.
    - Ladha, "Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes" (JEBO): correlation degrades aggregation gain continuously; the group remains more reliable than the individual. Two effective votes is a discount, not a nullity.
    - Static-analysis FP base rates 76%–>90% (arXiv:2601.18844): the denominator against which "four retractions" must be read.
    - Log-parsing evaluation (arXiv:2308.09003; ResearchGate 383974909): refined-metric template accuracy ~0.2 — parser divergence is the field's baseline, not a local anomaly.

  Risk level: **High**

  Why it is systemic: Two failure modes compound. First, without denominators no threshold in the system is calibratable, so every alarm level is arbitrary and every count is uninterpretable — "four retractions" and "three consecutive failures" mean nothing without a base rate. Second, the system repeatedly treats agreement as evidence. Six counters agreeing that nothing is wrong is six views of one blind spot; four escalations sharing a framing is one framing repeated four times if the escalators share a scaffold; and ASSUMPTION-1150's own reflexive limb concerns exactly this. The two modes reinforce each other: a missing denominator makes concordance the only available signal, and concordance among entangled observers is the least reliable one.

  Recommendation:
    1. Build the fleet-level record. One store, one row per run, with run ID, lineage, condition flag and timestamp. Streaks become queries; rates become computable. This is the single highest-leverage change in this flag and it closes 839 outright.
    2. Measure ρ locally between 15a and 15b rather than importing an effective-N from a paper about same-direction judge panels. Run both on items with known dispositions, build the 2×2 error table, compute phi. This resolves ASSUMPTION-1150's reflexive limb by measurement instead of argument, and it is cheap.
    3. Report every count with its denominator, or do not report it. "Four retractions" → "4 of N findings issued".
    4. Stop treating concordance as corroboration until independence is demonstrated for the specific observers involved. Where observers share a scaffold, agreement is a lower bound on shared bias, not an upper bound on error.
    5. Verify or drop the "Kohli 2026" attribution before it propagates further through the register. The paper exists; the author name has not been confirmed by this agent.
