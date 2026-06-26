SEARCH-AGAINST-ASSUMPTION-364:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-364
  Original statement: "That archiving a History snapshot only when content changes (one entry per real update) is the right anti-duplication rule"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-364
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: snapshot-on-change assumed correct anti-duplication rule
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Content-hashing / canonicalization literature (XML/JSON canonical forms; reproducible-build determinism). - Hashing a non-canonical representation makes non-semantic differences (timestamps, key ordering, whitespace) read as "changes," producing duplicate-but-meaningless entries - the opposite of the intended dedup.
    2. Change-data-capture literature on false negatives. - If the change detector compares only a subset/digest, a real semantic change that does not alter that field is MISSED, so a true update is never archived.

  Strength of challenge: Weak

  Summary: The rule itself is sound; the challenge is on its IMPLEMENTATION boundary. "Content changed" is only as good as what is compared. Compare too much (raw bytes with embedded timestamps/ordering) and you get churn - duplicate entries for non-semantic diffs. Compare too little (a coarse digest) and you get silent misses - real updates not archived. Both are documented failure modes of naive change-detection. Stakes are low (verified in-session) and the fix is canonicalization, but the edge case named in the item (near-identical content) is real.

  Specific risks: Either history churn (many near-identical entries) or missed updates (a real change not snapshotted) depending on what defines "changed."

  Mitigations available: Canonicalize/normalize before hashing; define the semantic fields that constitute a "change"; add a periodic full-snapshot safety net to bound missed-change risk.

  STEELMAN:
    Item: ASSUMPTION-364
    Strongest counterargument: "Snapshot on change" is correct in principle but underspecified: without a defined canonical form, the same rule yields either duplicates or silent misses, so the rule's correctness is entirely inherited from the change-definition it omits.
    What would need to be true for C2A2 to be safe: A stable canonicalization is applied before comparison, and the comparison covers exactly the semantic content of interest.
    How to test: Feed semantically-identical inputs differing only in whitespace/order (expect: no new entry) and a semantic change to a non-compared field (expect: new entry). Mismatch reveals the boundary bug.

  Search scope: Canonical hashing; change-data-capture false negatives. Adequate.

  Recommendation: PARTIALLY-CHALLENGED
