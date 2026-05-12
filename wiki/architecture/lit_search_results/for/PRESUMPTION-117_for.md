SEARCH-FOR-PRESUMPTION-117:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-117
  Original statement: "'Core Operational Discipline' sprint presumes registration / canonization / fallback share enough remediation-substrate to bundle"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-117
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD bundling-substrate question
      15a: Searched for architectural-debt cluster-vs-atomic remediation outcomes
    Current status: PARTIALLY-SUPPORTED

  Sources:
    1. Tornhill (2018) "Software Design X-Rays" — co-occurring defects in the same architectural region show bundled-fix efficiency gains when substrate-coupling is verified; supports bundling under condition.
    2. Fowler (2018) "Refactoring" — bundled refactoring is canonical when items share a single substrate; the substrate must be articulated, not presumed.
    3. Lehman & Belady (1985) "Program Evolution" — discipline-debt accumulation responds well to bundled remediation when items share class-coherence.
    4. Counter-evidence from the same literature (e.g., Brown et al. 1998 "AntiPatterns") — bundling distinct surfaces is documented as a failure mode when class-coherence is presumed rather than verified.
    5. C2A2-internal: registration (cross-session work-item handoff), canonization (decision-record promotion), fallback (channel-resilience) operate at distinct architectural surfaces; substrate-coupling is at the meta-level (operational-discipline track) rather than the implementation-level.

  Strength of support: Weak-Moderate

  Summary: Bundling is supported when substrate-coupling is verified at the implementation level. The C2A2 cluster's substrate-coupling is at the meta-level (all three are operational-discipline gaps) rather than at the implementation level (registration, canonization, fallback are distinct mechanisms). Literature support for meta-level bundling is weaker than for implementation-level bundling. The presumption is partially supported.

  Caveats: (a) Meta-level vs. implementation-level coupling is the core distinction; the literature supports the latter more strongly; (b) sprint scope creep is a documented failure mode for meta-level bundles; (c) bundling at the meta-level can give false coherence — the bundle "feels" coordinated but executes as parallel atomic tracks.

  Recommendation: PARTIALLY-SUPPORTED (meta-level coupling is real; implementation-level coupling needs verification before sprint commitment)
