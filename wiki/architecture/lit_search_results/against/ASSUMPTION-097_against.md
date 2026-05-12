SEARCH-AGAINST-ASSUMPTION-097:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-097
  Original statement: "Three-recurrence discipline cluster (registration / canonization / fallback) is bundleable as a single 'Core Operational Discipline' architectural sprint"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-097
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD recurrence-cluster observation
      15b: Searched for counter-evidence on bundling distinct remediation surfaces
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial-Moderate

  Sources:
    1. Brown et al. (1998) "AntiPatterns" — bundling distinct architectural surfaces under a single sprint is documented as failure mode when substrate-coupling is meta-level rather than implementation-level.
    2. Lehman & Belady (1985) "Program Evolution" — sprint scope creep is documented as common when bundle scope is defined by category ("operational discipline") rather than by implementation surface.
    3. Forsgren et al. (2018) "Accelerate" / DORA literature — small-batch atomic delivery outperforms large-batch bundled delivery on most quality and throughput dimensions; "Core Operational Discipline" sprint risks the large-batch failure mode.
    4. Counter-pattern literature in agile (Cohn 2010 "Succeeding with Agile") — atomic remediation tracks with explicit cross-track coordination outperforms bundled sprint when the items have distinct implementation surfaces.
    5. C2A2-internal: registration (work-item handoff via PROCESSED_LOG / Handoffs/latest.md), canonization (DECISION-NNN promotion criteria), fallback (channel-resilience) are distinct mechanisms; bundling them risks executing as parallel atomic tracks under a unified label rather than coordinated remediation.

  Strength of challenge: Moderate

  Summary: Bundling at the meta-level (operational-discipline category) is challenged by the small-batch / atomic-delivery literature. The three items in the cluster operate on distinct implementation surfaces; the substrate-coupling is at the meta-level, which the literature treats as weaker bundling justification. The "Core Operational Discipline" framing risks scope creep, parallel-track execution under a unified label, and large-batch quality regression.

  Specific risks: (a) Bundled sprint executes as three parallel atomic tracks under a unified label, with coordination overhead exceeding atomic-track baseline; (b) sprint scope creep — additional discipline gaps get pulled in once the bundle is defined by category; (c) bundled completion timeline is governed by slowest sub-item, not by individual urgency.

  Mitigations available: (a) Verify implementation-substrate coupling before sprint commitment; (b) bound sprint scope explicitly to the three items; (c) treat as parallel atomic tracks with documented coordination if substrate-coupling is meta-level only.

  Recommendation: PARTIALLY-CHALLENGED (meta-level coupling is real but implementation-level coupling needs verification; small-batch atomic delivery is the canonical alternative)

  STEELMAN:
    Item: ASSUMPTION-097
    Strongest counterargument: The three items (registration, canonization, fallback) operate on distinct implementation surfaces. Their substrate-coupling is at the meta-level (all are operational-discipline gaps), which is weaker bundling justification than implementation-level coupling. The "Core Operational Discipline" framing risks the large-batch failure mode documented in Accelerate / DORA: large-batch sprints have lower throughput and quality than small-batch atomic delivery for items with distinct surfaces. Bundling at the meta-level can give false coherence — the bundle "feels" coordinated but executes as parallel atomic tracks with the additional overhead of bundle-level coordination.
    What would need to be true for C2A2 to be safe: (a) Implementation-substrate coupling verified across the three items; (b) sprint scope bounded explicitly to the three items with no creep; (c) bundle-level coordination justified against parallel-atomic-track baseline.
    How to test: Examine the implementation surfaces of each item — does registration share code paths with canonization? Does canonization share code paths with fallback? If not, bundle is at meta-level only; parallel atomic tracks with documented cross-track coordination is the literature-endorsed alternative.
