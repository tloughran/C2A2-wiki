SEARCH-AGAINST-PRESUMPTION-462:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-462
  Original statement: "Fixed re-check cadences (7-day reviewer staleness rule; weekly 15d re-trigger) are right-sized — set once, never load- or change-rate-adapted."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-462
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, MEDIUM-HIGH, from 2026-07-08 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Juniper Networks. "sFlow Dynamic Polling and Adaptive Sampling Interval Overview." Junos OS documentation. — Production networking design: polling intervals are dynamically adjusted to load (lengthening under high interface counts, shortening when load falls) because fixed intervals either waste capacity or fall behind — the exact dichotomy a fixed weekly re-trigger faces as queue depth changes.
    2. Adaptive-polling literature (e.g., US Patent 8,724,612, "Adaptive timers for polling in a mobile wireless device"; ResearchGate, "Adaptive polling interval scheduling to support real-time service in Bluetooth networks"). — Quantified result: adaptive polling detects completion with 44-89% fewer polls than fixed periodic polling, and a fixed interval cannot simultaneously bound delay and avoid wasted checks — right-sizing a fixed cadence is impossible when the underlying rate varies.
    3. Slimmon, D., 2016/2022. Little's Law queue analyses (blog.danslimmon.com). — When arrival rate exceeds what a fixed-cadence service schedule can process, the queue grows without bound; cadence is a component of service capacity, so a load-blind cadence guarantees divergence whenever load drifts upward. C2A2's own 15d queue growth under the weekly cadence is a live instance.

  Strength of challenge: Moderate

  Summary: The scheduling and monitoring literature converges on a simple structural point: a fixed interval encodes a frozen guess about a variable rate, and it is wrong in one of two directions the moment the rate moves — too frequent (wasted checks, fatigue) or too infrequent (backlog growth, stale detection). Adaptive schemes exist in every mature polling domain because the optimum tracks load and change-rate. Both of C2A2's cadences show the mismatch already: the weekly 15d re-trigger admits ~55 items/week against a smaller per-run burn (queue growing — cadence too slow for the load), while the 7-day reviewer staleness rule fired with 13 proposals pending (staleness declared, nothing adapted — a detector with no actuator). The deeper challenge is to "set once": even a correct initial cadence decays as the system's scale changes, and this system is visibly scaling. Challenge is Moderate: fixed cadences are not inherently wrong, only load-blind ones in variable-load regimes, and simplicity has real value.

  Specific risks: Cadence-load mismatch compounds silently — each week the fixed re-trigger adds more than a run removes (ASSUMPTION-429's observed growth is this presumption's failure signature); the staleness rule degenerates into a ritual warning (feeding ASSUMPTION-428's normalization dynamic); as the wiki and thinker count grow, every fixed interval in the system drifts further from right-sized with no mechanism to notice.

  Mitigations available: Make cadences functions of observables: re-trigger cadence/batch size keyed to queue depth (e.g., run again or enlarge batch when depth > N); staleness rule keyed to pending count as well as age (escalate when both breach); cheap middle ground — keep fixed cadences but add a quarterly cadence-review that compares each interval against measured arrival/burn rates; alarm when any queue's depth trend is positive across 3 consecutive cycles.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Fixed cadences are predictable, trivially implementable, auditable, and free of the failure modes adaptive controllers introduce (oscillation, feedback bugs, unobservable scheduling state) — for a single-operator system, a weekly rhythm the human can anticipate is worth more than a theoretically optimal adaptive interval. The observed queue growth indicts the cadence's current VALUE, not fixedness itself: bumping to twice-weekly and staying fixed might fully solve the problem with none of the adaptive machinery.
    What would need to be true for C2A2 to be safe: Load and change-rate must be roughly stationary (they are visibly not — the system is growing); OR a human-in-the-loop periodic review must effectively serve as the slow adaptive layer, actually re-sizing cadences when queues trend upward; queue-depth trends must be surfaced so the review has the data.
    How to test: Retrospective: plot 15d queue depth against the weekly cadence over the past month — sustained growth proves current mis-sizing. Prospective: double the cadence (or batch size) for three weeks and observe whether depth stabilizes; then decide fixed-but-resized vs adaptive on the measured sensitivity.
