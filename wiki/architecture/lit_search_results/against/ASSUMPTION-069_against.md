SEARCH-AGAINST-ASSUMPTION-069:
  Date searched: 2026-04-27
  Original item: ASSUMPTION-069
  Original statement: "Proposal-ID collisions are flagged-and-rolled-forward rather than blocked-on"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-069
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-04-27 — collision-detection-and-rename pattern
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Identifier-system failure literature (Bryant et al. 2014 on persistent identifiers; DOI/Handle system retrospectives) — flag-and-roll-forward in identifier systems creates downstream reference-rot when external systems cite the colliding ID before resolution.
    2. Distributed-systems anti-patterns (Kleppmann 2017 "Designing Data-Intensive Applications"): silent rename without explicit redirect is a known failure mode; downstream consumers see different referents under the same identifier across time.
    3. Aaronson on identifier-collision-rate scaling: at low N, collisions are rare and roll-forward is cheap; the pattern degrades as ID-space density increases (birthday-paradox-like growth).
    4. Database-replay / event-sourcing literature: rolling forward identifier collisions can break replayability if the original→renamed mapping is not durable.
    5. Audit-trail literature (Bates et al. 2015): flag-and-roll-forward is fine if the flag is durably persisted with the rename; if either is lost, the audit trail breaks.

  Strength of challenge: Weak-to-Moderate

  Summary: The pattern is sound at low collision rates with durable mapping, but scales poorly as ID-space density grows and depends on durable persistence of the rename. For C2A2 today, the assumption is well-supported; for the assumption to remain valid as proposal volume scales, durable mapping and scaling-rate monitoring are required.

  Specific risks: (a) ID-space density growth raises collision rate beyond cheap-correction regime; (b) external citations (e.g., specialist agents referring to a proposal by its pre-collision ID) become stale references; (c) audit-trail breakage if the rename map is not durably persisted.

  Mitigations available: (a) Track collision rate as a monitored metric; (b) ensure rename-map is persisted in the wiki rather than only in-flight; (c) consider explicit "redirect" entries (like HTTP 301) when an ID is renamed.

  Recommendation: PARTIALLY-CHALLENGED (the pattern is well-grounded at current scale; scaling and durable-mapping conditions should be monitored)

  STEELMAN:
    Item: ASSUMPTION-069
    Strongest counterargument: Flag-and-roll-forward is the right pattern *in expectation*, but it is conditional on (a) collision rate staying low, (b) rename-mappings being durably persisted, and (c) external referrers being able to follow renames. C2A2's two same-day collision instances in 2026-04-27 are a small data point; without explicit rate-monitoring and durable mapping, the assumption could silently degrade as proposal volume grows.
    What would need to be true for C2A2 to be safe: (a) Collision rate is tracked over time; (b) rename mappings are persisted in a durable, queryable record; (c) downstream agents are taught to follow renames.
    How to test: Sample 10 cross-references in older wiki content; check whether each resolves to the post-rename target. If any fail, the assumption is locally falsified.
