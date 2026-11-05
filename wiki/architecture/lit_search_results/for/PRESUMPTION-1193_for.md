SEARCH-FOR-PRESUMPTION-1193:
  Date searched: 2026-10-28
  Original item: PRESUMPTION-1193
  Original statement: "[inferred] The print edition presumes that stripping internal material (Related-records lines, QC notes, sources) keeps the record auditable, while the ACPA pitch centres on an 'auditable record' and a claim-trace view. The same day found the July citation harvest covered 65 of 307 days and High ratings resting on an unheard recording: the stripped apparatus is where those defects show. Is a frozen print of a moving corpus (all 307 days changed since 09-03) a citable edition, and what links a printed claim back to its trace?"

  Claim tested (literature): Versioned publication of living documents (living systematic reviews; software/data version citation with DOIs or commit stamps); provenance retention in derived editions (W3C PROV). Does a commit stamp alone suffice for auditability?

  Reading used for the FOR direction: the item is a concern, so support means literature showing that (a) citable editions of living works need explicit version identity plus a record of what changed, and (b) auditability of a derived document needs a recorded derivation path back to its sources, not just a link between two states. 15a does not judge whether the print build in fact preserves enough.

  Search scope: PRELIMINARY. 2 web searches (standard), 0 fetches. Searched: living systematic review versioning and per-version DOIs; W3C PROV derivation and reproducibility, and commit hashes. Not reached: DataCite/Zenodo concept-DOI documentation; FORCE11 Software Citation Principles (Smith et al. 2016); Elliott et al. on living systematic reviews (PLoS Med 2014/J Clin Epidemiol 2017); the PROV-DM normative text.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-1193
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the print build stripping Related-records lines, QC notes and sources while the ACPA pitch centres on an auditable record. The same-day finding that the July citation harvest covered 65 of 307 days shows the defects sit in the stripped apparatus.
      15a: Searched for supporting literature (preliminary; 2 searches, 0 fetches)
    Current status: SEARCHED-15a — PARTIALLY-SUPPORTED

  Supporting evidence found: Partial. Versioning practice (a) is well attested. Derivation-path provenance (b) has standards-level support. The specific question of whether a commit stamp alone is enough was not addressed by any source found.

  Sources:
    1. CASRAI, "Living and versioned research outputs: dynamic publications and continuous updates" (casrai.org/wp/?p=1300). [snippet only, advocacy/institutional]. The recommended pattern is to mint a DOI for each specific version and a separate "concept" DOI for the evolving whole, with transparent records of what changed and when. Relevance: direct support for (a). A frozen print of a moving corpus is citable when it carries a version-specific identifier, a link to the evolving whole, and a change record.
    2. Cochrane, Living Evidence Network publishing slides (2017 LSRN Lawrence; 2019 LEN), community.cochrane.org; Wikipedia, "Living review" (Living Reviews in Relativity per-version DOIs, e.g. doi:10.12942/lrr-1998-1 vs lrr-2008-5). [snippet only]. Each Cochrane update gets a new citation, a new PubMed entry and a new DOI, linked to the previous version. Living Reviews cites each version separately, with the journal acting as "version control for the state of research". Relevance: empirical precedent for (a). Established living-document venues treat each frozen state as a separately citable, linked edition.
    3. W3C PROV Overview and PROV-DM drafts (w3.org/TR/prov-overview/; dvcs.w3.org PROV-DM revisions); W3C Provenance WG issue-tracker post, Feb 2012; Git2PROV (rrid SCR_002625). [snippet only; Overview is a W3C Note, issue post non-normative]. In its simplest form a derivation only relates two entities. Attaching activity, generation and usage information makes the derivation path explicit and is what "facilitates provenance-based reproducibility". The WG post argues precise derivation is required for that use case. Git history can be exported to PROV. Relevance: theoretical grounding for (b). A bare link between two states (comparable to a commit stamp) is the minimal derivation. Auditability is associated with recording the path (what was used, what activity, what was produced).

  Strength of support: Moderate

  Summary: Living-review venues (Cochrane, Living Reviews) and research-infrastructure guidance (CASRAI) agree on how to cite a frozen state of a moving work. It needs a version-specific identifier, a link to the evolving whole, and a record of what changed. W3C PROV separates a minimal derivation (two entities linked) from a full derivation path (usage, activity, generation), and ties reproducibility to the latter. This supports the item's concern on two counts. A print edition is citable only if version-stamped and linked. And stripping the apparatus that records sources and QC removes the derivation path that auditability depends on. Whether a commit stamp alone suffices was not answered by any source found. The PROV distinction suggests it gives identity but not trace.

  Caveats:
    - Sources are snippets of institutional guidance and slides. No empirical study of auditability loss in derived editions was found.
    - Mapping "commit stamp" onto PROV's minimal derivation is 15a's analogy, not a source claim.
    - A commit stamp plus a public repository may let a reader rebuild the trace. The literature found does not rule this out.
    - DataCite and FORCE11 software-citation guidance were not reached.

  Recommendation: PARTIALLY-SUPPORTED

  NOVELTY-FLAG: none. Established versioning and provenance practice addresses the concern.
