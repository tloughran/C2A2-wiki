SEARCH-FOR-PRESUMPTION-1106:
  Date searched: 2026-10-03
  Original item: PRESUMPTION-1106
  Original statement (presumption under test): An advisory lock file coordinates concurrent writers even when the check-the-lock rule is absent from the instructions those writers follow.
  Context only (candidate remedy, not tested): put the lock check and a staleness rule into the task spec; remove the duplicate schedule.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1106
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-1731 and the lock file.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources (searched; none supports the presumption):
    1. flock(2) man pages (OpenBSD, QNX, OSF/1, DG/UX) and the Griffith IPC guide. https://man.openbsd.org/OpenBSD-5.6/flock.2 ; https://www.ict.griffith.edu.au/teaching/2501ICT/archive/guide/ipc/flock.html [search-result] — Define advisory locks as working only among *cooperating* processes: "Advisory locks allow cooperating processes to perform consistent operations on files, but do not guarantee consistency (i.e., processes may still access files without using advisory locks...)". This is the authoritative definition, and it states the opposite condition.
    2. Kleppmann, M., 2016. "How to do distributed locking" (blog), and follow-on discussions (antirez.com/news/101; surfingcomplexity.blog 2025 "locks, leases, fencing tokens") [search-result; Kleppmann post itself not fetched] — Even leases need enforcement at the resource (fencing tokens) to be safe. Safety comes from the protected resource rejecting stale writers, not from the existence of the lock.
    3. Cron-overlap practice guides (Rackspace docs, BetterStack, uptimia, stackharbor) [search-result] — All describe lock files as effective only when each job wrapper explicitly checks or acquires the lock (e.g. `flock -n`) and handles staleness (timeouts, PID checks).

  Strength of support: None

  Summary: No literature, documentation or practice guide was found that supports advisory locks coordinating writers who do not check them. Every source defines advisory locking as cooperative: a lock that participants are not instructed to honour has no effect. The only mechanism that would make the presumption true is enforcement outside the writers (mandatory locks, fencing at the resource, or a single scheduler that serialises jobs). In those cases the coordination comes from that mechanism, not the advisory file. The supportive search came back empty because established theory predicts the opposite.

  Caveats: (a) Agents that are LLMs might "notice" a lock file during exploration and honour it without being told to. That would be emergent, unreliable cooperation, and no literature was found on it. (b) If the platform runs scheduled tasks one at a time, writers may never actually be concurrent, which would make the outcome safe for reasons unrelated to the lock. This search did not test that.

  Search scope: preliminary search (2 targeted searches plus 1 practice search shared with the scheduling lane, 0 fetches); OS documentation, distributed-systems commentary, ops practice. No academic papers fetched.

  Recommendation: NO-SUPPORT-FOUND
  (Not flagged NOVELTY: the topic is well covered in the literature, and that literature predicts the presumption fails.)
