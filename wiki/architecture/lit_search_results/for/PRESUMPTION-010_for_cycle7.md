SEARCH-FOR-PRESUMPTION-010 (literature limb, 15d cycle 7):
  Date searched: 2026-09-01
  Original item: PRESUMPTION-010 (MONITOR-012)
  Original statement: "The external benchmarks DRBench (insight recall), Deep Research Bench,
    LiveNewsBench and PluriHop measure the right construct for assessing whether an automated agent can
    reliably detect condition changes via web search without human intervention."
  Note on scope: this is the LITERATURE LIMB only. The parent item PRESUMPTION-010 is tagged
    [QUEUED-EMPIRICAL]; the empirical limb (a measurement of Agent 16 itself) is NOT addressed here and
    remains unexecuted. Cycle 6 (2026-08-08) stated this literature limb explicitly rather than folding
    it in; this run is its first execution.

  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15a, 15b -> 15c -> 15d -> 15a (cycle 7)
    Original item: PRESUMPTION-010
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from the design commitment that Agent 16 monitors conditions unattended
      15d: re-triggered weekly, cycles 1-7; cycle 6 named the literature limb
      15a: searched for supporting literature on the construct validity of the four named benchmarks
    Current status: PARTIALLY-SUPPORTED

  Search scope: Ten distinct queries covering each named benchmark individually; construct validity and
    best practice for agentic benchmarks; recall-primary evaluation in systematic-review screening
    automation; automated horizon-scanning evaluation; freshness/temporal QA (FreshQA, RealTimeQA); TREC
    Temporal Summarization and Real-Time Summarization as recall-of-updates precedent; benchmarks for
    unattended continuous monitoring. Depth: preliminary-to-moderate. Primary sources located and their
    stated constructs read from abstracts/overviews; full papers not read end to end; no independent
    replication of reported validation statistics.

  Supporting evidence found: Partial

  Sources:
    1. Abaskohi et al. (ServiceNow AI Research), 2025. "DRBench: A Realistic Benchmark for Enterprise
       Deep Research." arXiv:2510.00172; code at github.com/ServiceNow/drbench — Directly instantiates
       the recall construct: decomposes an agent's report into atomic cited insights, matches them
       against ground-truth injected insights via LLM judge, and scores recall (explicitly
       recall-oriented, not precision-oriented), paired with Distractor Avoidance, Factuality and Report
       Quality. 100 persona-grounded tasks over a heterogeneous search space including the open web.
    2. FutureSearch, 2025. "Deep Research Bench: Evaluating AI Web Research Agents." arXiv:2506.06287;
       drb.futuresearch.ai — 89 multi-step web research tasks across 8 categories with human-worked
       answers, including "Find Number" and "Validate Claim" categories that map closely to "has this
       condition changed / is this claim still true." Reports that offline (RetroSearch) agents perform
       comparably to live-web agents.
    3. Zhang et al., 2026. "LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated
       News." OpenReview 5HJkrZTtqr; arXiv:2602.13543 — Auto-generates QA pairs from recent news and
       refreshes quarterly from the preceding three months, explicitly so questions cannot be answered
       from parametric memory. Closest direct measure of "can the agent find newly published information
       it could not already know."
    4. Sveistrys et al., 2025. "PluriHop: Exhaustive, Recall-Sensitive QA over Distractor-Rich Corpora."
       arXiv:2510.14377 — Formalizes "pluri-hop" questions by three conditions: recall sensitivity,
       exhaustiveness, exactness — questions where a single missed passage flips the answer and there is
       no natural stopping point for retrieval. Motivated by recurring-report monitoring domains. The
       strongest theoretical grounding found for treating recall-under-distractors as the load-bearing
       construct for a monitoring agent.
    5. Aslam & Diaz et al., NIST. "TREC Temporal Summarization Track" (2013-2015) and "TREC Real-Time
       Summarization Track" (2016-). trec.nist.gov/data/tempsumm.html — Long-standing empirical
       precedent: systems monitor a document stream for an unfolding event and emit updates, scored with
       latency-penalized precision and recall plus a redundancy penalty. Establishes that
       recall-of-new-relevant-updates over a changing stream is an evaluable, community-validated
       construct rather than a novel one.
    6. Vu et al., 2023. "FreshLLMs / FreshQA." arXiv:2310.03214; and Kasai et al., "RealTime QA" —
       FreshQA's 600 questions are stratified by rate of answer change (never/slow/fast-changing, plus
       false-premise) with a human-validated RELAXED/STRICT protocol; RealTimeQA evaluates weekly on
       current events. Precedent that "detect that the answer has changed" is operationalizable.
    7. Microsoft Research, 2026. "SentinelBench: A Benchmark for Long-Running Monitoring Agents."
       arXiv:2606.05342 — 100 tasks across 10 synthetic web environments replaying scripted event
       sequences (e.g. a new paper being published), scoring task completion, reaction time and resource
       use for agents that must notice an external change and respond. Direct demonstration that
       unattended change-detection is a benchmarkable construct, and a validated instrument for the
       limb the four named benchmarks cover least. [arXiv ID independently verified by 15c, 2026-09-01]
    8. O'Mara-Eves / Norman / Scells lineage on screening automation, incl. Scells et al.,
       "Outcome-based Evaluation of Systematic Review Automation" (arXiv:2306.17614) and Kusa et al.,
       "CSMeD" (arXiv:2311.12474) — Analogous-domain validation: this literature converged on
       recall/sensitivity (>=95% recall convention, WSS@95%) as the primary metric precisely because
       missed-relevant-item cost is asymmetric, and warns that AUC-style metrics mislead in high-recall
       regimes.
    9. Nesta Discovery Hub / AiCE (DOI 10.1109/...9308128) and "Horizon Scans can be accelerated using
       novel information retrieval" (arXiv:2504.01627) — Horizon-scanning automation evaluates
       emerging-development detection using WSS@95% recall: the same recall-anchored frame applied to
       change detection over an open corpus.
   10. Zhu et al., 2025. "Establishing Best Practices for Building Rigorous Agentic Benchmarks."
       arXiv:2507.02825 — Audits 17 widely used agentic benchmarks and translates validity criteria into
       an actionable checklist. Supportive in that a construct-validity apparatus now exists and can be
       applied to justify or repair a benchmark selection.

  Benchmark verification:
    DRBench — VERIFIED (arXiv:2510.00172). Measures Insight Recall + Distractor Avoidance, Factuality,
      Report Quality over enterprise + open-web deep research.
    Deep Research Bench — VERIFIED (arXiv:2506.06287, FutureSearch). 89 human-answered multi-step web
      research tasks in a frozen "RetroSearch" environment.
    LiveNewsBench — VERIFIED (OpenReview 5HJkrZTtqr). Multi-hop questions auto-generated from news
      post-dating training cutoff, refreshed quarterly.
    PluriHop — VERIFIED (arXiv:2510.14377). Exhaustive, recall-sensitive, exact QA over distractor-rich
      repetitive corpora; instance is PluriHopWIND (48 questions, 191 wind-industry reports). Note: a
      document-corpus benchmark, NOT an open-web one.

  Strength of support: Moderate

  Summary: All four named benchmarks exist, are publicly documented, and three of the four measure a
    component of the target construct fairly directly. DRBench operationalizes insight recall explicitly
    and scores recall rather than precision; PluriHop supplies the formalization — recall sensitivity,
    exhaustiveness, exactness — that makes recall the correct primary metric when a single missed item
    flips the conclusion. LiveNewsBench most directly addresses the "newly published condition" limb by
    construction. Deep Research Bench contributes measurement reliability (frozen corpus, human-worked
    answers) and claim-validation tasks. The construct is not novel: TREC Temporal/Real-Time
    Summarization, FreshQA/RealTimeQA, and the systematic-review-screening and horizon-scanning
    literatures all provide independent, long-standing precedent for recall-anchored evaluation of
    detecting new relevant information over a changing stream.

  Caveats:
    1. Coverage is componential, not holistic. No one of the four measures the full conjunction of
       "reliably + detect condition changes + without human intervention." The unattended-longitudinal
       limb is measured by SentinelBench, not by any of the four; all four are single-session,
       prompted-task benchmarks rather than persistent monitors.
    2. PluriHop's evaluated instance is a closed 191-document corpus, so transfer to open-web monitoring
       is by analogy; absolute scores (<=40% F1 for naive/graph/multimodal RAG) show the construct is
       far from saturated.
    3. Deep Research Bench's frozen corpus buys reliability at the cost of live-web dynamics — precisely
       the variable a change-detection use case cares about.
    4. DRBench's recall is scored by LLM-as-judge; support weakens to the degree judge-human agreement
       was not independently established for the domain of interest.
    5. Benchmark aggregate scores are population-level; nothing found licenses an inference from
       benchmark rank to per-deployment reliability on a specific monitoring task.
    Support is strongest for "recall is the right metric family" and weakest for "these four, as a set,
    are sufficient to certify unattended reliability."

  Recommendation: PARTIALLY-SUPPORTED
