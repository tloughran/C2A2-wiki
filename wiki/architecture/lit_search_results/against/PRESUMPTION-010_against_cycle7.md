SEARCH-AGAINST-PRESUMPTION-010 (literature limb, 15d cycle 7):
  Date searched: 2026-09-01
  Original item: PRESUMPTION-010 (MONITOR-012)
  Original statement: "The external benchmarks DRBench (insight recall), Deep Research Bench,
    LiveNewsBench and PluriHop measure the right construct for assessing whether an automated agent can
    reliably detect condition changes via web search without human intervention."
  Note on scope: LITERATURE LIMB only. The empirical limb of PRESUMPTION-010 (a measurement of Agent 16
    itself) is NOT addressed here and remains unexecuted.

  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a, 15b -> 15c -> 15d -> 15b (cycle 7)
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from the design commitment that Agent 16 monitors conditions unattended
      15d: re-triggered weekly, cycles 1-7; cycle 6 named the literature limb
      15b: searched for challenging literature on the construct validity of the four named benchmarks
    Current status: STRONGLY-CHALLENGED

  Independence note: run in a separate agent context from 15a. Neither direction could read the other's
    files or results. Per PREMISE-197, context separation removes a contamination channel but does not
    create statistical independence — both directions share a base model and prompt scaffold.

  Search scope: Comprehensive for the challenge limb. Nine distinct queries plus two primary-source
    fetches. Angles: existence/scope verification of each named benchmark; construct-validity critiques
    of LLM and agentic benchmarks; search-time contamination and parametric-knowledge leakage;
    frozen-snapshot vs live-web ecological validity; benchmark-to-deployment transfer failure and
    run-to-run reliability; the answer-exists assumption, abstention, and false-negative measurement in
    monitoring and horizon scanning; LLM-as-judge reliability for rubric metrics; benchmark aging.

  Challenging evidence found: Yes

  Sources:
    1. Abaskohi et al., 2025. "DRBench." arXiv:2510.00172 — 100 synthetically generated enterprise tasks
       over a FIXED heterogeneous corpus, LLM-judge scored. Verifies the benchmark but shows the tasks
       are static and analyst-report-shaped, not change-detection over time.
    2. Sveistrys et al., 2025. "PluriHop / PluriHopRAG." arXiv:2510.14377 — PluriHopWIND is 48 questions
       over 191 FIXED wind-industry PDF reports. Explicitly a closed-corpus RAG benchmark; contains no
       web search and no temporal/novelty dimension.
    3. FutureSearch, 2025. "Deep Research Bench." arXiv:2506.06287 — Agents are served "RetroSearch," a
       frozen ~189k-page scrape rather than live pages, explicitly to buy reproducibility.
    4. Du et al., 2025. "DeepResearch Bench." arXiv:2506.11763 — A DIFFERENT benchmark with a
       near-identical name: 100 PhD-expert-authored tasks, LLM-judge scoring against LLM-generated
       reference reports.
    5. Zhang et al., 2026. "LiveNewsBench." arXiv:2602.13543 — Verified, but bounded known-answer QA
       capped at 5 searches / 5 page visits per question; not open-ended surveillance.
    6. "LiveBrowseComp: Are Search Agents Searching, or Just Verifying What They Already Know?", 2026.
       arXiv:2605.28721 — Documents "Intrinsic Knowledge Dependence": agents answer up to 44.5% of
       BrowseComp without tools, generate over half their queries from internal hypotheses rather than
       retrieved leads, and do WORSE than closed-book when supporting evidence is removed. Performance
       on genuinely post-cutoff questions collapses below 2%.
       [arXiv ID and title independently verified by 15c, 2026-09-01]
    7. "Search-Time Contamination in Deep Research Agents", 2026. arXiv:2606.05241 — Retrieval can
       surface benchmark answers directly from the public web, inflating measured performance.
    8. Reuel, Weidinger et al., 2025. "Measuring what Matters: Construct Validity in Large Language
       Model Benchmarks." arXiv:2511.04703 — Review of 445 benchmark papers: only 16% use uncertainty
       estimates or statistical tests; 27% use convenience sampling; predictive/ecological validity is
       almost never established.
    9. Zhu, Kang et al., 2025. "Establishing Best Practices for Building Rigorous Agentic Benchmarks."
       arXiv:2507.02825 — Severe validity issues in 8 of 10 popular agent benchmarks, in some cases
       producing up to 100% misestimation of agent capability.
   10. FAIR, 2025. "AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions." arXiv:2506.09038 —
       Models systematically fail to abstain on unanswerable, underspecified, false-premise and
       outdated-information items; reasoning fine-tuning makes abstention worse.
   11. "Agentic Abstention: Do Agents Know When to Stop Instead of Act?", 2026. arXiv:2606.28733 —
       Identifies the answer-exists bias: corpora document what is known, so agents read unknowability
       as insufficient search effort.
   12. "Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?" (RUVERBENCH), 2026.
       arXiv:2606.29920 — Substantial residual noise in LLM judges' fine-grained rubric verification for
       deep-research outputs.
   13. "When Benchmarks Age: Temporal Misalignment through LLM Factuality Evaluation", EACL 2026.
       arXiv:2510.07238 — More than half of examined benchmarks mislabel factually-correct current
       answers as wrong because gold labels have gone stale.
   14. "Towards a Science of AI Agent Reliability", 2026. arXiv:2602.16666 — Single-attempt benchmarks
       are structurally unable to measure reliability; pass@k rewards one-in-k success while pass^k is
       what deployment requires, and the two diverge sharply.
   15. "From benchmarks to deployment: a comprehensive review of agentic AI evaluation." Artificial
       Intelligence Review, 2026. DOI 10.1007/s10462-026-11571-0 — Structural mismatch between clean
       single-turn benchmark conditions and production conditions. NOTE: accompanying ~37%
       lab-to-production and 60%->25% eight-run figures in the same result set are VENDOR-REPORTED, not
       peer-reviewed; treated as indicative only.
   16. "WebForge: Breaking the Realism-Reproducibility-Scalability Trilemma in Browser Agent
       Benchmarks", 2026. arXiv:2604.10988 — 12% of sampled Mind2Web tasks expired within one year;
       live-environment drift silently corrupts scores.

  Benchmark verification:
    DRBench — VERIFIED (arXiv:2510.00172)
    Deep Research Bench — VERIFIED BUT AMBIGUOUS: two distinct 2025 artifacts carry near-identical
      names — FutureSearch's "Deep Research Bench" (arXiv:2506.06287, 89 tasks, frozen RetroSearch) and
      "DeepResearch Bench" (arXiv:2506.11763, 100 expert tasks, LLM-judge). The presumption does not
      disambiguate, and the two differ precisely on the disputed axis.
    LiveNewsBench — VERIFIED (arXiv:2602.13543)
    PluriHop — VERIFIED, but the artifact (PluriHopWIND) is a 48-question closed-corpus RAG benchmark,
      not a web-search benchmark.

  Challenges:
    CHALLENGE 1: [direct contradiction] PluriHop does not involve web search at all.
      Finding: PluriHopWIND is 48 questions over 191 fixed PDFs, evaluated by statement-wise F1 in a RAG
        setting. No open web, no live retrieval, no temporal dimension, no notion of new or changed
        information. Citing it as evidence about open-web condition-change detection is a category
        error, not a matter of degree.
      STEELMAN: PluriHop's genuine contribution is the formalization of recall sensitivity — one missed
        passage sinks the answer, with no natural stopping condition. That property is real and shared
        with monitoring. If invoked only as evidence that recall-sensitive tasks are hard and current
        methods top out near 40% F1, the citation is legitimate as an upper-bound warning. It cannot
        bear the weight of "measures whether an agent can detect condition changes via web search": it
        bounds performance on the easier closed static case, which argues AGAINST confidence in the
        harder open case.

    CHALLENGE 2: [direct contradiction] The benchmarks reward verification of what the model already
      knows, not discovery of what is new.
      Finding: LiveBrowseComp (arXiv:2605.28721) measures Intrinsic Knowledge Dependence: agents answer
        up to 44.5% of BrowseComp with no tools, generate more than half their queries from internal
        hypotheses, and perform worse than closed-book baselines when supporting evidence is removed
        from the environment. On questions restricted to the 90 days before construction, scores fall
        below 2%. Detecting a newly published condition change is by definition outside parametric
        knowledge — precisely the regime where measured performance collapses.
      STEELMAN: LiveNewsBench was designed against exactly this objection. The strongest version is
        narrower but still severe: freshness is necessary, not sufficient. Even a freshness-controlled
        benchmark measures whether an agent can find a fact it has been TOLD to look for, with a
        guaranteed-existing answer, inside a 5-search/5-click budget. It does not measure whether an
        unprompted agent with a standing monitoring brief and no target will notice a change.
        LiveNewsBench corrects the freshness confound while leaving the TASKING confound untouched.

    CHALLENGE 3: [boundary condition] None of the four measures the false-negative rate, which is the
      governing metric for monitoring.
      Finding: All four rest on the answer-exists assumption. Monitoring inverts this: the decisive
        question is whether an agent reporting "no change" is correct, i.e. FN/(FN+TP). AbstentionBench
        and "Agentic Abstention" show models systematically fail to abstain and read unknowability as
        inadequate search effort. A targeted search for a benchmark evaluating agentic detection of
        newly-published change surfaced no such artifact among the four.
      STEELMAN: DRBench's Distractor Avoidance is a partial proxy for the false-positive side and
        PluriHop's recall sensitivity a partial proxy for the false-negative side, so miss behaviour is
        not entirely unmeasured. But these are per-task, within-corpus proxies. Neither is a miss rate
        over an unbounded, continuously-changing corpus, and no published number from the four reads as
        "this agent will detect X% of real condition changes." The metric the presumption needs cannot
        exist in these benchmarks even in principle, because the denominator (all changes that
        occurred) is not enumerable in an open-web setting.

    CHALLENGE 4: [failed transfer] Frozen snapshots buy reproducibility by removing the live-web
      dynamics the construct depends on.
      Finding: Deep Research Bench serves a frozen ~189k-page archive, deleting index latency between
        publication and indexability, paywalls, anti-bot denial of authoritative sources, snippet
        staleness and content drift. WebForge/WebCanvas documents the mirror problem for live
        benchmarks: 12% of Mind2Web tasks expired within a year and drift silently corrupts scores. The
        field is in an acknowledged realism/reproducibility trilemma; either horn breaks the inference.
      STEELMAN: This is not an oversight — the authors name the tradeoff and choose reproducibility,
        correctly, for their stated purpose of ranking agents. The challenge is to the USE, not the
        artifact: a frozen-corpus score measures reasoning-and-synthesis holding retrieval-environment
        quality CONSTANT, and condition-change detection is dominated by exactly the
        retrieval-environment variance that was held constant. High RetroSearch performance is
        compatible with arbitrarily poor field detection, and the benchmark cannot distinguish them.

    CHALLENGE 5: [scale failure] Single-run scoring cannot certify reliability over repeated cycles.
      Finding: "Towards a Science of AI Agent Reliability" argues single-attempt benchmarks are
        structurally unable to measure reliability, and that pass@k diverges sharply from pass^k.
        Monitoring is definitionally a pass^k task: an agent run weekly for a year must not miss the one
        cycle that matters. None of the four reports pass^k, seed variance, or per-task reliability
        distributions.
      STEELMAN: One could argue mean accuracy across 100 tasks is itself repeated sampling. The honest
        rebuttal: averaging across DIFFERENT tasks estimates breadth, not per-task stability, and cannot
        distinguish an agent that reliably solves 60% of task types from one that solves any given task
        60% of the time. Only the second matters for monitoring, and it is the one not reported.

    CHALLENGE 6: [boundary condition] The measurement instruments are themselves noisy, and
      contamination and label aging bias them in opposite, unbounded directions.
      Finding: DRBench and both Deep Research Bench variants rely on LLM judges; RUVERBENCH finds
        substantial residual noise for exactly these scenarios. Search-time contamination inflates
        scores; benchmark aging deflates them; the construct-validity survey reports only 16% of 445
        benchmarks use any uncertainty estimate.
      STEELMAN: These are field-wide problems with partial mitigations (DeepResearch Bench validated
        against expert annotators; LiveNewsBench includes a human-verified subset). The strongest form
        is about error DIRECTION: contamination biases up, stale labels bias down, judge noise widens
        the interval; the net is unknown and unbounded, so these scores cannot support a reliability
        claim at a specific threshold — the form the presumption requires.

    CHALLENGE 7: [boundary condition] The citation itself is under-specified.
      Finding: "Deep Research Bench" resolves to two different artifacts with different tasks, scoring,
        sizes and environments. "PluriHop" names a question type and a method; the benchmark is
        PluriHopWIND.
      STEELMAN: Citation hygiene rather than substance, and either artifact is a plausible referent. It
        matters here only because the two differ precisely on the frozen-vs-live axis under dispute, so
        the presumption's own evidence cannot be checked without further specification.

  Strength of challenge: Strong

  Summary: All four benchmarks exist and are legitimate published artifacts, but the claim that they
    measure the construct in question does not survive scrutiny. PluriHop contains no web search
    whatsoever, and "Deep Research Bench" is ambiguous between two papers differing on exactly the
    disputed axis. More fundamentally, all four instantiate a known-target, answer-exists, single-shot,
    judge-scored design: they ask whether an agent can find a fact it was directed to find, whereas
    condition monitoring asks whether an unprompted agent will notice something changed and whether its
    "nothing changed" reports can be trusted. LiveBrowseComp is the sharpest empirical challenge —
    agents use retrieval to confirm parametric hypotheses rather than to discover, and collapse below 2%
    on genuinely post-cutoff material. Layered on top are field-wide validity failures documented at
    scale, plus contamination, label aging, judge noise, and the absence of any pass^k or variance
    reporting a repeated-cycle monitoring commitment would require.

  SYSTEMIC-RISK-FLAG: All seven challenges share one root vulnerability — THE BENCHMARKS MEASURE
    RETRIEVAL-GIVEN-A-KNOWN-TARGET ON A BOUNDED CORPUS, WHILE THE DEPLOYMENT CONSTRUCT IS
    SURVEILLANCE-FOR-UNKNOWN-TARGETS ON AN UNBOUNDED, CONTINUOUSLY-CHANGING ONE. Three consequences
    follow that no score improvement can remedy:
      (1) the false-negative rate, the governing metric for any monitoring commitment, has no
          denominator in an open-web setting and is reported by none of the four;
      (2) high scores are compatible with an agent that succeeds by RECOGNIZING rather than
          DISCOVERING, so improvements may reflect growing parametric coverage rather than growing
          search competence — a proxy that DEGRADES precisely as models get better;
      (3) all four report single-run aggregate accuracy, so a commitment expressed as "will not miss a
          material change" is underwritten by evidence that cannot speak to per-task repeatability.
    Any C2A2 reliance chain treating a benchmark percentile as monitoring assurance inherits all three
    at once. These benchmarks can establish a CEILING (if agents cannot do the easier bounded task they
    cannot do the harder open one) but cannot establish a FLOOR — and the presumption uses them as a
    floor.

  Recommendation: STRONGLY-CHALLENGED
