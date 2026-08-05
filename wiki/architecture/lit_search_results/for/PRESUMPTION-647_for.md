SEARCH-FOR-PRESUMPTION-647:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-647
  Original statement: That a guard's tolerance can be validly calibrated from
    the single incident that motivated it — thresholds of +20 skips and 25%
    node change derived from one observed 2 -> 1164 jump.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-647
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation of a guard whose
        thresholds were set from the single 2 -> 1164 skip-count jump that
        prompted it
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. ANSI/ISA-18.2 (Management of Alarm Systems for the Process Industries)
       and EEMUA Publication 191 (Alarm Systems: A Guide to Design, Management
       and Procurement, 4th ed.). — Both treat alarm rationalization as a
       lifecycle activity in which every alarm must be individually justified
       and then periodically re-reviewed; an incident-derived initial setpoint
       is a legitimate entry into that lifecycle, but the standards make
       ongoing revision mandatory rather than optional.
    2. Detection-as-code / detection-engineering practitioner literature
       (Splunk, Deepwatch, Work-Bench primers, 2025-2026). — Documents the
       established SOC practice of deriving a new detection rule from each
       observed incident, then version-controlling and iteratively tuning it;
       this is direct precedent for incident-seeded thresholds as a starting
       posture.
    3. Cvach, M., 2012. "Monitor Alarm Fatigue: An Integrative Review."
       Biomedical Instrumentation & Technology 46(4). — The counterweight:
       thresholds set too tight generate nuisance alarms, and when an alarm is
       viewed as a nuisance the operator disables, silences or ignores it,
       converting a safety control into a hazard.
    4. EEMUA 191 alarm-rate benchmarks (<6 alarms/operator/hour acceptable;
       >30 indicates a seriously deficient system) and ISA-18.2's alarm-flood
       definition (>10 alarms in 10 minutes). — Provides the empirical yardstick
       against which an incident-derived threshold must later be checked.

  Strength of support: Moderate

  Summary: The literature supports incident-seeded threshold setting as a
    legitimate first move, not as a finished calibration. Detection
    engineering explicitly recommends generating a detection from each
    incident, and alarm-management standards accept that setpoints originate
    from operational experience. What no source supports is treating the
    n=1-derived setpoint as settled: ISA-18.2 and EEMUA 191 both make periodic
    re-review a mandatory lifecycle stage, and the alarm-fatigue literature
    supplies the mechanism by which an unrevised, badly-placed threshold
    degrades into a disabled or ignored control. The practice is therefore
    defensible in its provisional form and indefensible in its terminal form.

  Caveats: Support is conditional on three things the literature treats as
    inseparable from the practice — an explicit review date, a measured false-
    alarm rate, and a documented rationale per threshold. None of the located
    sources offer a statistical basis for choosing the specific magnitudes
    (+20, 25%) from a single observation; the numbers are unconstrained by
    anything in the evidence base. The alarm-management standards are process-
    industry documents and transfer to software guards by analogy only.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: alarm threshold setting from
    single incidents; alarm rationalization; ISA-18.2 and EEMUA 191 lifecycle
    requirements; alert fatigue and nuisance-alarm disable rates; alert
    threshold design; detection engineering and detection-as-code; incident-
    derived detection rules and iterative tuning.
