SEARCH-AGAINST-PRESUMPTION-635:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-635
  Original statement: That re-queuing a monitored item constitutes progress on it, and
    that queue activity is a valid proxy for attention.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-635
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a detailed processing report and a stated zero-consumption
           figure in the same register block (origin ASSUMPTION-656, ASSUMPTION-657)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Count.co, "Backlog Health Analysis: Metrics & Best Practices" — the governing
       measure is the intake-to-throughput ratio; below 100% the backlog is growing.
       Touch events are not an input. Explicitly names "items sit untouched for months"
       and "growing percentage exceeding aging thresholds" as the failure signature.
    2. GB Advisors, "Service Desk Ticket Backlog: Why It Keeps Growing" — backlogs grow
       because ingress exceeds sustainable throughput; reports ~30% efficiency loss at
       large backlog size, i.e. the backlog is not inert, it degrades the server.
    3. easydesk, "Ticket Aging Guide"; InvGate, "How to overcome aged tickets" — aging is
       measured creation-to-resolution. Re-touching does not reset or improve age.
    4. Umbrex, "Backlog Burn-Down Rate" — burn-down is defined by completions only.
    5. "The queue backlog that slowly eroded our system SLOs" (Medium, System Design with
       Sage) — unbounded queues absorb backpressure instead of enforcing it, so the queue
       silently hides the fact that demand exceeds capacity.

  Strength of challenge: Strong

  Summary: No standard measure of backlog health counts handling events, and several
  sources treat a high touch-to-completion ratio as a diagnostic of dysfunction rather
  than of activity. The queueing result is decisive and structural: when arrival rate
  exceeds service rate, an unbounded queue does not degrade gracefully, it grows without
  bound, and re-triggering increases the arrival rate. Re-queueing is therefore not
  merely non-progress; on the standard model it is a contribution to the instability.
  C2A2's own figures are the textbook picture — 1,773 [QUEUED] tags against 26 consecutive
  days of zero drain.

  Specific risks: If re-triggering is not progress, then the register's growth is not
  backlog management, and every report that presents re-trigger cohorts as pipeline
  activity overstates what the system did. The proxy failure is self-concealing: the more
  the system re-triggers, the busier its logs look and the further behind it falls. The
  unbounded-queue result adds that the pipeline currently has no backpressure signal at
  all — nothing in the architecture tells 14a/14b to slow intake.

  Mitigations available: Yes. (i) Publish intake-to-throughput ratio as a first-class
  figure in the daily summary — one number, computable by command, that cannot be
  satisfied by touching. (ii) Bound the queue, or set an explicit WIP limit, so that
  backpressure is enforced rather than absorbed. (iii) Report age-to-disposition
  distribution rather than counts. (iv) Distinguish "touched" from "advanced" in the tag
  vocabulary so the two can never be summed.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-635
    Strongest counterargument: A re-trigger changes nothing about an item's evidential
    state — it is the same claim with the same evidence and a later date. If it counted as
    progress, then progress would be a resource the system could manufacture at zero cost
    and unbounded rate, which is a reductio. The deeper problem is that the proxy is not
    merely weak, it is anti-correlated with the thing it stands for: a system under-
    resourced relative to its intake will generate re-trigger events at exactly the rate
    at which it fails to dispose of items, so activity rises as attention per item falls.
    Queue activity is thus the one metric guaranteed to look healthiest at the moment of
    greatest failure. 26 consecutive days of zero drain alongside daily re-trigger cohorts
    is not a system managing a backlog; it is a system whose backlog is managing it.
    What would need to be true for C2A2 to be safe: that service rate exceeds arrival rate
    over any sustained window, so the queue is transient and re-triggering merely reorders
    work that will be done anyway. The measured 26-day drain of zero falsifies this.
    How to test: in-house and cheap. Compute items dispositioned per day against items
    queued per day over the last 30 days. If the ratio is below 1, the queue is unstable
    and no amount of re-triggering is progress.
