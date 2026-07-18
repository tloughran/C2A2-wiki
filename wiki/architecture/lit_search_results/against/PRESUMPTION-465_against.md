SEARCH-AGAINST-PRESUMPTION-465:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-465
  Original statement: "Appending a FAIL line to a file constitutes surfacing — fail-loud presumes a reliable listener, never verified."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-465
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. [OWASP, 2025. "A09: Security Logging and Alerting Failures" (OWASP Top 10:2025). — The category was renamed from "Monitoring" to "Alerting" failures to stress the point: logs that no one is guaranteed to read do not constitute detection; a written record without an activated response path is a recognized top-ten failure class.]
    2. [InstaTunnel / industry breach analyses of the 2013 Target breach. "Insufficient Logging and Monitoring: The Blind Spot That Hides Breaches for Months." — Target's tooling generated alerts that were recorded but not acted upon; attackers operated for ~a month until an external party (DOJ) notified Target. Canonical proof that emitting a signal is not surfacing it.]
    3. [The Joint Commission, 2013. "Sentinel Event Alert Issue 50: Medical device alarm safety in hospitals." — 80+ alarm-related deaths in its database; the core mechanism is alarms that fire correctly but are not attended (fatigue, no assigned listener, no escalation). Establishes across domains that an unattended alarm has no safety value.]
    4. [ITOC360. "IT Alerting Solution: Why Most On-Call Teams Are One Silent Alert Away From Disaster." — Describes the exact pattern: alerts landing in a channel "three people are technically members of and zero people are watching"; the fix is acknowledgment-based alerting with automatic escalation when no one acknowledges within a window.]
    5. [LogicMonitor whitepaper. "Best Practices for Alert Management." — Alerting best practice requires delivery to an accountable responder, acknowledgment tracking, and escalation ladders; write-only notification (log/file append) is classified as informational routing, explicitly not appropriate for actionable failures.]

  Strength of challenge: Strong

  Summary: The literature across security operations, IT alerting, and clinical alarm safety converges on a sharp distinction the presumption erases: recording a failure and surfacing a failure are different acts, joined only by a verified listener. OWASP now names "alerting failure" — signals generated but never acted on — as a top-ten weakness; the Target breach is the standard citation for alerts that were written down while the incident ran for a month; and the Joint Commission's alarm-safety work shows that even loud alarms kill when no accountable listener exists. Best practice therefore requires closed-loop alerting: delivery to a specific responder, acknowledgment, and automatic escalation on non-acknowledgment. A FAIL line appended to a file has none of these properties — it is write-only logging whose "loudness" is a property of the writer, not of any receiver.

  Specific risks: C2A2 failures are dutifully recorded and never read; the system believes it fails loud while actually failing silent, so failures compound across scheduled runs — each agent assuming a human or agent saw the FAIL line — until an unrelated symptom finally exposes a long chain of unread failures.

  Mitigations available: Route FAIL lines to a channel with a verified reader (e.g., the daily-walk Chat digest must include a mandatory check of the FAIL file); make a scheduled agent's first action "read the FAIL file and acknowledge each line" with acknowledgment recorded; add an escalation rule (unacknowledged FAIL older than N days triggers a more intrusive surfacing); periodically inject a synthetic FAIL line and measure time-to-acknowledgment.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Every domain that has studied alarms reaches the same conclusion: an alert's value is exactly the probability a listener acts on it, and that probability must be engineered and verified, not presumed. Appending to a file is the weakest possible delivery — no notification, no assigned responder, no acknowledgment, no escalation — and history's most cited breach (Target 2013) happened with far stronger signaling than a file line. Calling this "fail-loud" is a category error: loudness without a listener is silence with a paper trail.
    What would need to be true for C2A2 to be safe: Some process (human or scheduled agent) must read the FAIL file on a cadence shorter than the acceptable failure-response time, must reliably act on entries, and this reading must itself be monitored — i.e., the listener must exist and be verified.
    How to test: Write a synthetic FAIL line and measure how long until any human or agent responds; if the answer is "never" or "unbounded," the presumption is empirically false. Repeat monthly as a fire-drill.
