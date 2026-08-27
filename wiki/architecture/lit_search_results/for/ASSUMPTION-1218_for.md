SEARCH-FOR-ASSUMPTION-1218:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1218
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 4 of 14 — Priority Medium
  Original statement: "Two STALE-WATCH-FLAGs raised (**first in this agent's history**), both
    recommending **Escalate to Tom**, not Cancel and not Continue." WATCH-002: "every retrieval route
    exhausted"; WATCH-003: "isn't separable from the INTEGRITY FLAG; one ruling closes it either way."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1218
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the C2A2 deferred action monitor — both weekly checks fired (count 5 → 6),
        both conditions unmet. The option set the agent named itself (Escalate / Cancel / Continue)
        was preserved, since the assumption is in the *selection* and not in the reasoning. Recorded
        neutrally: the agent had three terminal options and chose the one that requires an attended
        decision, on the fiftieth-plus consecutive unattended day; the choice may be correct and is
        also the choice that cannot resolve under current conditions.
      15a: Searched for supporting literature
    Current status: UNTESTED (entering 15a); 15a result SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch unavailable to this run; **all sources
    SNIPPET-ONLY.**
    Queries covered: (a) escalation policy design — unacknowledged alerts, time-based promotion,
    escalation chains; (b) ITIL functional vs. hierarchical escalation and the authority criterion;
    (c) ISA-18.2 alarm rationalisation — the requirement that every alarm have a defined operator
    response; (d) alarm shelving as a time-bounded, audited suppression with automatic re-arm;
    (e) auto-close / stale-ticket policies.
    Assessment: **good coverage of the terminal-state question, poor coverage of the
    unresponsive-channel question.** Limbs NOT covered, and they matter: (i) I found **no literature
    at all on escalation into a channel that does not answer** — every escalation source I read
    presupposes that some tier eventually responds, and the failure mode they model is *slow*
    response, not *absent* response. This is the queue's second explicit question and I could not
    answer it. (ii) I did not search the human-factors literature on unattended/lights-out operation
    or on autonomy handoff when the supervisor is absent, which is where an answer would most likely
    live. (iii) I did not search the workflow/BPM literature on deadline expiry and escalation
    timeouts in long-running processes, nor the medical "watchful waiting" / diagnostic-stopping-rule
    literature, either of which could speak to when a watch should expire.

  Supporting evidence found: Yes

  Sources:
    1. "Escalation Management ITIL: Process, Types & Best Practices." NovelVista.
       https://www.novelvista.com/blogs/it-service-management/escalation-management-itil
       — The strongest support for the *selection* 14a recorded. ITIL distinguishes **functional**
       escalation (pass to a more specialised technical tier, on skill grounds) from **hierarchical**
       escalation (move up the management chain when authority is required). Hierarchical escalation
       is the prescribed action when "a decision requires authority that the technical team doesn't
       have." Both of the monitor's flags are of that kind: WATCH-002 has exhausted every retrieval
       route (so no functional escalation remains), and WATCH-003 explicitly turns on a *ruling*,
       which is an authority question by definition. On this framework "Escalate" is not one of three
       equally-weighted options — it is the specified terminal state for this exact condition.
       Practitioner ITSM source, not peer-reviewed. SNIPPET-ONLY.
    2. Atlassian. "Escalation policies for effective incident management."
       https://www.atlassian.com/incident-management/on-call/escalation-policies
       — Corroborates the same two-type distinction and the design pattern of tiered chains with
       time-based promotion. SNIPPET-ONLY.
    3. "Incident Escalation Process Explained with Examples." ITSM Docs.
       https://www.itsm-docs.com/blogs/it-operations-playbook/incident-escalation-process-explained-with-examples
       — Corroborating practitioner statement of the same taxonomy; notes the two types are not
       mutually exclusive and can fire together on one event. SNIPPET-ONLY.
    4. incident.io. "Escalation policy anti-patterns: Common mistakes that increase alert fatigue."
       https://incident.io/blog/escalation-policy-anti-patterns
       — Relevant as the nearest located treatment of escalation *failure*, though it frames the
       failure as alert fatigue at the receiving end rather than an absent receiver. SNIPPET-ONLY.
    5. "Alarm Management Best Practices in SCADA: A Guide with Ignition." OperaMetrix.
       https://www.operametrix.com/en/blog/alarm-management-best-practices-scada-ignition/
       — Documents **shelving** as the standard third option that 14a's monitor did not have:
       shelving temporarily suppresses a known, non-actionable alarm for a *defined period*, is
       "time-limited and fully audited," carries a clear visual indicator, and **automatically returns
       to active status when the shelving period expires**. This is a fourth terminal state — neither
       Escalate, Cancel nor Continue — and it is precisely designed for a watch that cannot resolve
       now but should not be discarded. Strong analogous support for the existence of a bounded-defer
       state. SNIPPET-ONLY.
    6. ANSI/ISA-18.2, "Management of Alarm Systems for the Process Industries," as summarised in:
       PAS/ISA, "Understanding and Applying the ANSI/ISA 18.2 Alarm Management Standard,"
       https://www.isa.org/getmedia/55b4210e-6cb2-4de4-89f8-2b5b6b46d954/PAS-Understanding-ISA-18-2.pdf ;
       Emerson, "Alarm Rationalization" white paper (Oct 2019),
       https://www.emerson.com/documents/automation/white-paper-alarm-rationalization-deltav-en-56654.pdf ;
       Rockwell Automation, "Alarm Rationalization and Implementation,"
       https://literature.rockwellautomation.com/idc/groups/literature/documents/wp/proces-wp015_-en-p.pdf
       — The standard defines an alarm as an indication of a condition **"requiring a response,"** and
       the rationalisation stage requires that for each candidate alarm the consequence, response time
       and **operator action** be documented; alarms that cannot justify a defined response are
       eliminated or reclassified as events rather than alarms. This is a genuine two-edged finding
       and I report both edges. It supports 14a's choice insofar as the monitor's flags *do* name a
       required response (a ruling by a specific person). It equally supports the WONTWATCH option:
       a watch whose response cannot be performed fails the rationalisation criterion and should be
       demoted to an event or removed. SNIPPET-ONLY.
    7. "Alarm Management in SCADA: ISA-18.2 Implementation Guide." iFactory.
       https://ifactoryapp.com/blog/alarm-management-scada-isa-18-2 — corroborating summary of the
       rationalisation criterion. SNIPPET-ONLY.
    8. "How to Build Escalation Policies." OneUptime (2026-01-30).
       https://oneuptime.com/blog/post/2026-01-30-escalation-policies/view
       and "What is Escalation policy?" SRE School. https://sreschool.com/blog/escalation-policy/
       — Both describe the standard structure: tiered chains with defined promotion windows
       ("engineer at 10 minutes, team lead at 30"), explicitly to prevent alerts going stale. Note
       what this presupposes and what C2A2 lacks: **a further tier above the one being escalated to.**
       SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: On the first half of the question — is escalation the right terminal state for a monitoring
    task whose retrieval routes are exhausted — the literature supports the monitor's selection
    fairly cleanly. ITIL's standing distinction is that *functional* escalation applies when more
    skill or a different specialism is needed, and *hierarchical* escalation applies when the required
    decision needs authority the responder does not hold (source 1). WATCH-002 reports every retrieval
    route exhausted, which closes the functional path; WATCH-003 turns on a "ruling," which is an
    authority question by construction. Under that framework "Escalate" is not one of three
    equally-plausible options but the specified terminal state, and Cancel would be premature
    (nothing has been decided) while Continue would be a null action (no new route exists). On the
    second half — the terminal-state *inventory* — the alarm-management literature supplies an option
    the monitor did not have: **shelving**, a time-bounded, audited, automatically re-arming
    suppression designed exactly for a known, currently non-actionable condition (5). ISA-18.2's
    rationalisation criterion cuts both ways and is reported as such: an alarm must have a defined
    response, which the flags do have (a ruling), but which under current conditions cannot be
    performed — and the standard's own remedy for a response that cannot be performed is demotion or
    removal, not escalation (6).

  Caveats: (1) All sources SNIPPET-ONLY; sources 1–5, 7 and 8 are practitioner/vendor writing rather
    than peer-reviewed research, and the ISA-18.2 material is read through third-party summaries
    rather than the standard itself. (2) **The central caveat, and it is severe: every escalation
    source located assumes the escalation target responds.** Escalation policies are built as chains
    with promotion windows precisely so that a non-responding tier is bypassed to a *higher* tier.
    C2A2 has no tier above Tom. The literature therefore validates the *form* of the monitor's action
    while being silent on the condition that actually obtains — a terminal escalation into a channel
    unattended for fifty-plus days. I could not find any treatment of this and I record it as a real
    gap, not a soft one. (3) Domain transfer: alarm management and ITSM both presume a staffed
    operations function on a duty roster; C2A2 is a scheduled autonomous system with a single
    unrostered human. The transfer conditions for these standards are not met. (4) The
    rationalisation criterion (6) arguably tells against the assumption more than for it, and 14a's
    own neutral framing anticipates this: the choice "may be correct and is also the choice that
    cannot resolve under current conditions." Nothing found resolves that tension. (5) I did not find
    literature on when a *watch* (as opposed to an alarm or an incident) should expire; the closest
    is shelving, which is a suppression, not an expiry.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1218
    Supported sub-claims: (i) that escalation is the prescribed terminal action when the required
      decision needs authority the responder lacks and no further specialist route exists —
      hierarchical escalation, ITIL; (ii) that a defined, time-bounded, auto-re-arming defer state
      (shelving) is standard practice and constitutes a fourth option beyond Escalate / Cancel /
      Continue; (iii) that a monitored condition must have a documented response, response time and
      responsible actor to justify its continued existence as an alarm.
    Unaddressed sub-claim: **escalation into an unresponsive channel.** This is the queue's own second
      question and the search returned nothing on it. Every located escalation framework is built on
      the premise of a higher tier that can be reached when the current one does not answer; none
      models a terminal tier that does not respond, and none prescribes what a monitoring agent
      should do on the fiftieth consecutive unattended day. The nearest adjacent literature is alert
      fatigue, which concerns a receiver who is present but desensitised — a different failure.
    Implication: the specific configuration — an autonomous monitor whose only escalation target is a
      single absent human, with no tier above and no expiry rule — appears to be undescribed. If C2A2
      formulates a rule for it (e.g. escalate once, then shelve with a defined re-arm, then WONTWATCH
      with a recorded reason), that rule would be an original contribution rather than an application.
      Recommended status for this sub-question: NOVEL.
