SEARCH-FOR-ASSUMPTION-246:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-246
  Original statement: Swarm contract written to root `architecture/` as ground truth + mirrored to `wiki/architecture/swarm-contract.md` is the ground-truth doc for the two new weekly watch agents; architectural-reviewer pinned for post-ISME.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-246
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 swarm-contract canonization event.
      15a: Searched for supporting literature on canonical-source-plus-mirror conventions and ground-truth-document patterns.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. Nygard (2018) "Release It! 2nd ed." — Single-source-of-truth + mirror is documented as standard for runbooks and operational ground-truth; mirror convention is acceptable when drift is controlled.
    2. Bass et al. (2021) "Software Architecture in Practice" — Architecture-decision-records / canonical-architecture-docs literature supports a primary location + cross-references; the root + wiki mirror matches this shape.
    3. Allspaw (2015) — Runbook canonicalization is documented as best-practice; ground-truth location is a property of organizational discipline more than tooling.
    4. Kleppmann (2017) "Designing Data-Intensive Applications" — Replication / mirror conventions supported when accompanied by a defined consistency model.
    5. C2A2-internal: prior canonization events (decisions.md, presumptions.md, assumptions.md) have used analogous single-source patterns successfully.

  Strength of support: Moderate (canonical-source convention is well-supported; the specific root+mirror choice has trade-offs against symlink that the literature does not resolve).

  Summary: Canonical-source ground-truth conventions for architectural documents are well-supported across software-architecture and operational-readiness literature. Both Nygard and Bass support the pattern. The specific implementation choice (write to root + mirror to wiki) is one valid approach among several; symlink and single-location are also documented. The "architectural-reviewer pinned for post-ISME" deferral is the contested element (PRESUMPTION-274).

  Caveats: (a) Mirror conventions need a defined consistency model — not visible in the assumption; (b) post-ISME named-trigger deferral is a separate concern (PRESUMPTION-274); (c) the relationship between root and wiki/architecture during the pre-ISME period is not separately documented.

  Recommendation: PARTIALLY-SUPPORTED (Moderate)
