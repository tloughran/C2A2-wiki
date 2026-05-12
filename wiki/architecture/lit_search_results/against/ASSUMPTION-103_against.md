SEARCH-AGAINST-ASSUMPTION-103:
  Date searched: 2026-05-10
  Original item: ASSUMPTION-103
  Original statement: "Today's 8-scheduled-task fire-rate is itself sufficient positive data point against the daemon-link-count = 1 regression hypothesis for THIS task (per-task-positive-evidence framing)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-103
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-09 EOD per-task evidence-frame observation
      15b: Searched for counter-evidence on per-task evidence transferability across selectively-affected tasks
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Failure-mode diagnosis literature (Vesely 1981; Stamatis 2003 FMEA) — per-task positive evidence is locally informative but does not generalize across selectively-affected systems without per-node disaggregation.
    2. Distributed-systems literature (Lamport 1978; Birman 2012) — selectively-affected systems are documented; per-node positive evidence requires per-node sample, not aggregate inference.
    3. Selection-effect literature (Heckman 1979) — tasks that fired are by construction the tasks for which we have positive evidence; this selects against the very tasks we want evidence about (the silent-skipped ones).
    4. C2A2-internal: ASSUMPTION-080 partition predicts selective-affectedness; per-task fire evidence cannot rule out other-task silent skips. PRESUMPTION-124 captures this failure mode.
    5. Master-narrative-gap (3 days missing) is the very thing the link-count = 1 regression was hypothesized to cause; per-task fire evidence about scheduled tasks does not transfer to wiki-orchestrator.

  Strength of challenge: Moderate (limited to the cross-task generalization, not the per-task framing itself)

  Summary: Per-task positive evidence is locally valid for THIS task but is challenged when used as global negative inference about other tasks. The fire-rate aggregation is per-system; the link-count = 1 hypothesis is per-task; selectively-affected tasks (e.g., wiki-orchestrator) cannot be ruled out by other-task fire evidence. The framing "for THIS task" is correct; the framing "8-task fire-rate is sufficient" risks the cross-task generalization that PRESUMPTION-124 captures.

  Specific risks: (a) Per-task evidence treated as cross-task evidence forecloses per-task investigation of selectively-affected tasks (e.g., wiki-orchestrator); (b) the master-narrative-gap that motivated the regression hypothesis is itself per-task evidence about wiki-orchestrator that the 8-task aggregate cannot address; (c) selection-effect — the tasks-that-fired are not random samples of all tasks.

  Mitigations available: (a) Per-task disaggregation (check wiki-orchestrator status today); (b) explicit framing "this task only"; (c) avoid cross-task inference from per-task positive evidence.

  Recommendation: PARTIALLY-CHALLENGED (per-task framing is supported; cross-task inference is challenged; PRESUMPTION-124 captures the cross-task generalization concern)

  STEELMAN:
    Item: ASSUMPTION-103
    Strongest counterargument: The per-task framing is correct — if THIS task fires, its link-count is >1 by ASSUMPTION-080's partition. But the "8-scheduled-task fire-rate" framing aggregates across tasks and risks transitive inference about selectively-affected tasks. The 3-day master-narrative-gap was the very thing the link-count regression hypothesis was meant to explain — per-task evidence about other tasks does not address the wiki-orchestrator status today. Selectively-affected systems are documented; "system fire-rate is positive" does not transfer to "every task in the system fired".
    What would need to be true for C2A2 to be safe: (a) Per-task evidence framed explicitly as per-task; (b) per-task disaggregation (check wiki-orchestrator status today); (c) avoid cross-task inference from per-task positive evidence.
    How to test: Check the wiki-orchestrator's status today directly — if it fired, per-task positive evidence; if it did not, the link-count regression hypothesis still has scope.
