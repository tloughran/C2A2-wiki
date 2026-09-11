SEARCH-FOR-ASSUMPTION-1311:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1311
  Original statement: "*Two verification failures recorded rather than glossed:* the AJR mammography
    quote load-bearing for PREMISE-201 clause (3) failed retrieval and is flagged unverified; and **the
    Zimmermann ICSE'12 paper does not publish the reopen rate its search summary implied** — 15b caught
    that by reading it, and the 'mid-teens to low twenties' estimate in REVISE-445 inherits the weakness
    and is labelled a prompt to measure, not a finding."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1311
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim. First time a minted premise (PREMISE-201) carries a clause resting on an
        unverified quotation, and first time a lit-search summary has been caught misreporting its own
        source by reading the source. Both are credits to the run. Recorded against it: PREMISE-201 was
        minted anyway and REVISE-445 still stands on the weakened number. See PRESUMPTION-954.
      15a: Searched for supporting literature on the general limb; found a large, quantified, and
        strikingly convergent literature. The two instances are already settled in-house.
    Current status: SUPPORTED

  Register pre-check: This item is close to fully pre-answered by ACTIVE premises — the most clearly
    pre-answered of the ten.
    - PREMISE-132: "CITING IS NOT VERIFYING... in generated text the measured rate of full support
      between a sentence and its own citation is roughly half, so a register in which 'all items do cite
      external referents' is not thereby evidenced."
    - PREMISE-148: quotation error rates are measured and not small; object-level content carries the
      higher measured error rate of the two things this system could audit.
    - PREMISE-178: "AN EXISTENCE CHECK AND A LABEL CHECK DO NOT ESTABLISH THAT A CITED SOURCE SUPPORTS
      THE SENTENCE IT ANCHORS... Reading the body is the only operation that decides it." This is
      precisely the operation 15b performed on Zimmermann and it is already an ACTIVE premise.
    - PREMISE-203: the verification discipline attaches to the assertion, not to the artefact class.
    - PREMISE-188: an evidentiary qualifier travels with the claim or it does not travel — which governs
      the REVISE-445 residual directly and says the caveat will be stripped.
    Searched anyway per OPEN-192.

  Supporting evidence found: Yes

  Sources:
    1. Jergas H. & Baethge C. 2015. "Quotation accuracy in medical journal articles — a systematic review
       and meta-analysis." PeerJ 3:e1364. — VERIFIED (full text fetched and read) — 28 studies, 7,321
       references. Major quotation errors 11.9% [95% CI 8.4-16.6]; minor 11.5% [8.3-15.7]; total 25.4%
       [19.5-32.4]. Heterogeneity high (I² 95-97%) but the LOWEST single-study total error rate across
       all 28 studies was 6.7%. Meta-regression found no improvement over time (slope 0.0050, p=0.817).
       A major error is defined as one where the cited source "contradicted, failed to substantiate, or
       was irrelevant to the author's assertion" — which is exactly the Zimmermann failure mode.
    2. Jergas & Baethge 2015, discussion section. — VERIFIED (same fetch) — Cites Simkin & Roychowdhury's
       misprint-propagation estimate that roughly 70-90% of citations in physics are copied from other
       papers' reference lists without the original being read. Reported here as the authors report it;
       I have not retrieved Simkin & Roychowdhury and it is therefore SECONDARY within a VERIFIED source.
    3. Wager E. & Middleton P. 2008 (review of quotation accuracy studies to mid-2007). — SECONDARY
       (reported inside the Jergas & Baethge full text I fetched) — Median quotation error rate 20%.
       Independent of the meta-analysis and concordant with it.
    4. Walters W.H. & Wilder E.I. 2023. "Fabrication and errors in the bibliographic citations generated
       by ChatGPT." Scientific Reports. — SECONDARY (figures from multiple retrieved descriptions; paper
       not fetched) — 18% of GPT-4-generated citations entirely fabricated across 42 multidisciplinary
       topics. The canonical figure in this literature.
    5. Chelli M. et al. 2024. "Hallucination Rates and Reference Accuracy of ChatGPT and Bard for
       Systematic Reviews." J Med Internet Res. — SECONDARY (not fetched) — GPT-4 hallucination rate
       28.6% in a systematic-review citation task.
    6. 2026 mental-health literature-review audit (reported via EurekAlert and Newswise press releases).
       — SECONDARY, PRESS-RELEASE-LEVEL ONLY — 19.9% of GPT-4o citations across six simulated literature
       reviews entirely fabricated; 29% for an unfamiliar topic (body dysmorphic disorder) vs 6% for a
       familiar one (major depressive disorder); among seemingly real citations, 45.4% carried
       bibliographic errors. The topic-familiarity gradient is the most operationally useful finding
       located and I flag that I read it in press coverage, not the paper.

  Strength of support: Strong

  Summary: The general limb — that search summaries do not reliably carry their sources' claims
    faithfully — is supported about as well as a claim of this kind can be, from two independent
    literatures that converge. In human-authored medical writing, a fetched meta-analysis of 28 studies
    puts total quotation error at 25.4% and major error (source contradicts, fails to substantiate, or is
    irrelevant to the assertion) at 11.9%, with no improvement over three decades and a floor of 6.7%
    even in the best study. In LLM-generated citation work, outright fabrication runs 18-29% and
    bibliographic error among non-fabricated citations runs near half. The Zimmermann instance is a
    textbook major quotation error and the AJR instance is a retrieval failure; both fall inside
    well-characterised base rates rather than being anomalies. The practical consequence is the one 14a
    already recorded: a lit-search summary's fidelity must be established by reading the source, not
    inferred from the citation's presence — which is PREMISE-178 verbatim.

  Caveats:
    - The medical quotation-error literature measures human authors writing papers; the LLM literature
      measures citation *generation*, not summary *fidelity* to a source the model actually retrieved.
      This pipeline does the latter, and neither literature measures it directly. The base rates bracket
      the question rather than answering it.
    - Jergas & Baethge's own warning applies and should be carried: heterogeneity was I²=95-97% and the
      authors state the estimates "have to be viewed with extreme caution and to be taken as what they
      are: weighted averages from a heterogeneous field, calculated in order to describe the average
      magnitude of the effect, not to put a final number to a phenomenon." Quoting 25.4% without that
      sentence would repeat the very error this item is about.
    - The 70-90% copied-citation figure is a model-based estimate from misprint propagation in physics,
      not a direct measurement, and its transfer to any other field is untested. It should not be quoted
      as a rate.
    - The 2026 mental-health figures come from press releases; I did not retrieve the paper. They should
      not carry weight until the paper is read.
    - The residual obligation is not a search question and is not discharged here: PREMISE-201 was minted
      with a known-unverified load-bearing clause, and PREMISE-188 predicts the "mid-teens to low
      twenties" caveat in REVISE-445 will be stripped in transit. Both are engineering, not research.

  Search scope: comprehensive search — quotation accuracy and citation-content error rates in biomedical
    and cross-disciplinary literature (Jergas & Baethge; Wager & Middleton; ecology/marine biology/
    geography replications), LLM citation hallucination and fabrication rates (Walters & Wilder; Chelli
    et al.; 2026 mental-health audit; reference-hallucination detection work), citation-integrity NLP
    corpora.

  Recommendation: SUPPORTED — the recommendation rests on the general limb (summaries do not reliably
    carry source claims; measured base rates are high in both human and machine authorship). The two
    named instances were already settled in-house. Note that PREMISE-132, PREMISE-148 and PREMISE-178
    jointly pre-answer this item; the new content this search adds is the specific, fetched, quantified
    base rate (11.9% major / 25.4% total, with no secular improvement) rather than a new proposition.
