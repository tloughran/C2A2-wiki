SEARCH-AGAINST-PRESUMPTION-863 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-09
  Original item: PRESUMPTION-863
  Original statement: [inferred] Per-run caps are presumed to be constants of the system rather than
    parameters of it, so a queue diagnosed as undrainable is reported rather than re-scoped.
  Under test this cycle (MONITOR-549): the AUTHORITY limb only — who holds the cap, and whether an
    agent's re-scoping request has any route to that party. Owed: control-theoretic software
    adaptation, autoscaling, decentralised decision rights, Kanban/CONWIP admission policy. The
    arithmetic limb is settled (PREMISE-106) and was NOT re-searched.

  NOTE ON CYCLE STATUS: the cycle-0 15b file (2026-08-25) was a DECLARED NON-SEARCH (WebSearch budget
    exhausted; four of seven sources stated from background knowledge). This is therefore the first
    15b pass on this item that executed queries. Nothing in the cycle-0 15b file is treated here as
    evidence.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today. I read the 15a cycle-0 summary only as
    reproduced inside MONITOR-549 (permitted).

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-863
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-08-23): Inferred from three same-day reports treating per-run caps as terrain
        ("At 6 pairs/run this task cannot drain it") with no proposal to re-scope.
      15a (cycle 0): PARTIALLY-SUPPORTED — strong on arithmetic; authority limb by MAPE-K analogy only.
      15b (cycle 0, 2026-08-25): DECLARED NON-SEARCH (budget exhausted); recorded as absent reading.
      15c: → MONITOR-549 (authority limb only under monitoring).
      15d (2026-09-13): Re-triggered, cycle 1; owed = authority-limb literature on fresh budget.
      15b (re-trigger cycle 1, 2026-10-09): 3 searches (CONWIP/WIP-cap setting; control-theoretic
        autoscaling stability; decentralised MAPE-K loop interference); 2 fetches (Wikipedia CONWIP,
        full text of a short article; Arcaini et al. 2017 abstract page).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Two fetched pages (one encyclopaedic, one abstract); remainder
    search-result level. No primary control-theory paper read end to end.

  Challenging evidence found: Partial — against the implied remedy (that the cap should be adjustable
    by, or on request of, the agents that encounter it), NOT against the claim that the cap is unowned.

  Sources:
    1. Spearman, M. L., Woodruff, D. L. & Hopp, W. J. 1990. CONWIP: a pull alternative to kanban.
       (via Wikipedia "CONWIP") [fetched, full text of the encyclopaedia article; primary not read]
       In CONWIP "no part is allowed to enter the system without a card (authority)"; the card count
       is the single system-level WIP control and is "easier to implement and adjust" than per-station
       kanban. Bearing: in the canonical admission-control design the cap is DELIBERATELY a constant
       during operation — constancy is the mechanism, not an oversight — and adjustment is a
       system-level act on one parameter, not something a station negotiates. An undrainable queue at
       a fixed cap being "reported rather than re-scoped" by the worker is exactly what CONWIP
       prescribes for the worker.
    2. Hopp, W. J. & Roof, M. L. 1998. "Setting WIP levels with statistical throughput control (STC)
       in CONWIP production lines." International Journal of Production Research. [search-result —
       citation only; findings NOT seen] Bearing: the literature treats WIP-level setting as a
       separate, slower, statistically-triggered outer process. This is a challenge to any reading of
       PRESUMPTION-863 that wants per-run re-scoping; it is consistent with (not against) the claim
       that SOMEONE must own the outer loop.
    3. Arcaini, P., Riccobene, E. & Scandurra, P. 2017. "Formal Design and Verification of
       Self-Adaptive Systems with Decentralized Control." ACM TAAS 11(4), 25:1–25:35.
       doi:10.1145/3019598. [fetched, abstract] "The design of complex distributed self-adaptive
       systems having decentralized adaptation control by multiple interacting MAPE components is
       among the major challenges"; the paper exists to discover "unexpected interfering MAPE-K
       loops." Bearing: distributing cap-adjustment authority across the agents that each see a
       backlog creates multiple interacting loops over shared capacity — a recognised hazard needing
       formal verification. Decentralised decision rights are not a free remedy.
    4. Control-theoretic autoscaling stability literature (search-result level only): MAS-H2
       hierarchical multi-agent autoscaling, arXiv:2603.07607 (stability "once hysteresis oscillations
       die out"); complex-stability orchestration, arXiv:2605.08139 (reports VM "flapping" reduction;
       argues orchestrators need formal stability constraints); DDQN autoscaling, arXiv:2609.14894
       (adds a fixed 60 s control interval for stability); survey arXiv:1608.05917 (control-theoretic
       methods need many actuations on the real system to stabilise). [search-result; none fetched;
       headline figures unverified] Bearing: in the domain where "caps as parameters" is most
       developed, the dominant engineering problem is oscillation from adjusting too readily, and the
       standard cures are hysteresis, damping windows and fixed control intervals — i.e. holding the
       parameter constant for a run. A per-run re-scoping regime driven by each run's own backlog
       diagnosis is a textbook flapping configuration.
    NOT FOUND: any source that locates cap-adjustment authority as a DESIGN OBLIGATION (MONITOR-549's
       INCORPORATE condition). The decentralised-MAPE literature I reached frames authority
       allocation as a coordination/verification problem, not an obligation; the CONWIP literature
       assumes a single system owner without arguing for one. This is a null from a preliminary
       search, not a declared negative.

  Strength of challenge: Weak-to-Moderate

  Summary: The literature does not challenge the core of the authority limb — that a cap no one owns
    cannot be tuned — and nothing found argues that an unowned parameter is acceptable. What it does
    challenge is the presumption's implied diagnosis that treating the cap as a constant WITHIN a run
    is itself the defect. In CONWIP the fixed card count is the control, and in autoscaling the
    principal failure of adjustable caps is oscillation, cured by holding the parameter fixed across
    a control interval and adjusting it in a slower outer loop. Decentralising adjustment authority to
    the agents that observe backlogs is, per the MAPE-K literature, a source of interfering loops. The
    defensible reading is therefore two-timescale: caps constant per run (correct), parameter of a
    slower owned outer loop (missing). That is PREMISE-119's "assign an owner" requirement, and points
    toward MONITOR-549's CLOSES-WITH-NO-MINT branch rather than INCORPORATE.

  Specific risks: (i) if the item is resolved by granting per-run re-scoping authority to agents,
    expect cap flapping and agents competing for shared review/human capacity (interfering loops);
    (ii) if resolved by "assign an owner" with no trigger rule, the outer loop never fires — the
    STC-style statistical trigger (Hopp & Roof) is the missing piece, not authority per se;
    (iii) the 15a authority finding and this file both rest on analogy to manufacturing/cloud
    domains in which arrival processes are exogenous; in C2A2 the agents generate their own arrivals,
    which neither literature models.

  Mitigations available: two-timescale design — fixed per-run cap plus an owned outer loop with an
    explicit trigger (e.g. backlog monotone for N runs, λ/μ > 1 over a window) and a hysteresis band;
    a single named owner (Tom, per MONITOR-549's REVISE branch) rather than distributed authority; run
    MONITOR-549's in-house trace before any further literature work.

  Recommendation: PARTIALLY-CHALLENGED — the authority gap stands unchallenged; the reading that
    per-run constancy is the defect is challenged. Search scope: preliminary — broader search
    recommended only if the in-house trace does not settle it (Hopp & Roof 1998 and Hellerstein et al.
    "Feedback Control of Computing Systems" are the unread primaries).

STEELMAN:
  Item: PRESUMPTION-863 (authority limb)
  Strongest counterargument: A cap that does not move during a run is not "terrain mistaken for a
    parameter"; it is the standard way every mature admission-control discipline prevents oscillation.
    CONWIP fixes the card count precisely so that workers do not negotiate it, and autoscaling
    practice spends most of its effort stopping controllers from adjusting too eagerly. An agent that
    reports an undrainable queue instead of re-scoping is behaving as a well-designed inner loop
    should; the defect, if any, is the absence of an outer loop, and that is already named by
    PREMISE-119. Minting a new item would double-count it.
  What would need to be true for C2A2 to be safe: an outer loop exists with a named owner, a trigger
    condition and a hysteresis band, and the three same-day reports are inputs to it.
  How to test: MONITOR-549's trace — did any of the three same-day reports change a cap, a schedule
    or a staleness window within 30 days? Zero changes = no outer loop (routing gap confirmed);
    any change = outer loop exists and the item closes into PREMISE-119.
