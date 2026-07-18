SEARCH-AGAINST-ASSUMPTION-465:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-465
  Original statement: Today's git persistence blocker is a stale unremovable `.git/index.lock` left by a concurrent 04:40 process (sandbox mount: "Operation not permitted"), a different proximate cause than 07-16's mount-denies-writes/no-creds diagnosis (A-463).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-465
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. DevToolbox Blog, 2026. "git index.lock ... by root cause (stale process, permissions, concurrency)." — Notes that an "Operation not permitted" on the lock points to the PERMISSIONS class, not merely a stale-process class; the fix for permission drift differs from clearing an orphaned lock.
    2. openai/codex Issue #19190, "Unable to create '.git/index.lock': Permission denied, has full permissions." — Shows the same surface error arising from ownership/mount semantics (container volume mounts, shared user contexts), i.e. the mount layer — the SAME root family as A-463's "mount denies writes."
    3. GeeksforGeeks, "How to Fix Git Error 'Unable to create ... index.lock'." — Attributes such failures to ownership drift from container volume mounts / shared user contexts, reinforcing a mount/permission root rather than a distinct lock-hygiene root.

  Strength of challenge: Moderate

  Summary: The literature challenges the "different proximate cause" framing. That the lock is UNREMOVABLE ("Operation not permitted") indicates a permission/mount constraint sitting on top of the lock — the same sandbox-mount write-permission layer that A-463 (07-16) diagnosed. So today's and yesterday's blockers may be two surface presentations of ONE root cause (sandbox mount denies `.git` writes/removals), not two genuinely independent causes. Treating them as distinct risks prescribing two narrow fixes when a single mount-permission remedy would resolve both.

  Specific risks: Mis-attributing to "orphaned lock from the 04:40 process" could send the fix toward lock-hygiene/worktrees while the real blocker (mount write permission) persists, wasting a cycle and leaving persistence broken.

  Mitigations available: Empirically separate the two: (a) test whether a fresh `.git/index.lock` can be created AND removed by the scheduled user on the mount; if removal is denied, it is the mount/permission root (A-463 family), not lock hygiene. Fix at the mount/credential layer resolves both.

  STEELMAN:
    Strongest counterargument: A stale lock and a mount-permission denial are not mutually exclusive, but the OPERATIVE blocker today is the permission that prevents removing/replacing the lock — which is the same class A-463 named. Calling it a "different proximate cause" risks fragmenting one root into two tickets and missing the shared fix.
    What would need to be true for the assumption to hold: The scheduled user must be able to create/remove index.lock on the mount (proving write permission exists), leaving a genuinely orphaned lock as the sole blocker — i.e., a lock-hygiene problem distinct from mount permission.
    How to test: In the sandbox, `touch .git/index.lock && rm .git/index.lock` as the scheduled user; success ⇒ distinct lock-hygiene cause (assumption holds); "Operation not permitted" ⇒ same mount/permission root as A-463.

  Recommendation: PARTIALLY-CHALLENGED
