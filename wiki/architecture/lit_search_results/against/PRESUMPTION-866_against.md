SEARCH-AGAINST-PRESUMPTION-866:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-866
  Queue ref: LIT-QUEUE-2026-08-24-004
  Original statement: "A monitoring system discharges its function by detecting and reporting faithfully, independent of whether any responder acts."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-866
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by placing the watchdog's stated design principle beside its own six-day record of unheeded output
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Comprehensive within the constraint noted below. Queries run against alarm fatigue,
    unheeded/unnoticed alarms, operator-in-the-loop assumptions in safety-critical monitoring, and
    system-theoretic accident modelling (STAMP/STPA). Venues reached: Journal of the Acoustical
    Society of America (1988), Proceedings of the Human Factors and Ergonomics Society (1999, 2003),
    Ergonomics (1995), Safety Science / MIT preprint (Leveson), the Google SRE book (2016/2017),
    Google SRE engineering blog, and investigative reporting backed by ECRI Institute and FDA MAUDE
    adverse-event data (Boston Globe, 2011). Date range 1956–2026.
    GAPS: the session's web-search budget was exhausted after six queries, and subsequent retrieval was
    restricted to URLs already in the provenance set. Several primary sources (Sorkin 1988; Woods 1995;
    Xiao et al. 2003; Bliss et al. 1995; Seagull & Sanderson 2001) were reached only at
    abstract/reference-list level, not full text. No systematic review or meta-analysis of unheeded-alarm
    outcome rates was retrieved. The 216-death ECRI/Globe dataset is journalism over a regulatory
    database, not a peer-reviewed epidemiological study.

  Challenging evidence found: Yes

  Sources:
    1. Kowalczyk, L. 2011. "Patient alarms often unheard, unheeded." The Boston Globe, 13 Feb 2011
       (full text reproduced at https://www.massnurses.org/2011/02/13/patient-alarms-often-unheard-unheeded/).
       — Analysis with the ECRI Institute of FDA adverse-event reports found 216 deaths (Jan 2005–Jun 2010)
       in which monitor-alarm problems occurred; in 49 of the cases where hospitals claimed no warning was
       given, manufacturers' review of the monitors' internal alarm logs showed the monitors *had* detected
       and *had* alarmed correctly. In 25 further cases staff silenced a correctly-firing alarm without
       providing care. This is the direct empirical counterexample: faithful detection and faithful
       reporting, and the monitored subject died anyway. FULL-TEXT.
    2. Kowalczyk, L. 2011, ibid., reporting a Joint Commission review (Feb 2002 alert) of 23 patients who
       died or were left comatose after ventilator malfunction: in 65% of cases staff did not respond to
       alarms, set them incorrectly, or did not hear them at low volume. — Establishes that non-response is
       the modal contributor, not detection failure. FULL-TEXT (as reported).
    3. Kowalczyk, L. 2011, ibid., reporting ECRI's Pennsylvania data: 35 deaths related to physiological
       monitor alarms since June 2004, of which 28 involved a "staff failure," including nine explicitly
       attributed to alarm fatigue. — Same direction, independent state dataset. FULL-TEXT (as reported).
    4. Xiao, Y., Seagull, F. J., Nieves-Khouw, F., Barczak, N., Perkins, S. 2003. "Why are They not
       Responding to our Alarms? Another Analysis of Problems with Alarms." Proceedings of the Human
       Factors and Ergonomics Society Annual Meeting 47(3):386–390. DOI 10.1177/154193120304700329.
       — Abstract states that investigations into adverse-outcome incidents "often lead to blames of not
       responding to auditory alarms which in most cases sound at audible levels," and identifies a spectrum
       of structural reasons (alarm volume, alarm confusion, transient high workload, economic pressure) why
       correctly-sounding alarms are not acted on. The paper's existence as a research question is itself
       evidence that the field does not treat faithful sounding as discharge of function. ABSTRACT-ONLY.
    5. Sorkin, R. D. 1988. "FORUM: Why are people turning off our alarms?" Journal of the Acoustical Society
       of America 84(3):1107–1108. DOI 10.1121/1.397232. — Canonical statement of the problem that a
       technically correct alarm whose base rate of nuisance firing is high will be disabled by its
       responders, i.e. detection quality and response quality are coupled, not independent.
       SNIPPET-ONLY (citation verified against two independent reference lists; body not read).
    6. Woods, D. D. 1995. "The alarm problem and directed attention in dynamic fault management."
       Ergonomics 38(11):2371–2393. DOI 10.1080/00140139508925274. — Frames alarms as a problem of
       *directing attention*, not of emitting signal; the design objective is the responder's attentional
       state, which cannot be assumed. SNIPPET-ONLY (citation verified via reference list; body not read).
    7. Leveson, N. "A New Accident Model for Engineering Safer Systems." MIT preprint,
       http://sunnyday.mit.edu/accidents/safetyscience-single.pdf [published venue Safety Science —
       details unverified]. — States the four conditions required to effect control over a system
       (attributed to Ashby, 1956): "1. The controller must have a goal or goals... 2. The controller must
       be able to affect the state of the system, 3. The controller must be (or contain) a model of the
       system, and 4. The controller must be able to ascertain the state of the system." A monitor satisfies
       conditions 1, 3 and 4 and *not* condition 2. Under this framework a detect-and-report component with
       no acting responder is not a control loop at all; it is an open loop, and open loops do not enforce
       safety constraints. FULL-TEXT (PDF, read in relevant part).
    8. Leveson, ibid., §on Challenger. — "One constraint that was violated during operations was the
       requirement to correctly handle feedback about any potential violation of the safety design
       constraints... There were several instances of feedback that was not adequately handled, such as data
       about O-ring blowby and erosion during previous shuttle launches and feedback by engineers who were
       concerned about the behavior of the O-rings in cold weather." Challenger is the canonical case where
       detection and reporting were performed faithfully and repeatedly, and the monitoring function was
       nonetheless not discharged. FULL-TEXT (PDF, read in relevant part).
    9. Holthaus, G. "Teaching a new way to prevent outages at Google." Google SRE,
       https://sre.google/stpa/teaching/ [no publication date on page]. — Reports a real Google outage:
       a software controller scheduled an unsafe control action to occur after 30 days; "Even though there
       were indicators that this unsafe action was going to occur, no software engineers—humans—were
       actually monitoring the indicators. So, after 30 days, the unsafe control action occurred, resulting
       in an outage." Detection existed, indicators were correct and available for 30 days, nobody was
       attending, and the loss occurred. A software-domain counterexample structurally identical to C2A2's
       49-day condition. FULL-TEXT.
   10. Ewaschuk, R. "Monitoring Distributed Systems," Ch. 6 in Beyer, B., Jones, C., Petoff, J., Murphy, N. R.
       (eds.), Site Reliability Engineering. O'Reilly/Google, 2016 (online at
       https://sre.google/sre-book/monitoring-distributed-systems/). — Defines the purpose of monitoring in
       responder terms: "we want a human to investigate the alert, determine if there's a real problem at
       hand, mitigate the problem, and determine the root cause." Prescribes that "Every page should be
       actionable" and that a valid alert rule must answer "Can I take action in response to this alert?"
       Footnote 22 on email alerts: "Sometimes known as 'alert spam,' as they are rarely read or acted on."
       The chapter's conclusion is that "Email alerts are of very limited value." An unattended reporting
       channel is treated by this literature as near-zero-value by definition, not as a discharged function.
       FULL-TEXT.

  Strength of challenge: Strong

  Summary: No literature was found in the human-factors, safety-engineering, or site-reliability traditions
    that treats faithful detection and reporting as sufficient discharge of a monitoring system's function.
    The uniform position across all three traditions is the opposite: monitoring is defined instrumentally by
    the response it enables, and detection without response is classified as a failure of the monitoring
    system (not merely of the responder). Leveson's restatement of Ashby's four conditions makes the
    theoretical version precise — a component that can ascertain state but cannot affect state does not
    close a control loop — and the ECRI/FDA, Joint Commission, and Pennsylvania datasets supply the
    empirical version, where the modal path to a monitoring-related death is a correctly-functioning,
    correctly-sounding alarm that no one acted on. The Google STPA outage narrative supplies a pure-software
    instance at a 30-day unattended horizon. The presumption as stated is not a boundary-condition
    disagreement; it is contradicted at its core.

  Specific risks: If PRESUMPTION-866 is false, C2A2's self-awareness layer has been accumulating a
    reported-but-unactioned backlog for 49 days while its own health metric reads as satisfied, which means
    (a) the layer's status signal is uninformative about the property it exists to guarantee, (b) every
    downstream component that treats "watchdog reported" as equivalent to "condition handled" is operating
    on a false premise, and (c) the longer the unattended interval runs, the more the literature predicts
    active *degradation* of eventual response — Sorkin's and Woods's findings are that unattended and
    nuisance-heavy channels get disabled, muted, or filtered by their responders, so the 49-day record does
    not merely represent 49 days of neutral waiting but 49 days of conditioning toward permanent
    non-response. The failure is silent and self-concealing: the layer will continue to report health
    correctly right up to and through the loss it exists to prevent.

  Mitigations available:
    - Redefine the layer's success criterion in outcome terms rather than emission terms — the SRE
      formulation "every page should be actionable" and "can I take action in response to this alert?"
      (Ewaschuk, SRE book Ch. 6) is the operational test.
    - Instrument the acknowledgement edge, not just the emission edge: track time-to-acknowledge and
      time-to-close per report, and treat unacknowledged-for-N-days as its own alarm condition (analogue of
      Google's finding that missing feedback *to humans* was the causal factor, per Holthaus).
    - Escalate on non-response rather than repeat at the same level. Repetition at constant level is what
      Sorkin (1988) and the ECRI data identify as the mechanism producing desensitisation.
    - Reduce report volume aggressively so the surviving reports carry attention (Ewaschuk, ibid.:
      "Signals that are collected, but not exposed in any prebaked dashboard nor used by any alert, are
      candidates for removal").
    - Where response can be automated at all, automate it and page only on the automation's failure —
      SRE Ch. 6: "Every page response should require intelligence. If a page merely merits a robotic
      response, it shouldn't be a page."
    - Close condition 2 of Ashby's four (Leveson): give the layer at least one real actuator (halt,
      quarantine, refuse-to-proceed) so that it is a controller and not an open loop.

  STEELMAN:
    Item: PRESUMPTION-866
    Strongest counterargument: A monitor with no actuator is still not worthless — it is a *sensor*, and
      sensors are legitimately evaluated on fidelity alone within a larger architecture that supplies the
      controller elsewhere. The literature above condemns unattended alarms in settings where the alarm was
      the last line of defence before an irreversible loss (patient death, launch failure, outage); if
      C2A2's monitored conditions are reversible, non-time-critical, and reconstructable from the report log
      whenever a human eventually reads it, then non-response is a deferred cost, not a null result. The
      strongest form of this defence is that the report log is durable: unlike a beep in an ICU, a written
      report persists, so the detection retains its value across the unattended interval and can be
      actioned in arrears. On this reading the layer's fidelity is exactly what makes eventual remediation
      possible, and the 49-day gap indicts the responder, not the monitor.
    What would need to be true for C2A2 to be safe: (1) every condition the layer detects must be
      recoverable after arbitrary delay — no condition may have a deadline, compound over time, or destroy
      the evidence needed to fix it; (2) the report channel must be durable, complete and readable in
      arrears, with no truncation, rotation or overwrite; (3) no other component may treat "reported" as
      "handled" in its own control logic; (4) the layer's own health metric must not count emission as
      success, or the system as a whole loses the ability to distinguish "nothing wrong" from "everything
      wrong and no one looking"; (5) there must exist an actual scheduled attendance event with a bounded
      period, and the observed 49-day interval must be an anomaly against that period rather than the de
      facto steady state.
    How to test: Empirically checkable inside C2A2 without new instrumentation. (a) Inject a known,
      benign, uniquely-tagged fault; measure wall-clock time from detection to any state change caused by a
      responder. If no state change occurs within the intended attendance period, condition (5) is false.
      (b) Audit the existing report backlog for conditions that have compounded, expired, or become
      unreconstructable since first report — any single instance falsifies condition (1). (c) Grep the
      codebase for consumers that branch on "reported/logged" as a proxy for "resolved" — any hit falsifies
      condition (3). (d) Compare the layer's self-reported health series against the count of open
      unacknowledged reports over the same 49 days; if the two are uncorrelated, condition (4) is false and
      the metric is measuring emission.

  Recommendation: CHALLENGED
