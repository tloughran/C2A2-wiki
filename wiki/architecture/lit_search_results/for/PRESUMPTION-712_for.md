SEARCH-FOR-PRESUMPTION-712:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-712
  Original statement: That a register which grows every day is thereby doing its
    job; a sibling agent diagnosed its own output the same day ("the register
    grew by five with no consumer"), and the same night 14a/14b appended 41 + 21
    items into registers with a measured backlog drain of zero for a thirtieth
    day. Risk: High. REFLEXIVE.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-712
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Applied a sibling agent's same-day self-diagnosis to this agent and
        measured tonight's own append against it.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Near-miss reporting rate as a leading indicator — consistent practitioner
       and safety-profession position located across several independent sources
       this session (Umbrex, "Near Miss Reporting Rate Guide"; MangoApps,
       "Near-Miss Reporting: The Leading Indicator Nobody Wants to Fill Out";
       Safety Services Company; ASSP proceedings paper, "Near-Miss Reporting:
       The Missing Link of Safety Culture," 2012, aeasseincludes.assp.org
       [author not captured]; the sources attribute the leading-indicator
       designation to OSHA). — The genuine FOR case, and the only one found.
       Safety science treats a *high* near-miss reporting rate as a positive
       signal in itself: it indicates a reporting culture in which people feel
       safe flagging hazards, and mature safety cultures are described as
       reporting more near misses, not fewer. Under this framing a register that
       grows every day is evidence of a functioning detection layer and its
       growth is the metric. This is direct, if analogical, support for the
       presumption.
    2. The same literature, on the condition attached. — Every located source
       that endorses the rate as an indicator attaches the same qualifier, and
       it is the qualifier this item fails. The rate is described as a positive
       signal *paired with* low incident rates and *predictable follow-up*; the
       explicit statements located are that if near-miss reports sit in files or
       emails without action the hazards remain unaddressed, and that when near
       misses are reported and no action is taken, people stop reporting because
       the absence of feedback signals that reporting does not matter. The stated
       requirements for a functioning programme are easy reporting, protected
       reporters, and predictable follow-up. Growth with a drain of zero
       satisfies one of three.
    3. Backlog Management Index (BMI) — standard software-quality metric,
       located this session in general software-quality-metrics material
       (tutorialspoint software quality management metrics page and comparable
       testing-metrics summaries). [Textbook-level sources; the metric is
       usually credited to Kan's "Metrics and Models in Software Quality
       Engineering" — attribution from established knowledge, NOT confirmed in
       this session's results.] — Supplies the field's own answer to the
       presumption, and it is a formal one. BMI = (problems closed in period /
       problems arrived in period) x 100%. Above 100 the backlog shrinks; below
       100 it grows. The metric exists because the field concluded that arrival
       rate alone is not a health measure and must be read against closure. A
       drain of zero for thirty days is BMI = 0, the floor of the scale.
    4. Defect arrival rate as a legitimate metric — same body of material.
       — Partial support, honestly reported. Defect arrival rate is a standard
       and respectable metric, and a high arrival rate early in a test cycle is
       described as expected and healthy because it means testing is finding
       things. So "the register grew" is not a meaningless number and the
       presumption is not absurd. The qualifier in the located material is
       temporal: this reading applies *early*, within a cycle that is expected
       to close, and the companion framing (fix backlog, defect inflow not
       outpacing resolution capacity) is what governs sustained operation.
    5. Little's Law and unbounded queues — L = λW (Wikipedia; Slimmon, D.,
       "Using Little's Law to scale applications," blog.danslimmon.com, 2022;
       InfoQ, "The Mathematics of Backlogs: Capacity Planning for Queue
       Recovery"; LeSS "Flow & Queueing Theory"). [Located this session; not
       opened beyond returned summaries.] — Theoretical grounding for why the
       thirty-day observation is the operative one. Little's Law holds
       independently of arrival distribution, service distribution and service
       order. With a positive arrival rate and a service rate of zero the queue
       has no stationary solution; the located material states plainly that
       allowing a queue to be unbounded means latency continues to increase, and
       that bounding response time requires bounding queue length. This is the
       formal statement of the production-rate governor the item asks about.
    6. Alarm and alert fatigue — clinical monitoring literature located this
       session: AHRQ PSNet, "Reducing the Safety Hazards of Monitor Alert and
       Alarm Fatigue"; Drew et al. (or similar), "Insights into the Problem of
       Alarm Fatigue with Physiologic Monitor Devices: A Comprehensive
       Observational Study of Consecutive Intensive Care Unit Patients," PMC
       4206416 [author attribution NOT verified — the snippet did not give it];
       Cvach, M., "Monitor Alarm Fatigue: An Integrative Review," Biomedical
       Instrumentation & Technology 46(4):268 [author/volume from the located
       DOI string 10.2345/0899-8205-46.4.268, year not confirmed]. — The
       measured consequence of production without consumption, and it is not
       neutral. Reported non-actionable alert rates exceed 70% across
       physiological monitoring, with 80-99% of ECG monitor alarms false or
       clinically insignificant. [Figures as returned in search summaries; I did
       not open these papers and these numbers should be verified before reuse.]
       The described endpoint is desensitisation, silencing without checking,
       and adverse events when a true signal is not attended to. Production
       without consumption does not merely fail to help; it degrades the
       channel.

  Strength of support: Weak

  Summary: One real supporting case exists and it comes from safety science:
    near-miss reporting rate is treated by OSHA and the safety profession as a
    leading indicator, and a high rate is read as a positive signal about
    culture rather than a negative signal about risk. A register that grows
    every day can, on that reading, be doing its job by the growth alone. But
    every located source that endorses the rate attaches the same condition —
    the rate is a positive indicator when paired with predictable follow-up, and
    the explicit warning in that literature is that reports which sit without
    action leave hazards unaddressed and cause reporting to stop. The condition
    is exactly what a thirty-day drain of zero denies. The software-quality
    field reached the same conclusion formally and built a metric for it: the
    Backlog Management Index is the ratio of closures to arrivals precisely
    because arrival count alone was found insufficient, and a drain of zero puts
    BMI at the floor of its scale. Little's Law supplies the mechanism —
    positive arrivals against zero service admit no stationary solution and the
    queue's latency grows without bound — and the alarm-fatigue literature
    supplies the measured consequence, in which non-actionable rates above 70%
    produce desensitisation and missed true signals rather than a merely
    unproductive archive. The presumption is not absurd, and I would not report
    it as unsupported: detection has value, arrival rate is a real metric, and
    the safety-culture reading is a serious position. It is, however, supported
    only under a condition the item's own measurements record as absent, and
    the reflexive point stands unrefuted — a 62-item append on the thirtieth day
    of zero drain is measured by every located framework as a worsening, not a
    contribution.

  Caveats: The near-miss transfer is analogical: safety reporting rate measures
    *willingness to report* in a population of humans who might not, and its
    value as a culture indicator derives from that reluctance. An automated
    agent has no reluctance to overcome, so the specific reason a high rate is
    good in safety science does not obviously transfer to a register appended by
    software, and this materially weakens source 1 — I am recording it as the
    best FOR case available while noting that its mechanism may not apply here
    at all. Source 3's attribution to Kan is from established knowledge and
    unverified. Source 6's figures were taken from search summaries of papers I
    did not open and its author attributions are uncertain; the direction is
    consistent across four independent sources but the specific percentages
    should not be quoted downstream. Source 5 is textbook material applied to a
    system whose "service" is a human reading a register, which is not the
    process Little's Law was derived for, though the law's independence from
    service distribution is unusually favourable to the transfer. One
    counterargument the search did not defeat: a register may be a durable
    archive rather than a queue, in which case zero drain is not a failure but
    the intended steady state, and Little's Law does not apply because nothing
    is meant to leave. No located source addresses registers designed as
    archives rather than as work queues, and the item's framing assumes the
    queue reading without arguing for it.

  NOVELTY-FLAG: Not raised for the general claim, which is well covered. A gap
    is noted on one sub-question the item asks directly and that nothing located
    answers: no source was found describing a *production-rate governor* on an
    issue or defect register — a mechanism by which the detecting party throttles
    its own output as a function of the consuming party's drain rate. WIP limits
    and back-pressure exist for work queues, and alarm-suppression exists for
    monitoring, but a self-throttling audit producer was not located. If C2A2
    builds one, it may be an original contribution.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: alert fatigue and signal-to-noise
    in monitoring, non-actionable alarm rates and their consequences; defect
    arrival rate versus closure rate, Backlog Management Index; Little's Law,
    unbounded queues and back-pressure; near-miss reporting rate as a leading
    indicator and the conditions attached to it. Not searched, and recommended:
    WIP limits in Kanban as an explicit production governor; the information-
    overload literature on document production exceeding reading capacity; and
    the discussion of "audit findings backlog" in internal-audit practice, which
    would be the closest domain match to a register of process defects.
