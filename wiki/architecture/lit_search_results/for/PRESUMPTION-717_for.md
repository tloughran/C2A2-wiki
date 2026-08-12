SEARCH-FOR-PRESUMPTION-717:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-717
  Original statement: That a missed day heals itself; the daily 14a/14b series broke for the first time in 118 days and nothing fired on the absence — the gap was found incidentally by a downstream queue count, not by any liveness signal.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-717
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from what did not happen — no alarm, no retry, no gap marker, and a next-day all-clear
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Dead Man's Switch, explained for developers" and "Dead Man's Snitch: Detecting Silent Cron Job Failures" (industry practitioner sources, crontap.com / medium.com, 2025-2026) — [unverified — from search snippet] describe the "dead man's switch" / heartbeat pattern: monitoring must be inverted from "alert on error" to "alert on absence of a success ping," because scheduled jobs that vanish (crash before completion, get skipped, silently no-op) produce no error signal at all. This is a direct, named pattern for exactly the failure mode PRESUMPTION-717 describes.
    2. Lamport, L. (foundational formulation) and subsequent literature, e.g. "Safety and liveness properties" (Wikipedia summary of the formal CS distinction) and "Assurance of Distributed Algorithms and Systems: Runtime Checking of Safety and Liveness" (arXiv:2008.09735) — establishes the formal distinction: safety properties ("nothing bad happens") are violated in finite time and are checkable by watching for a bad event, whereas liveness properties ("something good eventually happens") can only be verified by absence over an unbounded horizon, which is exactly why absence-detection needs a different mechanism than error-detection.
    3. OneUptime, "How to Set Up Heartbeat and Dead Man's Switch Alerts" (2026) and watchflow.io, "Why Cron Jobs Fail Silently" — [unverified — from search snippet] note explicitly that "the absence of data does not trigger any alert" in most observability setups, and that this is the single most common blind spot in scheduled-pipeline monitoring.

  Strength of support: Moderate

  Summary: The literature strongly validates the underlying diagnosis — that presence-based monitoring (alert on error) structurally cannot catch absence-based failures (nothing runs at all), and that this is a well-known, named failure class with an established countermeasure (heartbeat / dead-man's-switch monitoring, liveness-property checking). This supports treating "a missed run requires an active liveness signal, not passive assumption of self-healing" as correct practice, well precedented outside C2A2. The literature is drawn from mature DevOps/SRE tooling and formal distributed-systems theory (safety vs. liveness), both directly analogous to a multi-agent pipeline's daily cadence.
    Note: the literature supports the *diagnosis* (absence needs a dedicated detector) far more than it supports the *presumption itself* (that a missed day "heals itself") — which is, as expected for a presumption, not something literature defends; rather the literature confirms why that presumption is risky and well-documented as risky elsewhere.

  Caveats: Sources are largely practitioner/industry blog material (Dead Man's Snitch, Healthchecks.io, Cronitor-style tooling) rather than peer-reviewed empirical studies of failure rates in silent-absence scenarios; treat "industry consensus" framing with the usual caution about vendor content. The formal liveness/safety distinction (arXiv:2008.09735 et al.) is peer-reviewed and directly on point for why "presence of a next-day all-clear" is not proof that the intervening gap was benign. No source specifically addresses a 118-day-clean-streak-then-silent-gap scenario in a multi-agent LLM pipeline — this is a domain-transfer inference from general cron/distributed-systems monitoring practice.

  Recommendation: PARTIALLY-SUPPORTED
