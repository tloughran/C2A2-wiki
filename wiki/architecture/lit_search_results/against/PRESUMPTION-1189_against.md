# PRESUMPTION-1189 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Run id sched-lit-2026-10-27-6d9c5b33. Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": evidence that the concern about a co-located watchdog is overstated, or that the implied remedy (external dead-man's-switch or absence-of-signal alerting) is weaker or harder than the item assumes. I did not dispute the in-house facts: the apparent 10-19..10-23 gap and the watcher being silent since 10-06.

```
SEARCH-AGAINST-PRESUMPTION-1189:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1189
  Original statement: "[inferred] The watchdog is presumed able to report the absence of what it
    watches. Scheduler health runs from the same scheduler it monitors. ... Morning status reads
    'everything due overnight fired on time' as health."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1189
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the outage surfacing only through a weekly timestamp report and the
           cloud-routine watcher's silence.
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial. Nothing contradicts the diagnosis. Practitioner sources
    bound the remedy.

  Sources:
    1. Absence-alerting practice: Robust Perception, "Absent alerting for jobs"; PromLabs (2023)
       "Dealing with Missing Time Series in Prometheus"; sapcc absent-metrics-operator README;
       OneUptime (2026-09-23) on zero vs missing series. [snippet only; practitioner/vendor]
       — Bounding challenge to the remedy. Absence alerting is standard but known to be fragile.
       Alerts on a value silently never fire when the series is missing. Sparse or legitimately
       absent signals cause false alarms. Hand-written absence rules drift, which is why tools
       generate them. "The hard part is choosing an expectation source that remains present when
       the monitored metric disappears." So an external heartbeat is not enough. Its schedule of
       expected check-ins must also live outside the monitored scheduler, or a deregistered task
       goes missing from both the signal and the expectation.
    2. Alarm-fatigue literature (ICU physiologic monitoring, e.g., the UNC/Zègre-Hemsey study;
       AHRQ PSNet "Harm from alarm fatigue"), plus a DEV Community piece on dead man's switches
       for monitoring stacks. [snippet only; clinical results are an analogy]
       — Boundary. In a 31-day ICU study, 88.8% of arrhythmia alarms were false and
       desensitised staff. On a laptop-hosted scheduler that sleeps, heartbeat misses will often
       be benign, so a naive dead man's switch can generate noise and be ignored. The DEV piece
       supports the item's core point (the watcher must not depend on the watched stack). That
       is confirmation, noted here only for completeness.

  Strength of challenge: Weak. The co-located-watchdog blind spot is well recognised, and I
    found nothing disputing it. The challenge is only that absence alerting is error-prone and
    noisy, so adopting it is not sufficient on its own.

  Summary: The literature agrees with the presumption's concern. Where it pushes back is on the
    implied remedy: absence detection needs an expectation registry independent of the monitored
    system, tolerance for legitimate absence (host asleep), and alert-volume control. Without
    these, an external watcher either misses tasks that were never registered or produces alarms
    that get ignored. The "apparent" 10-19..10-23 outage also shows that absence inferred from
    timestamps can be ambiguous: a true outage, a sleeping host, or a reporting gap.

  Specific risks: (a) An external heartbeat that alarms on every sleep cycle is soon ignored.
    (b) An expectation list derived from the scheduler's own task registry shares its failure.

  Mitigations available: Keep a static expected-run manifest outside the scheduler. Set a grace
    window that matches host sleep patterns. Separate "host was off" from "task did not fire"
    using a host-uptime signal. Send a daily digest rather than per-miss pages.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1189
  Strongest counterargument: Moving the watchdog outside the scheduler fixes shared fate but
    does not fix how expectations are defined. Absence alerting is a well-known source of both
    silent misses and false alarms. On an intermittently sleeping personal machine, a naive
    external switch would cry wolf often enough to be ignored, as in clinical monitoring.
  What would need to be true for C2A2 to be safe: the watcher, its expected-run manifest and its
    alert channel all sit outside the scheduler. Grace windows reflect host uptime. False-alarm
    rate is tracked.
  How to test: Replay 10-01..10-26 run logs against a candidate manifest and grace window. Count
    true misses caught versus benign sleep-induced alarms.
```

Source quality: all snippet only. I did not read the Google SRE book directly, so black-box monitoring claims are UNVERIFIED and not relied on here.
