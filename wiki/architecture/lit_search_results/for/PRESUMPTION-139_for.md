SEARCH-FOR-PRESUMPTION-139:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-139
  Original statement: "Sewing-agent-recommended one-time backlink-injection pass presumed to make connectivity metric 'sensitive' — sensitivity threshold not specified"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-139
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 sewing-agent intervention-without-sensitivity-threshold
      15a: Searched for metric-sensitivity threshold literature in graph-connectivity contexts
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. (None found supporting intervention design without sensitivity-threshold specification.)
    2. Fenton & Bieman (2014) "Software Metrics" — metric design requires operational definition of "sensitive" (e.g., minimum-detectable-effect, statistical-power) before intervention is endorsed as effective.
    3. Cohen (1988) "Statistical Power Analysis" — sensitivity claims require specification of the smallest effect of operational interest; "make sensitive" without threshold is meaningless.
    4. Newman (2018) "Networks" — graph-connectivity metric sensitivity depends on threshold definitions for orphan/sparse/connected; modifying graph without re-defining thresholds produces uninterpretable shifts.
    5. C2A2-internal: PRESUMPTION-130 (this cycle) is the paired threshold-definition gap; PRESUMPTION-139 is the paired sensitivity-threshold gap.

  Strength of support: None

  Summary: No literature supports intervention design without sensitivity-threshold specification. Metric-design literature (Fenton-Bieman, Cohen) explicitly requires operational definition of sensitivity before intervention is endorsed. The presumption is unsupported; the documented practice is threshold specification first, intervention second, post-intervention validation third.

  Caveats: "Sensitive" may be used informally to mean "more-responsive-than-current" — under that reading, the claim is weakly supported (any backlink injection mathematically reduces orphan count). Operational sensitivity (detect smallest meaningful change) is the unsupported reading.

  Recommendation: NO-SUPPORT-FOUND — sensitivity-threshold specification is canonical metric-design prerequisite; absent threshold, "sensitive" claim is operationally meaningless
