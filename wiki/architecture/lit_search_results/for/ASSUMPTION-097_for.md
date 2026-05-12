SEARCH-FOR-ASSUMPTION-097:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-097
  Original statement: "Three-recurrence discipline cluster (registration / canonization / fallback) is bundleable as a single 'Core Operational Discipline' architectural sprint"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-097
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD recurrence-pattern observation (PRESUMPTION-105/106/111 third-recurrence cluster)
      15a: Searched for supporting literature on architectural-debt cluster-remediation patterns and sprint-bundle outcomes
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Fowler (2018) "Refactoring" 2nd ed. — bundled refactoring under a single sprint when items share substrate (process-discipline gaps in this case) is a canonical pattern with documented outcomes.
    2. Kim et al. (2016) "The DevOps Handbook" — operational-discipline backlog grouping (registration, canonization, escalation) is a recognized sprint-bundle pattern when items are substrate-coupled.
    3. Lehman & Belady (1985) "Program Evolution" — discipline-debt accumulates with same-class recurrence; bundled remediation outperforms atomic remediation when class-coherence is verified.
    4. Tornhill (2018) "Software Design X-Rays" — co-occurrence of defects in the same architectural region predicts bundled-fix efficiency gains; "Core Operational Discipline" naming aligns with this pattern.
    5. C2A2-internal: PRESUMPTION-105 (registration) + PRESUMPTION-106 (canonization) + PRESUMPTION-111 (fallback) all third-recurrences in 2026-05-09; substrate is the operational-discipline track.

  Strength of support: Moderate

  Summary: Bundled remediation of substrate-coupled discipline gaps is canonical when (a) items share remediation substrate, (b) coordination cost across atomic tracks exceeds bundling overhead, and (c) the bundle has a clear scope boundary. Refactoring, DevOps, and software-evolution literature support sprint-level bundling for operational-discipline clusters. The three items in the C2A2 cluster (registration, canonization, fallback) operate on the same substrate (cross-session / cross-decision discipline track), satisfying the bundling precondition.

  Caveats: (a) Bundling only outperforms atomic tracks when substrate-coupling is verified; PRESUMPTION-117 captures the verification gap; (b) sprint-bundle scope creep is a documented failure mode — clear scope boundary is required; (c) bundling distinct surfaces (registration ≠ canonization in some codifications) can dilute focus and slow each.

  Recommendation: SUPPORTED (with caveat that substrate-coupling verification per PRESUMPTION-117 is the precondition for bundling rather than parallel atomic tracks)
