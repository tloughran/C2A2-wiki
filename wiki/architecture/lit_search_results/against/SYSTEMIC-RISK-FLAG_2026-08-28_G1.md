SYSTEMIC-RISK-FLAG:
  Date: 2026-08-28
  Filed by: Agent 15b (literature search AGAINST), 2026-08-27 intake cohort
  Affected items: ASSUMPTION-1230, PRESUMPTION-890, PRESUMPTION-891 (primary);
    ASSUMPTION-1232 and PRESUMPTION-879 (secondary, via the escalation limb)

  Common vulnerability: **The estate's monitors read proxies and are triggered by events rather than by
    state.** Three of this cohort's items are the same defect seen from three angles: a health check that
    reads a scheduler instead of the artifacts (ASSUMPTION-1230); a monitor that treats job liveness as
    output and reports green while declaring its own read failure (PRESUMPTION-890); and an agent whose
    intake channel defines its world, so that a change arriving outside the channel is missed permanently
    (PRESUMPTION-891). An edge-triggered instrument reading a proxy has two independent ways to be wrong at
    once and no mechanism that would ever correct either.

  Demonstrated instance, in-house, not hypothetical: the 2026-08-26 pipeline produced no outputs in
    `changelog/` or `metrics/`. The health check reported green. The absence was found on 2026-08-27 by a
    human-directed directory listing, roughly 24 hours later. The same architecture produced a stale
    WATCH-003 and an idle report issued on a day of maximal activity.

  Literature basis:
    - Level- vs edge-triggered reconciliation: Bowes, "Level Triggering and Reconciliation in Kubernetes";
      Kopf documentation, "Reconciliation"; golinuxcloud, "Kubernetes Reconcile Loop Explained".
      "If you miss an event, the next reconciliation catches it anyway" — in a purely edge-triggered system
      a missed event means a permanently missed action. [all SNIPPET-ONLY]
    - Liveness vs correctness: Dumont, "Health Checks That Actually Work"; Frontiers in Computer Science
      (2026), doi:10.3389/fcomp.2026.1811944; web-alert, "Black-Box vs White-Box Monitoring". [SNIPPET-ONLY]
    - Absence detection: Crontap, "Dead man's switch, explained for developers"; Kriss-V, `deadmancheck`;
      Datashelter, "Backup Monitoring: Solving the Dead Man's Switch Problem" — "the first sign of failure
      is silence." [SNIPPET-ONLY]
    - Limits of the naive fix: Splunk, "Assert Like You Mean It" — a test without assertions "can pass even
      when functionality is broken." [SNIPPET-ONLY]

  Risk level: High

  Why it is systemic rather than three bugs: the three items would each be closed by a different local patch,
    and all three patches would leave the shared property intact. The shared property is that instruments in
    this estate are permitted to (a) infer output from a proxy and (b) hold a belief that no later run
    re-derives. Any new monitor built on the current pattern inherits both.

  Recommendation (three changes, in cost order, cheapest first):
    1. **A monitor that cannot read its source reports UNKNOWN, never green.** One-line semantics change.
       This is the highest value-per-cost item in the cohort and it closes the undefended limb — no source
       in either direction defends a green verdict from a self-declared-blind instrument.
    2. **Assert on a content property that cannot occur by accident** — the run date inside the artifact, a
       non-zero item count — rather than on file existence. Existence checks are the same class of
       instrument as the scheduler check they would replace.
    3. **Convert state-reading agents from edge-triggered to level-triggered**: on each run, re-derive the
       relevant state from the artifacts of record and reconcile, rather than reacting only to items
       arriving in an intake channel. Start with the pipeline-health monitor, where the state of record is
       already a parseable directory listing. Cost: one listing per run.

  Known objection, recorded: the estate lacks a canonical parseable state of record for most agents (the
    queue file alone carries the `[QUEUED]` marker on three different line shapes), so full level-triggering
    is a parsing project, not a one-line change. This is why recommendation 3 is scoped to the cases where a
    clean state of record already exists.

  Routed to: 15c for disposition; cross-referenced from ASSUMPTION-1230_against.md, PRESUMPTION-890_against.md
    and PRESUMPTION-891_against.md.
