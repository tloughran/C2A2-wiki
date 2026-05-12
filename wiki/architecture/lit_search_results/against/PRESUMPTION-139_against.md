SEARCH-AGAINST-PRESUMPTION-139:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-139
  Original statement: "Sewing-agent-recommended one-time backlink-injection pass presumed to make connectivity metric 'sensitive' — sensitivity threshold not specified"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-139
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 sewing-agent intervention-without-threshold
      15b: Searched for counter-evidence on intervention-without-sensitivity-threshold-specification
    Current status: CHALLENGED

  Sources:
    1. Fenton & Bieman (2014) "Software Metrics" — sensitivity claims require operational definition of minimum-detectable-effect; "make sensitive" without threshold is metric-design anti-pattern.
    2. Cohen (1988) "Statistical Power Analysis" — sensitivity requires specification of smallest effect of operational interest.
    3. Newman (2018) "Networks" — graph-connectivity metric sensitivity depends on threshold definitions; modifying graph without re-defining thresholds produces uninterpretable shifts.
    4. Boehm (1981) — intervention design without success-criterion specification is documented requirements-gap.
    5. PRESUMPTION-130 (this cycle) — paired threshold-definition concern; same agent-defined-metric-without-validation gap.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. Intervention without sensitivity-threshold specification contradicts canonical metric-design (Fenton-Bieman), statistical-power (Cohen), network-analysis (Newman), and requirements-engineering (Boehm) literatures. The presumption is unsupported; the documented practice is threshold specification first, intervention second, post-intervention validation third.

  Specific risks: (a) Intervention "succeeds" in nominal sense (orphan count drops) but the substantive sensitivity claim is unverified; (b) downstream metrics interpreted relative to unspecified threshold; (c) "sensitive" claim is unfalsifiable absent threshold; (d) cluster joint with PRESUMPTION-130 — same agent-judgment-without-validation gap.

  Mitigations available: (a) Specify minimum-detectable-effect for "sensitive"; (b) pre/post measurement design with explicit success criterion; (c) document threshold change rationale; (d) paired-validation with PRESUMPTION-130 threshold-definition fix.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-139
    Strongest counterargument: Metric-design literature is unambiguous: sensitivity claims require operational definition before the intervention. Without minimum-detectable-effect specification, "make sensitive" is operationally meaningless — any intervention that reduces orphan count would nominally "succeed" without actually improving the metric's diagnostic capacity. The C2A2 case is paired with PRESUMPTION-130 (threshold definitions un-validated); both surface the same agent-judgment-without-validation gap. The fix is cheap (specify a numerical threshold) but its absence renders the intervention's success criterion non-existent.
    What would need to be true for C2A2 to be safe: (a) Minimum-detectable-effect specified; (b) pre/post measurement design with success criterion; (c) threshold change rationale documented.
    How to test: Read sewing-agent's intervention recommendation for sensitivity-threshold specification; check whether pre/post measurement is planned with explicit criterion.
