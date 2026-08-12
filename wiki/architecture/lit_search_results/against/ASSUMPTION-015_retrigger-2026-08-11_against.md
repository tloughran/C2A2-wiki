SEARCH-AGAINST-ASSUMPTION-015:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-015
  Original statement: "Running a potentially biased pipeline (FOR/AGAINST search) is better than not running one at all."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: ASSUMPTION-015
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from lit-search pipeline session 2026-04-13, where the pipeline acknowledged structural bias but continued operating
      15b (cycle 1, 2026-04): initial challenging search — anchoring bias, epistemic pollution, confirmation-bias cascade
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: CHALLENGED

  Search scope: Comprehensive for the LLM-pipeline angle, which is where the field moved. Covered (a) anchoring in chained LLM pipelines, (b) role-assignment fidelity and drift in adversarial multi-agent debate, (c) identity/peer bias in debate, (d) LLM cognitive-bias benchmarks 2026, (e) classical anchoring/epistemic-pollution baseline from cycle 1. Not covered: formal decision-theoretic treatments of "biased signal better than no signal" (value-of-information under known bias) — preliminary, broader search recommended on that specific sub-question.

  Challenging evidence found: Yes

  Sources:
    1. Zylos Research, 2026-06-29. "Anchoring and Contamination in Chained LLM Pipelines: How Upstream Scores Corrupt Downstream Reasoning." — Directly on point and new. Upstream stage outputs establish reference points that distort downstream reasoning AND downstream human review; contamination is described as "the default behavior of a naively designed pipeline," requiring no intentional manipulation. C2A2's 14a→15a/15b→15c→15d chain is precisely such a pipeline.
    2. "When Roles Fail: Epistemic Constraints on Advocate Role Fidelity in LLM-Based Political Statement Analysis." arXiv:2604.27228 (2026). — Measures Role Drift Index, Expected Drift Distance, Directional Drift Index and Entropy-based Role Stability for LLMs assigned adversarial advocate roles. Finds the core assumption — that models reliably maintain assigned adversarial roles — does not hold. This challenges the pipeline at a deeper level than cycle 1 did: the FOR/AGAINST split may not even produce the bias it was designed to produce, in a stable direction.
    3. "Understanding the Anchoring Effect of LLMs." ICLR HCAIR Workshop 2026 / arXiv:2505.15392. — LLMs exhibit anchoring at magnitudes comparable to or greater than humans; critically, "estimate-first" prompting (the intuitive debias) can *increase* bias in some models. Prompt-level anti-anchoring instructions are unreliable; structural mitigation is required.
    4. "Localizing Anchoring Pathways in Language Models." arXiv:2606.12818 (June 2026). — Mechanistic localisation of anchoring circuits; conventional mitigation methods shown ineffective. Removes the "we told the agent to be unbiased" defence.
    5. "Contextual Drag: How Errors in the Context Affect LLM Reasoning." arXiv:2602.04288 (2026). — Errors present in context degrade downstream reasoning even when the model is not asked to rely on them. A flawed cycle-1 result sitting in a cycle-5 agent's context is an active harm, not inert.
    6. "When Two LLMs Debate, Both Think They'll Win." arXiv:2505.19184. — Adversarially-assigned LLM debaters hold systematically miscalibrated confidence in their own side. A FOR agent and an AGAINST agent will both over-certify their own outputs, so downstream reconciliation (15c/15d) inherits two overconfident inputs rather than one balanced one.
    7. "When Identity Skews Debate: Anonymization for Bias-Reduced Multi-Agent Reasoning." arXiv:2510.07517. — Debate agents are influenced by *who* produced a response, not only what it says. In C2A2, 15c/15d see labelled FOR and AGAINST outputs; the labels themselves bias reconciliation.
    8. "CogBias: Measuring and Mitigating Cognitive Bias in Large Language Models." arXiv:2604.01366 (2026). — Broad benchmark confirming persistent, hard-to-remove cognitive biases across model families.
    9. Cycle-1 baseline retained: anchoring persists with implausible anchors (J. Comput. Soc. Sci. 2021); anchoring cascades across unrelated dimensions (PMC 2024); "epistemic pollution" (Levy, Bad Beliefs); anchoring vs confirmation bias in diagnostic vignettes (Front. Public Health 2026).

  Strength of challenge: Strong

  NEW SINCE LAST CYCLE: Yes — substantially. Six new sources: Zylos (Jun 2026), arXiv:2604.27228, arXiv:2606.12818 (Jun 2026), arXiv:2602.04288 (Feb 2026), arXiv:2604.01366 (Apr 2026), plus arXiv:2505.19184 and arXiv:2510.07517 now clearly in scope. What they add: April 2026's challenge was analogical — it borrowed human anchoring research and argued it should apply. The 2026 literature makes the argument directly about chained LLM pipelines with assigned adversarial roles, i.e. about C2A2's exact architecture. Two findings are genuinely new in kind: (i) role fidelity itself is unstable, so the FOR/AGAINST design does not reliably deliver the balanced bias it assumes; (ii) prompt-level debiasing is not merely weak but sometimes counterproductive, so the standard mitigation is unavailable.

  Evidence trajectory (challenging): growing

  Summary: This item has moved from "argued by analogy" to "directly measured" in four months. The 2026 pipeline-anchoring literature describes contamination as the default behaviour of naively chained LLM stages, which is what C2A2 runs. The role-fidelity work is the more damaging addition: it undermines the assumption's own logic, since the claimed benefit of a "potentially biased" pipeline rests on the biases being known, opposed and therefore cancellable — and role drift means they are none of those things. Prompt-level mitigations are now shown to be ineffective or counterproductive, leaving only structural fixes. The assumption is not refuted outright — a biased pipeline may still beat nothing — but the specific reason to believe it (opposed biases cancel) is no longer supported.

  Specific risks: If false, the entire C2A2 evidence base is contaminated rather than merely noisy, and contaminated in a way that is invisible: outputs look like balanced adjudication while actually being anchored on whichever upstream stage spoke first. Because the pipeline has now run five cycles, contamination compounds — cycle-5 agents read cycle-1 conclusions as context (documented harm per arXiv:2602.04288). Worse, a contaminated pipeline that *feels* rigorous produces false confidence and crowds out the genuine external validation that would catch the problem. Retraction cost scales with cycle count and is already high.

  Mitigations available: (a) Blind 15c/15d to the FOR/AGAINST provenance labels (per arXiv:2510.07517) — cheap, structural, testable; (b) run FOR and AGAINST from independent context with no shared upstream text; (c) side-swap — re-run the same item with roles reversed and compare, as in the lechmazur/debate side-swapped protocol; (d) measure role drift explicitly using RDI/ERS from arXiv:2604.27228 rather than assuming role fidelity; (e) require at least one non-LLM evidence path (direct source reading) per high-stakes item; (f) stop feeding prior-cycle conclusions into re-trigger prompts — feed only the item statement.

  STEELMAN:
    Strongest counterargument: The alternative to a biased pipeline is not an unbiased pipeline; it is no pipeline at all, i.e. unexamined assumptions carried forward silently. A pipeline with known and documented bias is strictly more auditable than tacit belief, because the bias is at least located and named — which is exactly what this document does. Value-of-information arguments favour a noisy signal over no signal whenever the noise is not adversarially correlated with the truth, and there is no evidence here that FOR/AGAINST role assignment produces anti-correlated error. The anchoring literature shows contamination is real but does not show that the contaminated output is *worse than the prior*, which is the actual comparison the assumption makes.
    What would need to be true for C2A2 to be safe: (1) Pipeline errors are not systematically correlated with the conclusions the project wants to reach — the one condition that would make the noisy signal worse than nothing; (2) role drift is bounded and measured, not assumed; (3) contaminated conclusions are marked and revisable, so downstream artefacts do not harden around them; (4) at least one evidence channel is independent of the LLM chain.
    How to test: Side-swap trial. Select 10 completed items, re-run with FOR/AGAINST role labels swapped and with 15c/15d blinded to provenance. If final recommendations flip on more than a small fraction, the pipeline is measuring role assignment rather than evidence. Additionally, seed 3 fabricated "control" claims into a cycle and check whether the pipeline reliably returns CHALLENGED for them — a pipeline that cannot fail a fake claim is not producing information.

  Recommendation: CHALLENGED
