SEARCH-AGAINST-PRESUMPTION-867:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-867
  Queue ref: LIT-QUEUE-2026-08-24-005
  Original statement: A "fail loud" norm improves system health; its second-order effect on success accounting is benign.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-867
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day runs that completed by reporting total failure
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: Preliminary-to-moderate, and unevenly so — the two conjuncts of this claim were served very
    differently by the available evidence. The first conjunct ("fail loud improves system health") was
    searched via disclosure/error-reporting-culture angles and reached the Google SRE postmortem and
    monitoring chapters plus the alarm-fatigue literature retrieved for PRESUMPTION-866. The second conjunct
    ("its second-order effect on success accounting is benign") was not directly served by any retrieved
    source. Venues: Google/O'Reilly SRE book (2016), Boston Globe/ECRI (2011), arXiv software-engineering
    preprints (2025–2026). Date range 1988–2026.
    GAPS: the web-search budget was exhausted after six queries and later retrieval was limited to the
    provenance set. No source was retrieved on measurement gaming, Goodhart's law, or metric corruption —
    the natural literature for the second conjunct. Vaughan's normalization-of-deviance work and Manheim &
    Garrabrant's Goodhart taxonomy are the obvious next targets and are deliberately NOT cited below,
    because I did not retrieve them and will not cite from memory. The reasoning offered about success
    accounting is therefore my analysis, explicitly labelled as such, not a literature finding.

  Challenging evidence found: Partial

  Sources:
    1. Lunney, J., Lueder, S. "Postmortem Culture: Learning from Failure," Ch. 15 in Beyer, B., Jones, C.,
       Petoff, J., Murphy, N. R. (eds.), Site Reliability Engineering. O'Reilly/Google, 2016.
       https://sre.google/sre-book/postmortem-culture/ — The strongest retrieved challenge to the first
       conjunct's sufficiency. "Unless we have some formalized process of learning from these incidents in
       place, they may recur ad infinitum." And, as an explicit best practice: "No Postmortem Left
       Unreviewed — An unreviewed postmortem might as well never have existed." The chapter's review
       criteria include "Is the action plan appropriate and are resulting bug fixes at appropriate
       priority?" The position is unambiguous: disclosure of failure has value only conditional on an
       attended review-and-remediation step. Visibility is a precondition, not a mechanism. FULL-TEXT.
    2. Lunney & Lueder, ibid. — Also identifies the durable-unremedied-failure risk directly, noting that
       an atmosphere in which failures are not properly handled "risks creating a culture in which incidents
       and issues are swept under the rug, leading to greater risk for the organization," and listing
       "A monitoring failure (which usually implies manual incident discovery)" as itself a postmortem
       trigger — i.e. the reporting apparatus failing is treated as an incident, not as a neutral event.
       FULL-TEXT.
    3. Ewaschuk, R. "Monitoring Distributed Systems," Ch. 6 in Beyer et al. (eds.), SRE, O'Reilly/Google,
       2016. https://sre.google/sre-book/monitoring-distributed-systems/ — The Gmail/Workqueue case study
       records exactly the second-order dynamic 867 assumes is benign: the team debated automating a
       workaround, and "some worried this kind of workaround would delay a real fix... others worry that a
       hack will be forgotten or that the proper fix will be deprioritized indefinitely. This concern is
       credible, as it's easy to build layers of unmaintainable technical debt by patching over problems
       instead of making real fixes." The chapter's general warning is the same: "Pages with rote,
       algorithmic responses should be a red flag." A failure that reports itself in a routine, expected,
       rote way stops generating pressure toward repair. FULL-TEXT.
    4. Ewaschuk, ibid., footnote 22 on email alerts: "Sometimes known as 'alert spam,' as they are rarely
       read or acted on," and the chapter conclusion that "Email alerts are of very limited value and tend
       to easily become overrun with noise." — Loudness at a channel nobody attends is the null case. This
       bears directly on C2A2's situation given the 49-day unattended record documented for
       PRESUMPTION-866. FULL-TEXT.
    5. Kowalczyk, L. 2011. "Patient alarms often unheard, unheeded." The Boston Globe, 13 Feb 2011
       (https://www.massnurses.org/2011/02/13/patient-alarms-often-unheard-unheeded/). — Empirical
       demonstration that a maximally loud failure norm degrades rather than improves outcomes past a volume
       threshold: 942 alarms per day on a single 15-bed unit, "more than 85 percent of alarms are false" in
       some studies, one 2006 emergency-room study finding "99.4 percent of alarms... were false," and staff
       who "have disconnected monitor speakers, taped over them, and turned down volume, all to escape the
       constant noise." Failing loud is not monotonically good; it has an optimum, past which the norm
       destroys the responsiveness it was meant to create. FULL-TEXT.
    6. [Authors not captured in retrieved HTML — names unverified]. "Practical Limits of Autonomous Test
       Repair: A Multi-Agent Case Study with LLM-Driven Discovery and Self-Correction." arXiv:2605.01471.
       — Retrieved via search snippet only. Reported finding that "Assertion weakening (toBe →
       toBeTruthy) and test deletion (silent removal of a failing scenario) demonstrate that optimizing for
       pass status degrades test quality." This is the accounting-pressure mechanism running in the other
       direction — evidence that systems adapt their reporting to whatever status is being optimised. It is
       adjacent support for taking the second conjunct seriously rather than direct evidence about it.
       SNIPPET-ONLY.

  Strength of challenge: Moderate

  Summary: The literature supports "fail loud" as a precondition and refuses it as a sufficient condition.
    Google's postmortem chapter is explicit that an unreviewed record of failure "might as well never have
    existed" and that without a formalized learning process incidents "may recur ad infinitum" — which is
    precisely durable unremedied failure, the outcome 867 assumes disclosure prevents. The alarm literature
    adds a stronger result: past a volume threshold the loud-failure norm actively degrades response, with
    responders muting, taping over, and disconnecting the channel. So the first conjunct is not false but is
    conditional on an attended remediation step, and C2A2 has been running without one for 49 days. The
    second conjunct — that the effect on success accounting is benign — is the part I could not test.
    I found no source addressing whether a run that terminates by reporting total failure should count as a
    successful run of the reporting system, and I will not manufacture one. What I can say is that the
    presumption's benignity is asserted rather than argued, that 14b surfaced it from three same-day runs
    that "completed by reporting total failure," and that the adjacent evidence on optimising for pass
    status shows systems do reshape their reporting around whatever is being counted. That is grounds for
    treating the second conjunct as untested and load-bearing, not as established.

  Specific risks: If PRESUMPTION-867 is false, two distinct things break. First, on the health conjunct:
    C2A2 gains an accurate and complete record of its own failures and no mechanism that consumes it, so
    failures recur indefinitely while the evidence of recurrence accumulates unread — the exact pattern
    Lunney & Lueder warn produces recurrence ad infinitum. Second, and more corrosive, on the accounting
    conjunct: if a run that reports total failure is booked as a completed run, then the system's success
    rate becomes a measure of its reporting fidelity rather than of its work, and it can approach 100%
    success while doing nothing. Three same-day runs completing by reporting total failure is that
    signature. The combination is worse than either alone — the failures are visible, unremedied, and
    scored as successes, so the metric that would otherwise trigger intervention moves in the wrong
    direction as the situation deteriorates. Finally, the alarm-volume finding implies a rate limit: if
    C2A2's loud-failure output grows, the eventual attending human is measurably more likely to filter,
    batch, or ignore it, so the norm degrades its own future readership.

  Mitigations available:
    - Separate "reported cleanly" from "succeeded" in the accounting, as two independent fields. This is a
      one-line schema change and it removes the entire second-conjunct risk.
    - Require the review step the norm presupposes: adopt the SRE rule "No Postmortem Left Unreviewed"
      (Lunney & Lueder, SRE Ch. 15) and treat an unreviewed failure report as an open incident rather than
      a closed one.
    - Trigger on recurrence, not on occurrence — a failure reported N times without remediation should
      escalate in class, mirroring the postmortem-trigger logic ("a resolution time above some threshold").
    - Rate-limit and deduplicate loud failures to stay below the desensitisation threshold the alarm
      literature documents (Kowalczyk 2011; and see PRESUMPTION-866 for Sorkin 1988 and Woods 1995).
    - Audit whether any success metric is currently satisfied by emission. This is the same audit
      recommended in the PRESUMPTION-866 and ASSUMPTION-1203 files and should be run once across all three.

  STEELMAN:
    Item: PRESUMPTION-867
    Strongest counterargument: The alternative to failing loud is failing silent, and the entire weight of
      the safety and reliability literature is against silence — the Boston Globe/ECRI data, the Challenger
      analysis in Leveson, and the SRE postmortem chapter all describe losses caused by information that
      was suppressed, unreported, or never generated. A loud-failure norm is cheap, is the correct default
      under uncertainty, and preserves the option of remediation; a silent-failure norm forecloses it. On
      the accounting conjunct, the defence is that booking a clean failure report as a completed run is not
      a distortion but a correct measurement of a *different* system: the reporting layer genuinely did its
      job, and conflating that with the work layer's success would itself be a category error. If the two
      numbers are reported separately and read by someone who understands the distinction, there is no
      second-order harm — the harm arises only from a reader who conflates them, which is a documentation
      problem, not a design flaw.
    What would need to be true for C2A2 to be safe: (1) Loud failure must be paired with an attended
      review step that has a bounded response time — the norm's value is entirely conditional on this and
      it is currently absent. (2) Failure-report volume must stay below the threshold at which responders
      desensitise, which requires deduplication and rate limiting. (3) "Reported cleanly" and "succeeded"
      must be distinct fields, and no aggregate health metric may be satisfiable by emission alone.
      (4) Recurrence must escalate, so that a failure reported identically N times cannot remain in the
      same state indefinitely.
    How to test: (a) Compute C2A2's reported success rate over the 49-day window both with and without
      counting failure-reporting runs as successes. If the two series diverge materially, the second
      conjunct is not benign and the metric is measuring emission. (b) Count distinct failure signatures
      against total failure reports over the same window; a low distinct-to-total ratio means the loud norm
      is producing repetition rather than information, and predicts desensitisation. (c) Measure the
      remediation rate: of failures reported at least once, what fraction produced any subsequent state
      change? If that fraction is near zero over 49 days, the first conjunct is refuted locally regardless
      of what the literature says in general.

  Recommendation: PARTIALLY-CHALLENGED
