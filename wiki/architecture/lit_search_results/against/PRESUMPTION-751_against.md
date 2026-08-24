SEARCH-AGAINST-PRESUMPTION-751:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-751
  Original statement: Whether agreement between two same-model readers is evidence about the world or about the model. Risk: Critical.

  Reading challenged: The operative (reassuring) reading — that concordance between two readers drawn from the same model family carries evidential weight about the object being read. This search attacks that reading.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-751
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from operational review; queued as literature-testable.
      15b: Searched for challenging literature; found direct, quantified empirical evidence that same-family LLM agreement is largely correlated error and carries near-zero incremental information.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kim, E., Garg, A., Peng, K., & Garg, N. (2025). "Correlated Errors in Large Language Models." ICML 2025; arXiv:2506.07962. — Empirical evaluation over 350+ LLMs on two leaderboards and a resume-screening task. On one leaderboard dataset, when two models both err they land on the *same* wrong answer 60% of the time. Error correlation is *higher* for larger and more accurate models, and higher still for shared architecture/provider. Directly contradicts the presumption's reassuring reading: agreement concentrates precisely where the pipeline most wants to trust it, and same-provenance readers are the worst case, not the neutral case. [VERIFIED — arXiv abstract page, ICML 2025 acceptance noted.]
    2. Kohli, G. (2026). "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels." arXiv:2605.29800. — Panel of 9 frontier LLMs from 7 *different* model families yields only ~2 independent votes' worth of information (Kish effective sample size). ~75% of nominal independence lost to shared mistakes on shared items. Panel accuracy falls 8–22 percentage points short of the independent-voting ideal; the best single judge matches or beats the full panel in every condition; aggregation algorithms close at most 11% of the gap even given the correct answers. Robust across prompt variants, temperature, chain-of-thought, and a pairwise-preference task. If seven *distinct families* collapse to n_eff≈2, two readers from the *same* model plausibly collapse to n_eff≈1. [VERIFIED — arXiv abstract page.]
    3. Berg, S. (1993). "Condorcet's jury theorem, dependency among jurors." Social Choice and Welfare 10(1), 87–95. — Formal result: positive intra-voter correlation *decreases* jury competence; only negative correlation improves it. Establishes that the theoretical warrant for treating concordance as confirmatory requires (conditional) independence, which same-model readers by construction do not have. [VERIFIED — Springer article page, author and pagination confirmed.]
    4. Dietrich, F. & Spiekermann, K. "Jury Theorems." Stanford Encyclopedia of Philosophy. — Survey of the conditionalisation strategy and its failure: conditionalising on common causes does not restore probabilistic independence when information flows directly between votes. Relevant because two readers sharing a prompt, a context window, or a prior artefact are causally, not merely commonly, coupled.
    5. Wataoka, K., Takahashi, T., & Ri, R. (2024). "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819; NeurIPS 2024 Safe Generative AI Workshop. — LLM judges systematically assign higher evaluations to lower-perplexity (more familiar) text than human evaluators do, *regardless* of whether the text was self-generated. So a same-model reader pair will agree preferentially on text that is typical for that model — agreement is a fluency signal, not a truth signal. [VERIFIED — arXiv abstract page; note first author is Wataoka, not Ri.]
    6. [Partially verified] Ladha, K. — "Information pooling through majority-rule voting: Condorcet's jury theorem with correlated votes." Journal of Economic Behavior & Organization (1995). [unverified — title and venue located, author attribution not independently confirmed in this search.]

  Strength of challenge: Strong

  Summary: The literature does not merely qualify this presumption; it inverts it. Two independent lines — the empirical LLM-correlation literature and the formal jury-theorem literature — converge on the conclusion that agreement between correlated estimators is close to uninformative, and that the correlation is worst exactly where the estimators are most capable and most similar in provenance. Kim et al. show 60% same-wrong-answer coincidence; Kohli shows a nine-model, seven-family panel is worth two votes and that no aggregation scheme rescues it. Berg supplies the formal reason: positive correlation monotonically degrades collective competence. Wataoka et al. supply the mechanism by which the residual agreement is actively misleading — it tracks perplexity, i.e. familiarity to the model, not correctness. For C2A2 the implication is blunt: a second same-model reader agreeing with the first is evidence about the model, and the marginal evidential yield is nearer zero than the pipeline's design appears to assume.

  Specific risks:
    - Confidence inflation: every "two readers concurred" annotation in the corpus may be carrying a confidence weight it has not earned. If any downstream gating uses concordance as a threshold, the threshold is miscalibrated in the unsafe direction.
    - Systematic, not random, residual error: correlated error is not noise that averages out. It produces a coherent, self-consistent wrong answer that looks exactly like a right answer.
    - Fluency capture: per Wataoka et al., concordance will be highest on smooth, canonical, low-perplexity passages — i.e. on precisely the wiki material that is most conventionally phrased, which is not the same as most accurate.
    - Scale failure: adding readers does not fix it. Kohli shows panel size and aggregation sophistication both fail. C2A2 cannot buy its way out with more agents.
    - Recursive contamination: because this presumption governs the warrant of the pipeline that surfaced it (flagged by 14b for 15c), a same-model 15a/15b pair evaluating *this very item* inherits the defect. This search cannot certify its own independence.

  Mitigations available:
    - Measure, do not assume: compute Kish effective sample size (n_eff) on the reader pair against a held-out human-annotated set, as Kohli does. If n_eff ≈ 1, stop reporting concordance as evidence.
    - Replace concordance with disagreement-triggered escalation: treat agreement as *no signal* and disagreement as the only informative event routed to a human or to a genuinely different substrate.
    - Adversarial role assignment (as the pipeline already does with 15a/15b) reduces but does not eliminate correlation; Kohli's finding that chain-of-thought and prompt variation do not restore independence bounds how much this buys.
    - Substrate diversity: a non-LLM check (deterministic lint, citation resolver, symbolic constraint) is worth more than a third LLM reader.
    - Record provenance of concordance so that any later recalibration can be applied retroactively rather than requiring re-reading.

  Search scope: Web search across arXiv, ACL Anthology, Springer, SEP, and journal indexes for: LLM ensemble error correlation; LLM-as-judge self-preference and self-consistency; Condorcet jury theorem under correlated/dependent votes; effective sample size for judge panels; algorithmic monoculture. Searched 2026-08-18. Web search budget for the session was exhausted before I could cover the adversarial-collaboration literature (Kahneman/Mellers-style) or the mutual-information formalisation of agreement between correlated estimators; those two gaps are the main uncovered surface.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-751
    Strongest counterargument: Correlated does not mean identical. Kim et al. report 60% coincidence *conditional on both erring*, which leaves 40% of joint errors divergent, and Kohli's n_eff≈2 from 9 judges is small but strictly greater than 1 — so agreement retains some non-zero information. Further, the C2A2 use case may not be the one these papers measure: the LLM-judge literature studies preference and NLI tasks where ground truth is contested and the models are asked to score quality. Many C2A2 reader tasks are closer to extraction or verification against a present artefact, where the correct answer is locally determined by text that both readers can see, and where correlated priors matter less because the evidence is in the window. Finally, the presumption's harm depends on how concordance is *used*: if it is used only as a cheap triage filter and never as a certification, correlated error costs throughput, not correctness.
    What would need to be true for C2A2 to be safe: (a) The reader tasks must be evidence-bounded — answerable from material in context — so that shared priors have little room to act; (b) concordance must be used as triage, never as warrant, with no downstream artefact citing "two readers agreed" as a reason to believe something; (c) an independently-substrated check must exist for every claim class where a correlated false-positive would be expensive; (d) n_eff for the actual reader pair must be measured on a human-labelled sample and must exceed 1 by a margin large enough to matter, with the measurement repeated whenever the model changes.
    How to test: Build a gold set of 100–200 wiki items with human adjudication. Run the two same-model readers independently. Compute (i) raw agreement, (ii) agreement conditional on both being wrong, (iii) Kish n_eff against a Condorcet null, exactly as in Kohli. Then run the identical protocol with one reader replaced by a different model family and by a non-LLM checker, and compare n_eff. If same-model n_eff is not materially above 1, retire concordance as an evidential construct across the pipeline and rewrite every artefact that reports it. Secondary test: regress agreement on passage perplexity/fluency to detect the Wataoka et al. familiarity effect; if agreement tracks fluency, concordance is a style detector.
