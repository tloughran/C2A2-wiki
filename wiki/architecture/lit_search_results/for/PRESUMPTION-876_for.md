SEARCH-FOR-PRESUMPTION-876:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-876
  Queue ref: LIT-QUEUE-2026-08-24-010
  Original statement: "A dated health verdict in an append-only register can be read as current state without a staleness or retraction mechanism."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-876
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b surfaced it during 14a's resolution of a three-way contradiction that dissolved once observation times were applied
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-25. Queries covered (a) temporal validity of assertions —
    bitemporal data modelling, valid time vs. transaction time, as-of queries over immutable
    stores; (b) the knowledge-representation literature on default persistence — event calculus,
    the commonsense law of inertia, non-monotonic formalisation of persistence; (c) alarm
    auto-clear and re-arm semantics — ISA-18.2 alarm state model, latched vs. non-latched alarms,
    OPC UA Alarms & Conditions. Venues: arXiv, Imperial College (Shanahan), TPTP seminar notes,
    O'Reilly (Mueller, *Commonsense Reasoning*), ScienceDirect topic pages, Springer, XTDB and
    JUXT documentation, OPC Foundation reference, ISA/ANSI standard summaries, the Alerta
    open-source ISA-18.2 implementation, USPTO.
    Assessment: **preliminary — broader search recommended.** The web-search budget was exhausted
    before I could run the event-sourcing limb (current state as a fold over an immutable log;
    corrections as compensating events) or the belief-revision limb (AGM, recency priority), both
    of which are likely to add support. Gap: I found no empirical study of whether *readers* in
    practice apply the latest-assertion-wins convention to an undated-status register.

  Supporting evidence found: Yes

  Sources:
    1. Shanahan, M. "The Event Calculus Explained." Imperial College London.
       https://www.doc.ic.ac.uk/~mpsha/ECExplained.pdf
       — Canonical statement of default persistence: the event calculus "embodies a notion of
       default persistence according to which fluents are assumed to persist until an event occurs
       which terminates them." This is the formal warrant for reading a dated verdict as still
       holding: persistence-until-terminated is the standard, formalised default, not an oversight.
       FULL-TEXT available; SNIPPET-ONLY as read here.
    2. Mueller, E. T. *Commonsense Reasoning*, Chapter 5: "The Commonsense Law of Inertia."
       Morgan Kaufmann / O'Reilly. ISBN 9780123693884.
       https://www.oreilly.com/library/view/commonsense-reasoning/9780123693884/xhtml/B978012369388450062X.htm
       — Textbook treatment of the inertia principle: objects stay in the same state unless
       affected by an event (a light stays on until turned off). Establishes that
       "assume-still-true-until-something-changes-it" is the convention readers actually follow.
       SNIPPET-ONLY.
    3. "Commonsense Law of Inertia — an overview." ScienceDirect Topics.
       https://www.sciencedirect.com/topics/computer-science/commonsense-law-of-inertia
       — Traces the axiom of inertia to McCarthy and Hayes ("things normally tend to stay the
       same") and notes that it is formalised via non-monotonic machinery (default logic,
       circumscription), i.e. it is a *defeasible* default that a later assertion can override.
       This supports the supportive reading directly: retraction is expressible as a new dated
       assertion rather than requiring a separate retraction mechanism. SNIPPET-ONLY.
    4. "Event Calculus." TPTP seminar notes, University of Miami.
       https://tptp.cs.miami.edu/Seminars/EventCalculus/EventCalculus.html
       — Confirms the standard formulation: instantaneous events initiate or terminate fluents,
       which "persist by default through inertia until terminated." SNIPPET-ONLY.
    5. "Inferring High-Level Events from Timestamped Data: Complexity and Medical Applications."
       arXiv:2604.21793. https://arxiv.org/pdf/2604.21793 [authors unverified]
       — Recent work applying event-calculus-style inference over timestamped observation streams
       in a health/monitoring setting — the closest located analogue to reading current health
       state off a dated observation record. SNIPPET-ONLY.
    6. "Bitemporality." XTDB v1 documentation.
       https://v1-docs.xtdb.com/concepts/bitemporality/
       — Defines valid time vs. transaction time and the as-of query. Establishes the key
       supportive point: in an immutable, append-only store, "current state" is well defined
       without deletion or retraction, because it is the value at the latest valid-time
       coordinate. Corrections are made by writing new assertions, including retroactively; the
       transaction-time axis is monotone and cannot be rewritten. SNIPPET-ONLY.
    7. JUXT. "The Value of Bitemporality." https://www.juxt.pro/blog/value-of-bitemporality/
       — Practitioner argument that transaction time gives an audit trail and that immutability is
       preserved precisely because nothing is erased; queries recover the state of the world at a
       chosen point without any retraction operation. Supports append-only + dates as *sufficient*
       for current-state reads. SNIPPET-ONLY.
    8. "Bitemporal Property Graphs: Dealing with Both Valid and Transaction Time." Springer
       (chapter, DOI 10.1007/978-3-032-05281-0_15).
       https://link.springer.com/chapter/10.1007/978-3-032-05281-0_15 [authors and year unverified]
       — Extends the two-axis temporal model to graph-structured registers, i.e. the pattern
       generalises beyond relational stores. ABSTRACT-ONLY.
    9. ANSI/ISA-18.2 "Management of Alarm Systems for the Process Industries" (2009; rev. 2016),
       as summarised in: ISA São Paulo symposium slides,
       https://isasp.org.br/wp-content/uploads/2020/01/ISA-18_2-III-Simp%C3%B3sio-ISA-S%C3%A3o-Paulo-Sabesp-Nov2016.pdf ;
       "MES Alarm Management: ISA-18.2, Smart Alerting & Escalation," Symestic; and the reference
       implementation at https://github.com/alerta/alerta/blob/master/alerta/models/alarms/isa_18_2.py
       — The standard defines a ten-state alarm lifecycle with deterministic transitions, in which
       the *default* (non-latched) behaviour is that an alarm returns to normal when the
       underlying condition clears — automatically, without operator action. Supports the claim
       that auto-clear semantics are the well-specified norm and that a standing alarm record does
       not by itself require a retraction entry. SNIPPET-ONLY.
   10. OPC Foundation. OPC Unified Architecture Part 9: Alarms & Conditions, §4.8 "Alarms."
       https://reference.opcfoundation.org/specs/OPC-10000-9/4.8
       — Specifies LatchedState as an *opt-in* addition for alarms that require explicit reset
       after physical inspection. The fact that latching must be added supports the converse: in
       the base specification an alarm's currency tracks the underlying condition without a
       separate clear-mechanism. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: The knowledge-representation literature supplies a direct and long-standing warrant for
    reading a dated assertion as describing current state: the commonsense law of inertia, traced
    to McCarthy and Hayes and formalised in the event calculus, holds that fluents persist by
    default until an event terminates them. On this account, treating a dated health verdict as
    still in force is not a lapse but the application of the standard default, and because that
    default is formalised non-monotonically it is defeasible — a later dated assertion simply
    overrides the earlier one, so retraction needs no dedicated mechanism. The bitemporal data
    literature makes the same point operationally: in an append-only, immutable register, "current
    state" is fully determined as the value at the latest valid-time coordinate, corrections are
    written as new assertions rather than by deletion, and the append-only discipline is what
    preserves the audit trail. The alarm-management standards add that auto-clear is the specified
    default: under ISA-18.2 and OPC UA Alarms & Conditions, an alarm returns to normal when its
    condition clears unless latching is explicitly opted into. Taken together, these support the
    presumption's core: a dated verdict in an append-only register is readable as current state
    under conventions that are formalised, standardised, and widely followed.

  Caveats: The support is strong for the *formal readability* of such a register and much weaker
    for the *practical* claim. (1) Every supportive source presupposes that the reader applies the
    latest-assertion-wins or persistence-until-terminated rule and that observation timestamps are
    present, legible and comparable; the 14a episode that generated this item is itself an
    instance where the contradiction only dissolved once observation times were *applied*, which
    means the convention had to be invoked deliberately. (2) The bitemporal literature's guarantee
    holds because the store distinguishes valid time from transaction time; a register carrying
    only one date does not support as-of queries in the same way, and no located source addresses
    the single-timestamp case. (3) Inertia is a *default*, and defaults are exactly what fail when
    the terminating event is unobserved — event calculus assumes termination events are recorded,
    which is precisely what an append-only register with no re-check will not contain. (4) The
    alarm evidence cuts both ways: auto-clear is the default, but it is implemented by a monitoring
    system that continuously re-evaluates the condition, which is arguably itself the staleness
    mechanism the presumption dispenses with; and the standards define latching precisely because
    some conditions must not be assumed cleared. (5) The verdicts here are agent-authored health
    assessments, not sensor readings; no source located addresses the temporal validity of
    *judgements* as opposed to *measurements*.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that persistence-until-terminated is the formalised, standard default
    for reading dated assertions; (ii) that an append-only, immutable, dated register fully
    determines current state without deletion or an explicit retraction operation, corrections
    being expressible as further assertions; (iii) that auto-clear rather than latching is the
    specified default in mainstream alarm standards.
    Unaddressed sub-claim: **whether readers of an append-only register carrying agent-authored,
    single-timestamped health verdicts actually apply the latest-assertion-wins / default-
    persistence convention in practice, absent any explicit staleness marking — and what the
    contradiction rate is when they do not.** The formal literature establishes that the register
    is *readable* as current state; I found no empirical or human-factors study of whether it *is*
    so read. The single-timestamp case (no valid-time/transaction-time separation) and the
    temporal validity of judgements rather than measurements are both, so far as this search found,
    unaddressed.
