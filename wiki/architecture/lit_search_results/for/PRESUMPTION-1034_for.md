SEARCH-FOR-PRESUMPTION-1034:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1034
  Original statement: A recorded check verdict and an executed check are distinguishable in principle but are routinely conflated in status reporting; a no-op or skipped check reported in the same field as a pass corrupts every downstream "last known good" attribution.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1034
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (general property of status-reporting systems; related ASSUMPTION-1509, ASSUMPTION-1510, OPEN-237, OPEN-240)
      15a: Searched for supporting literature; found direct documentation and bug-tracker evidence for the conflation half and the "no data != OK" rule; no source found for the downstream "last known good" corruption half; strength: Moderate
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. GitHub Docs, "About status checks / Status checks" (docs.github.com/en/pull-requests/reference/status-checks), fetched 2026-10-05. — States: "A job that is skipped will report its status as 'Success'. It will not prevent a pull request from merging, even if it is a required check." Direct, authoritative example of a no-op reported in the same field as a pass.
    2. Grafana Labs, "Missing data" alerting best-practices guide (grafana.com/docs/grafana/latest/alerting/best-practices/missing-data/), fetched 2026-10-05. — Missing data will not trigger alerts unless explicitly checked for; describes "Silent Failure" when series stop reporting. Supports the monitoring-practice rule that no data must not be read as healthy. (Vendor documentation, not peer-reviewed.)
    3. Currents.dev, "Test status translation guide" (currents.dev/posts/test-status-translation-guide), fetched 2026-10-05. — Across nine JS test runners "skipped" means opposite things (Playwright: deliberately excluded; Cypress: should have run but did not); a rising skipped count signals silent coverage loss. Shows routine conflation of executed vs not-executed vocabulary. (Vendor blog.)
    4. Jenkins/Hudson issue JENKINS-1251 (issues.jenkins.io/browse/JENKINS-1251), fetched 2026-10-05. — "Skipped tests should not be considered to have passed, they haven't even been run"; skipped TestNG tests were being counted as passed. Historical bug-tracker evidence of the same conflation in CI reporting.
    5. Search-result listings seen but NOT opened (titles only, not relied on): Atlassian Bamboo BAM-15936 "Summary reporting incorrect test status"; Gradle forum thread on Android instrumentation "ignored" tests shown as "passed"; Katalon forum on skipThisTestCase showing PASSED. Indicative of recurrence; unverified.

  Strength of support: Moderate

  Summary: Documentation and issue trackers from GitHub, Grafana, Jenkins and test-reporting vendors confirm the first half of the claim: executed-and-passed and not-executed states are distinct in principle yet are routinely collapsed into one status field (GitHub reports skipped jobs as Success; Jenkins once counted skipped as passed; test-runner vocabularies for "skipped" conflict). Monitoring practice (Grafana) independently codifies the "no data is not OK" rule, which is the same epistemic distinction applied to alerting. The consequence half (corruption of "last known good" attribution) follows logically from these facts but I found no source that studies it directly. Within the item's scope, support is solid for conflation and for the alerting rule, and inferential only for the downstream attribution effect.

  Caveats:
    - No peer-reviewed literature located; sources are vendor docs, bug trackers and blogs. Publication-bias and source-quality limits apply.
    - Nothing found directly on "last known good build" attribution error or regression-attribution (bisect) sensitivity to skipped/no-op checks; that part rests on inference. Bisect documentation was listed in results but not opened or cited.
    - GitHub's skipped-as-success behavior is a deliberate design choice for conditional jobs, not an accident; it supports "conflated in the same field" but not "unintended".
    - Grafana's rule concerns missing data, an analogy to (not identical with) a skipped check that did report.
    - Scope: preliminary search (4 search queries, 4 pages opened); broader search recommended, esp. peer-reviewed work on flaky/skipped tests (e.g. empirical CI studies) and regression-attribution literature.
    - Tradition wikis (wiki/traditions/*) not consulted in this run.

  Recommendation: PARTIALLY-SUPPORTED

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1034
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: GitHub Docs, "Status checks" — "A job that is skipped will report its status as 'Success'. It will not prevent a pull request from merging, even if it is a required check."
  Summary: Conflation of skipped/no-op with pass in a single status field is documented in GitHub, Jenkins and cross-runner test reporting, and Grafana codifies "no data is not OK". The downstream "last known good" corruption claim has no direct source and is inferential.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1034_for.md

NOVELTY-FLAG: not warranted (general property of status-reporting systems is well documented; only the "last known good" sub-claim lacks direct literature, a partial gap rather than novelty).

QUEUE-SUMMARY: PRESUMPTION-1034 [SEARCHED-15a: 2026-10-05] PARTIALLY-SUPPORTED, Moderate; conflation and "no data != OK" confirmed, last-known-good attribution effect unsourced.
