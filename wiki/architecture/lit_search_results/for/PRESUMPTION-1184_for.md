SEARCH-FOR-PRESUMPTION-1184:
  Date searched: 2026-10-26
  Original item: PRESUMPTION-1184
  Original statement: "[inferred] The earliest same-day output is presumed complete and authoritative. Later firings stand down on finding any prior output, without checking it. 15d: 'The other copy finished first ... so its entry is the official one', yet that copy misrouted MONITOR-685 and the later copy had to correct it. Telemetry wrote PASS for a run that 'only partly produced' the feeds and credited the rest to an unidentified overlapping run. Distinct from PRESUMPTION-1180 (whether later runs defer at all): this concerns what deferring ratifies."

  Reading used for the FOR direction: support means literature confirming that (a) standing down on the mere existence of prior output is a recognised hazard, because existence does not imply completeness or correctness; and (b) established designs either verify completeness before skipping or make "output exists" mean "output is complete" through an atomic commit. 15a does not judge whether the 10-25 runs actually misrouted MONITOR-685.

  Search scope: PRELIMINARY. 3 web searches (standard), 1 fetch attempted. The fetch of the Kubernetes CronJob documentation was refused by the fetch tool (URL not in the provenance set). No content was returned and it was not retried. Searched: Kubernetes CronJob concurrencyPolicy and Airflow duplicate-run handling; _SUCCESS markers, atomic commit and skip-if-exists idempotency; Kleppmann DDIA ch. 11 exactly-once and idempotence. Not reached: DDIA ch. 11 text itself, Airflow documentation (no Airflow results came back), the academic literature on idempotent consumers and transactional outboxes. A broader search is recommended.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1184
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-25 intake from 15d's "the other copy finished first ... so its entry is the official one" (where that copy misrouted MONITOR-685) and from telemetry recording PASS for a partial run. Framed as distinct from PRESUMPTION-1180: the question is what deferring ratifies, not whether runs defer.
      15a: Searched for supporting literature (preliminary; 3 searches, 1 fetch refused, 0 pages read)
    Current status: SEARCHED-15a — PARTIALLY-SUPPORTED

  Supporting evidence found: Partial. Support for (a) and (b) comes from practitioner sources and Hadoop documentation. The canonical anchors named in the claim (DDIA ch. 11, scheduler documentation) were reached only through secondary summaries.

  Sources:
    1. Apache Hadoop documentation, "Manifest Committer Protocol" (r3.3.5 / 3.3.6 / 3.4.1), and Cloudera Runtime docs, "Job summaries in _SUCCESS files." [snippet only]. Task output is staged in a temporary directory and moved into the destination only at job commit. The v2 FileOutputCommitter algorithm is described as unsafe because output becomes visible as individual tasks commit. Relevance: the strongest support for (b). Mature batch frameworks do not let visible output stand for completion unless it was committed atomically. A downstream existence check is safe only because the commit protocol guarantees that existence means complete. C2A2's feeds have no such commit step, so the "partly produced" output looks the same as finished output.
    2. Practitioner idempotency guidance: yomotherboard Q&A "How can a Bash batch resume safely after interruption?", flaviocopes "Make the work idempotent", and an idempotency notes file (pan-wizard learnings, jsDelivr). [snippet only, practitioner]. "On restart, validate the final output rather than trusting that its mere existence means success." Check that the destination "already reflects this exact action (file present with same hash, row present with same key)". Use write-to-temp, validate, then atomic rename. Relevance: direct support for (a), in nearly the item's own terms. Skip-if-exists without validation is named as the anti-pattern.
    3. Kleppmann, M. 2017. Designing Data-Intensive Applications, ch. 11 "Stream Processing," via reader notes (Goodreads highlights; stonecharioteer notes) and a Confluent Current 2025 talk, "Exactly-Once vs. Idempotency: When Misconceptions Create Complexity." [snippet only, secondary]. Exactly-once is framed as making the final effect match a fault-free run, even under retries. Non-idempotent operations can be made idempotent with extra metadata, and end-to-end idempotency must cover the whole flow. The Confluent talk reports that infrastructure-level exactly-once did not remove the need for application-level deduplication. Relevance: theoretical grounding. Correctness is defined by the effect matching a fault-free run, not by which writer arrived first. "First copy is official" does not meet that standard if the first copy was wrong.
    4. Kubernetes CronJob documentation (kubernetes.io, "CronJob"); Red Hat MicroShift API reference (CronJob batch/v1); OneUptime, "How to Configure CronJob concurrencyPolicy for Allow, Forbid, and Replace." [snippet only]. Forbid skips a new run if the previous one has not finished. Replace cancels the running Job in favour of the new one. Allow (the default) permits overlap. The policy only governs Jobs from the same CronJob. Relevance: weak and indirect. The scheduler resolves duplicates by run state (finished or running), not by validating output. None of the three policies checks whether a finished run's output is complete, so scheduler-level dedup does not ratify output. The documentation reached says nothing about output completeness, which leaves that check to the application.

  Strength of support: Moderate

  Summary: The literature found supports the diagnosis that output existence is not evidence of completeness or correctness. Practitioner idempotency guidance says outright to validate the final output and not trust its mere existence. Hadoop's commit protocols exist so that visible output means fully committed, and they flag a non-atomic variant as unsafe. DDIA-style exactly-once semantics define correctness as matching a fault-free outcome, which a "first finisher wins" rule does not guarantee. Scheduler concurrency controls (Kubernetes concurrencyPolicy) handle duplicate runs by run state alone. They do not certify output, so a system relying only on "someone already ran" has nothing that certifies the output. The item's specific claim, that C2A2's later runs ratify an unchecked earlier output, matches the anti-pattern these sources warn against.

  Caveats:
    - No primary source was read. The Kubernetes fetch was refused, and DDIA ch. 11 was seen only through reader notes. The DDIA attribution is secondhand.
    - The established remedy is often an atomic commit plus an existence check, not a content-validating completeness check. Literature supports "existence alone is unsafe without atomic commit." It does not necessarily require later runs to re-validate content. Either remedy fits the sources.
    - First-writer-wins is a legitimate pattern where the first write is atomic and complete (e.g. conditional put-if-absent with a full payload). The hazard the sources identify is specifically partial or unvalidated output, which matches the item's evidence ("only partly produced") but not all first-writer-wins designs.
    - Most direct support is practitioner-grade (Q&A, blogs), not peer-reviewed.
    - The Airflow part of the claim (max_active_runs, task-level idempotence) returned no results.

  Recommendation: PARTIALLY-SUPPORTED

  (No NOVELTY-FLAG: validate-before-skip and atomic-commit semantics are established. The item applies them to C2A2's duplicate firings.)
