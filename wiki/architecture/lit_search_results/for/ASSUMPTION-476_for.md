SEARCH-FOR-ASSUMPTION-476:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-476
  Original statement: A staleness detector keyed to cycle count loses sensitivity exactly as consumption stalls — "the longer consumption stalls, the less able the staleness detector is to report it." A wall-clock companion rule is the stated remedy, deliberately not implemented.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-476
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 periodic monitor weekly transcript
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Fail-safe design literature: "Fail-safe" (Wikipedia); Inspiro, "How to Design Fail-Safe Systems for Critical Embedded Applications"; Nenvitech, "Is your sensor fail-safe?" — Direct theoretical grounding for the general form of the claim. A fail-safe system "is designed to avoid situations where a fault preventing the system from performing its safety function goes undetected," and the named canonical case is a sensor that fails in an always-ON or always-OFF state, where "neither of these faults can be detected until the machine fails to operate correctly." A cycle-count-keyed detector in a stalled pipeline is structurally identical: its input has gone constant, and the constant reads as nominal.
    2. Aeron.io, "Liveness Detection" (Distributed Systems Basics); CloudOpsNow, "What is Liveness probe?" (2026). — Establishes that liveness detection in distributed systems is "typically imperfect," that different failure detectors "can provide inconsistent results about the same monitored process," and — supporting the remedy — that timing parameters (frequency, timeout) are the controls that set sensitivity. The Kubernetes liveness-probe model is itself wall-clock-keyed (periodSeconds, failureThreshold), which is analogous precedent for the item's proposed companion rule: the industry-standard liveness primitive does not key on the monitored process's own progress counter.
    3. Machine-protection systems literature: "Controls and Machine Protection Systems" (arXiv:1608.02836); Industrial Monitor Direct, "Understanding Fail-Safe PLC Systems." — Watchdog timers are the established remedy for exactly this class: an independent timebase that must be actively fed, so that cessation of activity produces an alarm rather than silence. The watchdog is by construction wall-clock-keyed and independent of the monitored process's internal event count. This is direct engineering precedent for the item's unimplemented remedy.
    4. Nenvitech / fail-safe diagnostics literature on "detected" vs "undetected" failure classification. — Supports the item's implied severity claim: the relevant design question is not the failure rate but the *diagnostic coverage* — what fraction of failures the monitor can see at all. A detector whose sensitivity is conditioned on the monitored process has coverage that goes to zero in the worst case.
    5. COUNTER-INDICATION, reported per spec (no cherry-picking): "Bistable by Construction: Wall-Clock-Calibrated State Monitors Have No Moment-Detection Regime at Agent Cadence" (arXiv:2606.19386). — Argues that a wall-clock-calibrated leaky-integrator monitor on agent-cadence streams "has no cadence regime in which it detects moments" — below a critical band it alarms constantly, above it the monitor is dead, and real deployments sit in the transition band. This does not challenge the item's diagnosis but does challenge the sufficiency of the proposed remedy in precisely C2A2's regime (agent cadence). I have not read the against-side file and do not know whether 15b retrieved this; recording it here because my spec forbids reporting only the favourable range.

  Strength of support: Moderate

  Summary: The diagnosis is strongly supported by transfer from safety engineering, where a monitor whose pass state is reachable while the monitored subsystem is dead is a named and central failure mode, and where the standard classification (detected vs undetected failure, diagnostic coverage) makes the item's concern quantifiable. The watchdog timer is a direct, mature, and near-universal engineering precedent for the specific remedy proposed: an independent wall-clock timebase that must be actively fed, so that absence of activity is itself the alarm. Support is graded Moderate rather than Strong for two reasons. First, all direct evidence is analogous rather than domain-matched — it comes from embedded, PLC, and distributed-systems monitoring, not from queue-management of a self-awareness pipeline. Second, the one source found that addresses wall-clock monitors *at agent cadence specifically* argues the remedy is bistable in exactly this regime. The observation is well grounded; the remedy's adequacy for C2A2's cadence is not established by this search.

  Caveats: (a) Watchdogs assume a known nominal period against which silence becomes anomalous. C2A2's pipeline cadence is nominally daily but has an observed history of skipped and partial runs, so the threshold is not free to choose and a badly-set threshold reproduces the alert-fatigue failure named in PRESUMPTION-495. (b) The item's stated in-house test (add the rule, count newly-visible stale items among the 67 carried) is a good discriminating test and should precede adoption — this is exactly the discipline ASSUMPTION-479 says is being skipped, so implementing this remedy without running the test would be a same-day instance of the pattern the same batch flags. (c) The counter-indication in source 5 should be read before implementation. (d) No literature was found on staleness detection for *agent work queues* as such; the domain-matched search returned nothing. Partial NOVELTY on the specific application.

  Recommendation: PARTIALLY-SUPPORTED
