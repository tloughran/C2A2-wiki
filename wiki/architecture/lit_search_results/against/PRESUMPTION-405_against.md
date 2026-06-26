SEARCH-AGAINST-PRESUMPTION-405:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-405
  Original statement: "That a SIGKILL'd (Killed: 9) backfill left the DB consistent because counts rose and the cleanup trap fired"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-405
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: DB consistency after SIGKILL inferred from rising counts + a cleanup trap
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. POSIX signal semantics - SIGKILL (9) is uncatchable and cannot be trapped. - A shell/process "cleanup trap" CANNOT fire on SIGKILL; if a trap appeared to fire, it ran on a different signal/exit, so "the cleanup trap fired" is not evidence about the SIGKILL'd write.
    2. SQLite atomic-commit / integrity_check docs. - Consistency after abrupt termination is established by PRAGMA integrity_check (and reconciling expected rows), NOT inferred from row counts; the proper test is explicit, not circumstantial.
    3. Pillai et al. 2014 (OSDI), "All File Systems Are Not Created Equal"; crash-consistency literature. - Abnormal termination during bulk writes is a documented source of subtle inconsistency; "it looks like it worked" is exactly the unreliable signal these studies caution against.

  Strength of challenge: Strong

  Summary: The CONCLUSION (DB consistent) may well be true for SQLite (15a), but the EVIDENCE offered is invalid. "Counts rose" proves only partial progress, not completeness or integrity. "The cleanup trap fired" is impossible to attribute to a SIGKILL, because signal 9 is uncatchable - no trap runs on it - so that clause is a misreading. Inferring integrity from these is the silent-measurement / fail-quiet anti-pattern the project's own "fail-loud" value targets: torn or partial records can read as success. Integrity must be PROVEN (integrity_check + count reconciliation), not inferred.

  Specific risks: Treating a partially-completed/torn backfill as complete; downstream stats computed on incomplete data; the failure is silent and confidently misread as success.

  Mitigations available: Run PRAGMA integrity_check (and quick_check) + reconcile actual vs expected row counts against the source; make the backfill idempotent/resumable so re-running is safe; fail loud on mismatch rather than inferring success.

  STEELMAN:
    Item: PRESUMPTION-405
    Strongest counterargument: Both pieces of cited evidence are non-probative: counts can rise on an incomplete run, and a SIGKILL by definition runs no trap - so the integrity claim rests on signals that cannot establish it; the database may be consistent (SQLite design) but the inference used to assert it is unsound and would equally "confirm" a corrupted result.
    What would need to be true for C2A2 to be safe: integrity_check passes AND row counts reconcile to the expected total from the source.
    How to test: Run integrity_check + count reconciliation; re-run the idempotent backfill and confirm no additional rows are needed.

  Search scope: Signal semantics; SQLite integrity; crash consistency. Comprehensive.

  Recommendation: CHALLENGED
