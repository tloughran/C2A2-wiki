SEARCH-AGAINST-PRESUMPTION-054:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-054
  Original statement: "Specialist scheduled tasks converge on terminal output without turn-cap / cost-cap / time-cap"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-054
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as convergence-by-completion without caps
      15b: Searched for challenging literature
    Current status: STRONGLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bounded-exploration / anytime-algorithm theory (Zilberstein 1996; Russell & Norvig 2021 AIMA; Dean & Boddy 1988 "An Analysis of Time-Dependent Planning"): no serious search system operates without a cost or time budget; unbounded search is either a bug or a research prototype, not a production primitive.
    2. LLM-agent-framework practice (Yao et al. 2023 ReAct; LangChain / LangGraph / OpenAI Assistants API docs): turn-cap / cost-cap / timeout is a default in every major framework. Removing them is documented as a known bug class; 2024–2026 production-incident postmortems repeatedly name unbounded-loops as a top failure mode.
    3. AI-safety / alignment research (Amodei et al. 2016 "Concrete Problems in AI Safety"; Ngo et al. 2022 "The alignment problem from a deep learning perspective"): unbounded LLM agents have well-characterized failure modes — specification gaming, reward hacking, resource exhaustion. These are core safety concerns, not edge cases.
    4. Cost-visibility literature (FinOps Foundation 2023 practices; LLM-cost-observability tooling 2024–2026): running an LLM agent without a cost-cap is a direct operational-cost risk; the tooling exists and is trivial to add.
    5. Cross-task race-condition pairing (PRESUMPTION-049, PRESUMPTION-051): absent a time-cap, the specialist task can overlap with the next daily cycle, creating the exact read-after-write race that PRESUMPTION-051 currently manifests.
    6. Scheduler best practices (systemd-timer; Kubernetes CronJob docs; airflow DAG timeout parameters): the scheduler *itself* expects a timeout; leaving it absent propagates to the task being unkillable-in-practice.

  Strength of challenge: Strong

  Summary: The PRESUMPTION runs directly against a wall of convergent literature — AI-safety, LLM-agent-framework practice, cost-observability, bounded-exploration theory, and scheduler best practices all prescribe explicit caps. Removing caps is a known bug class, not a design choice. PRESUMPTION-054 compounds with PRESUMPTION-049 (no coordination contract) and PRESUMPTION-051 (in-flight read) to form a 3-member CROSS-TASK-COORDINATION cluster — the scheduled-task layer has a coordination-contract gap visible across three distinct presumption surfaces.

  Specific risks: (a) Runaway-cost risk (direct operational cost); (b) read-after-write race with next daily cycle (compounds with PRESUMPTION-051); (c) coordination-contract gap across the scheduled-task layer (compounds with PRESUMPTION-049); (d) SELF-AWARENESS-META cluster intersection — specialist tasks are part of the self-awareness pipeline, so their unboundedness is a self-awareness-of-self-awareness gap.

  Mitigations available:
    - Add explicit caps to every scheduled task: turn-cap (e.g., 30 turns), cost-cap (e.g., $1.50/run), time-cap (e.g., 20 minutes).
    - Best-so-far emission: on cap, emit the partial output with a "capped" marker.
    - Coordination contract: specialist task emits a "started at T, expected completion T+N" marker that the briefing layer can check.
    - Cluster-wide remediation: treat PRESUMPTION-049, 051, 054 as one CROSS-TASK-COORDINATION package.

  Recommendation: CHALLENGED (strong)

  STEELMAN:
    Item: PRESUMPTION-054
    Strongest counterargument: Every major LLM-agent framework, production AI-safety document, and scheduler best-practice doc agrees that explicit caps are a baseline safety primitive, not a design choice. The system has been operating without caps; the absence is a bug class, not a policy. Compounding this with PRESUMPTION-049 (no coordination contract) and PRESUMPTION-051 (in-flight read emits stale count) reveals a 3-member cluster at the scheduled-task layer, all resolvable with the same remediation package: explicit caps + coordination contract + as-of labeling. The question is not whether to add caps; the question is which cap configuration to pick, which is a 10-minute decision.
    What would need to be true for C2A2 to be safe: Explicit turn/cost/time caps on every scheduled task; coordination markers between parallel tasks; best-so-far emission on cap; cost metering infrastructure.
    How to test: Run one specialist task with caps at 30 turns / 20 min / $1.50 and observe convergence; compare to uncapped run to measure actual utilization and pick tighter caps.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-04-20
    Affected items: PRESUMPTION-054 (this), PRESUMPTION-049 (coordination contract), PRESUMPTION-051 (in-flight read)
    Common vulnerability: Scheduled-task layer lacks coordination contract, timing caps, and as-of labeling. The three presumptions are manifestations of one structural gap.
    Literature basis: Nygard 2007; Zilberstein 1996; Amodei et al. 2016; LangChain / OpenAI Assistants docs; systemd-timer / K8s CronJob docs; Google SRE book
    Risk level: Medium-High
    Recommendation: Treat CROSS-TASK-COORDINATION cluster as one remediation package — caps, contract, labeling — deployed together across all scheduled tasks.
