SEARCH-AGAINST-ASSUMPTION-1175:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1175
  Original statement: "I ran 15a and 15b as **separate agent contexts that could not read each other** — a first for this pipeline, and what REVISE-292 asked for." And, in the same run: "This doesn't resolve REVISE-350 — they still share a model family — but discordance is now visible."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1175
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted a discharged revision flag and the run's own statement of what it left undischarged. [stated]
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive for the 2024-2026 ML literature on correlated LLM error, LLM-as-judge
    self-preference, ensemble independence, and multi-agent debate failure. Queries run via WebSearch
    (LLM-as-judge self-preference / same base model correlated error; multi-agent debate correlated
    failure under shared base model; self-consistency as false independence signal; correlated errors
    under shared pretraining). Bibliographic details then verified directly against arXiv abstract
    pages and the arXiv Atom API. Venues reached: arXiv cs.CL/cs.AI/cs.LG, ICML 2025, ICML MAS
    Workshop 2025, NeurIPS 2024 Safe Generative AI Workshop, ACM Conference on AI and Agentic Systems,
    OpenReview. Date range 2024-2026.
    GAPS: (a) The session WebSearch budget (200 calls) was exhausted partway through this assignment,
    so later queries were run through Crossref/OpenAlex/arXiv/PubMed APIs instead of a general search
    engine; broad grey-literature sweep is therefore incomplete for this item. (b) I found NO study
    that isolates *context isolation* as the independent variable while holding the base model fixed —
    the closest is the isolated-self-correction-vs-debate comparison below, which manipulates
    communication rather than context per se. The specific quantity the assumption needs ("by how much
    does context isolation reduce correlated error at fixed base model?") appears to be unmeasured in
    the published literature. That gap is itself part of the challenge.

  Challenging evidence found: Yes

  Sources:
    1. Kim, E., Garg, A., Peng, K., & Garg, N. 2025. "Correlated Errors in Large Language Models."
       arXiv:2506.07962; accepted to ICML 2025. DOI 10.48550/arXiv.2506.07962. — Large-scale evaluation
       across 350+ LLMs finds substantial error correlation: on one leaderboard dataset models agree
       60% of the time *when both err*. Crucially, "larger and more accurate models have highly
       correlated errors, even with distinct architectures and providers" — so the correlation channel
       is not something two same-family agents can escape by any prompt-level manipulation, and shared
       architecture/provider is identified as an amplifying factor. Demonstrates the effect
       specifically in LLM-as-judge evaluation. ABSTRACT-ONLY (arXiv abstract page fetched directly).
    2. Kuai, C., Jiang, J., Zhu, Z., Wang, H., Wu, K., Li, Z., Zhang, Y., Liu, C., Tu, Z., Fan, Z., &
       Zhou, Y. 2026. "A Statistical Framework for Auditing Behavioral Dependence and Induced Bias in
       LLM Judges." arXiv:2604.07650. — States the exact failure mode the assumption assumes away:
       "Shared pretraining data, distillation, and alignment pipelines can induce hidden behavioral
       dependencies, or latent entanglement, that undermine multi-model systems ... which implicitly
       assume independent signals. In practice, this manifests as correlated reasoning patterns and
       synchronized failures, where apparent agreement reflects shared error modes rather than
       independent validation." Across 18 LLMs from six families they find statistically significant
       entanglement, with their Cumulative Information Gain metric associating with judge-precision
       degradation (Spearman 0.64, p<0.001 for GPT-4o-mini; 0.71, p<0.01 for Llama3-based judges).
       Note the causal channel is *pretraining/alignment*, not context — context isolation cannot
       touch it. ABSTRACT-ONLY (arXiv API).
    3. Denisov-Blanch, Y., Kazdan, J., Chudnovsky, J., Schaeffer, R., Guan, S., Adeshina, S., &
       Koyejo, S. 2026. "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM
       Truthfulness." arXiv:2603.06612. — The strongest single challenge. Across five benchmarks and
       models, polling-style aggregation yields no consistent accuracy gain even at 25x inference cost
       and "often amplifies shared misconceptions"; "models are better at predicting what other models
       will say ... than at identifying what is true"; and correlated outputs persist even when models
       are conditioned on out-of-distribution random strings and asked for pseudo-random output — i.e.
       correlation survives the removal of all shared task content, which is the strongest possible
       demonstration that context isolation is not a decorrelation mechanism. ABSTRACT-ONLY (arXiv API).
    4. Ding, K. 2026. "When LLMs Agree, Are They Right? Auditing Self-Consistency and Cross-Model
       Agreement as Confidence Signals." arXiv:2607.08065 (v2, 28 Jul 2026). — 265,000 samples across
       53 runners on GPQA Diamond and AIME. Agreement is only a weak positive predictor of correctness
       (rho 0.20-0.59) and is *worst* for the most consistent frontier model: agreement >=0.8 on 77% of
       GPQA case-result entries, 48% of those wrong. An exploratory cross-family check on three Claude
       tiers shows the same frontier over-confidence with confident errors recurring across providers.
       Directly challenges the inferential value of the "discordance is now visible" clause: absence of
       discordance carries almost no information at the frontier. ABSTRACT-ONLY (arXiv abstract page).
    5. Bugaud, Z. 2026. "Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model
       Ensembles." arXiv:2603.17111. — Quantifies the collapse of nominal into effective independence:
       across 17 VLMs from 8 families, family-correlated errors "reduce effective ensemble
       dimensionality to 2.5-3.6 independent voters," and create a "Misleading tier" (1.5-6.5% of
       questions) where correlated majority error drives accuracy to 0% despite the best single model
       being correct. If 17 models across 8 families are worth ~3 independent voters, two agents on one
       model family are worth close to one. ABSTRACT-ONLY (arXiv API).
    6. Wataoka, K., Takahashi, T., & Ri, R. 2024 (v2 2025). "Self-Preference Bias in LLM-as-a-Judge."
       arXiv:2410.21819; NeurIPS 2024 Safe Generative AI Workshop. — Identifies the mechanism as
       perplexity-based familiarity: LLMs assign significantly higher evaluations than human evaluators
       to low-perplexity outputs "regardless of whether the outputs were self-generated." This matters
       for the assumption because a familiarity bias keyed to the model's own likelihood function is
       invariant under context isolation — 15a and 15b share the likelihood function. ABSTRACT-ONLY
       (arXiv abstract page).
    7. Wynn, A., Satija, H., & Hadfield, G. 2025. "Talk Isn't Always Cheap: Understanding Failure Modes
       in Multi-Agent Debate." arXiv:2509.05396; ICML MAS Workshop 2025. — Debate can *decrease*
       accuracy over time even when stronger models outnumber weaker ones; models "frequently shift
       from correct to incorrect answers in response to peer reasoning, favoring agreement over
       challenging flawed reasoning." Relevant as the counterfactual: the harm isolation avoids is
       conformity, not correlation. ABSTRACT-ONLY (arXiv API).
    8. Bertalanič, B., & Fortuna, C. 2026. "The Cost of Consensus: Isolated Self-Correction Prevails
       Over Unguided Homogeneous Multi-Agent Debate." arXiv:2605.00914; ACM Conference on AI and
       Agentic Systems. — PARTIALLY SUPPORTIVE of the assumption and included for honesty. Ten
       homogeneous agents over three rounds on GSM-Hard and MMLU-Hard: peer debate produces sycophantic
       conformity (modal adoption up to 85.5%), contextual fragility (vulnerability up to 70.0%) and
       consensus collapse (oracle gap up to 32.3pp), and isolated self-correction beats debate at
       2.1-3.4x lower token cost. So isolation *is* the better of the two designs. But note what is
       measured: isolation prevents contamination between agents; the paper does not claim and does not
       show that isolation reduces the correlation of the agents' independent errors. ABSTRACT-ONLY
       (arXiv API).

  Strength of challenge: Strong

  Summary: The literature converges on a single structural point that runs against the assumption's
    implicit accounting. Correlated error between LLM instances is generated at the level of weights,
    pretraining corpus and alignment pipeline — not at the level of the prompt or the conversation
    context (Kuai et al. 2026; Kim et al. 2025). Denisov-Blanch et al. (2026) show this most sharply:
    correlation persists even when models are conditioned on out-of-distribution random strings, i.e.
    when shared context has been removed by construction. Context isolation therefore removes a
    genuinely harmful channel — mutual contamination, conformity, anchoring, which the debate
    literature shows is severe (Wynn et al. 2025; Bertalanič & Fortuna 2026) — while leaving the
    dominant correlated-error term untouched. The second half of the assumption's claim fares worse
    than the first: "discordance is now visible" presumes that non-discordance is informative, and Ding
    (2026) shows agreement is a weak predictor of correctness that becomes *least* informative exactly
    where confidence is highest (48% of high-agreement GPQA entries wrong). Bugaud (2026) supplies the
    quantitative scale: 17 models across 8 families behave as 2.5-3.6 independent voters, so two
    instances of one model family should be treated as approximately one voter, not two.

  Specific risks: If this claim is false in the direction the literature indicates, then (i) the
    discharge of REVISE-292 bought less than the pipeline recorded — the flag was about correlated
    error, and the implemented remedy addresses a different channel; (ii) every finding on which 15a
    and 15b concurred is at risk of being a shared-prior artefact recorded as independent
    corroboration, which is exactly PRESUMPTION-859's mechanism; (iii) the reliability of C2A2's
    for/against architecture as a whole degrades, because the adversarial split was the main structural
    guard against systematic error; (iv) most concretely, any count of "N corroborating agent runs"
    inside this estate has an effective N far below its nominal N — which is the same defect
    ASSUMPTION-1176 identifies for source counts, from the other end.

  Mitigations available:
    - Cross-family adversarial pairing rather than cross-context pairing. Kim et al. (2025) show error
      correlation is *reduced* (though not eliminated) by differing architecture/provider; Bugaud
      (2026) shows family-aware aggregation recovers +18-26pp on the correlated-majority tier.
    - Report a measured entanglement statistic rather than assuming independence. Kuai et al. (2026)
      give a runnable procedure (Behavioral Entanglement Index; Cumulative Information Gain) and show
      that de-entangled reweighting beats majority voting by up to 4.5%.
    - Stop treating agreement between 15a and 15b as corroboration. Ding (2026) and Denisov-Blanch et
      al. (2026) both recommend demoting consensus from a verification signal to, at most, a graded and
      regime-conditional prior. Record *discordance* as informative and *concordance* as uninformative,
      which is the asymmetric reading the assumption's own wording almost reaches.
    - Retain context isolation. On the evidence of Bertalanič & Fortuna (2026) it is still the right
      design; the correction is to the size of the claim, not the practice.

  STEELMAN:
    Item: ASSUMPTION-1175
    Strongest counterargument: The pipeline discharged a flag whose stated content was "these two
      searchers can read each other," and it did discharge exactly that. What it recorded as remaining
      open — shared model family — is precisely what the literature says is the dominant residual, so
      the run's own bookkeeping is accurate as far as it goes. The error is one of proportion rather
      than of fact: the discharged channel is the smaller one and the undischarged channel is the
      larger one, and the write-up's framing ("a first for this pipeline," "discordance is now
      visible") assigns the emphasis the other way round. The literature adds one thing the run did not
      know: correlated error survives even the total removal of shared context (Denisov-Blanch et al.
      2026), which means isolation's contribution to decorrelation is not merely partial but close to
      nil, and the residual risk should be re-rated from "an adjacent open flag" to "the whole of the
      original problem."
    What would need to be true for C2A2 to be safe: (a) the pipeline's substantive claims rest on
      documented external sources rather than on agent agreement, so that concordance between 15a and
      15b is treated as a routing convenience rather than as evidence; (b) discordance, not
      concordance, is what triggers escalation — an asymmetry that remains valid even when agents are
      maximally correlated, since correlated agents that nonetheless disagree have found something real;
      (c) any gate expressed as a count of agreeing runs is either removed or discounted by a measured
      entanglement factor. Under (a)-(c) the shared base model degrades sensitivity but does not
      manufacture false positives.
    How to test: Directly and cheaply within this estate. Take a stratified sample of items already
      processed by both 15a and 15b. Re-run 15b's assignment (i) at a different temperature on the same
      model, (ii) on a different model family, and (iii) with a deliberately reordered/perturbed brief.
      Compute pairwise error agreement against a human-adjudicated ground truth for each condition.
      Kim et al.'s "agreement rate conditional on both being wrong" is the right statistic. If
      same-family cross-context agreement-on-error is close to same-family same-context
      agreement-on-error, and both substantially exceed cross-family agreement-on-error, the assumption
      is falsified as stated and the effective-N of the 15a/15b pair can be estimated from the gap.
      Kuai et al. (2026) provide the entanglement metrics; Bugaud (2026) provides the
      effective-dimensionality framing.

  Recommendation: CHALLENGED
