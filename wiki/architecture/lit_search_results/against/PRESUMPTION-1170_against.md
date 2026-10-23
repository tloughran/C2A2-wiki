# PRESUMPTION-1170 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH — broader search recommended. 5 web searches, 2 successful fetches (1 additional fetch of sre.google ch. 6 was refused by the fetch tool as a session duplicate; the O'Reilly-hosted excerpt of the same chapter was read instead).

Reading of "challenge" used: I treated "challenge" as evidence that the presumption's *risk* is overstated, mis-specified, or bounded, not as evidence that the factual description is false. The factual core (every watcher co-located on one host, so a whole-host outage is invisible while it happens) is close to definitional and I found nothing contradicting it. The search therefore targeted (a) whether the outage was a failure at all versus an expected host state, (b) whether the "High" risk rating holds for this setup, (c) the costs and failure modes of the off-host remedy, and (d) boundary conditions on the Supabase keep-warm part of the claim.

```
SEARCH-AGAINST-PRESUMPTION-1170:
  Date searched: 2026-10-23
  Original item: PRESUMPTION-1170
  Original statement: "[inferred] The schedule presumes its host is awake, and every watcher
    that would notice otherwise (scheduler health, system health, project status, keep-warm)
    runs on that same host. A five-day host outage (10-18..10-22) was therefore detectable only
    retrospectively, by the first jobs to fire after wake; nothing off-host raised an alarm
    while it was happening, including the Supabase free-tier keep-warm."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1170
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-23 transcripts (final assistant message per session, read
           directly via session_info).
      15b: Searched for challenging literature (preliminary; 5 searches, 2 fetches)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Ewaschuk, R., 2016. "Monitoring Distributed Systems." In Beyer, Jones, Petoff & Murphy
       (eds.), Site Reliability Engineering, ch. 6 (O'Reilly excerpt). [fetched/read in full —
       excerpt covering Definitions through Black-Box vs White-Box; the later sections of the
       chapter were NOT read]
       — Challenges the risk rating, not the mechanism. The chapter says paging a human is
       "a quite expensive use of an employee's time", that alerts should fire only on a clear
       failure that needs a human, and that noisy alerting leads people to "second-guess, skim,
       or even ignore incoming alerts". It also says that observations with long horizons and
       low sampling rates "can also often tolerate more fragility because occasional missed
       samples won't hide a long-running trend". C2A2's daily batch pipeline is that kind of
       low-rate, long-horizon workload. Its context is a Google team of 10–12 people with a
       dedicated "monitoring person", which does not transfer directly to a single-user system.
       Note: the chapter does not say anything about whether monitors should be off-host; the
       black-box/white-box distinction is about symptom versus internals.
    2. Supabase, n.d. (current). "Project Pausing" (docs/guides/platform/free-project-pausing).
       [fetched/read in full]
       — Bounds the keep-warm part of the claim. Pausing is triggered by "low activity over a
       7-day period". Supabase emails a warning "roughly one week before the pause takes
       effect", and paused projects can be restored for up to 1 year "including data and
       configurations". So (a) a 5-day outage is under the 7-day threshold and should not by
       itself pause the project, (b) an off-host alarm already exists in the form of Supabase's
       warning email, which comes from outside the failure domain, and (c) the worst case is
       recoverable. The statement's "nothing off-host raised an alarm ... including the Supabase
       free-tier keep-warm" is accurate for the outage window, but it overstates the exposure:
       the vendor supplies an off-host check of its own, and it would fire before any data loss.
    3. Apple Developer Documentation, "Scheduling Timed Jobs" (launchd), as reported in
       search results. [snippet only]
       — Boundary condition / possible mis-specification. Apple's documentation reportedly says
       that a StartCalendarInterval job due while the machine is asleep runs on wake, but a job
       due while the machine is powered off is skipped until the next scheduled time. If the
       host was asleep (not off or crashed), "detectable only retrospectively, by the first jobs
       to fire after wake" is the platform's designed catch-up behaviour, not a silent failure.
       On a personal laptop host, being asleep is an expected state rather than an outage.
       Whether 10-18..10-22 was sleep, power-off, or crash is not established in the item.
       Whether missed calendar runs are coalesced into one run on wake is UNVERIFIED.
    4. Healthchecks.io status page, incident of Feb 2020 ("alerts weren't being sent";
       invalid cron expression crashed the notification jobs, ~7 h). [snippet only]
       — The off-host remedy has failure modes of its own. A hosted dead-man's-switch can fail
       silently, so moving the monitor off-host shifts the "who watches the watcher" problem
       rather than ending it. It also adds a third-party dependency, an account, and secrets.
    5. Practitioner sources on dead-man's-switch / heartbeat monitoring (DEV Community "A dead
       man's switch for your monitoring stack"; setten-io/ecg; adamdecaf/deadcheck;
       omarmerroun "Can't Monitor Yourself"). [snippet only]
       — Mostly SUPPORTIVE of the presumption, so recorded here only for completeness and for
       the caveats relevant to the AGAINST direction. They describe grace periods and retries
       as needed to avoid false alerts, and they describe heartbeats as "complementary ... an
       additional failsafe", not a replacement. They also note that a heartbeat proves only that
       the host and scheduler are alive, not that the pipeline output is correct. On a laptop
       host, a heartbeat with no sleep-awareness would fire on every ordinary sleep, overnight
       or while travelling. That is the "something seems a bit weird" alert Source 1 advises
       against.
    6. Practitioner sources on alert fatigue in small teams (Intercom "8 questions"; DEV
       Community "Scaling on-call when you only have 5 engineers"; Atlassian/Opsgenie).
       [snippet only]
       — Small teams are advised to page only for "user-facing impact right now" and to send
       everything else to tickets or summaries. C2A2 has no external users and no SLO, so a
       multi-day gap may not meet a page-worthy bar.

  Strength of challenge: Weak-to-Moderate (Weak against the mechanism; Moderate against the
    "High" risk rating and against the implied remedy)

  Summary: Nothing found contradicts the structural claim: a monitor that shares the host's
    failure domain cannot report that host's total outage while it is happening. The challenges
    are to severity and specification. Google SRE guidance treats every alert as costly and
    reserves pages for clear failures that need a human. It says low-rate, long-horizon workloads
    tolerate missed samples, and a daily personal research pipeline with no external users fits
    that description. The keep-warm part is overstated: Supabase's pause threshold (7 days) is
    longer than the 5-day outage, Supabase itself sends an off-host warning email about a week
    before pausing, and a paused project can be restored with its data for a year. If the host
    was asleep rather than crashed, catch-up on wake is launchd's documented behaviour, and
    "outage" may be the wrong frame. Off-host heartbeat services have their own silent-failure
    history and would produce false positives on every normal laptop sleep unless tuned.

  Specific risks: If the presumption is over-weighted, C2A2 may take on an external
    monitoring dependency (account, secret, a new failure mode) and an alert stream that fires on
    routine sleep. That trains the operator to ignore it, which is the alert-fatigue failure mode.
    If it is under-weighted, the real residual exposures are: (a) an outage of 7+ days that pauses
    Supabase, recoverable but disruptive; (b) a host that is ON but wedged (scheduler dead,
    machine awake), where launchd catch-up does not happen and co-located watchers may also be
    dead — the AGAINST arguments here are weakest for this case; (c) power-off, where missed
    jobs are skipped, not caught up.

  Mitigations available: (i) Classify host states (sleep / off / wedged) before deciding a
    remedy; only "wedged" and "off for more than N days" clearly need an off-host check. (ii) Use
    the existing off-host signal: make sure Supabase's pause-warning email reaches an inbox
    that is read. (iii) If a heartbeat is added, set its grace window longer than ordinary
    sleep/travel (e.g. 48–72 h), deliver it as a digest or ticket rather than a page, and accept
    that it is a complementary failsafe. (iv) Retrospective detection on wake (the current
    behaviour) may be an acceptable design point if it is written down as one rather than
    left implicit.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1170
  Strongest counterargument: Seen as a risk, the presumption imports an operations frame built
    for always-on services with users and SLOs into a single-operator research pipeline on a
    laptop, where "host asleep" is the normal, expected state for much of each day. In that
    setting, catching up and detecting the gap retrospectively on wake is the platform's
    designed behaviour (launchd), not a blind spot. The one external dependency at stake
    (Supabase free tier) has a 7-day threshold, its own off-host warning email, and a 1-year
    restore window, so the five-day gap was below every consequential threshold. Adding an
    off-host dead-man's switch would buy little here. It adds a dependency that has failed
    silently itself, plus an alert that fires on every ordinary sleep unless its grace window is
    so long that it detects little more than retrospective wake already does. SRE doctrine says
    not to page for things that are merely odd and to keep paging rules simple; for this system,
    that argues for documenting the gap rather than closing it.
  What would need to be true for C2A2 to be safe: (1) the 10-18..10-22 gap was sleep or
    deliberate power-off, not a wedged-awake host; (2) no pipeline output is time-critical within
    a window shorter than the realistic host-off period; (3) Supabase pause-warning emails reach
    a monitored inbox; (4) on-wake jobs reliably detect and report the gap (the retrospective
    detector itself works); (5) no host-off period approaches 7 days without the operator
    already knowing.
  How to test: (a) Check pmset/system logs (`pmset -g log`) for 10-18..10-22 to classify the
    gap as sleep vs. shutdown vs. hang. (b) Confirm launchd behaviour on this macOS version with a
    near-future StartCalendarInterval job across a sleep and across a shutdown. (c) Confirm the
    Supabase project owner email and whether a pause-warning was or would be received.
    (d) Count host-asleep periods over 24 h in the last 90 days to size the false-positive
    rate a naive heartbeat would have produced.
```

Source-reading status: Source 1 [fetched/read in full — excerpt only, chapter sections after "Black-Box Versus White-Box" not read]; Source 2 [fetched/read in full]; Sources 3–6 [snippet only]. Beyer et al. 2016 chapter text at sre.google was not fetched in this session (tool refused as duplicate); claims attributed to it come only from the O'Reilly excerpt of the same chapter.
