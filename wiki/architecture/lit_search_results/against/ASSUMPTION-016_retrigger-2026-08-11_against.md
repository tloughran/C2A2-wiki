SEARCH-AGAINST-ASSUMPTION-016:
  Date searched: 2026-08-11
  Original item: ASSUMPTION-016
  Original statement: "Literature search results should gate implementation decisions (a development pause)."
  Cycle: 5 (RE-TRIGGER by 15d, queued 2026-07-05; processed 2026-08-11)

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 5)
    Original item: ASSUMPTION-016
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from evening cowork-to-chat sync 2026-04-13, which recommended pausing Phase 2a pending literature results
      15b (cycle 1, 2026-04): initial challenging search — analysis paralysis, agile counter-evidence, cost of delay
      15d: re-triggered for cycle 5 monitoring
      15b (cycle 5, 2026-08-11): re-searched for challenging literature; checked for new sources since April 2026
    Current status: PARTIALLY-CHALLENGED

  Search scope: Preliminary — broader search recommended. Covered stage-gate critique and Agile-Stage-Gate hybrid literature, analysis-paralysis practitioner literature 2026, cost-of-delay/approval-delay statistics, and 2026 gate-review practice guidance. The peer-reviewed base here is thin and mostly pre-2024 (Cooper's Agile-Stage-Gate work); 2026 material is predominantly practitioner and vendor content, which is weak evidence. A targeted search of R&D management and innovation-management journals (Cooper, Sommer, Edwards) is recommended if this item is to be closed rather than monitored.

  Challenging evidence found: Partial

  Sources:
    1. McKinsey & Company, 2023 (widely cited through 2026 gate-review guidance). — Reports that 70% of strategic projects fail due to approval delays and bureaucracy. Gating is not a neutral safety measure; it has a measured failure contribution of its own.
    2. Cooper's Agile-Stage-Gate literature, as summarised in 2026 practitioner reviews (Coforge; Profit.co; SI Labs "Stage-Gate Process: Guide, Critique, and Alternatives"). — The consensus position is explicitly *not* "gate on evidence before proceeding" but hybrid: gates are retained for portfolio discipline while development proceeds in parallel iterations. Reported outcomes: Siemens cut delays 25%; P&G cut time-to-market 30% after revising gates; hybrid approaches improve time-to-market ~30% at maintained quality. This challenges the *serial* form of ASSUMPTION-016, not gating per se.
    3. SI Labs, "Stage-Gate Process: Guide, Critique, and Alternatives for Service Innovation." — Standard critique: classical Stage-Gate is criticised as too linear, too rigid, and poorly suited to high-uncertainty/exploratory work, which is exactly C2A2's category.
    4. Moosend, 2026. "Analysis Paralysis: Why More Data Doesn't Mean Better Decisions." / monday.com, 2026. "Analysis paralysis 2026." — Practitioner framing of the failure mode: paralysis arises specifically when the cost of a wrong decision feels high, the criteria for a right decision are unclear, and available information keeps expanding without converging. All three conditions describe C2A2's literature pipeline, which has now run five cycles without a stated convergence criterion.
    5. Cycle-1 baseline retained: ISACA 2024 analysis-paralysis anti-pattern; Leadership IQ over-analysis research; the "act on 40–70% of information" heuristic; the mid-size software firm case (year-long design phase, product shipped late and mismatched to evolved needs).
    6. Countervailing note (found and reported for honesty): monday.com 2026 "Gate review in project management" and rework-cost data (up to ~$2M average rework in enterprise Agile transformations driven by missing validation steps) support *some* gating. The 2026 direction of travel is toward AI-augmented gates that surface risk earlier — i.e. faster gates, not fewer.

  Strength of challenge: Moderate

  NEW SINCE LAST CYCLE: Partial. No new peer-reviewed challenging source since April 2026. New in this cycle are 2026-dated practitioner syntheses (monday.com gate-review 2026, moosend 2026, Coforge/Profit.co hybrid comparisons) which restate rather than extend the April position, plus the McKinsey approval-delay figure which was not in the cycle-1 file. The most useful genuinely-new framing is the Agile-Stage-Gate hybrid consensus: the literature does not say "don't gate," it says "don't gate serially." That is a sharper and more actionable challenge than April's blunt analysis-paralysis argument.

  Evidence trajectory (challenging): stable

  Summary: The challenge is real but bounded, and it has not grown since April. The literature does not support abolishing evidence gates; it supports replacing serial gates with parallel iteration plus lightweight decision checkpoints. Applied to C2A2, the target is not the existence of a literature-informed pause but its serial, open-ended form: five cycles with no declared stopping rule, no convergence criterion, and no cost-of-delay estimate is the textbook shape of analysis paralysis as described in the 2026 practitioner literature. The strongest single data point remains McKinsey's 70% figure for approval-delay-driven failure, which reframes gating as a risk rather than a control. Evidence quality on the challenging side is weak (mostly gray literature); this should be stated plainly rather than laundered into a strong claim.

  Specific risks: If false, C2A2 stalls indefinitely in an epistemic loop that feels like diligence. Concretely: the pipeline generates items faster than it retires them, each cycle re-triggers monitored items, and no decision criterion exists that could ever return "proceed." The opportunity cost is the empirical work that would actually resolve most of these assumptions — several items in this very batch specify a one-day test that has not been run in four months. There is also a second-order risk: prolonged gating on LLM-generated evidence (see ASSUMPTION-015) means the delay buys contaminated information, so the project pays the cost of delay without receiving the benefit of evidence.

  Mitigations available: (a) Declare an explicit stopping rule per item — e.g. two consecutive cycles with no new sources closes the item; (b) adopt Agile-Stage-Gate form: proceed with reversible implementation in parallel with literature work, gate only irreversible commitments; (c) estimate cost of delay per gated decision and compare against expected information gain before pausing; (d) distinguish blocking gates (irreversible, high-cost) from advisory gates (everything else) and let advisory gates never block; (e) cap cycles — an item still MONITOR at cycle 5 with a stable trajectory should be closed as "unresolvable by literature search" and routed to empirical test.

  STEELMAN:
    Strongest counterargument: Analysis-paralysis literature is overwhelmingly about *commercial product* decisions where delay has a measurable revenue cost and where being wrong is recoverable. C2A2 is a research and knowledge-construction project where the artefact is a permanent, linked, narrated wiki — errors are not recoverable in the same way, because a false finding propagates into every downstream page that links to it, and retraction cost rises monotonically with time. In that regime the asymmetry favours gating: the cost of delay is a few weeks of personal project time, while the cost of building 33 agents on top of a false unification claim is the whole artefact. Furthermore, the Agile-Stage-Gate literature that appears to challenge serial gating actually *endorses* evidence-based go/no-go decisions at defined points — it challenges bureaucracy, not evidence.
    What would need to be true for C2A2 to be safe: (1) The pause is bounded and has a declared exit criterion; (2) the pause is being used to run tests that could actually change the decision, not to accumulate more literature summaries; (3) the gated decision is genuinely irreversible or expensive to reverse — otherwise gate nothing; (4) cost of delay is being tracked, even roughly.
    How to test: Audit the last three cycles. Count (i) how many gated decisions were actually unblocked by literature evidence, (ii) how many items changed status as a result of a re-trigger, (iii) elapsed time and agent-hours consumed. If re-trigger cycles are producing status changes at a low rate and no gated decision has been unblocked, the gate is not functioning as a decision instrument and ASSUMPTION-016 is falsified in practice regardless of its theoretical merit.

  Recommendation: PARTIALLY-CHALLENGED
