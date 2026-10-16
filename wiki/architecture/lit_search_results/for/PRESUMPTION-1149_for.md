SEARCH-FOR-PRESUMPTION-1149:
  Date searched: 2026-10-16
  Original item: PRESUMPTION-1149
  Original statement: "What do studies of advisory file locking over network or synced filesystems (NFS lock semantics; fencing tokens, e.g., Kleppmann on distributed locks) imply for a lock-file protocol shared by cloud and local twins of the same job?"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1149
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-15 transcripts.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Search scope: PRELIMINARY — broader search recommended. 2 WebSearch calls, snippets only, no fetches. Kleppmann 2016 seen only through secondary summaries.

  Sources:
    1. Jane Street, n.d. "Lock_file_blocking / Lock_file_blocking.Nfs." OCaml Core docs. — Calls a mkdir lock the simplest scheme with "pretty good mutual exclusion"; notes stale locks and a race where stale cleanup removes a live lock. (seen, snippet)
    2. Muffett, A., n.d. "Exclusive locks in Bourne shell scripts." alecmuffett.com. — mkdir(2) atomic on local filesystems, "pretty good over NFS even". (seen, snippet)
    3. proper-lockfile 4.1.2 README. — O_EXCL broken on NFS, mkdir works; uses an mtime heartbeat for staleness rather than a fixed age. (seen, snippet)
    4. Kleppmann, M., 2016. "How to do distributed locking." martin.kleppmann.com. — Lease/timeout locks cannot ensure mutual exclusion after a pause; fencing tokens checked by the resource are the fix. (UNVERIFIED firsthand; secondary descriptions seen)
    5. etcd contrib/lock README. — A lease-based lock alone "cannot provide mutual exclusion"; recommends fencing or version validation. (seen, snippet)

  Strength of support: Weak

  Summary: Practitioner sources back mkdir as the best simple atomic lock primitive, locally and on NFS. That supports the primitive choice. They do not support "safe" serialization: a 6-hour stale break is a lease, and leases without fencing can admit two holders. No source covers consumer sync services (iCloud, Dropbox), which propagate directory creation late and perform no atomic remote mkdir. If the cloud twin cannot see the folder, there is no shared lock.

  Caveats: Support covers mkdir atomicity on one filesystem or a true network filesystem only, not eventually consistent sync folders. Sources are practitioner docs, not peer-reviewed studies.

  Recommendation: PARTIALLY-SUPPORTED

NOVELTY-FLAG:
  Item: PRESUMPTION-1149
  Searched: 2 web searches on mkdir/NFS locking and lease/fencing locks.
  Finding: No literature on a lock file spanning a cloud agent and a local twin over a consumer sync folder.
  Implication: An untested configuration, not a known-safe pattern. Not an original contribution to knowledge.
  Recommended status: NOVEL (configuration-level only)
