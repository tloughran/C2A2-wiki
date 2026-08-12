SEARCH-FOR-PRESUMPTION-031:
  Date searched: 2026-08-11
  Original item: PRESUMPTION-031
  Original statement: "A specialist-rotation schedule (2 specialists/day over 6 days) provides adequate coverage via generalist-orchestrator fallback."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 5)
    Original item: PRESUMPTION-031
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — unstated adequacy claim for the specialist rotation across 11 traditions
      15a (cycle 1, 2026-04-16): initial supporting search — round-robin scheduling, fair-queueing theory, human-review rotation with escalation; PARTIALLY-SUPPORTED, Moderate for the general pattern / Weak for the specific claim
      15d: re-triggered for cycle 5 monitoring
      15a (cycle 5, 2026-08-11): re-searched for supporting literature; checked for new sources since April 2026
    Current status: PARTIALLY-SUPPORTED

  Search scope: Task routing and capability-aware agent selection in multi-agent LLM pipelines (2026); role-specialised vs all-in-one agent benchmarks; fallback and graceful-degradation patterns; on-call rotation and round-robin escalation coverage design. Comprehensive for the routing/fallback design pattern; preliminary for the quantitative adequacy question — no source measures coverage adequacy for an 11-item rotation at 2/day.

  Supporting evidence found: Partial

  Sources:
    1. "Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows." arXiv 2605.08761 (2026). — NEW and the most directly relevant source. Benchmarks role-specialised collaboration against a single generalist agent. Supports the *rotation* half of the presumption (specialisation is worth scheduling for) while implying the fallback half carries a real quality cost, since the generalist is the benchmarked-inferior condition.
    2. "Optimal-Agent-Selection: State-Aware Routing Framework for Efficient Multi-Agent Collaboration." arXiv 2511.02200. — NEW. State-aware routing that assigns tasks by agent specialisation; supports the design premise that a router plus specialist pool with defined fallback is a principled architecture rather than an ad hoc arrangement.
    3. "Orchestrating Intelligence: Confidence-Aware Routing for Efficient Multi-Agent Collaboration across Multi-Scale Models." arXiv 2601.04861 (2026). — NEW and the most useful for the adequacy question. Confidence-aware routing means the fallback path is taken as a function of measured confidence rather than merely as a function of who is on shift — the mechanism by which a fallback arrangement can be made adequate rather than merely available.
    4. Zylos Research, 2026-02-20. "Graceful Degradation Patterns in AI Agent Systems." — NEW (2026). Establishes graceful degradation as the design goal for fallback, with two conditions relevant here: fallbacks must be validated through drills/simulation before deployment, and degraded output "must be labeled as potentially outdated." Supports the pattern conditionally on instrumentation C2A2 has not been shown to have.
    5. Rootly, "Round Robin escalation policies: do's and don'ts" / "Why On-Call Schedule Design Shapes Team Health, Reliability, and Burnout Risk"; UpTickNow, "On-Call Rotation and Escalation Policies in 2026." — NEW to this file. Supportive of rotation-plus-escalation as recognised coverage doctrine, with an explicit and important limitation: "round-robin has no built-in notion of capacity or quality; it only advances the pointer."
    6. Tanenbaum, Modern Operating Systems (round-robin with fallback); Kleinrock, 1975, Queueing Systems (bounded staleness under fair scheduling). — Carried forward. General-pattern foundations.

  Strength of support: Moderate (for the rotation-plus-fallback pattern); Weak (for the adequacy of 2/day over 6 days across 11 traditions)

  NEW SINCE LAST CYCLE: Yes — sources 1-5 are new since April 2026, four of them 2026-dated. What they add: the April file rested on classical scheduling theory and human-review analogies. The 2026 literature supplies domain-matched evidence: role specialisation measurably beats an all-in-one generalist (1), state- and confidence-aware routing frameworks exist (2, 3), and graceful degradation has named preconditions (4). Net effect on the presumption is mixed and should be reported as such: the *pattern* is better supported than in April, while the *adequacy of generalist fallback* is worse supported, because 2026 benchmarking makes the specialist-generalist quality gap explicit rather than assumed.

  Evidence trajectory (supporting): stable (pattern support grew; adequacy support did not)

  Summary: The design pattern PRESUMPTION-031 relies on — specialists on rotation with an orchestrator absorbing the gaps — is well recognised and now has 2026 domain-specific literature behind it, including routing frameworks and graceful-degradation guidance. But the presumption's operative word is "adequate," and the strongest new source cuts against it: role-specialised collaboration outperforms an all-in-one generalist, which means orchestrator fallback is a documented quality decrement rather than a neutral substitution. The on-call literature adds the sharpest observation, that round-robin "has no built-in notion of capacity or quality; it only advances the pointer" — a rotation guarantees a turn, not coverage. Adequacy therefore remains an unmeasured empirical claim, exactly as in April, and the three quantities identified in cycle 1 (fallback quality relative to specialist, acceptable staleness per tradition, whether unscheduled traditions systematically under-appear in the PRS distribution) are still unmeasured four months later.

  Caveats: (a) The specialist-vs-generalist benchmarks are enterprise-workflow tasks, not tradition-representation tasks; the size of the fallback decrement in C2A2's domain is unknown. (b) Confidence-aware routing supports adequacy only if confidence is actually measured and acted on; a fixed calendar rotation is not confidence-aware. (c) Graceful-degradation guidance conditions adequacy on pre-deployment drills and on labelling degraded output as such — neither is evidenced in C2A2. (d) The Google/MIT scaling work reports 39-70% degradation on sequential tasks under multi-agent delegation, which is the regime a hand-off from specialist to orchestrator occupies. (e) "Adequate" is still undefined in the queue item, so no source can confirm or refute it as stated. (f) Most new sources are preprints or vendor/practitioner material.

  Recommendation: PARTIALLY-SUPPORTED
