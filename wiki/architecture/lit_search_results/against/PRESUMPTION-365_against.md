SEARCH-AGAINST-PRESUMPTION-365:
  Date searched: 2026-06-19
  Original item: PRESUMPTION-365
  Original statement: "[inferred] The single-source-of-truth payoff presumes agents/Tom will actively maintain the wiki.md Summary blocks going forward."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-365
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated maintenance dependency beneath the SSOT payoff
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Documentation/data rot — documentation reliably goes stale when its currency depends on voluntary discipline; "docs rot" is a well-documented default, so an SSOT whose payoff rests on ongoing manual upkeep tends to erode.
    2. Maintenance-contingent benefits decay — benefits that require sustained human effort to realize are systematically over-estimated at design time and under-delivered over time (the upkeep is the first thing dropped under load).
    3. Single-maintainer / bus-factor fragility — when upkeep depends on one or two people remembering to update Summary blocks, lapses are likely and unannounced; the SSOT then quietly serves stale content with full apparent authority.

  Strength of challenge: Moderate

  Summary: The presumption is correct that the payoff DEPENDS on upkeep — and that is the problem: the documentation-rot literature says discipline-dependent currency is the default to FAIL, not to hold. An SSOT whose freshness rests on agents/Tom remembering to maintain the blocks is likely to drift into authoritative-looking staleness. The dependency is real and is a liability, not a safe assumption.

  Specific risks: Summary blocks go stale; the pop-ups present outdated bios with the full authority of "single source of truth"; staleness is invisible because there is no second copy to disagree.

  Mitigations available: Add a freshness signal (last-updated date per block; a check that flags blocks unchanged past a threshold or out of sync with tradition activity); fold Summary upkeep into the agents' existing maintenance loop so it is not a separate discipline; make staleness visible rather than relying on memory.

  STEELMAN:
    Strongest counterargument: The Summary blocks live in the same wiki.md the agents already maintain continuously, so upkeep is not a NEW discipline but a rider on existing maintenance — the rot argument applies to orphaned docs, not to a block inside an actively edited canonical file.
    What would need to be true for C2A2 to be safe: Summary-block upkeep is genuinely coupled to the agents' routine maintenance (not a separate remembered task), and staleness is detectable.
    How to test: Check whether Summary blocks are updated as a side effect of normal tradition maintenance; if they require separate remembering, the rot risk is live.

  Search scope: documentation/data rot; maintenance-contingent benefit decay; single-maintainer upkeep fragility. Comprehensive.

  Recommendation: CHALLENGED
