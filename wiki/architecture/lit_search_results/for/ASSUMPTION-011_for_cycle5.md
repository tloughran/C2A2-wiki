SEARCH-FOR-ASSUMPTION-011 (cycle 5 re-check):
  Date searched: 2026-09-03
  Original item: ASSUMPTION-011
  Original statement: "Specialist-agent-first / orchestrator-fallback scheduling is the right division of labor."
  Monitor ID: MONITOR-015, monthly cycle 5

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15a (cycle 5)]
    Original item: ASSUMPTION-011
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Original extraction of architectural assumption about agent scheduling
      15a (cycle 0, 2026-04-13): searched for supporting literature; returned PARTIALLY-SUPPORTED (Moderate)
      15d: re-triggered monthly cycles 1-5 (cycles 1-3 recorded no queries and are treated as NOT RUN)
      15a (cycle 5, 2026-09-03): re-searched for supporting literature — first substantive re-search
    Current status: PARTIALLY-SUPPORTED (but see CRITICAL CITATION FINDING; cycle-0 support was materially misstated)

  Queries run this cycle:
    1. "LLM multi-agent routing specialist agent first versus orchestrator fallback empirical comparison 2026"
    2. "agentic scheduling strategy benchmark specialist routing vs monolithic generalist agent 2025 2026 arXiv"
    3. "AgentArch benchmark enterprise workflows specialist versus generalist agent orchestrator findings results"
    4. "Magentic-One generalist multi-agent system arXiv 2411.04468 authors Fourney" (carried-forward citation check)
    5. "\"Harnessing Pre-trained Generalist Agents\" software engineering arXiv 2312.15536" (carried-forward citation check)

  Supporting evidence found: Partial

  CRITICAL CITATION FINDING — AGAINST MY ASSIGNED DIRECTION (read this before the source list):
    Cycle-0 source 1 was cited as showing "specialist agents outperform generalists on focused tasks; validates specialist-first principle." The arXiv ID resolves, but the paper says the opposite. Mindom, Nikanjam & Khomh (2023/2024), "Harnessing Pre-trained Generalist Agents for Software Engineering Tasks" (arXiv:2312.15536; published Empirical Software Engineering, doi 10.1007/s10664-024-10597-8) reports that *generalist* agents outperform *specialist* agents with very little fine-tuning effort: a 20% reduction in makespan over specialized-agent performance on job-shop scheduling, and up to 85% more bugs detected than specialist agents in game testing. The cycle-0 entry inverted the paper's direction of finding.
    Compounding this: cycle-0 source 3 attributed that same "20% makespan improvement" figure to Magentic-One and reported it as specialists beating generalists. The 20% figure belongs to the Mindom paper and points the other way. So the cycle-0 file cited one real result twice, under two different papers, with the sign flipped both times.
    Net effect: the single strongest empirical citation in the cycle-0 FOR file is, correctly read, evidence AGAINST ASSUMPTION-011. 15c should not treat this FOR return as symmetric with 15b's AGAINST return on this item — part of my assigned-direction evidence base has migrated to the opposing side under audit.

  Sources:
    1. NEW-THIS-CYCLE — Bogavelli, T. et al. / ServiceNow AI Research (2025). "AgentArch: A Comprehensive Benchmark to Evaluate Agent Architectures in Enterprise," arXiv:2509.10769. — The closest thing to the empirical comparison the change-condition asks for: 18 agentic configurations, four orchestration strategies, explicitly including "orchestrator-led, isolated agent" (orchestrator assigns to specialists and mediates all inter-agent communication — structurally C2A2's design) versus "orchestrator-led, open agent network." Mixed for the assumption: multi-agent orchestration is reported as crucial for complex logic, but no configuration dominates, and absolute performance on the complex Customer Routing task tops out at 35.3% (Claude Sonnet 4) versus 70.8% on the simple Time Off task. Also reports that no model performs best under Multi-Agent ReAct.

    2. NEW-THIS-CYCLE — "Beyond the All-in-One Agent: Benchmarking Role-Specialized Multi-Agent Collaboration in Enterprise Workflows," arXiv:2605.08761 (2026). — Directly on the specialist-decomposition question in a workflow setting; the most on-target 2026 benchmark located. Supportive of role specialization as a design, though I could only read the indexed abstract-level material this cycle.

    3. NEW-THIS-CYCLE — "Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation," arXiv:2605.05007 (2026). — Argues for delegating selectively rather than routing every task through the full specialist catalog. Supports the *fallback* half of the assumption (don't invoke the orchestrator's full machinery by default) while cautioning against specialist-first as an unconditional rule.

    4. NEW-THIS-CYCLE — "AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence," arXiv:2602.16873 (2026). — Explicitly task-adaptive: the right division of labor is a function of task type, not a fixed policy. Qualifies the assumption's "is the right division of labor" as too unconditional.

    5. NEW-THIS-CYCLE — "ORCH: many analyses, one merge — a deterministic multi-agent orchestrator for discrete-choice reasoning with EMA-guided routing," arXiv:2602.01797 (2026). — Compares random, rule-based, and performance-based adaptive routing head to head, and reports that routing strategy strongly affects performance, efficiency and reliability. Supports the general claim that *scheduling policy matters*; does not single out specialist-first as the winner.

    6. CARRIED-FORWARD — Horling, B., & Lesser, V. (2004). "A Survey of Multi-Agent Organizational Paradigms," The Knowledge Engineering Review 19(4), 281-316. — PRESUMED-RESOLVED; recognized canonical survey, but NOT directly re-queried this cycle (search budget went to the two citations that showed decay signals). Flagged for direct re-resolution at cycle 6.

    7. CARRIED-FORWARD (RE-RESOLVED, DIRECTION INVERTED) — Mindom, P. S. N., Nikanjam, A., & Khomh, F. (2023). "Harnessing Pre-trained Generalist Agents for Software Engineering Tasks," arXiv:2312.15536 / Empirical Software Engineering (2024). — See CRITICAL CITATION FINDING. Correctly read, this is AGAINST the assumption.

    8. CARRIED-FORWARD (RE-RESOLVED, ATTRIBUTION AND CLAIM BOTH WRONG) — Fourney, A., Bansal, G., Mozannar, H., et al. (2024). "Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks," arXiv:2411.04468, Microsoft Research. — The real paper describes an Orchestrator that plans, tracks progress, re-plans on error, and directs specialized agents (web browser, file navigator, coder). That architecture *is* genuinely supportive of orchestrator-plus-specialist decomposition, so the citation survives as support — but for orchestrator-*led* delegation, not specialist-first-with-orchestrator-fallback. Magentic-One reports no 20% specialist-over-generalist result.

  Carried-forward citation audit:
    - arXiv:2312.15536 (cycle-0 source 1): INCONSISTENT. arXiv ID resolves. Authors as cited ("Graßer, F., Bamberg, T., Müller, F., Iribarren Sanchez, J., & Schäfer, L.") are entirely wrong; actual authors are Mindom, Nikanjam & Khomh (Polytechnique Montréal). Year cited as 2024 (preprint is Dec 2023; journal version 2024 — acceptable). Reported finding is INVERTED relative to the paper.
    - Horling & Lesser 2004 (cycle-0 source 2): PRESUMED-RESOLVED, not directly re-queried. See note on source 6.
    - arXiv:2411.04468 (cycle-0 source 3): INCONSISTENT. arXiv ID and title resolve exactly. Authors as cited ("Gawantka, R., Sander, T., & Scourfield, J.") are fabricated; actual first authors Fourney, Bansal, Mozannar et al. Year cited as 2025, actual 2024. The attributed empirical claim (20% makespan improvement of specialists over generalists) does not appear in this paper and is a cross-contamination from source 1 with the sign flipped.

    METHODOLOGICAL NOTE: Two of three cycle-0 citations have fabricated author lists over real arXiv IDs, and both empirical claims attached to them are wrong — one inverted, one transplanted. Cycles 1, 2 and 3 each recorded "no new sources; prior finding stands," which means this error propagated unexamined through four recorded cycles. This is a citation-integrity failure of the same shape flagged elsewhere in the April cohort, but here it changes the sign of the evidence rather than merely its provenance.

  Strength of support: Weak to Moderate (cycle 0 recorded Moderate; the audit removes the empirical basis for that grade, and the 2026 benchmarks add breadth but not a decisive result)

  Summary: After audit, cycle 0's Moderate grade was resting on a misread. The genuine 2026 literature does support agent specialization and orchestrated decomposition as sound architecture — AgentArch, the role-specialization benchmark, Uno-Orchestra, AdaptOrch and ORCH all take specialist decomposition as the working design and report that routing policy materially affects outcomes. But the specific ordering claim in ASSUMPTION-011 — specialists *first*, orchestrator as *fallback* — is not what these papers test. AgentArch's closest analogue is orchestrator-*led* delegation, i.e. the orchestrator goes first. AdaptOrch and ORCH both argue the correct policy is task-adaptive rather than fixed, which cuts against any unconditional "is the right division of labor." And the one carried-forward paper that made a direct specialist-vs-generalist measurement found generalists ahead. The honest position is that the architectural family is well supported and the specific scheduling ordering is untested.

  Caveats: Nearly all 2026 evidence is from enterprise-workflow and coding benchmarks; C2A2's domain (wiki synthesis and self-audit) has different task-classification difficulty and different failure costs. Absolute success rates on complex tasks in AgentArch (35.3%) are low enough that architecture-level conclusions drawn from them are fragile. The distinction the assumption turns on — who is invoked first — is rarely reported as an independent variable; papers report orchestration *topology*, not invocation *order*. Publication bias strongly favours multi-agent architectures in this literature. Search-scope confidence: MODERATE-TO-HIGH for the 2026 agentic-orchestration literature, LOW for the specific first-vs-fallback ordering question, which appears to be genuinely unstudied rather than merely unfound.

  Change since cycle 0: SUPPORT-WEAKENED. Substantial new 2026 literature exists (five new sources, versus "no new sources" recorded in cycles 1-3), so the item was demonstrably not being searched. But the net effect of reading it is downward: the strongest cycle-0 empirical citation reverses direction under audit, and the strongest new sources (AdaptOrch, ORCH) argue for adaptive rather than fixed scheduling policy.

  Recommendation: PARTIALLY-SUPPORTED
