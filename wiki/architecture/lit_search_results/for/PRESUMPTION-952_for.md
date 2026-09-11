SEARCH-FOR-PRESUMPTION-952:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-952
  Original statement: "[inferred] That when a script cannot run in an environment, the environment is
    what must change — that the byte-copy the extractors perform is a fixed property of the task rather
    than a choice in the code."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-952
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an absent alternative named identically by two independent runs; high
        confidence, since both reports quote the copying mechanism and neither questions it.
      15a: Searched for supporting literature; found the code-layer alternative documented in SQLite's
        own primary reference, and found one genuine condition under which the copy is nonetheless
        justified.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-092 (ACTIVE) — the safe-recovery sequence for a large SQLite database: stop writers, take
      a raw file-level copy first, confirm version, checkpoint/backup via the online backup API. Bears
      on *recovery*, not on read-only consumption, but establishes that the estate already holds a
      considered position on SQLite file handling.
    - PREMISE-098 (ACTIVE) — scripts correct interactively on the Mac must not be presumed to behave
      identically when invoked headless in the sandbox; each scheduled script asserts its context
      invariants and fails loud. This is the general form of the item's environment question.
    - PREMISE-107 (ACTIVE) — "A remedy attached to an observation without being validated against the
      actual mechanism costs effort AND leaves the fault in place; where two candidate mechanisms
      present the same symptom, the discriminating test is the operative construct and skipping it is
      the defining error of fault isolation." This bears directly: "approve Desktop Commander" and
      "move to launchd" are remedies attached to a disk-space symptom without a mechanism test.
    - ASSUMPTION-1313 as named in the entry (arithmetic, NOT-QUEUED).
    Recording the hits per OPEN-192; searched anyway.

  LIMB SPLIT:
    Limb A (THE COPY IS NECESSARY): a read-only consumer of a live SQLite database genuinely must copy
      it to obtain a consistent read.
    Limb B (THE QUESTION BELONGS AT THE ENVIRONMENT LAYER): given the constraint, the right move is to
      change the host/permissions rather than to re-examine the code.

  Supporting evidence found: Partial (Limb A only, and conditionally)

  Sources:
    1. SQLite documentation, "Write-Ahead Logging," §5 "Read-Only Databases" (sqlite.org/wal.html).
       — **VERIFIED** (retrieved and read the section text directly) — "Older versions of SQLite could
       not read a WAL-mode database that was read-only... This constraint was relaxed beginning with
       SQLite version 3.22.0 (2018-01-22). On newer versions of SQLite, a WAL-mode database on read-only
       media, or a WAL-mode database that lacks write permission, can still be read as long as one or
       more of the following conditions are met: The -shm and -wal files already exist and are readable.
       There is write permission on the directory containing the database so that the -shm and -wal
       files can be created. The database connection is opened using the immutable query parameter."
       This is decisive against Limb B: the code-layer alternative is documented, supported since 2018,
       and requires no environment change at all.
    2. SQLite documentation on the `immutable` URI parameter, and the SQLite user forum thread "Opening
       DB from readonly filesystem (btrfs snapshot)" (sqlite.org/forum/info/42bcda311d3654b3). —
       SECONDARY — "SQLite always opens immutable database files read-only and it skips all file locking
       and change detection on immutable database files." This is the *warning* that supports Limb A:
       `immutable=1` asserts the file cannot change. Pointing it at a database that is being written
       concurrently is not a safe substitute for a snapshot — it is undefined behaviour dressed as a
       flag. So the extractors' copy is not simply superstition; it buys snapshot isolation that
       `immutable=1` does not.
    3. SQLite documentation, "Write-Ahead Logging," §2.2 (shared-memory requirement), as summarised in
       practitioner material (Coddy "WAL & Concurrency"). — SECONDARY — WAL relies on a shared-memory
       (mmap) region between processes; NFS, SMB and similar network filesystems do not support that
       reliably. **This is the strongest FOR-direction finding on the whole item.** If the 6 GB database
       lives on a mounted/synced path rather than local disk — which is what "the sandbox limit" implies
       — then WAL read-only access over the mount may genuinely fail, and a local copy is not a design
       laziness but the documented workaround.
    4. rqlite "Directly accessing SQLite" guidance (rqlite.io/docs/guides/direct-access). — SECONDARY —
       Production guidance for exactly this pattern: reading a live SQLite file that another process
       owns, with the read-only / snapshot options laid out. Supports Limb A's *framing* (consistency is
       a real requirement) while refuting Limb B (there is a documented code-layer decision to make).
    5. better-sqlite3 issue #640, "Support sqlite3's immutable parameter for reading from RO
       filesystems" (github.com/WiseLibs/better-sqlite3). — SECONDARY — Confirms that the parameter is
       not uniformly exposed by wrappers, which is a plausible proximate reason the estate's extractors
       copy: the binding may not surface the option. That is a code-layer fact, not an environment one.

  Strength of support: Weak-to-Moderate (Limb A, conditional on the mount type), None (Limb B)

  Summary: The presumption splits cleanly and the FOR direction lands on the narrower half. Limb A has a
    real defence I did not expect to find: WAL's shared-memory requirement is documented as unreliable
    over network and SMB-style mounts, so if the live database is on a mounted path the copy may be the
    only correct read, and `immutable=1` is explicitly *not* a drop-in replacement because it disables
    locking and change detection and therefore assumes a file that is not being written. The extractors'
    copy buys snapshot isolation, which is a genuine requirement, and PREMISE-092 shows the estate
    already treats file-level copies as the safe primitive. Limb B has no support: SQLite has shipped
    read-only WAL access since 3.22.0 under three named conditions, the third of which needs nothing
    from the host, and the cheaper alternatives 14b lists (WAL read with pre-existing -shm/-wal, a
    writable containing directory, `immutable=1` over a filesystem snapshot) are all code-layer choices.
    The correct reading is therefore that the two runs were right that a constraint exists and wrong
    about where the decision sits — and PREMISE-107 already names that error class: a remedy attached to
    a symptom without a mechanism test.

  Caveats: Everything here is engineering-practice documentation rather than research literature, so
    there are no effect sizes and nothing to rate for study quality; the SQLite documentation is
    authoritative for its own behaviour and nothing more. Critically, **which limb wins depends on a
    fact I do not have**: whether the 6 GB database is on local disk or a mounted/synced path, and
    whether it is in WAL or rollback-journal mode. On local disk in WAL mode with a writable containing
    directory, no copy is needed and Limb A collapses. On an SMB/NFS-style mount, Limb A holds and the
    copy is correct. The estate can determine this in one command.

  Search scope: comprehensive for the SQLite question, not attempted for the general principle —
    searched SQLite read-only modes, `mode=ro` vs `immutable=1`, WAL shared-memory and network-mount
    limitations, filesystem-snapshot read patterns, and wrapper-level parameter support. I did **not**
    find a literature for 14b's broader framing ("an environment constraint should first be questioned
    at the code layer"); that framing is a design maxim, not a researched claim, and it is already
    covered inside the estate by PREMISE-107.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on Limb A, and only conditionally — the
    copy is defensible if and only if the database is on a mount where WAL shared memory is unavailable.
    Limb B is NO-SUPPORT-FOUND. The literature cannot settle this item and does not need to: 14b's
    in-house test is the whole answer and takes one command. Run, from the sandbox, against the live
    file: `sqlite3 'file:/path/to/db?mode=ro' 'pragma journal_mode; select count(*) from sqlite_master;'`
    and, if that fails, the same with `?immutable=1`. Either it reads or it does not, and the answer is
    today's. If it reads, `metabolism_data.json` stops being seven days cold this afternoon and the
    `--no-copy` path in the intake queue is a one-line change rather than a host-permissions request.
