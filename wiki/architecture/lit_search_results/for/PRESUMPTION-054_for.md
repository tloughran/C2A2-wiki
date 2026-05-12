SEARCH-FOR-PRESUMPTION-054:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-054
  Original statement: "Specialist scheduled tasks converge on terminal output without turn-cap / cost-cap / time-cap"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-054
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as convergence-by-completion in specialist scheduled tasks without bounded-exploration safeguards
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Bounded-exploration / anytime-algorithm literature (Zilberstein 1996; Russell & Norvig 2021 AIMA ch. 4): well-designed search agents carry an explicit time or cost budget and emit best-so-far results at the budget cutoff — unbounded search is not a standard design primitive.
    2. LLM-agent convergence practice (Yao et al. 2023 ReAct; Schick et al. 2023 Toolformer; LangChain/OpenAI agent-framework docs 2024–2026): turn-cap, cost-cap, and time-cap are universal in production agent systems; removing them is explicitly documented as a bug class, not a design choice.
    3. Runaway-task risk literature (Amodei et al. 2016 "Concrete Problems in AI Safety"; production LLM incident-reports 2023–2025): unbounded LLM tasks have documented failure modes (loops, excessive cost, resource exhaustion) — these are core alignment-safety concerns, not tail risks.
    4. CRON / scheduled-task best practices (systemd-timer / Kubernetes CronJob docs): time-cap is the default safety primitive on all major schedulers; not setting one is a configuration smell.

  Strength of support: None

  Summary: No literature supports unbounded convergence as a valid scheduled-task design. Every relevant body — AI-safety, LLM-agent-framework practice, bounded-exploration theory, and CRON-task best practices — prescribes explicit caps. Removing caps is documented as a known bug class, not as a legitimate design choice. PRESUMPTION-054 is extra concerning because it interacts with PRESUMPTION-049 (cross-task scope-partition) and PRESUMPTION-051 (pending-count emitted during in-flight specialist) — together these form a cross-task coordination gap.

  Caveats: (a) A specialist task may be short-running *in practice* even without caps — but that is contingent, not guaranteed; (b) cost-caps require a cost-metering infrastructure, which may not exist yet in this setup.

  Recommendation: NO-SUPPORT-FOUND (strong convergence against unbounded scheduled tasks; caps are a universal safety primitive)
