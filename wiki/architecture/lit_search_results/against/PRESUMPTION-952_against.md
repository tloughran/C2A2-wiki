SEARCH-AGAINST-PRESUMPTION-952:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-952
  Original statement: "[inferred] That when a script cannot run in an environment, the environment is
    what must change — that the byte-copy the extractors perform is a fixed property of the task rather
    than a choice in the code."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-952
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an absent alternative named identically by two independent runs; high-confidence,
        both reports quote the copying mechanism and neither questions it.
      15b: Searched for challenging literature; retrieved SQLite's own URI documentation, which supports
        the presumption's critics on one path (`mode=ro`) and supports the copy on the other
        (`immutable=1`/`nolock=1` carry an explicit corruption warning). Reported both directions.
    Current status: PARTIALLY-CHALLENGED

  Register pre-check:
    - PREMISE-146 (ACTIVE) — "A TASK SPECIFICATION'S SATISFIABILITY IS A PROPERTY TO BE ESTABLISHED, NOT A
      DEFAULT." Directly on point: nobody established that a 6 GB copy is required by the task.
    - PREMISE-115 (ACTIVE) — before an agent is called broken, check whether its specification ever
      instructed the behaviour; specification and design issues are the largest single category of
      multi-agent failure (41.8%). Applied here: before the host is called too small, check whether the
      requirement was ever established.
    - PREMISE-098 (ACTIVE) — scripts that run correctly interactively must not be presumed to behave
      identically headless in the sandbox; each scheduled script asserts its context invariants —
      filesystem/mount reach, lock state — at startup and fails loud. **Lock state is the invariant that
      decides this item**, and PREMISE-098 already names it.
    - PREMISE-092 (ACTIVE) — the SQLite safe-recovery sequence, including "take a raw file-level copy
      first" and the WAL-reset corruption bug band (3.7.0–3.51.2, fixed 3.51.3). Cuts FOR the copy in the
      recovery case; note the scope difference — 092 governs a CORRUPT database, not a healthy read.
    - PREMISE-107 (ACTIVE) — where two candidate mechanisms present the same symptom, the discriminating
      test is the operative construct. Two mechanisms present "cannot run in sandbox": host too small, and
      code copies unnecessarily. The discriminating test is one command.
    - PREMISE-153 (ACTIVE) — ephemeral-compute exposure; relevant to where any temp copy would live.

  Challenging evidence found: Partial — and it cuts in both directions. Reporting honestly which way each
    source cuts, as instructed.

  Sources:
    1. SQLite documentation, "Uniform Resource Identifiers" (sqlite.org/uri.html), §3.3 Recognized Query
       Parameters. — **VERIFIED** (page retrieved and read in full, 2026-09-11) — Three findings, and they
       do not all point the same way:
         (a) **CUTS AGAINST THE PRESUMPTION (i.e. for the critics).** `mode=ro` opens a database read-only
             with normal locking and change detection intact. No copy is involved and no corruption
             warning attaches. If the sandbox mount supports POSIX advisory locking, this is the correct
             mechanism for a read-only consumer and the 6 GB copy is simply unnecessary work.
         (b) **CUTS FOR THE PRESUMPTION (i.e. for the copy).** `immutable=1` — the parameter one would
             reach for on a read-only or lock-less mount — carries an explicit warning in the official
             documentation: SQLite "skips all file locking and change detection on immutable database
             files," and "if this query parameter… asserts that a database file is immutable and that file
             changes anyhow, then SQLite might return incorrect query results and/or SQLITE_CORRUPT
             errors." Against a LIVE, concurrently-written database, `immutable=1` is not a safe
             substitute for a copy. This is the strongest single fact in this file and it cuts against the
             `--no-copy` proposal as naively stated.
         (c) **ALSO CUTS FOR THE PRESUMPTION.** `nolock=1` carries a parallel warning: "If two or more
             database connections try to interact with the same SQLite database and one or more of those
             connections has enabled 'nolock', then database corruption can result. The 'nolock' query
             parameter should only be used if the application can guarantee that writes to the database are
             serialized."
       Net reading: the copy is NOT a fixed property of the task — `mode=ro` exists and is the right
       answer where locking works. But the copy is also not arbitrary: it is the mechanism that guarantees
       the consistent snapshot, and the two cheap substitutes named in the presumption's own text
       (`immutable=1`, WAL read) are documented as unsafe against a concurrent writer. The presumption is
       wrong about "fixed property"; its critics would be wrong to reach for `immutable=1`.
    2. SQLite Forum, "Opening DB from readonly filesystem (btrfs snapshot)" (sqlite.org/forum). —
       SECONDARY (search summary; thread located, not read in full) — The canonical safe use of
       `immutable=1` is against a filesystem-level SNAPSHOT, which is genuinely immutable. This names the
       real third option for C2A2 and it is the best one: a filesystem or storage-layer snapshot gives the
       consistency guarantee the copy provides at near-zero space cost, if the host filesystem supports it
       (APFS snapshots on macOS do).
    3. SQLite Online Backup API / `VACUUM INTO`. — UNVERIFIED (not retrieved this run; named from
       PREMISE-092's own text, which cites the online backup API) — The documented mechanism for taking a
       consistent copy of a live database without a raw byte-copy, and it can be size-bounded and
       incremental. Recorded as the fourth option, unverified this run.
    4. Requirements-engineering literature on questioning the requirement before the platform — sought and
       NOT usefully found. NEGATIVE RECORDED: I searched for the engineering-literature framing ("is the
       requirement real?" before "is the platform adequate?") and retrieved nothing citable beyond the
       general goal-driven RE line already held in PREMISE-146. This limb of the search failed and I am
       not manufacturing a source for it. PREMISE-146 is the register's own statement of it and is better
       than anything I found.

  Strength of challenge:
    - Limb A, "the byte-copy is a fixed property of the task": **Strong** challenge. Refuted by
      documentation I read directly. `mode=ro` and snapshot-based reads both exist; neither requires
      copying 6 GB. PREMISE-146 independently forbids treating the requirement as a default.
    - Limb B, "therefore a `--no-copy` path is simply available": **Weak** challenge — and this is the
      limb where the honest answer runs against the critics. Whether `mode=ro` works depends entirely on
      whether the sandbox's mount supports POSIX advisory locking; the fallbacks that do not need locking
      (`immutable=1`, `nolock=1`) both carry documented corruption warnings against a live writer. So the
      presumption's critics do not get a free win either.
    - Limb C, "the question migrated to 'which host' and never migrated back to 'why a copy'": **Strong**,
      and it is the limb that matters. Two independent runs quoted the copying mechanism and neither asked
      about it, and the intake queue has carried "needs a `--no-copy` path or a retitle" unchanged for six
      days.
    The recommendation rests on Limbs A and C.

  Summary: The presumption is wrong in the form 14b states it — the copy is a choice in the code and
    SQLite documents at least two alternatives — but the naive remedy is also wrong, and I would be
    misreporting the source if I did not say so. `mode=ro` is the correct mechanism and involves no copy;
    it requires working file locking on the mount, which is precisely the invariant PREMISE-098 already
    requires scheduled scripts to assert. The two lock-free alternatives named in the presumption's own
    text — `immutable=1` and a bare WAL read — are documented by SQLite as producing incorrect results
    or SQLITE_CORRUPT if the file changes anyway, which against a live 6 GB database it will. The genuinely
    best option surfaced by this search is the one neither side named: a filesystem-level snapshot, which
    is the only configuration in which `immutable=1` is safe and which costs almost no space. The whole
    question is settled by one command in the sandbox and 14b is right that the answer is today's.

  Specific risks: `metabolism_data.json` is seven days cold and a downstream health check reads it as
    current — which is PREMISE-100's false-green and PRESUMPTION-955's cost, realised. Beyond the specific
    instance, the shape recurs for every future consumer of a database that outgrows the sandbox, and the
    databases are growing, so the failure rate is increasing. A second, quieter risk: if a `--no-copy`
    path is implemented as `immutable=1` because it is the obvious lock-free option, the estate trades a
    disk-space error (loud, correct, stops the run) for silent wrong query results (PREMISE-128's
    silent-data-corruption class). That would be a strictly worse outcome than today's, and it is the
    likely outcome of acting on this presumption without reading the documentation.

  Mitigations available:
    - **Run the discriminating test today** (PREMISE-107): one `sqlite3 'file:/path/db?mode=ro'` open from
      the sandbox against the live file, plus one trivial query. Either locking works or it does not.
    - **If locking works:** `mode=ro`, no copy, done. Add PREMISE-098's startup assertion that the mount
      supports locking, and fail loud if it stops doing so.
    - **If locking does not work:** take an APFS (or equivalent) snapshot and open the snapshot with
      `immutable=1`. This is the documented-safe configuration and preserves the consistency guarantee the
      copy was providing.
    - **Do not adopt `immutable=1` or `nolock=1` against the live file.** Documented corruption risk;
      record this as the negative result of the search.
    - **Retitle in the meantime.** The intake queue's own alternative — "needs a `--no-copy` path or a
      retitle" — is half a fix and the half nobody took. A task named "Metabolism regen daily" that has
      not regenerated in seven days is PREMISE-140's naming defect and can be repaired without touching
      the database question at all.

  STEELMAN:
    Item: PRESUMPTION-952
    Strongest counterargument: The copy is not an unexamined habit; it is the only mechanism that provides
      the guarantee the extractors need, and the two runs that named it were right not to relitigate it
      under time pressure. A read-only consumer of a live OLTP database is reading a moving target:
      without a snapshot it can observe a torn read across a checkpoint, and SQLite's own documentation
      says so twice, for two different parameters, in the section I read. The disk-space error is
      therefore not a symptom of a bad design choice — it is the design choice working correctly and
      telling the operator that the environment can no longer support the guarantee. "Change the
      environment" is the *correct* conclusion from a correct premise, and the alternative the critics
      propose (`immutable=1`) is the one configuration SQLite explicitly warns produces SQLITE_CORRUPT.
      Reaching for it to save disk space would be trading a loud failure for a silent one, which
      PREMISE-128 already names as the worse outcome.
    What would need to be true for C2A2 to be safe: (a) whichever path is chosen, the consistency
      guarantee must be explicit — either the mount supports locking (so `mode=ro` gives it), or a snapshot
      provides it, or the copy provides it; there is no fourth option in which the guarantee is simply
      assumed; (b) the guarantee must be ASSERTED at startup per PREMISE-098, not inferred from the
      absence of an error; (c) the downstream consumer of `metabolism_data.json` must alarm on AGE
      (PREMISE-086), so that whatever happens at the database layer, seven-day-cold data cannot be read as
      current. (c) is independent of the database question, is the highest-value fix here, and is
      currently absent.
    How to test: 14b's test, with one addition. Attempt one read-only open with `mode=ro` from the sandbox
      against the live database and run `PRAGMA quick_check` plus one small SELECT. Record whether the
      open succeeds, whether locking is functional (attempt a second concurrent connection), and the
      wall-clock cost. Then separately confirm whether the host filesystem supports snapshots. Three
      commands, one afternoon, and they settle the item and its steelman together.

  Search scope: comprehensive on the mechanism question (SQLite URI parameters, read-only open semantics,
    `immutable=1`/`nolock=1` warnings, WAL and read-only-media handling, snapshot-based reads);
    FAILED on the requirements-engineering limb — I could not find citable literature on "question the
    requirement before the platform" beyond what PREMISE-146 already holds, and I record that as a null
    rather than filling it. `sqlite.org/c3ref/open.html` was BLOCKED on first attempt (not in the fetch
    provenance set) and was reached indirectly via `sqlite.org/uri.html`, which carried the needed text.

  Recommendation: PARTIALLY-CHALLENGED
