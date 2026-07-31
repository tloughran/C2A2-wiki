SEARCH-FOR-PRESUMPTION-546:
  Date searched: 2026-07-26
  Original item: PRESUMPTION-546
  Original statement: [inferred] Calling the review-tool bug "benign this time" presumes damage is bounded by the visible outcome, but the same hardcoded-pids mechanism silently recorded 7 phantom APPROVEs and likely dropped 2 real proposals on 07-20 — disposition records are presumed trustworthy, so a record-corrupting defect that never errors persists across cycles.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-546
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a record-corrupting bug framed benign because its output looked plausible
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Silent Data Corruption (SDC) literature — Meta Engineering (2022), "Detecting silent errors in the wild"; Synopsys, "What is Silent Data Corruption." — SDCs are faults that "produce incorrect results without raising logs, exceptions, or error reports" and "can propagate across several services." Exactly the failure mode here: a defect whose output looks plausible corrupts records without erroring, so the corruption is invisible at the point of failure and compounds downstream. Strongly supports that "no error + plausible output" is not evidence of "no damage."
    2. Detection-latency literature — Bosilca et al., "On the Combination of Silent Error Detection and Checkpointing" (2013). — The defining hazard of silent errors is DETECTION LATENCY: corrupted data is identified "only when some numerical anomaly is detected... with an arbitrary delay." Supports the claim that a per-cycle "benign this time" judgment cannot bound damage, because the damage surfaces later, elsewhere, and the recorded APPROVEs/drops feed subsequent cycles.
    3. Fail-silent vs fail-safe design; audit-trail integrity — fault-tolerance patterns literature (fail-silent = "loss of functionality on fault, faults not propagated"; fail-safe adds "detect that a function is no longer functioning and switch to a safe state"); audit-trail = "immutable record of changes; incomplete trails reduce trust." — A record-corrupting defect that never errors is neither fail-silent (it DID propagate corrupted records) nor fail-safe (no detection, no safe state); it is fail-SILENT-and-WRONG. This is the worst quadrant. Supports treating disposition records as untrustworthy until the mechanism is audited, not presumed trustworthy.

  Strength of support: Strong

  Summary: Strongly supported. The silent-data-corruption and detection-latency literatures directly describe this defect class: a fault that emits no error and plausible output, so its damage is neither bounded by nor visible in the immediate outcome, and it propagates through records that downstream cycles trust. The audit-trail/fail-safe literature adds that a record-corrupting defect with no detection is the most dangerous fault posture (silent AND wrong), which is precisely why "benign this time" is an unsafe inference: the 7 phantom APPROVEs and 2 likely dropped proposals are already-realized corruption, not hypothetical risk. The correct posture is to treat the disposition records touched by the hardcoded-pids path as suspect and to add detection (an assertion/reconciliation), not to certify benignity per cycle.

  Caveats: "Benign this time" is not entirely empty — severity/priority triage is a real discipline (see 15b), and a low-blast-radius bug can be correctly deprioritized. The support here is specifically for record-corrupting silent defects, where the blast radius is by construction unknown at the point of failure.

  Recommendation: SUPPORTED
