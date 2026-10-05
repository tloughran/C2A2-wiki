SEARCH-AGAINST-PRESUMPTION-1034:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1034
  Original statement: A recorded check verdict and an executed check are distinguishable in principle but are routinely conflated in status reporting; a no-op or skipped check reported in the same field as a pass corrupts every downstream "last known good" attribution.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1034
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (queue item p1034; related ASSUMPTION-1509, ASSUMPTION-1510, OPEN-237, OPEN-240)
      15b: Searched for challenging literature; found boundary-condition and robustness evidence but no direct refutation; strength: Weak
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Search scope: PRELIMINARY — broader search recommended. Web search returned mostly index pages; three sources were fetched and read. Delta-debugging primary literature (Zeller & Hildebrandt) was NOT verified from a fetched source and is not cited as evidence.

  Sources:
    1. Git project. "git-bisect Documentation." https://git-scm.com/docs/git-bisect (fetched 2026-10-05). — Bisect has a first-class `skip` verdict distinct from good/bad, so regression attribution tolerates untestable/no-op points by design. Caveat quoted: if a skipped commit is adjacent to the culprit, git "will be unable to tell exactly which of those commits was the first bad one." Result degrades to a range rather than being corrupted. Challenges the "corrupts EVERY downstream attribution" universality; also shows the failure mode requires the skip to be a distinct verdict, which partly supports the presumption's remedy.
    2. VirtusLab. "Bazel book, 1.2.1 Test Caching." https://bazel.virtuslab.com/book/1~2~1/ (fetched 2026-10-05; third-party secondary source, not official Bazel docs). — Describes Bazel replaying a prior result without re-executing, shown as "(cached) PASSED". For hermetic, input-determined tests, a non-executed check reported as a pass is the intended default and is sound. The text states caching is only reliable when results depend on declared inputs; non-hermetic tests risk "false positives". Supports a boundary condition: conflation is harmless for idempotent/hermetic checks, harmful only for non-hermetic ones. Note the label still distinguishes cached from executed, so the display convention partly cuts the other way.
    3. Google/LLVM-style flaky/skipped-test discussions surfaced by search (e.g. lldb-dev "proposal for reworked flaky test category," https://lists.llvm.org/pipermail/lldb-dev/2015-October/008613.html) were returned by search but NOT fetched or read; listed only as leads, not evidence.

  Strength of challenge: Weak

  Summary: No source found that argues recording a skip/no-op as a pass is correct in general. The challenge is narrower. (a) For hermetic, idempotent checks, reusing a prior verdict without executing is standard and correct (Bazel test caching), so "no-op reported as pass" is not inherently corruption. (b) Mature attribution tooling (git bisect) treats "unknown" as an explicit third verdict and degrades gracefully, bounding the damage to a candidate range rather than an erroneous attribution; this implies the claim's "every downstream attribution" is overstated where a tri-state exists. (c) Neither source contradicts the core claim that conflating an unexecuted verdict with an executed pass is hazardous for non-hermetic checks; Bazel's own docs warn of false positives there.

  Specific risks: If C2A2's checks are non-hermetic (depend on repo state, time, or external services), a no-op recorded as pass becomes a false "last known good," and estate-wide dating of when a defect was introduced would be wrong. Conversely, if the presumption is over-applied to idempotent checks, the system may add costly re-execution or a tri-state schema where plain cached-pass would have sufficed.

  Mitigations available: Add an explicit verdict-provenance field (executed | cached | skipped | no-op) rather than overloading pass; treat skipped/no-op as "unknown" for attribution, as git bisect does; keep reuse of pass only for checks whose result is a pure function of declared inputs, with the input hash recorded; widen candidate ranges when adjacent points are unknown.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1034
  Strongest counterargument: For idempotent checks, a recorded verdict IS the check's value: if inputs are unchanged, re-running yields the same result, so replaying the verdict loses no information and a separate "not executed" state is pure overhead. Systems like Bazel are built on this and report such results as passes at scale. Moreover, attribution from a green baseline is robust to occasional no-ops because bisection-style methods only need a monotone good-to-bad transition; an unknown point widens the candidate range (git bisect skip) but does not produce a wrong answer unless it is adjacent to the culprit. So "corrupts every downstream attribution" overstates a bounded, detectable degradation, and demanding strict executed-vs-recorded separation may add schema complexity with little attribution benefit.
  What would need to be true for C2A2 to be safe: Checks are either hermetic and idempotent (cached-pass is valid) or carry an explicit non-pass state for skip/no-op that attribution logic treats as unknown; the pass-field never mixes hermetic replays with non-hermetic no-ops.
  How to test: Audit C2A2 status records for checks reported pass without execution; classify each as hermetic or not; replay historical dating of a few known defects with no-ops treated as pass vs. as unknown and compare attributed introduction points.

SYSTEMIC-RISK-FLAG: not raised. Only one item examined; no shared vulnerability established. Related ASSUMPTION-1509/1510 and OPEN-237/240 were not read, so a cross-item flag cannot be assessed here.

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1034
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak
  Key source: Git project, "git-bisect Documentation" (https://git-scm.com/docs/git-bisect), with VirtusLab, "Bazel book 1.2.1 Test Caching" (third-party) as boundary-condition source
  Specific risk: If checks are non-hermetic, a no-op logged as pass yields a false last-known-good and wrong estate-wide dating; if over-applied to idempotent checks, adds unneeded tri-state overhead.
  Summary: No direct refutation found; evidence only bounds the claim (hermetic idempotent checks make recorded-pass sound; tri-state attribution degrades to a range, not corruption). Search was preliminary.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1034_against.md

SYSTEMIC-RISK: none flagged
QUEUE SUMMARY: [SEARCHED-15b: 2026-10-05] PRESUMPTION-1034 — PARTIALLY-CHALLENGED (Weak); boundary conditions only (hermetic caching; git bisect skip); preliminary search.
