SEARCH-FOR-ASSUMPTION-480:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-480
  Original statement: A summarizing agent asserted "No failures to report" and named two failing pipelines as clean, on a morning with four concurrent failure reports, and delivered it outbound.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-480
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 morning project status transcript, cross-checked against four same-morning failure transcripts
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. ServiceNow Developer Blog, "Every Dashboard Is Green. The Service Is Down. Explain That!" — Near-verbatim precedent for the item's observation, treated as a routine and named condition rather than an anomaly. Diagnosis: green dashboards alongside a degraded service occur "whenever a service failure stems from a dependency issue — a shared component that looks fine on its own," with the key principle stated as "infrastructure health and service health are not the same thing." Establishes that a false-green summary is an expected structural property of component-oriented reporting, not an isolated defect.
    2. ThousandEyes, "Why You Shouldn't Trust (Only) the Status Page." — Supports the specific mechanism of naming failing components as clean: "by splitting the status update into different service components, it can give a false impression of how serious an outage is... the dashboard is only reflecting the status of those individual components, not the overall service delivery chain." Names the root causes as component-level rather than holistic reporting, absent real-time data, and no root-cause detail. Also supplies the illustrative case — an authentication component down makes the rest of the green irrelevant — which is the structure of "two failing pipelines reported clean."
    3. "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime" (arXiv:2606.14589). — The closest domain match found, and strikingly specific: documents a production case where "a weekly review job whose LLM call failed fell back to a mechanical line-filter that emitted leftover container headings as if they were review content, and the user-visible artifact looked plausible enough to pass casual inspection for weeks." Coins the operative principle: "a fallback path that manufactures plausible-shaped output is a hallucination implemented in shell." This is empirical precedent for a summarising agent in an LLM fleet emitting confident, well-formed, false status — including the aggravating factor the item stresses, that it was delivered outbound.
    4. Data lineage / observability literature: DataHub, "Data Lineage vs. Data Observability"; Datadog, "Understanding data lineage"; Atlan, "Data Lineage and Data Observability." — Supports the item's proposed remedy. Column-level lineage "traces every field from source to dashboard," and observability supplies freshness monitoring so teams can "find the root cause of broken dashboards or models faster." The item's remedy — bind each health claim to a named artifact with a freshness bound — is the standard combination of lineage plus freshness SLA, an established practice with mature tooling.
    5. Silent-failure detection prior art: "Method, system and computer program product for improving system reliability" (US 7,278,048). — Codifies detecting silent failure by comparing live operational measurements against an established operational signature. Precedent for the item's implied check: a "no failures" assertion should be inconsistent with a signature derived from same-period artifacts.

  Strength of support: Strong

  Summary: The event ASSUMPTION-480 records is a well-documented class with an established name and an established cause. Monitoring practitioners treat "all green while the service is down" as a structural consequence of reporting that aggregates component status without binding to the service delivery chain, and specifically identify component-splitting as the mechanism by which a summary understates or misstates severity — matching the item's detail that two failing pipelines were individually named as clean. The LLM-runtime taxonomy supplies domain-matched empirical precedent that a summarising agent's fallback path can manufacture plausible-shaped false status that survives casual inspection for weeks, which raises the item's severity: the failure is not merely possible in agent fleets, it has been observed and characterised in one. The item's proposed remedy is also the literature's: trace each derived claim to a named source with a freshness bound, i.e. lineage plus freshness monitoring, which is mature and tool-supported rather than novel.

  Caveats: (a) The retrieved literature explains false-green as component-vs-service scope mismatch; the item's case may instead be a read-set problem (the summariser never read the failure artifacts at all), which is a different mechanism and is the one PRESUMPTION-503 names independently. These two mechanisms have different fixes — holistic service modelling vs read-set coverage — and this search does not discriminate between them. Per ASSUMPTION-479's own discipline, that discrimination should be done before a remedy is chosen. (b) The "delivered outbound" aggravating factor found no specific literature; the harm of a false-green that leaves the organisation is asserted, not evidenced here. (c) Source 3 is a preprint; source 5 is a patent. Sources 1, 2 and 4 are high-quality practitioner material rather than peer-reviewed research — this whole area is documented mainly in industry sources. (d) The item is a single dated incident; the literature establishes the class, not the frequency.

  Recommendation: SUPPORTED
