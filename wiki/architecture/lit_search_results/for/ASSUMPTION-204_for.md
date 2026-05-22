SEARCH-FOR-ASSUMPTION-204:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-204
  Original statement: "Coil altitude should encode discovery-time (~2026), not idea-age ("axis follows model")."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-204
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: design decision that a coil's vertical altitude encodes discovery-time, not the age of the underlying ideas.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Snodgrass, R. (1999). "Developing Time-Oriented Database Applications" (valid-time vs transaction-time / bitemporal). — A system must choose which time it encodes; transaction/discovery time is a legitimate, decision-relevant axis.
    2. Provenance/lineage visualization (W3C PROV; Git-history views). — Encoding when something entered the system is a standard, defensible choice.
    3. Temporal-network viz conventions (Bach et al. on time-varying graphs). — Time axes are a well-supported encoding.

  Strength of support: Moderate

  Summary: Choosing discovery/provenance time as the altitude axis is defensible: temporal-data theory recognizes multiple legitimate time axes, and provenance time is decision-relevant for 'what the system learned when.' Support is partial because the choice is genuinely underdetermined (PRESUMPTION-225) — idea-age is also defensible.

  Caveats: Bitemporal theory says both times carry information; collapsing to one loses the other. Best practice often makes the axis switchable.

  Recommendation: PARTIALLY-SUPPORTED
