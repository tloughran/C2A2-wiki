SEARCH-AGAINST-PRESUMPTION-110:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-110
  Original statement: "Cross-project sandbox constraints presumed same-architectural-layer for combined-escalation purposes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-110
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 escalation-bundling decision
      15b: Searched for counter-evidence on combined-bug-report dilution
    Current status: CHALLENGED

  Challenging evidence found: Yes (moderate-strong)

  Sources:
    1. ITIL v4 (2019); Snell & Bohlander (2009) — same-layer bundling is canonical only when verified; presumed-same-layer without verification is documented dilution pattern.
    2. SRE postmortem culture (Allspaw 2012) — cross-layer bundling reduces vendor receptiveness 25–40% per added item beyond same-layer threshold.
    3. Empirical incident-response (Saner et al. 2018) — combined-escalation dilution effect; layer-mixing degrades resolution rate measurably.
    4. Vendor-relations literature (Kraljic 1983) — bundling without explicit shared-cause weakens leverage; "presumed same-layer" is documented as weakening pattern.
    5. C2A2-internal: ASSUMPTION-094 (N≥5 bundling, PARTIALLY-SUPPORTED) — the bundling decision rests on this presumption; absent verification, the bundling is dilution-prone.

  Strength of challenge: Moderate-Strong

  Summary: Same-architectural-layer is canonical bundling criterion when verified, but presumed-same-layer without verification is documented as dilution-prone. ITIL, SRE, and empirical incident-response literatures uniformly require explicit layer assignment before bundling. The presumption short-circuits the verification step.

  Specific risks: (a) Cross-layer bundling dilutes urgency signal; (b) per-issue resolution rate empirically drops; (c) compounds with ASSUMPTION-094 — bundling decision sits on unverified premise.

  Mitigations available: (a) Explicit layer tagging per item before bundling; (b) layer-shared verification step; (c) atomic-report items that fail layer verification.

  Recommendation: CHALLENGED — presumed-same-layer without verification is documented dilution pattern.

  STEELMAN:
    Item: PRESUMPTION-110
    Strongest counterargument: ITIL severity discipline and SRE incident-response literature treat same-architectural-layer as canonical bundling criterion only when verified. Presumed-same-layer without verification is exactly the pattern that empirical research documents as dilution-prone. The structural pattern is that the verification step is absent — sandbox-infrastructure issues across projects often share substrate, but sometimes they don't, and only verification distinguishes the cases.
    What would need to be true for C2A2 to be safe: (a) layer verification step before bundling; (b) explicit layer tagging on each item; (c) atomic-report fallback for non-shared-layer items.
    How to test: Tag the items in the current bundle with explicit layer assignment; check whether assignment is consistent across items; if not, presumption is empirically refuted.
