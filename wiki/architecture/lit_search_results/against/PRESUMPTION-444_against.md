SEARCH-AGAINST-PRESUMPTION-444:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-444
  Original statement: "[inferred] That deadline-driven gating ('ready for ISME') is the right release principle for public artifacts of an evidence-bearing system."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-444
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session behavior that "ready for ISME" (a calendar date) was operating as the release gate rather than a quality criterion
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kuutila, M., Mäntylä, M., Claes, M., Elovainio, M., 2020. "Time pressure in software engineering: A systematic review." Information and Software Technology 121, 106257. — Systematic review of 102 papers; the majority of quantitative results support reduced quality (more defects) under time pressure, even where productivity rises. Directly challenges deadline gating as quality-neutral.
    2. Rogers Commission Report, 1986 (and CED Engineering ethics case study of Challenger). — Under launch-schedule pressure, the burden of proof inverted from "prove it is safe" to "prove it is unsafe"; deadline-anchored go/no-go decisions systematically bias toward "go" and suppress valid objections.
    3. Vaughan, D., 1996. "The Challenger Launch Decision." University of Chicago Press. — Production/schedule pressure is a core ingredient of normalization of deviance; readiness criteria erode incrementally when evaluated against a fixed date rather than fixed standards.
    4. Olschewski, S., Rieskamp, J., 2021. "Distinguishing three effects of time pressure on risk taking: Choice consistency, risk preference, and strategy selection." Journal of Behavioral Decision Making 34(4). — Time pressure reduces choice consistency and shifts strategy selection; decision quality effects are real though heterogeneous.
    5. Effects of time pressure on decision-making under uncertainty (Acta Psychologica, 2000; and PMC studies 2022–2023 on risk preference under time pressure). — Perceptual narrowing, reduced vigilance, reduced working memory and information utilization under time pressure; riskier choices in gain frames.
    6. "Go fever" literature (space-industry term; Lead Wise / engineering ethics sources). — Named phenomenon in which decision-makers fixate on a goal date at the expense of risk assessment; deadline-as-gate is its institutional form.

  Strength of challenge: Strong

  Summary: The literature challenging deadline-driven release gating is substantial and convergent. Kuutila et al.'s systematic review finds time pressure predominantly reduces software quality. The Challenger record (Rogers Commission, Vaughan) is the canonical demonstration that date-anchored go/no-go decisions invert the burden of proof and override readiness criteria — the exact structure of "is it ready for ISME?" replacing "does it meet the release rule?". Cognitive literature adds mechanism: time pressure narrows attention, degrades information use, and shifts risk preferences. A caveat: deadlines also have documented benefits (forcing function against perfectionism, Parkinson's-law control), and some studies find weakened framing bias under pressure — so the challenge targets deadline-as-gate, not deadline-as-motivator. For an evidence-bearing system whose public artifacts are its credibility, criterion-based gating with the deadline as a scheduling constraint is what the literature supports.

  Specific risks: The ISME date silently substitutes for the system's own release rule (visual sign-off), so a defective or unverified artifact ships because the calendar said so; burden of proof inverts ("prove it's not ready"); each deadline-gated release erodes the criteria further; the system's documented principles diverge from its actual practice, which for a self-documenting evidence system is itself a defect.

  Mitigations available: Separate the two questions explicitly — "does it pass the release rule?" (quality gate) and "can it be done by ISME?" (schedule); pre-commit written go/no-go criteria before the deadline week; designate scope reduction (ship less, verified) rather than criteria reduction (ship all, unverified) as the sanctioned deadline response; require any criteria waiver to be logged as an exception with a named owner.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-444
  Strongest counterargument: Deadline gating does not merely risk shipping worse artifacts — it structurally inverts the decision. Once "ready for ISME" is the question, the null hypothesis becomes "ship," and evidence of unreadiness must clear a bar that evidence of readiness never faced; this is precisely the inversion the Rogers Commission identified at NASA. The systematic-review evidence (Kuutila et al. 2020) shows this is not anecdote: across 102 studies, time pressure predominantly degrades quality. For C2A2 the stakes are compounded because the artifact is the public evidence of an evidence-bearing system — a deadline-gated defect is a self-refuting exhibit.
  What would need to be true for C2A2 to be safe: The release rule (e.g., visual sign-off) is applied unchanged under deadline conditions, and the only deadline-driven variable is scope, never criteria.
  How to test: Audit the ISME release retrospectively — list each release criterion and whether it was applied, waived, or substituted (e.g., marker-grep for visual check); any substitution made in the deadline week that would not have been accepted a month earlier confirms the failure mode.
