SEARCH-FOR-ASSUMPTION-364:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-364
  Original statement: "That archiving a History snapshot only when content changes (one entry per real update) is the right anti-duplication rule"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-364
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: snapshot-on-change (content-hash dedup) assumed correct anti-duplication rule
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Quinlan & Dorward 2002. "Venti: A New Approach to Archival Storage." FAST. - Content-addressed, write-only archival storage stores a block only when its content (hash) is new; the canonical validation of "store only on real change."
    2. Git object model (content-addressable store; blobs keyed by SHA of content). - The dominant version-history system dedups identical content by construction; identical snapshots collapse to one object.
    3. rsync / content-defined chunking literature (Tridgell). - Change-detection on content is the established basis for avoiding redundant transfer/storage.

  Strength of support: Moderate

  Summary: "Archive only when content changed" is the standard and well-validated anti-duplication rule, instantiated in content-addressable storage (Venti), version control (Git), and delta/sync systems (rsync). One entry per real change is exactly how these systems avoid storing redundant snapshots. The principle is mature and low-risk. The only open question is the DEFINITION of "content changed" - i.e., what is hashed/compared - which determines false-positive (churn) and false-negative (missed) rates.

  Caveats: Validity depends on comparing a CANONICALIZED form. If non-semantic fields (timestamps, ordering, whitespace) enter the comparison, identical content can read as changed; if a meaningful field is excluded, real changes can be missed (see 15b).

  Search scope: Content-addressable storage; dedup; version control. Adequate.

  Recommendation: SUPPORTED
