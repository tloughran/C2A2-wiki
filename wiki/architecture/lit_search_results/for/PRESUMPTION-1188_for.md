SEARCH-FOR-PRESUMPTION-1188:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1188
  Original statement: "[inferred] Concurrency safety for shared-writer tasks is presumed to come from later copies noticing in-flight writes, not from mutual exclusion. Only the lit pipeline holds a lock. The wiki daily run (both firings ~04:36), reviewer-review state file and chat scrape rely on a late copy seeing recent output. Distinct from PRESUMPTION-1184 (what a stand-down ratifies): this is the race window before any output exists."

  Reading used for the FOR direction: support means literature showing that "detect another writer, then back off" without an atomic lock or compare-and-set is a recognised race (check-then-act / TOCTOU / lost update), and that standard overlap prevention for scheduled jobs uses mutual exclusion. 15a does not judge whether the named C2A2 tasks actually collided.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: cron overlap prevention (flock vs process/lockfile checks); optimistic concurrency, lost update, atomic compare-and-set. Not reached: flock(1) man page, Airflow max_active_runs docs, primary DB-theory texts. Kubernetes concurrencyPolicy was covered at snippet level in PRESUMPTION-1184_for and not re-searched.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1188
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from duplicate ~04:36 firings and unlocked shared-writer tasks (wiki daily run, reviewer-review state, chat scrape). Only the lit pipeline holds a lock. Scoped to the pre-output race window, distinct from PRESUMPTION-1184.
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — SUPPORTED

  Supporting evidence found: Yes, practitioner-grade and consistent. No source endorses detect-in-flight-writes as a substitute for mutual exclusion.

  Sources:
    1. Cron overlap guidance: ma.ttias.be, "Prevent cronjobs from overlapping in Linux"; Rackspace docs, "Managing Duplicate Cron Jobs"; Better Stack, "How to prevent duplicate cron jobs from running?"; Oracle-Base blog, "When Overlapping CRON Jobs Attack" (2023); dev.to (mochafreddo), "Understanding the use of flock in Linux cron jobs". [snippet only, practitioner]. The standard remedy is a non-blocking `flock -n` on a per-job lock file. The OS releases the lock on crash, so no stale lock is left. PID-file and pgrep-style checks are described as alternatives. One source warns that flock fails if instances use different lock paths. Relevance: direct support that the accepted practice is mutual exclusion. Check-then-create PID/lockfile schemes have a gap between check and write. That TOCTOU framing is 15a's inference; the snippets do not use the term. The lock-path warning also connects to PRESUMPTION-1187.
    2. Optimistic-concurrency documentation: Red Hat JBoss/Hibernate EntityManager guide §4.4, "Optimistic concurrency control"; OneUptime blog, "Prevent lost updates with optimistic locking" (2026); alchemiq docs, "Optimistic locking". [snippet only, vendor/practitioner docs]. OCC is valid only when the version check is atomic with the write (e.g. `UPDATE ... WHERE version = $n`). Application-level read-then-compare is weaker. Confusing detection with prevention corrupts data unless there is retry logic. Without a check, "last commit wins". Relevance: theoretical grounding. The optimistic alternative to locking needs an atomic compare-and-set at commit. "A later copy notices recent output" has no such atomic step, so it is neither pessimistic nor properly optimistic.

  Strength of support: Moderate

  Summary: Practitioner literature on scheduled jobs consistently prescribes mutual exclusion (flock, per-job lock files, scheduler concurrency policies) to prevent overlap. It does not prescribe having a late instance notice the earlier one's output. Concurrency-control documentation allows an optimistic alternative only when conflict detection is atomic with the write, and warns that detection without that atomicity lets lost updates through. Two copies started at roughly the same time, with no output yet to notice, is the textbook check-then-act window. The item's concern matches a recognised failure mode.

  Caveats:
    - No primary source was read (flock man page, Airflow docs, Kleppmann/Gray & Reuter). The TOCTOU link is 15a's inference from the described patterns.
    - All sources are practitioner or vendor material.
    - Idempotent tasks can tolerate overlap without locks. If a C2A2 task is genuinely idempotent, the risk is reduced. The literature supports the concern only for non-idempotent shared writers.
    - The "~04:36 both firings" timing claim was not checked (in-house).

  Recommendation: SUPPORTED

  (No NOVELTY-FLAG.)
