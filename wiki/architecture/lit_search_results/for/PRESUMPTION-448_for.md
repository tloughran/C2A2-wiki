SEARCH-FOR-PRESUMPTION-448:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-448
  Original statement: "[inferred] Racing concurrent writers is an acceptable coordination mechanism for repo operations."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-448
    Item type: PRESUMPTION (unstated — surfaced by inference; severity HIGH)
    Transform at each step:
      14b: Inferred from the session's handling of index.lock/HEAD.lock collisions that first-writer-wins racing was being treated as the de facto coordination mechanism
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Kung, H.T. & Robinson, J.T., 1981. "On Optimistic Methods for Concurrency Control." ACM TODS 6(2). — The canonical legitimation of "racing" as a concurrency strategy: transactions proceed without locks and validate at commit; when conflicts are rare, this outperforms pessimistic locking. Direct theoretical grounding for letting writers race IF conflicts are reliably detected and losers safely retried.
    2. Optimistic vs. pessimistic concurrency practice literature (Microsoft Learn "Optimistic Concurrency"; Databricks "Concurrency Control"; Oracle MAA blog series; siddontang, Medium, real-world TiDB customer scenarios). — Consistent industry consensus: optimistic (racing) concurrency is acceptable and preferred under low contention; under frequent contention, retry storms make it costly and pessimistic coordination is indicated.
    3. Wang, T. & Kimura, H., 2016. "Mostly-Optimistic Concurrency Control for Highly Contended Dynamic Workloads." PVLDB 10(2). — Shows the research frontier treats pure optimism as insufficient under contention and hybridizes it with targeted pessimistic locks; supports racing only as one component of a designed mechanism.
    4. Git lockfile semantics (Microsoft Learn "Git index.lock"; practitioner guides). — Git's atomic lock acquisition gives racing writers detect-and-abort semantics (loser fails cleanly), which is precisely the conflict-detection primitive OCC requires; supports the view that racing on a git repo is a degenerate but real OCC instance.

  Strength of support: Moderate

  Summary: Unlike most of this cohort, this presumption has a substantive theoretical pedigree: optimistic concurrency control is a fifty-year-old, formally analyzed strategy in which writers deliberately race and conflicts are resolved after detection, and git's lockfiles supply the required atomic conflict-detection primitive. Under low contention — plausibly the normal regime for scheduled agents plus one attended session — the literature actively endorses this pattern as more efficient than locking. The support is therefore real but conditional on the two OCC load-bearing requirements: reliable conflict detection (git provides it) and safe backoff/retry by the losing writer (nothing in the described setup provides it). The literature endorses racing-with-validated-retry; it nowhere endorses racing-with-manual-lock-deletion, and the documented incident pattern (deleting index.lock under uncertainty) is exactly the anti-pattern the practitioner literature warns converts a clean abort into corruption risk.

  Caveats: Support collapses when contention stops being rare (retry storms; the observed collisions suggest the low-contention assumption is already marginal), when losers do not retry idempotently, or when humans/agents respond to lock contention by deleting the lock rather than waiting — at that point the mechanism in use is no longer OCC and has no literature support. Git's locks also protect only ref/index updates, not working-tree interleavings, so racing writers with divergent working-tree expectations fall outside even the OCC reading.

  Recommendation: PARTIALLY-SUPPORTED
