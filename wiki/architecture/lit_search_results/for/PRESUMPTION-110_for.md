SEARCH-FOR-PRESUMPTION-110:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-110
  Original statement: "Cross-project sandbox constraints presumed same-architectural-layer for combined-escalation purposes"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-110
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 escalation-bundling decision: cross-project sandbox issues bundled without same-layer verification
      15a: Searched for supporting literature on incident-classification framework and layered failure-surface taxonomies
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes (weak — supportive only when same-layer is in fact verified)

  Sources:
    1. ITIL v4 (2019) — same-architectural-layer is the canonical bundling criterion; combined escalation across layers is documented dilution.
    2. SRE literature (Beyer et al. 2016 Ch. 14) — incident-classification frameworks treat layer as primary axis; cross-layer bundling reduces vendor receptiveness.
    3. Vendor-management literature (Snell & Bohlander 2009) — bundling within layer is endorsed; bundling across layer is documented anti-pattern.
    4. C2A2-internal: ASSUMPTION-094 (N≥5 cross-project bundling, PARTIALLY-SUPPORTED) — bundling literature endorses same-layer condition; the presumption short-circuits the verification step.

  Strength of support: Weak

  Summary: The "same-architectural-layer" assumption has weak supportive grounding because the literature endorses same-layer bundling as canonical when same-layer is verified. The presumption short-circuits verification — it presumes same-layer rather than checking. Supportive literature exists for the criterion itself; it does not exist for the unverified version of the criterion.

  Caveats: (a) Sandbox-infrastructure issues across projects often are same-layer (sandbox is a shared substrate), but this is empirical, not presumptive; (b) the presumption is operationally usable when verification is cheap (e.g., quick layer check); it becomes anti-pattern when verification is skipped entirely; (c) supportive literature pairs same-layer bundling with documented layer assignment — the absence of explicit layer-tagging is the structural gap.

  Recommendation: PARTIALLY-SUPPORTED (same-layer bundling is canonical; presumption-without-verification is the gap)
