SEARCH-FOR-PRESUMPTION-691:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-691
  Original statement: That the review queue's growth measures the hunt's
    health; queue 34 -> 40, sixteen days without a decision, and no metric in
    this system falls when the queue rises. Risk: High. NOTE: compounds
    PRESUMPTION-677.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-691
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a framing shared by three independent runs reporting
        the same queue.
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Ridgway, V.F., 1956. "Dysfunctional Consequences of Performance
       Measurements." Administrative Science Quarterly 1(2): 240-247. — The
       foundational refutation, and the closest structural match found. Ridgway
       documents public employment interviewers evaluated on number of
       interviews conducted, who consequently conducted fast interviews and
       placed very few applicants; and law-enforcement investigators given a
       quota of eight cases per month, who selected easy fast cases. In both,
       the producer-side count rose while the outcome the count was meant to
       proxy fell. His general claim is that quantitative measures are useful
       but that undue confidence in them is common because their consequences
       are poorly understood. A queue count is the purest form of the metric he
       warns about: it counts what was produced and is structurally incapable
       of falling when the outcome degrades.
    2. Little, J.D.C., 1961. "A Proof for the Queuing Formula: L = λW."
       Operations Research 9(3): 383-387; and the flow-metrics application of
       it (Kanban/WIP-limit practice; multiple practitioner sources this
       session). — Gives the mathematical reading of the exact numbers in this
       item and inverts their sign. With average cycle time equal to
       work-in-progress divided by throughput, a queue rising from 34 to 40
       against a throughput of zero over sixteen days does not indicate more
       health; it indicates cycle time diverging. The standard practitioner
       formulation is explicit that once WIP rises above capacity, system
       throughput *declines*, and that reducing WIP at constant throughput
       shortens lead time. Queue growth is therefore a degradation signal in
       the very framework that defines it.
    3. Goodhart's law and the strong-form treatment (Goodhart 1975 [UNVERIFIED
       — cited from established knowledge, not confirmed this session];
       Manheim & Garrabrant and the RL-alignment literature, e.g. "Goodhart's
       Law in Reinforcement Learning," arXiv:2310.09144). — Explains why the
       item's second clause is the load-bearing one. The strong form holds that
       optimising a proxy does not merely stop helping but becomes actively
       harmful once the proxy and the target decouple. The condition under
       which this bites hardest is an unopposed proxy — which is exactly the
       state the item reports: no metric in the system falls when the queue
       rises, so there is no term in the objective that registers the cost of
       growth.
    4. Counter-metric / guardrail / paired-indicator practice (practitioner
       literature, consistent across many independent sources this session:
       balanced-scorecard treatments, guardrail-metric guides, and the DORA
       pairing convention of deployment frequency with change failure rate).
       — Names the specific structural defect the item identifies and gives its
       standard remedy. The recurring prescription is that every quantity or
       speed indicator must be paired with a quality or value indicator —
       cycle time with post-release defect rate, PR volume with PR review load
       — and that a dashboard should be a system of checks and balances rather
       than a single metric. A register in which no indicator falls when the
       queue rises is, by this standard, an unpaired metric, and unpaired
       metrics are the documented gaming and self-deception surface.
    5. Peer-review capacity literature: Horta, H. et al. [co-author list
       uncertain], 2024. "The crisis of peer review: Part of the evolution of
       science." Higher Education Quarterly 78(x); and "Can We Volunteer Out of
       the Peer Review Crisis?" arXiv:2604.27900. — The best available empirical
       case of a single-consumer review queue and it reports the opposite of
       health. Submissions have roughly doubled per decade across most fields
       while the qualified reviewer pool has stagnated; NeurIPS submissions
       grew from 1,678 in 2014 to 17,491 in 2024. The documented consequences
       are longer review times, editors inviting ten to twelve reviewers to
       secure two, and degraded review quality. Nobody in this literature reads
       submission growth as a measure of the field's health; it is uniformly
       reported as the cause of the crisis.

  Strength of support: None

  Summary: No literature was found supporting queue growth as a health measure,
    and the two most relevant traditions treat it as a degradation signal.
    Ridgway's 1956 cases are the direct structural analogue: a producer-side
    count that rises while the outcome it proxies falls, precisely because the
    count cannot register the failure. Little's Law reads the item's own
    figures against it — 34 to 40 with zero decisions in sixteen days is cycle
    time diverging, and the WIP-limit practice built on Little's Law holds that
    throughput declines once WIP exceeds capacity. The item's second clause is
    the more serious finding and is well covered: counter-metric and guardrail
    practice holds that every quantity indicator must be paired with a quality
    indicator, so a register in which nothing falls when the queue rises is an
    unpaired metric by definition, and Goodhart's strong form describes what
    unopposed proxies do to the systems that optimise them. The peer-review
    capacity literature supplies the empirical single-consumer case, where
    submission growth against a static reviewer pool is universally reported as
    the crisis rather than as a sign of vigour. This item compounds
    PRESUMPTION-677 exactly as flagged: 677 concerns the production rate being
    treated as independent of consumption capacity, and 691 identifies the
    measurement layer that keeps that independence invisible.

  Caveats: One narrow and honest defence exists. Queue growth is a valid
    leading indicator of *upstream detection activity* — it does show the hunt
    is finding things — and if the intended referent of "the hunt's health" is
    strictly generation rather than the review pipeline, then the metric is not
    wrong, only incomplete. That defence collapses the moment the figure is
    read as a system-health measure, which is what the item reports three
    independent runs doing, and it is exactly the substitution Ridgway names.
    Scope limits: the flow-metrics and WIP literature is largely practitioner
    rather than peer-reviewed, though it rests on Little's Law which is not;
    Little's Law itself assumes a stable system, and a system with zero service
    over sixteen days is outside its stationarity assumption, so the formula is
    used here diagnostically rather than predictively. The peer-review analogy
    involves many consumers rather than one, which if anything understates the
    severity of the single-consumer case. Goodhart 1975 is unverified; source
    5's co-author list is uncertain.

  NOVELTY-FLAG: Not raised. Thoroughly covered, and the coverage runs against
    the presumption.

  Recommendation: NO-SUPPORT-FOUND

  Search scope: Comprehensive. Concepts searched: Ridgway and the dysfunctional
    consequences of performance measurement; Goodhart's law and strong-form
    proxy failure; Little's Law, WIP limits and Kanban flow metrics; vanity
    metrics and producer-side proxies; counter-metrics, guardrail metrics and
    paired quantity/quality indicators; peer-review reviewer-capacity crisis as
    a single-consumer queue. Overlaps deliberately with the PRESUMPTION-677
    search, which covered the alarm-management standards (EEMUA 191,
    ANSI/ISA-18.2) and Google's static-analysis warning-suppression results —
    both apply here and were not re-searched.
