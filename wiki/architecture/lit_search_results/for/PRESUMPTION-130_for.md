SEARCH-FOR-PRESUMPTION-130:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-130
  Original statement: "Sewing agent's threshold definitions for 'orphan' / 'sparse' / 'connected' accepted as canonical baseline without external validation"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-130
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 sewing-agent first-run threshold acceptance without external validation
      15a: Searched for first-run metric-design validation patterns
    Current status: NO-SUPPORT-FOUND

  Sources:
    1. (None found supporting agent-defined thresholds adopted as canonical baseline without external benchmark.)
    2. Fenton & Bieman (2014) "Software Metrics" — operational-definition and external-validation are both required for canonical baseline status; agent-defined threshold alone does not satisfy.
    3. Boehm (1981) "Software Engineering Economics" — baseline definition without independent validation is documented over-fitting risk.
    4. Newman (2018) "Networks" — degree-based connectivity definitions (orphan=0 neighbors, etc.) have standard conventions; deviation from convention requires justification.
    5. C2A2-internal: ASSUMPTION-110 (this cycle, MONITOR-bound) is the paired stated-claim about baseline canonicalness; this PRESUMPTION captures the threshold-definition gap.

  Strength of support: None

  Summary: No literature supports agent-defined thresholds being adopted as canonical baseline without external validation or convention-alignment. Standard practice (Fenton-Bieman, Boehm, Newman) requires operational definition + independent validation or convention adherence. The presumption is unsupported.

  Caveats: Sewing-agent thresholds may align with standard graph-theory conventions (orphan=0, sparse=1-2, connected=3+) — alignment would partially support canonical baseline status. Verification of alignment is the load-bearing follow-up.

  Recommendation: NO-SUPPORT-FOUND — agent-defined thresholds without external validation or convention-alignment do not meet canonical baseline standards
