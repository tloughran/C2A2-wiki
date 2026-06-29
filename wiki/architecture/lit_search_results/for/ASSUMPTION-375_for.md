SEARCH-FOR-ASSUMPTION-375:
  Date searched: 2026-06-27
  Original item: ASSUMPTION-375
  Original statement: "Peak-hour torn copies are environment (WAL checkpoint) contention, not a code defect; the 06:15 quiet window is the right production posture"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-375
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: torn copies attributed to checkpoint contention; off-peak window chosen as posture
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite WAL checkpoint documentation. - Concurrent writes and automatic checkpointing do increase the chance that a naive copy taken mid-checkpoint is internally inconsistent; contention is a real aggravating factor, supporting the environmental component of the diagnosis.
    2. Batch/ETL scheduling practice (off-peak extraction windows). - Scheduling extract jobs against low-write windows to reduce contention and torn reads is standard, well-documented operational practice.
    3. Workload-periodicity / diurnal-pattern literature. - Many workloads exhibit stable daily troughs; scheduling against a known quiet window is a recognized mitigation.

  Strength of support: Moderate

  Summary: The environmental half of the claim has real support: WAL checkpoint contention during high write volume genuinely raises torn-copy probability, and choosing an off-peak window is standard ETL practice. To that extent the 06:15 posture is reasonable. However, support for "not a code defect" is weaker - the same literature implies the copy METHOD (naive cp vs backup API) is the deterministic root, with contention only modulating its visibility (see 15b and ASSUMPTION-374).

  Caveats: Support is for "off-peak scheduling reduces torn copies," NOT for "the cause is purely environmental." If a plain file copy is used, the defect is present at all hours and merely less likely to manifest off-peak.

  Search scope: WAL checkpointing; off-peak ETL scheduling; workload periodicity. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
