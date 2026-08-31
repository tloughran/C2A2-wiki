SEARCH-FOR-ASSUMPTION-1234:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1234
  Original statement: "Write to a temp file and rename. Both halves of this incident disappear under that rule."
  Generalizable limb searched: Does write-temp-then-rename provide *complete* failure atomicity for file
    replacement, such that no residual failure mode of the same class survives the rule? (Per intake instruction,
    the test is the completeness claim, not whether the practice is good.)

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 2 queries run; no full-text reads. Sources are strong in kind
    (POSIX semantics, kernel mailing lists, PostgreSQL commit discussion, an upstream bug tracker) but I read only
    search snippets of each.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1234
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from the 2026-08-30 daily digest as a stated remedy rule offered as fully covering the incident.
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. POSIX rename(2) semantics, as restated across multiple results (0xKiire, "Crash Consistency: fsync(),
       rename(), and Durability"; comp.unix.programmer thread) — Snippets uniformly state that rename is atomic as
       a *namespace* operation: a reader observes either the old complete file or the new complete file, never a
       partial one. This is direct support for the core of the rule and for the exclusion of torn-read exposure.
    2. alexwlchan, 2019. "Atomic, cross-filesystem moves in Python." alexwlchan.net — Snippet states the motivating
       contrast plainly: writing directly to the final filename lets readers observe partial content, whereas
       temp-then-replace does not. Supports the rule's benefit; also documents the EXDEV limit.
    3. npm/write-file-atomic, GitHub Issue #64: "Rename atomicity is not enough." — Title and snippet are directly
       on the completeness question, from the maintainers of a library whose entire purpose is this idiom. Bears
       against completeness.
    4. PostgreSQL commit/message thread (postgresql.org message-id E1adrE0-0001Or-CA@gemulon.postgresql.org) —
       Snippet: rename(2) is not guaranteed durable across crashes, "especially on filesystems like xfs and ext4
       when mounted with data=writeback"; correct replacement requires fsync of old name, rename, fsync of new
       name, and fsync of the containing directory. Bears against completeness of the bare rule as stated.
    5. f2fs kernel patch thread, LKML 2018 ("[PATCH 5/5] f2fs: enforce fsync_mode=strict for renamed directory") —
       Evidence that rename-durability edge cases were live enough to warrant kernel-level mitigation.
    6. anthropics/claude-code GitHub Issue #32533 (Windows: EXDEV cross-device rename fails when projects are on a
       different drive than AppData) and NousResearch/hermes-agent Issue #34252 (atomic_replace() fails with EXDEV
       across a filesystem symlink) — Two independent field reports that the rename idiom fails outright across
       mount points. Snippet-level; I did not read the issue threads.
    7. "Unix Tools and the FITO Category Mistake: Crash Consistency and the Protocol Nature of Persistence."
       arXiv:2603.01384 — Snippet asserts that rename is atomic in namespace semantics but *not* in persistence
       semantics, and that assuming instantaneous atomic state transitions is a category mistake at every layer
       from ext4 journaling through fsync failure semantics to NVMe Flush/FUA. CAUTION: I saw this only as a
       search-result snippet and could not verify the paper's provenance or peer-review status; treat as
       unverified.

  Strength of support: Weak (for the completeness claim as written; Strong for the underlying practice)

  Summary: Searching in the supportive direction, the literature endorses the practice without endorsing the
  completeness claim. Every source agrees that rename gives failure-atomic *visibility*: a concurrent or
  post-crash reader sees the whole old file or the whole new file, never a half-written one, which is genuinely
  the failure mode described in the first half of the incident. What no source supports is "both halves disappear."
  The consistent finding is that rename is atomic in namespace semantics and not in persistence semantics — the
  durable-replacement protocol requires fsync of the temp file before rename and fsync of the parent directory
  after it, or a crash can resurrect the old file despite an apparently completed rename. Independently, rename
  fails with EXDEV across filesystem boundaries, which is not a subtle case: two field bug reports found in this
  search are exactly that failure, one of them in Claude Code itself on Windows. The rule is correct and worth
  adopting; the totality attached to it is not something the literature will carry.

  Caveats: (i) The support that does exist is for the two-step idiom *plus* explicit fsync ordering; the assumption
  as stated names only write-and-rename, and the residual failure modes attach specifically to the omitted steps.
  (ii) EXDEV means the rule can fail loudly rather than silently, which is a different and milder failure than the
  original incident — the completeness claim fails, but not catastrophically. (iii) Filesystem-specific: several
  hazards are conditioned on ext4/xfs mount options or on non-POSIX platforms, so a same-filesystem POSIX
  deployment sees a narrower residual surface than the literature's worst case. (iv) One source (arXiv:2603.01384)
  is unverified.

  Recommendation: PARTIALLY-SUPPORTED
