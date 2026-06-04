SEARCH-AGAINST-PRESUMPTION-294:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-294
  Original statement: [inferred] The pipeline presumed "git threw no error" == "changes were staged/tracked"; a stale index.lock silently disabled staging for ~4 days while runs reported a clean tree, and a rider premise assumes clearing the lock today restores correctness for the lock-window days.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-294
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated methodological presumption (no-error==effect) plus a recovery rider.
      15b: Searched for when optimistic success signals are acceptable and the cost of verifying every infrastructure op.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (against the no-error==effect half); the RIDER is CHALLENGED-STRONGLY

  Sources:
    1. Optimistic success signals acceptable in low-stakes ops (optimistic-ack / at-least-once practice). — For many infra ops, trusting the success signal is fine; verifying every one is costly. Bounds the no-error==effect critique to consequential, silently-failing ops.
    2. Idempotency & recovery semantics (Kleppmann; at-least-once + verify). — Directly CHALLENGES the rider: clearing a stale lock restores forward staging but is NOT idempotent over the missed window; the 4 days of unstaged changes are not retroactively committed by lock removal.
    3. Recovery-completeness / RCA practice (Rootly recurrence/RCA lineage). — Post-outage correctness requires explicitly reconstructing the affected window's intended state, not assuming the blocker's removal heals history.

  Strength of challenge: Weak-Moderate (no-error==effect half); STRONG against the recovery rider

  Summary: The no-error==effect critique is mildly bounded — optimistic success signals are acceptable for low-stakes ops, so the rule should target consequential/silent-failure-prone ops (like the index write) rather than every op. But the presumption's RIDER ("clearing the lock restores correctness for the lock-window days") is strongly challenged: lock removal is forward-only and not idempotent over the missed window; the ~4 days of silently-skipped staging must be explicitly reconstructed and verified. This split is decisive for disposition (REVISE).

  Specific risks: If the rider stands, the system believes the 4-day window is healed when those changes remain unstaged/untracked — a second silent data-integrity gap layered on the first.

  Mitigations available: After clearing the lock, explicitly diff working tree vs last good commit for the lock window and re-stage/commit; verify via read-after-write. Add a stale-lock pre-flight check (couples ASSUMPTION-265).

  Recommendation: PARTIALLY-CHALLENGED (with the recovery rider strongly challenged)

  STEELMAN:
    Item: PRESUMPTION-294
    Strongest counterargument: Trusting "no error == done" is fine for cheap, frequently-repeated ops where a miss self-heals next run; the real defect is narrower — a silently-failing, NON-self-healing op (index write) on the data spine. And the recovery rider is simply wrong: removing the lock does not re-run four days of skipped staging, so correctness for the lock window must be actively reconstructed, not assumed.
    What would need to be true for C2A2 to be safe: The verify-the-effect rule is applied to consequential/non-self-healing ops (not blanket), AND a post-incident reconstruction of the lock-window changes is performed and verified rather than presumed healed.
    How to test: After clearing the lock, compare working tree to the last confirmed-staged commit; any un-tracked change from the lock window proves the rider false and must be recovered.
