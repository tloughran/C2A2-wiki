SEARCH-FOR-PRESUMPTION-722:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-722
  Original statement: That a provenance field naming a file that was not read is harmless because the two are believed identical; disclosed in prose while the artefact carries the live mtime — the prose-vs-artefact split PRESUMPTION-680 named, from the same task that answered it correctly two days earlier.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-722
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inferred by comparing where the caveat was recorded against where the field will be read
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Content-addressable storage literature (Git object model; general CAS design docs, e.g. Kivabe, "Git Object Hashing and Content Addressability"; DevOpsBeast, "Git Is a Content-Addressable Filesystem") — establishes the general engineering principle that when two artefacts are *verified* identical (via cryptographic hash of content), their origin/naming/location becomes provably irrelevant to correctness: "identical content = identical SHA = stored once," and provenance is irrelevant once content-identity is established.
    2. W3C PROV-O provenance model and related data-provenance literature (Secoda, "What constitutes provenance metadata in data management?"; eDIRepository, "Provenance Metadata") — [unverified — from search snippet] standard practice treats provenance metadata as administrative/structural annotation layered on top of content identity, consistent with the idea that a provenance *label* can be decoupled from the artefact's substantive correctness as long as content equivalence holds.
    3. Foldermanifest.com, "How to Find Duplicate Files Safely with Checksums" (2026) [unverified — from search snippet] — notes that hash-based duplicate detection has no false negatives (same content always yields the same hash) but does not eliminate the need to actually compute/check the hash; "believed identical" without verification is explicitly the weak link duplicate-detection tooling exists to close.

  Strength of support: Weak

  Summary: The literature on content-addressable storage and provenance metadata supports a narrower version of the presumption: if content identity is *verified* (e.g., by hash comparison), then a provenance field pointing to an unread-but-identical file is indeed harmless, because provenance/location is provably decoupled from correctness once content-addressing establishes equivalence. This is a well-established engineering pattern (Git, CAS systems). However, the presumption as stated rests on the two files being merely "believed identical," not verified identical — and no literature was found endorsing "belief" (as opposed to checksum/hash verification) as a sufficient basis for treating unread and read artefacts as interchangeable.

  Caveats: The support found is for a stronger, verified-identity version of the claim, not the as-stated "believed identical" version. Duplicate-file-detection literature explicitly frames unverified belief in identity as the exact failure mode that hash-checking exists to catch (false positives are technically possible via hash collision, and unverified visual/heuristic identity judgments are known to be unreliable). This is a moderate-confidence gap between what was found and what the presumption claims — the search did not surface anything addressing mtime-carrying artefacts specifically, so this is a preliminary rather than comprehensive search.

  Recommendation: PARTIALLY-SUPPORTED
