SYSTEMIC-RISK-FLAG — 2026-09-11

  Date: 2026-09-11
  Raised by: Agent 15b (literature search, AGAINST direction)

  Affected items: ASSUMPTION-1308, ASSUMPTION-1310, ASSUMPTION-1311
    (and, by inheritance, every premise minted from prior 15a/15b cycles)

  Common vulnerability:
    **This pipeline's agents can almost always retrieve a confident quantitative SUMMARY of a source and
    frequently cannot retrieve the SOURCE. The two are not distinguished by the pipeline's output format
    at the point where a premise is minted, so the cheapest path and the correct path diverge
    systematically — and the divergence is invisible downstream.**

    This is not an inference. It is what happened to me today, in this batch, on the items where the
    numbers mattered most:

      - **Schwenk, C.R. (1990), OBHDP 47(1), 161-176** — the one meta-analysis of devil's advocacy and
        dialectical inquiry, explicitly named in the 15b charter for ASSUMPTION-1310. Bibliographic
        record VERIFIED at RePEc/IDEAS. **RePEc records "No abstract is available for this item."
        ScienceDirect full text is paywalled.** I could not read a single number from it. The finding I
        report for it ("DA more effective than the expert approach in general; DI's superiority not
        demonstrated on ill-structured tasks") comes from a search-engine summary and is SECONDARY. No
        effect size was obtainable.
      - **Schulz-Hardt, Jochims & Frey (2002), OBHDP 88(2), 563-586** — the key replication. Paywalled.
        Abstract only. Cell means unobtainable, so I cannot say whether devil's advocacy beat the
        no-dissent control or merely lost to heterogeneity.
      - **Hróbjartsson et al. (2012), BMJ 344:e1119** — the source of the "36% exaggeration" and the
        pooled ROR 0.76 (0.61–0.94) that carry ASSUMPTION-1308's whole challenge. **The PubMed record
        served a reCAPTCHA challenge, which I did not attempt to bypass.** BMJ full text not retrieved.
        Both figures are SECONDARY.
      - **"Inducing Disagreement in Multi-Agent LLM Executive Teams: Only the Devil's Advocate Works"
        (OpenReview mxBmj5LYU2)** — the single most directly on-point source for ASSUMPTION-1310. **The
        PDF endpoint returned empty and the forum page served a browser-verification challenge.** The
        circulating figures (99.2% vs 48.3% disagreement; 4.9% "persuasion override"; 9.2% "hidden
        agreement") are UNVERIFIED and I have excluded them from my rating.
      - **monitoring-plugins.org developer guidelines** (canonical four-state return-code standard,
        ASSUMPTION-1314) — outside my fetch provenance set; documented from four secondary sources
        instead.

    Five load-bearing retrievals attempted, five blocked, across three distinct mechanisms: paywall,
    bot-detection challenge, and tool provenance restriction. In every case a fluent, specific,
    quantitative summary was freely available and the primary text was not.

  Literature basis:
    - Liu, N.F., Zhang, T. & Liang, P. (2023). "Evaluating Verifiability in Generative Search Engines."
      *Findings of EMNLP 2023*. — **VERIFIED (PDF retrieved from cs.stanford.edu and figures read
      directly)** — citation recall **51.5%**, citation precision **74.5%**. Roughly one citation in four
      does not support the sentence it is attached to. This is the measured error rate of exactly the
      layer this pipeline is forced to rely on when the source is unreachable.
    - PREMISE-132 (ACTIVE) — CITING IS NOT VERIFYING; measured full-support rate in generated text is
      roughly half.
    - PREMISE-148 (ACTIVE) — object-level content carries the higher measured error rate of the two
      things this system could audit.
    - PREMISE-103 (ACTIVE) — absence of primary text is a KIND-difference in evidence, not a degree
      difference; no confidence label over metadata-only material is well-founded, and downgrading
      confidence is not a valid substitute for an explicit "unfounded pending retrieval" state.
    - PREMISE-188 (ACTIVE) — an evidentiary qualifier travels with the claim or it does not travel; the
      stripping of hedges on re-quotation is systematic, not careless.
    - ASSUMPTION-1311 itself — the estate has already caught one search summary attributing a figure to a
      paper that does not publish it (Zimmermann ICSE'12). That was one instance. The retrieval-failure
      rate measured here says the opportunity for that error arises on most load-bearing sources.

  Why this compounds with the other flag:
    The propagation flag (see `SYSTEMIC-RISK-FLAG_2026-09-11_premise-propagation-not-routing_...`) says
    ACTIVE premises do not reach the runs they govern. This flag says the premises themselves may rest on
    unread sources. Together they describe a register whose contents are (a) not reaching the decisions
    they should govern, and (b) not traceable to sources anyone has read. PREMISE-103's remedy — an
    explicit "unfounded pending retrieval" state — exists precisely for this and is not being applied:
    PREMISE-201 was minted with a known-unverified load-bearing clause rather than held.

  Risk level: **High**

    Not Critical only because the remedy is cheap, local, and already specified by ACTIVE premises. It
    becomes Critical if a pre-route grep (ASSUMPTION-1309) is adopted as a filter, because premises
    resting on unread sources would then be permanently shielded from re-examination.

  Recommendation:
    1. **Make the verification grade a required field on every load-bearing quantity, stored with the
       number.** VERIFIED (retrieved and read) / SECONDARY (reported in a source I did retrieve) /
       UNVERIFIED (could not retrieve). These eleven files do this; `validated_premises.md` does not.
       Per PREMISE-188 the grade must sit beside the figure, not in a document header, or it will be
       stripped on first quotation.
    2. **Audit the existing register for grade.** For each of the 158 ACTIVE premises, record whether any
       agent ever read the primary source for its load-bearing quantities. This is a one-pass
       retrospective and it is what PREMISE-118 requires when an instrument is found out of tolerance.
    3. **Apply PREMISE-103 rather than minting with a caveat.** A premise whose load-bearing clause rests
       on an unretrievable source goes to `UNFOUNDED-PENDING-RETRIEVAL`, not to ACTIVE-with-a-note.
       PREMISE-201 clause (3) is the live instance and should be the first correction.
    4. **Obtain institutional access, or record its absence as a standing constraint.** Four of the five
       blocked retrievals above would have succeeded with a university library proxy. If the estate is
       going to run a literature pipeline against paywalled social-science and medical journals, the
       access gap is a structural property of the instrument and belongs in the register, not in
       individual search-scope notes.
    5. **Never bypass a bot-detection challenge to obtain a source.** Two of the five blocks were
       CAPTCHAs. The correct response is to report the block, which I have done in each file. A pipeline
       that resolves retrieval failures by defeating access controls would be trading an epistemic
       problem for a conduct one.
    6. **Seed and count.** PREMISE-162 names the only way to get a denominator for a self-audited
       detector: insert 5 synthetic claims attributing plausible fabricated findings to real papers, and
       count how many reach a minted premise. Run it separately against 15a and 15b — the difference is
       also a reading on ASSUMPTION-1310.
