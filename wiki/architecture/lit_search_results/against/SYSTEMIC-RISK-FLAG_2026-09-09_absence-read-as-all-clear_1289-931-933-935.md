SYSTEMIC-RISK-FLAG:
  Date: 2026-09-09
  Filed by: Agent 15b (Literature Search AGAINST), run on the 2026-09-08 end-of-day intake
  Affected items: PRESUMPTION-931, PRESUMPTION-933, PRESUMPTION-935; ASSUMPTION-1289 as the reflexive
    case

  Common vulnerability: **Absence read as all-clear.** In all four items the estate treats a *missing
  record* as a *record of nothing having happened*, and in every case the missing record is one that
  the party being evaluated was supposed to write about itself. The estate has no channel that reports
  absence, so absence is silently converted into good news at the point of reading.

    - PRESUMPTION-931: no freshness complaint in the 08:00 summary is read as no staleness. The summary
      asks whether jobs fired; it does not ask, and cannot see, whether outputs changed. Five freshness
      FAILs existed on the same estate ninety minutes later.
    - PRESUMPTION-933: no terminal verdict from a scheduled run is read as an uneventful run.
      `metabolism-regen-daily` wrote no verdict under a fail-loud spec and `morning-system-health`
      stalled at a permission prompt; both were counted as fired, by every consumer.
    - PRESUMPTION-935: no closure record against a recommendation is read as nothing outstanding. Four
      sewing recommendations have been NOT DONE since 08-09/08-16/08-23, REVISE-436 sits at a fifth
      unruled cycle, and 2,111 bare-`[QUEUED]` tags carry an oldest item from 2026-07-05 — none of
      which generates an event.
    - ASSUMPTION-1289: no measured effect for a control is read as the control working. This is the
      same move at the level of mechanism credit, and yesterday's flag already named it. It is included
      here because it is the general form: the four together show that the estate applies the
      absence-is-fine rule to run status, to output health, to recommendation closure, and to control
      efficacy — i.e. at every layer at which it observes itself.

  The four therefore share a single structural defect: **every channel by which the estate learns about
  itself is written by the thing it reports on, and none of them can emit "no record."** A silent agent
  writes no failure. A stale output writes no complaint. An unactioned recommendation writes no
  reminder. An unmeasured control writes no doubt. Each of these is a case where the signal and its
  own absence are indistinguishable to the reader — which means the estate's apparent health is
  bounded above by its instrumentation and has no lower bound at all.

  Literature basis:
    - Huang, P., Guo, C., Zhou, L., Lorch, J.R., Dang, Y., Chintalapati, M. & Yao, R., 2017. "Gray
      Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS '17, doi 10.1145/3102980.3103005.
      [VERIFIED: full PDF read 2026-09-09] — Names the defect precisely as *differential
      observability*: "a system is defined to experience gray failure when at least one app makes the
      observation that system is unhealthy, but observer observes that system is healthy." Reports that
      "gray failure is behind most cloud incidents," that fail-stop-assuming mechanisms "are inadequate
      … and in some cases even aggravate the situation," and — closing off the only available defence
      — that "gray failure is not unique to large systems. Small-scale or even single-node systems can
      also experience peculiar failure symptoms." Their prescription is the remedy for all four items at
      once: "moving from singular failure detection (e.g., with heartbeats) to multi-dimensional health
      monitoring."
    - HHS Office of Inspector General, 2012. "Hospital Incident Reporting Systems Do Not Capture Most
      Patient Harm," OEI-06-09-00091. [VERIFIED: report page read 2026-09-09] — The magnitude, in the
      only comparable case with a hard denominator. A self-report channel that administrators "rely
      heavily on" captured 14% of actual harm; 61% of the misses were events staff "did not perceive as
      reportable." And for the events that *were* captured and formally investigated, hospitals "made
      few policy or practice changes as a result." The same report supplies the base rate for
      PRESUMPTION-933's detection gap and for PRESUMPTION-935's closure gap.
    - Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed Systems."
      JACM 43(2); with Fischer, Lynch & Paterson, 1985. [PARTIALLY verified — concepts confirmed across
      multiple independent sources; papers not opened 2026-09-09] — The in-principle limb: in an
      asynchronous system a stalled process and a slow one are indistinguishable from outside, and no
      failure detector is both complete and accurate. C2A2's scheduler has no bounded response time, so
      this is not an engineering shortfall to be fixed by better agents; it is a property of the
      architecture, and the only escape is an external timeout that is *allowed to be wrong*.
    - Hallowell, M., Quashne, M., Salas, R., Jones, M., MacLean, B. & Quinn, E., 2020. "The Statistical
      Invalidity of TRIR as a Measure of Safety Performance." CSRA, Univ. of Colorado Boulder.
      [VERIFIED: full PDF read 2026-09-09] — The counterweight, and the reason this flag does not simply
      endorse yesterday's remedy. Over 3.26 trillion worker-hours, "changes in TRIR are due to 96-98%
      random variation," there is "no discernible association between fatalities and TRIR," and
      organisations using it for evaluation "are likely rewarding nothing more than random variation."
      Adding a number where there was an absence is not automatically an improvement: a meaningless
      number reads as a measurement, and a register full of them is a *worse* epistemic state than one
      that visibly lacks them.
    - RCA and accident-investigation follow-up corpora (Joint Commission Journal 2024, 148 corrective
      actions: 97.6% completion for weak actions vs 73.3% for strong; US Chemical Safety Board 1998–2015,
      733 recommendations: 78% implementation for low-impact vs 38% for high-impact; French experience-
      feedback-committee study: implementation deadline defined in only 26% of actions).
      [NOT-verified — all from search-result summaries; PMC and PubMed were behind reCAPTCHA on
      2026-09-09] — The drift limb. Completion runs *inverse* to consequence in two independent
      datasets. Any remedy that measures itself by uptake rate will therefore select for weak items,
      and the estate will get better at closing recommendations while getting worse at changing
      anything.

  Risk level: High

  Why it is systemic rather than three coincidences: The four items sit at four different observational
  layers — output health (931), run status (933), governance closure (935), and mechanism credit
  (1289) — and the identical inference appears at each: *no signal, therefore no condition.* That
  distribution is the signature of a systemic defect. It is not that one monitor is blind; it is that
  the estate has no concept of a negative observation. There is no artefact anywhere in the vault whose
  content is "the thing that should have written here did not." Two further properties make it worse
  than the sum of its parts. First, **correlated failure**: a permission change, a credential expiry, an
  unmounted volume (cf. ASSUMPTION-1287) or a suspended host silences many agents at once, and the
  estate's most likely bad day is therefore also its quietest-looking one. Second, **compounding**: on
  2026-09-08 the liveness channel said all jobs fired (931) while two of those jobs had in fact produced
  nothing (933), and the run that noticed filed four recommendations that nothing is positioned to
  action (935). Three green-looking signals in sequence, each blind to the same event class, each
  inheriting the previous one's blindness. A single instrumented negative observation anywhere in that
  chain would have broken it.

  Recommendation (for 14a/14b/12 to consider; 15b does not make design decisions): Consider one
  cross-cutting mechanism rather than four fixes — **an expectation register with an external reader**.
  For every recurring obligation in the estate (a scheduled run, a declared output, an open
  recommendation, a credited control), record in one place: what is expected, by when, and who reads
  it — where the reader is not the writer. Then the estate's daily question stops being "what was
  reported?" and becomes "what was expected and did not arrive?" Concretely:
    (i)   scheduled runs — an expected-completion window per task; absence of a terminal verdict inside
          the window is itself a recorded event (the dead-man's-switch pattern, accepting per
          Chandra–Toueg that the timeout will sometimes be wrong, because a detector that is sometimes
          wrong strictly dominates one that is structurally blind);
    (ii)  outputs — a declared output per task with a content hash, so "ran" and "produced" are
          separately observable and the fired-and-stale cell becomes countable (this is the same build
          that PRESUMPTION-925's mitigation asked for, and it serves 931 and 933 at once);
    (iii) recommendations — owner and date mandatory at mint time, closure state readable by something
          other than the author, and completion reported *stratified by strength* so the weak/strong
          inversion cannot hide in an aggregate;
    (iv)  controls — per ASSUMPTION-1289, but stratified rather than universal: require the effect
          statistic only where the event count can support one, and label the rest
          *operated-but-unevaluated* rather than forcing them into a binary that would produce noise
          with a decimal point.
  Every one of these is cheap and retrospective — items (i)–(iii) can be computed from data the estate
  already has, over the last 30–60 days, without new instrumentation. The individual result files name
  the specific tests.

  Cross-reference and tension with the 2026-09-08 flag: yesterday's unmeasured-control-credit flag
  proposed a universal per-control effect statistic. The TRIR evidence found today qualifies that
  proposal materially — at this estate's event rates most such statistics would be random variation
  presented as measurement, and three separate literatures (safety clutter, bureaucratisation, audit
  society) predict that a universal measurement mandate produces surface compliance and selects for
  controls that are easy to count over controls that work. The two flags should be reconciled rather
  than stacked. The compatible reading is that the fix for absence-read-as-all-clear is not *more
  numbers* but *an external reader of expectations*: a negative observation is not a statistic and does
  not need a sample size.

  Reflexivity note: this flag is, on its own analysis, an absence waiting to be read — filed into a
  directory whose oldest unconsumed item is 65 days old, by a layer that has just been given evidence
  that high-consequence recommendations are implemented at 38% under far better conditions than these.
  It carries no owner and no date and is therefore an instance of PRESUMPTION-935. It should not be
  credited with force until something outside 15b reads it and says so in writing.
