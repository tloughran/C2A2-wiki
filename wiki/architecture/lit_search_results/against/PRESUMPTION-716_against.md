SEARCH-AGAINST-PRESUMPTION-716:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-716
  Original statement: That a Critical severity flag which fires no action is still a control;
    sixth consecutive day at the top of the scale with an observed action rate of zero across
    the preceding five.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-716
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read the severity level against the measured action rate of prior instances at the
        same level — five prior Critical flags, zero actions, sixth flag issued at the same
        level.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Alarm fatigue in clinical monitoring — the best-evidenced instance of the exact failure.
       Located this session: AHRQ PSNet perspective, "Reducing the Safety Hazards of Monitor
       Alert and Alarm Fatigue" (psnet.ahrq.gov; author and year [UNVERIFIED]); OpenAnesthesia
       overview of clinical alarms and alarm fatigue; "Appropriateness of Overridden Alerts in
       Computerized Physician Order Entry: Systematic Review" (PMC7400042; authors and year
       [UNVERIFIED]); "Effects of workload, work complexity, and repeated alerts on alert fatigue
       in a clinical decision support system" (PMC5387195, 2017; authors [UNVERIFIED]). Figures
       below are taken from search summaries and abstracts, not full texts: 80-99% of ECG monitor
       alarms are false or clinically insignificant; non-actionable alert rates frequently exceed
       70% across physiological monitoring; average override rates across CPOE studies span
       46.2%-96.2% and exceed 90% in some settings. The mechanism named — insufficient time or
       cognitive resource to separate relevant from irrelevant, leading recipients to process the
       queue by volume rather than content — is the same mechanism operating on a top-severity
       flag whose prior instances produced nothing. The literature's central finding is that the
       *highest* alarm categories are not exempt from this; they are where it does most damage,
       because responders learn the level's real meaning from its history, not from its name.
    2. Severity inflation and classification drift in incident management. Located this session:
       incident.io on severity versus priority; PagerDuty's incident-severity classification
       guide; Last9, Atlas Systems, Giva, Xurrent, AtomPing and Secure.com practitioner
       treatments. [All non-peer-reviewed practitioner material. Cited because they are unanimous
       and because they state the finding in exactly the register of this item.] Two statements
       are directly on point. First, severity inflation is named as the most common failure mode
       in incident classification: teams classify everything Critical or High to obtain faster
       response, which destroys the framework's value and produces a permanent state of
       emergency. Second, and decisively for PRESUMPTION-716: responders begin treating SEV-1
       alerts with lower urgency *because they have learned that not all of them require an
       immediate response*. That is the calibration mechanism, and a sixth consecutive day at the
       top of the scale with five prior zero-action instances is precisely the training signal it
       describes. The recommended countermeasure — review the severity distribution periodically
       to catch classification drift before it becomes a norm — is a measurement C2A2 has not
       made.
    3. Normalization of deviance. Vaughan, D., 1996. "The Challenger Launch Decision: Risky
       Technology, Culture, and Deviance at NASA." (Author, title and year confirmed this session
       from a Columbia Magazine feature and multiple secondary treatments; the book itself was
       not read and no quotation is asserted.) The relevant account: engineers at Morton Thiokol
       warned about O-ring behaviour in cold conditions, were overruled by managers under
       schedule pressure, and — the load-bearing part — because the shuttle kept returning, the
       organisation progressively reclassified the O-ring issue as an acceptable risk. The
       secondary literature located (Psych Safety; US Army; CRisk; Columbia Magazine) makes the
       organisational-silence point explicitly: deviation risk fails to reach decision-makers who
       have the *authority to halt* the practice. This supplies the second and sharper half of
       the challenge to PRESUMPTION-716. A warning is not a control unless it is coupled to
       authority to stop the thing being warned about; a Critical flag that fires and is
       succeeded by business as usual is not a weak control but a *rehearsal* of the deviance,
       and each repetition lowers the level's future meaning. Columbia, seventeen years later at
       the same organisation, is the literature's own demonstration that this pattern is
       recurrent rather than incidental.
    4. Static-analysis warning suppression as the software-domain analogue: "Quieting the Static:
       A Study of Static Analysis Alert Suppressions," arXiv 2311.07482 (identifier and title
       confirmed; authors [UNVERIFIED]); "Which Alert Removals are Beneficial?" arXiv 2603.21322
       (identifier and title confirmed; authors [UNVERIFIED]); Parasoft and JetBrains/Qodana
       practitioner material on warning backlogs. Establishes that unadopted warnings are ignored
       as a matter of routine, that suppression becomes habitual, and that habitual suppression
       generalises beyond the warnings that provoked it.

  Strength of challenge: Strong

  Summary: A severity level is not a property of the flag; it is a claim about the response the
    flag will receive, and its meaning is set empirically by the responses prior instances
    actually received. On that reading a Critical flag with a measured action rate of zero across
    five prior instances is not a control operating weakly — it is a level whose operational
    meaning has already been redefined by its own history to "no action required," and the sixth
    instance inherits that meaning regardless of its content. The incident-management literature
    names this precisely: responders down-rate the top severity because they have learned that
    not all instances of it require immediate response, and the recommended countermeasure is a
    periodic review of the severity distribution, which has not been done here. The alarm-fatigue
    literature supplies both the mechanism and the scale of the effect in the best-studied
    analogous system, where the top alarm categories are where the damage concentrates. Vaughan's
    account adds the structural point that matters most: a warning issued to a party without the
    authority to halt is not a control at all, and the repetition of unheeded warnings is the
    documented pathway by which an organisation converts an anomaly into an accepted condition.
    The item's own figures — six consecutive days, five prior zero-action instances — are exactly
    the pattern all three literatures identify, and the fact that this is the *sixth* rather than
    the first is what converts a possible challenge into a strong one.

  STEELMAN:
    Item: PRESUMPTION-716
    Strongest counterargument: The severity level may be doing work that "action rate" does not
      capture, and the strongest version of this is a record-keeping argument rather than a
      control argument. A Critical flag establishes on the record that a condition was observed,
      classified at the top of the scale, and communicated on a specific date — which preserves
      the information for a future reader and forecloses any later claim that the condition went
      unnoticed. That value is realised at write, and a zero action rate is compatible with it.
      There is a second reading with real force: the action rate may be zero because the flag is
      correctly aimed at a party who cannot act *yet*, not because the level is miscalibrated. If
      the condition requires the single human authoriser's decision (PRESUMPTION-710) and that
      authoriser is a saturated single consumer, then the flag has done its job — routed the
      condition to the right party at the right level — and the failure is entirely downstream in
      the queue, not in the classification. On that reading downgrading the severity would be the
      error: it would reduce the flag's chance of ever being acted on while doing nothing about
      the actual constraint. Third: the alarm-fatigue analogy requires a fatigued party, and if
      the flag's only reader is a human who reads it once every several days rather than a
      clinician processing 180 alerts a shift, the volumes are not comparable and the mechanism
      may not transfer. Six flags is not 180 alarms per day.
    What would need to be true for C2A2 to be safe: (a) the Critical level is coupled to a named
      party with the authority to halt or change something — otherwise, on Vaughan's finding, it
      is a notification and should be named one; (b) the level carries a defined response
      obligation with a time bound, so that "no action" is a detectable breach rather than the
      default; (c) the severity distribution is reviewed periodically, which is the specific
      countermeasure the incident-management literature names and which would have surfaced this
      at instance two or three rather than six; (d) if the intended function is record-keeping
      rather than control, that is stated, and the level is renamed accordingly — a
      record-keeping category and a control category should not share a name, because sharing one
      is what produces the drift; (e) the zero action rate is diagnosed: is it miscalibration
      (the flags are not Critical), saturation (the consumer cannot act), or absent authority (no
      one can act)? These have entirely different remedies and the current record does not
      distinguish them. Condition (e) is decisive, and none of the mitigations below should be
      applied before it is answered.
    How to test: Runnable from the record. First, tabulate every Critical-severity flag ever
      issued alongside whether any action followed within a defined window; the item states 0/5,
      and extending this over the full history gives the level's true operational meaning as a
      number. Second, run the same tabulation for every other severity level. If the action rate
      is zero at *all* levels, the problem is not severity calibration but the consumption gap
      identified in PRESUMPTION-712, and no amount of re-calibration will help. If the action
      rate varies by level, the scale is working and only the top is inflated — a different and
      much easier problem. Third, test the authority question directly: for the most recent
      Critical flag, name the party who could have acted on it and confirm that party both saw it
      and had the authority to act. If no such party can be named, the Vaughan reading is
      established and the flag is a notification. Fourth, test the drift prediction: compare the
      elapsed time to first read for early Critical flags against recent ones. Increasing latency
      is the observable signature of the level losing meaning, and is measurable now.

  Specific risks: If a zero-action Critical flag is not a control, then (i) the system holds a
    false belief about its own safety margin — it believes it has a top-severity escalation path
    and it does not, which is worse than knowing it has none, because a believed-in control
    suppresses the search for a real one; (ii) the damage is cumulative and irreversible in the
    short run: each unactioned Critical instance further devalues the level, so by the time a
    genuinely urgent condition arrives the level's operational meaning is already "no action
    required," and it will be read that way; (iii) the effect generalises downward — the
    static-analysis literature finds that habitual suppression does not stay confined to the
    warnings that provoked it, so an ignored top level degrades the whole scale; (iv) the
    normalization pathway means the flag's *content* becomes accepted along with the flag —
    whatever condition is being flagged Critical is, six days in, on its way to being a known and
    tolerated feature of the system; (v) reflexively, this file is itself a document about a
    condition flagged Critical, filed into a register whose measured drain is zero
    (PRESUMPTION-712), which means the expected fate of this challenge is the same as the fate of
    the five flags it examines.

  Mitigations available: (1) Diagnose the zero rate before treating it — miscalibration,
    saturation and absent authority have different remedies and the current evidence does not
    distinguish them. (2) Couple the top severity to a named party with authority to act and a
    time-bounded response obligation; a level without both is a notification and should be
    renamed one. (3) Publish the action rate per severity level as a standing figure, so the
    level's operational meaning is visible next to its name — the single cheapest control
    available and it makes the presumption falsifiable. (4) Review the severity distribution
    periodically, the countermeasure the incident-management literature names, which would have
    caught this at instance two. (5) Separate the record-keeping function from the control
    function into distinct categories, because the drift is produced by their sharing a name. (6)
    Introduce an explicit escalation-on-repetition rule: a condition flagged at the top level
    more than N times without action must either be escalated outside the normal channel or
    formally accepted as a known condition — the second option is unattractive but it is honest,
    and it is what the normalization-of-deviance literature says happens by default and unspoken
    if no rule exists.

  Search scope: Comprehensive for alarm and alert fatigue, which supplies the mechanism, the
    scale and the finding that top-severity categories are not exempt; the specific percentages
    are relayed from abstracts and search summaries and are flagged as unverified. Comprehensive
    for severity inflation and classification drift, though that entire body of material is
    practitioner rather than peer-reviewed — it is unanimous and internally consistent, but no
    empirical study of severity drift was located and that is a real weakness in this file.
    Adequate for the normalization-of-deviance framing: Vaughan's work is well attested and
    correctly attributed here, but was reached through secondary treatments rather than the book,
    and no quotation is asserted. Not searched, and directly relevant: the human-factors
    literature on warning compliance and on the credibility of alarms as a function of prior
    false-alarm rate (the "cry wolf" effect, which has real experimental measurements and would
    replace the practitioner sources on drift with quantified ones), and the safety-science
    literature on escalation authority and stop-work authority specifically. Broader search
    recommended on the cry-wolf effect in particular — it is the quantified form of exactly this
    presumption and would likely make the challenge decisive.

  Recommendation: CHALLENGED
