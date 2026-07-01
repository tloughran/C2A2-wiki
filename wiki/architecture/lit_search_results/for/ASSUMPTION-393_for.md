SEARCH-FOR-ASSUMPTION-393:
  Date searched: 2026-07-01
  Original item: ASSUMPTION-393
  Original statement: "Clear the PRS backlog now via a single attended ingestion pass rather than a bounded unattended agent (acting on OPEN-101)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-393
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-06-30 EOD "PRS backlog runbook" attended session
      15a: Searched for supporting literature (genuine web search 2026-07-01)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. IMS Datawise / Forage.ai — human-in-the-loop (HITL) extraction reduces coding error rates 30-40% vs fully automated extraction; pure automation plateaus at ~94-95% accuracy while HITL reaches enterprise-required accuracy. Directly supports preferring an attended pass for quality-sensitive structured-claim extraction.
    2. Digital Divide Data / Docsumo — HITL vs full automation decision framework: human involvement is essential in domains with compliance/quality stakes where small errors compound. PRS ingestion (structured claim cards feeding the connectome) is exactly such a quality-sensitive domain.
    3. C2A2-internal: the attended runbook found and correctly handled the 8-of-152 QC drops and the proposal_id-vs-filename keying bug (A-396) mid-pass — an unattended bounded agent would have committed those silently.

  Strength of support: Moderate-Strong

  Summary: The HITL literature strongly supports a human-attended pass for quality-sensitive extraction: measured error-rate reductions of 30-40% and the observation that automation alone plateaus below the accuracy such pipelines require. For a one-time backlog whose contents feed a downstream connectome and validated-premise register, the attended choice is well grounded. The support is for the ONE-TIME correctness of the decision, not for its durability.

  Caveats: The HITL advantage is about per-item accuracy on a bounded set; it says nothing about repeatability or scale. The literature explicitly warns that "what works in a pilot collapses under volume" if humans are required for every item indefinitely — so the support does not extend to using attended passes as the standing cadence (that gap is PRESUMPTION-425).

  Recommendation: SUPPORTED (Moderate-Strong — for the one-time, quality-sensitive backlog clear; durability is out of scope)
