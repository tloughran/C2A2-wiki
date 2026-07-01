SEARCH-AGAINST-ASSUMPTION-400:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-400
  Original statement: "Recovering a 4.35 GB SQLite file with a live writer attached risks compounding corruption; stop writer -> checkpoint/backup -> .recover -> swap."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-400
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 OpenStory DB recovery plan
      15b: Searched for challenging literature (genuine web search 2026-07-01)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (boundary conditions)

  Sources:
    1. SQLite online backup API docs — the backup/.backup API produces a CONSISTENT copy even while other connections are writing; so "a live writer risks compounding corruption" overstates the risk for the backup step specifically (the API is designed for exactly this).
    2. sqlite.org WAL-reset bug notice (2026-03) — a corruption bug existed in 3.7.0 through 3.51.2 (fixed 3.51.3). If the corruption originated from this bug, the causal story ("live writer compounds it") is wrong; the fix is upgrading SQLite, not just quiescing writers.
    3. General recovery caution — a naive "checkpoint" on an already-corrupt DB can itself propagate bad pages (checkpoint is the one WAL operation that can corrupt); so "checkpoint" before backup may be riskier than a straight file-level copy of the corrupt DB first.

  Strength of challenge: Weak

  Summary: The recovery SEQUENCE is sound, but two boundary conditions qualify it. First, the backup API can copy consistently even with a live writer, so the writer is not the sharp danger the phrasing implies. Second, if the corruption came from the 2026-03 WAL-reset bug, the root cause is the SQLite version, and the recovery should include an upgrade — otherwise recovery may reproduce the corruption. Also, "checkpoint" on a corrupt DB should be handled carefully since checkpoint is itself the corruption-prone WAL op.

  Specific risks: Following the sequence without checking SQLite version could recover into a still-buggy binary; checkpointing a corrupt DB before a raw-file backup could propagate damage.

  Mitigations available: Take a raw file-level copy of the corrupt DB (belt) BEFORE any checkpoint; verify SQLite >= 3.51.3; then .recover into a fresh file and swap, removing stale wal/shm.

  STEELMAN:
    Item: ASSUMPTION-400
    Strongest counterargument: For an already-corrupt 4.35 GB file, conservatism is cheap and correct — stopping writers removes a whole class of concurrent-mutation confounds during salvage, and the exact ordering matters less than the principle "quiesce, copy, recover into fresh, swap." The assumption's instinct is right even if one clause overstates the writer risk.
    What would need to be true for C2A2 to be safe: A raw pre-copy is taken before checkpoint, and the SQLite version is confirmed patched.
    How to test: Verify recovered DB with PRAGMA integrity_check on the fresh file before swap.

  Recommendation: PARTIALLY-CHALLENGED (Weak — sequence is sound; refine: raw-copy-first, version-check, careful checkpoint)
