SEARCH-FOR-ASSUMPTION-440:
  Date searched: 2026-07-11
  Original item: ASSUMPTION-440
  Original statement: "'lastRunAt is authoritative for *fired*; output files are secondary for *succeeded*; missing output is a warning, not proof' — and unverifiable checks downgrade to 'unverified, not failed.'"

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-440
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-10 EOD daily run
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. [Nagios Plugins project, "Plugin Return Codes / State Retention" (nagios-plugins.org; Nagios Core documentation, "State Types"). — Industry-standard monitoring defines a four-state model (OK / WARNING / CRITICAL / UNKNOWN) in which UNKNOWN is reserved for checks that could not be executed or evaluated — explicitly distinct from CRITICAL. Direct precedent for "unverifiable downgrades to unverified, not failed."]
    2. [Kubernetes documentation, "Liveness, Readiness, and Startup Probes" (kubernetes.io). — Canonical separation of signal tiers: liveness answers only "did the process fire/respond," readiness answers "is it fit to serve," and each tier has distinct consumers and failure consequences. Direct support for keeping *fired* (lastRunAt) and *succeeded* (outputs) as separate signals with separate semantics.]
    3. [PulsAPI, 2025-2026. "Heartbeat vs Health Check Endpoints" (and OneUptime, 2026, "How to Implement Health Checks That Distinguish Between Liveness and Readiness"). — Practitioner literature stating that a heartbeat's only correct claim is "the process is alive enough to respond — nothing more," and that correctness/outcome must be established by a separate, richer check; conflating the tiers is named as an antipattern in both directions (a heartbeat proving nothing about outcomes, and a missing rich signal not being treated as identical to failure).]
    4. [Google SRE Book, 2016, Ch. 6 "Monitoring Distributed Systems" (sre.google). — Grounds the layered-evidence approach: different signals warrant different alerting severities, and monitoring should distinguish "already ongoing and contributing to real symptoms" (page-worthy) from ambiguous or secondary indicators (ticket/warning-worthy). Supports "missing output is a warning" as a severity-assignment decision.]
  Strength of support: Strong
  Summary: The assumption restates, almost clause for clause, the established layered-signal model of production monitoring. The fired/succeeded split maps onto liveness vs readiness/health semantics; treating lastRunAt as authoritative only for the "fired" claim matches the heartbeat literature's insistence that a heartbeat asserts nothing beyond process responsiveness; and downgrading unverifiable checks to an explicit non-failure state is directly precedented by Nagios's UNKNOWN, a fourth state that has been standard for two decades precisely so that "could not check" is never silently conflated with "failed." Treating missing output as a warning rather than proof matches SRE severity-assignment practice for secondary signals.
  Caveats: Search scope confidence is high; this is well-trodden operational literature. One boundary condition from the same sources: the layered model presumes the outcome tier is actually monitored somewhere — UNKNOWN states and warnings are safe only if they are triaged rather than absorbed as green (see PRESUMPTION-467, where C2A2's recent watchdog-green-during-outage incident shows the failure mode when the outcome tier is missing). Support is for the epistemic taxonomy, not for any particular alert-routing choice built on it.
  Recommendation: SUPPORTED
