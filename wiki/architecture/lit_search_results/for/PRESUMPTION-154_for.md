SEARCH-FOR-PRESUMPTION-154:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-154
  Original statement: "Phone-as-confirmation-modality presumed without considering alternatives (push-notification, email-magic-link, in-cowork-confirmation, pre-authorized scope tokens); two-options-of-same-form-factor framing renders form factor invisible"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-154
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-121 SMS-link-vs-reply-keyword framing without modality comparison
      15a: Searched for modality comparison literature in DevOps and enterprise paging
    Current status: SUPPORTED

  Sources:
    1. PagerDuty / Opsgenie / VictorOps design literature (2018-2024) — multi-modality (push + SMS + email + voice) is canonical for asynchronous approval flows; single-modality is recognized as a fragility.
    2. Bryar & Carr (2021) Amazon decision-record practice — explicit option enumeration including "do nothing" and alternative form factors is required.
    3. Nielsen Norman Group (2020) "Notification modality and attention" — modality comparison is a recognized design step.
    4. "Two options of the same form factor" anti-pattern — Don Norman's affordance literature describes this as form-factor-invisibility.

  Strength of support: Strong

  Summary: Modality-comparison-before-mechanism-choice is endorsed across paging tool design, decision-record practice, and notification-UX literature. The "two-options-of-same-form-factor" reading is a recognized affordance-invisibility pattern. Strong support for the inference that ASSUMPTION-121 should have compared SMS to alternative modalities (push, email-magic-link, in-cowork-confirmation, pre-authorized scope tokens).

  Caveats: (a) For external escalation specifically (phone-as-out-of-band), SMS has a defensible "in-band-failure-isolation" justification that the in-cowork-confirmation alternative does not have; (b) Comparison-cost vs. choice-clarity tradeoff exists; (c) The presumption is correctly framing this as a process gap, not necessarily a wrong-mechanism gap.

  Recommendation: SUPPORTED — modality-comparison gap is real; the inference identifies a recognized anti-pattern
