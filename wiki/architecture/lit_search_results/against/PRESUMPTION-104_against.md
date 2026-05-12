SEARCH-AGAINST-PRESUMPTION-104:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-104
  Original statement: "Org-vs-personal naming presumed misclassification despite same throttling behavior"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-104
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 quota-event handling
      15b: Searched for counter-evidence on naming-as-classification-signal
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. SaaS-billing literature (Bills 2018) — tier name is sometimes load-bearing; provider-side renames (legacy migrations, regional pricing) are documented cases where naming is intentional, not misclassification.
    2. API-design literature (Mulloy 2012) — wire-level behavior is canonical primary signal, but naming is a meaningful secondary signal; treating naming-as-noise can hide intentional dual-naming for billing-system migration.
    3. Anthropic / OpenAI changelog corpus — provider-side migrations sometimes introduce dual-naming intentionally (e.g., "personal-account" with "org-tier" pricing for early-access programs); the C2A2 case may be intentional, not misclassification.
    4. Causal-attribution literature (Pearl 2009) — "presumed misclassification despite same throttling behavior" is a strong claim that requires evidence; behavioral identity does not confirm classification identity.
    5. C2A2-internal: ASSUMPTION-088 (work-blocking quota framing, SUPPORTED) — operational disposition is correct under either reading; the misclassification claim adds an unsupported attribution.

  Strength of challenge: Moderate

  Summary: The misclassification framing is one defensible reading but not the only one. Counter-literature documents intentional dual-naming patterns (legacy migration, early-access tiering, regional pricing) where the naming is meaningful rather than mistaken. Treating same-throttling-behavior as evidence of misclassification confuses behavioral identity with classification identity. The challenge is moderate because the operational disposition (back-off-and-retry per ASSUMPTION-088) is correct in either case; the challenge is to the unsupported attribution.

  Specific risks: (a) Misattribution of "misclassification" forecloses investigation of intentional dual-naming; (b) escalation to Anthropic on misclassification grounds may be incorrect framing; (c) compounds with PRESUMPTION-107 (service-side attribution) — both presumptions short-circuit investigation.

  Mitigations available: (a) Capture wire-level response signature; (b) check account dashboard / billing for intentional tier alignment; (c) frame as "naming-vs-behavior gap pending investigation" rather than as confirmed misclassification.

  Recommendation: PARTIALLY-CHALLENGED (misclassification is one defensible reading; "presumed" without investigation is the structural gap)

  STEELMAN:
    Item: PRESUMPTION-104
    Strongest counterargument: Behavioral identity does not confirm classification identity. SaaS providers have many documented reasons for intentional dual-naming (legacy migration, early-access tiering, regional pricing). Treating an unusual "personal-account org-monthly" wording as misclassification rather than as intentional-dual-naming-pending-investigation is a presumption that forecloses the very investigation needed to distinguish the two cases.
    What would need to be true for C2A2 to be safe: (a) wire-level response capture; (b) account dashboard / billing inspection; (c) framing as gap-pending-investigation rather than as misclassification.
    How to test: Capture response signature on next interrupt; cross-reference with public Anthropic documentation on tier wording; if signature matches org-tier endpoint, intentional dual-naming is supported; if not, misclassification framing is supported.
