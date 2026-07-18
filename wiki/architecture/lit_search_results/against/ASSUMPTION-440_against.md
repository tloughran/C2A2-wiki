SEARCH-AGAINST-ASSUMPTION-440:
  Date searched: 2026-07-11
  Original item: ASSUMPTION-440
  Original statement: "'lastRunAt is authoritative for *fired*; output files are secondary for *succeeded*; missing output is a warning, not proof' — and unverifiable checks downgrade to 'unverified, not failed.'"

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-440
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Huang, P., Guo, C., Zhou, L., Lorch, J., Dang, Y., Chintalapati, M., & Yao, R., 2017. "Gray Failure: The Achilles' Heel of Cloud-Scale Systems." HotOS 2017. — Introduces "differential observability": the system's own detectors report health while applications experience failure. A liveness signal (lastRunAt) is exactly the detector-side view; treating it as authoritative institutionalizes the gray-failure blind spot.]
    2. [Lou, C., Jing, Y., & Huang, P., 2022. "Demystifying and Checking Silent Semantic Violations in Large Distributed Systems." OSDI 2022. — 109 real-world failures where systems ran and responded (fired, live) while silently violating their semantics; crash/timeout detectors structurally cannot catch the fired-but-failed class, which the study shows is common and long-lived in production.]
    3. [Beyer, B., Jones, C., Petoff, J., & Murphy, N.R., 2016. "Site Reliability Engineering" (Ch. 6, Monitoring Distributed Systems), Google/O'Reilly (sre.google). — Monitoring doctrine: alert on user-visible symptoms/outcomes, not on internal cause-side signals; an execution timestamp is a cause-side signal with no information about outcome quality.]
    4. [TheTrueCode / production health-check literature, 2024-2026 (e.g., "Your Production Health Checks Are Lying to You"; OneUptime, "Health Checks That Distinguish Liveness and Readiness," 2026). — Liveness-only checks that pass while the service cannot do useful work are among the most common documented incident patterns; the industry consensus is that liveness must never be conflated with success, and that "unknown" states in critical checks should page (fail-closed), not downgrade to informational.]
  Strength of challenge: Strong
  Summary: The policy is defensible as epistemology (a timestamp really does only prove firing) but dangerous as monitoring doctrine, and C2A2's own recent history is a live counterexample: the scheduler watchdog reported green while multi-day outcome-level outages persisted — i.e., the fired-but-failed case was the actual dominant case. The gray-failure and silent-semantic-violation literature shows this class is common, not exotic: processes run, heartbeats update, and semantics silently fail. The most challengeable element is the last clause: downgrading unverifiable checks to "unverified, not failed" is a fail-open design. In safety and monitoring practice, when a critical verification channel is itself unavailable, the conservative reading is "assume broken until verified" (fail-closed), because the same fault that broke the check frequently broke the thing being checked — which is precisely what a multi-day runtime outage does. Meanwhile "missing output is a warning, not proof" is technically true and operationally corrosive: warnings that never escalate are how 102-hour outages accumulate.
  Specific risks: Multi-day outcome outages ride under a green watchdog (already observed); "unverified" accumulates as a silent third state that nobody owns and no alert fires on; warning fatigue normalizes missing outputs; post-hoc timelines built from lastRunAt overstate system health during the outage window.
  Mitigations available: Escalation ladder — one missing output = warning, N consecutive missing outputs = failure, no human override; treat "unverified" as failed for paging purposes when the verification channel has been down beyond a threshold (fail-closed on staleness); add outcome-side probes (semantic checks on the produced artifact: nonzero size, parseable, expected sections) so "succeeded" has a primary signal instead of being inferred; separate dashboards for fired-rate vs. succeeded-rate so divergence is visible.
  STEELMAN:
    Strongest counterargument: The statement is an evidence-grading rubric, not an alerting policy — and as a rubric it is correct: conflating "no output found" with "proven failed" produces false incident reports, especially in a shared output tree where the checker itself is unreliable (see PRESUMPTION-468). Fail-closed monitoring in a noisy, best-effort agent pipeline would generate constant false alarms, and alarm fatigue is as well-documented a failure mode as silent failure. Precise epistemic states (fired / succeeded / unverified) are strictly more information than a binary, and better decisions can be built on top of them.
    What would need to be true for C2A2 to be safe: The three-state rubric feeds an escalation policy that converts persistent "unverified" and repeated "warning" into failures automatically; some independent outcome-level check exists outside the rubric (e.g., a consumer agent that fails loudly when expected inputs are absent); and historical data shows fired-but-failed is rare rather than dominant.
    How to test: Audit the last 30 days of runs — for every run where lastRunAt advanced, independently verify whether the intended artifact was produced and valid. The fired→succeeded conversion rate is the empirical answer: if it is below ~99%, liveness is not an acceptable proxy and the rubric needs the escalation ladder.
  Recommendation: CHALLENGED
