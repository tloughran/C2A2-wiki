SEARCH-FOR-PRESUMPTION-676:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-676
  Original statement: That an interrupted run leaves no partial state — an
    external side effect (`unlabel_message` on a Gmail decision email) was
    applied before the run died, with no corresponding archive entry, so a
    future run will treat that decision as handled.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-676
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from one tool call in an interrupted transcript,
        cross-checked against `review/archive/`
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (support exists only inside a scope this case
    does not have)

  Sources:
    1. Gray, J. & Reuter, A., 1993. Transaction Processing: Concepts and
       Techniques. Morgan Kaufmann. — The theoretical grounding, and the only
       route to support. Under ACID atomicity an aborted transaction leaves no
       partial state; this is a real and strong guarantee. It is scoped to
       operations inside a single resource manager, or across several that are
       enrolled in one commit protocol. A tool call into a third-party mailbox
       is in neither category.
    2. Garcia-Molina, H. & Salem, K., 1987. "Sagas." Proceedings of the 1987
       ACM SIGMOD International Conference on Management of Data: 249-259. —
       The counter-case, and the reason the field has a name for this. Sagas
       exist because long-lived multi-step work cannot hold atomicity across its
       steps; the guarantee offered instead is that either all steps complete or
       compensating transactions run to amend a partial execution. Partial
       execution is assumed to occur; the compensating action is what makes it
       tolerable. Note the paper's own qualifier: compensation restores an
       acceptable approximation of the prior state, semantically, not the exact
       prior state.
    3. Helland, P., 2007. "Life beyond Distributed Transactions: an Apostate's
       Opinion." CIDR 2007. — States the applicable rule for this case
       explicitly. Beyond a single scale-unit, distributed transactions are not
       available, and correctness must instead be built from entities that are
       atomically updatable individually but never atomically updatable across
       each other, plus messages designed to be idempotent under retry. The
       mailbox and the archive are two entities; there is no atomic update
       across them.
    4. The dual-write problem and the transactional outbox pattern
       (practitioner literature, Confluent / Debezium lineage, 2019-2026). —
       The applied statement of the same result: writing to two systems in one
       logical operation with no atomic guarantee across them leaves them
       inconsistent whenever one write succeeds and the other does not. The
       reported case is a textbook instance — the external write (unlabel)
       succeeded, the local write (archive entry) did not. The outbox pattern is
       the standard remedy and works by collapsing the two writes into one
       transaction plus an idempotent replay.
    5. "SagaLLM: Context Management, Validation, and Transaction Guarantees for
       Multi-Agent LLM Planning," 2025. arXiv:2503.11951. — Domain-transfer
       evidence: the saga model has already been adapted specifically to
       multi-agent LLM planning, with compensating rollback and independent
       validation, on the stated grounds that agent steps commit externally and
       cannot be undone by the agent that made them. This is the closest
       published analogue to C2A2's situation and it treats orphaned external
       side effects as the expected failure, not the exception.
    6. Durable-execution literature (Temporal, Restate, Hatchet documentation
       and adjacent practitioner writing, 2023-2026). — Consistent operational
       finding: exactly-once execution of an external effect is not achievable;
       the achievable property is that the effect is idempotent or paired with a
       compensating action, and that completed steps are replayed from a
       recorded result rather than re-executed. The correctness argument is
       always about recovery, never about the absence of partial state.

  Strength of support: Weak

  Summary: No support was found for the claim as it applies to this case. The
    supportive theory is genuine — atomicity does guarantee that an aborted
    unit leaves no partial state — but it holds only within a single resource
    manager or a set enrolled in one commit protocol, and a tool call into an
    external mailbox is outside any transaction the run controls. Every body of
    work that addresses precisely this configuration (sagas, Helland's entities
    and activities, the dual-write problem, durable execution, and the recent
    saga-for-LLM-agents work) is constructed on the opposite premise: that a
    multi-step run interrupted mid-flight leaves committed external effects
    behind, and that the only available correctness property is compensation or
    idempotent replay, not absence. The specific asymmetry reported — external
    write succeeded, local record absent — is the canonical dual-write failure,
    and the direction of the asymmetry is the dangerous one, because the
    surviving artifact is the one that a later run will read as evidence of
    completion.

  Caveats: The distributed-systems literature assumes the compensating action is
    definable, which is not always true for an agent's external effects — a
    re-label restores a mailbox flag but does not restore whatever downstream
    reading occurred while the flag was absent, so compensation here is
    semantic approximation in Garcia-Molina & Salem's sense rather than undo.
    The evidence base for the agent-specific case is thin and recent (one 2025
    preprint plus practitioner sources); the classical citations are strong but
    are transferred by analogy. The theoretical support would become real
    support if the local archive write and the external label change were made a
    single recoverable unit — write the intent locally first, then apply the
    external effect idempotently on replay. That is the outbox pattern and is
    the standard remedy the literature points to.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: sagas and compensating
    transactions; long-lived transactions and ACID scope limits; life beyond
    distributed transactions, entities and activities, idempotence; the dual-
    write problem and the transactional outbox; orphaned side effects and
    partial execution in workflow engines; durable execution and replay; and
    transaction guarantees for interrupted LLM agent runs.
