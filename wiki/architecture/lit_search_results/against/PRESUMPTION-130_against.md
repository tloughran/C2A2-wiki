SEARCH-AGAINST-PRESUMPTION-130:
  Date searched: 2026-05-11
  Original item: PRESUMPTION-130
  Original statement: "Sewing agent's threshold definitions for 'orphan' / 'sparse' / 'connected' accepted as canonical baseline without external validation"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-130
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-10 sewing-agent threshold acceptance
      15b: Searched for counter-evidence on agent-defined thresholds without external benchmarking
    Current status: CHALLENGED

  Sources:
    1. Fenton & Bieman (2014) "Software Metrics" — baseline status requires external validation or convention alignment; agent-defined threshold alone does not satisfy.
    2. Boehm (1981) "Software Engineering Economics" — over-fitting risk from agent-defined thresholds is documented.
    3. Newman (2018) "Networks" — graph-theory conventions exist for orphan/sparse/connected; deviation requires justification.
    4. ISO/IEC 25010 (2011) software-quality-model — measurement validity requires reproducibility across instruments; single-agent threshold definition does not establish reproducibility.
    5. PRESUMPTION-131 (this cycle) — paired autonomous-agent boundary-setting concern; both surface the same agent-judgment-without-policy gap.

  Strength of challenge: Moderate-Strong

  Summary: The challenge is moderate-to-strong. Agent-defined thresholds adopted as canonical baseline without external validation contradicts converging metric-validity literature (Fenton-Bieman, Boehm, Newman, ISO/IEC 25010). The presumption is essentially the same anti-pattern as PRESUMPTION-131 (agent-judgment-without-policy) applied to threshold definitions. Mitigation is straightforward (document thresholds, check convention alignment).

  Specific risks: (a) Baseline locked in by agent-defined thresholds; (b) future measurements interpreted against un-validated baseline; (c) downstream metrics inherit threshold-definition gap; (d) agent-judgment becomes policy-by-accretion.

  Mitigations available: (a) Document thresholds in policy file; (b) verify alignment with standard graph-theory conventions; (c) external review checkpoint before "canonical" designation; (d) version threshold definitions so changes are traceable.

  Recommendation: CHALLENGED (Moderate-Strong)

  STEELMAN:
    Item: PRESUMPTION-130
    Strongest counterargument: Metric-validity literature is unambiguous: baseline status requires either external validation or convention alignment. Agent-defined thresholds satisfy neither by default. The convention check is trivial (orphan=0 neighbors, sparse=1-2, connected=3+ are standard graph-theory definitions) — performing the check would either resolve the presumption (alignment confirmed) or surface a gap (deviation requires justification). Skipping the check means downstream measurements are interpreted against an un-validated baseline; the threshold definitions can drift across runs without anyone noticing.
    What would need to be true for C2A2 to be safe: (a) Threshold definitions documented; (b) convention-alignment verified; (c) version controlled.
    How to test: Read the sewing-agent's threshold definitions; compare against standard graph-theory conventions; check version control on threshold parameters.
