SEARCH-AGAINST-PRESUMPTION-891:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-891
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium-High)
  Original statement: [inferred] That an agent's intake channels define its world — that bulk state changes
    occurring outside those channels need not be detected.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-891
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an idle report and a day of maximal activity coinciding, with the run's own stale
        WATCH-003 reading as corroboration.
      15b: Searched for challenging literature
    Current status: CHALLENGED — and the challenge carries the remedy

  Search scope: WebSearch, 2026-08-28, one dedicated query on level-triggered vs edge-triggered
    reconciliation. Reached: James Bowes, "Level Triggering and Reconciliation in Kubernetes" (HackerNoon);
    Kopf documentation on reconciliation; golinuxcloud's reconcile-loop explainer and its companion on
    reconcile-loop explosions; Tony De La Nuez on solid Kubernetes controllers; a blog on tracing
    edge-triggered systems. NOT COVERED: Hanks' and the original Borg/Kubernetes design papers, where the
    level-triggered argument is made in primary form. All SNIPPET-ONLY. Confidence: MODERATE-HIGH — this is
    a well-settled engineering distinction and the practitioner sources agree closely.

  Challenging evidence found: Yes — strongly

  Sources:
    1. Bowes, J., "Level Triggering and Reconciliation in Kubernetes" [SNIPPET-ONLY]
       https://medium.com/hackernoon/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d —
       The distinction: edge-triggered systems react to changes; level-triggered systems continuously compare
       current state to desired state. The thermostat, not the motion sensor.
    2. golinuxcloud, "Kubernetes Reconcile Loop Explained" [SNIPPET-ONLY]
       https://www.golinuxcloud.com/kubernetes-reconcile-loop-explained/ ; Kopf documentation,
       "Reconciliation" [SNIPPET-ONLY] https://docs.kopf.dev/en/stable/reconciliation/ —
       The decisive property, stated plainly: "if you miss an event, the next reconciliation catches it
       anyway," whereas in a purely edge-triggered system a missed event means a permanently missed action.
       Kubernetes controllers are event-*triggered* but level-*based*, and that single choice is why they
       survive missed events, partitions and restarts.
    3. Tony De La Nuez, "Fundamentals for solid kubernetes controllers" [SNIPPET-ONLY]
       https://tdoot.com/writing/building-solid-kubernetes-controllers/ —
       Adds the cost boundary: do not busy-loop; sub-10-second polling is wasteful, and watch-based triggers
       are preferred where the source can emit events. The remedy is not "poll everything."

  Strength of challenge: Moderate-Strong

  Summary: The presumption describes a design choice as though it were a necessity, and the distributed-
    systems literature has both the name for the choice and the standard alternative. An agent whose world is
    its intake channel is edge-triggered: a change that arrives outside the channel is missed permanently,
    because nothing ever re-asks. The level-triggered pattern — re-read the state of record on every run and
    compare it to what the agent believes — costs one read per cycle and converts a permanent miss into a
    one-cycle delay. Two of the estate's demonstrated failures are exactly the predicted symptom: an idle
    report issued on a day of maximal activity, and a stale WATCH-003 that no event ever refreshed. This is
    the one item in the cohort where the against direction found not just a challenge but a specific, cheap,
    well-attested fix.

  Specific risks: Leaving the presumption in place means every state-reading agent in the estate remains one
    missed event away from a permanently wrong belief, with no mechanism that would ever correct it. The
    2026-08-26 miss and the stale watch are not two incidents; they are two instances of one architecture.

  Mitigations available: Convert state-reading agents from edge-triggered to level-triggered: on each run,
    re-derive the relevant state from the artifacts of record rather than from the queue of arriving items,
    and reconcile. Keep event triggers for latency; do not use them for truth. Cost is one directory read per
    agent per run.

  STEELMAN:
    Item: PRESUMPTION-891
    Strongest counterargument: Level-triggered reconciliation requires a well-defined "state of record" to
      reconcile against. Kubernetes has one — the API server's object graph — and this estate does not: its
      state is spread across markdown registers with at least three different block shapes, inconsistent tag
      placement, and a queue file where the same status marker appears on three kinds of line. Reconciling
      against that is not one read, it is a parsing project, and an agent that reconciles against a
      mis-parsed state is worse than one that waits for events.
    What would need to be true for C2A2 to be safe: there would have to be a canonical, parseable state of
      record per agent. For some agents (file presence in `changelog/`, `metrics/`) there already is, and
      those should convert first.
    How to test: pick the cheapest case — the pipeline-health monitor — and have it list the output
      directories on every run instead of reading the scheduler. If that one conversion catches the 08-26
      class of failure, the pattern is validated at a cost of one directory listing.

  Recommendation: CHALLENGED
