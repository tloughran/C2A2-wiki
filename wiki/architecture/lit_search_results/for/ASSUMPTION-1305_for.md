SEARCH-FOR-ASSUMPTION-1305:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1305
  Original statement: "**Phase 2 skipped on judgement**, not omission: refilling the queue the same
    morning you emptied it would put new cards in front of you before any of today's 85 triplets had been
    looked at."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1305
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. First day in the register on which `pending/` reached zero and
        the run's response was to withhold supply; the cost side (a day of un-surveyed tradition output)
        is not priced, and was surfaced separately as PRESUMPTION-950.
      15a: Searched for supporting literature; found a well-populated and largely convergent literature
        (queueing theory / Little's law, WIP limits, Theory of Constraints, code-review size effects,
        peer-review assignment-load effects) supporting BOTH limbs, with one important scope caveat.
    Current status: SUPPORTED

  Register pre-check: Four ACTIVE premises bear directly and one of them is close to dispositive.
    - PREMISE-070: "Since 06-16 the binding constraint on the proposal pipeline is human review
      throughput, not literature discovery (review-bound). By Theory of Constraints, other stages should
      be subordinated to review — i.e., do not over-feed intake while review is the bottleneck." This is
      ASSUMPTION-1305's limb (a) and limb (b) already validated, in this estate, for this pipeline.
    - PREMISE-119: production and judgment are not independently schedulable; unbounded production
      imposes a congestion externality.
    - PREMISE-121: reviewer per-item cost is not constant and capacity does not scale with production;
      review-queue acceptance falls with workload and cumulative exposure.
    - PREMISE-050: a bounded, quality-sensitive ingest backlog should be drained in small scoped batches.
    Also adjacent: PREMISE-106 (queue in the unstable regime), PREMISE-147 (age, not count, carries the
    information). Per the intake's own instruction and OPEN-192's unruled status, the search was run
    anyway; the hit is recorded.

  Supporting evidence found: Yes

  Sources:
    1. Little, J.D.C. 1961. "A Proof for the Queuing Formula: L = λW." Operations Research 9(3):383-387.
       — SECONDARY (theorem statement retrieved via multiple secondary expositions; primary paper not
       fetched) — L = λW is the formal basis for the WIP-limit practice: with throughput fixed, average
       cycle time rises linearly in work-in-process. Adding items to a queue whose service rate is
       unchanged lengthens time-in-system for everything already in it. This supports the *mechanism* of
       the claim, not its empirical magnitude here.
    2. Goldratt, E.M. 1984/1990. Theory of Constraints — subordination principle. — SECONDARY — The
       standard operations prescription is that non-constraint stages be subordinated to the constraint;
       feeding a non-constraint at full rate while the constraint is saturated raises inventory without
       raising throughput. This is exactly the run's stated reasoning, and it is the mechanism already
       encoded in PREMISE-070.
    3. Cohen, J. et al. (SmartBear / Cisco Systems code review case study), 2006. "Best Kept Secrets of
       Peer Code Review" / Cisco case study. 2,500 reviews, 3.2M LOC. — SECONDARY (PDF at
       static1.smartbear.co returned empty body on fetch; figures taken from two independent retrieved
       secondary descriptions, SmartBear's own guidance page and the Conley write-up) — Reported: defect
       density falls sharply above ~200-400 LOC per review; no review larger than 250 lines produced more
       than 37 defects/kLOC; reviewers working faster than ~450 LOC/hour produced below-average defect
       density in 87% of cases. This is the closest measured analogue to "a batch that exceeds the
       reviewer's absorption window yields less per item."
    4. ALMA Proposal Handling Team, 2022. "Analysis of the ALMA Cycle 8 Distributed Peer Review Process."
       arXiv:2204.05390. — VERIFIED (fetched; Figure 15 caption read directly) — "Reviewers with 5 or
       more proposal sets wrote significantly shorter comments than reviewers with 4 or fewer proposal
       sets." A per-reviewer assignment-load threshold measured in a real large-scale review system
       (1,497 proposal sets). Note the measured variable is comment *length*, a proxy.
    5. Reinertsen, D.G. 2009. The Principles of Product Development Flow. — SECONDARY — Standard source
       for queueing economics in knowledge work: queues are the root cause of most product-development
       waste, and the cost of a queue is convex in its length. Widely cited as the bridge between
       queueing theory and knowledge-work batch policy.
    6. Kanban WIP-limit practice literature (multiple practitioner sources retrieved). — SECONDARY —
       Consistent claim across sources that a hit WIP limit is *diagnostic*: it reveals that the
       downstream stage cannot consume, which is precisely what an emptied `pending/` with 85 unabsorbed
       triplets downstream represents. One retrieved source states the caveat directly and I record it
       under Caveats.

  Strength of support: Strong (for limb a: reviewer attention is the binding constraint);
                       Moderate (for limb b: presenting new items before old are absorbed reduces
                       throughput).

  Summary: The two limbs separate cleanly and are not equally well supported. Limb (a) — that reviewer
    attention rather than proposal supply is the binding constraint — is supported by the general
    operations result that a saturated stage downstream of an unsaturated one defines system throughput,
    and is already an ACTIVE premise of this estate (PREMISE-070) established on this pipeline's own
    data. Limb (b) — that *adding* items reduces throughput — is the weaker one. Little's law gives it
    rigorously for cycle time (more WIP, longer latency at fixed throughput) but does NOT by itself give
    it for throughput: in the pure queueing model, throughput is set by the server, and arrivals neither
    help nor hurt it. The empirical case for a genuine throughput penalty rests on human-factors
    evidence — the Cisco size effect, the ALMA 5+ assignment-load effect, and the context-switching
    literature — which shows per-item review quality and effort degrading as load rises. That evidence
    is real but is about per-item quality degradation rather than items-per-day, so it supports limb (b)
    in the form "throughput of *adequately reviewed* items falls," not "raw throughput falls."

  Caveats:
    - Little's law is an identity about a stable system; it constrains latency, not throughput. Citing it
      for limb (b) without the human-factors evidence would be an overclaim, and I flag that explicitly
      because it is the easiest error to make here.
    - One retrieved practitioner source makes a pointed counter-observation that cuts against the run's
      remedy even while conceding limb (a): a team with one overloaded reviewer "doesn't really have a
      WIP problem — they have a review-capacity problem wearing a WIP costume," and capping upstream
      supply "shifts the queue from 'in progress' to 'waiting to start' but doesn't ship faster." On this
      reading, withholding Phase 2 protects the reviewer's experience but does not increase the number of
      triplets absorbed; the cost 14a says is unpriced (a day of un-surveyed tradition output) is then a
      real, uncompensated loss. This is the single strongest qualification found and it belongs in any
      adoption note.
    - The Cisco figures are widely repeated but I could not retrieve the primary PDF; the exact
      denominators behind "37 defects/kLOC" and "87%" are SECONDARY only and must not carry weight.
    - Domain transfer: code review, grant peer review, and PRS-triplet absorption differ in per-item
      cost, reversibility, and whether items are independent. The direction of the effect transfers well;
      the thresholds (200-400 LOC, 5 proposal sets) do not transfer at all and must not be imported as
      numbers.
    - The run made a one-day judgement, not a policy. None of this literature licenses a standing rule
      to withhold supply; PREMISE-050's "batch size must be tuned" caveat applies.

  Search scope: comprehensive search — queueing theory and Little's law in knowledge work, WIP limits and
    Kanban, Theory of Constraints subordination, code-review batch-size and review-rate effects (Cisco /
    SmartBear), peer-review reviewer workload and assignment-load effects (ALMA distributed review, peer
    review fatigue literature), context-switching costs.

  Recommendation: SUPPORTED — with the recommendation resting on limb (a), which is strongly supported
    and already an ACTIVE premise. Limb (b) is PARTIALLY-SUPPORTED and should be recorded in the weaker
    form ("throughput of adequately reviewed items"), with the review-capacity-costume objection attached.
