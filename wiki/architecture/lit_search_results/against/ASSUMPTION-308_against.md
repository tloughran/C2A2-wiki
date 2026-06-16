SEARCH-AGAINST-ASSUMPTION-308:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-308
  Original statement: A deterministic scheduler should precede any bandit layer in agent-activity optimization.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-308
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (sequencing claim: deterministic before adaptive)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. Li, Chu, Langford & Wang, 2011. "Unbiased Offline Evaluation of Contextual-Bandit-Based News Article Recommendation Algorithms." WSDM. — Offline evaluation/training of a future bandit requires randomized logging with known propensities; a purely deterministic scheduling phase produces confounded logs that cannot later validate or warm-start the bandit, so "deterministic first" can actively delay the adaptive layer it is supposed to precede.
    2. Kuleshov & Precup, 2014. "Algorithms for multi-armed bandit problems." arXiv:1402.6028. — Simple bandit heuristics (ε-greedy, Boltzmann) are cheap, dominate at short horizons, and carry negligible implementation overhead — undercutting the premise that adaptivity is a heavyweight layer needing a deterministic predecessor.
    3. Bayati, Hamidi, Johari & Khosravi, 2020. "Unreasonable Effectiveness of Greedy Algorithms in Multi-Armed Bandit with Many Arms." NeurIPS. — At small N/many-arms regimes the practical gap between principled exploration and naive policies is small; the choice is less consequential than the sequencing debate implies, in either direction.
  Strength of challenge: Moderate (note: substantial literature also SUPPORTS the assumption — simple/deterministic baselines beat bandits at short horizons; the challenge is narrower than full contradiction)
  Summary: The strongest documented challenge is the logging-confound argument: if the deterministic phase is also the data-collection phase, its logs lack the randomization needed for unbiased off-policy evaluation, so the bandit layer cannot be validated against history when it arrives — the sequencing creates the very cold-start it was meant to avoid. Second, an ε-greedy layer is ~10 lines and degrades gracefully to near-deterministic behavior at small ε, so the framing of bandits as a later "layer" overstates their cost; a thin randomized component inside the deterministic scheduler captures most future option value. Third, deterministic schedules in non-stationary agent workloads can lock in allocations that look fine and are never tested against alternatives, an invisible-regret failure mode. None of this shows the sequencing is wrong for C2A2's tiny N; it shows the pure form (zero randomization first) is the weakest version of it.
  Specific risks: When the bandit layer arrives, no usable training/evaluation data exists (all logs confounded by the deterministic policy); meanwhile the deterministic schedule may carry sustained unmeasured regret on task-mix allocation; the "later" layer is deferred indefinitely because the migration cost grows.
  Mitigations available: Run deterministic-with-ε: keep the deterministic schedule but add small-probability randomized deviations and log propensities, preserving future off-policy evaluability; predefine the trigger condition (N of scheduling decisions, or measured regret bound) at which the bandit layer activates; keep per-decision reward logging from day one.
  STEELMAN:
    Strongest counterargument: At C2A2's scale (one human, a handful of agent activities, noisy delayed rewards via PRS), bandit machinery optimizes a reward signal that does not yet exist in trustworthy form (see ASSUMPTION-307/PRESUMPTION-339 challenges); adding exploration on top of an invalid reward metric automates Goodhart. A deterministic, inspectable schedule preserves human accountability and produces interpretable baselines — the literature (Kuleshov & Precup) itself shows naive policies are near-optimal at short horizons, so the cost of deferring adaptivity is tiny while the cost of premature optimization against a bad proxy is large.
    What would need to be true for C2A2 to be safe: Reward signal (PRS completion) matures before the bandit activates; decision logs with timestamps/outcomes are kept from the start; the deterministic phase has an explicit exit condition rather than indefinite tenure.
    How to test: After 4-6 weeks, attempt an off-policy estimate of one alternative schedule from the logs; if the estimate is undefined for lack of overlap, the confound risk is confirmed.
  Search scope: 1 WebSearch ("multi-armed bandit vs simple baseline heuristic small sample exploration overhead when bandits underperform round-robin"); plus off-policy evaluation literature.
  Recommendation: PARTIALLY-CHALLENGED
