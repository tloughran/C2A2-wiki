SEARCH-FOR-PRESUMPTION-294:
  Date searched: 2026-06-02
  Original item: PRESUMPTION-294
  Original statement: [inferred] The pipeline presumed "git threw no error" == "changes were staged/tracked"; a stale index.lock silently disabled staging for ~4 days while runs reported a clean tree, and a rider premise assumes clearing the lock today restores correctness for the lock-window days.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-294
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated methodological/structural presumption (no-error==effect-achieved) plus a recovery rider.
      15a: Searched silent-failure / liveness-vs-safety, verification of side effects, the "no error" vs "intended effect" gap.
    Current status: SUPPORTED (the silent-failure concern is well-grounded)

  Supporting evidence found: Yes (for the silent-failure half)

  Sources:
    1. Safety vs liveness (Hillel Wayne; Lamport). — "git threw no error" is a safety-style observation; "changes were staged" is the liveness property that actually matters, and the former does not entail the latter. Strong support that the equation is invalid.
    2. Verify-the-side-effect / read-after-write (consistency literature; PREMISE-045 family). — Side effects must be confirmed by reading resulting state; a clean-tree report from a process that could not write the index is precisely the unverified-side-effect failure.
    3. Idempotency & recovery semantics (Kleppmann; at-least-once + verify). — Recovery after a silent outage requires re-establishing the intended state for the affected window, not merely removing the blocker — directly relevant to the rider premise (see Caveats).

  Strength of support: Strong (silent-failure half); the recovery RIDER is NOT supported (see Caveats).

  Summary: The core presumption — that "no git error" was wrongly equated with "changes staged" — is strongly supported: it is a textbook safety-vs-liveness / unverified-side-effect failure, empirically realized over ~4 days. Support is for the presumption being a REAL defect, mirroring ASSUMPTION-265's verify-don't-infer remedy.

  Caveats: The RIDER premise ("clearing the lock today restores correctness for the lock-window days") finds NO support and is likely false: removing a stale lock fixes forward staging but does not retroactively stage or commit the 4 days of changes that were silently skipped; those must be explicitly reconstructed/verified for the lock window. This split (supported core, unsupported rider) is the basis for 15c routing to REVISE.

  Recommendation: SUPPORTED (core); rider NO-SUPPORT-FOUND
