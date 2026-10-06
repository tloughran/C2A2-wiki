SEARCH-AGAINST-PRESUMPTION-1099:
  Date searched: 2026-10-01
  Original item: PRESUMPTION-1099
  Original statement: Monitoring a system split across execution environments needs a shared run record; per-environment health checks give false negatives.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1099
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Irin (DEV Community), n.d. "A Dead Man's Switch for Your Monitoring Stack". https://dev.to/irinobservability/a-dead-mans-switch-for-your-monitoring-stack-2335 — a central record/monitor can itself fail silently and needs an external heartbeat; makes the shared record a single point of failure. [fetched]
    2. Bhayani, n.d. "Heartbeats in Distributed Systems". https://arpitbhayani.me/blogs/heartbeats-in-distributed-systems/ — heartbeat staleness and false suspicion. [search-snippet, not read]
    3. dvystrcil, homelab-heartbeat repo. https://github.com/dvystrcil/homelab-heartbeat — stamped-record staleness pattern. [search-snippet, not read]

  Strength of challenge: Weak

  Summary: No source says per-environment checks are sufficient or a shared record is harmful. Only indirect challenge: a shared record adds a failure point and a last-seen record is stale when the writer dies, so it needs TTL semantics. The dead-man's-switch literature mostly corroborates a shared record with an external staleness check.

  STEELMAN: A central run record couples every environment to one store/writer path. When it breaks, every environment looks healthy because nothing new is written, or the last record looks "recent". Per-environment checks with independent alerting fail in uncorrelated ways, which is the better property.

  Caveats: Sources concern monitoring stacks and cron, not agent systems; transfer by analogy only.

  Search scope: preliminary search — broader search recommended (web-only, 4 searches / 4 fetches across all four items; no academic sources; independent of 15a — 15a results were not read).

  Recommendation: PARTIALLY-CHALLENGED
