SEARCH-AGAINST-PRESUMPTION-463:
  Date searched: 2026-07-10
  Original item: PRESUMPTION-463
  Original statement: "Platform pause policy is stable and a synthetic query is a trustworthy activity proxy — the keep-warm loop needs no outcome verification."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-463
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference from 2026-07-09 EOD cohort
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. [CloudQA, 2026. "Synthetic Monitoring vs Real User Monitoring: Why 2026 Demands Both." — Synthetic checks passing does not guarantee the real outcome; the field's consensus is that synthetic signals must be closed-loop-verified against real outcomes because scripts diverge from reality silently.]
    2. [Checkly Docs. "Synthetic Monitoring — Concepts, Benefits & Challenges." — Documents the canonical failure: synthetics pass while the real condition fails, because the synthetic probe is not representative; a keep-warm ping that "succeeds" locally may not register as activity on the platform side.]
    3. [travisvn, GitHub. "supabase-pause-prevention." — The keep-alive ecosystem itself warns the workaround fails silently if the cron host goes down or the ping doesn't traverse a counted path; i.e., the loop's success signal (cron ran) is not the outcome (project stayed unpaused).]
    4. [SimpleBackups blog. "Supabase Free Tier Paused and Lost Data: What Happened." — Real-world reports of projects pausing despite presumed activity, plus explicit warnings that the pause threshold "can change as Supabase updates its policies" — free-tier policies are changed by vendors without individual notice.]
    5. [Supabase GitHub Discussions #38442. "Clarification on what 'inactivity' means." — The definition of counted activity is ambiguous enough that users must ask the vendor; a proxy whose counted-ness is undocumented cannot be trusted open-loop.]

  Strength of challenge: Strong

  Summary: This presumption combines three independently challenged beliefs. (1) Policy stability: PaaS free-tier terms are routinely revised — Supabase's own ecosystem documents that the pause threshold has changed and may change again, and vendors are under no obligation to notify free-tier users individually. (2) Proxy trustworthiness: what counts as "activity" is ambiguous (REST vs direct SQL vs dashboard), community clarification threads exist because the vendor's definition is underspecified, and keep-alive tools carry explicit warnings that pings can fail to count. (3) No outcome verification: the synthetic-monitoring literature is unequivocal that open-loop synthetic signals diverge from real outcomes silently; monitoring the intent (cron fired) instead of the outcome (project unpaused) is the textbook open-loop control failure. Each leg is individually shaky; the conjunction is worse.

  Specific risks: The keep-warm loop reports green (cron executed, query returned) while the project pauses anyway — because the policy changed, the ping stopped counting, or the ping host died — and C2A2 discovers the pause only when a dependent feature fails, possibly days later, with a manual restore required.

  Mitigations available: Close the loop: verify the outcome, not the action — periodically probe project reachability/status (management API or a REST read) from a second vantage point and alert on failure; watch for Supabase's pre-pause warning email and route it somewhere monitored; diversify the keep-alive path (GitHub Actions plus in-platform edge-function heartbeat); schedule a periodic policy re-check as a recurring task.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: An unverified keep-alive is open-loop control over a system whose transfer function (the pause policy) is undocumented, discretionary, and known to change. The monitoring literature's core lesson is that synthetic action-success is not outcome-success — the two diverge silently, and the divergence is only discovered at failure time. Betting continuity of the system's only database on "the vendor won't change a free-tier policy and my ping counts" is a hope, not a control.
    What would need to be true for C2A2 to be safe: The pause policy remains as documented; the daily query traverses a counted path; the ping infrastructure never silently fails; and any policy change is noticed before its effect lands. All four must hold simultaneously, indefinitely.
    How to test: Add an outcome probe (does a REST read against the project succeed today? is project status "active"?) and compare its history against keep-alive execution history; any divergence proves the proxy untrustworthy. Optionally test whether a scratch project pauses despite the same ping regimen.
