SEARCH-FOR-PRESUMPTION-703:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-703
  Original statement: That a parser bug announces itself by an implausible
    result; "the tell was the 100% miss rate; real defects are sparse"
    generalised in the same summary that records a near-miss it would not have
    caught (a plausible 21-pair difference). Risk: High.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-703
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read the stated heuristic against the one near-miss in the same run
        that it would not have caught.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Kahn, M.G., Callahan, T.J., Barnard, J., Bauck, A.E., Brown, J., Davidson,
       B.N., Estiri, H., Goerg, C., Holve, E., Johnson, S.G., Liaw, S.-T.,
       Hamilton-Lopez, M., Meeker, D., Ong, T.C., Ryan, P., Shang, N., Weiskopf,
       N.G., Weng, C., Zozus, M.N. & Schilling, L., 2016. "A Harmonized Data
       Quality Assessment Terminology and Framework for the Secondary Use of
       Electronic Health Record Data." eGEMs / EGEMS 4(1):1244. PMID 27713905.
       [Full author list from established knowledge; title, year, venue and the
       three-category structure confirmed in search results this session. Paper
       not opened.] — The strongest theoretical grounding for the heuristic.
       Kahn et al. harmonised competing data-quality vocabularies into three
       categories — Conformance ("do data values adhere to specified standards
       and formats?"), Completeness ("is a particular variable present?") and
       Plausibility ("are data values believable?") — and Plausibility is a
       first-class category, not an afterthought. The framework was validated
       against ten published DQ terminologies. So "does this result look
       believable?" is not folk reasoning; it is one third of the field's
       standard assessment structure, and using it as an error signal is
       sanctioned practice.
    2. The same framework, on what plausibility is for. — Kahn's plausibility
       checks are, in the located material, framed around atemporal, temporal
       and cross-variable believability: values outside expected ranges,
       sequences that cannot occur, distributions that cannot arise. A 100%
       miss rate against a known-sparse-defect prior is a clean instance of a
       distributional implausibility check and the framework endorses it. This
       is genuine, direct support for the specific inference the run made.
    3. Meta Engineering, 2022. "Detecting silent errors in the wild: Combining
       two novel approaches to quickly detect silent data corruptions at scale."
       engineering.fb.com, 17 March 2022. [Located and summarised in search
       results; page not opened.] — Supports the heuristic's motivating premise
       and then bounds it. Silent data corruption is defined as data error that
       goes undetected by the larger system, leaving no trace in logs; the
       stated reason detection is hard is that corrupted results can remain
       computationally plausible. Meta's reported answer is not "watch for
       implausible outputs" but two structural methods — opportunistic/periodic
       testing and in-production ripple testing — with both described as
       equally necessary. That is: the organisation with the largest measured
       exposure to this exact problem does not rely on outcome plausibility,
       because plausibility is the property corrupted results retain.
    4. Silent data corruption literature more broadly — titles located this
       session include "Detection and correction of silent data corruption for
       large-scale high-performance computing" (IEEE Xplore document 6468485;
       authors and year not captured), "The Detection and Correction of Silent
       Errors in Pipelined Krylov Subspace Methods" (arXiv 2409.16796), and
       "LLM-PRISM: Characterizing Silent Data Corruption from Permanent GPU
       Faults in LLM Training" (arXiv 2604.10390). [All located by title only;
       none opened; no figures taken from any of them.] — The consistent framing
       across this literature is that the defining hazard is the *absence* of an
       error signal, and that rarity plus lack of explicit signal is what makes
       these faults hard. The heuristic under test ("the tell was the extreme
       result") is a detector for the loud tail of a distribution whose
       dangerous mass is by definition quiet.
    5. Differential and known-answer testing as parser oracles — located via
       "Validating Network Protocol Parsers with Traceable RFC Document
       Interpretation" (arXiv 2504.18050) and "Parser Knows Best: Testing DBMS
       with Coverage-Guided Grammar-Rule Traversal" (arXiv 2503.03893). [Titles
       and IDs only; not opened.] — Relevant as the named alternative. The
       pattern reported is that a parser bug is found by running two
       implementations over the same input and flagging disagreement — a
       sentinel/oracle method that is independent of whether the output looks
       plausible. This is the control the item's heuristic substitutes for. The
       located material also notes the known cost of that method (standards
       divergence between parsers produces false positives), which is a fair
       point in the heuristic's favour: outcome-plausibility is cheap and
       oracle construction is not.

  Strength of support: Moderate (for plausibility as a legitimate check);
    None (for plausibility as a sufficient one)

  Summary: The heuristic is a recognised and formally catalogued method, not an
    improvisation. Kahn et al.'s harmonised framework makes Plausibility one of
    three top-level data-quality categories alongside Conformance and
    Completeness, and reasoning from "this result cannot be believable given
    what I know about the defect base rate" is a textbook plausibility check
    used exactly as intended. To that extent the run's reasoning is supported.
    What no located source supports is the generalisation — the move from "an
    implausible result revealed this parser bug" to "a parser bug announces
    itself by an implausible result." The silent data corruption literature is
    organised entirely around the opposite proposition: the defining property of
    the dangerous cases is that they produce no signal and remain
    computationally plausible, which is why the practitioners with the largest
    exposure invest in periodic and ripple testing rather than in output
    inspection. The parser-testing literature makes the same point positively by
    reaching for differential and grammar-driven oracles that do not depend on
    result appearance at all. The item's own evidence is the decisive local
    datapoint and it points the same way: a plausible 21-pair difference in the
    same run is precisely the class the heuristic cannot see, and its presence
    in the same summary means the counterexample was in hand at the moment of
    generalisation.

  Caveats: Kahn et al. is medical-informatics data quality, where plausibility
    checks are applied to structured clinical variables with known physiological
    ranges; a "100% miss rate" against a sparse-defect prior is a looser object
    and the transfer is on category rather than on method. Sources 3-5 are a
    mix of an engineering blog post and preprints located by title only, with no
    figures verified; I have deliberately quoted no numbers from them. The
    strongest caveat in the heuristic's favour, which the search did not
    dissolve: plausibility checks are cheap and oracles are expensive, and a
    check that catches the loud failures at near-zero cost is worth having even
    if it catches nothing else. Nothing located argues against keeping the
    heuristic; the sources argue only against treating it as coverage. There is
    also a scope point the search could not settle — the located SDC literature
    concerns hardware-induced corruption, where faults are random, whereas a
    parser bug is deterministic and systematic, and a systematic bug is
    arguably *more* likely to produce a uniform, and therefore conspicuous,
    result than a random one. That is a real argument for the heuristic in this
    specific domain and no source was found that tests it.

  NOVELTY-FLAG: Not raised for the general claim. A narrow gap is noted: no
    located source estimates the detection sensitivity of outcome-plausibility
    checks — that is, what fraction of a realistic parser-defect population
    produces results extreme enough to trip a human's implausibility judgement.
    The literature asserts the fraction is well below one; nothing found
    quantifies it.

  Search scope: Adequate. Concepts searched: silent data corruption detection
    and its characteristic absence of error signals; plausibility as an error
    signal and its formal status in data-quality frameworks; the Kahn et al.
    conformance/completeness/plausibility taxonomy; sentinel, canary,
    known-answer and differential test oracles for parsers; outcome-based versus
    oracle-based bug detection. Not searched: signal detection theory's
    treatment of decision thresholds under low base rates, which would give the
    sensitivity/specificity framing the item's "real defects are sparse" clause
    implicitly invokes; and mutation testing, which would speak to whether a
    checking pipeline can detect its own blindness. Both recommended.

  Recommendation: PARTIALLY-SUPPORTED
