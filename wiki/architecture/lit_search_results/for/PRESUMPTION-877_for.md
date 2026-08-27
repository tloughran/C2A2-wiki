SEARCH-FOR-PRESUMPTION-877:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-877
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 7 of 14 — Priority Critical
  Original statement: [inferred] "That id-resolution *is* citation health — that a reference which
    points at an existing record is thereby a good reference."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-877
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading the nightly verification transcript against the same day's two Summa
        frames — a comparison no run made. Evidence it was operative: the headline "zero dead
        citations ... 979 attributable PRS references ... resolve" was reported as the corpus's
        citation result, while the same day two hand-reading frames found five citation defects
        across five days (Rohr PRS-03 cited for a claim it does not make ×2; Wright PRS-03 listed in
        frontmatter and cited nowhere; an id-less Levin by-theme gesture; Levin PRS-03 carrying a
        half-correct gloss) — **every one of which resolves.** High confidence: the disjointness of
        the two defect classes is demonstrable, not interpretive.
      15a: Searched for supporting literature
    Current status: UNTESTED (entering 15a); 15a result UNSUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch was unavailable to this run (the tool refused
    every URL outside the provenance set), so **all sources below are SNIPPET-ONLY**.
    Queries covered: (a) the citation-accuracy vs. quotation-accuracy distinction and whether either
    has ever been validated against the other; (b) what automated reference/citation checking tools
    detect and what they explicitly cannot; (c) measured proportions of citation defects by class
    (metadata vs. content; major vs. minor; secondary-citation errors); (d) link rot, content drift
    and the known limits of DOI-resolution-based integrity checks; (e) citation-distortion literature
    on defects invisible to any per-reference check.
    Assessment: **good coverage of the FOR question as asked; the answer is negative and I am
    reasonably confident it is negative rather than merely unfound.** The distinction is so
    consistently drawn in the sources that a validation of one as a proxy for the other would be a
    notable and locatable result. Limbs NOT covered: (i) the library/catalogue-quality literature,
    where link-integrity auditing has its own tradition and might treat resolution as a quality
    proxy in a way scholarly-citation research does not; (ii) knowledge-graph and ontology
    quality-assessment frameworks, where "link validity" metrics exist and might be validated against
    semantic correctness — this is the most likely remaining home for supporting evidence and I did
    not reach it; (iii) wiki-specific internal-link-quality research.

  Supporting evidence found: No

  Sources:
    1. "SemanticCite: Citation Verification with AI-Powered Full-Text Analysis and Evidence-Based
       Reasoning." arXiv:2511.16198. [authors unverified]
       https://arxiv.org/pdf/2511.16198 · https://arxiv.org/html/2511.16198v1
       — The single most directly on-point source found, and it is on-point *against* the
       presumption. States the field's position plainly: existing automated verification systems
       validate citations against authority databases (Web of Science, PubMed, CrossRef), detecting
       incorrect metadata or non-existent references, but **cannot verify whether citation claims
       accurately reflect source document content**; "a reference may exist with correct metadata
       whilst the citing author mischaracterises the source's actual findings"; and format-checking
       systems "do not analyse semantic alignment between claims and sources." The paper's entire
       motivation is that resolution-based checking leaves the semantic class unmeasured — i.e. it
       exists because the presumption is false. SNIPPET-ONLY.
    2. "Assessing citation integrity in biomedical publications: corpus annotation and NLP models."
       PMC11231046. [authors, journal and year unverified]
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11231046/
       — Codifies the two-class taxonomy: *citation accuracy* = metadata errors; *quotation accuracy*
       = the reference fails to support the statement it is cited for. Adds that quotation errors
       "are more pernicious in that they are difficult to detect for humans and can distort the
       integrity of scientific evidence." Also notes reference errors of varying degrees run 11–41%
       depending on domain, journal and methodology. SNIPPET-ONLY.
    3. "Accuracy of cited 'facts' in medical research articles: A review of study methodology and
       recalculation of quotation error rate." PLOS One / PMC5599002. [authors unverified]
       https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0184727
       — Supplies the proportion figure the queue asks for. Meta-analysis of 28 studies: overall
       quotation error rate 25.4%, recalculated 14.5% (95% CI 10.5–18.6%). Of *content* errors,
       **64.8% are major** — the reference fails to substantiate, is unrelated to, or contradicts the
       assertion — and 35.2% minor. Improper secondary/indirect citation runs 10.4%. Every one of
       these defect types is invisible to id resolution. SNIPPET-ONLY.
    4. "Quotation errors in general science journals." Proc. R. Soc. A 476(2242), 20200538 (2020).
       [authors unverified] https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0538
       — 25% total error rate; noted as consistent across fields. SNIPPET-ONLY.
    5. "CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References
       in the LLM Era." arXiv:2602.23452. [authors unverified]
       https://arxiv.org/pdf/2602.23452
       — A benchmark built specifically because reference *existence* and reference *support* come
       apart in machine-generated text. The existence of a dedicated benchmark is itself evidence
       that the community treats the two as non-substitutable. SNIPPET-ONLY.
    6. "Detecting Reference Errors in Scientific Literature with Large Language Models."
       arXiv:2411.06101. [authors unverified] https://arxiv.org/pdf/2411.06101
       — Same framing: the detection target is references that do not support their claims, which is
       posed as an open problem distinct from bibliographic validation. SNIPPET-ONLY.
    7. "Reference Rot in the Repository: A Case Study of Electronic Theses and Dissertations (ETDs)
       in an Academic Library." Information Technology and Libraries. [authors and year unverified]
       https://ital.corejournals.org/index.php/ital/article/view/9598
       — The nearest thing to a *quantified* answer to "what proportion of defects are invisible to
       resolution checking" in the link-integrity setting: 77% of links resolved, and roughly **half
       of the resolving links had drifted in content**. Resolution passing while the citation had
       stopped being true. SNIPPET-ONLY.
    8. Greenberg, S. A. (2009). "How citation distortions create unfounded authority: analysis of a
       citation network." BMJ. https://www.semanticscholar.org/paper/d860c6d3e941e1cb28fd9f899035fb926fba7747
       — Names three distortion types — citation bias, amplification, invention — none of which is
       detectable by checking that a reference resolves. Documents a claim whose "is often stated to"
       qualifier was silently dropped in a later review, upgrading a hypothesis to a fact, with the
       reference chain intact throughout. Direct demonstration that a fully-resolving citation network
       can be systematically wrong. SNIPPET-ONLY.
    9. Sarol, M. J. et al. (2025). "Automatic Identification of Citation Distortions in Biomedical
       Literature: A Case Study." Proceedings of the Association for Information Science and
       Technology, 62(1). DOI 10.1002/pra2.1281. https://jodischneider.com/pubs/asist2025.pdf
       — Recent work automating Greenberg-style distortion detection; presupposes that distortion is
       not visible to reference-resolution checks. [co-authors partially verified from the ASIS&T
       listing; first-author surname read from the Wiley entry.] SNIPPET-ONLY.

  Strength of support: None

  Summary: I found no literature supporting the presumption, and the literature I did find contradicts
    it explicitly and repeatedly. The scholarly-citation field draws a standing terminological
    distinction between *citation accuracy* (is the metadata right, does the reference exist and
    resolve) and *quotation accuracy* (does the source actually support the statement it is cited
    for), and treats these as measuring disjoint defect classes — the same disjointness 14b observed
    internally. The verification-tool literature states the limitation as its own motivation: systems
    that validate against CrossRef/PubMed/Web of Science detect non-existent or mis-fielded
    references and "cannot verify whether citation claims accurately reflect source document content"
    (source 1). On the queue's second question — what proportion of defects are invisible to
    resolution-based checking — the best available answer is that the invisible class is the larger
    and more damaging one: quotation error rates of roughly 15–25% across medicine, general science,
    history and education, of which about 65% are *major* (the source fails to substantiate, is
    unrelated to, or contradicts the claim), plus a further ~10% improper secondary citation. The
    citation-distortion literature adds a class invisible to *any* per-reference check: bias,
    amplification and invention operating across a network of perfectly valid citations. And in the
    one link-integrity study that measured both, roughly half of still-resolving links had drifted.

  Caveats: (1) All sources SNIPPET-ONLY; no full text was read. (2) "No support found" is a claim
    about my search, not about the world — see the three uncovered limbs in Search scope, of which
    knowledge-graph quality assessment is the most likely to hold a counter-case. (3) The numbers are
    from human-authored external citation; C2A2's references are internal, machine-generated and
    point into a wiki the same system wrote. The direction of the base-rate difference is genuinely
    unknown — internal references might resolve *and* be accurate more often (shared authorship,
    shallower retrieval chain), or considerably less often (no external check, no cited author to
    object, and the generator can fabricate an internally-plausible gloss). Nothing found addresses
    this. (4) I am reporting an absence honestly: the presumption's *weaker* neighbour — that link
    integrity is a legitimate quality dimension worth reporting *alongside* accuracy — is well
    supported (see ASSUMPTION-1206_for.md). It is only the identity claim, that resolution **is**
    citation health, that finds nothing.

  Recommendation: UNSUPPORTED

  NOVELTY-FLAG:
    Item: PRESUMPTION-877
    Searched: citation-accuracy vs. quotation-accuracy validation; automated citation-verification
      tool capability statements; quotation-error meta-analyses across four fields; link rot and
      content drift; citation-distortion networks. Nine sources located, all SNIPPET-ONLY.
    Finding: **No existing literature treats id resolution as a validated measure of citation
      quality.** The presumption is not merely untested — it is contrary to the field's standing
      distinction, and several recent systems exist precisely because resolution and support come
      apart. In the FOR direction this is a null result, and I record it as such rather than
      stretching the reference-rot literature to cover it.
    What *is* novel and unaddressed: I found no study reporting the ratio of resolution-visible to
      resolution-invisible citation defects **within a single corpus**, and none at all for a
      machine-generated corpus of internal cross-references. C2A2 is unusually well placed to produce
      that number: it has an automated resolution pass over 979 references and a hand-reading frame
      running at roughly one pair per twenty minutes. A stratified hand-audit of a random sample of
      the 979 would yield a corpus-specific invisible-defect rate that, so far as this search found,
      does not exist anywhere in the literature for this class of corpus.
    Implication: potential original contribution — but it requires a *measurement*, not a further
      literature search. Recommended next step is in-house sampling, not re-queueing.
    Recommended status: NOVEL (for the sub-question); UNSUPPORTED (for the presumption as stated).
