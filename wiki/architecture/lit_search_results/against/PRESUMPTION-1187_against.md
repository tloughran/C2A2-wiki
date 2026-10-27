# PRESUMPTION-1187 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Run id sched-lit-2026-10-27-6d9c5b33. Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": evidence that the presumption's concern is mis-specified or overstated, or that its implied remedy is wrong. The implied remedy is to give each coordination artefact one canonical location and to have an independent check. I did not dispute the in-house facts: two lock files, the stale one read, and the error propagating to OPEN-275, PRESUMPTION-1185 and MONITOR-697.

```
SEARCH-AGAINST-PRESUMPTION-1187:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1187
  Original statement: "[inferred] A named coordination artefact is presumed to have one canonical
    location, so that checking 'the file' settles a question. Two lit_pipeline.lock files exist
    ... The self-audit layer is subject to the same artefact-as-proof failure it reports in
    other agents."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1187
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 10-25 14a pass reading the stale architecture/ lock and logging the
           result as "Verified".
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial. It challenges the remedy implied by "one canonical
    location" and the expectation that an independent audit fixes the problem. It does not
    challenge the diagnosis.

  Sources:
    1. Lock-file practice: O'Reilly, "Secure Programming Cookbook" ch. 2.9; FreeBSD flock(2) man
       page; cgit commit "use F_SETLK to avoid stale lock files". [snippet only]
       — Mis-specification. In this practice a lock file's existence or location is not treated
       as authoritative, even when only one copy exists. Existence-based lock files go stale when
       the holder dies, and PID-in-file staleness checks add a check-then-remove race and suffer
       from PID reuse. The standard fix makes authority come from a live kernel lock (flock/fcntl)
       held by a running process, not from a file at the right path. So making the path unique
       would not have made the check authoritative. A single stale file would have produced the
       same "Verified".
    2. "Single source of truth" critiques: itnext ("Copying data is not an anti-pattern; copying
       data without a strategy is"); adhdecode "fallacy of the single source of truth"; Segal's
       Law page. [snippet only; informal/secondary]
       — Bounding. These sources say copies are normal and that one source becomes a single point
       of failure. The defect they identify is copies with no designated authority or freshness
       signal, not the copies themselves.
    3. Knight, J.C. & Leveson, N.G., 1986. "An Experimental Evaluation of the Assumption of
       Independence in Multi-Version Programming." IEEE TSE 12(1):96-109. [secondary; abstract and
       summaries only]
       — Bounds the "who audits the auditor" remedy. Twenty-seven independently written programs
       failed together far more often than independence predicts, because their authors made
       similar mistakes on the same hard parts of the problem. Adding a separately specified
       auditor does not by itself remove common-mode error. An auditor that uses the same
       artefact-as-proof heuristic will inherit the failure, which is what the item reports.

  Strength of challenge: Moderate against the implied remedy ("one canonical location" or "add
    an auditor"). None against the diagnosis that checking a file was treated as proof.

  Summary: The literature locates authority in liveness and freshness, not in uniqueness of
    location. Removing the duplicate lock would stop this specific misread, but a lone stale lock
    file would still pass a "the file says X" check. The self-audit finding also matches a
    known pattern: independent checkers with the same heuristics fail together (Knight-Leveson).
    So more audit layers are a weak remedy unless they change the method of verification.

  Specific risks: (a) Deleting the stale copy is treated as the fix, leaving existence-as-proof
    in place. (b) A further audit agent re-reads the same artefacts and certifies the same error.

  Mitigations available: Have the lock record holder and run id plus a heartbeat or expiry, and
    have a check confirm the holder is alive. Record which path was read when a check is logged
    as "Verified". Make audits check by a different method (for example, process state or the
    scheduler log instead of the file).

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1187
  Strongest counterargument: The failure is not that two files exist. It is that any file was
    taken as proof of a live condition. The lock-file literature treats even a single, canonical
    lock file as untrustworthy without a liveness check, and the N-version literature predicts
    that auditors sharing a heuristic fail together. Consolidating to one path is cosmetic, and
    the real fix is a change of evidence type, from artefact to live state.
  What would need to be true for C2A2 to be safe: a lock check reads both holder identity and
    freshness, a "Verified" log line cites the path and the method, and at least one audit uses a
    method that does not rely on artefacts.
  How to test: Plant a single stale lock at the canonical path with no duplicate, run 14a, and see
    whether it still logs "Verified".
```

Source quality: all sources are snippets or secondary. I did not read Knight-Leveson in full. No source addresses LLM-agent pipelines directly.

```
SYSTEMIC-RISK-FLAG (candidate):
  Date: 2026-10-27
  Affected items: PRESUMPTION-1187, PRESUMPTION-1188, PRESUMPTION-1189 (and 1184 from 10-26)
  Common vulnerability: An artefact's presence or absence, or its timestamp, is read from inside
    the same system as proof of live state (lock held, write in flight, task ran). The usual
    remedies (a canonical file, more locks, a self-hosted watcher, another auditor) keep the same
    evidence type and so share its failure mode.
  Literature basis: lock-file staleness and PID-race literature; Kung & Robinson 1981
    (validation must be atomic at commit); Knight & Leveson 1986 (common-mode failure of
    "independent" checkers); absence-alerting practice (expectation source must outlive what it
    monitors).
  Risk level: High
  Recommendation: for 14b reconciliation. Consider the items together, not one at a time.
```
