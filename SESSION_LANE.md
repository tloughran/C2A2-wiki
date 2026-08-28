# Session lane declaration — paste at the top of each concurrent session

Coordination happens at the only point that sees every session: you, at session start.
Not a lockfile. A lockfile on this mount cannot be deleted if it gets stuck
(`rm` is forbidden), which is the exact failure mode that killed sync_vault on 08-23.

---

## Paste this, filled in:

```
LANE: <short name, e.g. "sociogram-z" or "commentary-reconcile">
WRITES: <explicit files or directories this session may write>
GIT: yes | no
REGEN: yes | no
CONCURRENT: <lane names of other sessions running now, or "none">

Rules for this session:
- Write nothing outside WRITES. If the task needs a file outside it, STOP and tell me
  rather than widening the lane yourself.
- GIT: no  ->  run no git commands at all, `git status` included. A read-only status
  leaves a 0-byte .git/index.lock on this mount that cannot be removed normally.
- REGEN: no  ->  do not run regen_sociogram.sh. It rewrites a 4MB artifact whole;
  two concurrent regens are silent last-writer-wins.
- Never run git or regen 20:55-21:15 any day, or 19:45-21:30 Sunday. See the
  collision window below.
- Close the session by reporting: files written, anything irreversible, anything
  skipped or assumed.
```

---

## The rule that makes lanes work

**Two sessions may run concurrently if and only if their WRITES sets are disjoint.**
Reading is unrestricted — read whatever you need. Partition by write-target, never by
clock, because the scheduled agents do not respect your clock.

Two resources are **singletons** and cannot be shared no matter how the lanes are drawn:

| singleton | why |
| --- | --- |
| **git** on this repo | one index, one lock; concurrent writers corrupt or deadlock |
| **regen_sociogram.sh** | whole-artifact rewrite, no merge, silent overwrite |

If both tasks need git, they are not concurrent tasks. Sequence them.

---

## Verified collision window (2026-08-24)

**Cloud scheduled tasks — SAFE, none touch this repo's git:**

| time (Eastern) | task | touches |
| --- | --- | --- |
| 08:00 daily | C2A2 Pages deploy check | WebFetch only, explicitly no git |
| 08:00 weekdays | Morning brief | calendar/mail |
| 08:00 daily | System health check | monitoring services |
| 14:00 Thursdays | Demo Lab weekly sweep | Gmail + its own artifact |

Three stack inside 08:00-08:20 but none write here. This window is fine for repo work.

**Mac launchd jobs — THIS is the hazard:**

| time (Eastern) | job | holds git |
| --- | --- | --- |
| 21:00 daily | `sync_vault.plist` | yes — commits and pushes |
| 20:00 **Sundays** | `weekly_review.plist` | likely — long-running |

Plus the agent stack documented in `feedback_evening_agent_collision_kills_sync`:
19:50 and 19:57 sewing-agent writes, 20:03 bootstrap audit.

**Sunday 19:45-21:30 has five occupants.** That is what failed on 2026-08-23: pid 56282
held `.git/index.lock` continuously from before 21:00:18 to past 21:01:34, sync_vault
waited 90s across six attempts, refused to steal a live lock, and failed loud. The
lock-wait logic worked correctly and still lost. Nothing was committed or pushed.

Do not schedule a session of any size into that window, and do not leave one running
into it.

---

## Session close, every time

```sh
cd "$HOME/Documents/Claude/Projects/RC Karpathy Wiki Project"
L=.git/index.lock
[ -f "$L" ] && [ ! -s "$L" ] && mkdir -p _to_delete && mv "$L" "_to_delete/index.lock.cowork-$(date +%s)"
```

Only ever move a **0-byte** lock. A non-empty lock means a real write is in flight —
leave it. `mv`, not `rm`.
