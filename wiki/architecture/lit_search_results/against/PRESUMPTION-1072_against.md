SEARCH-AGAINST-PRESUMPTION-1072:
  Date searched: 2026-09-23
  Original item: PRESUMPTION-1072
  Original statement: Parallel same-model agents with separate contexts show error correlation
    comparable to a single agent when prompt wording and tools are shared.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1072
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by checking the fix claim against the premise register.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (the direction is strongly corroborated; only the
      strength implied by "comparable to a single agent" is challenged)

  Direction note: For this item a "challenge" means evidence that same-model parallel agents
  ARE meaningfully decorrelated. Most of what the search found runs the other way, and this is
  stated plainly below. It is the mirror image of ASSUMPTION-1624, which was CHALLENGED by the
  same literature.

  Challenging evidence found: Partial

  Sources (challenging):
    1. Wang, X., Wei, J., Schuurmans, D., Le, Q., Chi, E., Narang, S., Chowdhery, A., & Zhou, D.
       (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." ICLR
       2023. Sampling several reasoning paths from one model with one prompt and taking the
       majority answer raises accuracy "with a striking margin" on arithmetic reasoning.
       Majority voting can only help if sampled errors are not perfectly correlated. So
       same-model, same-prompt runs are measurably less correlated than a single greedy run.
    2. Du, Y., Li, S., Torralba, A., Tenenbaum, J.B., & Mordatch, I. (2024). "Improving
       Factuality and Reasoning in Language Models through Multiagent Debate." ICML 2024, PMLR
       v235. Several instances of the same model debating improve reasoning and reduce
       hallucination compared with one instance. This is evidence that same-model instances in
       separate contexts carry some independent error signal.

  Sources (corroborating, reported for completeness):
    3. Kim et al. (2025). "Correlated Errors in Large Language Models." ICML 2025 (PMLR v267;
       arXiv:2506.07962). Error agreement is highest within a model family, reaching 0.97 for
       one related pair.
    4. Zhang, H. et al. (2025). "Stop Overvaluing Multi-Agent Debate." arXiv:2502.08788.
       Same-model debate often fails to beat single-agent Self-Consistency; model heterogeneity
       is the reliable fix.
    5. "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness."
       arXiv:2603.06612 (2026). Changing temperature flipped the plurality answer in only 2.9%
       of cases, and wrong answers stayed highly concentrated.

  Strength of challenge: Weak

  Summary: The literature supports the presumption's direction: same-model agents are highly
  error-correlated, and homogeneous multi-agent setups add little beyond resampling. The only
  challenge is to the word "comparable." Self-consistency and same-model debate produce
  reproducible accuracy gains, so parallel same-model runs are not as correlated as one agent
  run once, where the correlation is 1 by definition. The gains are real but modest, and
  Zhang et al. show they are often matched by plain resampling. The fair reading is "highly
  correlated, somewhat less than a single agent." The evidence also comes from closed-answer
  benchmarks, not from open-ended literature search, so it may not transfer.

  Specific risks: If C2A2 takes the presumption at full strength ("no better than one agent"),
  it may dismiss the 15a/15b split as worthless when it does provide some decorrelation. The
  larger risk runs the other way (see ASSUMPTION-1624): treating the split as independent.

  Mitigations available: Same as ASSUMPTION-1624. Measure the overlap between the two sides
  directly instead of presuming it, and introduce model or backend heterogeneity for one side.

  Search scope: Moderate — shares the search set of ASSUMPTION-1624 (6 searches, 2 fetches),
  with 2 searches aimed at the challenge direction (self-consistency and same-model debate).

  Excluded results: dev.to persona-diversity blog post (title echoes the claim's framing; no
  venue); emergentmind and Lacuna aggregator pages; GitHub repository for the Du et al. code
  (the paper itself is cited instead).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1072
  Strongest counterargument: (This is the strongest form of the challenge.) Self-consistency
    works. If same-model, same-prompt samples really had error correlation comparable to a
    single agent, majority voting over them could not raise accuracy, yet it reliably does
    across benchmarks and model sizes. Separate contexts add further path divergence: each
    agent's early tool results condition its later queries, so small initial differences
    compound over a multi-step search. For agentic, multi-turn tasks, as opposed to single
    closed-form answers, the trajectories of same-model agents can diverge substantially even
    when prompts are identical.
  What would need to be true for the presumption to hold anyway: The residual decorrelation
    from sampling is small compared with the shared blind spots, which is what Kim et al. and
    arXiv:2603.06612 suggest for closed questions. In search tasks, the dominant errors are
    errors of omission tied to shared query habits, which sampling does not diversify.
  How to test: Run 15b k times on the same item with fresh contexts. Measure how often each
  source appears across runs and how unique the queries are. If k runs converge on
  near-identical source sets, the presumption holds for this task type. If each run adds
  distinct sources, the challenge holds.
