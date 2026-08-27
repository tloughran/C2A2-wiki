SEARCH-FOR-ASSUMPTION-1161:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1161
  Original statement: That a multi-phase job which mutates external state (Gmail labels) before
    committing internal state (proposal moves) is recoverable after a mid-phase death.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1161
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Traced the daily run's termination point and measured the resulting five-day
        review-page gap and queue growth.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, August 2026, no date restriction. Queries covered: saga pattern and
    compensating transactions (incl. the Garcia-Molina & Salem origin paper); the dual-write
    problem and the transactional outbox pattern; idempotency keys and at-least-once delivery
    with non-idempotent side effects; durable-execution workflow engines (Temporal) and
    replay-based mid-workflow crash recovery; Gmail API `users.messages.modify` /
    `users.threads.modify` idempotency semantics. Classification: comprehensive for the
    distributed-transaction and workflow-recovery patterns literature; preliminary on the
    Gmail-specific idempotency question, where official documentation was reached only via
    snippet and the individual `modify` endpoint's retry semantics were not clearly documented.
    Gaps: no full text obtained for the Sagas paper; no empirical/measured study located on
    recovery success rates for external-effect-before-commit orderings specifically.

  Supporting evidence found: Yes

  Sources:
    1. Garcia-Molina, H., Salem, K., 1987. "Sagas." *Proceedings of the 1987 ACM SIGMOD
       International Conference on Management of Data* / ACM SIGMOD Record 16(3):249–259.
       DOI 10.1145/38714.38742. https://dl.acm.org/doi/10.1145/38714.38742
       — [read as search snippet + abstract, not full text] The foundational result: a long-lived
       transaction decomposed into sub-transactions T1..Tn each paired with a compensating
       transaction C1..Cn, where the system "guarantees that either all the transactions in a saga
       are successfully completed or compensating transactions are run to amend a partial
       execution." This is direct, canonical support that a multi-phase job with external effects
       is recoverable after a mid-phase death — that recoverability is exactly what the saga
       construction provides.
    2. AWS Prescriptive Guidance, "Transactional outbox pattern."
       https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html
       — [read as search snippet + landing page] Documents that the dual-write problem (updating
       local state and emitting an external effect as two independently-failing operations) has a
       standard, deployed solution: atomically persist the state change and the intended external
       effect in one local transaction, then let a relay perform the external effect
       asynchronously. Supports recoverability, but note this pattern achieves it by *inverting*
       the ordering the claim assumes: the durable commit precedes the external effect.
    3. Temporal, "Understanding Temporal" and "Workflow Execution overview."
       https://docs.temporal.io/evaluate/understanding-temporal ;
       https://docs.temporal.io/workflow-execution
       — [read as search snippets + landing pages] Durable-execution engines make mid-workflow
       crash recovery a platform guarantee: "If the Worker crashes, the Worker uses the Event
       History to replay the code and recreate the state of the Workflow Execution to what it was
       immediately before the crash. It then resumes progress from the point of failure as if the
       failure never occurred." Activities that already succeeded are skipped on replay. This is
       strong support that the claim is *achievable* for a multi-phase job with external calls —
       under the condition that the job runs on such an engine and its external calls are modelled
       as Activities.
    4. System Overflow, "Implementation Patterns: Transactional Outbox, Idempotency, and Saga
       Pivots." https://www.systemoverflow.com/learn/distributed-primitives/distributed-transactions/implementation-patterns-transactional-outbox-idempotency-and-saga-pivots
       — [read as search snippet] Practitioner synthesis linking the three mechanisms. Notes that
       at-least-once delivery means events "might be retried multiple times," and that "downstream
       systems should be designed to be idempotent, ensuring that processing the same event
       multiple times does not result in different outcomes." Supports the claim conditionally:
       recovery-by-retry is safe precisely when the external effect is idempotent.
    5. Google, "Method: users.messages.modify," Gmail API reference.
       https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/modify
       and "Method: users.threads.modify,"
       https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.threads/modify
       — [read as search snippet only; official docs not fetched in full] The API's mutation is
       expressed as a set operation (`addLabelIds` / `removeLabelIds`), which is the shape that
       makes re-application naturally idempotent. A search snippet asserted that "the batchModify
       endpoint is idempotent: re-applying an existing label is a no-op, not an error." I could
       not verify equivalent explicit wording for the single-message `modify` endpoint, and flag
       this as the weakest link in the citation chain. If the set-semantics reading holds, the
       specific external effect in this claim (Gmail label application) falls into the
       "safe to retry" class, which materially strengthens the claim in this instance.
    6. McCaffrey, C., 2015. "Applying the Saga Pattern." GOTO Chicago 2015.
       https://gotocon.com/dl/goto-chicago-2015/slides/CaitieMcCaffrey_ApplyingTheSagaPattern.pdf
       — [read as search snippet] Restates the saga construction and, importantly for this claim,
       the semantic-undo caveat: a compensating step "semantically undoes" its transaction but
       "does not necessarily return the database to the state that existed when the step began" —
       compensation "will restore the world to a state which is an acceptable approximation."
       Supports recoverability while bounding what "recovered" can mean.

  Strength of support: Moderate

  Summary: There is a large, mature, and well-founded body of work establishing that multi-phase
    jobs with external side effects are recoverable after mid-phase death — the saga pattern with
    compensating transactions (Garcia-Molina & Salem 1987) is the canonical result, and
    durable-execution engines such as Temporal turn it into an off-the-shelf platform guarantee
    via event-history replay with skip-on-replay for completed activities. The particular external
    effect at issue here, Gmail label mutation, is expressed as a set operation and so appears to
    fall in the naturally-idempotent class, which is the property that makes retry-based recovery
    safe. The support is real but conditional in a way worth stating plainly: every source treats
    recoverability as an engineered property that follows from specific mechanisms — compensations,
    idempotency keys, a durable event log, or an outbox — and not as a property a multi-phase job
    has by default. The literature therefore supports "such a job *can be made* recoverable" more
    firmly than it supports "such a job *is* recoverable."

  Caveats: (a) The outbox pattern, the most direct answer to the dual-write problem, achieves
    recoverability by reversing the ordering this claim assumes — durable commit first, external
    effect second. Support for the claim under the stated ordering (external mutation *before*
    internal commit) rests on the saga/compensation branch, which requires that compensating
    actions actually exist and be reachable after the death. (b) Compensation is semantic, not
    literal: McCaffrey's "acceptable approximation" caveat means a recovered state may not equal
    the pre-run state. (c) The Gmail idempotency evidence is the weakest citation here — the
    explicit idempotency statement I found was scoped to `batchModify`, and the individual
    `modify` endpoint's retry semantics were not clearly documented in what I could reach.
    (d) Idempotency of the external effect is necessary but not sufficient: recovery also requires
    that the run know, on restart, which phase it died in. None of the located sources supports
    recoverability for a job that keeps no durable record of its own progress. (e) All sources are
    pattern/mechanism literature; I found no empirical study measuring recovery outcomes for this
    ordering in practice.

  Recommendation: PARTIALLY-SUPPORTED
