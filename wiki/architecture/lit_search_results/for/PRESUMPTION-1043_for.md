SEARCH-FOR-PRESUMPTION-1043:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1043
  Original statement: A failure taxonomy organised per-component systematically hides causes shared across components, and the independence it implicitly assumes inflates estimates of system reliability.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1043
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (per-component FAIL rows carried as independent; two C2A2 tasks died on one shared 5.9 GB ceiling)
      15a: Searched for supporting literature; found direct support for the reliability-inflation half (NUREG/CR-5485, Ford et al. 2010) and partial support for the taxonomy-hiding half (Gunawi et al. 2016, not fully verified); strength: Strong (inflation) / Moderate (taxonomy)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Mosleh, A., Rasmuson, D. M., Marshall, F. M., 1998. "Guidelines on Modeling Common-Cause Failures in Probabilistic Risk Assessment." NUREG/CR-5485 (US NRC / INEEL). https://nrcoe.inl.gov/publicdocs/CCF/NUREGCR-5485_Guidelines%20on%20Modeling%20Common-Cause%20Failures%20in%20PRA.pdf — Fetched. States that when dependencies are ignored the actual probability of joint failure is higher than that computed under independence; the document supplies the alpha-factor / multiple-Greek-letter quantification (beta-factor lineage). Directly supports the inflation claim. (Author list as returned by fetch tool; the fetched summary rendered one name as "Moslehl", read as Mosleh.)
    2. Ford, D., Labelle, F., Popovici, F., Stokely, M., Truong, V.-A., Barroso, L., Grimes, C., Quinlan, S., 2010. "Availability in Globally Distributed Storage Systems." OSDI '10. https://research.google/pubs/availability-in-globally-distributed-storage-systems/ — Authors/venue verified at the Google Research page; quantitative findings read from the Princeton course copy of the paper (cs.princeton.edu/courses/archive/spring13/cos598C/Ford.pdf). Reports 37% of failures are part of a burst of at least 2 nodes, and that ignoring correlation overestimates availability by at least two orders of magnitude (eight for RS(8,4); Table 3). Strongest empirical analogue in distributed systems. Also notes that faster recovery helps far less under correlated failures.
    3. Gunawi, H. S., Hao, M., Suminto, R. O., Laksono, A., Satria, A. D., Adityatama, J., Eliazar, K. J., 2016. "Why Does the Cloud Stop Computing? Lessons from Hundreds of Service Outages." SoCC 2016. — Bibliographic entry verified via dblp; full text could not be fetched (request rejected), so its findings on multi-service outages from shared dependencies are NOT verified by this search and are not relied on for the rating.
    4. Stott, J. E., Britton, P. T., Ring, R. W., Hark, F., Hatfield, G. S. "Common Cause Failure Modeling: Aerospace vs. Nuclear." NASA NTRS 20100025991. https://ntrs.nasa.gov/api/citations/20100025991/downloads/20100025991.pdf — Fetched. Argues that CCF parameter-estimation choices (staggered vs non-staggered testing) can artificially reduce modelled risk. Supports the point that CCF treatment materially changes reliability estimates outside nuclear (aerospace). Publication year not confirmed (fetch summary said 1998; the NTRS id suggests ~2010).

  Strength of support: Strong for the reliability-inflation half (sources 1, 2); Moderate for the "taxonomy hides shared causes" half (inferred from the CCF literature's need for explicit common-cause groups; no source fetched that tests per-component taxonomies directly).

  Summary: Reliability engineering has long held that treating redundant or co-located components as independent overstates reliability; NUREG/CR-5485 states this plainly and provides parametric CCF models (alpha-factor, MGL) to correct it. Ford et al. quantify the effect in a production distributed system: ignoring correlated failures overstated availability by two to eight orders of magnitude, and correlation also blunts the benefit of faster per-node recovery. Together these directly support the claim that implicit independence inflates reliability estimates. The "hiding" half is supported by implication (CCF methods exist because component-level views do not reveal shared causes), with Gunawi et al. a candidate source on shared-substrate outages that remains to be verified.

  Caveats:
    - The searched literature concerns quantitative reliability estimates for redundant systems. C2A2's per-component FAIL rows are a qualitative taxonomy with no formal probability estimate, so the "inflates estimates" claim transfers by analogy, not directly.
    - Domain transfer: nuclear PRA and Google storage differ from an agent-pipeline estate; the two C2A2 tasks failing on one 5.9 GB ceiling is a single-case instance, not evidence of prevalence.
    - No source was found that directly tests "per-component taxonomy" as the mechanism of hiding; that link is inferential.
    - Gunawi et al. findings unverified (paper not retrievable). Search-engine results gave titles only for several other candidates (PSAM proceedings, arXiv 2206.11321), which were not opened and are not cited.
    - Publication bias: incident and CCF literature over-represents cases where common cause mattered.
    - Search scope: preliminary search (4 web queries, 7 fetches; tradition wikis not consulted); broader search recommended for shared-quota/clock post-incident literature (e.g. published postmortems) and the beta-factor origin (Fleming 1974), neither verified here.

  Recommendation: SUPPORTED

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1043
  Search direction: FOR (supportive)
  Result: SUPPORTED
  Strength: Strong (reliability inflation); Moderate (taxonomy hiding, inferential)
  Key source: Ford et al., 2010, "Availability in Globally Distributed Storage Systems," OSDI '10 (ignoring correlated failures overestimates availability by >= 2 orders of magnitude); Mosleh et al., 1998, NUREG/CR-5485
  Summary: Both CCF methodology and a large Google fleet study confirm that independence assumptions overstate reliability. The link to per-component taxonomies specifically is inferred, not directly tested.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1043_for.md

NOVELTY-FLAG: not warranted (existing literature addresses the claim).

QUEUE SUMMARY: [SEARCHED-15a: 2026-10-05] PRESUMPTION-1043 — SUPPORTED, Strong/Moderate; Ford 2010 + NUREG/CR-5485.
