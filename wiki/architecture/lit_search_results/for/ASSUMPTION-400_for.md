SEARCH-FOR-ASSUMPTION-400:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-400
  Original statement: "Recovering a 4.35 GB SQLite file with a live writer attached risks compounding corruption; stop writer -> checkpoint/backup -> .recover -> swap."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-400
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 OpenStory DB recovery plan
      15a: Searched for supporting literature (genuine web search 2026-07-01)
    Current status: SUPPORTED

  Sources:
    1. sqlite.org "How To Corrupt An SQLite Database File" and WAL docs — in WAL mode the one operation that can cause corruption is a checkpoint; leftover -wal/-shm files paired with a swapped main file confuse SQLite. The safe restore sequence is: stop every process holding the DB open, then remove/replace wal+shm — exactly the "stop writer -> ... -> swap" shape.
    2. SQLite backup API / .backup docs (Coddy) — the online backup API produces a consistent copy even while other connections write; making a checkpoint/backup before .recover is the recommended pre-repair step.
    3. runebook SQLite WAL recovery guide — .recover is the correct salvage path for a corrupt DB; recovering into a fresh file and swapping (rather than repairing in place under load) is the recommended pattern.

  Strength of support: Strong

  Summary: The stop-writer -> checkpoint/backup -> .recover -> swap sequence is essentially textbook SQLite recovery practice. Corruption risk concentrates at checkpoint and around stale wal/shm files, so quiescing writers before backup and recovering into a fresh file to swap is exactly what the SQLite project recommends. Strong, primary-source support.

  Caveats: "Live writer risks COMPOUNDING corruption" is slightly stronger than the docs' claim (the backup API can copy consistently even with live writers) — but the conservative stop-writer stance is still endorsed for recovery of an already-corrupt file. Also note the 2026-03 WAL-reset corruption bug (fixed 3.51.3): corruption can originate independent of the writer, so version should be checked too.

  Recommendation: SUPPORTED (Strong — the recovery sequence is primary-source best practice)
