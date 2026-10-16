SEARCH-AGAINST-PRESUMPTION-1149:
  Date searched: 2026-10-16
  Original item: PRESUMPTION-1149
  Original statement: "What do studies of advisory file locking over network or synced filesystems (NFS lock semantics; fencing tokens, e.g., Kleppmann on distributed locks) imply for a lock-file protocol shared by cloud and local twins of the same job?"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1149
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-15 transcripts.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Search scope: PRELIMINARY — broader search recommended. 2 WebSearch calls, snippets only, no fetches. Kleppmann original not seen firsthand. No source covers mkdir locks on iCloud/Dropbox/Drive sync folders specifically.

  Sources:
    1. Kleppmann, M., 2016. "How to do distributed locking." martin.kleppmann.com. — Leases expire while the holder is paused, so two holders can write. Timeouts give liveness, not mutual exclusion; a correctness lock needs fencing tokens checked by the resource. (UNVERIFIED firsthand; seen via surfingcomplexity.blog 2025, system-design.space, hackernoon)
    2. surfingcomplexity.blog, 2025. "Locks, leases, fencing tokens, FizzBee." — Fencing still fails if the lower token reaches the resource first. (seen, snippet)
    3. flufl.lock docs (PyPI); JGit NFS LockFile commits; Mail::Box::Locker::NFS. — On NFS exclusive create is not reliably atomic; locks survive SIGKILL; stale cleanup can delete a live lock. (seen, snippets)

  Strength of challenge: Strong (snippet-level evidence)

  Summary: mkdir is atomic only within one filesystem's view. A synced folder gives two machines two local views reconciled later, so both twins can create the lock before sync propagates. A cloud twin that cannot see the folder is not excluded at all. The 6-hour stale break is a timeout lease, so a slow or paused run can lose its lock while still writing.

  Specific risks: Both twins run at once and make duplicate or conflicting writes (as happened 2026-10-01 and 2026-10-15). Sync may create conflicted copies of the lock directory (inferred, not sourced). Stale break can take a live lock. A killed run blocks runs for up to 6 hours.

  Mitigations available: One twin owns the schedule (the other removed or read-only). Idempotent writes, or a monotonic run ID checked at write time (fencing). One authoritative lock store reachable by both twins. Owner, host and heartbeat in the lock, verified before breaking it.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1149
  Strongest counterargument: A mkdir lock in a synced folder does not exclude a twin on another machine, and does nothing for a twin that cannot see the folder. The lock gives assurance exactly where it cannot provide it. Timeouts give liveness, not safety; without a fencing check at the write target, any pause longer than the lease admits a second writer.
  What would need to be true for C2A2 to be safe: Double execution is harmless (idempotent writes); or both twins provably write only through the same synced folder, with sync delay much shorter than the gap between runs, and no run approaching 6 hours.
  How to test: Start both twins seconds apart and check whether both take the lock. Measure sync delay for a new directory. Kill a run mid-write and check stale-break behaviour. Check past logs for duplicate or conflicted outputs.
  Steelman for the presumption (15b's own): runs are rare and short relative to the window; if the cloud twin never writes the same targets there is nothing to protect; Kleppmann's "efficiency lock" tolerates harmless double runs.
