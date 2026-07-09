SEARCH-AGAINST-PRESUMPTION-448:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-448
  Original statement: "[inferred] Racing concurrent writers is an acceptable coordination mechanism for repo operations."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-448
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the late-evening events (lock deleted under uncertainty, bare push retried after non-fast-forward rejection) that "just race and see who wins" was operating as the de facto coordination mechanism
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. MITRE CWE-367, "Time-of-check Time-of-use (TOCTOU) Race Condition." — Canonical weakness classification: any check-then-act sequence with a window between check and use (e.g., "no other git process seems to be running" → delete lock → operate) is a defined vulnerability class, not an acceptable mechanism; the check and use must be atomic.
    2. Kung, H.T., Robinson, J.T., 1981. "On Optimistic Methods for Concurrency Control." ACM TODS. (Via Wikipedia/OCC syntheses.) — Optimistic concurrency is only sound when paired with validation (conflict detection) and rollback/retry. Racing without a validation-retry loop is not OCC; it is the lost-update problem.
    3. binaryigor.com, "Optimistic vs Pessimistic Locking: concurrency control, conflicts, lost updates, retries and blocking." — Explicit treatment of lost updates when concurrent writers proceed without version checks; on conflict the transaction must be rolled back and retried, never blindly re-applied.
    4. DEV Community (rijultp), "Fixing Common Git Lock Errors"; DevToolbox 2026 "git index.lock file exists: safe fix by root cause." — Both state removing .git/index.lock while another git process is active can corrupt the repository; the documented safe procedure is verify-no-live-holder-first, i.e., the lock deletion under uncertainty in the C2A2 incident violated the published procedure.
    5. DeepStrike, "What Is Time of Check Time of Use (TOCTOU)?" — Race windows pass normal testing because code works 99.999% of the time; racing "works" until it doesn't, which is precisely why absence of past corruption is not evidence of an acceptable mechanism.
    6. Microsoft Learn, "Handling Concurrency Conflicts" (EF Core) and Azure Cosmos DB OCC docs. — Industry-standard guidance: concurrent writers require either pessimistic locks or version-checked writes with retry; git's non-fast-forward rejection is exactly such a version check, and the correct response is fetch/rebase/retry, not force or race.

  Strength of challenge: Strong

  Summary: Concurrency-control literature from Kung & Robinson (1981) through current industry documentation is unanimous: concurrent writers need either mutual exclusion (pessimistic) or conflict detection with rollback-and-retry (optimistic); "race and hope" is neither — it is the textbook lost-update anti-pattern, and check-then-act under uncertainty is CWE-367. The incident's two moves map cleanly onto known failure modes: deleting a lock file without verifying the holder is dead is the documented repo-corruption path, and treating a non-fast-forward rejection as an obstacle rather than as git's conflict-detection signal misreads the one safety mechanism that was working. Notably, git's push rejection means git itself provides the optimistic-concurrency validation step; the challenge is that the workflow around it (no pull-rebase-retry discipline, manual lock deletion) discards that protection. The absence of corruption so far is survivorship, not validation — TOCTOU literature emphasizes race windows are rarely hit in testing and routinely hit at scale.

  Specific risks: Lost commits when a racing writer's push or index write silently overwrites the other's work; repository corruption if a live-held lock is deleted mid-write (half-written index/HEAD); escalation under pressure from rejected push to force push, destroying the remote history that constitutes C2A2's evidence chain; intermittent, unreproducible failures that consume debugging time near deadlines.

  Mitigations available: Adopt the documented safe-lock procedure (check for live git PIDs and lock age before any lock removal; never delete under uncertainty); mandate fetch→rebase→push with bounded retry as the only response to non-fast-forward rejection; ban force-push on shared branches via server-side protection; move to per-writer branches/worktrees so writers never race on the same ref (see PRESUMPTION-446 mitigations); add a session-level advisory lock with owner+PID+timestamp metadata making staleness checkable.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-448
  Strongest counterargument: Every mature concurrency framework — databases, distributed systems, git itself — treats an uncoordinated write race as a defect to be engineered out, because its failure mode is silent data loss rather than a visible error. The C2A2 incident contains both halves of the anti-pattern in one evening: a check-then-act lock deletion (CWE-367) whose safe alternative is explicitly documented, and a conflict-detection signal (non-fast-forward rejection) that the workflow had no principled procedure for handling. The system survived, but TOCTOU literature is explicit that surviving a race window is the expected outcome most of the time and provides no evidence of safety; for a system whose git history is its evidentiary substrate, the tail risk is loss of the very artifact the system exists to maintain.
  What would need to be true for C2A2 to be safe: Writers either never overlap (enforced scheduling) or every conflicting write is detected and resolved by a defined retry/merge procedure; lock removal only ever follows a verified-stale check.
  How to test: Grep session logs and reflog for the incident window to confirm no commits were lost; run a controlled two-writer race in a sacrificial clone to demonstrate the lost-update outcome; verify a written procedure now exists for (a) stale-lock verification and (b) non-fast-forward response, and that agents follow it in a drill.
