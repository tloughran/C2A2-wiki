SEARCH-FOR-ASSUMPTION-140:
  Date searched: 2026-05-15
  Original item: ASSUMPTION-140
  Original statement: "Morning chat-scrape succeeded second consecutive day; sign-in fix from 2026-05-13 is holding (two data points)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-140
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-14 operational summary
      15a: Searched for operational stability patterns after credential-layer fixes
    Current status: PARTIALLY-SUPPORTED (Weak-Moderate)

  Sources:
    1. SRE practice (Beyer et al. 2016 "Site Reliability Engineering") — N=2 is below the canonical "trending" threshold; SRE practice requires N ≥ 7 (one week) or N ≥ 14 (two weeks) for stability claims.
    2. Statistical process control (Shewhart, Deming) — two data points cannot establish a trend; minimum N for control-chart stability claim is typically 8-20.
    3. Allspaw (2009) "10+ Deploys Per Day" — post-incident stability is canonically tracked for one full incident-cycle (typically 7-30 days).
    4. C2A2-internal: prior 7-day drought (2026-05-06 to 2026-05-13) establishes the failure-cycle scale; two successful days is < 30% of the failure-cycle duration.
    5. Counterpoint within 15a support: at minimum, two consecutive success days breaks the "every-day-failure" pattern observed during the drought; weak positive signal.

  Strength of support: Weak-to-Moderate

  Summary: Two consecutive success days is a positive signal but well below canonical stability-claim thresholds (SRE N≥7, SPC N≥8). The claim "sign-in fix is holding" is honest about the N=2 sample size in the statement itself ("two data points") — this is good epistemic practice but the inference must be correspondingly weak. Support is Weak-to-Moderate: the data points exist; the inference to "holding" is provisional. PRESUMPTION-177 paired (Chrome-MCP failure recurred same day) further weakens the broader "credential-layer-fix-is-stable" framing.

  Caveats: (a) N=2 below stability-claim threshold; (b) PRESUMPTION-177 paired — Chrome MCP failed today; credential-layer is not fully restored at the system level; (c) "Holding" suggests an inference the sample doesn't support; (d) Joint with ASSUMPTION-141 (evening cowork-to-chat failed) — same day shows partial-success, not full-success; (e) PRESUMPTION-159 carry-forward — credential-layer-as-architectural-fix anti-pattern remains under REVISE.

  Recommendation: PARTIALLY-SUPPORTED (Weak-Moderate) — two data points are honest; "holding" inference is provisional; load-bearing concern is the credential-vs-architectural framing
