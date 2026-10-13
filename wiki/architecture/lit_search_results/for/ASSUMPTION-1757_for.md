SEARCH-FOR-ASSUMPTION-1757:
  Date searched: 2026-10-10
  Original item: ASSUMPTION-1757
  Original statement: 15c counted 15a/15b agreement on sources fetched from a shared cache as one reading, not two.
    Question: Is discounting correlated evidence to a single reading the right correction when two "independent"
    reviewers share retrieval? (Evidence dependence; double counting in evidence synthesis; correlated-source corrections.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1757
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 15c's stated practice of collapsing 15a/15b agreement over a shared fetch cache into a single
        reading; queued 2026-10-09
      15a (2026-10-10): 3 web searches, 1 fetch (succeeded, abstract). Found strong theoretical and methodological support
        for DISCOUNTING correlated evidence: Clemen & Winkler dependent-expert results, Clemen 1987 on overlapping
        information, and Cochrane unit-of-analysis / double-counting rules. Collapsing to exactly ONE reading is supported
        only as the limiting case where the shared component is total.
    Current status: SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) double counting / non-independent evidence in evidence synthesis;
    (b) Cochrane Handbook unit-of-analysis errors and shared groups; (c) Clemen & Winkler dependent experts / equivalent
    number of independent experts. 1 fetch: IDEAS/RePEc record for Clemen 1987 (succeeded; abstract only). No full texts
    read. Tradition wikis not searched this run.

  Supporting evidence found: Yes (Moderate)

  Sources:
    1. Clemen, R.T., 1987. "Combining Overlapping Information." Management Science 33(3):373–380.
       DOI 10.1287/mnsc.33.3.373. [fetched, abstract] Studies how a decision maker should aggregate expert opinions
       "when he believes that the experts' opinions are dependent due to shared information". The abstract reports
       "surprising general insights regarding the impact of the dependence on the posterior". Relevance: shared retrieval
       is the "shared information" case, so this is direct theoretical grounding for discounting.
    2. Clemen, R.T. & Winkler, R.L., 1985. "Limits for the precision and value of information from dependent sources."
       Operations Research 33. [search-result] Morrison & Schmittlein, 1991. "How Many Forecasters Do You Really Have?
       Mahalanobis Provides the Intuition for the Surprising Clemen and Winkler Result." Operations Research
       39(3):519–523. [search-result] An additional correlated expert usually adds very little information. The
       standard exchangeable-correlation reading gives an effective N = N/(1+(N−1)ρ), which approaches 1 as ρ → 1. This
       formula is a standard textbook reading surfaced by the search summary. It is NOT verified as a quotation from the
       1985 paper. Relevance: "one reading" is exactly the ρ = 1 limit.
    3. Cochrane Handbook, Ch. 23 (multiple intervention groups; unit-of-analysis errors) and Ch. 16 (v5.1).
       [search-result] Entering several comparisons that share a group "double counts" participants. The result is
       spuriously narrow CIs, small P values and over-weighting. The remedies are to combine, split the shared group, or
       model the dependence. Relevance: empirical and methodological precedent that shared inputs must not be counted
       twice. The "split the shared group" remedy is a direct analogue of collapsing shared-cache sources.
    4. Double counting with routinely collected data (Int. J. Technol. Assess. Health Care, PP254 abstract; and PMC9733214).
       [search-result] Double counting of participants artificially inflates precision. Common mitigations: use the
       single most comprehensive source plus sensitivity analysis. Relevance: "keep one" is a recognised practitioner
       remedy.
    5. 2025 Synthese paper on testimony and non-independence (Springer s11229-025-04969-w; title not captured).
       [search-result] Two witnesses who both heard the same radio forecast is the canonical "double counting the common
       forecast" problem. The paper notes that the same issue applies to repeat readings of a measuring device. Relevance:
       philosophical grounding; the shared cache plays the role of the radio forecast. Author/title unverified.
    6. Evidence-Based Subjective Logic (arXiv 1402.3319). [search-result] Defines double counting as present whenever
       the evidence underlying two combined items is dependent. Relevance: formal definition that covers shared retrieval.

  Strength of support: Moderate. The principle (discount correlated evidence) is strongly grounded, but the sources
    reached are abstract or search-result level. The specific magnitude ("one, not two") is supported only for the
    shared-data component.

  Summary: Decision analysis (Clemen 1987; Clemen & Winkler 1985), meta-analysis methodology (Cochrane
    unit-of-analysis rules) and epistemology of testimony converge: evidence that shares a common source must not be
    counted as independent, or confidence is inflated. When the shared component is total (identical fetched documents),
    the effective number of readings tends to one, so 15c's collapse is the principled limit. Where reviewers apply
    genuinely independent interpretation to the shared documents, the literature implies a partial discount rather than a
    full collapse.

  Transfer caveats: (i) 15a and 15b search in opposite directions and may interpret the same document differently.
    Agreement on interpretation carries some independent information even if retrieval is shared (ρ < 1), so a strict
    "one reading" may over-correct. (ii) The literature handles dependence quantitatively (correlation, multilevel
    models); C2A2 has no estimate of ρ. (iii) No full texts were read; the effective-N formula is a standard reading,
    not a verified quote.

  NOVELTY flag: no. Correlated-source discounting is well established. Its application to paired AI reviewers sharing
    a fetch cache is a straightforward transfer.

  Recommendation: SUPPORTED (Moderate). Preliminary search; broader search recommended (full text of Clemen & Winkler
    1985; Cochrane Ch. 23 §23.3).
