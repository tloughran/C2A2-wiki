SEARCH-FOR-PRESUMPTION-875:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-875
  Queue ref: LIT-QUEUE-2026-08-24-007
  Original statement: "An unbounded accumulating queue is the right structure for a human review gate."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-875
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from absent alternatives across a sixteen-day discussion with a one-member remedy space
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-25. Queries covered (a) the affirmative case for unbounded
    accumulating review queues — completeness, auditability, no-item-lost guarantees; (b) general
    queue-discipline and backlog literature (queueing theory, WIP queues, capacity planning for
    queue recovery, content-moderation admission control); (c) messaging-systems literature on
    durable append-only logs, at-least-once delivery, bounded vs. unbounded buffers and
    backpressure; (d) regulated-domain registers that forbid automatic expiry (audit-finding
    lifecycles, ISO 27001 findings registers, risk registers, pharmacovigilance signal
    management); (e) the special case where server availability is zero rather than merely low —
    approached via queueing models with server vacations, breakdowns, and bulk/batch service.
    Venues reached: arXiv, ScienceDirect/Elsevier, SAGE, PMC/PubMed, AIMS, MDPI, InfoQ, AWS
    Builders' Library, vendor and practitioner documentation. Date range: no restriction; hits
    cluster 1998–2026.
    Assessment: **preliminary — broader search recommended**. Gaps: (i) I could not retrieve the
    AWS Builders' Library PDF ("Avoiding insurmountable queue backlogs") — the fetch was blocked
    as out-of-provenance, so it is cited SNIPPET-ONLY; (ii) the web-search budget was exhausted
    before I could search event-sourcing/backlog-as-option-value framings or the operations-
    research literature on *deliberately* uncapped work-in-process; (iii) I found no source that
    addresses a review queue whose server availability is identically zero over the observation
    window, as opposed to intermittently zero.

  Supporting evidence found: Partial

  Sources:
    1. AWS Builders' Library. "Avoiding insurmountable queue backlogs." Amazon Web Services
       (undated). https://d1.awsstatic.com/builderslibrary/pdfs/avoiding-insurmountable-queue-backlogs.pdf
       — Canonical practitioner treatment of durable queues as the correct structure when work
       must not be lost, alongside the mechanisms needed to keep such a queue survivable.
       SNIPPET-ONLY (full-text fetch blocked as out-of-provenance; cited from search result only).
    2. "At-Least-Once vs. At-Most-Once vs. Exactly-Once: Choosing by Failure Mode." OneUptime blog,
       2026-07-21. https://oneuptime.com/blog/post/2026-07-21-delivery-semantics-failure-modes/view
       — States the affirmative case directly: at-least-once semantics require the producer to
       write to a durable log or queue and the consumer to acknowledge only after processing; the
       broker redelivers on consumer failure. Explicitly names retention expiry and exhausted
       retry policy as the ways work *is* lost — i.e. the no-item-lost guarantee is purchased by
       *not* expiring items. SNIPPET-ONLY.
    3. Chandna, A. "Append-only Log: The core of Kafka." Medium (undated).
       https://medium.com/@aryan25822/append-only-log-the-core-of-kafka-5740fc965fe7
       — Describes the append-only discipline (records written once, monotonically increasing
       offset, consumers never remove) that underwrites replay and audit. Supports the structural
       half of the presumption: accumulation without disposition is a recognised, deliberate design.
       SNIPPET-ONLY.
    4. Vanlightly, J. "The advantages of queues on logs." jack-vanlightly.com, 2023-10-02.
       https://jack-vanlightly.com/blog/2023/10/2/the-advantages-of-queues-on-logs
       — Argues that layering queue semantics over a durable log gives both per-item disposition
       and full retention/replay, i.e. that accumulation and auditability are complementary rather
       than opposed. SNIPPET-ONLY.
    5. "Message Queue: A Guide to Asynchronous Communication." Kestra resources (undated).
       https://kestra.io/resources/infrastructure/message-queue
       — Supports the temporal-decoupling argument: unbounded capacity lets a queue absorb bursty
       or unpredictable workloads "without artificial limits," so the consumer can work at a
       sustainable rate. This is the strongest form of the affirmative case for *not* capping.
       SNIPPET-ONLY.
    6. "Audit Findings Lifecycle: From Identification to Closure." AuditFindings.com (undated).
       https://www.auditfindings.com/audit-findings-lifecycle/ — and companion practitioner
       sources: "Audit Finding Closure Process" (FieldPie), "ISO 27001 Audit Findings Register"
       (Auditor-Docs), "Risk Register Guide for Compliance Teams" (audited.online).
       — Converging practitioner/standards position that findings do **not** close automatically:
       a finding is opened at identification and remains open through remediation until *formally*
       closed with retained evidence. This is the regulated-domain analogue of an accumulating
       queue with no TTL, and it is the current norm, not a deviation. SNIPPET-ONLY.
    7. Malikova, M. A. (2020). "Practical applications of regulatory requirements for signal
       detection and communications in pharmacovigilance." Therapeutic Advances in Drug Safety.
       DOI: 10.1177/2042098620909614. https://journals.sagepub.com/doi/10.1177/2042098620909614
       (PubMed 32313617)
       — Documents a domain (EMA GVP Module IX; FDA 15-day Alert Reports) in which every case must
       enter a managed pipeline through validation, prioritisation and assessment, with no
       provision for silently dropping unassessed items. Supports the completeness rationale for
       exhaustive rather than sampled review. ABSTRACT-ONLY.
    8. Performance analysis of an infinite-buffer batch-size-dependent bulk service queue with
       server breakdown and multiple vacation. Journal of Industrial and Management Optimization,
       AIMS. DOI: 10.3934/jimo.2022143.
       https://www.aimsciences.org/article/doi/10.3934/jimo.2022143 [authors unverified]
       — Directly relevant to the zero-availability sub-case: formal *infinite-buffer* models in
       which the server is unavailable for extended, repeated intervals (vacations, breakdowns)
       and then serves accumulated work in batches. Establishes that an uncapped accumulating
       queue with a frequently-absent server is a tractable, stable, well-studied structure —
       provided vacations terminate. ABSTRACT-ONLY.
    9. "Analysis of Bulk Queueing Model with Load Balancing and Vacation." Axioms 14(1):18 (2025?),
       MDPI. https://www.mdpi.com/2075-1680/14/1/18 [authors and year unverified]
       — Companion evidence that stability conditions for vacation/bulk-service systems are
       derivable (matrix-geometric methods); i.e. accumulation between service epochs is a
       designed feature of these models, not a pathology. ABSTRACT-ONLY.
   10. "Markovian bulk service queue with delayed vacations." Computers & Operations Research (1998).
       DOI via https://www.sciencedirect.com/science/article/abs/pii/S0305054898000033
       [authors unverified]
       — Establishes the antiquity and maturity of the bulk-service-with-vacations family: the
       server waits until a threshold batch has accumulated before serving. Accumulating until a
       batch is worth processing is an *optimal* policy in this family, which is the sharpest
       supportive result for batched rather than per-item disposition. ABSTRACT-ONLY.

  Strength of support: Moderate

  Summary: The literature supplies a coherent affirmative case for the two components of this
    presumption that concern *retention* and *exhaustiveness*, and a weaker but real case for
    *accumulation*. On retention: durable-log and at-least-once delivery semantics are the
    standard answer whenever losing an item is worse than delaying it, and the explicit lesson of
    that literature is that items are lost precisely at retention expiry and exhausted retry — so
    declining to set a TTL is the mechanism by which the no-item-lost guarantee is obtained.
    On exhaustiveness: regulated audit-finding and risk registers are the closest institutional
    analogue to a human review gate, and their governing convention is that a finding remains open
    until formally closed with retained evidence, never by lapse of time. On accumulation:
    queueing theory contains a large, mature family of infinite-buffer models with server
    vacations, breakdowns and bulk service, in which the server is *routinely absent* and work is
    deliberately allowed to pile up until a batch worth serving has formed — batch-threshold
    policies are optimal in that family, which supports batch rather than per-item disposition.
    Burst-absorption and temporal-decoupling arguments add that an uncapped buffer lets a slow
    consumer work at a sustainable rate rather than at the arrival rate.

  Caveats: Every supportive strand is conditional on the server eventually serving. The
    vacation/bulk-service results are stability results, and stability in those models requires
    that vacations terminate and that mean service capacity exceed mean arrival rate; they say
    nothing favourable about a system in which availability is identically zero over the whole
    observation window. The messaging literature that supports unbounded retention does so in a
    setting where storage is cheap, items are machine-consumable, and replay is the point —
    none of which transfers cleanly to items whose consumption is scarce human attention. The
    audit-register analogy supports *no automatic expiry* but not *no periodic review*: the same
    practitioner sources pair open-until-closed with mandatory review dates and named owners, so
    they support the retention limb while being silent-to-unhelpful on the accumulation limb. The
    burst-absorption argument is explicitly a *transient* argument (absorb a spike, drain it
    later) and does not extend to a monotone arrival process with no drain. Finally, several of
    the supportive sources are practitioner blogs and vendor documentation rather than
    peer-reviewed work.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that not setting a TTL is the correct way to obtain a no-item-lost
    guarantee; (ii) that exhaustive rather than sampled disposition, with items open until
    formally closed, is the established norm in auditable/regulated review; (iii) that batched
    rather than per-item disposition is optimal when the server is intermittently absent.
    Unaddressed sub-claim: **that an unbounded accumulating queue remains the right structure when
    the server's availability is not merely low or intermittent but zero over the entire interval
    of interest.** No source located treats the identically-zero-service case. The queueing
    literature reaches it only as a degenerate limit outside its stability conditions, and the
    audit-register literature assumes an owner exists. The affirmative case for an uncapped queue
    with a never-present server is, so far as this search found, unaddressed in the literature.
