SEARCH-AGAINST-PRESUMPTION-691:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-691
  Original statement: That the review queue's growth measures the hunt's health; queue 34 -> 40,
    sixteen days without a decision, and no metric in this system falls when the queue rises.
    (NOTE: compounds PRESUMPTION-677.)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-691
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from a framing shared by three independent runs reporting the same
        queue.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Little's Law and WIP-limit practice in flow-based systems (Little's Law as applied in
       Kanban — Lead Time = WIP / Throughput — confirmed this session via Atlassian's WIP-limits
       guidance and Scrum.org/getDX flow-metrics material; these are practitioner rather than
       peer-reviewed sources, though Little's Law itself is a standard queueing-theory result).
       The arithmetic directly inverts the presumption. With throughput held constant, a rising
       WIP does not indicate more work being done; it indicates proportionally longer lead time
       and nothing else. The practitioner statement of the diagnostic is exact: "if WIP is
       climbing week over week, work is entering faster than it's leaving." C2A2's queue rose
       34 -> 40 with zero decisions in sixteen days — throughput is not merely constant, it is
       zero, and with zero throughput Little's Law makes lead time undefined/unbounded. Under
       any flow reading, 34 -> 40 is the signature of a stalled single-consumer system, not of
       a healthy hunt.
    2. Flow efficiency evidence (Scrum.org, "Flow Efficiency: The Hidden Metric Exposing Your
       Product Bottlenecks"; getDX flow-metrics material; both confirmed this session). Typical
       teams show flow efficiency of 15-20%, meaning 80%+ of an item's lifetime is queue time,
       and the literature's conclusion is that low flow efficiency "is a system problem, not a
       people problem." This matters for the specific framing 14b identified: three independent
       runs reading queue growth as productivity are all measuring the producer side of a
       system whose constraint is on the consumer side. The queue is where the item is *not*
       being worked on.
    3. NHS elective waiting-list statistics — the list-size versus waiting-time distinction
       (Institute for Fiscal Studies, "The past and future of NHS waiting lists in England" and
       "Can the government achieve its 18-week elective waiting time target?"; Nuffield Trust;
       Office for Statistics Regulation statement on comparability; all confirmed this session).
       The most instructive real-world case of a queue metric mistaken for a system-health
       metric. The IFS finding is decisive: there is no simple relationship between the size of
       the waiting list and the distribution of waiting times — the list stood at four million
       on multiple occasions since 2007 with very different waits each time, and the 18-week
       target could in principle be met at any list size. The corollary they draw is the one
       C2A2 needs: waiting lists measure *demand and activity*, not performance, so movements
       "do not necessarily reflect different levels of performance." A rising list is
       consistent with a healthy referral pipeline and with a collapsed treatment capacity, and
       list size alone cannot distinguish them.
    4. Goodhart's law and the vanity-metric literature (Wikipedia entry on Goodhart's law
       confirmed this session; Splunk, "What is Goodhart's Law?"; Axify, "Goodhart's Law: The
       Hidden Risk in Software Engineering Metrics"; also "The Strong, Weak and Benign
       Goodhart's law," arXiv:2505.23445, confirmed as existing this session, contents not
       read). The mechanism that makes 14b's second clause — "no metric in this system falls
       when the queue rises" — the dangerous part. Where a proxy correlates imperfectly with
       the goal, optimising the proxy selects for noise as well as signal, producing "progress
       that looks real but isn't," and effort reallocates toward the cheapest behaviours that
       move the number. Item *generation* is cheap; item *adjudication* is expensive. A metric
       set with no counterweight to queue growth is a system with a free lever, and the
       literature predicts the lever gets pulled.
    5. WIP-limit rationale (Atlassian, "Working with WIP limits for kanban," confirmed this
       session). States the harm mechanism explicitly: high WIP "creates congestion, increases
       context switching, and hides problems because nothing ever finishes." The last clause is
       the compounding risk for C2A2 — an unbounded review queue does not merely fail to
       measure health, it actively conceals the failure to decide, because unresolved items
       accumulate without ever registering as failures.

  Strength of challenge: Strong

  Summary: Every literature searched treats a growing queue with static throughput as
    pathology, and none supports reading it as vigour. Little's Law makes the inversion
    arithmetic rather than interpretive: with throughput at zero across sixteen days, queue
    growth conveys no information about the hunt's productivity and complete information about
    the review function's failure. The NHS case is the closest institutional analogue and its
    lesson is directly transferable — list size measures demand and activity, not performance,
    and the same list size is compatible with opposite system states. The second half of 14b's
    observation is the more serious finding: an instrument panel in which no gauge falls when
    the queue rises is, by Goodhart's-law reasoning, an instrument panel that rewards the cheap
    half of the loop. The compounding with PRESUMPTION-677 is expected on this reading, since
    both concern producer-side proxies standing in for system outcomes.

  STEELMAN:
    Strongest counterargument: Queue growth is a real signal about the *detector*, even if it
      says nothing about the system. A hunt that surfaces six new candidate items in a period
      is demonstrably finding things, and suppressing that signal because the consumer is
      backed up would penalise the one part of the loop that is working — the classic error of
      throttling detection to make a backlog look better, which in safety reporting systems
      destroys the reporting culture outright. Sixteen days is also a short window: for
      low-frequency, high-consequence review decisions, batching and deliberation are
      legitimate, and a queue that grows while a reviewer thinks carefully is not obviously
      worse than one that shrinks through hasty disposal. Additionally, the items in C2A2's
      review queue may have heterogeneous value; a queue of 40 containing three critical items
      is a different object from a queue of 40 uniform ones, and raw count is the wrong
      statistic in either direction, for health or for alarm.
    What would need to be true for C2A2 to be safe: (a) the queue is bounded, or has an
      explicit policy for what happens at a threshold, so growth cannot continue indefinitely;
      (b) age is tracked, not just count — sixteen days without a decision is the load-bearing
      number, and it is the one that is currently not instrumented; (c) at least one metric
      falls when the queue rises, so the dashboard cannot be improved by generation alone; (d)
      the deliberate-batching defence is actually true, i.e. there is a scheduled review event
      with a date, rather than an absence of review being retrospectively described as
      deliberation; (e) queue composition is visible, so that a critical item cannot age
      silently inside an aggregate. Conditions (b) and (c) are the ones 14b's evidence says are
      unmet.
    How to test: Reconstruct the review queue's time series from the vault's daily records and
      compute, for each day: arrivals, departures (decisions), queue size, and the age
      distribution of open items — specifically the maximum and 90th-percentile age. Then plot
      cumulative arrivals against cumulative departures; if the two lines diverge monotonically,
      the system is not a queue but an accumulator, and no interpretation of growth as health
      survives. Second test, on the metric set rather than the queue: enumerate every metric
      the system currently reports and, for each, determine its sign of response to a new
      unresolved item. If the count of metrics that fall is zero, 14b's claim is confirmed
      exactly and the Goodhart risk is live. Third: check whether any item has been in the
      queue longer than the oldest item was when the queue was 34 — if so, the growth is not
      turnover, it is sedimentation.

  Specific risks: If queue growth does not measure the hunt's health, then C2A2's principal
    progress signal is measuring the wrong side of the loop, with four consequences. First,
    misallocation: effort continues to flow to generation because generation is what registers,
    while the actual constraint — adjudication — receives none, so the backlog grows
    superlinearly. Second, concealment: the WIP literature's warning that high WIP "hides
    problems because nothing ever finishes" means an item that should have triggered action
    can sit indefinitely without ever being recorded as a failure; a Critical-risk item in a
    40-deep queue is functionally undetected. Third, decision decay: items age, and an
    assessment made against a system state sixteen or sixty days stale may be wrong by the time
    it is adjudicated, so throughput failure silently degrades the quality of the eventual
    decisions too. Fourth, and specific to this register: because the queue is read as health,
    the very growth that signals the review function's collapse will be reported as evidence
    that the system is working — the metric is not merely uninformative, it is inverted, which
    is worse than having no metric.

  Mitigations available: (1) Instrument age, not just count: report oldest-item age and
    90th-percentile age alongside queue size; sixteen days without a decision should itself be
    a reported number. (2) Add a falling metric — the minimal fix for 14b's second clause is a
    single gauge that declines when an item is added and unresolved, e.g. resolution rate,
    or a decision-debt figure. (3) WIP limit on the review queue with an explicit policy at the
    ceiling (stop intake, escalate, or batch-dispose), so unbounded growth is structurally
    impossible. (4) Cumulative flow diagram — arrivals versus departures on one chart is the
    single cheapest artefact that makes accumulation visually undeniable. (5) Separate
    detection health from system health in reporting, so the steelman's legitimate concern
    (don't punish the detector) is preserved: report find-rate and resolve-rate as two named
    metrics, never as one. (6) Composition breakdown by risk level, so a Critical item cannot
    age inside an aggregate. (7) Given the noted compounding with PRESUMPTION-677, audit the
    full metric set for other producer-side proxies standing in for outcomes.

  Search scope: Comprehensive for the flow/queueing framing (Little's Law, WIP limits, flow
    efficiency), for a strong institutional analogue (NHS elective waiting lists, where the
    list-size-versus-waiting-time distinction is authoritatively documented by IFS, the Nuffield
    Trust and the Office for Statistics Regulation), and for the metric-design framing
    (Goodhart's law, vanity metrics). Sources for the flow material are predominantly
    practitioner publications rather than peer-reviewed operations research; the underlying
    results (Little's Law, queueing stability under arrival rate exceeding service rate) are
    standard but were not traced to primary texts this session. Preliminary on two adjacent
    areas that would strengthen the case: peer-review backlog studies in scholarly publishing
    (single-consumer review queues with known ageing effects), and vulnerability-management
    literature on open-finding age as a risk measure. Broader search recommended if a
    peer-reviewed citation base is required.

  Recommendation: CHALLENGED
