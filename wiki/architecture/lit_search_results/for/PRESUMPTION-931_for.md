SEARCH-FOR-PRESUMPTION-931:
  Date searched: 2026-09-09
  Original item: PRESUMPTION-931
  Original statement: [inferred] Scheduler liveness is estate health — if the jobs fired, the system is
    working, and the freshness of what they produced is a separate and lesser question.
  Routed question: does process-liveness monitoring systematically mask output-staleness failures, and
    do freshness/SLO-based checks detect classes of failure that exit-status checks structurally cannot?

  DIRECTION NOTE: the intake routes the CORRECTIVE proposition to 15a — the FOR-claim is "liveness
    masks staleness; freshness checks catch what exit status cannot," and the intake's own AGAINST line
    ("evidence that liveness checks are adequate proxies for output health") goes to 15b. This means a
    SUPPORTED result here is evidence AGAINST the presumption as stated. Recorded explicitly so 14b's
    reconciliation does not invert the sign.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-931
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred from two same-morning reports that disagree because they ask different questions,
        neither of which states which question it is asking — the `Morning project status` 08:00 report
        ("all of today's jobs fired on schedule … Nothing is broken") read against the 09:45Z scheduler
        health check's five freshness FAILs on the same estate.
      15a: Searched for supporting literature (2026-09-09), FOR direction only.
    Current status: SUPPORTED

  PREMISE-REGISTER OVERLAP (checked before searching, per DEFECT-G): HEAVY — THIS ITEM IS SUBSTANTIALLY
  REGISTER-HELD AND THE SEARCH WAS NARROWED ACCORDINGLY.
    Grepped for: liveness, freshness, staleness, watermelon, symptom-based, green dashboard, exit
    status, heartbeat.
    Five ACTIVE premises already cover the ground:
    - PREMISE-100: "A liveness signal (lastRunAt / heartbeat) is not evidence of correctness, and a
      health check that cannot execute in its runtime context reports as passing rather than as absent;
      monitoring that conflates the two produces false-green at a rate proportional to the number of
      inoperable checks." THIS IS PRESUMPTION-931'S DENIAL, ALREADY VALIDATED.
    - PREMISE-086: alarm on the AGE of the last dated PASS/FAIL, not on the last displayed value;
      names "the perceived-liveness trap" by that name; requires a monitor-of-monitor. Its
      supporting-evidence line already credits "Google SRE Book (freshness / absence-of-signal
      alerting)" at 15a SUPPORTED/Strong.
    - PREMISE-089: freshness/liveness is a PER-SOURCE property; cross-source liveness inference is a
      known anti-pattern. Already cites the data-observability vendor literature at 15a
      SUPPORTED/Strong.
    - PREMISE-110: a monitor's pass-state is reachable while the subject is dead.
    - PREMISE-171: a declaration register is not a failure detector; completeness = 0; includes the
      launchd/cron "skipped and never run, silently" vendor statement, VERIFIED in that run.
    ASSESSMENT: PRESUMPTION-931 states, as an unexamined belief, the exact proposition that PREMISE-100
    was minted to deny. There is nothing new to establish. WHAT I SEARCHED, therefore, was narrow: the
    one gap I could identify is that the register's coverage is about MONITOR OUTPUT SEMANTICS
    (086/100/110) and REGISTER SEMANTICS (171), whereas 931 is about a HUMAN-FACING NARRATIVE REPORT
    that asserted estate health from firing status. I looked for the canonical statement that error-code
    channels are STRUCTURALLY incapable of detecting wrong-content failures, which is the sharpest form
    of the routed question and which the register asserts but does not, so far as I can see, source to a
    verified verbatim.
    RECOMMENDATION TO 15c UP FRONT: this should almost certainly NOT mint a new premise. PREMISE-138
    bars re-minting and PREMISE-100 already holds the claim. The right disposition is a REVISE or
    MONITOR binding the morning-report generator to PREMISE-100 and PREMISE-086, not a new PREMISE.

  Supporting evidence found: Yes

  Sources:
    1. Ewaschuk, R. (author), Beyer, B. (editor), "Monitoring Distributed Systems," Chapter 6 of Beyer,
       B., Jones, C., Petoff, J. & Murphy, N.R. (eds.), Site Reliability Engineering: How Google Runs
       Production Systems, O'Reilly / Google, 2016. sre.google/sre-book/monitoring-distributed-systems/
       [VERIFIED: FULL CHAPTER RETRIEVED AND READ THIS RUN. Chapter number, author and editor
       attribution, and the copyright line "Copyright © 2017 Google, Inc. Published by O'Reilly Media,
       Inc." read directly from the page. The 2016 first-publication date is from general knowledge and
       is not on the page; the page's own copyright year is 2017] — This is the load-bearing source and
       it answers the routed question's second limb directly and verbatim. From the "Four Golden
       Signals" section, on the Errors signal, quoted exactly: requests can fail "either explicitly
       (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with the
       wrong content), or by policy." And then the structural claim, quoted exactly: "catching HTTP 500s
       at your load balancer can do a decent job of catching all completely failed requests, while only
       end-to-end system tests can detect that you're serving the wrong content." Transposed to a
       scheduled estate, exit status IS the HTTP-500 channel and "fired on schedule" IS the 200 — and
       the canonical SRE text states, as doctrine, that the success-code channel structurally cannot see
       the wrong-content class, which requires a different instrument entirely. The chapter also makes
       the symptoms/causes distinction the organising principle of good monitoring ("'What' versus 'why'
       is one of the most important distinctions in writing good monitoring") and concludes: "it's
       better to spend much more effort on catching symptoms than causes." Job-fired is a cause-channel
       signal; output freshness is the symptom. WEIGHT: Strong. Canonical, verified, read in full, and
       it says the thing.
    2. Site Reliability Engineering, Chapter 25 "Data Processing Pipelines" and Chapter 26 "Data
       Integrity: What You Read Is What You Wrote."
       [VERIFIED: both chapter titles and their positions in the book exist — read from the chapter list
       in the sidebar of the Chapter 6 page retrieved this run. CHAPTERS THEMSELVES NOT READ] — Recorded
       as a pointer only, because the existence of a chapter titled "What You Read Is What You Wrote" in
       the canonical SRE text is itself a signal that output-correctness monitoring is treated as a
       distinct discipline from job monitoring. NO CLAIM RESTS ON THIS BEYOND THE TITLES.
    3. The "watermelon" pattern — green on the outside, red on the inside.
       [PRACTITIONER LEVEL ONLY. Retrieved this run from ITSM and observability vendor blogs
       (HappySignals, Alloy Software, Last9/dev.to) and a Forbes council post. NO PEER-REVIEWED SOURCE
       LOCATED FOR THIS TERM. NONE READ IN FULL. I am not attributing the coinage to anyone] — The
       industry's name for exactly PRESUMPTION-931's failure: dashboards report green while the people
       downstream are not served. The reported diagnosis is that the indicators do not capture the
       experience they are taken to represent. WEIGHT: Weak as evidence, useful as VOCABULARY. It gives
       the estate a shared name for the 08:00-vs-09:45Z discrepancy. It should not be cited as a finding.
    4. Data-freshness SLO / data-downtime practice.
       [PRACTITIONER LEVEL ONLY — vendor documentation and engineering blogs (dbt Labs, Databricks,
       Conduktor, Streamkap, Tacnode, PipeCode) retrieved this run; NONE READ IN FULL] — Convergent
       practitioner consensus, stated in several independent places: stale data "looks perfectly normal"
       — dashboards render, queries return, no errors are raised; a pipeline can be green on every
       operational metric and still be outside its freshness contract. The mature pattern reported is to
       define freshness precisely (max-timestamp lag, ingestion lag), express it as an SLI/SLO with a
       freshness budget, and back it with heartbeats and dead-man's switches. WEIGHT: Weak
       individually, Moderate in aggregate as evidence that an entire tool category exists BECAUSE
       exit-status monitoring does not cover this class. NOTE: PREMISE-089 already carries this
       literature (Elementary Data, Sifflet, Metaplane) at 15a SUPPORTED/Strong, so this is
       corroboration of an existing register entry, not new evidence.
    5. Silent-failure research in production ML and agent runtimes.
       - "Towards Observability for Production Machine Learning Pipelines," arXiv:2108.13557.
         [VERIFIED: arXiv identifier and exact title confirmed via the arXiv abstract listing retrieved
         this run. AUTHORS NOT VERIFIED AND DELIBERATELY NOT NAMED. PAPER NOT READ] — Reported framing
         from the listing: production ML systems "fail silently — not with crashes, but through wrong
         decisions," and suffer specifically from "corrupted or stale subsets of features." That is the
         exact fault class, named as the motivating problem of a vision paper.
       - "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM
         Agent Runtime," arXiv:2606.14589.
         [ALREADY REGISTER-HELD — cited in PREMISE-109's evidence line via
         lit_search_results/for/PRESUMPTION-503_for.md. NOT RE-VERIFIED THIS RUN]
       - "Evaluation Blindness: How Silent Measurement Failures …," arXiv:2608.02786.
         [SNIPPET LEVEL ONLY. Title truncated in the search result and I have not completed it; the
         reported headline figure — 53% of verifiable public incidents are silent — IS FROM A SEARCH
         SNIPPET AND UNVERIFIED. Included because it is the only quantitative figure found in this
         direction, and flagged hard because of that] WEIGHT: Moderate as a body, Weak per item.

  Strength of support: Strong — but note carefully that most of the strength comes from ONE verified,
    canonical, fully-read source (SRE ch. 6) plus a register that already holds the claim. The
    surrounding material is practitioner-grade.

  Summary: The routed question's second limb is answered affirmatively by the canonical text, verbatim
  and verified: catching error codes "can do a decent job of catching all completely failed requests,
  while only end-to-end system tests can detect that you're serving the wrong content." Exit-status and
  fired-on-schedule signals live on the error-code channel; output staleness lives on the wrong-content
  channel; the SRE text states these are different instruments, and organises its whole monitoring
  philosophy around preferring the symptom over the cause. That is precisely the 08:00-vs-09:45Z split
  14b observed — the morning report answered "did the causes fire?" and the health check answered "is
  the symptom present?", and only the second is the question the reader thought was being answered. The
  practitioner literature on data freshness converges independently and supplies the operative detail:
  stale output raises no error, so its absence of signal is indistinguishable from health unless
  freshness is measured as its own quantity against its own budget. The industry name for the resulting
  report is the watermelon dashboard. None of this is new to C2A2 — PREMISE-100 already states the
  denial of PRESUMPTION-931 in almost the same words, and PREMISE-086 already names the
  "perceived-liveness trap." What the literature adds is a verified canonical citation for the
  STRUCTURAL limb, which the register asserted but did not source verbatim.

  Caveats:
  (a) THE STRONGEST SOURCE IS DOCTRINE FROM ONE ORGANISATION, NOT A MEASUREMENT. The SRE chapter is
      Google's engineering philosophy, explicitly described in its own text as "a bit aspirational." It
      states that error-code monitoring cannot see wrong content; it does not measure a detection gap.
      I found NO study quantifying what fraction of scheduled-job failures are invisible to exit-status
      monitoring but visible to freshness checks. The one quantitative figure encountered (53% of
      incidents silent) is snippet-level and unverified. If the estate wants a number, it does not exist
      in what I searched.
  (b) THE PRACTITIONER SOURCES HAVE A COMMERCIAL INTEREST. Every data-freshness source found is a vendor
      selling freshness monitoring. Their convergence on "job success does not imply data freshness" is
      still informative — it is a claim against the adequacy of the free alternative, made by parties
      who would say it whether or not it were true. Weight accordingly. PREMISE-089 already rests on the
      same vendor corpus and inherits the same caveat.
  (c) THE PRESUMPTION IS ALREADY DENIED IN-HOUSE, WHICH CHANGES WHAT THIS RESULT IS FOR. Since
      PREMISE-100 is ACTIVE, the finding is not "we have learned something" but "a scheduled report
      violated an active premise." That is a PROPAGATION failure, and PREMISE-116's finding is directly
      on point: a recorded premise does not change the behaviour it governs unless propagation is
      engineered and confirmed. The literature result here is corroborative; the actionable observation
      is that the morning-report generator does not read the register.
  (d) SCOPE OF THE TRANSPOSITION. The SRE quote is about HTTP request serving. Applying "200 with wrong
      content" to "scheduled job with stale output" is an analogy — a good one, and the same analogy the
      data-freshness literature makes independently, but the source does not itself make it.
  (e) FRESHNESS ALERTING HAS ITS OWN KNOWN FAILURE, AND THE REGISTER ALREADY RECORDS IT. Register line
      ~4308 notes the preference for displaying artefact AGE over adding a pass/fail freshness alert per
      artefact per path, because "freshness is a high-volume alert class." PREMISE-131's habituation
      clause and PREMISE-119's override-rate finding both bear. Answering 931 with more freshness alerts
      risks the alert-fatigue failure the register has already validated.
  (f) SEARCH SCOPE: narrowed deliberately (see overlap section) — three queries, one full-text
      verification. Not covered: process-safety alarm philosophy (EEMUA 191 / ISA-18.2), which the
      intake named and which I did not reach; Kubernetes liveness-vs-readiness probe design literature;
      the SRE book's own Chapters 25 and 26 in full.

  Recommendation: SUPPORTED
    (for the routed proposition: liveness/exit-status monitoring structurally cannot detect the
     output-staleness class, and freshness checks detect failures it cannot — therefore
     PRESUMPTION-931 AS STATED IS UNSOUND.)
    DISPOSITION STEER FOR 15c: do NOT mint. PREMISE-100 and PREMISE-086 already hold this. The gap is
    propagation to the morning-report generator, not knowledge.
