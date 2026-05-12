SEARCH-FOR-PRESUMPTION-103:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-103
  Original statement: "Specialist outputs labeled by weekday-of-assignment; convention unstated"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-103
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as a labeling-convention presumption — outputs labeled by assignment-time, not execution-time, without articulation
      15a: Searched for supporting literature on assignment-vs-execution-time labeling conventions
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Workflow-orchestration literature (Airflow docs; Dagster docs) — assignment-time labeling (logical execution time) is a documented convention; both Airflow and Dagster use logical-date semantics by default.
    2. Cron / systemd literature — execution-time labeling is the simpler default; both conventions exist in practice.
    3. Distributed-systems literature (Kleppmann 2017) — both labeling conventions are valid; the canonical recommendation is to make the convention explicit.
    4. C2A2-internal: 2026-05-05 same-day catch-up — outputs labeled by their weekday assignment, not their actual fire date; matches Airflow's logical-date pattern.

  Strength of support: Weak-Moderate

  Summary: Both labeling conventions (assignment-time and execution-time) exist in practice; Airflow and Dagster default to assignment-time (logical-date) labeling. The convention C2A2 uses is not invalid, but the literature consistently recommends making the convention explicit. The "convention unstated" portion of the presumption is the unsupported element — implicit conventions are documented as drift risks.

  Caveats: (a) Assignment-time labeling is supported in literature; (b) the unstated-convention portion is the part that lacks support — implicit conventions drift; (c) downstream consumers may misread weekday-of-assignment as weekday-of-execution.

  Recommendation: PARTIALLY-SUPPORTED (convention itself is supported; unstated-convention portion is the gap; remediation is low-cost — document the convention)
