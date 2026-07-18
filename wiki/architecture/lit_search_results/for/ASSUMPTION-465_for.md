SEARCH-FOR-ASSUMPTION-465:
  Date searched: 2026-07-18
  Original item: ASSUMPTION-465
  Original statement: Today's git persistence blocker is a stale unremovable `.git/index.lock` left by a concurrent 04:40 process (sandbox mount: "Operation not permitted"), a different proximate cause than 07-16's mount-denies-writes/no-creds diagnosis (A-463).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-465
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-17 EOD run (persistence blocked by index.lock)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. anthropics/claude-code Issue #11005, "Stale `.git/index.lock` files created by CC's background git operations block user git commands." — Directly documents the exact failure mode: a concurrent/background git process leaves an index.lock that blocks subsequent commands. Establishes this proximate cause is real and recurring in this very toolchain.
    2. anthropics/claude-code Issue #57102, "Stale .git/index.lock left behind in worktrees during normal CLI operation (macOS)." — Confirms the macOS + worktree context and that the lock persists after the owning process exits, requiring external removal.
    3. Microsoft Learn / Azure Repos, "Git index.lock file." — Canonical description: git creates index.lock as a mutex for write ops (add/commit/pull); a terminated or unresponsive process leaves it behind and blocks other git processes. Grounds the mechanism.
    4. DevToolbox Blog, 2026. "git index.lock file exists: safe fix by root cause (stale process, permissions, concurrency)." — Enumerates precisely the three root causes named in the assumption (stale process, permissions, concurrency) and separates them as distinct diagnoses.

  Strength of support: Strong

  Summary: The literature strongly confirms both the mechanism and the specific instance. A stale index.lock is a standard git mutex artifact left behind when a concurrent write process is killed or hangs; two open Claude-Code issues document this exact behavior for background/scheduled git operations on macOS. The claim that today's blocker (orphaned lock) is a DIFFERENT proximate cause than 07-16's (mount-denies-writes / no-creds, A-463) is well supported: the sources treat lock-contention, permissions, and credentials as separable failure classes, so day-over-day diagnoses can legitimately differ.

  Caveats: "Operation not permitted" on lock REMOVAL points to a permissions/mount layer on top of the lock itself, so the true fix may be compound (lock hygiene AND mount-write permission), not lock hygiene alone. Support is for the diagnosis category; it does not by itself prove the 04:40 process was the specific owner.

  Recommendation: SUPPORTED
