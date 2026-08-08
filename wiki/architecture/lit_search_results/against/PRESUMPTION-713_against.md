SEARCH-AGAINST-PRESUMPTION-713:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-713
  Original statement: That one register item working once establishes that this register is
    consumable; the first recorded instance in ~1,460 items over ~118 days of a register item
    changing a run's action, occurring one day after filing — the condition least like the
    register's steady state. [POSITIVE case]

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-713
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Asked what one instance establishes and noted the age of the item that produced it —
        one day, against a register whose median item age is far larger.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tversky, A. and Kahneman, D., 1971. "Belief in the Law of Small Numbers." Psychological
       Bulletin. (Authors, title and year confirmed this session from multiple independent hosts,
       including a full PDF at stats.org.uk and an Academia.edu record; volume and page numbers
       [UNVERIFIED — commonly cited as 76(2), 105-110, but not confirmed here, and the full text
       was not read.]) The classical result: people treat a small sample as highly
       representative of its parent population, expecting samples to resemble the population far
       more closely than sampling theory allows. Tversky and Kahneman's demonstration is
       particularly apt because the subjects were *mathematical psychologists* — people who knew
       the sampling theory — and they still greatly exaggerated the likelihood that a
       significant result on 20 subjects would replicate on 10. The transfer is direct: a single
       success in ~1,460 trials is a point estimate of 0.068% with a confidence interval that
       includes essentially any small rate, and it licenses no conclusion about consumability.
       The representativeness heuristic named in the same work is the specific mechanism by which
       a single vivid instance is mistaken for a property of the process.
    2. Documentation and knowledge-base staleness literature. Located this session: episteca.ai,
       "The Documentation Decay Problem"; Slite, "Why knowledge bases fail"; Atlan on LLM
       knowledge-base staleness; ragaboutit.com on knowledge decay in RAG systems;
       knowledge-base.software content-audit guides; Startup House on outdated knowledge bases.
       [IMPORTANT SOURCING CAVEAT: every one of these is a vendor or practitioner blog, and the
       quantitative claims they carry are attributed to third-party surveys I did not locate —
       technical documentation becoming materially outdated within 30-90 days is attributed to
       Readme; 68% of enterprise technical content not updated in six months and 34% not in a
       year is attributed to Zoomin; 60% of employees not trusting their internal knowledge base
       is attributed to Guru. None of these figures was verified and none should be quoted as
       established. They are cited here only because they are unanimous on the *direction* of
       the effect.] The direction is what matters for this item: documentation utility declines
       with age from the moment of publication, and the decline is driven by divergence between
       the documented state and the actual state.
    3. Recency and retrieval. The knowledge-decay material above extends the same point to
       retrieval systems: as a corpus grows and ages, the proportion of retrievable content that
       is still accurate falls, and stale content actively degrades trust in the store as a
       whole. [Sourcing caveat as above — this was reached through practitioner RAG material, not
       through the information-retrieval literature.] The relevant structural claim for
       PRESUMPTION-713 is that P(useful | item) is a *function of item age*, not a constant, so
       an observation drawn at age 1 day does not estimate the parameter at the register's
       median age.
    4. Static-analysis and alert-suppression literature (shared with PRESUMPTION-712): "Quieting
       the Static: A Study of Static Analysis Alert Suppressions," arXiv 2311.07482 (identifier
       and title confirmed; authors [UNVERIFIED]), and the general finding that unadopted
       warnings are ignored and that suppression behaviour becomes habitual. Relevant here
       because it supplies a competing explanation for the single success: the item that worked
       was one day old, which means it was plausibly still salient in the run's working context
       rather than retrieved from the register at all. If so, the instance is not evidence about
       the register's consumability but about short-term recall, and the register's contribution
       is unestablished even in the one positive case.

  Strength of challenge: Moderate

  Summary: The inference is challenged on two independent grounds, one strong and one weakly
    sourced. The strong ground is elementary and does not require the literature at all: one
    success in ~1,460 items over ~118 days is a consumption rate of 0.068%, and the classical
    small-numbers result says that a single instance is treated as far more representative than
    it is, even by people who know better. The weaker but more interesting ground is the one 14b
    identified — the successful item was one day old, which is the condition *least* like the
    register's steady state, so the observation is drawn from the extreme tail of the age
    distribution and estimates the wrong parameter. The staleness literature supports the claim
    that utility declines with age, but its quantitative content comes entirely from unverified
    vendor surveys and cannot bear weight; the argument here rests on the structural point
    (utility is age-dependent, so a sample at age 1 does not estimate utility at the median age)
    rather than on any decay rate. A competing explanation deserves recording: a one-day-old item
    may have influenced the run through ordinary recency of context rather than through retrieval
    from the register, in which case the single success is not evidence about the register at
    all. This is a POSITIVE case and should be treated as genuinely good news about the item —
    the challenge is entirely to the generalisation drawn from it.

  STEELMAN:
    Item: PRESUMPTION-713
    Strongest counterargument: A single instance can establish something important even when it
      establishes nothing about a rate — namely *possibility*. Before this event, it was open
      whether a register item could change a run's action at all; the mechanism might have been
      broken end to end, in which case no amount of improvement to filing quality would help. One
      success rules that out, and existence proofs are legitimately established by n=1. That is a
      different and more modest claim than "this register is consumable," but it may be the claim
      actually being made, in which case 14b has read a possibility claim as a rate claim. There
      is also a real argument that the low rate is the wrong denominator. Most register items
      describe conditions that simply did not recur, so they had no opportunity to fire; the
      relevant base rate is not successes over items filed but successes over items whose
      triggering condition was met, and that denominator is unknown and probably very small. On
      that reading a 0.068% raw rate is uninformative in the *other* direction, and the register
      might be performing well on the cases that arose. Finally, the age observation admits a
      benign reading: if recency is what made the item consumable, that is actionable and cheap
      to exploit — surface recent items preferentially, or re-surface old ones — rather than
      being a reason to doubt the register.
    What would need to be true for C2A2 to be safe: (a) the claim made from the instance is
      explicitly the possibility claim, not the rate claim, and is recorded as such — this alone
      resolves most of the challenge; (b) the correct denominator is estimated: how many register
      items had their triggering condition recur, and of those, how many fired? Without this the
      register's performance is unknown in both directions; (c) the age dependence is measured
      rather than assumed, by recording the age of any item that influences a run; (d) the
      recency-versus-retrieval question is settled, because if the one success came from working
      context rather than from the register, the register's demonstrated consumption rate is
      zero, not 0.068%; (e) no policy is set on the basis of this instance until (b) and (d) are
      answered. Condition (d) is the decisive one and is the cheapest to check: it is a question
      about how the run actually obtained the item.
    How to test: Mostly runnable from the record. First, establish the denominator: sample n
      register items, determine for each whether its triggering condition recurred during the
      observation window, and count how many of those fired. This converts 0.068% into a
      meaningful rate or shows that it cannot be computed. Second, settle the recency question by
      examining the run that consumed the item: did it retrieve the item from the register, or
      was the item present in its context because it had been filed the previous day? A single
      inspection answers this. Third, run a direct experiment on age dependence: deliberately
      surface an item from the oldest decile of the register to a run whose task it bears on, and
      see whether it changes the action. If old items fire as readily as new ones, 14b's age
      observation is defused; if they do not, the age dependence is demonstrated in-system and is
      worth more than any of the vendor decay figures cited above. Fourth: track forward. Record
      every subsequent instance of a register item changing a run's action, with the item's age,
      and revisit the inference at n=10 rather than n=1.

  Specific risks: If one instance does not establish consumability, then (i) the system may
    conclude that the register mechanism works and stop investing in the thing that would make
    it work — retrieval, surfacing, triage — which is the standard cost of a premature positive;
    (ii) the age confound means any improvement effort will be aimed at the wrong stage, tuning
    filing quality when the binding constraint is retrieval of old items; (iii) the single
    instance is vivid and will be cited, and a cited n=1 becomes the system's belief about its
    own register, which is difficult to dislodge once the number 0.068% is no longer adjacent to
    it; (iv) if the recency explanation is correct, the register's true demonstrated consumption
    rate is zero and the system holds a positive belief with no supporting instance at all; (v)
    this is the item where the risk of *over*-correction also lives — treating a genuine positive
    as worthless would be its own error, and the register's one success is real and should be
    kept in view.

  Mitigations available: (1) Restate the claim as a possibility claim with the rate attached:
    "the mechanism can fire; observed rate 1/1,460 over 118 days; the firing item was 1 day old."
    This costs one sentence and removes almost the entire exposure. (2) Instrument consumption
    going forward — log every item that influences a run, with its age — so that n grows and the
    inference can be revisited on evidence rather than repeated. (3) Compute the conditional
    denominator (items whose trigger recurred), which is the only way to know whether the
    register is performing well or badly. (4) Determine whether the successful item was retrieved
    or merely recent, since the two have opposite implications. (5) Run the old-item surfacing
    experiment, which directly tests the age dependence at low cost. (6) Do not set policy on
    n=1 in either direction — neither "the register works" nor "the register is useless" is
    supported by the evidence currently held.

  Search scope: Adequate for the base-rate framing: the small-numbers result is classical and
    well attested, though the primary paper's volume and pages were not confirmed and the full
    text was not read. Weak for the documentation-decay and recency-of-retrieval framing — every
    source located was a vendor or practitioner blog relaying third-party survey figures that I
    could not verify, so those sources support only the direction of the effect and no magnitude
    should be taken from this file. This is a real limitation: the age-dependence argument, which
    is 14b's most interesting move, is currently supported by structure and plausibility rather
    than by a citable measurement. Not searched, and directly relevant: the information-retrieval
    literature on recency bias in ranking and on temporal relevance decay, and the software-
    engineering literature on comment/documentation drift relative to code (which has real
    empirical studies with measured drift rates and would replace the vendor figures entirely).
    Broader search strongly recommended on both — this is the item in the batch whose challenge
    would most improve with better sources.

  Recommendation: CHALLENGED
