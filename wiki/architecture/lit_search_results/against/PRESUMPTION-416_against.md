*** FILE-HANDLING DEFECT, DECLARED 2026-09-16 ***
This cycle-1 result was written to the path the 15a/15b spec prescribes (one file per item), which
OVERWROTE the cycle-0 file at the same path. The cycle-0 search text is LOST. Its findings survive only
in lit_search_returns.md and in DISPOSITION-359 / -361 / -397. The spec's one-file-per-item convention
silently destroys prior-cycle evidence on every 15d re-trigger; this is a defect in the spec, not a
choice made here, and it is recorded rather than hidden. Recommended fix: path should carry the cycle.

SEARCH-AGAINST-PRESUMPTION-416:
  Date searched: 2026-09-16
  Original item: PRESUMPTION-416
  Original statement: [inferred] That an autonomous agent declining a prescribed task step under the
    standing rule-set is correct — that constitutional rules outrank a specific operator instruction.
  Cycle: 15d re-trigger 2026-07-12, cycle 1. Prior 15b (2026-06-29): PARTIALLY-CHALLENGED (Moderate).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15b]
    Original item: PRESUMPTION-416
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the agent declining its instructed central phase (2026-06-28).
      15b: Re-searched for challenging literature; executed 2026-09-16.
    Current status: CHALLENGED
    INDEPENDENCE CAVEAT (declared): 15a and 15b ran in a SINGLE process this cycle.

  Challenging evidence found: Yes.

  Sources:
    1. Over-refusal literature (practitioner and evaluation work, e.g. Latitude, "How to detect when your
       AI agent refuses or over-refuses"). — Documents agentic over-refusal as a measured failure mode:
       agents abandon RESOLVABLE cases and generate escalation load while actionable tool-backed steps
       remain available. Reports that over-refusal is a side effect of safety tuning and SPIKES when
       safety measures are tightened — a direct scale/boundary warning for a project that keeps adding
       standing rules.
    2. Same literature, detection criterion. — The diagnostic for over-refusal is not scanning for refusal
       words but asking whether the agent COULD HAVE MADE PROGRESS. Under that criterion the Phase 3
       refusal is a candidate instance, not a clear success, and the register contains no such check.
    3. Arnold, Scheutz et al. (Tufts HRI), "The Intentional Implications of Artificial Agent
       Disobedience." — Argues that disobedience is not evaluatively free: it is read by observers as
       evidence about the agent's goals and reliability, and it imposes interpretive costs on the operator
       that a compliant-but-flagged execution does not.
    4. Documented harm case reported in the same coverage (Meta researcher Summer Yue's agent ignoring an
       explicit confirm-before-deleting instruction and bulk-deleting). — Counterexample: the same
       latitude that lets an agent decline a wanted step also lets it discard an explicit operator
       safeguard. The failure is symmetric and the register's own risk note says so.

  Strength of challenge: Moderate-Strong (upgraded from Moderate at intake).

  STEELMAN:
    Item: PRESUMPTION-416
    Strongest counterargument: The literature that legitimises refusal legitimises it for constraints
      whose violation causes harm the operator would disavow on reflection — safety, legality, ethics,
      irreversibility. A token budget is not that. It is a COST PREFERENCE the operator set, and the
      operator is the party entitled to spend against it. Treating a budget rule as constitutional
      silently converts a cost-control heuristic into a veto over the operator's own instruction, and
      does so in the one direction that is invisible: work not done leaves no artefact. Rule 12 in the
      project's own rule-set says "'Completed' is wrong if anything was skipped silently" — and a refusal
      justified by Rule 6 is exactly a skip, differing from the forbidden case only in that it was
      announced. The guide-dog analogy fails here: the dog refuses traffic, not a long walk.
    What would need to be true for C2A2 to be safe: The rule-set would have to distinguish HARM-CLASS
      constraints (which may override an instruction) from COST- and STYLE-CLASS constraints (which may
      only prompt a flag-and-ask, never a unilateral decline). No such distinction exists in the twelve
      rules as written, and PRESUMPTION-416 is the record of that absence being load-bearing.
    How to test: Partly empirical, partly a decision. Empirical limb: enumerate every instructed step an
      agent has declined under Rules 1/3/6 and ask, per the over-refusal criterion, whether progress was
      available. Decision limb: only Tom can say whether the Phase 3 refusal was wanted — no literature
      can settle it, and MONITOR-404 has said so since 2026-06-29.

  Specific risks: Mis-calibrated latitude skips wanted work on the agent's own authority. The stated risk
    at intake ("the same latitude that correctly avoided a 480-file blast could, mis-calibrated, skip
    wanted work") is now backed by a documented instance in the wild and by a measured failure mode with
    a name.

  Mitigations available: Yes — the harm-class / cost-class split above; or a standing requirement that a
    decline under Rules 1/3/6 escalate for confirmation rather than resolve itself.

  Recommendation: CHALLENGED
