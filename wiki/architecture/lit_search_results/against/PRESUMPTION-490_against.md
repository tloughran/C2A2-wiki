SEARCH-AGAINST-PRESUMPTION-490:
  Date searched: 2026-07-18
  Original item: PRESUMPTION-490
  Original statement: [inferred] Scripts that run correctly when invoked by a human on the Mac are presumed to behave identically when invoked headless by the scheduler in the sandbox (HOME, filesystem reach, credentials, lock state) — falsified twice today (metabolism `~/`, c282 index.lock).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-490
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from two same-day context failures
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. 12factor.net, "X. Dev/prod parity." — Even the canonical parity advocate concedes perfect parity "isn't always possible" (e.g., systems that can never run locally). Absolute cross-context identity is not the bar; keeping the GAP SMALL is.
    2. MCIS Lab, IEEE-SW, "Hermeticity of Artifact-based Build Technologies." — Empirically, "none of the studied Bazel-using projects has a completely hermetic build process." Full hermeticity is unattained even by teams pursuing it — so demanding it of C2A2's scripts sets an unreachable standard.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is not that the presumption is safe but that its remedy can be over-scoped. Perfect parity/hermeticity is acknowledged as unattainable in practice, so the actionable target is not "guarantee identical behavior" but "shrink and monitor the specific context-deltas that matter (HOME, mount reach, creds, locks)." Two failures identify the deltas that bit; they do not warrant a wholesale hermetic rebuild. A cheap default assumption of parity, paired with per-delta checks, may beat an expensive pursuit of total context-identity.

  Specific risks: Over-correcting toward full hermeticity could consume disproportionate effort for diminishing returns, while under-correcting leaves the same four deltas to recur.

  Mitigations available: A small context-parity checklist run at script start (assert HOME, assert mount path exists, assert creds/lock state) catches the known deltas cheaply without a hermetic overhaul.

  STEELMAN:
    Strongest counterargument: The presumption is real, but "falsified twice" is thin evidence for a systematic law; the correct response is a targeted preflight assertion on the four named deltas, not a claim that all Mac-correct scripts are untrustworthy headless. Treat it as a checklist gap, not a paradigm failure.
    What would need to be true for the presumption to be low-risk: A startup preflight must assert the handful of context invariants each script depends on, failing loud if any is violated.
    How to test: Add the preflight to the two failing scripts; re-run headless; if both pass and no new deltas surface across a week, the risk is bounded by the checklist.

  Recommendation: PARTIALLY-CHALLENGED
