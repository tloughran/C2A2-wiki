SEARCH-AGAINST-PRESUMPTION-124:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-124
  Original statement: "Today's 8-task fire-rate treated as global negative inference for daemon-link-count regression — wiki-orchestrator status today not in evidence frame"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-124
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD per-task-to-cross-task inference analysis
      15b: Searched for counter-evidence on global-from-partial inference for selectively-affected systems
    Current status: CHALLENGED

  Sources:
    1. Failure-mode diagnosis literature (Vesely 1981; Stamatis 2003 FMEA) — per-node positive evidence does not transfer to other nodes for selectively-affected systems.
    2. Distributed-systems literature (Lamport 1978; Birman 2012) — selectively-affected systems require per-node disaggregation.
    3. Selection-effect literature (Heckman 1979) — sample selected by the outcome being inferred is canonical selection bias.
    4. PRESUMPTION-114 (recency-priority cause attribution) cluster — same failure mode at adjacent layer.
    5. C2A2-internal: ASSUMPTION-080 partition (>1 fires; =1 silent skip) explicitly predicts selective-affectedness; wiki-orchestrator status today is not in the evidence frame of the 8-task aggregate.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged by failure-mode-diagnosis, distributed-systems, and selection-effect literatures. The challenge is uniform: global-from-partial inference for selectively-affected systems is canonical selection bias. The wiki-orchestrator-not-in-evidence-frame gap is the predicted failure mode.

  Specific risks: (a) Cross-task generalization from per-task evidence forecloses per-task investigation of selectively-affected tasks; (b) wiki-orchestrator status not addressed by aggregate fire-rate; (c) selection bias — the tasks-that-fired are not random samples.

  Mitigations available: (a) Per-task disaggregation (check wiki-orchestrator status today); (b) explicit framing "this task only" for per-task evidence; (c) avoid cross-task inference from per-task positive evidence.

  Recommendation: CHALLENGED (literature consensus strong; selection-bias failure mode)

  STEELMAN:
    Item: PRESUMPTION-124
    Strongest counterargument: The 8-task aggregate is exactly the wrong frame for the question being asked. The question is whether wiki-orchestrator was silent-skipped today; the evidence offered is that 8 OTHER tasks fired. These are independent under ASSUMPTION-080's partition by construction. The selection-effect is structural: the tasks-that-fired are by definition the tasks for which we have positive evidence; the silent-skipped tasks (if any) are by definition NOT in the evidence frame. Treating other-task evidence as global is the canonical selection bias.
    What would need to be true for C2A2 to be safe: (a) Per-task check on wiki-orchestrator specifically; (b) explicit per-task framing; (c) aggregate fire-rate framed as positive evidence about THOSE tasks only.
    How to test: Check wiki-orchestrator's status today directly; if it fired, per-task positive evidence; if it did not, the regression hypothesis still has scope and the aggregate evidence was not addressing it.
