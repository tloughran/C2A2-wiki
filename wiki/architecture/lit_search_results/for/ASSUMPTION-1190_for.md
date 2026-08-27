SEARCH-FOR-ASSUMPTION-1190:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1190
  Queue ref: LIT-QUEUE-2026-08-24-002
  Original statement: Throttling intake is an appropriate response to a stalled human review stage.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1190
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: 14a extracted from a second consecutive deliberate narrowing
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: Web searches run 2026-08-25 across operations-management, queueing-theory and
    distributed-systems literatures.
    Queries: drum-buffer-rope / Theory of Constraints / release at bottleneck rate / CONWIP / WIP
    limits; admission control, load shedding, backpressure, congestion collapse, bounded queue
    latency; metastable failures in distributed systems (Bronson et al., HotOS '21) and the
    sustaining-effect / load-shedding escape; Reinertsen, product-development flow, invisible queues,
    Little's Law, WIP constraints in knowledge work; human-in-the-loop review queues, reviewer
    capacity, backpressure to upstream producers; queueing stability condition (ρ < 1, Loynes'
    criterion) and unbounded growth when λ ≥ μ.
    Venues reached: HotOS/ACM, NSDI, Probability Surveys, arXiv (math.PR, cs.NI, cs.SE), plus
    operations-management textbook/practitioner sources and vendor grey literature.
    Date range: 1962 (Loynes' criterion, cited secondarily) – 2026.
    Assessment: COMPREHENSIVE for the general principle (throttle intake when a downstream stage is
    the constraint); PRELIMINARY for the specific boundary condition the brief singles out — a server
    that is *absent* (μ ≈ 0) rather than *saturated* (μ > 0 but λ > μ). Broader search recommended in
    the service-operations and healthcare-diversion literatures (ambulance diversion, ED boarding,
    call-centre blocking) which I did not reach.

  Supporting evidence found: Partial

  Sources:
    1. Goldratt, E.M. — Theory of Constraints, drum-buffer-rope. [primary text and edition details
       unverified; reached via secondary expositions at tocinstitute.org, leanproduction.com and
       Wikipedia "Theory of constraints"] — The core supporting principle, stated directly: the
       "rope" is the signal that controls when new work enters, synchronising release to the
       constraint's consumption rate so WIP does not accumulate beyond what the buffer needs.
       Subordinating intake to a non-producing constraint is the textbook prescription, not a
       departure from it. SNIPPET-ONLY (secondary sources).
    2. "Drum-buffer-rope and workload control in high-variety flow and job shops with bottlenecks:
       An assessment by simulation." [authors/venue unverified; located via ResearchGate record] —
       Simulation assessment of DBR and workload-control release methods in bottleneck shops.
       Relevant because it tests release-rate control empirically rather than asserting it.
       ABSTRACT-ONLY.
    3. Reinertsen, D.G. 2009. The Principles of Product Development Flow: Second Generation Lean
       Product Development. Celeritas Publishing. ISBN 978-1935401001. — Argues that invisible,
       unmanaged queues are the root cause of poor product-development performance, and names WIP
       constraints as a primary mechanism for controlling queue size and therefore delay. This is the
       direct knowledge-work analogue of the claim: constrain intake to control the queue at the
       stalled stage. SNIPPET-ONLY (book; reached via secondary summaries).
    4. Little's Law / queueing stability condition, as surveyed in Bramson, M. 2008. "Stability of
       Queueing Networks." Probability Surveys, vol. 5. DOI 10.1214/08-PS137. [page range
       unverified] — Supplies the formal warrant: a queue is stable iff the average arrival rate is
       strictly below the average service rate (Loynes' criterion); at ρ ≥ 1 the queue grows without
       bound, and expected queue length is infinite even at exact balance. When the review stage
       stalls, μ → 0 and *every* positive arrival rate is unstable, so reducing λ is the only lever
       on the intake side. FULL-TEXT available; read at SNIPPET level.
    5. "Stabilization of an overloaded queueing network using measurement-based admission control."
       arXiv:0708.2739. [authors/venue unverified] — Directly on point for the supportive direction:
       demonstrates that measurement-based admission control can stabilise a network that is already
       overloaded, i.e. throttling intake is a valid stabilisation response and not merely a
       preventive one. ABSTRACT-ONLY.
    6. Bronson, N., et al. 2021. "Metastable failures in distributed systems." Proceedings of the
       Workshop on Hot Topics in Operating Systems (HotOS '21), ACM. DOI 10.1145/3458336.3465286.
       [full author list beyond first author unverified] — Defines the self-sustaining congestive
       collapse in which a system degrades under a transient stressor and fails to recover after the
       stressor is removed, held there by a sustaining effect (retries, timeouts, queues that never
       drain). Load shedding — i.e. reducing intake — is identified as a principal mechanism for
       escaping the metastable state. This is the strongest support for throttling as a *recovery*
       measure, not just a preventive one. FULL-TEXT (PDF at sigops.org).
    7. "Metastable Failures in the Wild." USENIX ;login: online. [authors/date unverified] —
       Corroborates that the sustaining effect keeps systems in a degraded state and impedes
       recovery, and that queues which have grown during an outage are themselves the impediment.
       SNIPPET-ONLY.
    8. Protego: "Overload Control for Applications with Unpredictable Lock Contention." NSDI 2023.
       faculty.cc.gatech.edu/~amsmti3/assets/protego-nsdi23.pdf. [author list unverified] — Systems
       overload-control work built on the standard result that server throughput rises with offered
       load, peaks at saturation, then falls as overload-management overhead swamps useful work;
       admission control keeps the system near the peak. Establishes that intake reduction is the
       accepted primitive when the downstream server cannot keep up. ABSTRACT/SNIPPET-ONLY.
    9. "Human-in-the-Loop AI Review Queues (2026): Scalable Workflows, SLAs & Feedback Loops."
       alldaystech.com. — Grey literature, but the only source located that states the claim in its
       exact operational form: backpressure "must travel upstream — if the consumer is slow, the
       producer must change," with drain mode throttling output when review backpressure exceeds a
       threshold, "ensuring the loop does not outrun its merge infrastructure." Non-peer-reviewed;
       corroborative only. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: The general principle behind the claim is one of the better-established results in
  operations management and systems engineering. Theory of Constraints prescribes exactly this
  behaviour — the "rope" subordinates the release of new work to the constraint's consumption rate —
  and Reinertsen carries the same prescription into knowledge work via WIP constraints on invisible
  queues. Queueing theory supplies the formal warrant: with the review stage stalled the service rate
  collapses, no arrival rate is stable, and intake is the only variable on that side of the equation
  under the controller's authority. Two systems results strengthen the case that throttling is
  appropriate as a *response* and not merely as prevention: measurement-based admission control has
  been shown to stabilise an already-overloaded network, and the metastable-failure literature
  identifies load shedding as a principal means of escaping a degraded state that persists after its
  trigger has gone — the backlog accumulated during a stall is itself an obstacle to recovery. The
  supportive case for the claim therefore rests on three distinct benefits: bounding backlog growth,
  preserving the freshness and reviewability of queued items, and avoiding a recovery-time overload
  when the human stage resumes.

  Caveats: (a) Every source found addresses a *saturated* server (μ > 0, λ > μ) or a congestively
  collapsed one, not an *absent* one. The brief's own framing — "whether reducing arrival rate
  shortens or lengthens service latency when the server is absent rather than saturated" — is the
  precise question I could not find addressed. With μ ≈ 0, throttling slows the rate at which the
  backlog grows but does not by itself reduce any individual item's waiting time; the mechanism by
  which it helps is deferred (cheaper recovery, bounded WIP), not immediate. (b) TOC's prescription
  presumes the constraint is *producing* at some rate that release is synchronised to; a rate of zero
  is degenerate for drum-buffer-rope, so the transfer is by analogy rather than by direct
  application. (c) The metastable-failure support is conditional: it applies where a feedback loop
  (retries, resubmissions, growing per-item cost) makes the backlog self-sustaining. If the stalled
  human stage has no such loop, the recovery-cost argument weakens. (d) Load shedding and admission
  control both assume rejected or deferred work is genuinely lower-value or can wait; where intake
  items have decaying value, throttling trades queue length for lost value and the appropriateness
  becomes an economic question the located literature does not settle. (e) Several citations carry
  unverified author or venue details and are marked as such; the Goldratt and Reinertsen primary
  texts were reached only through secondary expositions.

  Recommendation: PARTIALLY-SUPPORTED

PARTIAL NOVELTY-FLAG:
  Item: ASSUMPTION-1190
  Searched: Admission control and backpressure under server unavailability (as distinct from
    saturation); queueing or operations results on whether reducing arrival rate helps when the
    service rate is zero; human-in-the-loop pipeline literature on throttling intake during reviewer
    absence.
  Finding: Strong, convergent support exists for throttling intake when a downstream stage is the
    binding constraint and is *slow*, and for load shedding as a means of escaping a degraded state
    whose backlog is self-sustaining. No located source treats the zero-service-rate case, and none
    distinguishes "the reviewer is overloaded" from "the reviewer is absent" as calling for different
    intake policy.
  Implication: The claim is well supported as a WIP-bounding and recovery-cost argument, and
    unsupported as a latency argument. The distinction the brief flags is real and the literature
    does not resolve it.
  Unaddressed sub-claim: that throttling intake is appropriate specifically when the review server is
    *stalled/absent* (μ ≈ 0) rather than saturated — including whether it shortens or merely defers
    service latency in that regime.
  Recommended status: NOVEL (stalled-server boundary case only)
