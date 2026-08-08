SEARCH-FOR-PRESUMPTION-713:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-713
  Original statement: That one register item working once establishes that this
    register is consumable; the first recorded instance in ~1,460 items over
    ~118 days of a register item changing a run's action, occurring one day
    after filing — the condition least like the register's steady state.
    Risk: Medium. POSITIVE case.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-713
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Asked what one instance establishes and noted the age of the item
        that produced it.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Pilot and feasibility study methodology — located this session via
       "Should treatment effects be estimated in pilot and feasibility studies?"
       Pilot and Feasibility Studies (BMC), 2019, DOI 10.1186/s40814-019-0493-7
       [authors not captured in the returned snippet and NOT verified];
       Teare et al. or similar, "Sample size requirements to estimate key design
       parameters from external pilot randomised controlled trials: a simulation
       study," PMC 4227298 [attribution uncertain]; Lakens, D., "Feasibility
       Sample Size Justification," The 20% Statistician blog, August 2020. —
       The most directly relevant methodological grounding, and it splits the
       claim cleanly in the way the item needs. The consistent position is that
       feasibility studies are designed to establish *that something can be
       done* and to yield logistical parameters — eligible-patient counts,
       consent rates, treatment fidelity, methods of measurement — while being
       inherently unable to give reliable effect estimates, because small-sample
       estimates are too imprecise and should not drive the main trial's power
       calculation. Mapped onto this item: one register item changing a run's
       action does establish feasibility — the consumption pathway exists and
       functions end to end — and does not establish a rate.
    2. The same literature, on the direction of the error. — The located
       material states that within-group change estimates from pilots are
       imprecise and do not support sound causal inference, and that the effect
       size for the main study should come from clinical judgement rather than
       from the pilot. This is the caution the item is pressing: a single
       observed success is an existence proof and a very poor estimator, and the
       standard methodological advice is to refuse to use it as one.
    3. Tversky, A. & Kahneman, D., 1971. "Belief in the law of small numbers."
       Psychological Bulletin. [Classic; located this session via Wikipedia
       "Law of small numbers," Effectiviology and an eScholarship working paper,
       "Inference by Believers in the Law of Small Numbers" — the latter is
       Rabin, M., c. 2002, attribution from established knowledge, NOT confirmed
       in the snippet.] — Names the failure mode precisely. The law of small
       numbers is the incorrect belief that small samples are highly
       representative of the populations they come from; people treat small
       samples as carrying the essential characteristics of the parent
       distribution. Generalising from n = 1 out of ~1,460 is the limiting case.
    4. Base rate neglect — same cluster of sources. — Supplies the second and
       more specific defect the item identifies. The base-rate fallacy is the
       tendency to ignore general statistical information about how common
       something is and instead judge from a specific case that matches a
       prototype. The available base rate here is stark and known to the run:
       one instance in ~1,460 items over ~118 days. Reasoning from the instance
       while that denominator is in hand is base-rate neglect in its textbook
       form.
    5. Documentation staleness and recency effects in retrieval — a body of
       2025-26 practitioner and preprint material located this session (Atlan,
       "LLM Knowledge Base Staleness"; ragaboutit.com, "The Knowledge Decay
       Problem"; TianPan.co, "RAG Knowledge Base Freshness"; arXiv 2509.19376,
       "Freshness and the Limits of Heuristic Trend Detection in Temporal RAG").
       [All located by title/URL only; none opened. The figures returned in
       summaries — 60% of enterprise RAG projects failing on freshness, up to
       20% retrieval degradation from stale embeddings — are UNVERIFIED and I am
       not treating them as measured.] — Supports the item's sharpest
       observation, that one day old is the condition least like the register's
       steady state. The recurring and consistent claim is that semantic
       similarity has no correlation with document recency, so retrieval systems
       surface stale items confidently and without an error signal, and that the
       fix requires explicit freshness penalties and maximum-age SLAs. If
       utility decays with age, a success at day one is drawn from the most
       favourable point of the decay curve and is the worst available estimator
       of the mean.

  Strength of support: Weak

  Summary: There is a legitimate and non-trivial FOR reading, and it should not
    be dismissed. The feasibility-study literature is explicit that a small or
    single-case result establishes *that a thing can be done* and yields
    logistical parameters, and by that standard the observation is real evidence:
    the consumption pathway from register to changed action exists and completed
    end to end for the first time in ~118 days, which was not previously
    demonstrated. That is a genuine finding and the correct claim to make from
    it. What no located source supports is the stronger reading the item
    surfaces — that this register is consumable, as a standing property. The
    same literature that licenses feasibility inference explicitly refuses rate
    inference from the same data, on the ground that small-sample estimates are
    too imprecise to plan from. Tversky and Kahneman's law of small numbers
    names the generalisation error and base-rate neglect names the specific one,
    which is acute here because the denominator was in hand: one in ~1,460 is
    not a hidden base rate. The item's second observation is the more damaging
    of the two and is independently supported. If documentation utility decays
    with age — which the staleness literature asserts consistently, and asserts
    with the additional point that retrieval gives no warning signal when it
    happens — then a one-day-old item is sampled from the most favourable point
    on the curve, and the register's steady state consists almost entirely of
    items far older. The single success is therefore drawn from a condition the
    register does not normally occupy, which makes it a weaker estimator than
    even n = 1 would ordinarily be.

  Caveats: The strongest sources are from clinical trial methodology, where the
    quantity of interest is a treatment effect in a defined population, and the
    mapping onto "is this register consumable" is loose — consumability is
    arguably a feasibility question rather than an effect-size question, which
    would put the observation on the licensed side of the distinction. That is a
    real defence and the search did not defeat it; the honest position is that
    the observation supports feasibility and the presumption overreaches into
    rate, and reasonable readers could differ on where the run's claim actually
    sat. Source 1's author list is unverified and source 3's secondary
    attribution (Rabin) is from established knowledge. Source 5 is entirely
    practitioner and preprint material located by title, with figures I have
    declined to treat as measured, and it concerns embedding-based retrieval
    rather than an agent reading a register — the decay mechanism may differ
    substantially. There is also a countervailing consideration no source
    addressed: a single success in a system that has never succeeded is
    informative out of proportion to its sample weight, because it discriminates
    between "the pathway is broken" and "the pathway is unused," and those are
    very different diagnoses with very different remedies. Nothing located
    quantifies that discriminating value, but it is real and it is the best
    argument available for the run's reading.

  NOVELTY-FLAG: Not raised. Base-rate reasoning, small-sample inference and
    documentation decay are all well covered. One sub-question was not answered
    by anything located: no source was found that measures the decay curve of a
    process-audit register item's utility as a function of age — the staleness
    literature covers factual documentation going out of date, which is a
    different mechanism from a process observation becoming irrelevant. If C2A2
    measures that curve it would be measuring something not found here.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: inference from single successes,
    the law of small numbers, base-rate neglect and hasty generalisation;
    feasibility and pilot study methodology and the feasibility/effect-size
    distinction; documentation decay, knowledge-base staleness and recency
    effects in retrieval effectiveness. Not searched, and recommended: survival
    analysis / hazard-rate framing, which is the natural formalism for "what
    does one event in 1,460 item-days establish" and would give the item a
    quantitative footing it currently lacks; and the organisational learning
    literature on lessons-learned repositories, which is the closest domain
    analogue to this register and has its own findings on non-consumption.
