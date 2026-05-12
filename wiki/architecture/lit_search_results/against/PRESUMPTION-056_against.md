SEARCH-AGAINST-PRESUMPTION-056:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-056
  Original statement: "Cost is the sole optimization target (no quality-regression smoke test in the rollout gate)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-056
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from smoke-test coverage gap in RC Wiki MCP Install Plan
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Continuous-delivery / deployment-gate literature (Humble & Farley 2010 "Continuous Delivery"; Accelerate — Forsgren et al. 2018): any production rollout gate needs both functional/quality checks and non-functional (cost/latency) checks. Cost-only gates are explicitly named as an anti-pattern.
    2. ML Test Score literature (Chen et al. 2020; Google "Rules of Machine Learning"): specific to ML deployments — quality-regression gates are non-negotiable for production rollouts; any architectural change that touches inference path must be validated for output-quality invariance.
    3. Goodhart's Law applied to optimization targets (Manheim & Garrabrant 2019 "Categorizing Variants of Goodhart's Law"): when a single metric becomes the optimization target, systems game the metric at the expense of unmeasured dimensions. Cost-alone gates reliably produce quality-degradation over time.
    4. LLM-specific quality-regression concerns (Anthropic model-card evaluations; OpenAI production deployment best practices 2024-2026): prompt-caching, while theoretically token-equivalent, has documented edge cases (truncation at cache-breakpoints, cache-miss fallback paths, attention-pattern interactions) that can produce quality degradation.
    5. Cost-framing of 70-80% saving (Monday Report): the headline number is cost; no quality floor is named; if quality regresses by 15%, cost-per-unit-quality may actually be worse. The architecture-as-specified cannot detect this.
    6. Bias-prevention pipeline interaction (ASSUMPTION-053 concern, 15a/15b isolation): if appended-turn topology (ASSUMPTION-053) degrades 15a/15b independence (PARTIALLY-CHALLENGED above), that is a quality regression invisible to byte-stability and cost-measurement alone.

  Strength of challenge: Strong

  Summary: Cost-alone optimization-target commitment is a documented anti-pattern across continuous-delivery, ML testing, and Goodhart's Law literature. LLM-specific quality-regression concerns make the gap more acute: prompt-caching has known edge cases that can degrade quality invisibly to byte-stability and cost measures. The fix is cheap and standard: add a quality-regression smoke test to the rollout gate (sample N proposals pre- and post-cache, have a judge-agent compare). The presumption creates a blind spot where cost wins can mask quality losses — this is the headline risk of the caching architecture as currently specified.

  Specific risks: (a) Quality regression under the cost-win headline; (b) Goodhart's Law optimization pressure toward cost at quality's expense; (c) 15a/15b independence degradation from ASSUMPTION-053 invisible to current gate; (d) cumulative drift undetected until manifested in a downstream failure (e.g., poor cross-tradition signal detection).

  Mitigations available: (a) Add a quality-regression smoke test to the rollout gate: sample N proposals from pre-cache and post-cache runs, LLM-judge compare; (b) define quality-floor thresholds (e.g., no more than 10% of proposals judged worse); (c) instrument quality-adjacent signals continuously (proposal length, reasoning depth, citation count); (d) require a quality-gate PASS in addition to cost-win for rollout approval.

  Recommendation: CHALLENGED (strong; cost-only gate is a documented anti-pattern; fix is cheap and should be required before 2026-04-27 rollout)

  STEELMAN:
    Item: PRESUMPTION-056
    Strongest counterargument: Cost-only deployment gates are universally named as an anti-pattern — continuous delivery, ML testing, and Goodhart's Law literature all converge on requiring quality gates alongside cost gates. LLM-specific concerns make the gap worse: prompt-caching has known edge cases (truncation at cache-breakpoints, cache-miss fallback paths) that can degrade quality invisibly. The fix is not expensive — a judge-agent compares N pre/post samples. Omitting this gate while deploying on a 70-80% cost-saving headline creates exactly the Goodhart's Law condition where cost wins mask quality losses. The presumption is not just a methodological gap; it is an exposed surface for the kind of silent regression the self-awareness pipeline was built to catch elsewhere but fails to catch here.
    What would need to be true for C2A2 to be safe: Add a quality-regression smoke test to the rollout gate; require quality-gate PASS (judge-agent finds no material degradation) AND cost-gate PASS for rollout.
    How to test: Pre-rollout, run 10 proposals in the current architecture and 10 in the cached architecture; LLM-judge each pair blind; any material quality delta blocks rollout.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-04-20
    Affected items: PRESUMPTION-056 (this), ASSUMPTION-054 (byte-stability as sole proxy), ASSUMPTION-053 (appended-turn may degrade 15a/15b independence)
    Common vulnerability: The rollout gate for the caching architecture checks cost and cache-determinism but not output-quality. Multiple known quality-regression vectors (appended-turn isolation, cache-breakpoint truncation, attention interactions) are invisible to the current gate.
    Literature basis: Humble & Farley 2010; Chen et al. 2020 ML Test Score; Manheim & Garrabrant 2019 Goodhart's Law
    Risk level: Medium-High
    Recommendation: Add a quality-regression smoke test to the rollout gate; this is cheap and is standard deployment practice.
