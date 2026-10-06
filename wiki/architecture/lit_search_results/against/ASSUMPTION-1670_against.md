SEARCH-AGAINST-ASSUMPTION-1670:
  Date searched: 2026-09-24
  Original item: ASSUMPTION-1670
  Original statement: Scope cut on budget grounds: QC and reviewer runs skipped extra pairs
    "because of your token budget"; the same guideline was exceeded ~6x by the lit pipeline.
    (Tested claim: a per-session token cap applied by the worker, with no priority rule, cuts the
    lowest-cost work rather than the lowest-value work.)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1670
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; the budget is the designer's stated preference (Rule 6), applied unevenly across jobs.
      15b: Searched for challenging literature (lane: bounded rationality; budget allocation under caps; cost-aware agent scheduling)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. BAGEN authors (Chen, B.; Su, J.; Wang, X.; Pei, J.; Li, M.; et al.; the full author list
       and first author were not confirmed from the fetched text) (2026). "BAGEN: Are LLM Agents
       Budget-Aware?" arXiv:2606.00198. [Fetched: HTML, partial read.] Across 20 model-environment
       pairs, agents systematically underestimate the remaining budget ("optimistic misses
       outnumber conservative ones at every rollout-progress bin"). Budget-estimation skill is
       decoupled from task success. So a worker applying its own cap has no reliable idea of what
       each piece of work costs. What gets cut is then set by where the running total happens to
       cross the cap, not by cost rank.
    2. Shortest-job-first starvation (standard OS-scheduling result; seen via Wikipedia "Shortest job
       next" and course notes in search results; no primary textbook fetched). A policy that favours
       cheap jobs under a capacity limit starves the long or expensive ones. By analogy, any worker
       that fits work into a fixed remaining budget by what still fits will cut the high-cost
       items, not the low-cost ones. This is a direct counterexample to the stated direction.
    3. Greedy knapsack by value density (seen in search results, e.g., arXiv:1007.3801 and lecture
       notes; not fetched). The standard way to cut the lowest-value work under a budget needs an
       explicit value-to-cost ranking. Without a priority rule no value signal is available, which
       CORROBORATES the "not lowest-value" half of the claim.

  Strength of challenge: Moderate

  Summary: The literature supports the core concern: without a priority rule, a cap does not
  preferentially cut low-value work. It challenges the specific direction claimed ("cuts the
  lowest-cost work"). Under a cap, what gets cut depends on execution order and on cost
  estimates. Agents underestimate costs, so the cap is usually hit mid-sequence and truncates
  whatever is last or in flight. Where the worker does pre-select by what still fits, the cut
  falls on the expensive items (the SJF-starvation pattern). The truncated tail is often the
  synthesis or report step, which is expensive and high-value. The claim's diagnosis of the
  outcome (value-blind cutting) holds; its mechanism (cost-ordered cutting) is not supported.

  Specific risks: If C2A2 adds a rule assuming cheap items are what gets dropped, it will miss
  that the reports and synthesis steps at the end of runs are the ones actually lost. Reviewer
  47834dc7 ending "with no report" fits this pattern. Caps applied unevenly (lit pipeline ~6x
  over) also mean the cap binds on the jobs that self-report it, not on the ones where cutting
  would be cheapest.

  Mitigations available: Declare in each task file the order in which work is cut (must-do items
  first, report always reserved). Reserve budget for the final report. Log per-item token spend
  so estimates are calibrated. Treat the cap as soft with an explicit overage policy.

  Search scope: Preliminary: 3 searches plus 1 fetch. No empirical study of self-imposed token caps
  in multi-agent LLM pipelines found.

  Excluded results: tianpan.co "Tokens Are a Finite Resource: A Budget Allocation Framework…"
  (vendor/individual blog whose framing closely echoes the lane); aisecuritygateway.ai "LLM Token
  Budget Strategies" (vendor blog); researchgate "Budget-Aware LLM Agents: Evaluation, Failure
  Modes…" (could not verify venue or authors; not fetched); Parkinson's-law results (4dayweek.io,
  monday.com, atlassian blog; popular sources, not evidence).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1670
  Strongest counterargument: A value-blind cap does not cut the cheapest work. It cuts whatever is
    running when a badly estimated total runs out. LLM agents are shown to underestimate remaining
    cost systematically, so the cap is reached late, and the late work in these runs is the
    expensive, high-value synthesis and reporting. Where agents do pre-select what "fits", the
    scheduling result is that expensive items starve. Either way the cheap items survive and the
    costly deliverable is lost.
  What would need to be true for C2A2 to be safe: Each task declares a cut order and reserves
    budget for its report. Per-item costs are measured, not guessed.
  How to test: Across the last N capped runs, list which items were skipped or truncated and their
    measured token cost. Check whether the skipped set is lower-cost, higher-cost, or last-in-order
    compared with the completed set.
