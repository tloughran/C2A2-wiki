SEARCH-AGAINST-PRESUMPTION-237:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-237
  Original statement: "The publish/untrack calls rest on an unstated, stable publishability criterion; the governing rule is tacit (normative smuggling)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-237
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from per-artifact publish/untrack decisions made without an articulated rule.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Data-classification best practice (NIST SP 800-60; ISO 27001 A.8). — Publication/handling decisions should follow an explicit, written classification rule; tacit per-case calls are not auditable or repeatable.
    2. "Normative smuggling" / value-laden design critique. — Unarticulated criteria embed values invisibly; without an explicit rule, the criterion drifts and cannot be reviewed or contested.
    3. Reproducibility/governance of decisions: undocumented decision rules fail consistency over time and across operators (couples ASSUMPTION-218 publishability discretion).

  Strength of challenge: Moderate

  Summary: A tacit, unwritten publishability criterion is workable for a single expert operator today but is fragile by every governance standard: it is not auditable, not consistently applicable, and silently encodes value judgments (normative smuggling). The risk is consistency drift — the same kind of artifact gets published one week and untracked the next — and the impossibility of review because the rule is never stated. The challenge is moderate (not strong) because the exposure today is limited and the fix is cheap: write the criterion down.

  Specific risks: An inconsistent or value-laden publish decision (publishing something that should have been withheld, or vice versa) made under a rule no one can inspect, with privacy/consent stakes (couples PRESUMPTION-238).

  Mitigations available: Articulate the publishability criterion explicitly (what is in/out and why), even a one-paragraph rule; log each publish/untrack decision against it; review the rule when the corpus or team changes.

  Recommendation: CHALLENGED (moderate)

  STEELMAN:
    Item: PRESUMPTION-237
    Strongest counterargument: Every data-governance standard requires publication decisions to follow an explicit, written rule precisely because tacit criteria are unauditable, drift over time, and smuggle in unexamined values; per-artifact publish/untrack calls under an unstated criterion are therefore fragile and unreviewable, and the stakes (privacy, consent, irreversibility of publication) are exactly where governance demands articulation.
    What would need to be true for C2A2 to be safe: The publishability criterion is written down and each decision is logged against it.
    How to test: Ask the operator to state the rule and apply it to three borderline artifacts; if the calls are not reproducible from the stated rule, the criterion is tacit and unstable.
