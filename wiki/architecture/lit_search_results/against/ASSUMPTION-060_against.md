SEARCH-AGAINST-ASSUMPTION-060:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-060
  Original statement: "Read-only observation of still-running specialist sessions is the correct default (natural-termination precedent from 2026-04-19 Levin-Friston)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-060
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from evening sync autonomous-choices note
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. N-of-1 precedent anti-pattern (Hogarth & Soyer 2015 "Providing Information for Decision Making"): generalizing from a single observation produces biased decision rules. A single natural-termination success does not establish a base rate for natural-termination reliability.
    2. Runaway-process / circuit-breaker literature (Nygard 2007 "Release It!"; SRE practices on bounded execution): unbounded process execution is a known failure mode. Industry default is cap-then-review, not observe-indefinitely. Turn-caps and wall-clock-caps are cheap, well-understood, and standard.
    3. Cost-accrual literature in LLM agents (2024-2025 agent-cost papers; OpenAI Assistants pricing documentation): running LLM agents accrue cost monotonically. "Natural termination" without a cost-cap accepts unbounded cost exposure — an economically-unsafe default.
    4. Internal tension with candidate DECISION-024 (turn-cap default = 20): the same day produced both ASSUMPTION-060 (natural-termination as default) and candidate DECISION-024 (turn-cap as default). These are directly opposing stances on the same question.
    5. Confounded-precedent literature (selection effects in case-study reasoning): the Levin-Friston precedent worked because the session happened to terminate. A single successful outcome does not validate the policy; it validates the outcome. Other natural-terminations could have run indefinitely without anyone noticing.
    6. Internal PRESUMPTION-063 (natural-termination as acceptable default) and PRESUMPTION-065 (two Morning tasks as independent data points): the precedent-base is smaller than claimed (2 correlated observations + Levin-Friston, not 3 independent), and the base rate for natural-termination reliability is not established.

  Strength of challenge: Strong

  Summary: Elevating one successful natural-termination to a default policy is methodologically fragile. Single-precedent generalization has well-documented biases (Hogarth & Soyer). Industry standard for bounded execution is cap-then-review, not observe-indefinitely — turn-caps and cost-caps are cheap standard infrastructure. The stance accepts unbounded cost exposure (a default no mature system chooses). And the same day produced a candidate DECISION-024 with the opposite stance (turn-cap default = 20), exposing an internal contradiction. PRESUMPTION-063 and PRESUMPTION-065 further erode the precedent base — today's "3 data points" is at best 2 independent (the two Morning tasks share environment), and successful natural-termination from one instance does not validate the class.

  Specific risks: (a) Unbounded cost exposure — runaway specialist sessions accrue LLM spend with no cap; (b) silent failure indistinguishable from natural termination — a session that hangs forever looks identical to a session that is "almost done"; (c) internal contradiction with candidate DECISION-024 blocks coherent policy; (d) extends PRESUMPTION-063 cluster and CROSS-TASK-COORDINATION gap.

  Mitigations available: (a) Formalize DECISION-024 (turn-cap default = 20) and supersede ASSUMPTION-060; (b) treat read-only observation as a correct first step paired with an escalation threshold (e.g., turn count or wall-clock); (c) add cost-cap primitive as a floor even if turn-cap is deferred; (d) demote "natural termination" from "default" to "fallback after turn-cap does not fire."

  Recommendation: CHALLENGED (strong challenge; N-of-1 precedent-generalization fragile; runaway-process literature endorses cap-then-review as industry default; internal tension with candidate DECISION-024)

  STEELMAN:
    Item: ASSUMPTION-060
    Strongest counterargument: Elevating one successful natural-termination to a default policy is the precedent-canonization anti-pattern. Single-precedent generalization has well-documented biases, and the precedent itself worked because the session happened to terminate — not because natural-termination is a reliable property of these sessions. Industry default for bounded execution is cap-then-review (turn-cap, wall-clock-cap, cost-cap); natural-termination-as-default accepts unbounded cost exposure, which no mature LLM-agent system chooses. The same day produced candidate DECISION-024 with the opposite stance, exposing an internal contradiction that needs resolution before either stance can be formalized. Read-only observation is correct as a first step; it is wrong as a termination policy.
    What would need to be true for C2A2 to be safe: Formalize DECISION-024 turn-cap; downgrade ASSUMPTION-060 to "read-only first step paired with escalation threshold"; add cost-cap floor primitive.
    How to test: Track natural-termination outcomes across N instances; measure fraction that terminate cleanly vs. require manual intervention; compare unbounded cost exposure vs. turn-cap exposure over 30 days.
