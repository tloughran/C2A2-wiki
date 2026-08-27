SEARCH-AGAINST-PRESUMPTION-875:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-875
  Queue ref: LIT-QUEUE-2026-08-24-007
  Original statement: An unbounded accumulating queue is the right structure for a human review gate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-875
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from absent alternatives across a sixteen-day discussion with a one-member
           remedy space
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Two WebSearch queries executed (unbounded queue / human review backlog / alert
    fatigue / SOC triage; queueing-theory instability when arrival rate exceeds service rate, and
    admission control), plus web_fetch of the arXiv SOC screening survey. Venues reached: ACM
    Computing Surveys, ACM Transactions on Internet Technology, arXiv (cs.CR), Columbia Business
    School queueing teaching materials, IEEE CDC proceedings archive, practitioner SOC literature.
    Date range: 1985–2026. COMPREHENSIVE on the alert-fatigue / review-backlog side, which turns out
    to be a large and directly analogous literature. PRELIMINARY on the explicit TTL/expiry-in-
    backlogs and sampled-vs-exhaustive-review sub-questions: the WebSearch budget was exhausted
    before I could search those separately, and dl.acm.org/doi/full/10.1145/3723158 returned an empty
    body on fetch, so the two ACM surveys are SNIPPET-ONLY. GAP: I found no literature at all
    defending unbounded accumulation, which is itself notable but should be read as an absence-of-
    evidence result given the search was not exhaustive.

  Challenging evidence found: Yes

  Sources:
    1. [Standard queueing-theory result, textbook.] Green, L. "Queueing Theory and Modeling."
       Columbia Business School teaching note.
       https://business.columbia.edu/sites/default/files-efs/pubfiles/5474/queueing%20theory%20and%20modeling.pdf
       — The stability condition: unless average utilisation is strictly less than 100%, the system
       is unstable and the queue grows without bound. If the average arrival rate exceeds the average
       service rate, queue length approaches infinity almost surely. This is not a challenge to the
       *design* so much as a statement that the design has no steady state. SNIPPET-ONLY.
       [Underlying result is canonical (Lindley/Loynes); details unverified in this search.]
    2. [Authors not captured.] "Unstable Queues." Proceedings of the 24th IEEE Conference on Decision
       and Control, 1985.
       https://people.eecs.berkeley.edu/~ananth/1981-1986/UnstableQueuesCDC1985.pdf
       — Cited for the standard remedy: an unstable queue is stabilised by a dropping/admission-control
       policy that reduces the effective arrival rate λ' < λ below service capacity. The literature's
       answer to "arrivals exceed service" is *shed load*, never *accumulate*. SNIPPET-ONLY
       [details unverified — I have the URL and the result, not the full citation].
    3. [Authors not captured.] 2026. "AI-Driven Security Alert Screening and Alert Fatigue Mitigation
       in Security Operations Centers: A Comprehensive Survey." arXiv:2605.08316.
       https://arxiv.org/html/2605.08316v1 — Frames the entire field as a pipeline with an explicit
       *pre-queue* filtering stage ("Category I: Alert Filtering and Noise Reduction (Screening
       Stage: Pre-Queue)") and a *queue-ordering* stage ("Category II: Automated Triage and
       Prioritization"). The mature engineering answer to a human review gate is therefore: filter
       before the queue, order within the queue, and budget the human's cognitive bandwidth
       explicitly — three mechanisms, none of which is present in an unbounded accumulating queue.
       FULL-TEXT (§3.1 and structure read via fetch; later sections truncated).
    4. [Authors not captured.] 2025/2026. "Alert Fatigue in Security Operations Centres: Research
       Challenges and Opportunities." ACM Computing Surveys. DOI: 10.1145/3723158.
       https://dl.acm.org/doi/full/10.1145/3723158 — Survey establishing that alert volume routinely
       exceeds human triage capacity, producing backlogs, delayed investigation and missed incidents.
       SNIPPET-ONLY (fetch returned an empty body; content from search summary).
    5. [Authors not captured.] 2024. "Towards Human-AI Teaming to Mitigate Alert Fatigue in Security
       Operations Centres." ACM Transactions on Internet Technology. DOI: 10.1145/3670009.
       https://dl.acm.org/doi/full/10.1145/3670009 — Treats capacity-exceeding queues as a problem
       requiring an architectural intervention (human-AI teaming), not a neutral holding structure.
       SNIPPET-ONLY.
    6. [Practitioner sources, non-peer-reviewed, cited for magnitude only.] Industry SOC reporting
       surfaced in search (underdefense.com, vectra.ai, daylight.ai, panther.com) converges on:
       ~42% of security alerts go uninvestigated; analysts face 1,000–5,000 alerts per shift against
       a realistic review capacity of ~15 per eight-hour shift; up to 67% of incidents go unaddressed;
       ~71% of analysts report burnout. SNIPPET-ONLY. These are vendor-marketing figures and should
       be treated as directionally indicative, not as measurements.

  Strength of challenge: Strong

  Summary: The claim fails on two independent grounds. First, formally: a queue whose arrival rate
  exceeds its service rate has no steady state and grows without bound; when the server's
  availability is not merely low but *zero* — the case flagged in the brief — the queue is not a
  gate at all, it is a write-only sink, and every item in it is functionally discarded while
  appearing retained. Second, empirically: the closest real-world analogue, SOC alert triage, has
  spent a decade discovering that unbounded accumulation against finite human attention produces
  backlog, degraded review quality ("triage becomes checkbox-clearing rather than investigation"),
  analyst burnout and missed incidents. The mature designs in that field all add structure the
  presumption lacks: pre-queue filtering, explicit prioritisation/ordering, cognitive-bandwidth
  budgeting, and load-shedding admission control. Notably I found no literature anywhere defending
  unbounded accumulation as a design; the entire remedy space in the sources is
  filter / prioritise / shed / expire. The presumption is not merely unsupported — the applicable
  literatures treat its negation as the starting point.

  Specific risks: If unbounded accumulation is the wrong structure, the C2A2 review gate is
  providing false assurance rather than review. Concretely: (a) the queue's existence licenses the
  pipeline to keep producing, because items appear to be "going somewhere," while nothing is
  consumed — the gate becomes a legitimation device; (b) with no TTL, no priority and no expiry,
  the *most recent* item and the *most important* item are indistinguishable, so if review ever
  does resume it will start from an undifferentiated pile whose ordering carries no information;
  (c) time-sensitive items (e.g. the health-verdict staleness issue in PRESUMPTION-876) rot in place
  and become actively misleading rather than merely unread; (d) queue depth was treated in the source
  discussion as the *cost* to be managed, which — per PRESUMPTION-865 — creates pressure to reduce
  upstream collection breadth to keep the depth down, meaning an unconsumed queue actively degrades
  coverage; (e) with a one-member remedy space, there is no second reviewer, so the queue's service
  rate is not just low but structurally fragile — a single unavailability event takes it to zero.

  Mitigations available:
    - Admission control / load shedding: reduce effective arrival rate below capacity (the standard
      stabilisation result; "Unstable Queues," CDC 1985).
    - Pre-queue filtering with an explicit false-negative budget (arXiv:2605.08316 §3, "Category I").
      Note this trades directly against PRESUMPTION-865 and must be budgeted, not improvised.
    - Explicit prioritisation / queue ordering rather than FIFO accumulation (arXiv:2605.08316 §4).
    - TTL and expiry: not found as a named mechanism in the sources I reached, but implied by the
      load-shedding result. Flagged as a search gap rather than an established remedy.
    - Sampled rather than exhaustive review: also a gap in my coverage; the SOC literature's
      prioritisation stage is the nearest analogue.
    - Batch disposition: the practitioner sources' observation that backlogged triage degenerates
      into "checkbox-clearing" suggests batch disposition happens *anyway* under load, and is better
      designed for explicitly than arrived at by exhaustion.

  STEELMAN:
    Item: PRESUMPTION-875
    Strongest counterargument: The queueing-instability result applies to systems where queued items
    have per-item value that decays and where the server is the bottleneck on a continuous process.
    A C2A2 review queue may be neither. If items are durable, cheap to store, and individually
    low-stakes, then an accumulating log is a legitimate *deferred* structure rather than a failed
    gate: the value is in having captured the item at all, and a human can later mine the accumulated
    corpus in aggregate rather than servicing it item-by-item. Dropping items via admission control
    would destroy information that costs almost nothing to retain, and any filtering policy imposed
    now would be tuned in ignorance of what the eventual reviewer actually wants — a real cost, and
    the exact failure PRESUMPTION-865 warns about. On this reading the queue is not an unbounded
    server queue at all; it is an append-only archive that was mislabelled as a gate, and the fix is
    to rename it rather than restructure it.
    What would need to be true for C2A2 to be safe: (i) queued items must not be time-sensitive —
    their value must not decay while waiting, which is precisely what PRESUMPTION-876 puts in doubt;
    (ii) nothing downstream may treat "queued" as equivalent to "reviewed," i.e. the queue must not
    be load-bearing for any release or trust decision; (iii) queue depth must not be treated as a
    cost that pressures upstream collection (else PRESUMPTION-865 activates); (iv) there must be a
    realistic aggregate-consumption path, not just a hypothetical one.
    How to test: Empirically testable and cheap. Measure the actual arrival rate and the actual
    service rate over the sixteen-day window: if service rate is zero, the "gate" designation is
    falsified outright by definition. Then measure decay: sample items queued more than N days ago
    and ask whether their content is still actionable — the staleness rate is a direct measure of
    whether the archive interpretation survives. Finally, check whether any downstream artefact
    cites "queued" as a status conferring assurance; if so, condition (ii) fails.

  Recommendation: CHALLENGED
