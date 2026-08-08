SEARCH-FOR-PRESUMPTION-716:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-716
  Original statement: That a Critical severity flag which fires no action is
    still a control; sixth consecutive day at the top of the scale with an
    observed action rate of zero across the preceding five. Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-716
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read the severity level against the measured action rate of prior
        instances at the same level.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Incident severity practitioner literature — a consistent 2025-26
       consensus located across many independent sources this session
       (oneuptime.com, "How to Build Incident Severity Definitions," 30 January
       2026; Nova AI Ops, "Designing Alert Severity Levels: A Framework That
       Survives Contact with Production"; Uptime Labs, "Incident Severity
       Levels: How to Define and Get Them Right"; Giva; Last9; Atlas Systems;
       secure.com, "Incident Severity Levels Explained: Not Every Alert Is a
       Fire Drill"). [All practitioner; no peer-reviewed source located for this
       specific claim.] — Searched for support and found the direct denial,
       stated in almost the item's own terms. Severity inflation is described as
       the most common failure mode of severity frameworks; the natural drift is
       toward inflation because every author wants their alert taken seriously;
       and the stated consequence is that inflation degrades the signal value of
       the highest tiers, summarised as "when everything is critical, nothing
       is." Most decisively for this item, one located source states that a
       severity level without a clear response expectation is useless and that
       one must always define who gets paged and when. On that framing, a
       Critical flag with a measured response rate of zero is not a weak control
       — it is the definitional case of a non-control.
    2. The same literature, on calibration as a maintained property. — The
       recommended practice located is monthly review of the severity
       distribution to catch classification drift before it becomes a cultural
       norm, with quarterly calibration reviews of severity accuracy and
       consistency. This matters for the item's specific shape: six consecutive
       days at the top of the scale is precisely the distributional signal these
       reviews exist to catch, and by the located standard it should trigger
       recalibration of the scale rather than reassertion of the level.
    3. Near-miss reporting programme requirements (Umbrex; MangoApps; Safety
       Services Company; goaudits; etraintoday; OSHA near-miss reporting policy
       template, osha.gov). — The closest thing to a FOR case, and it fails on
       its own terms. Safety science does credit *recording* independently of
       immediate remediation: a near miss is treated as proof that exposure
       already exists, near-miss rate is designated a leading indicator, and a
       high reporting rate is read as a positive cultural signal. So there is a
       real tradition in which flagging has value before action. But every
       located source in that tradition attaches the same condition and states
       it explicitly: if reports sit in files or emails without action, hazards
       remain unaddressed and the likelihood of an accident rises; and when near
       misses are reported and no action is taken, people stop reporting,
       because absence of feedback signals that reporting does not matter. The
       three stated requirements for a functioning programme are easy reporting,
       protected reporters, and predictable follow-up. A measured action rate of
       zero fails the third outright.
    4. Alarm fatigue — clinical monitoring literature located this session
       (AHRQ PSNet, "Reducing the Safety Hazards of Monitor Alert and Alarm
       Fatigue"; "Insights into the Problem of Alarm Fatigue with Physiologic
       Monitor Devices," PMC 4206416 [authors NOT captured or verified]; Cvach,
       M., "Monitor Alarm Fatigue: An Integrative Review," Biomedical
       Instrumentation & Technology 46(4):268, DOI 10.2345/0899-8205-46.4.268
       [year unconfirmed]; ScienceDirect, "A call to alarms: Current state and
       future directions in the battle against alarm fatigue," S0022073618304722
       [authors unverified]). — The measured version of the same finding, in the
       field that has studied it hardest. Reported non-actionable alert rates
       exceed 70% across physiological monitoring and 80-99% of ECG monitor
       alarms are described as false or clinically insignificant. [Figures from
       returned search summaries of papers I did not open; direction is
       consistent across four independent sources but the specific percentages
       are UNVERIFIED.] The documented endpoint is not neutrality: clinicians
       desensitise, silence alarms at the central station without checking the
       patient, or disable them permanently, and adverse events follow when a
       true instability is not attended to despite the alarm. A high-severity
       signal with a zero action rate is described here as actively degrading
       the channel it uses.
    5. Signal detection framing in the same alarm literature. — Located as the
       theoretical grounding and it is unfavourable. The effectiveness of an
       alerting system is described as set by both the stringency of the
       decision threshold and the discriminability index d' — the overlap
       between normal and abnormal parameter distributions. A tier that fires
       every day carries no discriminating information by construction,
       regardless of the threshold's label, because a signal present in all
       states distinguishes none of them.

  Strength of support: None

  Summary: No located source supports the proposition that a severity flag
    which produces no action is still functioning as a control, and the sources
    that come closest to supporting it deny it in explicit terms. The incident
    severity literature treats severity inflation as the standard failure mode,
    names its cause (everyone wants their alert taken seriously) and its effect
    (when everything is critical, nothing is), and states directly that a
    severity level without a defined response expectation is useless — which is
    the item's condition exactly. The near-miss tradition is the one place where
    recording is credited independently of remediation, and it was the FOR case
    I most expected to carry; it does not, because every source in it makes
    predictable follow-up a named requirement and warns that unactioned reports
    both leave hazards live and cause reporting to stop. The alarm-fatigue
    literature converts this into measurement, with non-actionable rates above
    70% and a documented progression to desensitisation, silencing and missed
    true signals — the finding being that unactioned high-severity signals do
    not sit inert but degrade the channel for the ones that matter. The signal
    detection framing supplies the reason in one line: a tier that fires in
    every state has no discriminability, so the label at the top of the scale
    carries no information. The item's own arithmetic — six consecutive days at
    the top, zero actions across the preceding five — is the pattern the
    calibration guidance exists to catch, and the located recommendation for
    that pattern is to recalibrate the scale, not to reassert the level.

  Caveats: The severity-framework sources are entirely practitioner material
    from 2025-26 and their near-verbatim agreement may reflect a shared upstream
    rather than independent confirmation; I found no peer-reviewed treatment of
    severity inflation despite looking. Source 4's author attributions are
    uncertain and its percentages come from summaries of papers I did not open;
    they should be verified before any downstream use. The alarm-fatigue
    transfer is to a domain with a human operator under time pressure and
    physical consequences, which is not obviously C2A2's situation, and the
    desensitisation mechanism specifically depends on a human attention budget
    that an automated consumer may not have — this weakens source 4 more than
    the consistency of its findings suggests. Two arguments in the presumption's
    favour survive the search unrefuted and should be recorded. First, five days
    is a short window and an action rate of zero over five instances is
    compatible with a low but non-zero true rate; the item's inference is itself
    a small-sample inference. Second, a flag may serve a record-keeping or
    accountability function distinct from triggering action — establishing that
    the condition was known at the time — and none of the located sources
    address a severity scale used deliberately as a ledger rather than as a
    trigger. That is the strongest available defence and no evidence was found
    either way on it.

  NOVELTY-FLAG:
    Item: PRESUMPTION-716
    Searched: Incident severity level design, calibration and inflation;
      alarm and alert fatigue including non-actionable rates and their
      consequences; near-miss reporting and the value of recording without
      remediation; escalation authority and response expectations; signal
      detection framing of alerting thresholds.
    Finding: No literature was located that addresses the specific case of a
      severity scale operated without any authority to act — that is, a system
      in which the flagging party is structurally unable to trigger the response
      the level names. The located sources all assume the escalation path exists
      and ask whether it is being calibrated or fatigued; none considers the
      case where it is absent by construction.
    Implication: C2A2 may be operating a severity scale in a configuration the
      literature does not model. This is a gap worth naming precisely because it
      cuts against the presumption rather than for it: the absence of literature
      is not permission, and the nearest analogues all indicate that severity
      without response expectation degrades rather than preserves the signal.
    Recommended status: NOVEL (as a gap in coverage, not as a validated design)

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Adequate on the practitioner side, thin on the peer-reviewed
    side. Concepts searched: alarm systems and alert fatigue, non-actionable
    alarm rates and downstream consequences; severity scale calibration, drift
    and inflation; escalation authority and response expectations; near-miss
    reporting as a leading indicator and its stated conditions; signal detection
    theory as applied to alarm thresholds. Not searched, and recommended: the
    normal accidents and high-reliability organisation literature (Perrow;
    Weick and Sutcliffe), which addresses warnings that were logged and not
    acted on as a recurring accident precursor and would be the most rigorous
    available treatment of this exact claim.
