SEARCH-FOR-PRESUMPTION-1189:
  Date searched: 2026-10-27
  Original item: PRESUMPTION-1189
  Original statement: "[inferred] The watchdog is presumed able to report the absence of what it watches. Scheduler health runs from the same scheduler it monitors. An apparent 10-19..10-23 outage surfaced only through a weekly report reading last-run timestamps, and the cloud-routine watcher has been silent since 10-06 without raising an alarm. Morning status reads 'everything due overnight fired on time' as health."

  Reading used for the FOR direction: support means literature showing that (a) a monitor sharing fate with the monitored scheduler cannot report that scheduler's absence; and (b) absence-of-signal (dead man's switch / heartbeat) alerting from an external watcher is standard practice. 15a does not verify the 10-19..10-23 outage or the 10-06 silence.

  Search scope: PRELIMINARY. 2 web searches (standard), 1 fetch (Google SRE book ch. 6, read in full). Searched: dead man's switch / cron heartbeat / external monitoring; SRE black-box vs white-box monitoring. Not reached: SRE book ch. 10 "Practical Alerting" and the SRE Workbook (possible meta-monitoring material), Healthchecks.io docs, academic watchdog / failure-detector literature.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1189
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from scheduler health running inside the scheduler it monitors, an outage found only by a weekly timestamp read, a watcher silent since 10-06, and morning status equating "fired on time" with health.
      15a: Searched for supporting literature (preliminary; 2 searches, 1 fetch read in full)
    Current status: SEARCHED-15a — SUPPORTED

  Supporting evidence found: Yes for (b), which is well documented in practice. (a) is supported by implication in the same sources. The canonical SRE text read does not state the shared-fate point explicitly.

  Sources:
    1. Cron heartbeat / dead man's switch guidance: OnlineOrNot, "Cron job monitoring: how to know when your scheduled tasks fail"; dev.to (dcwiklik), "Your cron job did not fail. It never ran"; Cronping, "Silent cron job failures"; Crontap blog, "Dead man switch explained for developers" and "Healthchecks: dead-man pair with scheduler". [snippet only, practitioner/vendor]. A job pings an external endpoint, and a separate service alerts when the ping does not arrive, i.e. it alerts on missing activity rather than reported errors. Error logging misses jobs that never start (e.g. cron not restarted after reboot). A missing ping also exposes a silently disabled scheduler. One author warns that an untested alert path is "only an assumption". One vendor recommends pairing an execution-failure monitor with an independent absence monitor. Relevance: direct support for (b) and indirect support for (a). The pattern is external specifically because a scheduler that is down cannot report itself. "It never ran" matches the item's "silent watcher" and "fired on time = health" concerns closely.
    2. Ewaschuk, R. (ed. Beyer, B.) 2016/2017. "Monitoring Distributed Systems," ch. 6 of Site Reliability Engineering (Google/O'Reilly), sre.google/sre-book/monitoring-distributed-systems/. [read in full]. Defines black-box monitoring as "testing externally visible behavior as a user would see it" and says it is symptom-oriented: "the system isn't working correctly, right now". Notes that only end-to-end tests detect some failures (e.g. wrong content behind a 200). Relevance: theoretical grounding for checking from outside. Honest limit: the chapter does NOT discuss watchdog shared fate, meta-monitoring, or absence-of-signal alerting. The claim's citation of "Google SRE black-box monitoring" is supported for the concept, not for the shared-fate point.

  Strength of support: Moderate

  Summary: Absence-of-signal monitoring by an external watcher is established practice for scheduled jobs. The rationale given is that jobs which never run produce no errors to log, and that a disabled scheduler is only visible from outside. This supports the item: a health check run by the scheduler it monitors cannot report that scheduler's absence, and "everything due fired on time" counts only what ran. The Google SRE chapter grounds the outside-in (black-box) principle but does not address shared fate directly. The item's concern is a recognised blind spot in practice, with weaker anchoring in canonical texts.

  Caveats:
    - Direct support is mostly vendor blogs with a commercial interest in selling cron monitors.
    - The SRE ch. 6 text (read in full) does not contain the shared-fate / meta-monitoring argument. It may be in ch. 10 or the Workbook, which were not checked.
    - No academic watchdog / failure-detector literature was reached.
    - An external monitor has failure modes of its own ("who watches the watchmen"). Sources suggest paired monitors but give no formal treatment.

  Recommendation: SUPPORTED

  (No NOVELTY-FLAG.)
