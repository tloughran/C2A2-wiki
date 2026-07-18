SEARCH-AGAINST-ASSUMPTION-430:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-430
  Original statement: "Priority-ordered partial burn (HIGH tier end-to-end, remainder waits, residue surfaced) is acceptable triage for an over-capacity queue."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-430
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, MEDIUM, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Silberschatz, A., Galvin, P., Gagne, G. "Operating System Concepts" (priority-scheduling chapter; standard OS literature, see also cs.uic.edu Bell course notes, "CPU Scheduling"). — Canonical result: strict priority scheduling in a loaded system produces indefinite blocking (starvation) of low-priority work; the standard, required complement is aging — waiting time must eventually raise an item's effective priority.
    2. "Aging (scheduling)." Wikipedia / OS references (en.wikipedia.org/wiki/Aging_(scheduling)). — Aging is defined as the mechanism that guarantees every request eventually becomes highest-priority after waiting long enough; priority scheduling without it has no such guarantee by construction.
    3. GeeksforGeeks, "Starvation and Aging in Operating Systems"; UC Berkeley CS162 discussion notes on starvation. — Teaching-canon treatments: in an over-capacity system (the exact condition stated in the claim), "remainder waits" is not a bounded wait — under sustained overload it is an unbounded wait, i.e., starvation with extra steps.

  Strength of challenge: Strong

  Summary: The scheduling literature accepts priority-ordered partial burn as sound triage under ONE condition the claim omits: an aging mechanism. In a queue that is over capacity every cycle (which ASSUMPTION-429 asserts is the standing condition), "the remainder waits" means MEDIUM/LOW items wait behind next week's fresh HIGH arrivals, and the week after's — strict priority plus sustained overload equals indefinite starvation of the lower tiers, by construction rather than by accident. Surfacing the residue does not bound the wait (see ASSUMPTION-428: surfaced deferrals normalize). The scheme also inherits PRESUMPTION-459's flaw: an item starved for weeks retains its queue-time LOW label even if the world has made it urgent. Triage per se is not challenged; triage without aging in a persistently overloaded queue is.

  Specific risks: MEDIUM/LOW self-awareness items are never processed — effectively a silent policy that only HIGH items exist; slow-burning risks that were correctly triaged MEDIUM at intake mature into incidents while starving in the queue; the surfaced residue list grows until it is itself ignored (alert fatigue), and the tier labels lose meaning because lower tiers carry no processing promise at all.

  Mitigations available: Aging: promote any item that survives N cycles un-burned one tier per period, guaranteeing eventual processing; reserved-capacity variant: each run spends a fixed minority quota (e.g. 20%) on the oldest non-HIGH items; queue-age SLO with alarm when the oldest waiting item exceeds a bound; periodic re-triage of the residue rather than static carry-forward.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Triage exists because under scarcity, treating everything is worse than treating the most important things — emergency medicine and incident response both run priority-ordered partial service deliberately. If the priority assignment is accurate and the important tail of the distribution is short, starving LOW items may be the correct outcome, not a failure: many LOW self-awareness items lose relevance on their own, and processing them would spend scarce capacity on work whose value has expired. "Residue surfaced" keeps the option to promote anything that turns out to matter.
    What would need to be true for C2A2 to be safe: Priority labels at queue time must be accurate AND remain accurate over multi-week waits (contradicted risk: PRESUMPTION-459); the overload must be temporary rather than standing (contradicted risk: ASSUMPTION-429); items must genuinely lose value with age so starvation approximates garbage collection; someone must actually read the residue list and occasionally promote from it.
    How to test: Compute the age distribution of the current residue and count how many non-HIGH items have EVER been burned across all runs. If that count is zero and residue ages grow linearly, starvation is operating and the acceptability claim fails on this system's own data.
