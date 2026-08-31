SEARCH-AGAINST-ASSUMPTION-1234:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1234
  Original statement: "Write to a temp file and rename. **Both halves** of this incident disappear
    under that rule."
  Generalizable limb searched: The completeness claim — that write-temp-then-rename is a sufficient
    and complete remedy for partial/torn-write failure classes, i.e. that no residual failure modes
    survive the rule.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 2 queries run (Pass 1 only; Priority Medium,
    so no Pass 2 by budget rule); no full-text reads. Note: the primary source found (Pillai et al.,
    OSDI 2014) is a strong peer-reviewed match and its findings were characterised in multiple
    independent secondary summaries, which raises confidence despite no full-text read.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1234
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced as an explicit stated remedy claim, with "both halves" flagged as a
        completeness assertion rather than a partial-mitigation assertion.
      15b: Searched for challenging literature (2026-08-31)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Pillai, Chidambaram, Alagappan, Al-Kiswany, Arpaci-Dusseau & Arpaci-Dusseau, 2014.
       "All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent
       Applications." OSDI '14, USENIX. — The central challenge. Studied eleven widely-used systems
       (databases, key-value stores, version control, distributed systems, virtualisation) and found
       60 crash vulnerabilities. Reports that applications are "extremely vulnerable to system calls
       being persisted out of order" (27 vulnerabilities of that class), and that persistence
       properties vary widely between file systems and even between configurations of the same file
       system. Critically for this item: the append-then-rename idiom is explicitly discussed, and
       the common delayed-allocation heuristic of persisting file data before rename is reported to
       fix only a small minority (3) of the vulnerabilities found.
    2. Mohan, Martinez, Ponnapalli, Raju & Chidambaram, 2018. "Finding Crash-Consistency Bugs with
       Bounded Black-Box Crash Testing." (arXiv:1810.02904; the CrashMonkey/B3 work, OSDI '18). —
       Reports discovering broken rename-atomicity bugs in btrfs, including cases where a file
       disappeared entirely or appeared in both source and destination locations after a crash. This
       is a direct counterexample to rename atomicity being a safe primitive in practice as opposed
       to in specification.
    3. POSIX rename() semantics as characterised across the search results (comp.unix.programmer
       thread; delta-rs issue #142; 0xKiire, "Crash Consistency: fsync(), rename(), and
       Durability"). — The consistent point: POSIX requires that a crash mid-rename leaves the file
       under either the old or the new name (atomicity of the *directory entry change*), but this
       says nothing about *durability*. Without fsync on the containing directory, the rename may
       not be persisted at all; snippet-level reports of bugs where directory entries were missing
       after an fsync on the directory, and where a rename was not persisted by fsync. Snippet-level
       only; I did not read the underlying bug reports.
    4. Ganger & Patt / soft-updates lineage, as characterised in the search results. — Traditional
       soft updates does not provide atomic rename: a crash during rename can leave both source and
       destination present. Newer Synchronous Soft Updates is described as fixing this. Establishes
       that rename atomicity is a property of specific implementations, not a universal guarantee.
       Snippet-level; original paper not identified precisely enough to cite by title/venue.

  Strength of challenge: Moderate

  Summary: The literature strongly supports write-temp-then-rename as the *correct idiom* — it is
    the recommended pattern precisely because it is better than in-place mutation — while directly
    contradicting the completeness word "both halves ... disappear." Pillai et al. is the decisive
    finding: the rename idiom does not eliminate crash vulnerabilities, it narrows them, and the
    residue is concentrated in ordering and durability rather than in atomicity. Three residual
    modes survive the rule as stated. First, durability: rename atomicity guarantees you get old-or-
    new, not that you get new; without fsync on the temp file before rename and fsync on the
    containing directory after, a crash can leave the old content or an empty/zero-length file.
    Second, implementation divergence: rename atomicity has been empirically broken in shipped file
    systems (btrfs), so the guarantee is probabilistic across the deployment surface, not absolute.
    Third, cross-filesystem rename: rename() is not atomic and generally fails with EXDEV across
    mount points, degrading to copy-then-delete, which reintroduces exactly the torn-write window
    the rule was meant to close — directly relevant where a temp directory and target directory are
    on different mounts, which is common. The challenge is Moderate rather than Strong because the
    remedy is genuinely the right one and the residue is addressable with two extra fsync calls and
    a same-directory temp file; the claim is over-stated rather than misdirected.

  Specific risks: If the completeness claim is taken at face value, C2A2 will implement the idiom
    without the fsync discipline and without constraining the temp file to the same directory as the
    target, and will then treat the failure class as permanently closed. The residual failures are
    rare and crash-triggered, so they will not appear in testing and will not be attributed to this
    remedy when they do occur — the incident will look like a new and unrelated class. A specific
    concrete risk: if the temp file is created in a system temp directory (/tmp, or a workspace temp
    path) while the target is in the vault, that is a cross-filesystem rename, and the remedy
    silently degrades to non-atomic copy for every write.

  Mitigations available: (a) Create the temp file in the *same directory* as the target, which both
    guarantees same-filesystem rename and makes the directory fsync meaningful; (b) fsync the temp
    file's contents before the rename and fsync the containing directory after it; (c) never assume
    EXDEV cannot happen — detect and fail loudly rather than falling back to copy; (d) restate the
    claim as "closes the torn-write half outright and the durability half conditional on fsync
    ordering" rather than "both halves disappear"; (e) note that on a single-user local vault with
    no crash pressure, the residual modes have low base rate — but that is an argument about
    likelihood, not about completeness.

  STEELMAN:
    Strongest counterargument: The crash-consistency literature is about surviving *power loss and
      kernel panics* in systems where durability is a contractual obligation — databases,
      key-value stores, distributed logs. The incident this remedy addresses is almost certainly a
      *process-level* failure: an agent or script crashed, was interrupted, or errored partway
      through writing a file, leaving a truncated artefact. Against process-level failure, rename is
      genuinely and completely atomic, because the kernel completes the rename regardless of what
      happens to the writing process, and the page cache preserves the content. Every one of the
      residual modes Pillai et al. document requires the machine itself to go down between the write
      and the flush. If the failure class under discussion is "agent died mid-write," then "both
      halves disappear" is simply correct, and importing OSDI crash-consistency findings is a
      category error about which failure model is in play.
    What would need to be true for C2A2 to be safe: The failure class being remedied must be
      process-level interruption rather than machine-level crash; the temp file and target must be
      on the same filesystem (same directory is the reliable way to ensure this); and the value of
      the artefact must be low enough that a power-loss-window data loss is acceptable, or the
      snapshot from ASSUMPTION-1233 must cover that window. If the failure model really is
      process-level only, the challenge substantially does not apply.
    How to test: Two separable tests. (1) Process-level: kill -9 the writing process at randomised
      points during the write and confirm the target is always either fully old or fully new — this
      should pass cleanly and would confirm the steelman. (2) Cross-filesystem: check at runtime
      whether the temp path and target path are on the same device (compare st_dev), and log it;
      if they differ, the atomicity claim is already void in production regardless of crash model.
      Test (2) is cheap, deterministic, and would settle the most likely real-world residue.

  Recommendation: PARTIALLY-CHALLENGED
