SEARCH-AGAINST-PRESUMPTION-1135:
  Date searched: 2026-10-14
  Original item: PRESUMPTION-1135
  Original statement: [inferred] Each health report presumes its own vantage suffices; none consumes the others' FAILs. Morning project status certified "no other issues" hours after scheduler health logged 7 FAILs; system health cited yesterday's telemetry failure. With 4+ overlapping monitors, no one owns the aggregate. Question under test: do multiple uncoordinated monitors raise or lower detection of failures?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1135
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cited evidence across 2026-10-13 transcripts and wiki files.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Note on what is being challenged: The presumption bundles (a) an observation (reports did not consume each other's FAILs) and (b) an implied concern that uncoordinated overlap is the problem and an aggregate owner is the fix. (a) is a factual in-house matter and was not challenged by literature. The search targeted (b).

  Sources:
    1. Landau M, 1969. "Redundancy, Rationality, and the Problem of Duplication and Overlap." Public Administration Review 29:346-358 (volume per secondary citation; one source printed "39", unverified). — Classic argument that overlap/duplication between organisational units, often treated as waste, is what produces reliability; uncoordinated parallel channels raise the probability that at least one catches a failure. Directly challenges "overlap without coordination is the defect." [Level: snippet/secondary only.]
    2. Bendor J, 1985. Parallel Systems: Redundancy in Government. University of California Press. — Formal development of Landau: parallel, independent agencies increase reliability and detection relative to a single coordinated channel, under independence. [Level: publisher snippet only.]
    3. Practitioner SRE/HA guidance (QNX High Availability Manager docs; "dead man's switch" monitoring write-ups). — An aggregating monitor/health manager becomes a single point of failure and must itself be watched by an independent, out-of-domain channel. Challenges the implied remedy: centralising ownership of the aggregate adds a new failure mode (aggregator silently stalls and reports stale "all clear" — the very "stopped ingest reported live" risk). [Level: snippet; vendor/practitioner, not peer-reviewed.]
    4. EEMUA 191 / alarm-flooding literature (Yokogawa vendor material; US CSB alarm-flood findings via secondary commentary). — Aggregating many monitors' FAILs into one operator view produces alarm floods in which critical alarms are missed; rationalisation (removing redundant alarms) improves detection. Challenges "consume all others' FAILs" as a fix. [Level: snippet; vendor sources; CSB report not read.]
    5. (Supports the concern; reported for balance) Sagan SD, 2004. "The Problem of Redundancy Problem: Why More Nuclear Security Forces May Produce Less Nuclear Security." Risk Analysis 24(4):935-946. — Redundancy can lower safety via common-mode error, social shirking (each unit assumes another will catch it) and overcompensation; Ghaffarzadegan (2007 SD conference) simulation found shirking amplifies common-mode error. This matches the presumption's "each vantage presumes it suffices" pattern. [Level: abstract/secondary only.]
    6. (Supports the concern) Darley & Latané 1968 diffusion of responsibility (secondary sources only). — Multiple observers each defer; relevant by analogy only to agentic monitors. [Level: secondary.]

  Strength of challenge: Moderate (against the remedy) / Weak (against the observation)

  Summary: Organisation-theory work (Landau, Bendor) predicts that overlapping, uncoordinated monitors RAISE detection probability provided their failures are independent, so the overlap itself is not the defect. Engineering and alarm-management practice further warns that the natural remedy — one owner aggregating every FAIL — creates a single point of failure and alarm flooding, both of which lower detection. Against this, Sagan's redundancy paradox describes exactly the observed pathology (shirking/"someone else has it"), which agents emulating human report conventions may reproduce. Net: the literature challenges the inference that overlap is harmful and that central aggregation is the cure, but does not challenge the observation that the monitors are currently failing to cross-reference. Whether overlap helps depends on independence and on whether any channel's FAIL can reach a decision-maker.

  Specific risks: If C2A2 responds by building one aggregate owner, a stalled or stale aggregator will reproduce the "stopped ingest reported live" failure at a single point, and alarm volume from 4+ feeds may bury signal. If C2A2 leaves overlap unaddressed, Sagan-type shirking persists.

  Mitigations available: Keep monitors redundant but make each one's FAILs directly visible (no suppression by downstream "all clear"); an out-of-domain dead-man heartbeat on the aggregator; alarm rationalisation (dedupe, prioritise); rule that an "all clear" must cite freshness of the inputs it relies on.

  Recommendation: PARTIALLY-CHALLENGED

  Search scope: preliminary search — 5 web searches, 0 page fetches; all sources at snippet/secondary level.

STEELMAN:
  Item: PRESUMPTION-1135
  Strongest counterargument: Overlap is the feature, not the bug. Four uncoordinated monitors give four independent chances to catch a stopped ingest, and in fact the 7 FAILs WERE detected — by the scheduler monitor. The failure was not overlap but that a downstream summary was allowed to overwrite upstream evidence. Introducing an aggregate owner concentrates trust in one more report that can go stale, flood, or shirk, converting a parallel system (fails only if all miss) into a series one (fails if the aggregator misses). Landau's lesson is that eliminating "duplication" in the name of coherence is how reliable systems become fragile.
  What would need to be true for C2A2 to be safe: Each monitor reads a different signal (not the same log), each monitor's FAIL is surfaced to Tom without needing another report to relay it, and no report is permitted to assert "no other issues" without enumerating its inputs.
  How to test: Over the last N days, list each real failure and which monitors flagged it; compute per-monitor and union detection rates and how often a later report contradicted an earlier FAIL. High union detection plus frequent "all clear" overrides => the problem is suppression, not overlap.
