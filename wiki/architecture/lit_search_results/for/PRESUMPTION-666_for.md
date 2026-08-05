SEARCH-FOR-PRESUMPTION-666:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-666
  Original statement: That an agent reporting on other agents has a channel into
    their outcomes; a status report asserted "No failures to report" and named as
    successful a run that had terminated with no output, while a second health
    instrument three hours earlier reported the opposite from the commit record.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-666
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading two same-morning health reports against the
        transcript both describe, one asserting no failures and the other
        reporting the opposite from the commit record
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Simons, R., 1995. "Levers of Control: How Managers Use Innovative Control
       Systems to Drive Strategic Renewal." Harvard Business School Press. —
       Theoretical grounding for the legitimacy of the reporting form. Simons'
       diagnostic control systems are formal information systems used to monitor
       outcomes and correct deviations from preset standards, and they operate by
       management-by-exception: only significant deviations are escalated, so
       silence is a defensible encoding of "nothing to escalate." The framework
       is well established and widely applied. Its own stated boundary condition
       is that diagnostic systems work only if the reported data are accurate and
       complete, and cannot work where exceptions are masked by the collection
       procedure.
    2. Conant, R.C. & Ashby, W.R., 1970. "Every good regulator of a system must
       be a model of that system." International Journal of Systems Science
       1(2):89-97. — The nearest theoretical support for reporting from a model
       rather than from measurement: a regulator that is maximally successful and
       simple must be isomorphic with the regulated system, which licenses
       regulating (and reporting) via an internal model. The support is
       conditional in exactly the way that matters here: the theorem requires
       isomorphism with the system as it actually behaves, and a schedule is a
       model of intended execution, not of execution. Note the paper is
       contested — there is a live literature disputing whether it establishes
       what its title claims.
    3. Feedforward/open-loop control theory (standard treatment; e.g. Stanford
       EE392m Lecture 5, "Feedforward"; Control Engineering, "Open- vs.
       closed-loop control"). — Analogous support with a sharp condition.
       Feedforward control from a plant model is a legitimate and often superior
       strategy where the model is accurate and the disturbances are modelled;
       the standard result is that it is far more sensitive to model error than
       feedback, offers no guarantee that the commanded effect occurred, and
       requires a feedback correction to guarantee performance under model
       uncertainty. A schedule-derived status report is precisely open-loop
       reporting.
    4. Parasuraman, R. & Manzey, D.H., 2010. "Complacency and Bias in Human Use
       of Automation: An Attentional Integration." Human Factors 52(3):381-410.
       — Supports the mechanism by which an unfounded "No failures to report"
       survives review rather than the presumption itself. Complacency is
       greatest for aids of high and constant reliability, and operators of
       consistently reliable systems detect failures markedly less often;
       failures of omission (not acting on an accurate signal) are the
       characteristic form. This predicts that the second, contradicting health
       instrument three hours earlier would not have prompted re-examination.
    5. Keil, M., Smith, H.J., Iacovou, C.L. & Thompson, R.L., 2014. "The Dynamics
       of IT Project Status Reporting: A Self-Reinforcing Cycle Fueled by
       Uncertainty and Ambiguity." Journal of the Association for Information
       Systems 15(12). Related: Snow, A.P., Keil, M. & Wallace, L., 2007. "The
       effects of optimistic and pessimistic biasing on software project status
       reporting." Information & Management. — Reported in full per the
       no-cherry-picking rule: this is the closest empirical work on whether
       status reporters have and use a channel into outcomes, and it goes against.
       Status reports on high-risk IT projects are biased roughly 60% of the
       time, optimistic bias twice as likely as pessimistic, arising from the
       combined effect of error in ascertaining true status and bias in reporting
       perceived status. Snow and Keil separate exactly the two failure modes at
       issue: not knowing, and misreporting what is known.

  Strength of support: Weak

  Summary: Support exists for the *design form* — exception-based reporting from
    a model is a recognised and validated control pattern, given a model that
    tracks the system and a feedback path that corrects it. Simons' diagnostic
    control systems and the good-regulator theorem both license reporting through
    a model; both attach the same condition, that the model correspond to actual
    behaviour and that the data feeding it be complete. No source was found that
    supports inferring an outcome from a schedule in the absence of an outcome
    channel, and the control literature states the negative directly: open-loop
    command offers no guarantee that the commanded effect occurred. The one
    directly on-point empirical literature — Keil, Snow and colleagues on IT
    project status reporting — finds that reporters frequently do not have
    accurate status and, separately, distort what they do have. The strongest
    genuinely supportive finding for the C2A2 case is Parasuraman & Manzey's, and
    it supports the failure rather than the premise: a highly reliable status
    channel is precisely the one whose contradictions go uninvestigated.

  Caveats: The Keil/Snow corpus concerns human reporters with incentives to
    shade, which does not transfer directly to an automated aggregator — but the
    "error in ascertaining true status" component of their model does transfer,
    and it is the component at issue here. Parasuraman & Manzey concerns human
    monitoring of automation, so its application to one agent monitoring another
    is analogical. Source 3 is textbook and trade material rather than a specific
    research finding; feedforward control is uncontroversial background, not a
    contested claim needing a primary citation. Publication-bias note: the
    monitoring-tools literature that would most readily "support" schedule-derived
    status is overwhelmingly vendor material and was not treated as evidence.
    The support here would convert to real if the reporting agent were given a
    measured outcome channel — a commit record, an exit verdict, or a turn count —
    which is the standard feedback correction the control literature prescribes,
    and which the second health instrument in this very incident evidently had.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: schedule-derived versus
    outcome-derived status aggregation; open-loop and feedforward control and
    their model-accuracy conditions; the good-regulator theorem; management by
    exception and diagnostic control systems; automation-induced complacency and
    monitoring of highly reliable systems; project status reporting bias and
    information asymmetry. Not searched: observability-pipeline literature on
    span-status rollup; organisational silence and bad-news reporting outside the
    IS project literature.
