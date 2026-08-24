SEARCH-FOR-PRESUMPTION-841:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-841
  Original statement: That a null result and an unattempted check are distinguishable downstream. Four
    runs wrote the distinction by hand in prose; no register field carries it.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that the
  distinction between "checked, found nothing" and "not checked" is (a) recognised as consequential and
  (b) conventionally carried by an explicit schema field or reporting item rather than left to prose.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-841
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by collecting the day's hand-written null qualifiers and noting each was written in
        prose because no schema field exists for it.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "PRISMA-S: an extension to the PRISMA Statement for Reporting Literature Searches in Systematic
       Reviews." *Systematic Reviews* (2021), doi:10.1186/s13643-020-01542-z; also published in *Journal
       of the Medical Library Association*. (author list not verified — Rethlefsen et al. commonly cited,
       not confirmed from the pages consulted) — A 16-item checklist developed by 3-stage Delphi plus
       consensus conference, whose stated intent is that "each component of a search is completely
       reported and therefore reproducible," covering database and platform, the full search strategy,
       limits applied, and the date of each search. This is the closest thing in the literature to the
       missing register field: an established standard requiring that what was searched be recorded as
       structured metadata, so that a reader can tell a covered-and-empty result from an uncovered one.
       NOTE: the pages I consulted do NOT state that PRISMA-S explicitly separates "searched, found
       nothing" from "not searched"; the support is that the standard exists and is built for exactly
       this reproducibility purpose. Do not overstate this citation.
    2. "Quality control, data cleaning, imputation." arXiv:2110.15877. (author list not verified) —
       States the distinction directly for data records: measurements that *cannot or should not* be taken
       (e.g. tumour characteristics for healthy patients) should not be coded as missing, "because it
       fails to recognize that no information is actually missing," and must be separated from the case
       where a variable could have been measured but was not recorded. This is a near-exact statement of
       PRESUMPTION-841's distinction, and it is stated as a data-quality requirement, not an option.
    3. Missing-data mechanism literature (MCAR / MAR / MNAR), consulted via Columbia Mailman School
       "Missing Data and Multiple Imputation" and standard teaching sources. [established-work] —
       Establishes that the *mechanism* of missingness determines whether downstream inference is valid at
       all, and that the mechanism generally cannot be recovered from the data alone; it must be recorded
       or assumed. Supports the item's core claim that if the register does not carry the distinction,
       downstream consumers cannot reconstruct it.
    4. Data-quality practice on missing-value indicators (e.g. the "Missing values" indicator
       documentation at dataquality.qihs.uni-greifswald.de). [methodological guidance] — Codifies
       separate codes for distinct reasons for absence, rather than a single null. Corroborates that the
       remedy 14b implies (a schema field) is the conventional one.

  Strength of support: Strong

  Summary: Both limbs of 14b's diagnosis are well supported. First, the distinction between a measured
  null and an unattempted measurement is treated in the data-quality literature as a requirement, not a
  refinement: arXiv:2110.15877 states that conflating the two misrepresents whether any information is
  missing at all, and the MCAR/MAR/MNAR framework establishes that the mechanism of absence governs
  whether downstream inference is valid — and that the mechanism cannot generally be recovered post hoc.
  Second, the conventional remedy is structural: distinct missing-value codes in data quality practice,
  and, in the systematic-review setting closest to this pipeline's actual work, the PRISMA-S checklist,
  which requires searches to be reported in enough structured detail to be reproduced. That four runs
  wrote the qualifier in prose is consistent with the literature's observation that where no field exists,
  the information either goes into free text or is lost.

  Caveats: I did NOT verify that PRISMA-S contains an item explicitly distinguishing "searched and found
  nothing" from "not searched"; the citation supports the general principle (structured search reporting
  for reproducibility), and 14b/15c should not read more into it than that. The MCAR/MAR/MNAR framework
  concerns statistical estimation from samples and transfers to an operational register only by analogy —
  no source studies agent-run registers. The file-drawer / null-result-reporting limb of the search angle
  was not searched directly; it is a distinct literature (publication bias) and may or may not support the
  same conclusion. Search scope: moderate — covered missing-data mechanisms, data-quality missing-value
  coding, and PRISMA-S; publication bias and negative-results reporting NOT covered.

  Recommendation: SUPPORTED
