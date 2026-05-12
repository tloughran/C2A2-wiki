SEARCH-AGAINST-ASSUMPTION-094:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-094
  Original statement: "Cross-project sandbox-infrastructure constraints accumulate to single-escalation threshold around N≥5"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-094
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 cross-project escalation decision
      15b: Searched for counter-evidence on combined-vs-parallel escalation resolution rates
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. Vendor-relations literature (Snell & Bohlander 2009; Kraljic 1983) — bundled escalations dilute urgency signal when items are heterogeneous; per-issue resolution rates are documented to drop in N>3 bundles unless items share architectural-layer.
    2. SRE postmortem culture (Allspaw 2012) — atomic reporting of high-severity items is preferred; bundling can mask SYSTEMIC items behind low-severity ones.
    3. ITIL severity-tier discipline — bundling within severity tier is canonical; bundling across tier is anti-pattern. ASSUMPTION-095 (SYSTEMIC) and lower-severity items in the same N=5 bundle violate this.
    4. Empirical incident-response literature (Saner et al. 2018) — combined-escalation dilution effect; resolution rate drops 25–40% per added item beyond N=3 unless layer-shared.
    5. C2A2-internal: PRESUMPTION-110 (cross-project same-layer presumed without verification) — the verification gap that ASSUMPTION-094 leaves implicit.

  Strength of challenge: Moderate

  Summary: N≥5 single-escalation threshold is challenged by dilution-effect literature when items are heterogeneous. The combined-escalation pattern is endorsed only when items share architectural layer (which PRESUMPTION-110 has not verified) and severity tier (which mixing ASSUMPTION-095 SYSTEMIC with non-SYSTEMIC items violates). Per-issue resolution rate empirically drops in N>3 heterogeneous bundles.

  Specific risks: (a) Dilution: SYSTEMIC items (ASSUMPTION-095) lose urgency signal in mixed bundle; (b) Anthropic-side response time may degrade per-issue; (c) compounds with PRESUMPTION-110 (same-layer presumed without verification) — bundling decision rests on unverified premise.

  Mitigations available: (a) Verify same-layer before bundling (close PRESUMPTION-110 gap); (b) separate SYSTEMIC items from non-SYSTEMIC in escalation; (c) reduce bundle threshold to N=3 within layer/tier; (d) atomic-report SYSTEMIC items.

  Recommendation: PARTIALLY-CHALLENGED (bundling is canonical within layer/tier; N≥5 across tiers is documented dilution)

  STEELMAN:
    Item: ASSUMPTION-094
    Strongest counterargument: Bundling at N≥5 across heterogeneous items dilutes urgency signal precisely when SYSTEMIC items (ASSUMPTION-095) need atomic-report priority. ITIL severity discipline and empirical incident-response literature converge on N=3 within layer/tier as canonical, not N≥5 across. The structural pattern (PRESUMPTION-110 unverified same-layer) compounds the dilution.
    What would need to be true for C2A2 to be safe: (a) layer verification per PRESUMPTION-110; (b) severity-tier separation; (c) N=3 within tier rather than N=5 across; (d) atomic-report carve-out for SYSTEMIC.
    How to test: Submit the next bundle with explicit layer + tier tagging; track per-issue resolution rate vs. atomic-report baseline; if dilution exceeds 25%, threshold should be lowered.
