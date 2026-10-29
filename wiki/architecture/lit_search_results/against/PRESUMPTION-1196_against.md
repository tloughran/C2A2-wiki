# PRESUMPTION-1196 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Scheduled run 2026-10-29 (run id cowork-sched-2026-10-29-ddd22cd5; lock held by parent). Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": this item is a concern. Following the template convention (PRESUMPTION-1190/1194), I search against the presumption as 14b states it: that once both copies of a task fire, the cloud and local copies are equivalent, so "the cloud trigger fires" is enough to disable the local entry. Evidence that liveness checks miss functional or capability divergence counts as a challenge to the presumption (and supports 14b's concern). I also looked for the other side: liveness/smoke checks accepted as a cutover gate, and parallel runs being costly or skipped. I did not verify the in-house facts (missing session_info on the cloud copy, NO-OP since 10-24, missing Routines connector on the local copy).

```
SEARCH-AGAINST-PRESUMPTION-1196:
  Date searched: 2026-10-29
  Original item: PRESUMPTION-1196
  Original statement: "[inferred] The double-registration fix ('confirm the cloud trigger
    fires before disabling the local entry') presumes the cloud and local copies of a task
    are equivalent once both fire. They are not: the cloud 14a/14b copy fires nightly but
    lacks session_info and has NO-OP'd since 10-24, while the local scheduler-health copy
    lacks the Routines connector that the cloud side has. 'Fires' is the only parity test
    named; tool parity is not. Following the rule as written would disable the only 14a/14b
    path that reads transcripts."
  Claim tested: Migration cutover verification beyond liveness: capability/feature-parity
    checks, shadow-run comparison of outputs (dark launching, parallel run). Does 'trigger
    fired' suffice as a cutover criterion?

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1196
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-28 local pass (final assistant message per session via
        session_info; no interactive session today).
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Practitioner posts on liveness vs health (dev.to: "Liveness Without Health Is
       Theater"; "Is It Alive Is the Wrong Question, Ask Is It Working"; "Silent Failures:
       The Bug That Won't Page You"). [snippet only]
       — Direct challenge. A heartbeat that fires on every invocation regardless of outcome
       stays green while the job short-circuits or writes to the wrong place. Liveness
       proves a scheduled job ran; it does not prove it did its work. This is the
       "fires nightly but NO-OPs" case.
    2. Migration-validation and parallel-run guides (gravitee.io "API Migration Validation"
       and "Parallel Run Migrations"; origami.sa legacy-modernization cutover;
       techinterview.org "Shadow Mode Testing"; rednafi.com "Tap compare testing").
       [snippet only]
       — Direct challenge. Recommended cutover practice compares outputs, not just
       availability: parity checks cover behaviour clients depend on (codes, timeouts,
       error semantics), and for batch jobs "run the batch on both environments with
       identical input and compare outputs — every number, every record". Shadow/tap-compare
       runs old and new side by side and diffs results before cutover.
    3. Zhang et al. (?), 2025. T2C, OSDI '25 preprint (web.eecs.umich.edu, Ryan Huang's
       group). [snippet only; authors not shown]
       — Mechanism. Production "silent failures" produce wrong results without crashing;
       the paper derives semantic checkers from existing tests to catch them. Supports the
       view that liveness and correctness need separate checks.
    4. arXiv 2608.02786, "Evaluation Blindness: How Silent Measurement Failures Corrupt AI
       Systems from Training to Deployment"; arXiv 2607.17525, "FailureAtlas: A Taxonomy of
       Failure Modes in Multi-Provider LLM Serving Infrastructure." [snippet only; preprints]
       — Adjacent-domain challenge. Availability, latency and error-rate monitoring measure
       whether a response exists, not its quality; LLM pipelines need quality/semantic
       monitoring. Relevant because the C2A2 copies are LLM agents whose output depends on
       which tools/connectors are present.

  Other side (reported honestly):
    a. Cutover runbooks do use liveness-type gates (synthetic checks, capacity
       verification, "no outstanding critical alerts") as pre-cutover gates (gravitee.io
       "Migration basics"). [snippet only] But these appear alongside parity/reconciliation,
       not as the sole criterion. I found no source recommending "it fires" as sufficient.
    b. Parallel runs have real cost: teams mirror only a slice of traffic (e.g. 10%) to
       limit load, and run in parallel for about two weeks (dev.to ACH shadow-traffic
       migration; track360.io "parallel migration vs hard cutover"). [snippet only] Hard
       cutovers without a parallel run are a recognised option. This bears on cost, not on
       whether firing implies equivalence.
    c. Separation-of-concerns caution: putting dependency/capability checks inside a
       liveness probe is called an antipattern (restart cascades). [snippet only] This
       argues for a separate parity check, not for dropping one.

  Strength of challenge: Strong (on the logic), sources Moderate. Every source found treats
    liveness as necessary but not sufficient, and recommends output or behaviour comparison
    before decommissioning the old path. No source defends "trigger fired" as a sufficient
    cutover criterion. Sources are practitioner/vendor snippets plus preprints; no
    peer-reviewed migration-methodology text was read in full.

  Summary: Migration and observability practice consistently separates "it ran" from "it
    did the work". Liveness checks stay green through short-circuits and no-ops, which is
    the failure 14b describes for the cloud copy. Accepted cutover practice adds parity or
    reconciliation (same input, compare outputs), shadow runs, and rollback rehearsal before
    the old path is switched off. Parallel runs are costly and sometimes skipped, but the
    literature presents that as a risk accepted, not as evidence that liveness implies
    equivalence.

  Specific risks: Disabling the local entry on a "fires" check removes the only copy that
    reads transcripts, while the remaining copy keeps reporting success. The loss is silent:
    scheduler health shows nightly firings, and the presumption layer degrades to NO-OP
    output with no alert. Rollback depends on someone noticing absent content.

  Mitigations available: Add a capability check (the required tools/connectors are present
    in each copy) and an output check (the cloud run produces a non-empty, comparable
    result for the same day) before disabling the local entry. Run both for a short window
    and diff outputs (shadow/parallel run, scoped to the 14a/14b task to keep cost down).
    Treat NO-OP runs as failures, not successes. Keep the local entry disabled-but-
    restorable and rehearse re-enabling it.

  Recommendation: CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1196
  Strongest counterargument: Every field that migrates live workloads learned that "the new
    one is up" is the cheapest and least informative check. A scheduled agent can fire on
    time every night and do nothing, because what it does depends on which tools it has,
    and firing says nothing about tools. Cutover practice therefore gates on behaviour —
    same input, compare outputs — and keeps the old path until the new one has been shown
    to produce the same work. A rule whose only named test is "fires" will, when two copies
    differ in capability, retire whichever copy is actually doing the job if that happens
    to be the one scheduled for removal.
  What would need to be true for C2A2 to be safe: both copies have the same tool and
    connector set (verified, not assumed), or the rule is amended to require an output
    comparison and a non-NO-OP result before the local entry is disabled.
  How to test: For one night, run both copies of the 14a/14b task on the same date and
    diff their outputs; list the tools each run actually invoked. Any NO-OP or missing-tool
    result on the cloud side fails the cutover.
```

Source quality: all snippets; sources 1, 2 and the "other side" items are practitioner/vendor material; sources 3-4 are preprints, titles from snippets only. Systemic note: this is a clear instance of the candidate 'a named check treated as a check performed' (the rule names "fires" and readers will take it as parity verified), and it extends 'artefact-as-proof' (a firing record taken as proof the work happened); see PRESUMPTION-1194_against.md. Recommend 14b consider promoting these to a SYSTEMIC-RISK-FLAG: liveness/artefact signals substituting for outcome checks.
