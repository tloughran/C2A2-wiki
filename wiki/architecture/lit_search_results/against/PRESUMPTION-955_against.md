SEARCH-AGAINST-PRESUMPTION-955:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-955
  Original statement: "[inferred] That a status vocabulary's first duty is to protect the downstream alarm
    from false positives, and only its second to protect the reader from false assurance."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-955
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the stated ordering of reasons in a run that asked for exactly this ruling.
        Moderate-confidence: the run may hold the opposite priority and have reported the reasons in the
        order they occurred rather than in order of weight.
      15b: Searched for challenging literature; found that the industrial standards resolve the dilemma by
        refusing it — a ternary quality vocabulary that is orthogonal to the alarm — and found the exact
        documented failure mode C2A2 is exhibiting (Good-quality stale tag, alarm stack does not trip).
    Current status: CHALLENGED

  Register pre-check:
    - **PREMISE-110 (ACTIVE) — the governing premise and it is verbatim.** "Detectors do not reliably
      degrade gracefully; they invert. A monitor whose failure presents as a nominal reading becomes MORE
      reassuring as the monitored condition worsens, and this is a catalogued fault class
      (stuck-at-nominal, one of five standard non-fail-stop sensor faults), not a novel or rare one."
      A PASS on a task that did not run is a manufactured stuck-at-nominal.
    - **PREMISE-100 (ACTIVE).** "A liveness signal is not evidence of correctness, and a health check that
      cannot execute in its runtime context reports as passing rather than as absent; monitoring that
      conflates the two produces false-green at a rate proportional to the number of inoperable checks."
    - **PREMISE-086 (ACTIVE).** Alarm on the AGE of the last dated PASS/FAIL; staleness is the signal
      (dead-man's-switch / heartbeat). This is the exact control that would have caught the seven-day-cold
      `metabolism_data.json` and it is ACTIVE.
    - **PREMISE-141 (ACTIVE).** "ABSENCE OF A REPORT IS A THIRD TERMINAL STATE, NOT A VALUE OF THE OTHER
      TWO." Cristian's failure-semantics taxonomy. ASSUMPTION-1314 describes the third state as something
      the run had to invent; PREMISE-141 already had it.
    - **PREMISE-167 (ACTIVE).** An escalation and a measurement are different objects and must be stored as
      different objects; an escalation expressed only as a withheld PASS-mark has no representation on
      disk distinct from staleness.
    - PREMISE-099 (ACTIVE) — a flag that annotates without gating does not prevent emission; the
      enforcement point is what matters, not the documentation. A qualifier on a PASS is annotation.
    - PREMISE-089 (ACTIVE) — freshness is a per-source property. PREMISE-063 (ACTIVE) — absence must be
      encoded as distinct from a true zero.

  Challenging evidence found: Yes

  Sources:
    1. OPC UA / OPC DA data-quality semantics — the ternary GOOD / UNCERTAIN / BAD quality code, with
       sub-status bits for stale data, device failure and communication timeout. — SECONDARY (search
       summaries of OPC Foundation forum material, Schneider GeoSCADA driver documentation and vendor
       knowledge-base articles; the OPC UA specification itself was NOT retrieved — recorded) — **This is
       the strongest challenge in the file and it dissolves the presumption's dilemma rather than
       answering it.** The industrial answer to "the value is current but I did not produce it" is not a
       decorated PASS; it is a THIRD QUALITY STATE carried on the datum itself, orthogonal to the alarm
       layer. Two consequences follow. First, the spec requires the VALUE be set to NULL when quality is
       Bad — i.e. the consumer is structurally prevented from using a datum whose provenance is broken,
       which is the enforcement point PREMISE-099 demands. Second, because quality is a separate channel
       from alarming, protecting the alarm from false positives costs nothing in truthfulness; the two
       duties are not in competition and no ordering is required. The presumption's whole framing — that
       one duty must come first — is an artefact of a binary vocabulary.
    2. The documented failure mode: OPC UA tags reporting Good quality while the value timestamp is hours
       or days stale, with the quality badge staying green and the alarming stack not tripping a Stale Data
       notification because the tag quality never went to Stale or Bad. — SECONDARY (vendor knowledge-base
       article, practitioner grade) — **This is C2A2's exact present condition, named as a defect in the
       industry that has it most often.** `metabolism_data.json` is seven days cold; `Morning system
       health` reads it and does not fire. The industry calls this a defect requiring a stale-data alarm,
       not an acceptable optimisation.
    3. ISA-18.2 / IEC 62682 and EEMUA 191. — SECONDARY (search summaries; standards texts not retrieved) —
       Two findings, and they cut in opposite directions, so both are reported. (a) CUTS FOR the
       presumption: ISA-18.2 defines an alarm as indicating a condition "requiring a response," and states
       that alarms requiring no operator response should be converted to indications or events. Firing
       `morning-system-health` over feeds that are genuinely current would be an alarm with no required
       response, which the standard says to demote. The telemetry run's instinct is standard-compliant.
       (b) CUTS AGAINST the presumption: the demotion target is an INDICATION OR EVENT — a distinct,
       recorded, visible object — not a PASS. The standard's remedy for "true but not alarm-worthy" is to
       move it to a different channel, never to report it as normal. And shelving, the standard mechanism
       for suppressing a nuisance signal, is explicitly time-bounded (EEMUA 191 default 4 hours) and
       self-clearing, which a `PASS` with a qualifier is not.
    4. Fail-safe / safe-state design and watchdog supervision, including the SAFEBUS freshness-monitoring
       pattern. — SECONDARY (search summaries, including patent literature) — Where data freshness is
       safety-relevant, the canonical design is: heartbeat absent → data flagged stale/invalid → transition
       to safe state. The default on staleness is to fail toward the conservative reading, not toward
       continuity. The estate's default is the opposite.
    5. Silent-failure / cron-monitoring practitioner literature. — SECONDARY (practitioner blogs; low
       evidential grade, reported as such) — The recurring formulation is directly on point: monitoring
       configured to alert on crashes rather than on the absence of a success signal cannot catch things
       that did not happen, and "the absence of an error is not the same as the presence of success." One
       account describes four of five backup paths failing silently for months with dashboards green.
       Anecdotal, but it is the failure shape and it is common enough to have a cottage industry.

  Strength of challenge: **Strong**.
    Limb split — and the split is the finding:
      - "Alarm precision matters and spurious firing is a real cost": **No challenge.** ISA-18.2 agrees;
        alarm fatigue is real and well-measured (the 49–96% override band, PREMISE-121). The run was right
        about this.
      - "Therefore the alarm's precision comes FIRST and the reader's protection SECOND": **Strong**
        challenge. Every standard family I searched refuses the ordering by refusing the binary. OPC's
        ternary quality, ISA-18.2's indication/event demotion target, and fail-safe watchdog design all
        provide a third channel so that neither duty is traded against the other. An ordering is only
        necessary if the vocabulary is impoverished, and ASSUMPTION-1314 says exactly that the vocabulary
        is binary — so the correct object of the finding is the vocabulary, not the priority.
      - "A qualifier on a PASS discharges the truthfulness duty": **Strong** challenge. PREMISE-099 holds
        that annotation without gating does not prevent emission, and the OPC pattern enforces at the
        consumer (value NULL on Bad quality) precisely because annotation was found insufficient. The
        same-day evidence is decisive: `Morning system health` read a seven-day-cold artefact and did not
        fire, which is the qualifier failing to travel exactly as PREMISE-188 predicts.
    The recommendation rests on the second and third limbs.

  Summary: The literature does not say the telemetry run chose wrongly between two goods; it says the
    choice should not have been available. Industrial monitoring resolves "verified current but not
    produced by me" with a ternary quality vocabulary carried on the datum and orthogonal to the alarm
    layer, and it enforces at the consumer rather than annotating at the producer. ISA-18.2 supports the
    run's instinct that a no-response alarm should not fire, but its remedy is demotion to an *indication
    or event* — a distinct recorded object — never a report of normal. The cost of the estate's ordering
    is visible in the same day's record and the industry has a name for it: a Good-quality tag with a
    days-old timestamp, whose green badge means the stale-data alarm never trips. That is the
    stuck-at-nominal inversion PREMISE-110 already holds, and PREMISE-086 already specifies the control
    (alarm on age) that would catch it.

  Specific risks: The estate now has a precedent for a green status on a task that did not run, at the
    same moment a downstream health check is silently reading a week-old artefact — so the presumption's
    cost is not prospective, it is realised. The precedent generalises badly: every future task that
    cannot do its work but can verify that someone else's work is current has a template for reporting
    PASS. Because the qualifier lives in prose and the consumer keys on the status token, the qualified
    PASS and an unqualified PASS are indistinguishable to every automated reader — which means the
    estate's monitoring becomes *more* reassuring as the number of non-running tasks grows, which is
    PREMISE-110's inversion at the system level rather than the sensor level.

  Mitigations available:
    - **Make the vocabulary ternary.** PASS / DEGRADED / FAIL, or better, borrow OPC directly: GOOD /
      UNCERTAIN / BAD, where UNCERTAIN is a first-class token that automated consumers must handle. This
      answers ASSUMPTION-1314 and PRESUMPTION-955 with one change and is the single highest-value item in
      this batch.
    - **Enforce at the consumer, not the producer.** OPC's rule — value NULL when quality is Bad — is the
      pattern. A downstream check reading an artefact whose quality token is not GOOD should refuse to
      compute rather than compute on it. This is PREMISE-099's enforcement point.
    - **Implement PREMISE-086 today, independently of all of the above.** Alarm on the AGE of
      `metabolism_data.json`. This is one comparison and it catches the realised failure regardless of how
      the vocabulary question is ruled. It is the cheapest fix in this batch and it is already an ACTIVE
      premise that nobody applied.
    - **If a signal must be suppressed, shelve it explicitly.** EEMUA 191's pattern: recorded,
      time-bounded, self-clearing. A qualified PASS is an indefinite unrecorded suppression.
    - **Store escalation separately from measurement** (PREMISE-167), so that "I could not do the work" has
      a representation on disk that is not a value of the health field.

  STEELMAN:
    Item: PRESUMPTION-955
    Strongest counterargument: The ordering the run chose is not a value judgement smuggled in as a
      technical one — it is the correct response to the only cost in this system that is actually
      measured. Alarm fatigue is real, is quantified (override rates 49–96%, already held as PREMISE-121),
      and is the documented mechanism by which monitoring systems stop working entirely; false assurance,
      by contrast, has no measured rate here and its harm in this instance was zero, because the feeds
      genuinely were current. A bare FAIL over current feeds would have taught the reader that FAIL does
      not mean failure, which degrades every future FAIL — a systemic, compounding cost — whereas a
      qualified PASS degrades only the reader's information about one run, once. Further, the ternary
      remedy is not free: OPC's UNCERTAIN state exists in a system with a specification, conforming
      clients, and a validation suite. Adding a third token to a vocabulary whose consumers are prose-
      reading agents and one human produces a token that is handled by nobody, which is worse than two
      tokens handled consistently. And the run did the most valuable thing available to it: it asked for
      the ruling rather than deciding silently.
    What would need to be true for C2A2 to be safe: (a) every automated consumer of a status token must
      actually parse and branch on it, or a third token is decoration — testable by reading the consumers;
      (b) the reader-protection duty must be discharged somewhere, and if not by the status token then by
      an age alarm on the artefact (PREMISE-086), which is independent and cheap; (c) the qualifier must
      travel with the token to every consumer (PREMISE-188), which it demonstrably does not, since the
      same day's health check read the stale artefact without noticing; (d) the alarm-fatigue cost must
      actually be binding in this estate — with single-digit daily alarms and one reader, it may not be,
      and that is measurable. (b) alone makes the system safe under either ordering and should be done
      first regardless of how the ruling goes.
    How to test: two measurements, both cheap. First, the consumer audit: grep every consumer of a status
      token and record whether it branches on the value or merely logs it. If most only log, the
      vocabulary question is moot and the answer is (b). Second, the fatigue measurement the steelman
      needs: count alarms fired per week over 30 days and the fraction acted on. If the rate is low and
      the action rate is high, alarm fatigue is not the binding cost here and the ordering the run chose
      is optimising against a cost this estate does not pay — which would convert this item from
      CHALLENGED to strongly CHALLENGED with a measured basis.

  Search scope: comprehensive — industrial alarm-management standards (ISA-18.2 / IEC 62682 / EEMUA 191,
    including rationalisation, priority and shelving semantics); OPC DA/UA data-quality code semantics and
    the stale-tag-with-good-quality failure mode; fail-safe and fail-operational design, watchdog and
    heartbeat freshness monitoring, safe-state transition on stale data; false-negative / false-positive
    cost asymmetry in safety-critical detection; silent-failure and cron-monitoring practitioner
    literature. NOT RETRIEVED: the ISA-18.2, IEC 62682, EEMUA 191 and OPC UA specification texts themselves
    (all paywalled or membership-gated — recorded). Every standards claim in this file is therefore
    SECONDARY, and the ratings are set accordingly; the practitioner failure-mode account is explicitly
    marked as low-grade and nothing rests on it alone.

  Recommendation: CHALLENGED
