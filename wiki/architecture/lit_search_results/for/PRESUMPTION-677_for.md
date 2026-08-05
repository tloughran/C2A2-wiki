SEARCH-FOR-PRESUMPTION-677:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-677
  Original statement: That the rate at which the system produces work for its
    single human consumer is independent of the rate at which he can act on it —
    34 pending proposals, 136 REVISE, 137 MONITOR, 30 days with no decision, 12
    days with no review pass — and 14b's own definition instructs it to err
    toward more. (Queries PREMISE-138 directly.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-677
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from six independently measured backlog figures read against
        the stated norm in 14b's own agent definition
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. EEMUA Publication 191, Alarm Systems: A Guide to Design, Management and
       Procurement (Engineering Equipment and Materials Users Association). —
       Directly contradicts independence. The guide sets human-capacity-derived
       rate targets (long-term average below roughly 6 alarms per operator per
       hour as acceptable; above ~30 indicating a seriously deficient system;
       peak rates bounded at roughly 10 per 10 minutes), on the explicit
       reasoning that human capacity to absorb alarms is limited and that if the
       limit is exceeded for long periods important alarms will be overlooked
       and in extreme cases the whole alarm system will be more or less ignored.
       The production rate is treated as a design variable constrained by the
       consumption rate, not as independent of it.
    2. ANSI/ISA-18.2, Management of Alarm Systems for the Process Industries. —
       Defines an alarm as an indication of a condition requiring a response,
       and builds rationalisation around that definition: an item with no
       defined, available operator response should not be raised as an alarm.
       This is the normative form of the dependence — the right to produce an
       item is conditioned on the consumer's capacity to act on it.
    3. Sadowski, C., van Gogh, J., Jaspan, C., Söderberg, E. & Winter, C., 2015.
       "Tricorder: Building a Program Analysis Ecosystem." ICSE 2015; and
       Sadowski, C., Aftandilian, E., Eagle, A., Miller-Cushon, L. & Jaspan, C.,
       2018. "Lessons from Building Static Analysis Tools at Google."
       Communications of the ACM 61(4). — The strongest analogous evidence, and
       the closest match to C2A2's structure (an automated producer feeding
       human reviewers). Google found developer trust to be highly sensitive to
       output quality, imposed an effective-false-positive ceiling of ~10% as a
       condition of an analyzer being surfaced at all, and observed that
       analyzers exceeding it were routinely dismissed or disabled. The
       operative lesson is that the producer's output rate and quality determine
       the consumer's response rate — the two are coupled, and Google manages
       the coupling by actively suppressing output.
    4. Little, J.D.C., 1961. "A Proof for the Queuing Formula: L = λW."
       Operations Research 9(3): 383-387. — The mathematical grounding, and it
       runs against the presumption. Where the arrival rate exceeds the service
       rate the queue length grows without bound; the six backlog figures cited
       in the item (34 / 136 / 137, with 30 days and 12 days of no service) are
       the observable signature of λ > μ sustained over time. Independence of
       the two rates is possible only in the limit of an unbounded buffer whose
       depth has no effect on the consumer, which is the assumption the alarm
       literature denies.
    5. Producer-consumer decoupling via buffering (standard concurrent- and
       distributed-systems design; AWS Builders' Library, "Avoiding
       insurmountable queue backlogs"). — The only route to support found, and
       it is explicitly bounded. A queue does decouple producer and consumer
       rates, but only transiently: the same source states that once arrival
       exceeds processing the system flips into a mode where end-to-end latency
       grows and recovery takes disproportionately long. Decoupling is a
       short-run smoothing property, not rate independence.

  Strength of support: None

  Summary: No supporting literature was found for the independence claim, and
    the most directly applicable literatures were written specifically to deny
    it. The alarm-management standards already in this system's citation base
    (EEMUA 191, ANSI/ISA-18.2) treat production rate as a design variable
    bounded by human absorption capacity, and state the failure mode that
    follows from ignoring the bound: important items are overlooked and the
    channel as a whole is discounted. Critically for this item, that failure
    does not require false positives — the alarm literature's degradation curve
    is driven by rate, so additional true positives past the threshold still
    reduce response rate. The Google static-analysis results supply the same
    finding in the closest available analogue to C2A2's own structure, and show
    an organisation actively suppressing valid output to preserve consumer
    response. Little's Law supplies the mathematics: with service rate near zero
    over 30 days, any positive production rate makes the backlog unbounded, and
    the six measured figures are that prediction realised. The only supportive
    principle located — producer-consumer decoupling by buffering — is
    explicitly a short-run property that its own sources say inverts under
    sustained overload.

  Caveats: The alarm standards were written for real-time process control, where
    the response deadline is seconds and the cost of a missed alarm is physical;
    C2A2's items are asynchronous with no hard deadline, so the transfer is by
    analogy and the thresholds themselves (6/hr, 10/10min) do not carry over as
    numbers. The Google case concerns false-positive rate more than raw volume,
    and its ~10% ceiling is a proxy for trust rather than a capacity limit. No
    peer-reviewed study of backlog depth as a demotivator in single-consumer
    review queues was located — that specific link is supported here only by
    practitioner sources and is a genuine gap. Note the reflexive dimension the
    item raises: since 14b's own definition instructs it to err toward more,
    this presumption is one that the producing agent has a standing instruction
    to act on, which means it cannot be resolved by the producer alone.

  NOVELTY-FLAG: Not raised. The claim is well covered by existing literature;
    the literature simply runs against it.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate. Concepts searched: alarm and alert fatigue; EEMUA 191
    and ANSI/ISA-18.2 alarm rate benchmarks, rationalisation and flood;
    desensitisation at rate rather than at error; static-analysis warning
    fatigue and the Google false-positive ceiling; queueing theory, Little's Law
    and unbounded backlog growth; defect backlog triage and the arrival-versus-
    fix-rate gap; producer-consumer decoupling and queue-based load levelling.
