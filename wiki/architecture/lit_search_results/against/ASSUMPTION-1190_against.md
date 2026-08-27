SEARCH-AGAINST-ASSUMPTION-1190:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1190
  Queue ref: LIT-QUEUE-2026-08-24-002
  Original statement: Throttling intake is an appropriate response to a stalled human review stage.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1190
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from a second consecutive deliberate narrowing
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: Preliminary. The web-search budget was exhausted before a dedicated admission-control /
    backpressure query could be issued, so this item was worked from sources already in the provenance set:
    the Google SRE book chapters on cascading failures and on monitoring, Leveson's system-theoretic
    accident model, and the Google SRE STPA material. Venues: Google/O'Reilly SRE book (2016), MIT preprint,
    Google SRE engineering blog.
    GAPS — significant, and the reader should weight this item accordingly: no queueing-theory paper, no
    admission-control paper, and no human-in-the-loop-pipeline study was retrieved directly. The blocked
    queries were `https://html.duckduckgo.com/html/?q=admission+control+human-in-the-loop+queue+
    backpressure+server+unavailable+latency` and an equivalent WebSearch, both refused (search budget /
    provenance restriction). Little's Law is invoked below as canonical mathematics rather than as a
    retrieved source and is marked accordingly. A follow-up pass with search budget should target:
    Little (1961); load shedding vs. circuit-breaking; head-of-line blocking; and empirical studies of
    human-review queues in content moderation and clinical triage.

  Challenging evidence found: Partial

  Sources:
    1. "Addressing Cascading Failures," Ch. 22 in Beyer, B., Jones, C., Petoff, J., Murphy, N. R. (eds.),
       Site Reliability Engineering. O'Reilly/Google, 2016.
       https://sre.google/sre-book/addressing-cascading-failures/ — The chapter scopes intake reduction
       (queue-length limiting, load shedding, returning HTTP 503) explicitly to the *saturation* case:
       "If there is insufficient capacity to handle all the requests at steady state, the server will
       saturate its queues," and the recommended control is "to return an HTTP 503 (service unavailable) to
       any incoming request when there are more than a given number of client requests in [the queue]."
       Critically, the chapter's own model of when queueing is even useful presumes a non-zero service rate:
       "If the request rate and latency of a given task is constant, there is no reason to queue requests:
       a constant number of threads should be occupied." The prescription is for a server that is slow, not
       for a server that is absent. Applying the saturation remedy to an absent-server condition is a
       transfer the source does not license. FULL-TEXT (read in relevant part via targeted extraction).
    2. Leveson, N. "A New Accident Model for Engineering Safer Systems." MIT preprint,
       http://sunnyday.mit.edu/accidents/safetyscience-single.pdf [published venue — details unverified].
       — The four conditions for control (after Ashby, 1956): the controller must have a goal; "must be able
       to affect the state of the system"; must contain a model of the system; and must be able to ascertain
       its state. Throttling intake is a control action on arrival rate. The unsafe state is "review stage
       not servicing." Arrival rate is not upstream of service availability, so the throttle satisfies
       condition 4 (it observes the stall) and fails condition 2 with respect to the actual goal: it cannot
       affect the variable that is out of bounds. The action is well-formed as control of the queue and
       null as control of the stall. FULL-TEXT (PDF, read in relevant part).
    3. Holthaus, G. "Teaching a new way to prevent outages at Google." Google SRE,
       https://sre.google/stpa/teaching/ [no date on page]. — Documents an outage in which a controller
       correctly detected a pending unsafe condition and deferred to human controllers who were not
       attending; the condition sat for 30 days and then produced the outage. The generalisable lesson is
       that a mechanism which buys time against an absent human controller buys only time, and time alone
       does not resolve; the outage arrived on schedule. Directly relevant to whether throttling is an
       "appropriate response" or merely a deferral that conceals the stall. FULL-TEXT.
    4. Little, J. D. C. 1961. "A Proof for the Queuing Formula: L = λW." Operations Research 9(3):383–387.
       [details unverified — cited from memory as canonical; NOT retrieved in this session]. — The relevant
       consequence is elementary and does not depend on the citation: with L = λW, reducing λ bounds the
       growth of L but has no effect on W for work already enqueued when the service rate is zero. Waiting
       time for items already in the queue is set entirely by when service resumes. Throttling therefore
       cannot shorten the latency it is deployed against. [details unverified]

  Strength of challenge: Moderate

  Summary: The retrieved sources do not show that throttling intake is harmful — they show that it is
    scoped to a different failure than the one it is being applied to. Every admission-control prescription
    found (SRE Ch. 22) presumes a server that is servicing too slowly; the remedy works by letting a
    still-running server drain. When the server is absent rather than saturated, the service rate is zero,
    and by Little's Law reducing the arrival rate bounds queue growth while leaving the waiting time of
    every enqueued item entirely determined by when the human returns. In control-theoretic terms
    (Leveson/Ashby) the throttle is acting on a variable it can affect rather than on the variable that is
    out of bounds, which is the textbook signature of an ineffective control action. The sharper objection
    is second-order: throttling makes the stall *less visible* — arrival rate falls, queue growth flattens,
    and the pipeline's own indicators improve — so the mechanism that is supposed to protect the system
    also suppresses the strongest signal that a human is missing. That is the same structure as
    PRESUMPTION-866 and ASSUMPTION-1203 and is the reason this item is flagged systemically below.
    I did not find evidence that throttling *lengthens* service latency; the honest finding is that it is
    inert with respect to the stated problem and actively counterproductive with respect to detection.

  Specific risks: If ASSUMPTION-1190 is false, C2A2 responds to an absent reviewer with an action that
    cannot restore the reviewer, and does so in a way that flattens the telemetry which would otherwise
    escalate. Concretely: (a) the review backlog's growth rate — the most legible proxy for "no human has
    been here" — is damped by the very mechanism triggered by the stall, so the 49-day condition looks
    milder in the metrics the longer it runs; (b) throughput is sacrificed for no latency benefit, since
    items already queued are unaffected; (c) the assumption licenses repeated narrowing (14a extracted it
    from a *second consecutive* deliberate narrowing), so the system has a ratchet with no release
    condition — each stall justifies a further intake reduction, and nothing in the mechanism ever
    reverses it; (d) if the throttle is deep enough, C2A2 approaches a quiescent state that is
    indistinguishable in its indicators from a healthy idle system.

  Mitigations available:
    - Separate the two controls: keep intake throttling as queue-bound protection, and add a distinct,
      escalating control whose target variable is reviewer presence (page, escalate, reassign, or
      time-boxed auto-approve/auto-reject with audit). This satisfies Ashby's condition 2 for the actual
      goal (Leveson).
    - Instrument reviewer *presence* independently of queue depth, so the throttle cannot mask the stall.
      SRE Ch. 6 (Ewaschuk) frames this as monitoring symptoms rather than causes.
    - Give the throttle an explicit release condition and a maximum cumulative depth, so consecutive
      narrowings cannot ratchet without bound.
    - Prefer fast rejection with a clear reason over silent slow-walking — SRE Ch. 22's 503 pattern is
      valuable precisely because it is loud at the caller; a throttle that merely slows intake without
      signalling why reproduces the invisibility problem.

  STEELMAN:
    Item: ASSUMPTION-1190
    Strongest counterargument: Throttling is not intended to fix the stall — it is intended to bound the
      damage while the stall persists, and at that job it is correct and well-supported. An unbounded queue
      in front of a zero-rate server exhausts memory, blows every downstream deadline, and guarantees that
      when the reviewer does return they face a backlog too large to clear, converting a recoverable pause
      into a permanent one. SRE Ch. 22 makes exactly this argument for bounded queues. Furthermore, if
      admitted-but-unreviewed work carries ongoing cost or risk (stale state, expiring context, holding
      locks), then reducing λ genuinely reduces total harm even though it does not reduce W. Judged as
      damage control rather than as remedy, the assumption is sound and the challenge is a category
      complaint about how the action was labelled, not about the action.
    What would need to be true for C2A2 to be safe: (1) The throttle must be accompanied by a separate
      escalation path that targets reviewer absence directly, and that path must not itself be gated on the
      queue metrics the throttle suppresses. (2) Reviewer-presence telemetry must be independent of intake
      rate and queue depth. (3) The throttle must have a bounded floor and an explicit release condition, so
      consecutive narrowings terminate. (4) The system must not report improved health as a consequence of
      throttling — the health metric must be invariant to the throttle, or the mechanism becomes
      self-concealing.
    How to test: Directly measurable in C2A2's own logs. Plot admitted-item rate, queue depth, and the
      layer's reported health across the 49-day window. If reported health improves or stays flat while
      reviewer-touch events remain at zero, condition (4) is violated and the throttle is masking. Separately,
      measure whether any item enqueued before a throttle event was serviced sooner than an otherwise
      identical item enqueued after it — if not, the throttle is confirmed inert with respect to latency,
      as Little's Law predicts.

  Recommendation: PARTIALLY-CHALLENGED
