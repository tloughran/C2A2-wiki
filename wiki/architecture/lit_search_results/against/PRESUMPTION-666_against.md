SEARCH-AGAINST-PRESUMPTION-666:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-666
  Original statement: That an agent reporting on other agents has a channel into their
    outcomes — whereas a status report asserted "No failures to report" and named as successful
    a run that had terminated with no output, while a second health instrument three hours
    earlier reported the opposite from the commit record.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-666
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading two same-morning health reports against the transcript both
        describe; the two reports disagree, and the one derived from the commit record is the
        one that is right
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Snow, A.P. & Keil, M., 2002. "A Framework for Assessing the Reliability of Software
       Project Status Reports." Engineering Management Journal 14(2). — Decomposes status
       reporting into *error* (the reporter's fallibility in determining true status) and
       *bias* (slanting toward the favourable), with the combination termed *distortion*. The
       key structural claim is that a status report is a two-stage inference, not an
       observation, and that the first stage — knowing the true state — is the one that fails
       silently. C2A2's aggregator has no first stage at all.
    2. Keil, M., Smith, H.J., et al., 2014. "The Dynamics of IT Project Status Reporting: A
       Self-Reinforcing Cycle." Journal of the Association for Information Systems 15(12). —
       Status misreporting is not a one-off but self-reinforcing: an optimistic report reduces
       the scrutiny that would have caught the next one. Directly predicts that an unchallenged
       "No failures to report" makes the next such report more likely and less examined.
    3. Reported in this literature and widely replicated: status reports on high-risk IT
       projects are biased roughly 60% of the time, with optimistic bias about twice as common
       as pessimistic. [FIGURE SOURCED FROM SECONDARY SUMMARY — MIT Sloan Management Review,
       "The Pitfalls of Project Status Reporting" (Spring 2014, Keil et al.); primary study not
       directly retrieved. Treat the exact percentages as UNVERIFIED; the direction of the
       effect is well established.]
    4. Parasuraman, R. & Riley, V., 1997. "Humans and Automation: Use, Misuse, Disuse, Abuse."
       Human Factors 39(2):230-253. — *Misuse* is defined as over-reliance on automation
       producing failures of monitoring. The paper identifies automation reliability and
       consistency, and the salience of automation state indicators, as the factors governing
       whether a monitor is actually monitored. A consistently green status report is the
       lowest-salience state indicator possible: it never changes, so it carries no information
       and attracts no attention.
    5. Skitka, L.J., Mosier, K.L. & Burdick, M., 1999. "Does Automation Bias Decision-Making?"
       International Journal of Human-Computer Studies 51(5):991-1006; and Skitka, Mosier &
       Burdick, 2000. "Accountability and Automation Bias." IJHCS 52(4). — Establishes *errors
       of omission*: failures to respond to real events because the automated aid did not
       detect or indicate them. Crucially, the 1999-2000 work finds that training reduced
       *commission* errors but NOT omission errors — the class C2A2 is exposed to is the one
       that resists the obvious countermeasure. It also finds that participants without an
       automated aid outperformed those with a highly-but-imperfectly-reliable aid on a
       monitoring task: a mostly-right status agent can make outcomes worse than no status
       agent.
    6. Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R., 2017.
       "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS '17. — Differential
       observability formalises exactly the observed disagreement: two observers of the same
       system reach opposite conclusions because they are reading different signals. The
       resolution rule the paper implies is that the observer closer to the *effect* is the
       authoritative one — here, the commit-record instrument.
    7. Beyer, B., Jones, C., Petoff, J. & Murphy, N.R. (eds.), 2016. Site Reliability
       Engineering, Ch. 6 "Monitoring Distributed Systems." O'Reilly/Google. — The standing
       rule is to page on *symptoms*, not causes, i.e. on observed user-visible effect rather
       than on a component's self-description. A report that a run was scheduled, or that a run
       reported nothing bad, is neither a symptom nor a cause — it is a restatement of intent.
    8. Cemri, M., Pan, M.Z., Yang, S., et al., 2025. "Why Do Multi-Agent LLM Systems Fail?"
       arXiv:2503.13657; NeurIPS 2025 D&B Track. — One of the three top-level MAST categories
       is *task verification*: multi-agent systems fail characteristically because a verifying
       agent accepts an unverified claim from a peer. This is the multi-agent-specific version
       of the presumption and it is empirically the largest structural class after
       specification issues.
    9. "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a
       Production LLM Agent Runtime," arXiv:2606.14589 (2026). [AUTHORS UNVERIFIED — title,
       identifier and abstract content confirmed via search index; abstract page fetch was
       blocked.] — Its class (C), "error swallowing and dilution," is the mechanism by which an
       aggregator converts a missing outcome into a benign summary. Observed 28 times in an
       eight-week window in a ~40-scheduled-job runtime.

  Strength of challenge: Strong

  Summary: Nothing in the literature supports the presumption and three independent traditions
    attack it. The IS project-status literature (Snow & Keil; Keil et al.) establishes that a
    status report is an inference with two failure points, and that the reporter's *knowledge*
    of true state is the weak one — C2A2's aggregator is a limiting case in which that stage is
    empty, so its output is pure restatement of schedule. The human-factors literature is
    harsher: Skitka et al. show that omission errors, the exact class here, are the ones that
    training does not fix, and that an imperfect monitoring aid can leave a system worse off
    than none, because it substitutes for the vigilance it was meant to support. The systems
    literature supplies the discriminator: where two observers disagree, prefer the one reading
    the effect (commits) over the one reading the intent (schedule), which is precisely the
    pairing observed. The decisive fact is internal to the item and needs no citation — two
    instruments read the same morning and returned opposite verdicts, and the one that measured
    an artifact was right. That is a controlled experiment C2A2 has already run on itself, and
    it falsifies the presumption directly.

  Specific risks: The status channel is currently an amplifier of the failure in
    PRESUMPTION-664 rather than a detector of it: a run that dies silently produces no failure
    report, which the aggregator renders as "No failures to report," converting an absence of
    information into a positive assurance. This is worse than having no status agent, because
    it consumes the attention that would otherwise have gone to checking. Per Keil et al.'s
    self-reinforcing cycle, each unchallenged green report lowers the scrutiny applied to the
    next, so the error rate is not stationary — it grows. Per Skitka et al., the resulting
    omission errors are resistant to the natural remedy of "read the report more carefully."
    Concretely: any downstream decision that consumed the "No failures to report" line — a
    scheduling decision, a green-light to proceed, a metric of streak length — is built on a
    statement with no evidential content. And because the aggregator names specific runs as
    successful, it does not merely fail to detect; it asserts a false particular, which is
    harder to unwind than a silence.

  Mitigations available: (1) Change the aggregator's input: it must read outcome artifacts
    (commits, file mtimes, output paths, terminal verdict records) and must be forbidden from
    reading the schedule. If an outcome artifact is missing, the correct output is UNKNOWN, not
    SUCCESS. (2) Add a three-valued status vocabulary — SUCCEEDED / FAILED / NO-EVIDENCE — and
    make NO-EVIDENCE visually and procedurally distinct from SUCCEEDED. The current binary
    forces the aggregator to lie. (3) Require every status claim to carry its evidence pointer
    (which artifact, which timestamp); a claim with no pointer is not publishable. This is
    cheap and makes the defect self-revealing. (4) Keep both instruments and alarm on
    *disagreement* between them rather than trusting either; the disagreement is itself the
    highest-value signal available and it was already produced today at no cost. (5) Per
    Parasuraman & Riley on indicator salience, make the green state carry information — report
    "4 of 4 runs verified by commit" rather than "no failures," so that a drop to 2 of 4 is
    visible without reading prose. (6) Per Skitka et al. on accountability reducing automation
    bias, require the human consumer to periodically spot-check one named run against its
    artifact; accountability was the one manipulation that reliably lowered automation bias.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-666
    Strongest counterargument: A status aggregator is not supposed to be an oracle — it is a
      cheap first-pass summary, and the system correctly carried a second, artifact-based
      instrument that caught what the first missed. On that reading the architecture worked
      exactly as designed: defence in depth, with a fast shallow check and a slow deep one, and
      the deep one won. Demanding that every status claim be artifact-backed would collapse the
      two instruments into one and remove the redundancy that produced the catch. Moreover the
      IS status-reporting literature concerns *human* reporters with incentives to slant; an
      automated aggregator has no motive to be optimistic, so the bias half of Snow & Keil's
      framework does not transfer, and only the error half applies — which is a much weaker
      claim. Automation-bias findings likewise come from time-pressured cockpit and monitoring
      tasks with seconds to respond; a wiki-maintenance status report read at leisure by an
      attentive reader is a different regime.
    What would need to be true for C2A2 to be safe: (a) The second, artifact-based instrument
      always runs, and its output is actually read — if it can itself be one of the silently
      killed runs (PRESUMPTION-664), the redundancy is illusory because the two instruments
      share a failure domain. (b) When the two disagree, the disagreement is surfaced and
      resolved rather than the reader taking whichever they saw first or last. (c) The shallow
      instrument's output is labelled as unverified, so no downstream artifact inherits its
      claim as fact. (d) No decision has already been made on the strength of the false
      particular ("named as successful a run that had terminated with no output").
    How to test: Direct and one-shot. Take the aggregator's last N status reports and, for each
      named-successful run, check whether an outcome artifact exists with a timestamp inside
      that run's window. The false-positive rate falls straight out. Then check the converse:
      how many runs that produced no artifact were reported as failures — if the answer is
      zero, the instrument has no negative-detection capability at all and its positive
      predictive value is undefined rather than merely low. Both queries are one join over data
      the vault already holds.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-05
    Affected items: PRESUMPTION-664, PRESUMPTION-666, PRESUMPTION-668, PRESUMPTION-669
      (continuous with PRESUMPTION-660, PRESUMPTION-661)
    Common vulnerability: All four substitute a *declaration* for a *measurement*. The system
      reads an artifact produced by, or adjacent to, the very process whose state is in
      question — an empty report channel (664), a status assertion (666), a retraction (668),
      a hold's label (669) — and treats that artifact as the state. In three of the four the
      failing component is the monitoring layer itself, which continues to emit reassurance
      while inside the failure domain it is supposed to observe.
    Literature basis: Huang et al. 2017 (differential observability); Mahmood & McCluskey 1988
      (checker independence); Cristian 1991 (omission ≠ crash); Cemri et al. 2025 (task
      verification as a top-level MAS failure category); Parasuraman & Riley 1997 and Skitka et
      al. 1999-2000 (automation complacency and omission errors in monitoring).
    Risk level: Critical
    Recommendation: Adopt a single invariant across the monitoring layer — no health claim may
      be derived from an artifact produced by the subject of the claim. Every green signal must
      trace to an independently observed, monotonically advancing quantity (a commit, a byte
      count, a file mtime, a counter). Audit all existing health instruments against this
      invariant; the ones that fail it are currently producing false assurance, not information.

  Search scope: Adequate. Concepts searched: schedule-derived vs outcome-derived status
    aggregation; software project status reporting error, bias and distortion; the mum effect
    and reluctance to report bad news; automation bias, complacency and omission errors;
    accountability as a debiasing manipulation; symptom-based vs cause-based monitoring; gray
    failure and differential observability; multi-agent verification failures. Not searched:
    the sensor-fusion / conflicting-evidence literature (Dempster-Shafer conflict measures),
    which would bear on how to arbitrate between two disagreeing instruments.
