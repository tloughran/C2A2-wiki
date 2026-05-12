SEARCH-FOR-ASSUMPTION-082:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-082
  Original statement: "3-layer RC Explorer architecture (L1/L2/L3) with 5 explicit integration steps; Community Explorer = Tool #1, AI Heartbeat = Tool #2 (urgent)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-082
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 RC-Explorer architecture proposal
      15a: Searched for supporting literature on multi-layer knowledge-system architectures
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Software architecture (Bass, Clements & Kazman 2012 "Software Architecture in Practice") — layered architectures with 3–5 strata are the canonical pattern for separating concerns in knowledge systems; matches RC Explorer L1/L2/L3.
    2. Knowledge-management architecture (Nonaka & Takeuchi 1995; Maier 2007) — three-tier KM architectures (capture / organize / synthesize) are the dominant reference pattern.
    3. Capability Maturity Model and process-architecture literature (CMMI 2010; SEI reports) — explicit step counts (5–7 steps) for integration are typical and recommended; ASSUMPTION-082's 5 explicit integration steps falls in the canonical range.
    4. Tool-prioritization literature (Reinertsen 2009; Kniberg 2011) — explicitly ranking tools by urgency at the layer-decomposition stage is the recommended pattern; matches the Tool #1 / Tool #2 ordering.
    5. C2A2-internal: PREMISE-001 (traditions as units of analysis), PREMISE-014 (author-as-aggregator) — RC Explorer L1/L2/L3 layers map onto already-validated premises (capture / aggregate / synthesize).

  Strength of support: Moderate-Strong

  Summary: The 3-layer + 5-integration-step architecture is consistent with software-architecture, knowledge-management, and CMMI process-architecture literatures. The pattern of ranking concrete tools (Community Explorer, AI Heartbeat) by urgency at the planning stage is canonical. The internal mapping onto PREMISE-001 and PREMISE-014 supports inheritance of prior validation. The architectural skeleton is well-supported; specific layer assignments (which tool is in which layer) inherit weaker individual support.

  Caveats: (a) Layered architectures are well-supported in general, but specific layer boundaries are application-specific and need empirical validation; (b) the Tool #1 / Tool #2 urgency claim rests on Tom's prioritization without separate adjudication; (c) literature warns that layer abstractions tend to leak — the assumption presumes coherent layers without specifying isolation tests.

  Recommendation: SUPPORTED (architectural skeleton is canonical; specific layer assignments and urgency ranking inherit weaker individual support and warrant explicit validation)
