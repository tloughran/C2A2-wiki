SEARCH-FOR-PRESUMPTION-953:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-953
  Original statement: "[inferred] That the estate's daily reports are read — that a finding correctly
    surfaced to a human is a finding on its way to being handled."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-953
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a convergence of six independent terminal requests in one day against a
        measured response record. Stated without accusation: the 36-card batch APPROVE is direct
        evidence the reader is there; the fourteen-day gap is direct evidence the latency is long.
      15a: Searched for supporting literature; found that the only well-measured version of this
        question is the audit/alert-response literature, and that it makes implementation a function of
        the *follow-up mechanism* rather than of the report.
    Current status: NO-SUPPORT-FOUND (for the unconditional presumption); PARTIALLY-SUPPORTED
      (conditional on an explicit tracking mechanism)

  Register pre-check: This is the most heavily pre-answered item of the ten, and the register's position
    is already adverse.
    - PREMISE-102 (ACTIVE) — "Fail-loud is an act of reporting, not an act of remediation. Where the
      notified channel has demonstrated zero throughput, repeated identical non-processing converts a
      one-time signal into an undecided standing policy of non-coverage; the loudness of the report is
      not evidence that anything is received."
    - PREMISE-108 (ACTIVE) — "Transmission is not delivery... the loop is closed only on evidence that
      the recipient received AND acted, and until then the finding is held by nobody while the record
      shows it discharged. That state is worse than not flagging."
    - PREMISE-116 (ACTIVE) — a finding does not change the behaviour it describes; the best-measured
      analogue is audit and feedback. **This premise already names the literature this search found.**
    - PREMISE-123 (ACTIVE) — a validated finding does not reach the agent it governs unless an explicit
      propagation mechanism carries it.
    - PREMISE-131, PREMISE-138 (ACTIVE) — a warning is not a control; repetition in a channel with no
      effector is not a remedy.
    Recording the hits per OPEN-192; searched anyway. Note that PREMISE-102 and PREMISE-108 between them
    appear to settle this item already, which is itself a datum for OPEN-192.

  LIMB SPLIT:
    Limb A (THE READER EXISTS AND READS): reports addressed to the principal are in fact read.
    Limb B (SOON ENOUGH TO MATTER): the reading happens at a latency short enough that deferring a fix
      to the reader is a responsible disposition.

  Supporting evidence found: Partial (Limb A), No (Limb B)

  Sources:
    1. Municipal and supreme-audit-institution follow-up reporting (Oakland City Auditor, *Audit
       Recommendation Follow-Up Report*, March 2024; South Florida Water Management District follow-up
       report 2023 Q2; EUROSAI 2021, *Follow-up of the implementation of audit recommendations*;
       Office of the Auditor General of Canada performance-audit manual §8020). — SECONDARY (PDFs
       located, tables not retrieved) — Departments implemented **44%** of recommendations from reports
       issued 2014–2023. Implementation rate by follow-up method: **61%** under formal follow-up, **82%**
       under self-assessment (the inversion is a measurement-validity artefact — self-assessed status is
       self-reported — and should not be read as self-assessment working better; it is a live warning
       about how the estate would measure its own latency). Over ten years, **21 repeat
       recommendations, 16 partially or not implemented**. This is the best-measured analogue to the
       estate's situation and it supports Limb A weakly (things do get implemented) while refuting Limb
       B (most do not, and the ones that do are carried by an apparatus).
    2. Audit follow-up practice as a mechanism (eCampusOntario, *Internal Auditing: A Practical
       Approach* §10.03 "Follow-Up: Monitoring and Verification"; ISACA follow-up-audit guidance, 2025).
       — SECONDARY — The Recommendation Implementation Status Summary is issued **90 days** after the
       final report, forcing a status and a target date; aging is reported in 30/60/90-day buckets. The
       structural finding: in every mature practice, implementation is produced by a *tracking system
       with forced responses and aging*, not by the quality of the report. The estate has excellent
       reports and no tracker.
    3. Static-analysis alert-response literature (Heckman & Williams actionable-alert work as reported
       in arXiv:2509.11787; *How Do Developers Act on Static Analysis Alerts? An Empirical Study of
       Coverity Usage*; Tricorder, in *Software Engineering at Google* ch. 20). — SECONDARY — Only
       **27.4%–49.5% (median 36.7%)** of alerts are actionable; and, the finding that matters here, "if
       developers mark reports in a particular scan as false positives, then they are less likely to
       triage future reports in the same file." A backlog of surfaced-but-unhandled findings degrades
       future attention to the same surface. The estate is accumulating exactly such a backlog.
    4. Clinical decision support override literature (Systematic review, *Appropriateness of Overridden
       Alerts in Computerized Physician Order Entry*, 23 articles, PMC7400042; JMIR Med Inform 2022
       e40511). — SECONDARY — Override rates range **46.2%–96.2%** across alert types; individual
       studies report **92.9%** and **92.2%** for drug-drug interaction alerts. The domain is a
       high-stakes channel with a professional reader who is present, attentive and trained, and the
       finding is still that most well-formed warnings are dismissed. If the presumption fails there, a
       daily-report channel is not a stronger case.
    5. Guo & Engler, 2009, "Linux Kernel Developer Responses to Static Analysis Bug Reports," USENIX
       ATC. — UNVERIFIED — located, not retrieved. The primary study of developer response to surfaced
       defects; named so a later run can read it.
    6. Email response-time benchmark material (EmailAnalytics Q1 2026 industry report; Emailmeter;
       Gmelius). — **UNVERIFIED as evidence, and I want this flagged clearly.** These are marketing
       assets from email-analytics vendors. The circulating figures — median reply ~1.78h; work-hours
       mean ~3h57m; overall mean ~11h28m; "62% of companies never respond to inbound emails"; and a
       "16 billion emails / 2 million users, median reply 2 minutes" study whose primary citation I
       could not locate — **carry no weight in this rating.** I list them only because they are what a
       search on this question returns, and a later run should not mistake them for findings. The
       underlying academic work (Kooti et al., *Evolution of Conversations in the Age of Email
       Overload*, WWW 2015) is the likely origin of the 2-minute median and was not retrieved.

  Strength of support: Weak (Limb A), None (Limb B)

  Summary: This is the item where the FOR direction is thinnest and the reason is structural: there is
    no literature on "are internal reports read," only literature on "are surfaced findings acted on,"
    and the answer there is consistently no-by-default and yes-with-an-apparatus. The audit literature
    is the closest analogue and the most usable: 44% implementation over a decade, produced by a
    90-day forced-status cycle and 30/60/90 aging buckets, in organisations with dedicated follow-up
    staff. The clinical alert literature is the adverse bound: 46%–96% override rates with a trained
    professional reader physically present. The static-analysis literature supplies the compounding
    mechanism: an unhandled backlog suppresses future triage of the same surface. Limb A survives at low
    strength — readers do exist and do act, and the estate has a direct positive datum in the 36-card
    batch APPROVE that is stronger than anything I found in the literature. Limb B does not survive at
    all, and Limb B is the one every deferral depends on. Note the shape 14b identified is exactly
    right: the honest measurement is a latency distribution, and the audit literature's 30/60/90 aging
    buckets are a ready-made schema for producing one.

  Caveats: Every quantitative source here is cross-domain — public-sector audit, clinical prescribing,
    large-scale software — into an estate with one reader, one principal and no follow-up staff. The
    rates transfer not at all; the *mechanism* finding (implementation tracks the apparatus, not the
    report) is what transfers, and it transfers well because it is structural. The email figures are
    vendor benchmarks and are excluded from the rating. I could not retrieve Guo & Engler or the Kooti
    et al. primary, which are the two sources that would most improve this file.

  Search scope: comprehensive for the act-on-findings limb, unsuccessful for the read-latency limb —
    searched audit recommendation implementation and follow-up mechanisms, static-analysis alert triage
    and fix rates, clinical decision support override rates and alert fatigue, escalation latency in
    incident management, and organisational email response-time distributions (which returned only
    vendor material). Did not search the organisational-communication literature on information overload
    or the "audit and feedback" Cochrane review that PREMISE-116 already cites — the latter is the
    single highest-value unretrieved source for this item and should be read directly.

  Recommendation: NO-SUPPORT-FOUND. The recommendation rests on Limb B, which is the limb carrying 14b's
    Critical risk and on which every "flagged, not fixed" disposition in the estate banks. Limb A is
    PARTIALLY-SUPPORTED and should be recorded separately: the reader is real, and the batch APPROVE
    proves it. What the literature supplies is not a verdict but a shape — implementation is a function
    of the tracking apparatus, and the estate has none, so the presumption is currently unfunded rather
    than false. The in-house measurement 14b specifies (latency distribution of human-addressed requests
    over 30 days, in 30/60/90-day buckets, per the audit RISS pattern) is the only thing that will
    settle it, and it is cheap. Until it exists, a deferral to the reader should not be recorded as a
    disposition — which is PREMISE-108 restated.
