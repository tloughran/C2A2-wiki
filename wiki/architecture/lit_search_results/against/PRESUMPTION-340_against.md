SEARCH-AGAINST-PRESUMPTION-340:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-340
  Original statement: "A dyad's own agreement ledger is valid Level-3 evidence without an external rater."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-340
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Wikipedia / standard psychometrics literature. "Inter-Rater Reliability." — Establishes that reliable coding of agreement requires at minimum two independent raters; without independent coding, there is no way to separate signal from shared bias, idiosyncratic labelling conventions, or motivated construal. Cohen's kappa and Fleiss's kappa both presuppose rater independence as a precondition of the metric being interpretable.
    2. Bazerman, M.H., Loewenstein, G., & Moore, D.A. (2002). "Why Good Accountants Do Bad Audits." Harvard Business Review. — Demonstrates that self-serving bias enters audit/coding judgments unconsciously and unintentionally; individuals making "impartial" judgments when they have a stake in the outcome systematically distort assessments even without awareness or intent to deceive.
    3. Moore, D.A., Loewenstein, G., Tanlu, L., & Bazerman, M.H. (2006). "Auditor Independence, Conflict of Interest, and the Unconscious Intrusion of Bias." — Experimental evidence that rater-as-stakeholder conditions produce biased coding even under instructions to be objective; the bias is not eliminated by good faith.
    4. Bazerman, M.H., Morgan, K.P., & Loewenstein, G.F. (1997). "The Impossibility of Auditor Independence." MIT Sloan Management Review. — Argues that when the party being evaluated is also the party doing the evaluation, structural conditions make psychological independence impossible; recommends mandatory external oversight as the only viable remedy.
    5. Simmons, J.P., Nelson, L.D., & Simonsohn, U. (2011). "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant." Psychological Science. — Shows that without pre-registration and external review, researcher degrees of freedom (analytic choices made by the same party that produced the data) can inflate false-positive rates to 60%, directly applicable to a ledger where the dyad both produces and codes the evidence.
    6. Critiquing Self-report Practices for Human Mental and Wellbeing Computing at Ubicomp (arXiv:2311.15496, 2023). — Reviews systematic biases in self-report instruments including social desirability, recall bias, and construct drift; argues these make self-report unsuitable as sole evidentiary base without external anchoring.

  Strength of challenge: Strong

  Summary: Standard psychometric practice requires at minimum two independent raters before agreement coding can be treated as valid evidence, because without rater independence there is no check on shared bias, motivated construal, or idiosyncratic labelling. The dyad-as-sole-rater structure of the C2A2 ledger violates this requirement by definition. Bazerman and colleagues' experimental work shows that self-serving bias penetrates coding even in good-faith conditions; the impossibility-of-independence argument extends this to structural, not merely individual, failure. Simmons et al.'s researcher-degrees-of-freedom literature shows that analytic flexibility in the hands of the same party that produced the data dramatically inflates false-positive rates. The combination makes the ledger's claim to be "Level-3 evidence" — i.e., a validated, codeable record — epistemically circular: the dyad defines what counts as an agreement, codes whether it was reached, and asserts the ledger as evidence of dyad maturity.

  Specific risks: If the ledger is circular, the maturity model built on top of it inherits that circularity — the system will self-report as mature regardless of whether genuine agreement or genuine growth has occurred. Rung counts will inflate due to motivated construal of ambiguous interactions as agreements, and the inflation will be invisible to the system because no independent baseline exists.

  Mitigations available: Introduce a subset of sessions coded by a blinded external rater (even a separate Claude instance prompted without prior context) and compute kappa against the dyad coding; pre-register coding rules before each session to reduce post-hoc flexibility; use behavioural outcomes (subsequent decisions consistent with the rung) as a convergent validity check rather than treating the ledger as self-sufficient.

  STEELMAN:
    Strongest counterargument: The dyad is not a standard research dyad — it consists of one human and one AI agent whose outputs are fully logged. Full logging eliminates recall bias; the AI member has no personal stake in outcomes in the usual psychodynamic sense; and the C2A2 system is explicitly designed as an exploratory tool rather than a publishable empirical study. Inter-rater reliability norms apply to measurement instruments intended for generalisation; if the ledger is treated as a practice log rather than a scientific instrument, the strictness of IRR standards may be inappropriate.
    What would need to be true for C2A2 to be safe: The ledger would need to be used only as a navigation aid (what did we decide?) rather than as evidence of dyad quality or system maturity. The moment rung counts enter any summative judgment — maturity level, pipeline health, external reporting — the self-validation problem fully activates.
    How to test: Randomly sample 20 rungs, have a blinded third party (human or independent LLM instance) recode from raw session transcripts, compute Cohen's kappa; a kappa below 0.6 is evidence of coding inconsistency that compromises evidentiary status.

  Search scope: Searched psychometrics literature on inter-rater reliability requirements, self-report bias, auditor independence (Bazerman/Moore corpus), and researcher degrees of freedom (Simmons/Nelson/Simonsohn). Comprehensive for core challenge directions; additional search on dyadic agreement coding in relationship science and couples therapy research recommended.

  Recommendation: CHALLENGED
