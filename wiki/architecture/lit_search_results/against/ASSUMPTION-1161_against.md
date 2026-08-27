SEARCH-AGAINST-ASSUMPTION-1161:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1161
  Original statement: That a multi-phase job which mutates external state (Gmail labels) before
    committing internal state (proposal moves) is recoverable after a mid-phase death.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1161
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Traced the daily run's termination point and measured the resulting five-day
        review-page gap and queue growth.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive on the distributed-transactions side, adequate on the
    Gmail-specific side. Queries: "saga pattern compensating transactions cannot achieve
    atomicity external API side effects not undoable"; "dual write problem external system
    mutation before database commit outbox pattern non-idempotent"; "exactly-once delivery
    impossible two generals at-least-once effectively-once durable execution"; "Gmail API
    modify labels idempotency retry at-least-once partial failure batch". Venues: Microsoft
    Azure Architecture Center, microservices.io, Confluent Developer, Google Workspace API
    reference, practitioner engineering blogs. Date range 2015–2026.
    Gaps: no peer-reviewed study of mail-label mutation as a saga participant; Gmail's own
    documentation does not state an idempotency contract in the terms this claim needs, so
    the strongest Gmail-specific evidence is secondary (vendor guides), which I have marked
    as such. Garcia-Molina & Salem's original Sagas paper was not retrieved in search and is
    therefore not cited.

  Challenging evidence found: Yes

  Sources:
    1. Microsoft, "Compensating Transaction pattern," Azure Architecture Center.
       https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction
       — States plainly that a compensating transaction is *not* a rollback: it is a new
       forward operation that is a logical inverse, it can itself fail, and the intermediate
       inconsistent state was visible to other readers in the interim. The claim's word
       "recoverable" imports rollback semantics the pattern does not provide. FULL-TEXT.
    2. Microsoft, "Saga design pattern," Azure Architecture Center.
       https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
       — Sagas explicitly give up isolation; intermediate states are observable and can
       produce dirty reads. In this job's case, the intermediate state is *user-visible in
       the mailbox*, which is the least reversible reader of all. FULL-TEXT.
    3. Richardson, "Pattern: Saga," microservices.io.
       https://microservices.io/patterns/data/saga.html
       — Canonical statement of the pattern and its lack of ACID guarantees; compensations
       must be designed per step and are the developer's obligation, not a property of the
       structure. FULL-TEXT.
    4. Practitioner synthesis of the compensation limit — effects that cannot be undone once
       externalized (emails, payments, deletions) fall outside the reach of compensation;
       "a saga can refund a charge but cannot un-send an email." Recovered as a search
       snippet across the saga-pattern result set (see e.g.
       https://www.conduktor.io/glossary/saga-pattern-for-distributed-transactions).
       SNIPPET-ONLY. — Directly relevant: a Gmail label change is an externalized, user-
       observable effect, and any human who acted on the relabelled mail during the gap
       cannot be compensated.
    5. Janssen, "Dual Writes — The Unknown Cause of Data Inconsistencies."
       https://thorben-janssen.com/dual-writes/ and Confluent Developer, "The Dual Write
       Problem," https://developer.confluent.io/courses/microservices/the-dual-write-problem/
       — The exact shape of this job: two independent systems, no shared transaction
       boundary, therefore *no safe ordering of the two writes*. Doing the external write
       first does not make the pair recoverable; it selects which inconsistency you get.
       FULL-TEXT.
    6. Treat, "You Cannot Have Exactly-Once Delivery." https://bravenewgeek.com/you-cannot-have-exactly-once-delivery/
       and Kleanthous, "The impossibility of exactly-once delivery."
       https://blog.bulloak.io/post/20200917-the-impossibility-of-exactly-once/
       — Two Generals: no protocol over an unreliable channel guarantees agreement, because
       the acknowledgement can be lost. On resume, the job cannot in general know whether its
       last Gmail call landed; "effectively once" is only reachable by adding idempotent
       application-level handling, which is an extra requirement the assumption does not
       state. FULL-TEXT.
    7. Google, "Method: users.messages.batchModify," Gmail API reference.
       https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/batchModify
       — Provides the batch mutation surface but no transactional or partial-failure
       semantics for the caller to rely on across a process death. FULL-TEXT (reference).
    8. Nylas, "Batch Modify Gmail Labels (API + CLI)."
       https://cli.nylas.com/guides/gmail-api-batch-modify-labels
       — Secondary claim that re-applying an existing label is a no-op rather than an error,
       i.e. label-add is idempotent under retry. SNIPPET-ONLY; this is a vendor guide, not
       Google's own contract, and should be verified before being relied on. Note this
       supports *partial* recoverability of the add-label step only; it says nothing about
       remove-label ordering, about labels the run intended but had not yet applied, or about
       reconstructing which messages a dead run had already reached.

  Strength of challenge: Strong

  Summary: The literature treats this exact ordering — mutate a foreign system, then commit
  locally — as the textbook dual-write problem, and the consensus finding is that there is no
  ordering of two independent writes that is safe without an additional mechanism. Sagas and
  compensating transactions are the standard response, but every authoritative description of
  them stresses that they do not restore atomicity: compensation is a new forward action that
  can itself fail, isolation is deliberately abandoned, and effects that have already been
  externalized to a user are outside the reach of compensation altogether. Gmail labels are
  precisely such an externalized effect — a human may have read, filtered, or acted on the
  relabelled mail during the gap, and that cannot be undone by re-labelling. On top of this,
  the Two Generals result means a resuming run cannot in general determine whether its final
  API call took effect, so recovery requires idempotency keys or a durable intent log written
  *before* the external call — neither of which is implied by the claim. The observed
  five-day review-page gap with queue growth is the predicted signature of an uncompensated
  partial saga, not an anomaly.

  Specific risks: If this claim is false, the failure is not a lost run but a divergence:
  Gmail state advances while C2A2's internal state does not, and the two never re-converge on
  their own. Concretely — messages labelled as processed that the proposal store still
  considers unprocessed (silent drop, invisible forever, because the label now hides them
  from the next run's query), or messages relabelled and then re-selected on the next run
  (double processing, duplicated proposals). Because the divergence is in a system C2A2 does
  not own, there is no internal audit that will surface it; the queue growth and page gap are
  downstream symptoms observed days later. Blind retry of the whole job after death makes it
  worse, not better, if any step is non-idempotent.

  Mitigations available:
    - Transactional outbox: write the *intent* to mutate Gmail into the same local
      transaction as the internal state change, then have a separate relay perform the
      external call and mark it done; this converts an unsafe dual write into one durable
      write plus a retryable delivery (Janssen, dual writes; Confluent, dual write problem).
    - Reverse the order: commit the durable internal record first, mutate external state
      second, and make the external mutation idempotent and replayable from the durable
      record. This makes the worst case "external state lags" rather than "external state
      leads and internal state has no memory of it."
    - Idempotency keys plus at-least-once delivery to obtain effectively-once processing;
      accept that exactly-once delivery is unobtainable (Treat; Kleanthous).
    - Per-message checkpointing rather than per-phase, so a mid-phase death loses one item,
      not the phase boundary.
    - Explicit compensations designed per step, with the acknowledgement that compensation
      can fail and needs its own retry and alarm (Azure compensating transaction pattern).
    - A reconciliation pass that periodically diffs Gmail label state against internal
      proposal state and reports drift — the only mechanism that detects divergence which has
      already happened.

  STEELMAN:
    Item: ASSUMPTION-1161
    Strongest counterargument: "Recoverable" is doing unearned work here. Recovery from a
    mid-phase death requires three things the design does not obviously have: a durable record
    of what the run intended before it acted, a way to determine on resume what actually
    landed on the far side, and an idempotent replay path. The dual-write literature's central
    result is that no ordering of the two writes supplies any of these — ordering only chooses
    which side ends up ahead. Compensation cannot help either, because Gmail labels are
    externalized to a human reader, and the saga literature explicitly excludes externalized
    effects from the reach of compensation. And the Two Generals result forecloses the
    remaining hope that the resuming run could simply ask whether the last call succeeded.
    What would need to be true for C2A2 to be safe: (a) every external mutation is idempotent
    under replay and this is verified against Google's documented behaviour, not a third-party
    guide; (b) a durable, crash-atomic record of intent exists *before* the external call, and
    resume reads from it; (c) checkpoint granularity is per-item, so the blast radius of a
    death is one message; (d) the label change is not itself the thing that makes a message
    invisible to the next run's selection query, or if it is, selection is driven by the
    internal record instead; (e) a scheduled reconciliation compares the two stores and alarms
    on drift, so an unrecovered divergence is detected rather than accumulating.
    How to test: Inject a kill between the Gmail mutation and the internal commit — SIGKILL
    the process at that exact point — then restart normally and assert full convergence:
    every mutated message has a corresponding internal record, no message is processed twice,
    and the review page has no gap. Repeat with the kill placed at every phase boundary and
    at a random point inside the loop. Separately, run the same message through the pipeline
    twice deliberately and check the resulting label and proposal state for duplication.

  Recommendation: CHALLENGED
