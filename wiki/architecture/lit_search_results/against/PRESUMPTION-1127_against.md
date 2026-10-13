SEARCH-AGAINST-PRESUMPTION-1127:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1127
  Original statement: [unstated] What does the alarm-fatigue literature (clinical alarms, SRE alerting)
    say about repeated non-actionable alerts, and which escalation or auto-remediation policies reduce
    it?
  Under test: the premise that repeated non-actionable alerts cause fatigue, and that fewer, escalated
    or auto-remediated alerts fix it. I searched for evidence that (a) the fatigue mechanism is
    under-tested, (b) alarm-reduction interventions have weak outcome evidence, and (c) suppression or
    auto-remediation hides real faults.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output for this item. I did consult my own prior 15b file
    PRESUMPTION-1121_against.md (alert-uptake metrics) to avoid duplication.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1127
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-12): Inferred from 2026-10-12 transcripts, where the same non-actionable flag repeated
        across runs.
      15b (2026-10-13): Searched for challenging literature. 3 searches: systematic reviews of
        alarm-fatigue interventions (Winters 2018, Paine 2016); critiques of the alarm-fatigue concept
        and habituation evidence; suppression and auto-remediation risks (SRE practitioner sources). No
        fetch.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Snippets and review summaries only. SRE material is practitioner or
    patent, not peer-reviewed.
  Search scope: preliminary (3 searches, 0 fetches). I could not verify Lewandowska 2020 or Kristensen
    et al. beyond citation stubs.

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Winters BD, Cvach MM, Bonafide CP, Hu X, et al. 2018. "Technological Distractions (Part 2): A
       Summary of Approaches to Manage Clinical Alarms With Intent to Reduce Alarm Fatigue." Crit Care
       Med 46(1). [snippet] Of the 62 usable articles, "no study used or developed a clear definition
       of 'alarm fatigue'." Paine CW et al. 2016 (J Hosp Med, "Systematic Review of Physiologic Monitor
       Alarm Characteristics and Pragmatic Interventions") [snippet] found most interventions were
       multicomponent and heterogeneous, with no meta-analysis possible. Widening parameters and alarm
       delays were judged "promising but still unproven". Bearing: the claim that reducing alarms fixes
       fatigue rests mostly on before/after studies that count alarms, not missed events or harm.
    2. Alarm fatigue scoping review, 2024/2025 (PMC12181921, "Alarm fatigue in healthcare: a scoping
       review of definitions, influencing factors, and mitigation strategies"). [snippet] There is no
       harmonised definition, and measurement is mostly self-report. Kristensen et al. are cited as
       arguing the field focused "solely on reducing the number of alarms, based on a premise of
       inferred causality". A conceptual-model study reported that for nurse response time "alarm
       fatigue plays no role, only working conditions and staff individuality". An FRA locomotive pilot
       found no habituation (small sample). Bearing: the mechanism (alert count → desensitisation) is
       contested. If response failures are driven by workload and ownership, cutting alert volume
       treats the wrong variable.
    3. SRE suppression and auto-remediation sources (Rootly 2025; DrDroid; USENIX SREcon17 EMEA
       Jalleda; US patent 11240263). [snippet, practitioner] Aggressive filtering creates "blind spots".
       Teams that mute flaky checks then miss real incidents. One auto-remediation design creates a
       suppression rule for events judged false positives, so a recurring real fault can be silenced
       permanently. Bearing: auto-remediation turns a visible repeating alert into an invisible
       repeating fault, which is the silent-failure problem of ASSUMPTION-1778.
    4. Huang et al. 2017 (fetched under 1778) [full text] §2.3: automated recovery (reboot) "kills,
       rather than heals". A detector-driven auto-fix looped and contributed to a cascading failure.
       Bearing: auto-remediation without diagnosis can make things worse.

  Summary: The literature supports the observation that most alarms are non-actionable (Paine: <1-36%
    actionable). It is much weaker on the remedy. Interventions are judged "promising but unproven".
    Outcome measures are mostly alarm counts, not detection of true events. The causal model linking
    alert count to fatigue is not even well defined, and at least one study attributes response failure
    to working conditions instead. In SRE, suppression and auto-remediation are documented ways to
    convert noise into silent failure. Reducing alert volume is an intermediate outcome, so the remedy
    is evaluated with exactly the kind of proxy PRESUMPTION-1124 warns about.

  Specific risks: (a) C2A2 suppresses or auto-closes the repeating flag, and the underlying condition
    persists unseen. (b) Success is measured as fewer alerts and not as true problems resolved. (c)
    Escalation to Tom adds load to the one human channel, which is already a bottleneck (cf. 2026-10-12
    flag on human-channel silence).

  Mitigations available: Measure each policy change by true events caught or missed, for example by
    replaying historical incidents. Every auto-remediation must log, count recurrences, and escalate
    after N recurrences instead of suppressing. Assign each alert class an owner. Treat a repeating
    non-actionable alert as a defect in the detector (fix or retire it), not as noise to filter.

  STEELMAN:
    Item: PRESUMPTION-1127
    Strongest counterargument: Alarm fatigue is one of the most cited and least operationalised
      constructs in safety science. The reviews find no agreed definition, interventions graded as
      unproven, and outcomes counted in alarms rather than harm. Some evidence puts response failure
      down to workload and ownership. In software, the two remedies most likely to be adopted,
      suppression and auto-remediation, are the two that convert a noisy visible fault into a quiet
      invisible one. A policy judged by "fewer alerts" will look successful whether or not anything
      was fixed.
    What would need to be true for C2A2 to be safe: Each alert-policy change is evaluated against
      ground-truth fault detection. Every auto-remediation is counted and escalates after it recurs.
    How to test: Before adopting a suppression or remediation rule, replay the last 30 days of flags
      under the new rule. Count real defects that would have gone unseen.

  Boundary conditions identified:
    - Clinical evidence concerns human attention under continuous physiological alarms. C2A2's "reader"
      is mostly downstream agents plus one human, so the fatigue mechanism may transfer only to the
      human channel.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see SYSTEMIC-RISK-FLAG_2026-10-13_remedy-is-another-proxy_1778-1780-1124-1125-1127.md
