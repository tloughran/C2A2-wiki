# PRESUMPTION-1188 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Run id sched-lit-2026-10-27-6d9c5b33. Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": evidence that "mutual exclusion is required" is overstated, or that the implied remedy (add locks) is not clearly better. I did not dispute the in-house facts: the double firing at about 04:36 and the absence of locks outside the lit pipeline.

```
SEARCH-AGAINST-PRESUMPTION-1188:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1188
  Original statement: "[inferred] Concurrency safety for shared-writer tasks is presumed to come
    from later copies noticing in-flight writes, not from mutual exclusion. Only the lit pipeline
    holds a lock. ... this is the race window before any output exists."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1188
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from shared-writer tasks (daily wiki run, reviewer-review state, chat scrape)
           that rely on a late copy seeing recent output.
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial. It challenges "mutual exclusion is the only accepted
    remedy". It does not support C2A2's current notice-recent-output practice.

  Sources:
    1. Kung, H.T. & Robinson, J.T., 1981. "On Optimistic Methods for Concurrency Control." ACM
       TODS 6(2). [secondary; abstract and summaries only; PDF located, not read]
       — Direct challenge to "locks are required". Non-locking (optimistic) control is an
       accepted substitute for locking and has higher throughput when conflicts are rare. For
       jobs that collide once a day, optimistic control is the textbook-preferred regime.
       Boundary: optimistic control is safe only because a validation step runs atomically at
       commit (read set checked against concurrent writes, then write or abort). Noticing output
       before starting is not that validation step. It is the race window this item names.
    2. Lock-file practice: O'Reilly "Secure Programming Cookbook" ch. 2.9; FreeBSD flock(2);
       Python-list (2001) and openlock docs on PID reuse. [snippet only]
       — Challenges the implied remedy. File-based locks bring their own failures: stale locks
       after a crash, which block all later runs; a race in PID-based staleness checks; and
       advisory locks that bind only cooperating processes. C2A2's one lock already shows a
       stale-copy failure (see PRESUMPTION-1187). Adding locks everywhere adds that failure class
       to each task.

  Strength of challenge: Weak to Moderate. It is moderate against the framing that only
    mutual exclusion is legitimate. It is weak or none against the concern itself, because the
    current practice meets neither the optimistic nor the pessimistic standard.

  Summary: The literature does not require mutual exclusion. Optimistic, detect-and-abort
    schemes are mainstream and preferable under low contention, which fits a task that fires at
    most twice a day. But they detect conflicts at write time, atomically, and C2A2's tasks
    detect them informally at start time. The real gap is the missing commit-time check, not
    the missing lock. Locks are also not free: stale locks would turn a rare duplicate write into
    a skipped run.

  Specific risks: (a) Rolling out lockfiles to every task turns occasional double-writes into
    stale-lock skips, which are silent unless monitored (see PRESUMPTION-1189). (b) Labelling the
    current practice "optimistic" would wrongly credit it with a validation step it lacks.

  Mitigations available: Use a compare-and-swap style write (version stamp or hash checked
    immediately before rename, abort on mismatch). Or use kernel advisory locks (flock), which
    release on process death. Prefer preventing the double fire at the scheduler.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1188
  Strongest counterargument: "Detect, don't exclude" is a respected design (OCC). At C2A2's
    contention level of roughly one collision per day, it is the better choice: locks add
    stale-lock and liveness failures that a twice-daily job does not need. The presumption is
    wrong only in where detection happens. Moving detection to an atomic check at write time
    gives safety without locks.
  What would need to be true for C2A2 to be safe: every shared-writer task validates a version or
    hash and writes in one atomic step (temp file, compare, rename), aborting on mismatch.
  How to test: Fire two copies 1s apart against a sandbox state file. Lost updates show the
    current practice is unsafe. Repeat with a version check before rename and confirm one copy
    aborts.
```

Source quality: snippets and secondary sources only. I did not read Kung-Robinson in full. The contention estimate is in-house (two firings a day), not from the literature.
