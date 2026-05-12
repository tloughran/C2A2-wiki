SEARCH-AGAINST-ASSUMPTION-034:
  Date searched: 2026-04-17
  Original item: ASSUMPTION-034
  Original statement: "The default regenerator model should be upgraded from claude-opus-4-6 to claude-opus-4-7"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-034
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — stated model-default change
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Sculley et al. (2015) "Hidden Technical Debt in Machine Learning Systems" — "swap-in" model upgrades without regression testing are a documented source of silent-failure technical debt.
    2. Bommasani et al. (2021) "On the Opportunities and Risks of Foundation Models" — successive foundation-model versions show non-monotonic task-level performance: improvements on benchmarks do not guarantee improvements on narrow downstream use cases.
    3. Chen et al. (2024) empirical studies on GPT-3.5 → GPT-4 and similar transitions — show both regressions (on formatting, style consistency, stable-latent narrative coherence) and improvements, depending on task; blanket upgrade = defensible only with task-specific regression test.
    4. Narrator-consistency / style-stability literature (Chung et al. 2022): model transitions can disrupt learned prompt/output conventions, especially for style-dependent generation.

  Strength of challenge: Moderate

  Summary: The literature challenges "newer = better" as a blanket upgrade rationale. Successive foundation-model versions exhibit non-monotonic task-level behavior, particularly for style-consistent and narrator-style generation tasks. Upgrade without documented rationale and without a regression check against the prior output corpus is a well-documented technical-debt pattern. The narrator task specifically (generating consistent-voice wiki narrations) is exactly the class most sensitive to model transitions.

  Specific risks: Narrator-voice drift (wiki_narration output character shifts post-upgrade); regression on specific idioms/conventions the prior corpus encoded; silent hallucination-profile changes (different failure modes, not necessarily fewer); breaking of prompts tuned to 4-6's quirks.

  Mitigations available:
    - Hold current default until a regression test against the 2026-04-15 corpus passes
    - A/B comparison on a held-out subset
    - Document rationale before change (what problem does the upgrade solve?)
    - Staged rollout with rollback switch

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-034
    Strongest counterargument: Blanket model upgrades without regression testing are the documented anti-pattern in ML systems engineering. Even minor-version model transitions regularly introduce task-specific regressions, especially for style-sensitive generation like narrator voice. The upgrade's rationale is unstated; without a stated problem being solved, the upgrade is a speculative change with asymmetric downside risk. "The new model is available" is not a rationale; regression test + documented rationale is the literature-supported bar.
    What would need to be true for C2A2 to be safe: Regression test against the 2026-04-15 narration corpus shows no quality regression; documented rationale for the change exists; rollback path is tested.
    How to test: Execute a regression test post-billing-clearance; compare outputs on a fixed prompt set.
