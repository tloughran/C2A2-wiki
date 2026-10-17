SEARCH-FOR-PRESUMPTION-1102 (RE-TRIGGER — 15d, MONITOR-637, cycle 1; Low):
  Date searched: 2026-10-17
  Original item: PRESUMPTION-1102
  Original statement: [inferred] Polling schedules sized for active work should back off when the work
    completes (adaptive scheduling).
  Owed (per 15d block): a source on idle-run cost / adaptive polling in agent or job scheduling.
  Cycle: 1 (RE-TRIGGER by 15d; processed 2026-10-17)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-1102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 2026-09-30 sessions.
      15a (cycle 0, 2026-10-01): PARTIALLY-SUPPORTED (Weak-Moderate). Brooker 2015 backoff/jitter [fetched];
        AWS REL05-BP03 [snippet]; SRE ch. 6 [fetched]; InfoQ/Cloudflare [snippet]. Retry backoff only; no
        source on idle polling after work completes.
      15b (cycle 0): independent; not read by this agent.
      15c: -> MONITOR-637 (Low)
      15d: re-triggered without evaluating evidence; owed = idle-run cost / adaptive polling source.
      15a (cycle 1, 2026-10-17): 2 web searches; 2 fetches (ICWSM abstract read in full; Bernstein ADR-005
        read in full).
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: (a) adaptive polling in feed aggregation, mobile sync, message consumers; (b) idle-run token
    cost in LLM-agent scheduling (project docs, ADRs).

  Supporting evidence found: Partial — both owed limbs now have a source, neither of them strong.

  Sources:
    1. Urbansky, D., Reichert, S., Muthmann, K., Schuster, D. & Schill, A., 2011. "An Optimized Web Feed
       Aggregation Approach for Generic Feed Types." Proc. ICWSM 5(1):638-641 (poster).
       doi:10.1609/icwsm.v5i1.14161. [abstract — read in full; full text not read, so reduction percentages
       not seen]
       - Problem stated: with fixed polling, "many times a client asks for updates, there is no new item".
       - Adaptive algorithms learn each feed's update behaviour and set the interval accordingly.
       - Tested on >180,000 real feeds over three weeks: adaptive polling "reduces traffic significantly and
         provides near-real-time updates".
       Relevance: peer-reviewed (poster) evidence that activity-adaptive polling cuts empty polls without
       losing timeliness. Analogous domain: feeds, not jobs.
    2. Bernstein project, 2026. "ADR-005: Short-Lived Agent Lifecycle" (docs.bernstein.run; supersedes
       ADR-001). [read in full — project ADR; self-reported pilot data, not peer-reviewed]
       Pilot: 12 LLM coding agents over a multi-day sprint, polling a task queue.
       - When the queue was empty, agents went idle or emitted status messages.
       - Worst agent: 283 bulletin messages, mostly idle status reports, zero commits, about 50,000 tokens
         spent on signalling.
       - "Only 3 of 12 agents were reliable producers. The rest were net consumers of tokens."
       - Idle state was "indistinguishable from the agent being stuck, confused, or dead".
       Fix: no idle state. Agents exit when their batch is done, and a deterministic orchestrator spawns new
       agents only when work exists.
       Relevance: direct, measured (if informal) evidence of idle-run cost in LLM-agent scheduling. Their
       remedy is a stronger form of back-off: stop polling entirely when work completes.
    3. Microsoft Exchange ActiveSync Direct Push documentation (learn.microsoft.com / TechNet, "Heartbeat
       Interval Adjustment"). [snippet] The heartbeat interval adapts: it lengthens after successful round
       trips and shortens on timeout, to minimise bytes over the air and battery use. Vendor design; no
       published figures.
    4. Agent-ops practitioner material. [snippet — practitioner, self-reported]
       - Looper (github.com/lapsrj/looper): gate the LLM behind a cheap check. "A model polling for its own
         work pays for each empty check in tokens and context."
       - #B4mad / brenner-axiom write-up: replacing one LLM cron job with system cron eliminated ~288
         unnecessary agent sessions per day (single case).
       - OpenClaw HEARTBEAT_OK no-op convention.
    5. Liu, H., Ramasubramanian, V. & Sirer, E.G., 2005. IMC '05 RSS measurement study (99,714 feeds polled
       hourly). [title / snippet only] Baseline measurement of fixed-interval polling waste.

  Strength of support: Moderate. Up from Weak-Moderate: there is now a peer-reviewed adaptive-polling
    result (feeds) and a measured idle-cost case in LLM-agent scheduling (project ADR).

  Summary: Adaptive polling that tracks observed activity reduces empty polls substantially without
    sacrificing freshness (Urbansky et al. 2011, 180k feeds). In LLM-agent orchestration, idle polling after
    the work runs out has measurable token cost and makes idle agents hard to tell from dead ones (Bernstein
    ADR-005: 9 of 12 agents were net token consumers). Several agent-ops sources converge on the same advice:
    gate the expensive run behind a cheap work-exists check or an event trigger. This supports the
    presumption, and suggests the strongest form of "back off" is to stop or gate, not merely lengthen the
    interval.

  Owed condition: MET at practitioner-plus level. Idle-run cost in agent scheduling: found (source 2, self-
    reported). Adaptive polling: found (source 1, peer-reviewed poster, abstract only). No controlled study
    of adaptive schedules for LLM-agent jobs.

  Caveats:
    - Source 2 is one project's informal pilot. Its numbers are self-reported, and its idle behaviour
      (persistent sessions) differs from C2A2's discrete scheduled runs, where an idle run is a full no-op
      session.
    - Source 1 reduction magnitudes were not seen; the feed domain has no "work completes" event, only
      variable update rates.
    - Back-off trades cost for detection latency if work resumes. The presumption's support depends on a
      reliable wake trigger (cf. ActiveSync shortening on timeout; Paperclip/Looper event triggers).

  Recommendation: PARTIALLY-SUPPORTED (Moderate).
