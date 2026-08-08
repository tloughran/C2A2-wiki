SEARCH-AGAINST-PRESUMPTION-710:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-710
  Original statement: That the held-state fix requires the single human authoriser's decision;
    stated ~3x as "it needs your decision rather than another run rediscovering it," with two
    alternatives never considered — that a run could cost the fix and propose a specific change,
    and that the single-authoriser convention is itself the binding constraint.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-710
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the alternatives absent from a thrice-repeated request — the request
        names the authoriser's decision as the only unblocking move and never entertains
        proposal-with-ratification or relaxation of the single-authoriser convention.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bezos, J. — the Type 1 / Type 2 (one-way door / two-way door) framework. Located this
       session across multiple secondary treatments (fs.blog, "Reversible and Irreversible
       Decisions"; LogRocket; Growth Method; The Uncertainty Project; Chief Executive). The
       framework's origin is variously attributed in these sources to the 1997 shareholder
       letter and to the 2015/2016 letters; [I did not retrieve any primary shareholder letter
       this session, so the attribution and dating should be treated as UNVERIFIED, and no
       quotation is asserted]. The content is consistent across sources and is directly on
       point: Type 1 decisions are consequential and effectively irreversible and warrant slow,
       consultative treatment; Type 2 decisions are reversible and *should be delegated* and made
       quickly by individuals or small groups, on roughly 70% of the information one would
       ideally want, because the cost of delay reliably exceeds the cost of a correctable
       mistake. The challenge to PRESUMPTION-710 is that the request never establishes which type
       the held-state fix is. If it is reversible — and a held-state fix in a version-controlled
       vault ordinarily is — the framework's prescription is the opposite of what was done.
    2. Winters, Manshreck and Wright (eds.), 2020. "Software Engineering at Google," Chapters 9
       (Code Review) and 22 (Large-Scale Changes), abseil.io (chapters located this session;
       chapter-level authorship [UNVERIFIED]). Supplies an existence proof rather than an
       argument: where a change is assessed as low risk, it is reviewed by *designated reviewers
       holding approval privileges across the entire codebase*, and low-risk LSCs are approved
       centrally and submitted without asking the individual owning teams. An organisation whose
       ownership model is far stricter than C2A2's has an explicit carve-out for exactly the
       case at issue — a mechanical change whose owner would almost certainly say yes. The
       carve-out exists because the alternative does not scale.
    3. "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency."
       arXiv 2605.30208 (identifier and title confirmed this session; authors, year and venue
       [UNVERIFIED]). Meta computes a risk score per change and automates the entire
       review-to-landing pipeline for low-risk diffs. This is the strongest available
       counterexample to the presumption's implicit claim that authorisation must be a human act
       per item: at scale, the authorisation decision is made once, at the level of a *policy*
       over a class of changes, and then applied automatically. The human decision is not
       eliminated; it is moved up a level and amortised.
    4. Queueing and constraint-theoretic material on single-consumer approval. Located this
       session: ScienceDirect topic overview on bottleneck queues; Adapt Consulting on Theory of
       Constraints for service teams; several practitioner treatments of approval bottlenecks
       (Flowmono, Tier2 Systems, Solution4Guru). All practitioner-level except the ScienceDirect
       overview; cited for the standard results rather than for novel findings. The load-bearing
       points: a queue forms whenever arrival rate exceeds service rate; sequential approval
       chains add latency multiplicatively with approver count and stall entirely when an
       approver is unavailable; and the standard remedies named are *delegation of lower-risk
       approvals*, *pre-approval stages*, and *automation of low-risk approvals*. Both of the
       alternatives 14b says were never considered are named remedies in this literature.
    5. Kanban/WIP and Little's Law material (Kanban Tool queueing-theory guide; Atlassian WIP
       limits; agility-at-scale). Practitioner sources, cited for the formal consequence: with a
       single consumer whose service rate over the relevant period is at or near zero and a
       non-zero arrival rate, queue length grows without bound and expected waiting time is
       unbounded. Applied here: if held-state items accumulate faster than the single authoriser
       clears them, the *convention* — not the difficulty of any individual decision — is the
       binding constraint, which is precisely the second alternative 14b identified as absent.

  Strength of challenge: Strong

  Summary: The presumption conflates three distinct things: that a decision must be *authorised*
    by the human, that it must be *originated* by the human, and that it must be originated
    *now*. The literature separates them cleanly. Reversible-decision frameworks say the
    delegation threshold is set by reversibility, and nothing in the thrice-repeated request
    establishes that the held-state fix is irreversible. Google and Meta both supply working
    counterexamples in which authorisation is exercised once over a *class* of low-risk changes
    and then applied without per-item human action — which dissolves the presumed dichotomy
    between "your decision" and "another run rediscovering it," because the third option is a run
    that costs the fix, proposes a specific change, and presents a yes/no rather than a problem.
    That third option reduces the human's work from analysis to ratification, which is exactly
    the move the approval-bottleneck literature names as its standard remedy. And the queueing
    result is the sharpest: with one consumer and a non-zero arrival rate, the constraint is the
    single-consumer convention itself, so a request repeated three times is evidence for 14b's
    second missing alternative rather than against it — the repetition is the queue.

  STEELMAN:
    Item: PRESUMPTION-710
    Strongest counterargument: The reversible/irreversible taxonomy is the whole argument, and
      it may cut the other way. A held-state fix is not obviously a two-way door: if the held
      state encodes a design commitment, changing it silently propagates through every
      subsequent run, and the cost of discovering the wrong choice later is not the cost of
      reverting one edit but of unwinding everything built on it. Under that reading the
      insistence on the authoriser's decision is not a bottleneck but correct Type 1 handling,
      and 14b's complaint would amount to asking for delegation of precisely the class the
      framework says not to delegate. There is a second, stronger defence. Both counterexamples
      cited — Google's central approvers and Meta's RADAR — delegate to *other humans* or to a
      *deterministic* pipeline with a test suite and a revert path. Neither delegates judgement
      to the same agent population that produced the problem, and this batch's PRESUMPTION-696
      finding is that C2A2 has no measured basis for treating one of its agents as an independent
      check on another. Delegating the held-state decision to a run would therefore be delegating
      to a component whose independence is unestablished — trading a slow, correct process for a
      fast one with unknown error properties. Third: the single-authoriser convention may be a
      *deliberate* rate limiter. A system that appends 41+21 items in a night (see
      PRESUMPTION-712) and drains none of them plainly has a production problem, not a
      consumption problem, and loosening the one constraint that forces items to stop moving
      would make that worse, not better.
    What would need to be true for C2A2 to be safe: (a) the held-state fix is genuinely
      irreversible or high-consequence — established by naming what could not be undone, not
      assumed from the fact that it is held; (b) if it is reversible, the request is restructured
      as a proposal — a run costs the fix, names the specific change, and presents a ratifiable
      yes/no, so the human's cost falls to a single decision; (c) the class of decisions
      requiring the authoriser is written down, so that membership is a policy rather than a
      per-item judgement made by whoever wrote the request; (d) the authoriser's actual clearing
      rate is measured against the arrival rate of items requiring authorisation — without this,
      whether the convention binds is unknown; (e) if the queue is growing, either the convention
      is relaxed for a named low-risk class or the arrival rate is throttled, because the
      literature admits no third resolution. Condition (b) is the cheapest and does the most
      work: it is available immediately, changes nothing about who authorises, and directly
      supplies the alternative 14b found missing.
    How to test: Runnable and mostly arithmetic. First, classify the held-state fix explicitly
      as reversible or not by writing down the revert procedure; if a revert procedure can be
      written, it is a two-way door and the delegation threshold applies. Second, measure the
      queue: count items in the record awaiting the single authoriser's decision, count how many
      were cleared over the last 30 days, and compute the ratio. A clearing rate below the
      arrival rate is a direct demonstration that the convention is the binding constraint and
      confirms 14b's second missing alternative. Third, count repetitions: the item records that
      this request was made ~3x. Extract the distribution of repetition counts across all
      requests to the authoriser in the record; a heavy tail is the observable signature of a
      saturated single consumer, and a light one would refute the queueing reading. Fourth,
      cheapest of all: attempt the missing alternative once — have a run cost the fix and propose
      a specific change — and observe whether the decision then clears faster. One trial settles
      whether the obstacle was the decision or its framing.

  Specific risks: If the single authoriser is not in fact required, then (i) the held state
    persists for as long as the queue does, and every run in the interim operates on known-wrong
    state, so the cost is not one delayed fix but a defect multiplied across all intervening
    runs; (ii) the repetition itself consumes capacity — three requests is three runs' worth of
    attention spent restating rather than resolving; (iii) the framing forecloses the cheap
    remedy, because as long as the only two options in view are "your decision" and "another run
    rediscovering it," no run will ever cost the fix, and the third option remains permanently
    unexercised; (iv) the convention becomes self-confirming — items that require the authoriser
    are exactly the items that do not get done, so the backlog of unauthorised items grows and
    is then read as evidence that these are hard problems rather than queued ones; (v) if the
    authoriser is genuinely a single point of failure, the system has no continuity plan, and any
    period of unavailability halts a whole class of work with no defined degradation path.

  Mitigations available: (1) Convert requests into proposals: a run costs the fix, states the
    specific change, and asks for ratification rather than analysis — the single highest-value
    change available and it requires no relaxation of the authorisation convention. (2) Write
    down the decision class: which categories require the authoriser and which do not, decided
    once at policy level rather than repeatedly at item level (the Google/Meta pattern). (3)
    Reversibility gate: any change with a written, exercised revert procedure defaults to the
    delegated class. (4) Instrument the queue — arrival rate, clearing rate, age of oldest item
    — so that the binding constraint is visible rather than inferred. (5) Batch: present held
    decisions as a single periodic slate rather than as scattered requests, which is the standard
    remedy for a saturated single consumer and reduces per-item overhead. (6) Define a
    degradation path for authoriser unavailability, even if it is only "these classes proceed,
    these halt." (7) Cap the number of open items awaiting authorisation, forcing the choice
    between clearing and not producing — the WIP-limit move.

  Search scope: Adequate for the delegation-threshold framing (reversible/irreversible decision
    literature), but the primary sources were not retrieved and the framework is cited from
    secondary treatments with attribution flagged. Comprehensive for the industrial
    counterexamples (Google's central approval for low-risk LSCs, Meta's risk-calibrated review
    automation), which are the strongest evidence here. Adequate but practitioner-heavy for the
    approval-bottleneck and queueing material; the formal queueing results invoked (arrival rate
    exceeding service rate implies unbounded queue) are standard and uncontroversial but were
    reached via Kanban and Theory-of-Constraints guides rather than a queueing text. Not
    searched: the human-factors literature on automation bias and on the appropriate scope of
    human-in-the-loop authorisation, which would speak to whether ratification-of-proposal
    preserves the value of the human check or degrades it — this is the most important gap,
    because the steelman turns on exactly that question. Broader search recommended there.

  Recommendation: CHALLENGED
