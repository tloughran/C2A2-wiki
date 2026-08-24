SEARCH-FOR-PRESUMPTION-855:
  Date searched: 2026-08-24
  Original item: PRESUMPTION-855
  Original statement: That a registry's last-run field records whether a task ran, so that the absence
    of an entry is read as evidence the task did not fire. The field is written on completion; the
    inference treats it as if it were written on attempt.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that
  completion-logging cannot license the inference from "no record" to "did not fire", that the gap
  between "did not start" and "started and died" is a recognised and named failure mode, and that the
  discipline's answer to it is an explicit start-side signal (heartbeat-on-start, lease acquisition,
  intent record) rather than better reading of the completion record.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-855
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by noticing that a conclusion about non-firing was drawn from a field whose write
        point is the end of the task rather than the beginning, with no clause acknowledging that the
        two produce the same observation.
      15a: Searched for supporting literature (2026-08-24)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Chandra, T. D. & Toueg, S. (1996). "Unreliable Failure Detectors for Reliable Distributed
       Systems." *Journal of the ACM* 43(2), 225–267. — The formal root of the item. In an asynchronous
       system it is impossible to distinguish with certainty a crashed process from a very slow one;
       silence is not a decidable observation. Chandra and Toueg's contribution is precisely the
       admission that a failure detector's output can be wrong, and the characterisation of how wrong it
       may be while remaining useful. Any monitor that reads absence as a determinate fact about the
       world is asserting something the theory says it cannot know.
    2. Fischer, M. J., Lynch, N. A. & Paterson, M. S. (1985). "Impossibility of Distributed Consensus
       with One Faulty Process." *Journal of the ACM* 32(2), 374–382. [established-work; cited here as
       the impossibility result the Chandra–Toueg failure-detector hierarchy was constructed to
       circumvent, per the Chandra–Toueg literature retrieved above.] — Theoretical grounding for why the
       problem is structural rather than a matter of instrumentation quality.
    3. Burrows, M. (2006). "The Chubby Lock Service for Loosely-Coupled Distributed Systems." *OSDI '06*,
       USENIX. — The canonical production answer. Chubby's design vests liveness in *lease acquisition*:
       a client holds a lock only while it keeps a lease alive, and the master itself holds office only
       for the duration of a master lease of several seconds. The state that matters is asserted at the
       start and continuously renewed, not written at the end. This is the pattern 14b's item says the
       registry lacks.
    4. Healthchecks.io documentation, "Measuring Script Run Time" and "Configuring Checks"
       (healthchecks.io/docs). [operational documentation of a widely used monitoring service] — The
       single most on-point source. The service exposes a `/start` endpoint distinct from the success
       ping *for exactly this reason*: "if a job sends a 'start' signal but does not send a 'success'
       signal within its configured grace time, Healthchecks.io will assume the job has failed and
       notify you." Without the start signal the two states are indistinguishable; with it they are
       separated. The design decision C2A2 did not make is here made explicitly and documented as the
       reason the feature exists.
    5. Practitioner literature on cron monitoring and the dead man's switch: watchflow, "Why Cron Jobs
       Fail Silently: Heartbeat Monitoring for Scheduled Tasks"; OnlineOrNot, "Cron job monitoring: How
       to know when your scheduled tasks fail"; UpDog, "What is a Dead Man's Switch? Heartbeat Monitoring
       Explained"; crontap, "Dead man's switch, explained for developers." [grey / vendor-practitioner]
       — Converge on the same statement of the hazard: "a cron job that doesn't run produces no errors —
       it just doesn't happen," and the alert must trigger "on absence of activity, not presence." They
       also converge on a caution 14b's item does not raise but which bears on it: the monitor must not
       share fate with the monitored thing.
    6. Prometheus / kube-prometheus `Watchdog` alert (runbooks.prometheus-operator.dev/runbooks/general/
       watchdog/) and the PagerDuty "Dead Man's Snitch" integration. [reference implementation] — The
       always-firing alert, defined as `vector(1)`, exists so that an external observer can detect the
       silence of the alerting pipeline itself. Institutionalises the principle that a channel which is
       only used to report events cannot report its own absence.
    7. Write-ahead logging / ARIES. Mohan, C. et al. (1992), "ARIES: A Transaction Recovery Method…,"
       *ACM TODS* 17(1). [established-work; the WAL principle as described in the recovery literature
       retrieved] — The general form: record the intent to stable storage *before* performing the
       action, so that a crash between intent and completion is recoverable and, crucially, *visible*.
       A registry that writes only on completion is the WAL discipline inverted.

  Strength of support: Strong

  Summary: The presumption is supported from three independent directions, and the support is unusually
  clean because the failure mode has a formal statement, a named production pattern, and a documented
  commercial product feature. Chandra and Toueg establish that "no signal" is not a decidable observation
  in an asynchronous system: a crashed process and a slow one are indistinguishable, which is why the
  entire failure-detector literature is built on oracles that are permitted to be wrong. The operational
  literature converts this into the specific instance 14b names — a scheduled task that does not run
  produces no error, only absence — and the recognised remedy in every source consulted is a signal
  emitted at the *start*: Chubby's lease, Healthchecks' `/start` endpoint, the dead-man's-switch
  heartbeat, the Watchdog alert. Healthchecks.io's documentation is close to a direct confirmation: the
  start signal exists because without it the system cannot tell a job that never began from a job that
  began and died, which is verbatim the distinction 14b says the registry's last-run field cannot make.
  The database-recovery tradition supplies the same rule in its most general form — log the intent before
  the act — and a completion-only registry is that rule run backwards.

  Caveats: The support is for the *general* claim (completion-logging cannot ground an inference to
  non-firing); it does not establish that C2A2's registry in fact suffers this, which is a fact about
  this estate and not a matter the literature can settle. Two scope limits are worth recording. First,
  none of the sources treats heartbeat-on-start as *mandatory* in a normative sense; they treat it as the
  standard answer to a problem the designer has to have noticed. Healthchecks.io offers `/start` as an
  opt-in feature, not a default, which is itself evidence that the presumption is easy to hold. Second,
  the distributed-systems sources concern processes that can crash mid-execution on hardware that can
  fail; an agent run in a scheduled pipeline has a different crash surface, and whether the analogy
  transfers intact is not something the literature addresses. Sources 5 and 6 are vendor and
  practitioner documentation rather than peer-reviewed study — appropriate as evidence of established
  design practice, not as empirical evidence of effectiveness; I found no quantitative comparison of
  start-signal monitoring against completion-only monitoring. FLP (source 2) and ARIES (source 7) are
  cited from established knowledge as theoretical grounding; no page-level claims are asserted.
  Search scope: moderate-to-good — covered failure-detector theory, lease/lock services, cron and
  heartbeat monitoring practice, and write-ahead logging. Did NOT cover the observability literature on
  "unknown unknowns" and black-box vs. white-box monitoring (Beyer et al., *Site Reliability
  Engineering*, ch. 6), which would likely add a fourth supporting line and remains unsearched.

  Recommendation: SUPPORTED
