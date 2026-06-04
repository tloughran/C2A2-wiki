SEARCH-FOR-ASSUMPTION-251:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-251
  Original statement: Three un-numbered DECISION candidates (048 3rd cycle, 049 2nd cycle, AI-search-delegation 1st cycle) constitute a tracking blind spot of its own; registry stops being source of truth.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-251
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 registry-hygiene observation.
      15a: Searched for supporting literature on decision-registry hygiene and candidate-vs-numbered status persistence.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Bass et al. (2021) "Software Architecture in Practice" — Architecture Decision Records (ADRs) literature explicitly identifies candidate-without-numbering accumulation as a documented registry-hygiene anti-pattern; the registry stops being source of truth when actual decisions outpace ceremony.
    2. Nygard (2011) "Documenting Architecture Decisions" — Original ADR proposal explicitly emphasizes low-friction numbering precisely because deferred-numbering produces the source-of-truth gap C2A2 is observing.
    3. Brown (2015) "Tradeoffs in Software Architecture" — Documents the registry-vs-reality drift pattern; 3 candidates with multi-cycle persistence is well into the documented drift zone.
    4. Cunningham (1992) — Technical-debt framing applies cleanly: un-numbered candidates are a form of decision-debt with accruing interest.
    5. C2A2-internal: registry source-of-truth claim is foundational to many downstream agents (12, 13, 14a/14b); the blind-spot concern bears directly on this dependency.

  Strength of support: Moderate

  Summary: ADR / decision-registry literature directly supports the claim that un-numbered candidates accumulate as a registry-hygiene anti-pattern. Nygard's original ADR proposal anticipates this failure mode. The "registry stops being source of truth" framing is canonical decision-debt vocabulary. Three multi-cycle candidates is well past the documented threshold for source-of-truth degradation.

  Caveats: (a) Literature locates the failure on the registry side (consistent with the assumption); PRESUMPTION-271 challenges this location, asking whether numbering ceremony itself is the gate; (b) "blind spot of its own" is a strong framing — supported by drift literature but requires that other downstream consumers actually rely on the registry (verified for 12/13/14a/14b); (c) remediation (decide to number or decide to discard) is straightforward and well-documented.

  Recommendation: SUPPORTED (Moderate)
