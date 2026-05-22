SEARCH-AGAINST-ASSUMPTION-189:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-189
  Original statement: "Recurring index.lock + 716/356 morass caused by colliding/silently-failing scheduled commit agents."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-189
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: recurring index.lock and 716/356 staging morass diagnosed as concurrent scheduled commit agents colliding.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Chacon, S. & Straub, B. "Pro Git" (stale-lock note). — A stale index.lock from a single crashed/killed process produces identical symptoms without any collision.
    2. NFS/networked-filesystem locking literature. — Lock files on networked or synced filesystems (e.g., cloud-synced vault dirs) can fail to release, mimicking concurrency bugs.
    3. Postmortem practice (Allspaw, 2012; Google SRE 2016). — Attributing a recurring failure to a single cause before instrumentation is a classic premature-diagnosis trap.

  Strength of challenge: Moderate

  Summary: The symptom (recurring index.lock, staging morass) is consistent with at least three causes: concurrent agents (the premise), a single crashed process leaving a stale lock, or filesystem-level lock-release failure on a synced directory. Without per-process logging, the collision hypothesis is under-instrumented. The challenge does not refute it but shows it is one of several causes that demand the same first move: serialize and instrument.

  Specific risks: Fixing only the concurrency angle while a stale-lock or FS-sync cause persists; recurrence after a 'fix' that addressed the wrong cause.

  Mitigations available: Serialize all scheduled git ops behind one exclusive lock (flock); add per-agent commit logging + lock-acquire/release receipts; clear stale locks on startup with a guard.

  Recommendation: PARTIALLY-CHALLENGED (alternative causes share the symptom)

  STEELMAN:
    Item: ASSUMPTION-189
    Strongest counterargument: The same index.lock symptom is produced by a single crashed process or a synced-filesystem lock that never releases — neither involves collision. Declaring 'colliding agents' the cause before any per-process instrumentation risks a fix that does not stop recurrence.
    What would need to be true for C2A2 to be safe: Safe once scheduled git ops are serialized AND logged, so the next occurrence (if any) is attributable.
    How to test: Add flock + per-op logging; if index.lock recurs with only one logged writer, the collision hypothesis is falsified and FS/stale-lock is implicated.
