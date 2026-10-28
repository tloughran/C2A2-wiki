# PRESUMPTION-1193 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY. Broader search recommended. Scheduled run 2026-10-28 (lock held by parent). Budget for this item: 2 web searches (standard), 0 fetches. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge": this item is a concern. Following the template convention (PRESUMPTION-1190), I search against the presumption as 14b states it: that a stripped, commit-stamped print of a moving corpus stays auditable and citable. Evidence that a version stamp alone does not support audit, or that frozen editions of living documents mislead, counts as a challenge. I did not verify the in-house facts (stamp `#71cbed5`, what was stripped, the 65/307 harvest).

```
SEARCH-AGAINST-PRESUMPTION-1193:
  Date searched: 2026-10-28
  Original item: PRESUMPTION-1193
  Original statement: "[inferred] The print edition presumes that stripping internal material
    (Related-records lines, QC notes, sources) keeps the record auditable ... Is a frozen print
    of a moving corpus (all 307 days changed since 09-03) a citable edition, and what links a
    printed claim back to its trace?"
  Claim tested: Versioned publication of living documents (living systematic reviews;
    software/data version citation with DOIs or commit stamps); provenance retention in
    derived editions (W3C PROV). Does a commit stamp alone suffice for auditability?

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1193
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the print build and the same day's vault defects.
      15b: Searched for challenging literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. CASRAI, "Living and versioned research outputs: dynamic publications and continuous
       updates" (casrai.org/wp/?p=1300 and tag pages). [snippet only; advocacy overview]
       — Boundary condition. Without clear versioning and dating of each update, readers
       cannot tell which version they are using, and superseded versions keep being cited as
       authoritative. The recommended fix is a DOI per version plus a concept DOI for the
       latest, so a citation is both fixed and resolvable.
    2. PeerJ blog, "Software Heritage is the repository the science community needs." [snippet
       only]
       — Direct challenge to "stamp alone". People cite GitHub repositories by commit hash,
       but GitHub is not an archive; the hash only works if the commit stays retrievable. The
       author recommends linking hashes to Software Heritage identifiers (SWHIDs).
    3. CASRAI, "Research software as a first-class output: citation, identifiers and credit."
       [snippet only]
       — Partly supportive. A result can be verified only if the reader can identify the
       exact version that produced it, so a stamp is necessary. It pairs the intrinsic
       identifier with a citation-layer DOI.
    4. De Nies et al., 2013. Git2PROV (ISWC poster); gitlab2prov. [snippet only]
       — Mitigation evidence. Version-control history can be exported as W3C PROV, so the
       trace from a printed claim to its history can be kept machine-readable outside the
       print.

  Strength of challenge: Moderate on "a commit stamp alone suffices" (it is necessary but not
    sufficient without an archived, resolvable copy). Weak on the stripping question: I found
    no source on provenance loss when a derived edition removes trace lines.

  Summary: The versioning literature treats a version identifier as necessary for audit but
    not enough on its own. It must resolve to an archived copy, and readers must be able to
    tell a frozen version from the current one. A hash in a repository that is private,
    unpublished or later rewritten does not let a reader check anything. Living-document
    practice warns that frozen editions get cited as current. The search did not address
    whether removing claim-level trace lines from a print breaks audit; that remains open.

  Specific risks: The print is cited as "the C2A2 record" while the corpus moves on, so a
    reader cannot reconcile a printed claim with the live trace. If `#71cbed5` is not in a
    public or archived repository, the stamp proves nothing to an outside auditor. The
    stripped QC notes are where the known defects (65/307 harvest; High ratings from an
    unheard recording) were visible, so the print may look cleaner than the record.

  Mitigations available: Archive the stamped commit (e.g., Software Heritage or a Zenodo DOI)
    and print the resolvable identifier. Mark the print as a dated, superseded-by-default
    edition with a pointer to the latest. Keep a claim-to-trace map (stable claim IDs, or a
    PROV export) outside the print. Carry a short errata or known-defects page into the print
    rather than stripping all QC material.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1193
  Strongest counterargument: A commit stamp is a promise that the source exists, not access to
    it. Scholarly practice for living outputs requires a resolvable, archived identifier for
    each version and a clear signal that a version is superseded, because otherwise frozen
    copies are cited as current. The print strips exactly the apparatus that links claims to
    evidence, and that apparatus showed the defects on the day of the build. An "auditable
    record" with the audit trail removed and a stamp only the designer can resolve is
    auditable only by the designer.
  What would need to be true for C2A2 to be safe: the stamped commit is archived and publicly
    resolvable; each printed claim carries a stable ID that maps to its trace; and the print
    is labelled as a dated snapshot.
  How to test: Give an outside reader the print alone and ask them to trace three printed
    claims to their sources. Record success and time taken.
```

Source quality: all snippets; CASRAI pages are advocacy-style overviews. Systemic note: extends the existing 'artefact-as-proof' candidate (a stamp taken as proof of auditability); see PRESUMPTION-1191_against.md.
