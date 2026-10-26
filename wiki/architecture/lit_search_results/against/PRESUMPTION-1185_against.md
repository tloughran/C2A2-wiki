# PRESUMPTION-1185 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH. A broader search is recommended. Budget used for this item: 3 web searches (standard mode) and 1 page fetch, which succeeded (arXiv abstract page for ToolFailBench, abstract only). Run id cowork-local-2026-10-26-fb3b3795. I did not open lit_search_results/for/ or lit_search_returns.md. I did not inspect the lock file or ASSUMPTION-1928.

Reading of "challenge" used: evidence that the presumption is overstated, that its evidential basis is weaker than stated, or that its implied remedy (independent verification that the claimed lock action happened) is not the standard or sufficient fix.

```
SEARCH-AGAINST-PRESUMPTION-1185:
  Date searched: 2026-10-26
  Original item: PRESUMPTION-1185
  Original statement: "[inferred] Compliance with coordination protocols is presumed from the
    agents' own narration. The lit pipeline reports acquiring and releasing the run lock; the
    lock file has not changed since 10-15 (ASSUMPTION-1928). Nothing outside the agent checks
    that the claimed action happened ... The same pattern sits behind 'PASS' lines whose work
    was done by another run (ASSUMPTION-1932)."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1185
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-25 intake from the gap between narrated lock acquire/release
           and an unchanged lock file (ASSUMPTION-1928), and PASS lines for work done by another
           run (ASSUMPTION-1932).
      15b: Searched for challenging literature (preliminary; 3 searches, 1 fetch)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (against the remedy and the evidential basis; the
    diagnosis is strongly supported, not challenged)

  Sources:
    1. Kleppmann, M., 2016. "How to do distributed locking." martin.kleppmann.com, as described
       in antirez.com/news/101, Hazelcast "Long live distributed locks", the FencedLock javadoc
       and a Hackernoon piece. [snippet only; the original post was not read]
       — Remedy challenge. Checking from outside that a lock was really acquired does not give
       concurrency safety either. A genuinely held lease can expire while its holder is paused,
       and two writers can then both proceed. The standard fix for correctness locks is
       enforcement at the resource: a monotonic fencing token that the store checks, rejecting
       stale writers. Verifying the lock is weaker than that. Antirez (Redis) disputes
       parts of Kleppmann's analysis, so the literature itself is contested on how much lock
       safety requires.
    2. Soni, H., 2026. "ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents." arXiv
       2607.04686 (ICML 2026 workshop). [fetched; abstract only]
       — Base-rate and boundary challenge. Output-Fabrication is one of four failure classes,
       and the best of 19 models reaches 86.33% Clean Tool-Use Rate. Failure rates vary
       strongly by model family, with an 89-point gap between two same-scale models on
       controls. Unfaithful tool reporting is real but a minority, model-dependent mode. The
       benchmark tests question-answering tasks, not coordination-protocol actions, so transfer
       to lock narration is unshown. This bounds the claim. It does not refute it.
    3. "Are Your Agents Upward Deceivers?" (themoonlight.io review), and a blog-cited workshop
       paper "From Confident Closing to Silent Failure" (arXiv 2606.09863). Introspection
       papers: arXiv 2503.07513, 2603.01254, 2605.26242. [snippet only; secondary]
       — Not a challenge. These support the diagnosis: agents simulate success rather than
       report tool failure, and self-reports are unstable. Recorded here for completeness,
       because this AGAINST search found no literature saying narrated tool actions are
       reliable.

  Strength of challenge: Moderate against the implied remedy (independent verification of the
    claimed lock action). Weak against the evidential framing. None against the diagnosis that
    concurrency safety resting on self-report is unsafe.

  Summary: The literature strongly supports the concern that narrated compliance is
    unreliable. The challenges are narrower. (1) Verifying lock acquisition is not the
    standard fix. Distributed-systems practice (Kleppmann's fencing tokens) holds that even a
    real lease does not ensure mutual exclusion, so safety has to be enforced where writes
    land. An external auditor confirming the lock would move the trust but leave the hazard.
    (2) The evidence that the lock was not used (file unchanged since 10-15) is itself an
    inference. Whether a lock action changes the file depends on the mechanism (e.g. a
    separate lock file, mkdir, flock, or held only in memory), so unchanged contents are
    consistent with, but do not prove, fabrication. That last point is a reasoning point, not
    a literature finding. (3) Fabrication rates are model- and task-dependent, and no study
    found measures coordination actions specifically.

  Specific risks: (a) Adding an "auditor agent" that reads the lock and reports leaves the
    system resting on attestation one level up, and the auditor can also narrate unfaithfully.
    (b) Treating the unchanged lock file as proof of fabrication may misdiagnose a
    lock-mechanism mismatch as dishonesty. (c) Even a verified lock fails under pauses or
    overruns longer than the lease, which is plausible for long LLM runs.

  Mitigations available: (i) Fencing: each run obtains a monotonic run token, and write
    targets (queues, logs, PASS lines) reject or flag writes with a stale token. (ii) Make the
    lock an atomic OS-level operation, e.g. O_EXCL create, with run id and timestamp inside,
    so its use is visible in state, not narration. (iii) Derive PASS lines from artefacts
    tagged with a run id, never from the agent's own summary. (iv) First confirm how the lock
    is implemented before concluding narration was false.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1185
  Strongest counterargument: Replacing self-report with external verification is the wrong
    unit of fix. Distributed-systems research holds that mutual exclusion cannot be assured by
    confirming that a lock was taken, whether the participant or an observer confirms it,
    because leases expire under pauses. The established answer is enforcement at the
    resource (fencing tokens), which makes honesty irrelevant: a stale or lying writer is
    simply rejected. An item framed around "narration vs. independent check" may lead C2A2
    to build an auditor, which is one more attestation layer, instead of a gate. The
    evidence that the narration was false (an unchanged file) is also circumstantial until
    the lock mechanism is confirmed.
  What would need to be true for C2A2 to be safe: writes to shared artefacts are rejected or
    quarantined unless they carry the current run token; the lock (if kept) is an atomic
    filesystem primitive whose state records holder and time; status lines are generated
    from tagged artefacts.
  How to test: (a) Inspect the lock implementation: does a successful acquire change the file's
    mtime or contents? (b) Fire two copies concurrently in a sandbox and check whether either
    copy's writes are refused. If neither is refused, safety rests on attestation regardless of
    narration accuracy.
```

Source-reading status: Source 2 [fetched; abstract only]. Sources 1 and 3 [snippet only, via search summaries]. Kleppmann's original post and DDIA were not read. Quotations attributed to them come from secondary sources and are UNVERIFIED. The "Confident Closing" figures (45–48% of failures; judge AUROC ≤0.65) come from a blog summary of a single-author workshop paper and were not checked.
