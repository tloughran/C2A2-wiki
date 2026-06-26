SEARCH-FOR-PRESUMPTION-405:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-405
  Original statement: "That a SIGKILL'd (Killed: 9) backfill left the DB consistent because counts rose and the cleanup trap fired"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-405
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: DB consistency after SIGKILL inferred from rising counts + a cleanup trap
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. SQLite, "Atomic Commit In SQLite" + Powersafe-Overwrite docs. - With default synchronous=FULL and rollback-journal/WAL atomic commit, SQLite is DESIGNED to auto-recover to a consistent state after abrupt process termination, automatically rolling back the incomplete transaction and handling torn pages.
    2. SQLite ACID / durability documentation. - On the next connection, an interrupted write is rolled back; the database is left consistent at a transaction boundary.

  Strength of support: Moderate

  Summary: There is genuine support for the CONCLUSION that the DB is likely consistent - but it comes from SQLite's atomic-commit design (auto-rollback of the interrupted transaction), NOT from the evidence the presumption actually cites. If the store is SQLite at synchronous=FULL, a SIGKILL should leave it consistent at the last committed transaction. The support is for "probably consistent given SQLite semantics," not for "consistent because counts rose and the trap fired," which is invalid reasoning (see 15b).

  Caveats: Support assumes SQLite (or an equivalently atomic store) with durable-commit settings, and consistency at a transaction boundary - NOT that the backfill COMPLETED. Completeness is a separate question from integrity.

  Search scope: SQLite atomic commit/crash recovery. Adequate.

  Recommendation: PARTIALLY-SUPPORTED
