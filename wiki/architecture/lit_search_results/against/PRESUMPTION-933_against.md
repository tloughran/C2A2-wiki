SEARCH-AGAINST-PRESUMPTION-933:
  Date searched: 2026-09-09
  Original item: PRESUMPTION-933
  Original statement: [inferred] Agents fail loudly — a run that reports nothing has nothing to report,
    so silence from a scheduled task is evidence of an uneventful run rather than of an unobserved one.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-933
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from two same-day silent runs that no consumer recorded as silent —
        `metabolism-regen-daily` produced no terminal verdict of any kind under a fail-loud spec, and
        `morning-system-health` stalled at a permission prompt and wrote no report. Both were counted
        as fired.
      15b: Searched for challenging literature (2026-09-09), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output for this item.
    Current status: CHALLENGED

  Challenging evidence found: Yes — strongly, and from four independent literatures that agree.

  Sources:
    1. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R., 2017. "Gray
       Failure: The Achilles' Heel of Cloud-Scale Systems." Proceedings of HotOS '17, Whistler BC,
       pp. 150–155. doi 10.1145/3102980.3103005.
       [VERIFIED: full PDF retrieved from Microsoft Research and read this run; all quotations
       verbatim.] — The single most on-point source found, and it names C2A2's exact failure geometry.
       The paper's central concept is *differential observability*: "a system is defined to experience
       gray failure when at least one app makes the observation that system is unhealthy, but observer
       observes that system is healthy." The illustrative example is almost a description of
       `morning-system-health`: "if a system's request-handling module is stuck but its heartbeat
       module is not, then an error-handling module relying on heartbeats will perceive the system as
       healthy while a client seeking service will perceive it as failed." On prevalence, from
       production Azure: "Our first-hand experience with production cloud systems reveals that gray
       failure is behind most cloud incidents." On the inadequacy of the fail-stop model that
       PRESUMPTION-933 assumes: "such mechanisms are inadequate to deal with gray failure, and in some
       cases even aggravate the situation. They often go wrong by assuming an overly simple failure
       model in which a component is either correct or stopped (i.e., fail-stop)." And on the specific
       consequence of silence: in their §2.2 case, "no recovery happens until a user reports an issue.
       This creates a long gap between the time when a user is affected and the time when the system
       becomes aware of the failure." The paper's prescription is exactly the one PRESUMPTION-933
       forecloses: "we advocate moving from singular failure detection (e.g., with heartbeats) to
       multi-dimensional health monitoring." Finally, and directly against any "this only matters at
       Azure scale" defence: "gray failure is not unique to large systems. Small-scale or even
       single-node systems can also experience peculiar failure symptoms."
    2. HHS Office of Inspector General, 2012. "Hospital Incident Reporting Systems Do Not Capture Most
       Patient Harm." Report OEI-06-09-00091, issued 2012-01-05.
       [VERIFIED: report page retrieved and read this run; figures quoted from it. Full 1.9 MB PDF not
       opened.] — The human analogue, with a hard number. Incident reporting systems "captured only an
       estimated 14 percent of the patient harm events." Of the missing 86%, hospital administrators
       classified 61% as "events that staff did not perceive as reportable" and 25% as "events that
       staff commonly report but did not report in this case." The first category is the one that
       matters for C2A2: the dominant cause of silence was not concealment or system failure but the
       reporter not classifying the event as reportable — an agent completing a run and not recognising
       that what happened was worth reporting. And the systems were being relied upon: administrators
       "indicated that they rely heavily on the systems to identify problems." A self-report channel
       trusted as complete, capturing one event in seven.
    3. Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed
       Systems." Journal of the ACM 43(2):225–267 (earlier tech-report version, 1991/1993, is on DTIC);
       with Chandra, Hadzilacos & Toueg, 1996, "The weakest failure detector for solving consensus,"
       JACM 43(4).
       [PARTIALLY verified — the DTIC PDF (ADA269016) and the ACM DL listing for the weakest-failure-
       detector paper were seen in search listings and the concepts confirmed across multiple
       independent secondary sources; neither paper was opened this run, so the properties below are
       stated as the field states them and no page or theorem number is claimed.] — The theoretical
       result: failure detectors are characterised by *completeness* (eventually suspecting every
       process that crashes) and *accuracy* (limiting wrong suspicions), and in an asynchronous system
       the two cannot both be had perfectly — a consequence of the FLP impossibility result (Fischer,
       Lynch & Paterson, 1985) that no deterministic consensus protocol tolerates even one crash
       failure. The load-bearing point for C2A2 is elementary and decisive: in an asynchronous system a
       stalled process and a slow process are formally indistinguishable from the outside. C2A2 runs
       agents under a scheduler with no bounded response time — it is an asynchronous system by
       construction — so "no report yet" cannot in principle be distinguished from "no report coming"
       without an external timeout. `morning-system-health` blocked on a permission prompt is not an
       implementation bug; it is the textbook case.
    4. Silent data corruption at fleet scale: Hochschild, P., Turner, P., Mogul, J.C. et al., 2021,
       "Cores that don't count," HotOS '21 (Google); and Meta/Facebook, 2021, "Silent Data Corruptions
       at Scale" (arXiv, Feb 2021) / "Silent data corruption: Mitigating effects at scale," Engineering
       at Meta.
       [NOT-verified — the Google HotOS PDF and the Meta engineering post appeared in search listings
       and are cross-referenced by multiple independent secondary sources; neither was opened this run.
       The rate figures below are from search summaries and should be treated as indicative.] —
       Reported: mercurial cores miscompute silently; Meta's fleet study reported SDC-inducing defects
       on the order of 1 in 1,000 cores; Google reported machines "credibly accused of corrupting
       multiple different stable well-debugged large-scale applications" while "conventional
       diagnostics found nothing wrong with them." Included because it establishes the floor: silence
       is not evidence of correctness even at the level of arithmetic, in fleets with vastly better
       instrumentation than this estate has.
    5. Self-report validity meta-analyses across domains — pro-environmental behaviour (r ≈ .46 with
       objective measures, 79% of variance unexplained); self-control measures (self-report vs cognitive
       test, r ≈ .06–.13); TPACK (r ≈ 0.243); device-measured vs self-reported sedentary behaviour
       (systematic review, 185 studies).
       [NOT-verified — all from search summaries; none opened this run, and the domains are remote from
       C2A2's.] — Cited only to answer the intake's request for the reverse direction: I looked for
       contexts in which self-report is empirically sufficient and did not find one. Where self-report
       has been validated against an independent measure, agreement ranges from moderate to negligible,
       and the moderating factor repeatedly identified is metacognitive — whether the reporter can
       recognise the thing being reported. That is the same moderator the OIG found (61% "did not
       perceive as reportable"), and it is the one that applies to an agent asked to report on its own
       incomplete run.

  Strength of challenge: Strong

  Summary: This presumption is challenged from four directions that do not share a literature and reach
  the same place. Distributed-systems theory says the inference is invalid in principle: in an
  asynchronous system, silence from a process is formally indistinguishable from slowness, and a
  failure detector that is both complete and accurate cannot exist — which is why the field builds
  external timeouts rather than waiting to be told. Production practice at cloud scale says the failure
  is not a corner case but the norm: Microsoft reports that gray failure is behind *most* cloud
  incidents, defines it precisely as the case where the observer sees health while the app sees
  failure, gives the heartbeat-alive-but-work-stuck example verbatim, and explicitly states that the
  problem is not confined to large systems. The human-organisational analogue supplies the magnitude —
  a trusted self-report channel captured 14% of real events, with the largest loss category being
  reporters who did not recognise the event as reportable. And the hardware work removes the last
  floor: even arithmetic fails silently at rates around 1 in 1,000 cores in instrumented fleets. Note
  the asymmetry that makes this worse than a simple reliability problem: an agent that has stalled, hit
  a permission prompt, or been killed is in exactly the state least able to report on itself, so the
  self-report channel's failure rate is *positively correlated* with the events it is supposed to
  report. Silence is therefore not weak evidence of an uneventful run; it is, conditional on anything
  having gone wrong, the most likely observation.

  Specific risks: (a) Both 09-08 instances are already the failure, not a hypothetical: a fail-loud
  spec that produced no verdict and a stalled task that wrote no report were both counted as fired, by
  every consumer. The presumption has a demonstrated in-house false-negative rate that nobody has
  computed. (b) The error is silent *and* self-concealing — the register that would record "this run
  was silent" is written by the run. There is no consumer in the estate positioned to notice absence,
  which means the error's rate is currently unbounded and unmeasurable from inside. (c) Correlated
  failure: a permission prompt, a credential expiry, a mount loss (cf. ASSUMPTION-1287's H-Drive) or a
  scheduler-host suspension will silence many agents at once, so the estate's most likely failure mode
  is also its least visible one — and it will present as an unusually quiet, apparently healthy day.
  (d) Downstream contamination: any register that treats "no adverse report" as "no adverse event"
  inherits the gap. The daily metrics, the changelog's activity counts, and any "N agents ran cleanly"
  claim are all downstream of this presumption. (e) The interaction with PRESUMPTION-931 is the
  dangerous one: liveness says fired, self-report says nothing, and the conjunction reads as a clean
  run — two independent-looking green signals that are in fact both blind to the same event class.

  Mitigations available: The literature's own answer is to stop asking the process and start asking
  someone else. (i) External heartbeat / dead-man's-switch: each scheduled task registers an expected
  completion window with an independent watchdog; absence of a terminal record within the window is
  itself an event. This converts silence from an absence into a positive signal and is the standard
  answer from the failure-detector literature — accepting, per Chandra–Toueg, that the timeout will
  sometimes be wrong, because a detector that is sometimes wrong is strictly better than one that is
  structurally blind. (ii) Require a terminal verdict record — success *or* failure — written by the
  runner rather than the run, so that the record's existence does not depend on the run's health.
  (iii) Huang et al.'s prescription applied locally: move from singular liveness detection to
  multi-dimensional health, i.e. check the run's declared *outputs* as well as its exit — which is the
  same instrumentation PRESUMPTION-931 needs, so one build serves both. (iv) Approximate the consumer's
  view: probe what a downstream reader would see (is yesterday's file there, is it non-empty, does it
  parse) rather than what the runner says. (v) Record the silence rate explicitly as a metric, so the
  false-negative rate stops being unmeasurable.

  Boundary condition requested by the intake (contexts in which self-report IS empirically sufficient):
  I searched for this and found nothing that would license it here. The nearest defensible statement is
  conditional and narrow: self-report is adequate where (a) the reporter is guaranteed to survive the
  event being reported, (b) the reporter can recognise the event as reportable, and (c) an independent
  channel exists to catch the cases where (a) or (b) fail. Condition (a) fails for stalls and kills by
  construction. Condition (b) is the OIG's 61% category. Condition (c) is what the estate currently
  lacks. Where all three hold, self-report is cheap and fine — but that is a description of a system
  that already has the watchdog, not an argument against building one.

  Search scope: Moderate — 5 queries, 2 successful full retrievals (Huang et al. read in full; OIG
  report page read in full). Literatures covered: cloud gray-failure and failure detection, distributed
  failure-detector theory, healthcare incident under-reporting, fleet-scale silent data corruption,
  self-report validity. Not covered at primary-source level: measured rates of unreported job failure in
  batch/ETL estates specifically (searched; nothing quantitative and peer-reviewed returned — a genuine
  gap), the aviation confidential-reporting (ASRS) literature which is the best candidate for a
  self-report-is-sufficient case, and Gunawi et al.'s cloud outage corpus (seen only as a citation
  inside Huang et al.). The two verified sources are sufficient to establish the challenge at Strong;
  further search would refine the magnitude, not the direction.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-933
  Strongest counterargument: The presumption treats absence of a report as a report of absence, and
  that inference is invalid in three separate senses at once. It is invalid *in principle*: C2A2's
  agents run asynchronously with no bounded response time, and the failure-detector literature's
  founding result is that in such a system a stalled process and a slow one cannot be told apart from
  outside — completeness and accuracy trade off, which is why the discipline builds external timeouts
  instead of waiting to be told. It is invalid *empirically*: Microsoft's production account of gray
  failure defines the exact pathology — the observer sees health while the app sees failure — offers
  the heartbeat-alive-but-request-handler-stuck case as its canonical example, reports that gray
  failure is behind most cloud incidents, and states outright that the problem is not confined to large
  systems. And it is invalid *by the numbers* in the human analogue: a trusted incident-reporting
  channel that administrators "rely heavily on" captured 14% of actual harm, with the dominant loss
  category being reporters who did not perceive the event as reportable. But the sharpest form of the
  objection is the conditional dependence. The self-report channel is not merely unreliable; it fails
  in a way that is correlated with the very events it exists to catch. An agent that stalled at a
  permission prompt, ran out of context, was killed, or lost its mount is precisely the agent least
  able to write a failure record. So silence is not uninformative and it is not weakly informative —
  conditional on something having gone wrong, silence is the *expected* observation. The estate has
  already produced two instances of this on a single day, and no consumer noticed either. That is not
  a warning about a future risk; it is a measurement of the presumption failing, and the only thing
  currently unknown is how often it has happened on the days nobody inferred it.
  What would need to be true for C2A2 to be safe: Every agent would have to be guaranteed to outlive
  every failure it can suffer — no stalls, no kills, no context exhaustion, no permission blocks, no
  host suspension — and to be capable of recognising every failure as reportable, and to have an
  unfailing write path for its report. Those conditions describe a fail-stop system with a reliable
  channel, and C2A2 is neither. A weaker and more realistic sufficient condition: an independent
  channel exists that would notice an absent report. That is exactly what the estate lacks, and
  building it is the whole mitigation.
  How to test: The measurement is cheap and produces the number that is currently missing — the silence
  rate. For 30 days, maintain an external expectation table: one row per scheduled task per day, with
  its expected completion window. At the end of each window, an independent process (not the agent)
  records one of three states: terminal-verdict-written, output-changed-but-no-verdict, or nothing. The
  count in the third bin over 30 days is the direct false-negative rate of the current self-report
  channel, and the count in the second is the gray-failure bin — ran, did something, reported nothing.
  A sharper version, available immediately and retrospectively: take the last 30 days of scheduled runs
  and count how many produced a terminal verdict of any kind. Every run that did not is a day on which
  the estate's health report rested on this presumption. If the answer for `metabolism-regen-daily` is
  more than the one instance already found on 09-08, the presumption has been failing continuously and
  the two observed cases were not anomalies but the first two anyone happened to look for.
