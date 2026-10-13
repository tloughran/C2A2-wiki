SEARCH-FOR-PRESUMPTION-1127:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1127
  Original statement: What does the alarm-fatigue literature (clinical alarms, SRE alerting) say about repeated
    non-actionable alerts, and which escalation or auto-remediation policies reduce it?

  Premise tested (unstated, inferred by 14b): Repeating the same non-actionable alert desensitises the reader. C2A2
    should therefore escalate, consolidate, or auto-remediate recurring alerts rather than re-emit them unchanged each
    cycle.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1127
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-12 transcripts where the same alert recurred across runs without action; queued
        2026-10-12
      15a (2026-10-13): 3 web searches (clinical non-actionable alarm rates / Drew 2014 / Bonafide 2015; Google SRE
        actionable-paging guidance; alarm-reduction interventions and auto-remediation). No fetches; evidence from
        search-result summaries. See also prior result ASSUMPTION-1766_for.md (rule/alert consolidation), which
        overlaps.
    Current status: SUPPORTED (Strong for the harm; Moderate for specific remedies; Weak for auto-remediation)

  Search scope: PRELIMINARY. Clinical alarm literature, SRE practitioner canon, and vendor auto-remediation material.

  Supporting evidence found: Yes

  Sources:
    1. Drew, B.J. et al., 2014. "Insights into the problem of alarm fatigue with physiologic monitor devices."
       PLoS One 9(10):e110274. [search-result summary] 2.56M alarms for 461 ICU patients in 31 days (about 187
       audible alarms per bed per day). 88.8% of an annotated arrhythmia-alarm subset were false positives. Causes
       included non-actionable events and poor settings. Relevance: scale of the non-actionable problem.
       (The "72%" figure in the query was NOT confirmed.)
    2. Bonafide, C.P. et al., 2015. J Hosp Med (paediatric alarms). [search-result summary] 87.1% (PICU) and 99.0%
       (ward) of alarms were non-actionable. Response time increased with the number of non-actionable alarms in the
       preceding 120 minutes. Relevance: direct empirical support for the dose-response of desensitisation to
       repeated non-actionable alerts.
    3. Beyer, B. et al. (eds), 2016. Site Reliability Engineering, ch. "Monitoring Distributed Systems" (Google),
       as summarised in SREcon16 slides (Rabenstein) and SoundCloud's "Alerting on SLOs". [search-result summary]
       Every page must be actionable and urgent. Responders can sustain urgency only a few times a day. Causes go to
       dashboards or tickets, symptoms to pages. Relevance: SRE canon matches the premise. Book text not read
       directly.
    4. Whalen, D.A. et al. (Boston Medical Center, ~2014; AHRQ innovation profile). [search-result summary]
       Reclassifying alarm tiers and removing self-resetting alarms cut daily audible alarms from 12,546 to 1,424,
       with no adverse events reported and fewer Code Blues. Relevance: intervention evidence that triage and
       escalation tiers reduce volume safely. Single site. (The "Welch 2011" attribution in the query was not
       confirmed; the lead author appears to be Whalen.)
    5. Michels et al., 2025. "Alarm fatigue in healthcare: a scoping review..." BMC Nursing. [search-result summary]
       Defines alarm fatigue as desensitisation from repeated frequent or non-actionable alarms. Lists mitigation
       strategies including setting customisation, delays, and escalation.
    6. Alarm-delay studies (adaptive time-delay algorithm, UKE Hamburg; simulation study showing a 10 s delay removes
       more than 50% of alarms). [search-result summary] Positive predictive value rose from 28% to 46% in one
       retrospective study. The authors say prospective safety proof is still needed.
    7. Auto-remediation / self-healing (Virtuslab maturity guide, vendor blogs). [search-result summary]
       Recommends fingerprinted, validated runbook automation with an escalation path when self-healing fails. No
       independent peer-reviewed outcome study found. Quantitative claims (e.g. "50% fewer pages") are unsourced or
       vendor claims.

  Strength of support: Strong (repeated non-actionable alerts cause desensitisation); Moderate (triage, tiering,
    delays, consolidation reduce volume); Weak (auto-remediation outcomes)

  Summary: Clinical and SRE literatures agree that most alerts in poorly tuned systems are non-actionable, and that
    exposure to them slows or blunts response in a dose-dependent way (Bonafide 2015). SRE doctrine requires every
    page to be actionable and moves everything else to tickets or dashboards. Interventions that reclassify and
    escalate alerts (BMC) or add delays show large volume reductions without reported harm. Auto-remediation is
    widely recommended for known, repeatable failure patterns, but its evidence base is practitioner and vendor
    material. The C2A2 stance (escalate or auto-fix recurring alerts, don't re-emit them) is consistent with this.

  Caveats: (i) In C2A2 the "responder" is partly agents, which do not fatigue, and partly one human reviewer.
    Desensitisation applies to the human end. For agents, the analogue is that repeated items dilute attention and
    context, which is plausible but not studied. (ii) Intervention studies are single-site QI designs, some
    vendor-sponsored. (iii) Delays and suppression trade against missed true events. (iv) Auto-remediation can mask
    the root cause, so logging remediations is recommended.

  NOVELTY flag: None for the principle. Partial for applying it to an unattended agent pipeline with a single human
    reader.

  Recommendation: SUPPORTED (Strong for the harm; Moderate for the remedies).
