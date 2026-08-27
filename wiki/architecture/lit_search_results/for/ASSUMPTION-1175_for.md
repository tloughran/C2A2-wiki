SEARCH-FOR-ASSUMPTION-1175:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1175
  Original statement: "Context isolation between adversarial searchers as a remedy for correlated error. The pipeline ran 15a and 15b as separate contexts that could not read each other, discharging REVISE-292, and stated that REVISE-350 remains open because they share a model family. Search: does isolating context between adversarial LLM agents reduce correlated error when the base model is shared, and by how much?"
    (Bears directly on MONITOR-001, open since 2026-04-13. Priority: HIGH.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1175
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Second-run extraction of the pipeline's own remedy claim for correlated error
        between adversarial searchers, with the shared-model residual (REVISE-350) noted
        as unresolved.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web search plus full-text fetch of three arXiv papers, 2026-08-25. Queries
    run: (1) correlated errors in LLM ensembles sharing a base model, self-consistency,
    multi-agent debate diversity, effect sizes; (2) LLM-as-judge self-preference bias,
    homogeneous vs heterogeneous debate; (3) multi-agent conformity and peer pressure,
    independent vs shared-context aggregation; (4) "Correlated Errors in Large Language
    Models" specifics; (5) independent parallel sampling vs shared-context agents,
    algorithmic monoculture; (6) attribution check on the same-model/cross-model correlation
    figures; (7) human analogue — blinded independent duplicate review. Full text read:
    arXiv:2605.00914v1 (abstract), arXiv:2605.08478v1 (abstract), arXiv:2101.02701 (full
    paper). Venues reached: arXiv (cs.MA, cs.LG, cs.CL, cs.CR), ICML 2025 proceedings
    listing, Springer/J King Saud Univ, PMC, Journal of Clinical Epidemiology listings.
    Status: COMPREHENSIVE for the general "shared context correlates error / isolation
    avoids it" question and for the shared-base-model correlation floor; PRELIMINARY for the
    specific adversarial (for/against) configuration — broader search recommended.
    Gaps: several key figures are search-snippet-only and their primary sources were not
    fetched (arXiv:2606.26583, arXiv:2506.07962, arXiv:2605.00844); author lists for those
    three are unverified. Session web-search budget exhausted before follow-up.

  Supporting evidence found: Yes

  Sources:
    1. Bertalanič, B. & Fortuna, C., 2026. "The Cost of Consensus: Isolated Self-Correction
       Prevails Over Unguided Homogeneous Multi-Agent Debate." arXiv:2605.00914v1 [cs.MA],
       29 Apr 2026. https://arxiv.org/html/2605.00914v1 — The most directly on-point source.
       Controlled study, N=10 homogeneous agents (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B),
       R=3 debate rounds, GSM-Hard and MMLU-Hard, comparing peer debate against **isolated
       self-correction** and a stochastic noise control. Reported effect sizes for the
       damage done by shared context: sycophantic conformity, modal adoption **up to 85.5%**;
       contextual fragility, where peer rationales destabilise previously correct reasoning,
       vulnerability rate **up to 70.0%**; consensus collapse, where plurality voting discards
       correct answers already present in the pool, oracle gap **up to 32.3 percentage
       points**. Debate consumed **2.1–3.4× more tokens** (up to 28,631 per problem) "for
       equal or lower accuracy." Conformity reached high levels at minimal peer exposure
       (K=2) and *intensified with greater initial diversity*. Conclusion: within the 7–8B
       class, homogeneous teams without structured roles do not benefit from unguided peer
       exchange, and isolated self-correction offers a more favourable cost-accuracy
       tradeoff. (read in full: abstract)
    2. "Preference Optimization Drives Monoculture in LLM Prediction Markets."
       arXiv:2606.26583 [authors unverified]. — Supplies the quantitative answer to the
       "by how much" question on the shared-model residual. Same-model agents show pairwise
       error correlation **ρ = 0.679 (±0.023)**; cross-model agents **ρ = 0.396 (±0.011)**.
       Ten same-model honest agents contribute the forecasting power of only **≈1.4
       independent forecasters**; a 10-agent same-model market reaches **67.6%** accuracy
       against **70.2%** for a single standalone agent. Cross-model diversity was the
       largest-effect mitigation tested (ρ 0.68 → 0.40); DPO fine-tuning is isolated as the
       causal driver (Δρ = +0.24 to +0.46 on identical-SFT controls at 8B and 70B), and
       N_eff stays flat from N=5 to N=40. (search-snippet-only — primary not fetched;
       figures should be verified before being quoted downstream)
    3. Kim, E., Garg, et al., 2025. "Correlated Errors in Large Language Models." ICML 2025;
       arXiv:2506.07962. https://icml.cc/virtual/2025/poster/44225 — Establishes the floor
       that context isolation cannot cross. Large-scale evaluation across 350+ LLMs on two
       leaderboards and a resume-screening task: on one leaderboard dataset **models agree
       60% of the time when both models err**; correlation is driven by shared architectures
       and providers, and "larger and more accurate models have highly correlated errors,
       even with distinct architectures and providers." Downstream effects demonstrated for
       LLM-as-judge evaluation. (search-snippet-only)
    4. Dong, Y. & Shigida, B., 2026. "When Independent Sampling Outperforms Agentic
       Reasoning." arXiv:2605.08478v1 [cs.LG], 08 May 2026.
       https://arxiv.org/html/2605.08478 — Independent generalisation of the same finding on
       a different task family: across 216 Codeforces problems, Divisions 1–3, repeated
       **independent** k-shot sampling consistently beat agent-based (context-accumulating)
       reasoning on both accuracy-cost and accuracy-query tradeoffs, and the gap persisted
       despite prompt caching. (read in full: abstract)
    5. "The Oracle's Fingerprint: Correlated AI Forecasting Errors and the Limits of Bias
       Transmission." arXiv:2605.00844 [authors unverified]. — Bounds the achievable
       decorrelation even across vendors: GPT-4o, Claude and Gemini showed mean pairwise
       error correlation **r = 0.78** on 568 resolved binary prediction questions despite
       independent development. (search-snippet-only)
    6. "LLMs Can't Handle Peer Pressure: Crumbling under Multi-Agent Social Interactions."
       arXiv:2508.18321; and "Easier to Mislead Than to Correct: Harmful and Beneficial
       Revision in LLM Conformity." arXiv:2606.01637; and "Do as We Do, Not as You Think: the
       Conformity of Large Language Models." arXiv:2501.13381 [authors unverified for all
       three]. — Converging mechanism evidence: models abandon their own correct answer
       because others agree on a different one; wrong answers propagate through a shared
       context more readily than correct peer answers repair prior mistakes; a single flawed
       response can propagate across agents and compromise the whole framework. This is the
       specific harm that context isolation forecloses. (search-snippet-only)
    7. Sun, M., Danfa, J. B. & Teplitskiy, M. "Does double-blind peer review reduce bias?
       Evidence from a top computer science conference." arXiv:2101.02701. — The human
       analogue, and methodologically the cleanest natural experiment available: ICLR's
       2018 switch from single-blind to double-blind review, 5,027 papers. Masking the shared
       identity cue **increased inter-reviewer standard deviation** (Fig. 1D — i.e. it
       decorrelated judgments) across high- and medium-prestige groups, and **improved
       decision quality**: papers rejected under double-blind drew significantly lower
       2-year citations than those rejected under single-blind (p=0.0016), an effect
       strongest for the papers most effectively anonymised (p=4.4×10⁻¹¹). The authors'
       interpretation is directly the one at issue: removing a shared cue reduces precision
       but improves accuracy, because the lost precision was correlated bias.
       (read in full)
    8. "When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning."
       arXiv:2510.07517 [authors unverified]. — Applies the same anonymisation logic inside
       multi-agent LLM reasoning. (search-snippet-only)

  Strength of support: Moderate

  Summary: The claim that context isolation reduces correlated error between LLM agents is
    well supported, and the direction is consistent across task families, model scales and
    the human analogue. The strongest single result is Bertalanič & Fortuna's controlled
    comparison of isolated self-correction against unguided homogeneous debate, where shared
    context produced sycophantic modal adoption up to 85.5%, destabilised previously correct
    reasoning at rates up to 70.0%, and discarded correct answers already present in the
    pool by up to 32.3 percentage points — while costing 2.1–3.4× more tokens for equal or
    lower accuracy. Dong & Shigida reproduce the ranking on competitive programming, and Sun
    et al.'s ICLR natural experiment shows the same signature in humans: masking a shared
    cue raised disagreement and improved decision accuracy. On "by how much," the honest
    answer is that the literature quantifies two different things. Shared *context* is worth
    a large, task-dependent margin, plausibly tens of percentage points on the failure
    modes measured. Shared *base model* imposes a floor that isolation cannot touch:
    same-model pairwise error correlation of ρ ≈ 0.68 against ρ ≈ 0.40 cross-model, with ten
    same-model agents worth only about 1.4 independent ones. Isolation removes the
    conversational contamination; it does not remove the monoculture.

  Caveats:
    - The pipeline's own framing is the right one and the literature confirms it: context
      isolation and model diversity are separable remedies for separable components of
      correlated error. REVISE-292 (context contamination) is genuinely addressable by
      isolation; REVISE-350 (shared model family) is not, and the same-model floor of
      ρ ≈ 0.68 is the quantity that should be carried forward against MONITOR-001.
    - Bertalanič & Fortuna's models are 7–8B parameter class and their own scope statement
      is explicitly limited to that class; they include a "Scaling to Larger Models" appendix
      I did not read. Their finding is also specific to *unguided homogeneous* debate without
      structured roles. An adversarial for/against assignment IS a structured role
      differentiation, so their result may understate what a role-differentiated shared-context
      design achieves — this cuts against transferring their headline to this pipeline
      unmodified.
    - Their finding that conformity "intensifies with greater initial diversity" is
      counterintuitive and, if it generalises, means the benefit of isolation grows precisely
      in the adversarial case where the two agents are expected to diverge.
    - Effect sizes here are almost all measured as *accuracy* or *conformity rate*, not as
      error correlation ρ before and after context isolation. I found no study that measures
      pairwise error correlation between two same-base-model agents with and without shared
      context, holding the task fixed. The "by how much" question as posed is therefore
      answered only indirectly.
    - Three of the numeric sources (arXiv:2606.26583, arXiv:2506.07962, arXiv:2605.00844)
      are search-snippet-only with unverified author lists. The ρ = 0.679 / 0.396 pair in
      particular should be verified against the primary before it is quoted in the register.
    - Sun et al. is a human peer-review natural experiment; its transfer to LLM agents is by
      analogy, and the authors themselves note they cannot rule out that the policy change
      altered the submission pool.
    - Task-domain gap: all the LLM evidence is on verifiable-answer tasks (maths, MCQ,
      competitive programming, binary forecasting). This pipeline's task is open-ended
      literature assessment with no ground truth, where "correlated error" is much harder to
      measure and where the conformity failure modes may express differently.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1175, adversarial-configuration limb.
    Searched: seven queries across multi-agent LLM, ensembling, algorithmic-monoculture and
      LLM-as-judge literature for a measurement of error correlation between context-isolated
      versus context-sharing agents that share a base model and are assigned *opposed*
      (for/against, prosecution/defence) roles.
    Finding: no such measurement located. The literature measures (a) isolated
      self-correction vs. cooperative debate among same-role homogeneous agents, and
      (b) same-model vs. cross-model error correlation among independent agents. Nothing
      found isolates the interaction of the two — role opposition × context isolation ×
      shared base model — nor reports a ρ delta attributable to context isolation alone.
    Unaddressed sub-claim, precisely: "for two agents sharing a base model and assigned
      deliberately opposed roles, isolating their contexts reduces pairwise error correlation
      by a measurable amount X, over and above the reduction attributable to role opposition
      itself."
    Implication: the direction of the pipeline's remedy is supported; its magnitude is not
      established, and the residual attributable to shared model family (ρ ≈ 0.68 same-model
      vs ≈ 0.40 cross-model) is the better-evidenced quantity. MONITOR-001 should be updated
      with the floor figure rather than with a claimed reduction. Measuring the delta
      directly in-pipeline would be genuinely new ground.
    Recommended status: NOVEL (adversarial-configuration limb only).
