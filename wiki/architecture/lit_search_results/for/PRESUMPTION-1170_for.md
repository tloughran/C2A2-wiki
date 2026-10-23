SEARCH-FOR-PRESUMPTION-1170:
  Date searched: 2026-10-23
  Original item: PRESUMPTION-1170
  Original statement: "[inferred] The schedule presumes its host is awake, and every watcher that would notice otherwise (scheduler health, system health, project status, keep-warm) runs on that same host. A five-day host outage (10-18..10-22) was therefore detectable only retrospectively, by the first jobs to fire after wake; nothing off-host raised an alarm while it was happening, including the Supabase free-tier keep-warm." Risk: High.

  Reading used for the FOR direction: support means literature or documented practice confirming that (a) a monitor co-located with the host it watches cannot detect, in real time, a failure of that whole host, and (b) the standard remedy is a minimal check that runs outside the failure domain (heartbeat / dead man's switch / external black-box probe). The 15a search does not judge whether C2A2 should adopt that remedy.

  Search scope: PRELIMINARY. 5 web searches, 3 fetches (budget cap). Searched: dead man's switch / heartbeat monitoring and same-host blindness; Google SRE book ch. 6 (black-box vs white-box); Prometheus "Watchdog" always-firing alert and external receivers; Supabase free-tier pausing policy. Tradition wikis grepped first (wiki/traditions/, terms "dead man", "heartbeat monitor"): no hits. No peer-reviewed distributed-systems paper (e.g. on failure detectors, Chandra and Toueg 1996) was searched or read in this pass. A broader search is recommended.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1170
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-23 transcripts (final assistant message per session, read directly via session_info).
      15a: Searched for supporting literature (preliminary, budget-capped: 5 searches, 3 fetches)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Ewaschuk, R. (ed. Beyer, B.), 2016/2017. "Monitoring Distributed Systems." Ch. 6 in Beyer, Jones, Petoff and Murphy (eds.), Site Reliability Engineering. O'Reilly / sre.google. [fetched/read in full] Defines black-box monitoring as "testing externally visible behavior as a user would see it," symptom-oriented and representing "active—not predicted—problems." Google combines "heavy use of white-box monitoring with modest but critical uses of black-box monitoring." It also says to keep paging elements "very simple and robust" and monitoring as "distinct systems with clear, simple, loosely coupled points of integration." Relevance: this is indirect theoretical grounding. The chapter does NOT explicitly address a monitor that dies with its host, and does not use the terms "dead man's switch" or "failure domain." The C2A2 watchers (scheduler health, system health, keep-warm) are all white-box and on-host. The chapter's model is that the critical black-box component catches whole-system symptoms.
    2. PromLabs (Volz, J., UNVERIFIED author attribution), n.d. "End-to-End Watchdog Alerts." Monitoring and Debugging Prometheus training. [fetched/read in full] Recommends, "as a last resort," an always-firing alert (e.g. PromQL `vector(1)`) routed "to an external service" that "expect[s] an incoming alert notification every x minutes (plus some slack time)" and alerts otherwise. It names the pattern ("dead man's switch, sentinel alert, beacon alert, or heartbeat alert"). The listed failure cases include the monitoring setup breaking and the organization's whole network being disconnected. This is direct practitioner support for both (a) and (b). It quotes the kube-prometheus project's default "Watchdog" rule, which ships as standard.
    3. prometheus-operator runbook "Watchdog" and GitLab runbook "Prometheus Dead Man's Snitch". [snippet only] Same pattern deployed as default practice: an always-firing heartbeat as an end-to-end pipeline test, with the external receiver (Dead Man's Snitch / PagerDuty) raising the alarm when it goes silent. This is empirical precedent that the pattern is standard in production.
    4. Practitioner write-ups: dev.to "A dead man's switch for your monitoring stack"; omarmerroun "Can't Monitor Yourself"; crontap "Dead man switch explained for developers"; healthchecks.io-style cron heartbeat examples. [snippet only] Explicit statements that "the system responsible for detecting that your monitoring is down must not depend on the monitoring stack itself." One example appends a curl ping to an existing cron line so that if "the whole VM goes offline, the heartbeat stops arriving" and the external service notices. These are grey literature (blogs), not peer-reviewed, but they are the closest match to C2A2's single-host, cron-style case. They also give the minimal off-host check the item asks about: one outbound ping per scheduled run to an external heartbeat service with a grace window.
    5. Supabase, 2026. "Project Pausing." Supabase Docs (page modified 2026-10-23). [fetched/read in full] Free-plan projects are paused after "low activity over a 7-day period." Supabase sends "a warning email roughly one week before the pause takes effect" and a confirmation once paused. Relevance: this confirms that the keep-warm job's purpose depends on the host running it. It also shows the only off-host signal is Supabase's own warning email. That email tracks inactivity, not the outage, and its timing (about one week before the pause) means a 5-day outage would not necessarily trigger it. This supports the claim that "nothing off-host raised an alarm" for an outage shorter than the pause window. (Inference by 15a, not a claim of the source.)

  Strength of support: Strong (for the general principle) / Moderate (for direct peer-reviewed grounding)

  Summary: Documented SRE and Prometheus practice agrees that a monitor sharing a failure domain with what it watches cannot report that domain's death. The standard remedy is an inverted, always-firing heartbeat received by an independent external service that alarms on silence. The PromLabs watchdog guidance, read in full, and the default kube-prometheus "Watchdog" rule state both the failure mode and the remedy explicitly. Practitioner write-ups apply the same reasoning to a single VM or host running cron jobs, which matches C2A2's configuration. The Google SRE book chapter gives theoretical grounding: black-box, externally visible checks catch active whole-system symptoms that white-box internals miss. It does not explicitly discuss co-located-monitor blindness.

  Caveats:
    - Most direct support is grey literature (training material, runbooks, blogs), not peer-reviewed research. The SRE book is authoritative but only indirectly on point.
    - The literature mostly concerns production services with paging. C2A2 is a single-user research pipeline on a personal machine (likely a laptop that sleeps), where a sleeping host may be intended behaviour rather than an outage. The literature's urgency assumptions ("page a human") may not transfer. Whether a five-day gap matters is a design question, not a literature one.
    - An external heartbeat detects silence, not cause. It cannot tell "host asleep by design" from "host failed." The SRE chapter's warnings against noisy, non-actionable alerts apply.
    - The Supabase point is 15a's inference from the docs. The docs give no exact inactivity threshold, and Supabase notes that "a few user requests" per day typically suffice.
    - Formal distributed-systems theory on failure detectors and heartbeats was not searched in this pass.

  Recommendation: SUPPORTED
