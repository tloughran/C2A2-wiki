SEARCH-AGAINST-PRESUMPTION-876 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-876
  Original statement (per MONITOR-553): A dated health verdict in an append-only register can be read as
    current state without a staleness or retraction mechanism.
  Owed this cycle: (i) SRE alarm lifecycle (auto-clear, re-arm, flapping, heartbeat/liveness timeout);
    (ii) bitemporal / temporal-database literature (valid time vs transaction time). ARBITRATION OWED:
    cycle-0 15a read the bitemporal literature as SUPPORTIVE; cycle-0 15b PREDICTED it would be
    decisive AGAINST without reading it. I have read a primary source and report what it says,
    including where it favours 15a.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for* file,
    `lit_search_returns.md`, or today's 15a output. Cycle-0 15a's position is known to me only via
    MONITOR-553 ("SUPPORTED, Moderate ... three self-named disqualifying conditions: single-timestamp
    registers are unaddressed; inertia fails when the terminating event is unobserved; agent-authored
    judgements are not sensor readings").

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-876
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced during 14a's resolution of a three-way contradiction that dissolved once observation
        times were applied.
      15b (2026-08-25): CHALLENGED (Moderate); NO targeted query (budget exhausted); one machine-checked
        "stale-generation" source (arXiv:2606.17182). Predicted bitemporal literature decisive against.
      15c: DISPOSITION-813 → MONITOR-553 (HIGH; Critical SYSTEMIC-RISK-FLAG 2 member).
      15d (2026-09-13): Re-triggered; owed = SRE alarm lifecycle + bitemporal; arbitrate 15a/15b.
      15b (re-trigger cycle 1, 2026-10-08): 2 searches (bitemporal; heartbeat/dead-man's-switch); 2 fetch
        attempts — Jensen & Snodgrass TKDE 1999 PDF returned EMPTY (no text extracted); Torp, Jensen &
        Snodgrass "Effective Timestamping in Databases" fetched in full text.
    Current status: CHALLENGED

  EVIDENCE GRADE: one primary bitemporal source read at full text (Torp/Jensen/Snodgrass); SQL:2011 and
    practitioner-glossary material at search-result level; SRE alarm-lifecycle material at search-result
    level and TRADE-ONLY (no Google SRE text was returned by the search). Moderate scope.

  Challenging evidence found: Yes (retraction limb, decisively); No (staleness-timer limb, taken alone)

  Sources:
    1. Torp, K., Jensen, C. S. & Snodgrass, R. T. "Effective Timestamping in Databases." VLDB Journal
       8(3–4), 2000 (reprinted as ch. 40 of Jensen's doctoral thesis, homes.cs.aau.dk/~csj/Thesis/pdf/
       chapter40.pdf). [fetched — full text; venue/year from background knowledge] What it actually says:
       (a) Transaction time = "when the facts are current in the database"; valid time = "when the facts
           are true in the modeled reality." These are distinct, independently recorded axes.
       (b) Current-state reading rests on OPEN-ENDED timestamps: "nobind now" and "until changed", which
           the authors gloss as "until we learn more." There is NO expiry/TTL in the model: a fact stays
           current until something supersedes it. → THIS FAVOURS 15a on the narrow question "is a
           staleness timer required?" The bitemporal model does not require one.
       (c) Supersession is performed by an explicit retraction act: a deletion "is effected by updating
           the T-Stop attribute ... indicating that our old belief no longer holds, and inserting a tuple
           to record our new belief." The worked example: Joe's department fact "was believed correct
           until January 20, when it was discovered ... the initial information was logically deleted, by
           placing 1998-01-20 in the T-Stop attribute." → THIS IS DECISIVE AGAINST on the retraction
           question. In the bitemporal model "current" is DEFINED as "transaction-time interval still
           open"; an append-only store in which superseding entries do not close prior entries has no
           well-defined current state — several contradictory entries would all be "current."
       (d) Facts carry BOTH timestamps. A register with a single date per verdict conflates "when the
           verdict was true of the system" with "when the verdict was recorded" — exactly 15a's own first
           disqualifying condition.
    2. SQL:2011 system-versioned tables (as summarised in search results; standard text not read):
       "an update or delete closes the current row and keeps it as a historical row"; users cannot set
       transaction time. [search-result] Bearing: the industrial standard implements (c) — retraction by
       closing the prior row is built into the write path, not left to the reader.
    3. Heartbeat / dead-man's-switch practice (oneuptime 2026; incident.io heartbeat docs; dev.to
       "A dead man's switch for your monitoring stack"). [search-result — trade sources only] Threshold
       alerts "don't fire when a series vanishes": an absent series "returns empty", and "most alerting
       systems treat empty query results as 'no data' and do nothing"; the remedy is a periodic liveness
       signal whose ABSENCE past a grace period fires. Bearing: this is the operational answer to the
       case the bitemporal model assumes away — "until changed" is sound only if changes are reported.
       When the event that would end a health verdict's validity is not itself written to the register
       (15a's second disqualifying condition), "until we learn more" degrades to "forever." Auto-clear,
       re-arm and flapping semantics were NOT reached by any returned source; I do not cite them.

  ARBITRATION (per PREMISE-161 — recorded as a finding, not averaged):
    15a and cycle-0 15b were answering different limbs of a conjunctive statement.
    - On "no STALENESS mechanism needed": the bitemporal literature sides with 15a. Persistence-until-
      changed with no TTL is the model's default semantics.
    - On "no RETRACTION mechanism needed": the bitemporal literature sides with cycle-0 15b, decisively.
      Retraction (closing transaction time) is constitutive of what "current" means in the model.
    - The persistence default is itself conditional on a closed-world update discipline (every change is
      written). That condition fails for health verdicts whose invalidating event is unobserved, which is
      where the SRE heartbeat literature — not the database literature — takes over and requires a
      liveness/staleness mechanism after all.
    Net: the presumption as stated ("without a staleness OR retraction mechanism") is contradicted. 15a's
    reading is correct about one limb and its own disqualifying conditions are exactly the conditions
    under which the supportive reading fails; cycle-0 15b's prediction was right in outcome but it
    over-claimed in scope (the bitemporal literature does NOT demand staleness timers).

  Strength of challenge: Strong on the retraction limb (primary source, full text); Moderate on the
    staleness limb (trade sources only; the requirement arises from the unobserved-change condition, not
    from the database literature itself). Overall: Moderate-to-Strong.

  Summary: Read at full text, the bitemporal literature does not support reading a dated verdict from an
    append-only register as current. It supports a weaker thing — that a recorded fact may be treated as
    current without a timeout — and only under two conditions the register does not meet: the store
    records separate valid and transaction times, and every superseding write closes the prior entry's
    transaction-time interval. Remove the retraction act and "current state" has no definition in the
    model. Where the event that ends a verdict's validity is not written to the store, operations
    practice adds the missing mechanism from the other side: a heartbeat whose absence fires.

  Specific risks: (i) multiple dated verdicts on the same subject coexist with no rule for which is
    current — the three-way contradiction that originally surfaced this item is the predicted symptom;
    (ii) a verdict that was true when written is read as true now because nothing writes its end;
    (iii) single-date entries make "true as of" and "written on" indistinguishable, so even a careful
    reader cannot apply bitemporal reasoning after the fact.

  Mitigations available: add a supersedes:/superseded-by: field (the append-only analogue of T-Stop) so
    that every new verdict closes its predecessor; record observed-at separately from written-at;
    for verdicts whose invalidating event is unobserved, attach a max-age after which the verdict reads
    as UNKNOWN rather than as its last value (heartbeat semantics); measure the register's stale-exposure
    rate (cycle-0 15b's test).

  Recommendation: CHALLENGED — the 15a/15b disagreement is resolved as a limb split, and the conjunction
    as stated fails on the retraction limb at primary-source level.

STEELMAN:
  Item: PRESUMPTION-876
  Strongest counterargument: The best-developed theory of reading current state from an append-only
    history — bitemporal databases — is not a counterexample to the need for retraction; it is a
    formalisation of it. "Current" in that theory means "the transaction-time interval has not been
    closed," and closing it is the retraction. An append-only register with no supersession act has no
    current state in that theory, only a pile of beliefs each true as of its own date. The theory's
    tolerance for open-ended validity ("until we learn more") is purchased by the assumption that the
    system will be told when to learn more; health verdicts are exactly the facts whose expiry nobody
    reports, which is why operations practice inverts the default and treats a missing heartbeat as an
    alarm.
  What would need to be true for C2A2 to be safe: each verdict is the only live verdict on its subject
    (later verdicts explicitly supersede earlier ones); verdict validity ends only by events that are
    themselves written to the register; readers always see the observed-at date.
  How to test: sample N subjects with ≥2 verdicts in the register; count how often a reader taking the
    latest-dated entry would have been wrong about the state on the read date; separately count
    subjects whose only verdict is older than the period over which the subject is known to change.
