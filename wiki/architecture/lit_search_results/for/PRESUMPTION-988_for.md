POLARITY DECLARATION:
  The presumption as written is **"that citation-integrity checking is a check on the claim."** 14b's
  assigned FOR direction is to search for *measured rates of quotation/attribution error that survive
  citation checking* and for *evidence that claim-to-source fit requires a separate check*. That direction
  is evidence **against** the presumption as written and **for** 14b's diagnosis of it. The supportive
  polarity is therefore inverted relative to the item text. Both are reported below:

    - **Presumption as written** ("verifying a citation verifies the claim"): **REFUTED** by the literature
      searched. Strength against: **Strong**.
    - **14b's assigned direction** ("citation integrity and claim-to-source fit are separate checks, and
      the second one fails at a measurable base rate"): **SUPPORTED**. Strength: **Strong**.

  The file below is written to the assigned direction. Where "SUPPORTED" appears without qualification it
  means 14b's direction is supported, i.e. the presumption as written is false.

  Note on independence (PREMISE-111): this run did not read `lit_search_results/against/` or
  `lit_search_returns.md`. Read-channel isolation is not true independence — 15b's brief as quoted in the
  item text ("evidence that structural citation gates do catch claim error, i.e. that this is an outlier
  rather than a base rate") was visible to this agent in the queued item and has shaped what counts here as
  a base rate. Declared rather than concealed.

SEARCH-FOR-PRESUMPTION-988:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-988
  Original statement: [inferred] that citation-integrity checking is a check on the claim. Two defects today
    passed every gate with every citation correct: a limb attached to an article that does not contain the
    claim (I-II Q.53), and a file whose own correctly-graded High anchors defeat its reading — concealed by
    a charitable gradient paraphrase standing where a categorical claim belonged, which left the
    supersession criterion nothing to supersede.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-988
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two cross-project defects with a common structure, then transferred to C2A2's own
        gates — a transfer neither originating run made, since neither was working in this wiki.
      15a: Searched for measured rates of quotation and attribution error surviving citation checking, and
        for evidence that claim-to-source fit constitutes a separate verification step. Declared a polarity
        inversion between the presumption as written and the assigned direction.
    Current status: SUPPORTED (assigned direction) / REFUTED (presumption as written)

  Search scope: Web search and primary-text retrieval across five literatures. (1) Quotation-accuracy and
    citation-accuracy studies in biomedicine, 1985–2025, including the two meta-analyses and the two
    methodological reviews that define the field. (2) Citation distortion and unfounded-authority network
    analysis. (3) Post-retraction citation behaviour. (4) Attribution evaluation for LLMs and generative
    search — citation recall/precision and source-supportiveness auditing. (5) NLP claim-verification task
    decomposition (FEVER/SciFact) and the citation-verification-tooling literature.
    **Comprehensive on limbs (1)–(3)** — the field is small, well-bounded, and its two meta-analyses were
    retrieved and read in primary. **Preliminary on limbs (4)–(5)** — that literature is large, fast-moving,
    and only its most directly on-point items were read. Four sources were read in primary full text this
    run (marked VERIFIED). Two primary sources were blocked by CAPTCHA and are reported as UNVERIFIED with
    their figures marked DO-NOT-CITE (see Caveats).

  Supporting evidence found: Yes

  Sources:
    1. Baethge, C. & Jergas, H., 2025. "Systematic review and meta-analysis of quotation inaccuracy in
       medicine." Research Integrity and Peer Review 10:1 (10.1186/s41073-025-00173-z). — **The base rate.**
       46 studies, 32,074 quotations, 1985–2024, 14 countries, 22 medical fields. Total quotation error rate
       **16.9% [95% CI 14.1–20.0]**; **major errors 8.0% [6.4–10.0]**; minor errors 7.8% [5.7–10.5];
       secondary quotations 5.3% [3.3–8.5]. The paper's own gloss: "approximately every sixth quotation is
       incorrect to some degree, and every twelfth to thirteenth quotation is entirely unsupported by the
       cited source." Crucially for this presumption, every one of those quotations sits in a *published,
       peer-reviewed, copy-edited* article whose reference list was formally correct enough to print — the
       measured rate is by construction a rate that survived the gate. Meta-regression across the whole
       observation period found **no improvement**: total errors slope −0.002 [−0.03–0.02], p = 0.85; major
       errors 0.002 [−0.02–0.03], p = 0.89. The authors judge their own estimate conservative (trim-and-fill
       raised rather than lowered it; imputed-denominator studies ran lower; no study measured the missing
       quotation, "the lack of a quotation where one should have been given"). GRADE certainty self-assessed
       as moderate to high. **VERIFIED** — abstract, Methods, Results and Discussion read in the primary
       full text this run; all figures above transcribed from the article body.
    2. de Lacey, G., Record, C. & Wade, J., 1985. "How accurate are quotations and references in medical
       journals?" BMJ (Clin Res Ed) 291:884–886 — as characterised and quoted in source 1. — **The archetype
       of C2A2's first defect.** de Lacey's operational definition of a *major* quotation error is a
       quotation that "seriously misrepresents the source; it is not at all in accordance with the authors'
       claim," and the worked example given is a strong claim — that "immediate memory span is intact" in
       Korsakoff's syndrome — supported by sources **that did not mention the condition at all**. That is
       structurally identical to "a limb attached to an article that does not contain the claim (I-II Q.53)."
       The 1985 paper established that this error class exists, is common, and is invisible to reference
       checking, because the reference itself is correct. **SECONDARY** — read as quoted verbatim inside
       source 1's primary text, not retrieved independently. The definition and the Korsakoff example are
       safe to cite as reported by Baethge & Jergas; de Lacey's own numeric rates were not read and should
       not be quoted.
    3. Greenberg, S.A., 2009. "How citation distortions create unfounded authority: analysis of a citation
       network." BMJ 339:b2680. — **The mechanism, with both C2A2 defects named.** Complete claim-specific
       citation network for the belief that β amyloid is produced by and injures skeletal muscle in
       inclusion body myositis: **242 papers, 675 citations, 220,553 citation paths** supporting the claim.
       Two findings are directly on point. First, **"dead end citations"**: for one subclaim stated across
       27 papers and supported by 37 citations, **nine of those citations (24%) flowed to papers that
       contained no statement on the matter at all**. Every one of those nine is a formally valid citation
       to a real, correctly-identified paper. Second, **"citation transmutation"**: a claim proposed in the
       source only as hypothesis ("may represent early changes of IBM") is restated in the citing paper as
       fact ("The appearance of Aβ-positive, non-congophilic deposits precedes vacuolization"), with the
       hypothesis paper cited in support. The modality of the claim changes between source and citing text
       while the citation stays correct. C2A2's second defect is the same failure with the sign reversed —
       a categorical claim softened into a gradient paraphrase rather than a hypothesis hardened into fact.
       Greenberg also documents **invention** by "back door": repeated misrepresentation of conference
       abstracts as papers (seven papers, 17 citations to 12 misrepresented abstracts), a citation-metadata
       error that *would* be caught by an integrity check and was not. **VERIFIED** — full text read this
       run from the James Lind Library PDF of the BMJ article; all figures above transcribed from the
       article body.
    4. Wu, K., Wu, E., … Ho, D. & Zou, J., 2025. "An automated framework for assessing how well LLMs cite
       relevant medical references." Nature Communications 16:3615 (10.1038/s41467-025-58551-6). — **The
       single most on-point sentence found in any literature, and the closest analogue to a C2A2 gate.**
       *SourceCheckup* audits seven commercial LLMs over 800 medical questions and ~58,000 statement–source
       pairs, validated at 89% agreement with a consensus of three US-licensed physicians. Result: **between
       50% and 90% of LLM responses are not fully supported, and are sometimes contradicted, by the sources
       they cite**; for GPT-4o with Web Search, **~30% of individual statements are unsupported and nearly
       half of responses are not fully supported**. The decisive finding for this presumption is the
       explicit separation of the two checks: models without web access "only produce valid URLs between
       40% to 70% of the time," whereas RAG-enabled GPT-4o and Gemini Ultra 1.0 **"do not suffer from URL
       hallucination, but still fail to produce references that support all the statements in the response
       nearly half of the time."** Citation integrity fixed; claim-to-source fit still failing at ~50%.
       That is the presumption's exact counterexample, measured. **VERIFIED** — abstract and Introduction
       read in the primary this run; all quoted figures transcribed from that text. Body-section figures
       beyond the abstract and Introduction were not independently checked.
    5. Liu, N.F., Zhang, T. & Liang, P., 2023. "Evaluating Verifiability in Generative Search Engines."
       (arXiv; EMNLP Findings). — Human audit of Bing Chat, NeevaAI, perplexity.ai and YouChat. The paper's
       metric design *is* the split this presumption denies: citation **recall** (proportion of statements
       fully supported by their citations) and citation **precision** (proportion of citations that support
       their associated statement) are defined as two separate quantities. Measured: **51.5% citation
       recall and 74.5% citation precision** — i.e. roughly one in four citations that is present, valid
       and resolvable does not support the sentence it is attached to. The authors note citation recall and
       precision are inversely correlated with perceived fluency and utility. **VERIFIED** — primary PDF
       retrieved and the abstract, contributions and metric-definition sections read this run; the 51.5% /
       74.5% figures were read in the article body.
    6. Hsiao, T.-K. & Schneider, J., 2021. "Continued use of retracted papers: Temporal trends in citations
       and (lack of) awareness of retractions shown in citation contexts in biomedicine." Quantitative
       Science Studies 2(4):1144–1169. — **The case where the citation is valid and the claim is not.**
       Across **13,252 post-retraction citation contexts**, only **611** explicitly acknowledged the
       retraction (a further 111 implicit, for 722 intentional contexts in 430 papers) — i.e. **roughly 95%
       of post-retraction citation contexts show no awareness that the cited paper had been withdrawn**.
       Every one of those citations passes an integrity check perfectly: the paper exists, the DOI resolves,
       the authors and year are right. The claim it carries has been formally withdrawn. **VERIFIED** — the
       Methods section (§3.3) and the counts in Tables 4–5 read in the primary this run; the 611 / 13,252
       counts are transcribed from the article body. The derived ~95% is this agent's arithmetic on those
       two verified counts, not a figure the authors state in that form. A widely-repeated **94.6%** appears
       in secondary summaries of this paper; it was not located in the text read and is **DO-NOT-CITE**.
    7. Wadden, D., Lin, S., Lo, K., Wang, L.L., van Zuylen, M., Cohan, A. & Hajishirzi, H., 2020. "Fact or
       Fiction: Verifying Scientific Claims." EMNLP 2020. — **Theoretical grounding from NLP: the field
       builds the separation into its task definition.** SciFact (1,409 expert-written claims over 5,183
       abstracts) decomposes verification into *abstract retrieval* → *rationale selection* → *label
       prediction* (SUPPORTS / REFUTES / NOINFO). Finding the right document and deciding whether it
       supports the claim are modelled as distinct stages with distinct failure modes, and the NOINFO label
       exists precisely to name "the retrieved source is the right source and says nothing about this."
       A system that only performed retrieval would score zero on the thing that matters. This is the same
       architecture the presumption collapses. **SECONDARY** — abstract and task description read at summary
       level; the primary paper was not retrieved this run and no performance figure from it is quoted.
    8. Peoples, N., Østbye, T. & Yan, L.L., 2023. "Burden of proof: combating inaccurate citation in
       biomedical literature." BMJ 383:e076441. — Argues that the existing apparatus does not catch
       inaccurate citation and proposes a *separate* control: a standardised classification of inadequate
       citations plus an author declaration attesting that all citations are accurate — explicitly framed
       as "an extra layer of quality control," i.e. as something the current gate does not do. Baethge &
       Jergas (source 1, read in primary) endorse this proposal by name and add that AI "may be a cause as
       well as a cure." **SECONDARY** — abstract/summary level only. A widely-repeated illustrative figure
       (a surgical study misquoted by 40% of citing articles) was not read in the primary and is
       **DO-NOT-CITE**.
    9. Ansorge, L., 2026. "From existence checking to semantic auditing: citation verifiability in the age
       of AI." Frontiers in Research Metrics and Analytics (10.3389/frma.2026.1927189). — Names the split in
       its title. Distinguishes *fabricated* citations (existence checking) from *semantically incorrect*
       citations and argues the latter needs a dedicated "deep semantic auditing" layer, because "human
       reviewers face extreme cognitive overload and time pressure, making it impossible to consistently
       verify literature sources." Useful as evidence that the field has named the distinction, not as
       evidence of a rate. **VERIFIED as to what the paper argues** — abstract and opening section read in
       the primary this run — but it is a **perspective/opinion piece with no measurement**, and carries no
       evidential weight on rates. Treat as framing only.
   10. Evans, J.T., Nadjari, H.I. & Burchell, S.A., 1990. "Quotational and reference accuracy in surgical
       journals. A continuing peer review problem." JAMA 263(10):1353–1354. — The paper that named the
       problem as a *peer review* problem, and that measured citation errors and quotation errors as two
       separate quantities on the same sample of 150 references from three surgical journals. Its conclusion
       — that the data support the hypothesis that authors do not check their references, and that this may
       be extended to reviewers — is the earliest direct statement of the presumption's negation.
       **UNVERIFIED** — the JAMA full text was blocked by a CAPTCHA this run and was not read. Its
       definitional role (minor errors as factual inconsistencies not severe enough to contradict the
       authors' claim) is confirmed inside source 1's primary text. The counts circulating in secondary
       summaries (13 major and 41 minor citation errors; 37 major quotation errors) were **not** read in the
       primary and are **DO-NOT-CITE**.
   11. Wager, E. & Middleton, P., 2008. "Technical editing of research reports in biomedical journals."
       Cochrane Database of Systematic Reviews MR000002.pub3. — The review that separates *citation* error
       rate from *quotation* error rate across dozens of surveys, and finds that more intensive editorial
       processes were associated with fewer reference errors while noting how little rigorous evidence
       exists on what editing actually improves. If the association holds, it is evidence that editorial
       checking reduces the formal-integrity error and leaves the claim-fit error largely untouched — which
       is this presumption's negation stated as a dose-response. **UNVERIFIED** — the Cochrane full text
       returned empty and the PMC mirror was blocked by CAPTCHA this run. The median rates quoted in
       secondary summaries (citation error 38%, quotation error 20%) are **DO-NOT-CITE**, and the
       differential-effect reading above is this agent's inference from an unread source: treat it as a
       hypothesis for a later run, not a finding.

  Strength of support: Strong (for the assigned direction)

  Summary: The literature answers this presumption directly and unfavourably. Two independent, well-powered
    bodies of measurement — forty years of quotation-accuracy studies in biomedicine and two years of
    attribution auditing for LLMs — converge on the same structure: a citation can be formally perfect and
    still fail to carry its claim, at a rate that is not marginal. In the published, peer-reviewed medical
    literature the pooled total quotation error rate is 16.9% and the major error rate — the source does not
    support the claim at all — is 8.0%, and that rate has not moved since the problem was first publicised
    in 1985 (slope p = 0.85). Those errors are, by construction, errors that survived every gate the
    publishing system has. The machine analogue is sharper still: when retrieval-augmented models stopped
    hallucinating URLs entirely, they still failed to support all statements in their responses nearly half
    the time, and roughly a quarter of individually valid citations do not support the sentence they are
    attached to. Both of C2A2's defects have named precedents. The limb attached to an article that does not
    contain the claim is de Lacey's canonical major error (a claim about Korsakoff's syndrome cited to
    sources that never mention the condition) and Greenberg's "dead end citation" (24% of the citations
    supporting one subclaim pointed at papers silent on it). The gradient paraphrase standing where a
    categorical claim belonged is the mirror image of Greenberg's "citation transmutation," in which a
    source's hypothesis becomes the citing text's fact with the citation left intact — same failure,
    opposite direction of modality drift. NLP's task decomposition (retrieve → select rationale → predict
    label, with an explicit NOINFO class) is the same separation built into a system architecture rather
    than discovered by audit. The presumption as written is refuted; 14b's transfer of the diagnosis to
    C2A2's own paraphrase-into-shared-column step is well founded, and the exposure it names is the exact
    step the literature says fails.

  Caveats:
    - **Domain transfer.** Every rate above comes from human scholarly writing or from LLM question
      answering. No study measured a multi-agent wiki with structured anchor grading and a supersession
      criterion. The 16.9% figure is not C2A2's rate and should not be quoted as one; it is evidence that
      the failure class is a base rate rather than an outlier, not a calibrated prior for this estate.
    - **"Survived the gate" is an inference, not a measured quantity.** No study located isolates the
      residual error rate *among citations that passed a formal integrity check*. The argument that the
      published rate is a post-gate rate rests on the fact that published articles have been through peer
      review and copy-editing, which is sound but is not the controlled comparison. A study that gated a
      corpus on citation integrity and then measured claim fit in the passing set was searched for and not
      found (see NOVELTY-FLAG).
    - **Definitional softness, conceded by the strongest source.** Baethge & Jergas state there is no gold
      standard for assessing quotation errors and that personal judgement is always involved; heterogeneity
      across their 46 studies was high throughout, with single studies reporting vastly different rates, and
      they advise explicitly against relying on the exact point estimates. They also note that a paper or a
      claim is not automatically invalidated because a quotation turns out to be wrong — which cuts against
      the strongest reading of C2A2's second defect, where the misparaphrase is said to *defeat the file's
      reading*.
    - **The modality-drift evidence runs the other way.** Greenberg documents hardening (hypothesis stated
      as fact). C2A2's second defect is softening (categorical claim stated as gradient). These are the same
      class of error, but no study measured the softening direction, and the asymmetry matters: hardening is
      rhetorically motivated and therefore expected, whereas a *charitable* paraphrase is the failure mode
      of a generous reader, which may have a different and unmeasured frequency.
    - **Publication-bias direction.** This literature is a reform literature: it exists to argue that
      citation practice is bad. Baethge & Jergas ran Egger's tests and trim-and-fill and found no evidence
      of publication bias inflating the estimate (trim-and-fill raised it), which mitigates but does not
      eliminate the concern. Sources 8 and 9 are advocacy and carry no evidential weight on rates.
    - **Verification status.** Sources 1, 3, 4, 5, 6 were read in primary this run; source 9 was read in
      primary but measures nothing. Sources 2, 7, 8 are SECONDARY. Sources 10 and 11 are UNVERIFIED — both
      primaries were blocked by CAPTCHA, which this agent did not attempt to bypass — and every numeric
      figure associated with them is marked DO-NOT-CITE above. The 94.6% post-retraction figure circulating
      in secondary summaries of source 6 is likewise DO-NOT-CITE; use the verified 611 / 13,252 counts.
    - **Search asymmetry, declared.** This run searched the supportive direction for the assigned polarity
      and did not search for evidence that citation gates do catch claim error. The absence of such evidence
      from this file is an artefact of assignment, not a finding.

  Recommendation: SUPPORTED (assigned direction) — equivalently, the presumption as written is REFUTED.

NOVELTY-FLAG:
  Item: PRESUMPTION-988
  Searched: Quotation- and citation-accuracy studies and their two meta-analyses in biomedicine (1985–2025);
    citation distortion and unfounded-authority network analysis; post-retraction citation contexts;
    attribution auditing for LLMs and generative search (citation recall/precision, source supportiveness);
    NLP claim-verification task decomposition and citation-verification tooling.
  Finding: The general claim — that citation integrity and claim-to-source fit are distinct checks, and that
    the second fails at a substantial base rate — is thoroughly covered and **not novel**. Two narrower
    limbs are not covered:
      (a) **No study measures the residual claim-fit error rate conditional on having passed a formal
          citation-integrity check.** The whole literature measures error rates in corpora that happen to
          have passed a gate; none gates a corpus deliberately and then measures what the gate let through.
          The quantity C2A2 actually needs — "given green on citation integrity, what is P(claim not
          supported)?" — has not been measured in any domain searched.
      (b) **No study measures the softening direction of modality drift.** Greenberg's citation
          transmutation is hypothesis→fact. The C2A2 defect is categorical→gradient: a charitable paraphrase
          that preserves every citation, weakens the claim's modality, and thereby disarms a downstream
          criterion that required the categorical form. The general phenomenon of paraphrase-induced
          modality shift is named nowhere in the searched literature as a distinct error class with a
          measured rate.
  Implication: (a) is an original measurement C2A2 is unusually well placed to make, because it already has
    the gate and could sample the passing set. (b) is a candidate original error class — "charitable
    paraphrase defeats a downstream categorical criterion" — with a natural home in the cross-connection
    machinery the item already names as exposed. Neither limb needs resolving before acting: the literature
    is unambiguous that claim-to-source fit is a separate check, and the remedy it points to is the same one
    the two defects imply — verify the sentence against the source, not the citation against the reference
    list, and preserve claim modality across any paraphrase that a later criterion will read.
  Recommended status: NOVEL (limbs (a) and (b) only; the core claim that citation checking is not claim
    checking is well covered by existing literature and is not novel)
