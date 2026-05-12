SEARCH-FOR-PRESUMPTION-104:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-104
  Original statement: "Org-vs-personal naming presumed misclassification despite same throttling behavior"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-104
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from 2026-05-08 work session: account-tier name treated as classification signal despite identical throttling behavior
      15a: Searched for supporting literature on account-tier-vs-message-wording in SaaS quota systems
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (weak)

  Sources:
    1. SaaS-billing literature (Bills 2018 "Subscribed"; Reichheld & Schefter 2000) — naming inconsistencies in account-tier UX are documented as common; tier name should not be primary classification signal when behavior matches a different tier.
    2. UX research on account-tier confusion (Nielsen Norman Group reports 2019–2024) — users frequently misread account-tier labels; naming-mismatch is documented as classification noise.
    3. API-design literature (Mulloy 2012 "Web API Design") — wire-level behavior is canonical classification signal; UX labels are secondary.
    4. C2A2-internal: ASSUMPTION-088 (work-blocking quota framing) — the misclassification framing is consistent with treating wire-level behavior as primary signal and naming as secondary.
    5. Cloud-pricing literature — SaaS providers occasionally use legacy or pre-migration tier names that don't match current behavior; this is documented as a benign naming-vs-behavior gap.

  Strength of support: Weak-Moderate

  Summary: The misclassification framing has weak supportive grounding: SaaS / API / UX literature consistently treats wire-level behavior as primary signal and naming as secondary. The presumption that an "org-monthly" label on a personal account is misclassification (rather than indicating real org-tier behavior) is one defensible reading of the situation. However, the literature is silent on the specific case of identical throttling behavior with mismatched naming — this is a small literature gap.

  Caveats: (a) "Same throttling behavior" is a behavior-only signal — without confirming wire-level identity (response codes, headers, retry-after), behavioral identity is presumptive rather than confirmed; (b) supportive literature distinguishes misclassification (UX label is wrong) from intentional dual-naming (legacy / migration / region-specific) — without provider clarification, attribution is uncertain; (c) the presumption short-circuits investigation — if behavior is identical, the operational disposition is quota event regardless of naming, which is what ASSUMPTION-088 recommends.

  Recommendation: PARTIALLY-SUPPORTED (naming-as-classification-signal is canonical to deprioritize; misclassification attribution is one defensible reading among several)
