SEARCH-FOR-PRESUMPTION-370:
  Date searched: 2026-06-21
  Original item: PRESUMPTION-370
  Original statement: "[inferred] An agent-only day with no attended session is presumed to carry no extraction-worthy epistemic content ('null day' = nothing to record)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-370
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated salience criterion — extraction-worthiness presumed to track attended human activity
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (Weak-Moderate)

  Sources:
    1. Signal-to-noise / selective logging best practice — observability and logging guidance broadly holds that recording everything is itself an anti-pattern: indiscriminate capture raises storage and review cost and buries signal in noise. Salience-based filtering (log what is decision-relevant) is a defensible default, lending qualified support to NOT extracting from low-salience periods.
    2. Alert fatigue / attention economy (SRE & clinical-alarm literature) — over-recording and over-alerting degrade responders' ability to act on what matters; some filtering of routine, no-change periods is not just tolerable but recommended. This supports the impulse behind the presumption (don't manufacture content from nothing), though not its strong form.
    3. Sampling / event-driven instrumentation — much monitoring is deliberately event-triggered rather than continuous; firing on change rather than on every interval is a standard, resource-rational design choice.

  Strength of support: Weak-Moderate

  Summary: There is genuine, if qualified, support for the impulse behind PRESUMPTION-370: recording-everything is a recognized anti-pattern, and salience- or event-based filtering (capture what is decision-relevant, skip routine no-change intervals) is standard practice in logging, observability, and alarm design. This supports a weak form of the claim — "don't fabricate extraction content from genuinely empty periods." It does NOT support the strong form actually presumed — that an agent-only day reliably carries NO extraction-worthy content — because the supportive literature conditions filtering on the period truly being low-information, which is precisely the thing that cannot be known in advance for a self-auditing system.

  Caveats: The support is for resource-rational filtering, not for equating "no attended session" with "no system-state worth recording." The two come apart sharply when the unattended period is exactly when a silent failure occurs (see PRESUMPTION-369 / OPEN-086): the 06-19→06-20 "null days" in fact contained the system's most important signal (the pipeline stall). So the supportive case applies to human-salience filtering but not to system-liveness recording.

  Search scope: selective logging / signal-to-noise; alert fatigue / attention economy; event-driven vs continuous instrumentation. Comprehensive for the supportive direction.

  Recommendation: PARTIALLY-SUPPORTED
