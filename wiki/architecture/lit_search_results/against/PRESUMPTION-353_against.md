SEARCH-AGAINST-PRESUMPTION-353:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-353
  Original statement: "[inferred] Vault folder-count is the authoritative source of team membership (1 folder = 1 member = 1 seat)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-353
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated data-model premise beneath ASSUMPTION-321
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ontology-as-data-model / "the map is not the territory" (data-modeling critique). — Letting a storage artifact (a directory listing) define a substantive concept (team membership) inverts the proper dependency: membership should be defined by a criterion and the folders should REFLECT it, not constitute it. A filesystem is an implementation detail; treating it as authoritative imports incidental structure (stub folders, archived folders, merged/split traditions) into the concept.
    2. Single-source-of-truth design (data integrity). — A robust SSOT is an intentional, validated registry, not a side-effect of where files happen to live. Folder count is mutated by routine operations (adding a scratch folder, reorganizing) that have nothing to do with membership decisions, so it fails the SSOT criterion of changing only on intentional domain events.
    3. Membership-criterion requirement (philosophy of science on demarcating programs; couples ASSUMPTION-321 / prior tradition-as-unit work). — Without an explicit criterion, "who is on the team" is decided by an accident of file organization; the count can change with zero conceptual deliberation, which is precisely what an authoritative membership source must not allow.

  Strength of challenge: Moderate

  Summary: The presumption is challenged: folder-count is at best a convenient INDEX, never the authoritative source of team membership. Letting the directory layout define the ontology means routine filesystem operations (a stub folder, an archive, a merge/split) silently change "the team" with no conceptual decision behind it. Authoritative membership requires an explicit criterion and an intentional registry that the folders reflect; the dependency the presumption asserts runs backwards. As a PRESUMPTION (the equation is implicit, not deliberated), it carries extra weight — the system is silently outsourcing a definitional question to its file tree.

  Specific risks: An accidental or archived folder inflates/deflates the "seat" count; a tradition split into subfolders double-counts; any analysis keyed on "number of team members" (and the contest/open-seat framing of PRESUMPTION-354) inherits an arbitrary, operations-driven number. Membership drifts without anyone deciding it changed.

  Mitigations available: Maintain an explicit membership registry (the criterion + the roster) as the source of truth; treat folders as a reflection to be RECONCILED against it (a periodic diff surfacing folders-without-members and members-without-folders — same reconciliation pattern as REVISE-110); define the membership criterion (couples ASSUMPTION-321) so the boundary is intentional.

  STEELMAN:
    Strongest counterargument: For a disciplined single-maintainer vault where the convention "one tradition = one folder" is deliberately and consistently upheld, the folder structure IS the intentional registry — convention-over-configuration makes the directory the SSOT in practice, and a separate registry would be redundant bookkeeping that can itself drift out of sync.
    What would need to be true for C2A2 to be safe: The folder-as-registry convention would need to be enforced (no stray/stub/archive folders in the traditions/ path) and reconciled, OR an explicit registry maintained; and the membership criterion must exist somewhere so the boundary is principled rather than incidental.
    How to test: Diff the current traditions/ folders against the intended roster; any folder that is not a member (or member not a folder) demonstrates that the count is not authoritative as-is.

  Search scope: Ontology-as-data-model risk, single-source-of-truth design, membership-criterion requirement. Comprehensive. (Couples ASSUMPTION-321; member of the Metabolism-proxy SYSTEMIC-RISK cluster.)

  Recommendation: CHALLENGED
