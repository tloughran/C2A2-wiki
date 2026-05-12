SEARCH-AGAINST-PRESUMPTION-117:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-117
  Original statement: "'Core Operational Discipline' sprint presumes registration / canonization / fallback share enough remediation-substrate to bundle"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-117
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD bundling-substrate question
      15b: Searched for counter-evidence on bundled-sprint completion vs. parallel-track completion
    Current status: CHALLENGED

  Sources:
    1. DORA / Accelerate literature (Forsgren 2018) — small-batch atomic delivery outperforms large-batch bundled delivery on most quality and throughput dimensions.
    2. Brown et al. (1998) "AntiPatterns" — bundling distinct architectural surfaces under a single sprint is documented anti-pattern when substrate-coupling is meta-level.
    3. Cohn (2010) "Succeeding with Agile" — atomic remediation tracks with explicit cross-track coordination outperforms bundled sprint when items have distinct implementation surfaces.
    4. Lehman & Belady (1985) "Program Evolution" — sprint scope creep is documented as common when bundle scope is defined by category rather than by implementation surface.
    5. C2A2-internal: registration (work-item handoff via PROCESSED_LOG / Handoffs/latest.md), canonization (DECISION-NNN promotion criteria), fallback (channel-resilience) operate on distinct implementation surfaces.

  Strength of challenge: Moderate-Strong

  Summary: The presumption that the three items share enough substrate to bundle is challenged by small-batch / atomic-delivery / anti-pattern / scope-creep literatures. The substrate-coupling is at the meta-level (operational-discipline category), which is weaker bundling justification than implementation-level coupling. Literature consensus favors atomic tracks with cross-track coordination over bundled sprint when implementation surfaces differ.

  Specific risks: (a) Bundled sprint executes as parallel atomic tracks under unified label; (b) sprint scope creep — additional discipline gaps get pulled in once bundle is defined by category; (c) bundled completion timeline governed by slowest sub-item.

  Mitigations available: (a) Verify implementation-substrate coupling before sprint commitment; (b) bound sprint scope explicitly; (c) treat as parallel atomic tracks if substrate-coupling is meta-level only.

  Recommendation: CHALLENGED (substrate-coupling at meta-level is weaker bundling justification than literature requires)

  STEELMAN:
    Item: PRESUMPTION-117
    Strongest counterargument: Registration, canonization, and fallback operate on distinct implementation surfaces. Their substrate-coupling is at the meta-level (operational-discipline category) only. The DORA / Accelerate literature shows that small-batch atomic delivery outperforms large-batch bundled delivery for items with distinct surfaces; the "Core Operational Discipline" sprint risks the large-batch failure mode. Bundling at meta-level can give false coherence — the bundle "feels" coordinated but executes as parallel atomic tracks with the additional overhead of bundle-level coordination.
    What would need to be true for C2A2 to be safe: (a) Implementation-substrate coupling verified across the three items; (b) sprint scope bounded explicitly; (c) bundle-level coordination justified against parallel-atomic-track baseline.
    How to test: Examine the implementation surfaces of each item — does registration share code paths with canonization? Does canonization share code paths with fallback?
