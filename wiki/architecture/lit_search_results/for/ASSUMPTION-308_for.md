SEARCH-FOR-ASSUMPTION-308:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-308
  Original statement: A deterministic scheduler should precede any bandit layer in agent-activity optimization.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-308
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption from architecture work log (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. Silva, N. et al., 2022. "User Cold-start Problem in Multi-armed Bandits: When the First Recommendations Guide the User's Experience." ACM Transactions on Recommender Systems. — In cold-start (new system/user, tiny N), simple non-personalized deterministic policies often outperform bandit exploration; early exploratory choices carry outsized downstream cost.
    2. Felicio, C. et al., 2017. "A Multi-Armed Bandit Model Selection for Cold-Start User Recommendation." UMAP 2017. — Benchmarks ε-greedy/UCB/Thompson against Random and Popular baselines, finding simple baselines competitive or superior until sufficient observations accumulate.
    3. Lattimore, T. & Szepesvári, C., 2020. "Bandit Algorithms." Cambridge University Press. — Standard regret theory: bandit advantage over a fixed policy accrues asymptotically; at small horizon T with few arms' pulls each, exploration overhead dominates and regret bounds are vacuous — theoretical grounding for deterministic-first.
  Strength of support: Moderate
  Summary: Both theory and empirical recommender-systems literature support installing a deterministic policy before an adaptive bandit layer. Regret analysis shows bandit benefit is asymptotic — with few rounds, exploration cost exceeds its value and a sensible fixed policy is near-optimal. Cold-start studies repeatedly find simple deterministic baselines (popularity, round-robin, fixed priority) competitive with or better than bandits at small N, and a deterministic baseline is additionally required to even evaluate whether a later bandit layer helps (counterfactual comparison). Non-stationarity of agent-activity reward (which is likely here) further weakens naive bandits, strengthening the staged approach.
  Caveats: "Should precede" is supported as engineering sequence, not as permanent architecture — the same literature shows bandits win once observation counts grow, so the deterministic layer needs an explicit graduation criterion. If the deterministic schedule systematically starves some activities, it biases the data the future bandit will learn from (logged-bandit feedback bias).
  Search scope: 1 WebSearch ("simple deterministic baseline before multi-armed bandit exploration overhead small sample cold start scheduling"); plus standard bandit-theory references.
  Recommendation: SUPPORTED
