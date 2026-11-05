SEARCH-AGAINST-PRESUMPTION-1210:
  Date searched: 2026-11-04
  Original item: PRESUMPTION-1210
  Original statement: Duplicate copies of a task are presumed temporally separable: the second copy is called harmless because it 'waits and only checks', which holds only if it can tell when the first copy has finished.
  Claim tested (literature lane): challenges to the claim that wait-and-check is a defect: designs where duplicates are made harmless by idempotence, where skipping is the accepted failure, where a lock record is enough at low stakes, and where heavier mechanisms fail too. The in-house limb is NOT 15a/15b scope and was not run.
  Search scope: PRELIMINARY. Same 4 web searches and 2 fetches as the 15a pass were available in the session; this file draws only on the SRE chapter and the idempotence/lease-failure hits, and was written without reading the 15a file. Independence is procedural, not subagent-separated, and the search results were shared. Not reached: Gray & Cheriton on leases, Kleppmann's text, any LLM-agent source.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1210
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from the claim that a second task copy is harmless because it 'waits and only checks'
      15b: Searched for challenging literature (preliminary; shared searches, 2 fetches)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Partial
  Sources:
    1. Beyer et al., 2016, Site Reliability Engineering, ch. 24 https://sre.google/sre-book/distributed-periodic-scheduling/ [fetched; summary read] - Google states some jobs are idempotent and safe to run again, others must not run twice, others cannot be skipped, and that "there is no single answer"; it favors skipping over double launch. Challenge to the framing: a second copy that only checks and does nothing is the skip-favoring behavior, and a defect exists only for jobs that cannot tolerate a skip or a double write.
    2. Hochstein, 2025, surfingcomplexity.blog https://surfingcomplexity.blog/2025/03/03/locks-leases-fencing-tokens-fizzbee/ [fetched; summary read] - the model shows fencing tokens do not fully prevent overlap when two processes both believe they hold the lock, and Kleppmann is reported to agree. Challenge: the heavier remedy is not a guarantee either, so the presumption's failure mode is not removed by adopting leases or fencing.
    3. dev.to "How we make every scheduled job safe to re-run" https://dev.to/savage_solutions/how-we-make-every-scheduled-job-safe-to-re-run-48o8 ; JobRunr "Why is Idempotence Important in Java Job Scheduling?" https://www.jobrunr.io/en/blog/idempotence-in-java-job-scheduling [title only; practitioner] - idempotent job design makes separability unnecessary: if each write is keyed by job plus scheduled time, overlap is harmless and no completion inference is needed.
  Strength of challenge: Weak
  Summary: Nothing found says wait-and-check is correct as a guarantee. The challenge is that the presumption need not hold for the design to be safe: if writes are idempotent or keyed by launch, or if skipping is acceptable, the second copy's harmlessness does not depend on telling when the first has finished. Whether C2A2's registers (appended with backups, no keys) are idempotent is an in-house question the literature cannot answer.
  Specific risks: Adding leases or fencing to a file-based lock log is heavy for a one-machine research wiki and, per source 2, still not a guarantee. Appends to shared registers by two overlapping copies can interleave or duplicate entries, which is the case idempotent keys would address.
  Mitigations available: Key each register entry by item plus date so repeat appends are detectable; keep wait-and-check but make the check read a record with holder identity and time.

STEELMAN:
  Item: PRESUMPTION-1210
  Strongest counterargument: Harmlessness should come from the work, not from timing. If every write is idempotent and keyed by scheduled launch, two copies can overlap, interleave or repeat and the result is the same, so no mechanism needs to tell when the first copy finished. Treating separability as the premise invites the heavier and still-fallible lease machinery.
  What would need to be true for C2A2 to be safe: register appends and queue tags are idempotent by item and date, or the second copy provably exits without writing; lock lines carry holder identity and are appended before any write.
  How to test: for 10-26..11-03, list each duplicate pair's start times against the first copy's RELEASED line; count overlaps and any duplicated or lost register entries.

SYSTEMIC-RISK check: Not flagged as a literature-backed shared vulnerability. Loose resemblance to PRESUMPTION-1208 (a copy's local view taken as the task's state) exists, but both are preliminary and mostly summary-level.

  Recommendation: PARTIALLY-CHALLENGED
