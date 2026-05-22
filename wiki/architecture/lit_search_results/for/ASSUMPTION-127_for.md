SEARCH-FOR-ASSUMPTION-127:
  Date searched: 2026-05-14
  Original item: ASSUMPTION-127
  Original statement: "Wiki agent daily run 2026-05-13 network delta +7 PRS / +8 CROSS / +7 findings; 3 new HIGH escalations (FINDING-025, 029, 030); network state 213 PRS / 86 cross / 33 findings"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-127
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-13 wiki-agent run output
      15a: Searched for Pattern-Detector escalation-rate stability and HIGH-finding rate normalization
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Operational metrics literature (Cook 2000 "Resilience Engineering" tradition; Allspaw 2012) — daily-rate counts are valid observational data; the issue is interpretation.
    2. Statistical process control (Shewhart 1931; Wheeler 2000) — single-day counts require baseline distribution before "normal" vs. "drift" can be assessed.
    3. C2A2-internal: parallel pattern with prior daily-run counts (network state 213 PRS represents accumulation).

  Strength of support: Weak-Moderate

  Summary: The factual claim (counts as recorded) is well-supported as a daily-snapshot. But "3 new HIGH escalations" carries an implicit normalization claim — that 3 is normal — which is the operational concern PRESUMPTION-160 (paired) flags. Statistical process control would require comparison to a baseline distribution before interpreting 3-HIGH-in-one-day as content density vs. criterion drift. Support for the recorded counts is strong; support for the interpretive framing is weak.

  Caveats: (a) PRESUMPTION-160 — 3-HIGH-in-one-day treated as normal output without per-day baseline; possible Goodhart cluster; (b) FINDING-030 (active-inference-as-OODA → KL-divergence) is itself paired with ASSUMPTION-128 / PRESUMPTION-161 transfer-validity audit; (c) Network state 213/86/33 represents accumulation; the appropriate operational metric may be rate-of-change of the rate.

  Recommendation: PARTIALLY-SUPPORTED — counts are correctly recorded; interpretive normalization (3-HIGH = normal) is the load-bearing concern
