SEARCH-FOR-PRESUMPTION-220:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-220
  Original statement: "On-cadence firing == healthy pipeline — no input/output-validity check paired to cadence."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-220
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — pipeline health inferred from on-cadence firing (the N=3 streak), with no input/output-validity check paired to liveness.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Liveness monitoring (heartbeats). — On-cadence firing is a legitimate liveness signal; weak support that cadence indicates the pipeline is at least running.
    2. Beyer, B. et al. (2016). "Site Reliability Engineering" (golden signals). — Liveness is one of several monitoring signals worth tracking.

  Strength of support: Weak

  Summary: On-cadence firing is a valid liveness signal — it shows the pipeline is running — giving weak support. But liveness is only one of the SRE golden signals; the same source insists correctness/quality must be monitored alongside it. The presumption equates liveness with health, which the supportive literature explicitly does not: a job can fire perfectly on time while producing garbage.

  Caveats: Support is for liveness-as-one-signal, not liveness-as-health; correctness is a separate, required signal.

  Recommendation: PARTIALLY-SUPPORTED (liveness only)
