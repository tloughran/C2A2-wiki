SEARCH-AGAINST-PRESUMPTION-1106:
  Date searched: 2026-10-03
  Original item: PRESUMPTION-1106
  Original statement (presumption under test): An advisory lock file coordinates concurrent writers even when the check-the-lock rule is absent from the instructions those writers follow.
  Candidate remedy (context only, not tested): Put lock check + staleness rule into the task spec; remove duplicate schedule.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1106
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-1731 and the lock file.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. flock(2) manual pages (4.3BSD / 2.11BSD / Linux / Apple), e.g. https://manpages.org/flock/2 [search-result] — "Advisory locks allow cooperating processes to perform consistent operations on files, but do not guarantee consistency (i.e., processes may still access files without using advisory locks possibly resulting in inconsistencies)." And: "a process is free to ignore the use of flock() and perform I/O on the file." This is the definitional refutation: advisory locks bind only participants that check them.
    2. Kleppmann, M., 2016, "How to do distributed locking" (blog), and Kleppmann, 2017, Designing Data-Intensive Applications, ch. 8 [background-knowledge; corroborated by search-results at antirez.com/news/101, system-design.space, hackernoon "The fencing gap"] — Even when every writer checks the lock, lease/timeout-based locks fail under process pauses or delays; safety requires the protected resource to reject stale writers via fencing tokens. A lock that writers do not even check offers strictly less than this.
    3. Cronitor, "How to prevent duplicate cron executions"; inventivehq; uptimia; Rackspace docs [search-result] — Duplicate cron/scheduled runs overlapping is a known failure mode; touch-file locks without PID/timeout checks suffer stale-lock and check-then-create race conditions; recommended practice is flock(1)/lockrun wrappers that enforce locking outside the job's own logic.

  Strength of challenge: Strong

  Summary: The presumption contradicts the definition of advisory locking: an advisory lock coordinates only processes that consult it, and the OS documentation states that non-participating processes may write freely. If the instructions an agent follows do not tell it to check the lock, the lock file is inert for that agent — it is documentation, not coordination. Even where checking is present, plain file-existence locks have check-then-act races and stale-lock problems, and lease-based schemes need fencing at the resource to be safe. Duplicate schedules are a well-documented source of exactly the concurrent-writer collisions the lock is presumed to prevent.

  STEELMAN:
    Item: PRESUMPTION-1106
    Strongest counterargument: Advisory locking is cooperative by definition; a writer whose instructions omit the lock check is a non-cooperating process, and the man pages say outright that such processes bypass the lock. For LLM agents the risk is sharper: a model may notice a lock file opportunistically on one run and ignore it on another, giving intermittent and unauditable coordination. Even a fully obeyed file lock lacks atomic acquire, staleness handling and fencing, so overlapping duplicate schedules can still interleave writes.
    What would need to be true for C2A2 to be safe: Every writer's task spec contains an explicit, atomic acquire step (e.g., O_CREAT|O_EXCL or flock), a staleness rule, and a release step; there is only one schedule per job; or writes are idempotent/append-only so collisions are harmless.
    How to test: Inventory every task spec that writes the shared file and grep for the lock check; inspect run logs for overlapping run windows; run two instances simultaneously and diff the result.

  Specific risks: Lost updates, interleaved/corrupted register files, duplicate entries from double runs.

  Mitigations available: Lock check in spec (the candidate remedy); OS-level flock wrapper; single scheduler; idempotent writes keyed by run ID; fencing token/version check before write.

  Caveats: Evidence is from OS and distributed-systems practice, not LLM agents specifically; an agent might incidentally respect a visible lock file, but that is not coordination by design.

  Search scope: preliminary search (2 searches, 0 fetches) plus well-established background literature; independent of 15a.

  Recommendation: CHALLENGED
