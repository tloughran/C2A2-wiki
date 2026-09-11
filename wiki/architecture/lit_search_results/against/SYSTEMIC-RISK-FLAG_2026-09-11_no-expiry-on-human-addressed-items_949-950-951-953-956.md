SYSTEMIC-RISK-FLAG:
  Date: 2026-09-11
  Filed by: Agent 15b (Literature Search AGAINST), run on the 2026-09-10 evening 14b PRESUMPTION intake
  Affected items: PRESUMPTION-949, PRESUMPTION-950, PRESUMPTION-951, PRESUMPTION-953, PRESUMPTION-956
    — five of ten. PRESUMPTION-955 is adjacent and is deliberately NOT included; see the exclusion note.

  Common vulnerability:
    **Every item the estate addresses to a human is created without an expiry, and the estate has no
    construction for what the passage of time means. Consequently an unanswered item, an unrouted item, an
    unrun survey and an unread report are all in the same state — "open" — and that state has no age-based
    semantics, no default, and no terminal condition. The estate cannot distinguish a queue from a
    dead-letter office, and it cannot distinguish either from a decision.**

    Item by item, the same absence:
      949 — a flag names its own falsification counter and its own remedy, and stops. The counter has no
            date and no actor, so nothing happens when it is reached. ASSUMPTION-1316's counter is at two
            and was not dispositioned.
      950 — a survey day is skipped and no record is written. A skipped day and an empty day are
            indistinguishable in the archive, so the skip has no age and cannot expire into a finding.
      951 — a defect logged "needs a human" is 31 days old and has misfired once. There is no threshold
            past which it is reclassified as anything.
      953 — six requests addressed to a person on one day, none with a date by which non-response would
            mean something. `decisions.md` has not moved in 14 days; nine rulings are named and owed.
      956 — a finding outside an agent's write scope is written down and released. There is no
            acknowledgement condition and no age at which the release is re-examined.

    In all five, the terminal act creates an object with no clock. The estate therefore has no answer to
    "what does thirty days of silence mean?", and — because no object carries a deadline — it cannot even
    pose the question as a query.

  Literature basis:
    - **Administrative-silence doctrine** (deemed refusal / deemed approval; France from the Law of 17
      July 1889, followed by Italy, Spain, Germany; the modern EU tacit-authorisation model with a common
      three-month default). — SECONDARY (search summaries; no statute or primary text retrieved) — This is
      the load-bearing source and it is a whole doctrine rather than a finding. Every legal system that has
      had to formalise the meaning of official silence has refused to leave it unconstrued, and the two
      available constructions (silence = refusal, silence = approval) differ in direction but agree
      completely on the essential: **a stated deadline, after which silence has a determinate legal
      effect.** Indefinite pendency is the one option the doctrine treats as intolerable, because it leaves
      the subject with no remedy — which is precisely the position of the four registers in
      PRESUMPTION-951.
    - **Dead-letter-queue design practice** (AWS SQS DLQ documentation; Elastic Logstash DLQ
      documentation; practitioner guidance). — SECONDARY — The universally named failure mode is unbounded
      DLQ growth; the universally named remedy is a retention/max-age policy plus alerting on queue depth
      AND age, with stated reclassification bands (commonly 30–90 days) at which a never-processed record
      is summarised and archived. The practitioner formulation is the sharpest statement of this flag's
      whole content: a message that ages out unexamined is one you decided to lose without deciding to
      lose it.
    - **AHRQ TeamSTEPPS 3.0, "Tool: Handoff"** (content reviewed May 2023). — **VERIFIED** (retrieved and
      read in full, 2026-09-11) — "You are accountable until the other party is aware of the transfer of
      responsibility"; "Until it is acknowledged that the handoff is understood and accepted, you cannot
      relinquish your responsibility. This step is particularly crucial for handoffs that occur
      electronically"; and you "cannot assume that the person obtaining responsibility will read or
      understand the communication without confirmation." The estate's handoffs are all electronic, none
      is acknowledged, and none carries a condition under which the raiser reacquires it.
    - **Cyentia Institute / Kenna Security, P2P Vol. 3** (2019). — VERIFIED at the authoring institute's
      own summary page (report itself gated) — "The typical organization only fixes about 10% of its
      vulnerabilities in any given month. And that's consistent regardless of how many assets are in the
      environment." The capacity-invariance clause is the part that makes this a systemic rather than a
      local finding: the fraction of correctly-surfaced items handled DECLINES as the surfacing rate rises,
      so an estate that gets better at finding things gets worse at closing them, with no signal.
    - **Delay-time inspection modelling** (Christer; Wang, RESS 2012; the departures-from-schedule line). —
      SECONDARY (ScienceDirect full texts PAYWALLED) — prices the cost of a skipped inspection interval as
      increased undetected-defect exposure, and explicitly models schedule departures caused by production
      being prioritised over maintenance. Supplies 950's missing ledger.
    - **EEMUA 191 / ISA-18.2 shelving semantics.** — SECONDARY — the industrial answer to deliberate
      suppression is a recorded, time-bounded, SELF-CLEARING object (EEMUA 191 default shelf life: 4
      hours). Every suppression in this estate is indefinite and none self-clears.
    - In-register, and these are the governing statements: **PREMISE-133** (abstention is a decision and
      requires a written discharge rule); **PREMISE-154** (scope-extends 133 to the deferral/queue cohort
      in TRIGGER-BOUND form — name what discharges it, who adjudicates, and a deadline); **PREMISE-147**
      (the statistic that carries the information is AGE, not count); **PREMISE-102** (repeated
      non-processing in a zero-throughput channel converts a signal into a standing policy of
      non-coverage); **PREMISE-108** (transmission is not delivery; the flagged-and-unheld state is worse
      than not flagging); **PREMISE-183** (a filed flag is a live obligation with a closure test).
      PREMISE-154 exists *specifically* because PREMISE-133 declined to license this cohort. The estate has
      already ruled on this question, in trigger-bound form, and the ruling is not implemented.

  Risk level: **Critical**

    Justification for Critical rather than High. Three properties, and it is their conjunction rather than
    any one of them:
      (1) **It is the common dependency of the batch's two highest-risk items.** PRESUMPTION-953 (Critical)
          and PRESUMPTION-956 (High) fail together and fail through this mechanism: 956 makes one human the
          sole receiver of every scope-blocked finding, and 953 asks whether that receiver receives in
          time. Neither question is answerable without an age on the objects, and no object has one.
      (2) **The defect is monotonic and self-concealing.** Items enter the open state and nothing removes
          them; the ledger of open items therefore grows without bound while reporting no change in status,
          and under PREMISE-108 the record simultaneously shows each item as discharged. The estate's
          belief about how much is handled diverges from reality in one direction only, at a rate that
          increases as the agents get better at surfacing findings. Cyentia's capacity-invariance result is
          the measured form of this.
      (3) **It has already produced a live failure, twice.** The duplicate-anchor defect misfired on
          2026-09-10 after 30 days in the undated state. PROP-2026-08-14-033 is held against a retrieval
          target retired on 09-08 and will misfire on every future ingest. These are not prospective risks.

  Recommendation (15b does not make design decisions; this is for 14a/14b/12):
    One change would close all five items, and it is a field, not a subsystem.
    1. **Every item addressed to a human acquires three fields at creation: an addressee, a date, and a
       default.** The default states what the item becomes if the date passes with no ruling. This is
       PREMISE-154's trigger-bound form, already ACTIVE and already scoped to this cohort, implemented as
       a template rather than as an aspiration. It costs three fields and one convention.
    2. **Choose the defaults deliberately, and do not use one default for everything.** The
       administrative-silence doctrine's two models map cleanly onto a discriminator the estate already
       has in PREMISE-176 (for an irreversible operation, reversibility is the control, not review):
         - *Irreversible or scope-widening* items default to DECLINED and escalate louder. Nothing is
           granted by the passage of time; this preserves PREMISE-196's capability control intact.
         - *Reversible repairs under version control* — the duplicate-anchor fix is one — may default to
           AUTHORISED at expiry, with a tombstone. This is the deemed-approval model and it is the only
           proposal here that actually repairs the four corrupted registers rather than re-labelling them.
       I flag honestly that limb (b) is a design decision with a real objection (a capability obtained by
       waiting), and that the literature settles *that a construction is needed*, not *which one*.
    3. **Report age, not count, everywhere.** PREMISE-147 and DLQ practice converge on the same statistic.
       Applied to 950 this means the oldest un-surveyed tradition-day; to 951, the age distribution of
       human-blocked defects; to 953, the latency distribution of human-addressed requests. All three are
       one pass over existing files and none requires a design ruling first.
    4. **Write the negative record** (950's specific fix, and the precondition for the rest). An object
       with no record has no age. One dated line per hunt-day, run or skipped.
    5. **Add an acknowledgement condition to scope-blocked findings** (956's fix, and it needs no new
       capability): the finding stays attributed to the raiser until a named receiver acknowledges. AHRQ's
       rule, implemented as a status value.
    6. **Honour stated counters.** ASSUMPTION-1316's counter is at two and this is the third consecutive
       cycle in which a flag from this lane names a defect in how the estate observes itself. A counter
       that is stated and not honoured is worse than no counter, because it manufactures the appearance of
       a trip point.

  Relationship to the two flags already filed in this directory — RECONCILE, DO NOT STACK:
    - **2026-09-10, `no-second-look`** named *a positive act being converted into a permanent state*: the
      control's lifetime is one instant, and nothing re-reads it. That flag's remedy is a SECOND READER.
      This flag names a different absence: not that nobody re-reads the object, but that **the object has
      no clock, so there is nothing for a re-reader to act on.** An expiry and a re-read are complements —
      the expiry says when to look and what the silence meant; the re-read says who looks. If one
      mechanism is built, it should carry both, and the expectation register proposed on 2026-09-09 is
      still the natural host for all three.
    - **2026-09-11, `premise-propagation-not-routing`** (filed earlier today by this lane on the
      ASSUMPTION side) named *the register's premises not reaching the runs that need them*. That is the
      cause of why PREMISE-154 is ACTIVE and unimplemented. This flag is downstream of it: propagation
      explains why the rule is not applied; this flag explains what the unapplied rule costs. An addendum
      recording the presumption-side replication has been appended to that file rather than duplicated
      here.
    None of the three is a restatement of another, and the distinction determines which remedy is built.

  Exclusion note, and it is part of the flag: **PRESUMPTION-955 is deliberately not included**, despite
    obvious surface similarity (a stale artefact read as current is an item with no clock). Its defect is
    different in kind: 955's problem is that the *status vocabulary* cannot express a third state, and its
    remedy is a ternary token plus a consumer-side enforcement point — an encoding fix, not a lifecycle
    fix. Folding it in would make this flag a general complaint about time in the estate rather than a
    claim about a specific missing field, and a flag that expands to fit everything in front of it is the
    failure mode this lane keeps recording. Five items, one missing field, one remedy.
    PRESUMPTION-947, 948, 952 and 954 are excluded for the same reason: 947 and 952 are measurement
    questions, 948 and 954 belong to the propagation flag.

  Reflexivity note: this flag is a production, filed by its author, into a directory whose consumption
    rate the estate has never measured, and — on its own analysis — it carries no expiry either. It names
    an addressee (14a/14b/12) and no date, which is exactly the defect. It should not be credited with
    force until a party other than 15b has read it and said so in writing. Consecutive-filing ordinal for
    this lane on defects in how the estate observes itself: **three**, counting 2026-09-09, 2026-09-10 and
    today. ASSUMPTION-1316 states that a third undispositioned flag would mean the flag channel is the
    defect. On the register's own stated rule, that condition is now met, and recording it is the most
    this agent can do about it — which is PRESUMPTION-949, observed in the act.
