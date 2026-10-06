SEARCH-AGAINST-PRESUMPTION-1096:
  Date searched: 2026-09-30
  Original item: PRESUMPTION-1096
  Original statement: Monitors co-located with the monitored system give adequate coverage.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1096
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 7886254b, b5f437f2, 6f1262b0.
      15b: Searched for challenging literature (scheduled run 2026-09-30; depth: web search + selective fetch)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Wilkinson, J. (2016). "Practical Alerting from Time-Series Data." Ch. 10 in Beyer et al.
       (eds.), Site Reliability Engineering, O'Reilly/Google. [Fetched: full chapter.] Monitoring
       from inside the system "does not provide a full picture ... queries lost due to a server crash
       never make a sound. You can only alert on the failures that you expected." Google adds
       external black-box probes (Prober), runs "two or more global Borgmon" replicas for "diversity
       in the face of maintenance and outages for this otherwise single point of failure", and
       exports internal metrics "for monitoring the monitoring". The reference practice treats a
       monitor that shares a failure domain with its target as incomplete by design.
    2. U.S. NRC (2023/2025). "Guidance for Addressing Common Cause Failure in High Safety-Significant
       Safety-Related Digital I&C Systems" (ML23205A190; ML25198A311). Also Oak Ridge National
       Laboratory (2013). "Update on Common-Cause Failure Experience and Mitigation", ORNL/TM-2013/563.
       [Search-result level.] Common-cause failure is defined as two or more components failing from
       one cause. The historical mitigation is independent and diverse instrumentation and control.
       The ORNL report adds that independence and diversity do not address every CCF source. A
       co-located monitor has neither.
    3. Practitioner and security sources. UpTime Web Hosting, "Remote Server Monitoring" ("The
       external check should not depend on the same server, power supply or internet connection it
       is monitoring, otherwise the failure can silence both"). ClawGuard, arXiv:2605.06205
       (host-based monitors "share the same trust boundary as the workload they observe"). [Both
       search-result level.]
    4. Background knowledge, not fetched this run. Prometheus/Alertmanager practice ships an
       always-firing "Watchdog" alert routed to an external dead man's switch, so that silence from
       the monitor itself triggers an alarm.

  Strength of challenge: Strong

  Summary: Safety engineering (common-cause failure, independence and diversity) and SRE practice
    (black-box probing, replicated and diverse monitors, meta-monitoring) agree that a monitor
    sharing a failure domain with its target does not give adequate coverage. In C2A2 the monitor
    and its targets share one scarce resource, sandbox disk. On 09-29 disk exhaustion silenced the
    health report while also degrading the monitored tasks. This is the common-mode pattern the
    literature describes: the detector goes quiet exactly when detection matters. No source found
    defends co-located monitoring as sufficient on its own. Co-located (white-box) monitoring is
    defended only as a complement to external checks.

  Specific risks: Disk-full, runaway processes or sandbox failure produce partial or missing health
    reports. Missing or partial reports get read as "nothing to report". Report rotation also fails
    (6 kept instead of 3), which makes the disk problem worse. The failures most in need of
    detection are the ones that silence the detector.

  Mitigations available: Add an out-of-sandbox check, such as a host-side (macOS) scheduled task or
    an external service, that expects a daily health artifact and alerts when it is absent or
    partial (a dead man's switch). Reserve disk headroom for the monitor. Treat a partial report as
    RED by default.

  Search scope: Preliminary: 2 searches, 1 fetch (the fetch is shared with ASSUMPTION-1702).
  Excluded results: Dynatrace, Middleware, NAKIVO product pages; USPTO patents on out-of-band
    agents (surfaced; not cited).

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1096
  Strongest counterargument: Every mature reliability discipline treats a monitor that shares a
    failure domain with its target as structurally blind to that domain's failures. Nuclear I&C
    requires independence and diversity for this reason, and Google layers external probes and
    replicated monitors over its in-system monitoring. The 09-29 disk-full event was not bad luck.
    It is the textbook case: the monitor's worst day is the day it reports least. A monitor that can
    be silenced by what it monitors reports health only when things are healthy.
  What would need to be true for C2A2 to be safe: A missing or partial health report is itself
    detected and escalated by something outside the sandbox, and the monitor has reserved
    resources.
  How to test: Fill the sandbox disk on purpose (or simulate ENOSPC) and check whether any alert
    reaches Tom within 24 hours.
