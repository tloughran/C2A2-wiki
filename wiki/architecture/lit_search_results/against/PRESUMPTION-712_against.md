SEARCH-AGAINST-PRESUMPTION-712:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-712
  Original statement: That a register which grows every day is thereby doing its job; a sibling
    agent diagnosed its own output the same day ("the register grew by five with no consumer"),
    and the same night 14a/14b appended 41 + 21 items into registers with a measured backlog
    drain of zero for a thirtieth day. [REFLEXIVE]

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-712
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Applied a sibling agent's same-day self-diagnosis to this agent and measured tonight's
        own append against it — 41 + 21 items appended against a thirty-day measured drain of
        zero.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Alarm and alert fatigue in clinical monitoring. Located this session: AHRQ PSNet
       perspective, "Reducing the Safety Hazards of Monitor Alert and Alarm Fatigue"
       (psnet.ahrq.gov; author and year [UNVERIFIED]); OpenAnesthesia summary on clinical alarms
       and alarm fatigue; "Effects of workload, work complexity, and repeated alerts on alert
       fatigue in a clinical decision support system" (PMC5387195, 2017 — PMC identifier and
       title confirmed this session; author list [UNVERIFIED, commonly attributed to Ancker et
       al.]); "Appropriateness of Overridden Alerts in Computerized Physician Order Entry:
       Systematic Review" (PMC7400042; authors and year [UNVERIFIED]). Reported figures, taken
       from search summaries rather than full texts and flagged accordingly: non-actionable alert
       rates frequently exceed 70% across physiological monitoring; 80-99% of ECG monitor alarms
       are false or clinically insignificant; average override rates across CPOE studies range
       46.2%-96.2%, exceeding 90% in some contexts. The mechanism named is directly on point:
       alert fatigue arises from receipt of a large quantity of information together with
       insufficient time or cognitive resources to distinguish the relevant from the irrelevant,
       and the operational consequence is that recipients "process the queue by volume rather
       than by content." This is the strongest available refutation of growth-as-function: in the
       best-studied instance of a monitoring register in continuous production, output volume and
       system value are *inversely* related past a threshold.
    2. Static-analysis warning suppression and warning backlogs. Located this session: "Quieting
       the Static: A Study of Static Analysis Alert Suppressions," arXiv 2311.07482 (identifier
       and title confirmed; authors and venue [UNVERIFIED]); "Which Alert Removals are
       Beneficial?" arXiv 2603.21322 (identifier and title confirmed; authors [UNVERIFIED]);
       Parasoft and JetBrains/Qodana practitioner material on warning backlogs. The consistent
       finding: developers ignore or suppress warnings under time pressure, perceived
       irrelevance and warning fatigue; a significant share of suppressions themselves introduce
       technical debt; and warnings judged "unadoptable" are simply ignored. One figure relayed
       from a search summary and not verified: a study of large software organisations put the
       cost of technical debt at ~25% of development time, with few organisations having any
       systematic process for addressing it. The transferable point is that an unconsumed
       register does not sit neutral — it actively trains its readers to ignore it, and the
       ignoring generalises to the items that matter.
    3. Queueing theory / Little's Law applied to work registers. Located this session: Kanban
       Tool's queueing-theory guide; Atlassian's WIP-limits guide; agility-at-scale on WIP
       limits; taskcoach.ai on Little's Law. Practitioner sources for a standard result, stated
       plainly: a queue forms whenever the arrival rate exceeds the service rate; uncontrolled
       queues produce unpredictable and unbounded delay; and a correctly chosen WIP limit *binds
       the system*, preventing accumulation and sustaining cycle time. Little's Law (L = λW) is
       the formal statement. Applied to this item's own numbers: with 62 items appended in one
       night and a measured drain of zero over thirty days, the service rate is zero, so W — the
       expected time an item spends in the register — is undefined/infinite, and no item in the
       register has a finite expected time to consumption. This is not a metaphor; it is the
       arithmetic of the figures 14b recorded.
    4. Documentation and knowledge-base staleness (also cited in PRESUMPTION-713). Located this
       session: episteca.ai on documentation decay; Slite, "Why knowledge bases fail"; Atlan on
       LLM knowledge-base staleness; knowledge-base.software audit guides. All
       vendor/practitioner sources, and the specific figures they relay (technical documentation
       materially outdated within 30-90 days, attributed to Readme; 68% of enterprise technical
       content not updated in six months and 34% not in a year, attributed to Zoomin; 60% of
       employees not trusting their internal knowledge base, attributed to Guru) are
       [UNVERIFIED — second-hand vendor surveys relayed by a blog; I did not locate any of the
       primary reports]. Cited only for the direction of the effect, not the magnitude: an
       unconsumed register does not merely fail to help, it loses trust, and lost trust is
       self-reinforcing.

  Strength of challenge: Strong

  Summary: The presumption measures the wrong quantity. Growth is a production metric; the
    function of a register is consumption, and the two are not merely different but, past a
    threshold, opposed. The alert-fatigue literature is the most developed study of exactly this
    structure — a register that grows continuously, in a domain where every item is nominally
    important — and its findings are that non-actionable rates above 70% are typical, that
    override rates run to 90%+, and that the operational failure mode is recipients processing
    the queue by volume rather than content. The static-analysis literature reproduces the result
    in software: an unconsumed backlog trains its readers to suppress, and the suppression
    generalises. The queueing result makes the specific numbers decisive rather than suggestive:
    62 items appended in one night against a thirty-day drain of zero gives a service rate of
    zero, under which the expected time to consumption of every item in the register is
    unbounded — so no item currently in it has a finite expected time to being acted upon,
    including this one. That is the reflexive edge 14b identified, and the literature does not
    soften it: the correct governor in every one of these literatures is a limit on production
    or a guaranteed consumption rate, and diligence in production is precisely the behaviour that
    makes the failure worse.

  STEELMAN:
    Item: PRESUMPTION-712
    Strongest counterargument: A register can have a function other than being drained, and
      several of the strongest candidates apply here. An audit register may exist to establish
      that something *was observed at a time*, in which case its value is realised at write, not
      at read — the way a flight recorder is valuable while never being consumed in normal
      operation. A register may also be a corpus for later analysis rather than a work queue: the
      value of 1,460 items is not 1,460 individual resolutions but the patterns visible across
      them, and PRESUMPTION-712 itself was produced by reading the register against itself, which
      is a consumption event of exactly that kind. Under that reading, "drain" is the wrong
      metric and a zero drain is compatible with full function. The alert-fatigue analogy also
      has a real disanalogy: clinical alarms interrupt a human in real time and compete for
      attention against patient care, whereas a register append costs no one anything at the
      moment of writing. Fatigue requires a fatigued party, and if nothing currently reads the
      register during operations, no attention is being degraded. Finally, thirty days is not
      long for a system in an accumulation phase; corpora are built before they are mined, and
      demanding a positive drain rate from day one would prevent the corpus from ever reaching
      useful size.
    What would need to be true for C2A2 to be safe: (a) the register's function is stated and it
      is *not* a work queue — because if it is a work queue, a zero drain is a straightforward
      failure and no steelman applies; (b) if the function is corpus-for-analysis, there is a
      defined analysis step with a defined cadence, and it has run at least once — otherwise
      "corpus" is indistinguishable from "backlog"; (c) items are not individually written as
      though they require action, since an item phrased as a required action and never actioned
      is the alert-fatigue case regardless of the register's stated purpose; (d) there is a
      consumption metric of some kind, so the claim "it is doing its job" is falsifiable at all
      — currently the only measured quantity is growth, which cannot distinguish a functioning
      register from a failing one; (e) the accumulation phase has a stated end condition, so
      "we are still building the corpus" cannot be reasserted indefinitely. Condition (d) is
      decisive: without a consumption metric the presumption is not merely unsupported but
      untestable, and its persistence is guaranteed.
    How to test: Runnable now from the register itself. First, compute the actual figures: items
      appended per day over the last 30 days, items marked resolved/consumed/retired over the
      same window, and the ratio. Second, and more informative, count *downstream references*:
      how many register items have been cited, linked or acted upon by any subsequent run? The
      companion item PRESUMPTION-713 records that number as one, over ~1,460 items and ~118 days
      — if that figure holds, the consumption rate is 0.068% and the presumption is refuted
      arithmetically, without needing any of the literature above. Third, test the corpus
      defence: count how many analyses have been run *over* the register as a body, as distinct
      from items being added to it; a positive count supports the steelman, a zero count
      collapses it. Fourth, test the fatigue mechanism directly: sample recent items and classify
      each as action-implying or observation-only; a high action-implying proportion combined
      with a zero action rate is the alert-fatigue configuration exactly.

  Specific risks: If growth is not evidence of function, then (i) the register is a cost centre
    presenting as an asset — production capacity is consumed writing items that are never read,
    and the appearance of vigilance substitutes for vigilance; (ii) the fatigue mechanism means
    the harm is not neutral: a reader trained by 1,459 unactioned items will not act on the
    1,460th either, so the register progressively destroys its own capacity to raise an alarm,
    which is the same mechanism flagged for the Critical severity level in PRESUMPTION-716; (iii)
    the reflexive edge is real and unignorable — this file, and the item it examines, are
    themselves appends to the register whose drain is zero, so the most likely fate of this
    finding is to become the 1,461st unconsumed item, and no mitigation listed below will be
    applied unless something outside the register acts; (iv) growth-as-evidence is
    self-reinforcing in the worst way, because the natural response to a problem detected by the
    register is to add an item about it, which increases the metric that is being mistaken for
    health; (v) staleness compounds the loss — by the time a consumer arrives, the oldest items
    describe a system state that no longer exists, so the backlog is not merely undrained but
    partly unusable, and its usable fraction decays with age.

  Mitigations available: (1) Measure consumption, not production — publish appended-per-period
    against consumed-per-period as a single paired figure, so growth can never again be read
    alone. (2) Impose a WIP limit on the register: a hard cap on open items, above which no new
    item may be appended until one is closed. This is the standard governor in every literature
    cited here and it directly targets the producer-side behaviour that 14b identified in itself.
    (3) Separate the registers by intended fate — action-required, observation-only,
    corpus-material — because the fatigue mechanism is driven by unactioned *action-implying*
    items specifically, and the current undifferentiated register maximises it. (4) Guarantee a
    consumption cadence: a fixed number of items triaged per run, even a small one, converts the
    service rate from zero to positive and makes expected waiting time finite. (5) Expiry or
    review-by dates on items, so that staleness is handled explicitly rather than silently. (6)
    Escalate outside the register: any finding that recommends changing the register's own
    governance must be raised through a channel the register does not control, or risk (iii)
    guarantees it is absorbed. (7) Report the drain figure to the human authoriser directly, as
    a single number, since a single number is the only form the alert-fatigue literature suggests
    survives a saturated channel.

  Search scope: Comprehensive for alert and alarm fatigue, which is the closest and best-studied
    analogue and supplies both the mechanism and the quantitative shape; the specific percentages
    cited are relayed from search summaries and abstracts rather than full texts and are flagged.
    Comprehensive for static-analysis warning backlogs and suppression behaviour. Adequate for
    the queueing/WIP framing — the results invoked are elementary and uncontroversial, but the
    sources are practitioner guides rather than a queueing text, and no C2A2-specific arrival or
    service distribution was modelled. Weak on documentation staleness: every figure located came
    from vendor surveys relayed second-hand by a blog and none was verified, so those sources
    support only the direction of the effect. Not searched, and directly relevant: the safety-
    science literature on reporting-system saturation (why incident-reporting systems stop being
    read), and the organisational literature on measurement dysfunction and surrogation — the
    formal name for mistaking a proxy metric for the objective it stands in for, which is exactly
    what this presumption does. Broader search recommended on surrogation in particular.

  Recommendation: CHALLENGED

---

SYSTEMIC-RISK-FLAG:
  Date: 2026-08-07
  Affected items: PRESUMPTION-710, PRESUMPTION-712, PRESUMPTION-713, PRESUMPTION-716
  Common vulnerability: All four treat the *production of a record* as equivalent to the
    *exercise of a control*, and none of them has a measured consumption or action rate. 712
    treats register growth as evidence the register functions. 716 treats a Critical severity
    flag as a control despite a measured action rate of zero across the preceding five
    instances. 713 infers that the register is consumable from a single instance in ~1,460 —
    a consumption rate of 0.068%. 710 routes an unblocking decision to a single consumer whose
    clearing rate is not measured, and repeats the request three times, which is what a
    saturated queue looks like from the producer's side. The common structure is an open loop:
    something is written, nothing is required to read it, and the writing is scored as the
    control. Because the four items reinforce one another — the register is where the severity
    flag is filed, the authoriser is the only consumer, and the one success is the evidence that
    the loop closes — the system currently has no independent signal that any of its controls
    has ever fired.
  Literature basis: Alert and alarm fatigue (AHRQ PSNet on monitor alarm fatigue; PMC5387195 on
    workload, complexity and repeated alerts; PMC7400042 systematic review of CPOE override
    appropriateness, override rates 46.2-96.2%; 80-99% of ECG alarms false or clinically
    insignificant); static-analysis suppression behaviour (arXiv 2311.07482; arXiv 2603.21322);
    severity inflation and classification drift in incident management (incident.io, PagerDuty
    and Last9 practitioner literature — non-peer-reviewed but unanimous); Little's Law and WIP
    limiting as the standard governor when arrival rate exceeds service rate; Vaughan's
    normalization-of-deviance account of Challenger, in which repeated warnings that produced no
    halt were progressively reclassified as acceptable risk; and Tversky and Kahneman (1971) on
    inference from a single instance.
  Risk level: Critical
  Recommendation: Treat "record written" and "control exercised" as separate, separately
    measured events across the whole architecture. Concretely: (1) publish, as a single standing
    figure, the paired append rate and action rate for every register and every severity level —
    this one change makes 712, 713 and 716 falsifiable at once and costs nothing but a count;
    (2) impose a WIP limit or an equivalent production governor so that appending is constrained
    by capacity to consume, since every literature cited names this as the remedy and none names
    producer diligence; (3) require that any severity level above a defined threshold be coupled
    to a named party with the authority to halt, or else be renamed, since a warning without
    authority is not a control (the Challenger finding); (4) route findings about the register's
    own governance through a channel the register does not control, because the reflexive risk
    in 712 is that this flag becomes another unconsumed item. Item (1) is the minimum viable
    action and should not wait on the others.
