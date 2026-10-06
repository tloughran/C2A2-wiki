POLARITY DECLARATION:
  The presumption as written is: *recording a correction is sufficient for it to reach the files that
  carry the corrected claim.* The direction 14b assigned to 15a — "retraction/erratum propagation rates in
  citing works; correction half-life; mechanisms that succeed" — is **not** the supportive direction for
  that sentence. That literature exists almost entirely as measurement of **failure** to propagate; it is
  the canonical disconfirming corpus. Searching it as instructed therefore produces evidence *against* the
  presumption, not for it.

  This file reports **both limbs**, labelled, and does not blend them:
    LIMB A — the claim as written ("recording suffices"). Searched independently for support. Result:
      **NO-SUPPORT-FOUND** for the claim as stated; **PARTIALLY-SUPPORTED** for a materially weaker
      restatement (recording a correction at the source reduces *future* uptake by *new* consumers).
    LIMB B — 14b's assigned direction (propagation rates, half-life, which mechanisms work). Result:
      **SUPPORTED, Strong** — with the sharp qualification that the best-powered test of the mechanism
      14b would presumably favour (active notification at the citing record) is itself null.

  15a's formal Recommendation field below reports LIMB A, because that is the item filed. LIMB B is
  reported in full and is the part of this file with the most decision-relevant content.

SEARCH-FOR-PRESUMPTION-989:
  Date searched: 2026-09-14
  Original item: PRESUMPTION-989
  Original statement: [inferred] that recording a correction is sufficient for it to reach the files that
    carry the corrected claim. Third consecutive day: the connexin result's consumer set is 30, not 24;
    zero carry a hedge; three were rewritten today without gaining one; a separate known violation was
    "rewritten *through*" by a pass that added ~1,300 words. A second project's agent independently asked
    for "a scheduled cross-tradition pass, not a local edit."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-989
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three days of the same shape, escalating, across two projects and four runs.
        Pre-check recorded as "read at source": premise register searched for `correction`, `retraction`,
        `propagat`, `blast radius`, `erratum`; no covering premise; OPEN-201 is the estate's own open
        question and is not a premise.
      15a: Declared the polarity inversion in 14b's assignment; then searched (a) for literature
        supporting the claim as written, and (b) the assigned direction — post-retraction citation rates,
        persistence over time, and comparative evidence on correction mechanisms (flagging at the source
        record vs. active notification at the citing record vs. tooling at the point of re-use), plus the
        nearest engineering analogue (dependency-graph advisories and automated fix PRs).
    Current status: NO-SUPPORT-FOUND (claim as written); the assigned direction is SUPPORTED (Strong)

  Search scope: Five literatures. (1) Post-retraction citation in biomedicine and scientometrics —
    Budd/Sievert/Schultz; Hsiao & Schneider; Schneider et al.; van der Vet & Nijveen; Furman/Jensen/Murray;
    2025 anaesthesia-journal audit. (2) Mechanism trials — RetractoBot RCT; Avenell et al. randomised alert
    trial. (3) Infrastructure-level flagging — database indexation of retracted literature; Retraction
    Watch → Crossref acquisition; Zotero retraction notifications. (4) Cognitive/communication literature
    on corrections — continued-influence meta-analysis; journalism corrections. (5) Software
    dependency-graph blast radius — Dependabot security PR adoption and merge rates.
    **Comprehensive on limbs (1) and (2)** — those two randomised trials are the field's only direct tests
    of "does issuing the correction reach the dependents," and both were located and read.
    **Preliminary on (3), (4) and (5)** — sampled, not swept; a fuller sweep of the software-supply-chain
    literature (npm audit adoption, CVE advisory lag, SBOM/VEX propagation) is recommended and was not run.
    Two primary full texts were blocked this session (PMC reCAPTCHA; publisher paywall) and are marked.

  Supporting evidence found: No (claim as written) / Yes, strong (assigned direction)

  Sources:

  — LIMB A: does recording a correction reach the artefacts that carry the claim? —

    1. **Furman, J.L., Jensen, K. & Murray, F., 2012.** "Governing knowledge in the scientific community:
       Exploring the role of retractions in biomedicine." *Research Policy* 41(2): 276–290. — **The
       strongest genuine FOR evidence located, and it supports a weaker proposition than the one filed.**
       Across the universe of biomedical retractions 1972–2006 against a matched control sample, retraction
       does measurably suppress onward citation: retracted articles fall to a minority share of their
       controls' citations within a year and decline further thereafter. The paper also reports the
       retraction system as reasonably fast (mean time to retraction under two years) and not
       systematically distorted by author prominence. **Crucially, this is a flow measure over *new*
       citers, not a stock measure over *existing* citing documents.** It says a correction reduces future
       uptake; it says nothing about repairing the documents already carrying the claim — which is
       precisely PRESUMPTION-989's object. **SECONDARY** (abstract/summary level). The specific 45%→20%
       figures circulating in summaries are **DO-NOT-CITE as verified**.
    2. **Zotero / Retraction Watch integration (2019– ), and Crossref's 2023 acquisition of the Retraction
       Watch Database.** — Documented *practice*, not measured outcome. Zotero flags retracted items in the
       library, warns at cite-time in the word-processor plugin, and — the one feature that matches this
       presumption's shape exactly — warns the author again on next citation-refresh if an item was
       retracted *after* it was already cited in a draft. This is the only widely deployed mechanism that
       pushes a correction at the artefact already carrying the claim. **UNVERIFIED as to effect**: no
       study measuring its effect on citation rates was found. The RetractoBot authors themselves name it
       only as a speculative explanation for their own null (see source 5).
    3. **NO-SUPPORT-FOUND, stated plainly.** No study in any of the five literatures searched reports that
       recording a correction *in one location* reliably reaches the artefacts that carry the corrected
       claim. Every measurement located points the other way, and the two randomised mechanism trials are
       null or negative.

  — LIMB B: propagation rates, persistence, and which mechanisms succeed —

    4. **van der Vet, P.E. & Nijveen, H., 2016.** "Propagation of errors in citation networks: a study
       involving the entire citation network of a widely cited paper published in, and later retracted
       from, the journal *Nature*." *Research Integrity and Peer Review* 1:3. — **VERIFIED — full text read
       directly.** The closest structural analogue to the estate's situation: one retracted result, its
       complete consumer set reconstructed, each consumer's text inspected. Of the 37 papers in the 2014
       network directly citing the retracted Narayan paper, **with two exceptions (both from the later 2015
       network) none of the directly citing papers shows any awareness of the retraction**, "yet most
       papers of the 2015 network have been published well after the retraction was published." Directly
       citing articles "just repeat the (retracted) result." The authors also report that the retraction
       was absent from Scopus two weeks after issue; that Google Scholar did not mark the retracted paper
       more than a year later and did not surface the retraction on the first page of results; and that
       adding a publication year to a search "is almost always sufficient to hide the retraction." Their
       own remedy is the citing-record mechanism: "Authors of a paper published previously should be warned
       when one of their citations gets retracted... At the very least, they may want to flag the offending
       citation as being retracted." Indirect (second-hop) citations, by contrast, showed **zero**
       propagation of the retracted result — the blast radius was one hop deep, not unbounded.
    5. **DeVito, N.J., Cunningham, C. & Goldacre, B., 2025.** "Notifying Authors That They Have Cited a
       Retracted Article and Future Citations of Retracted Articles: The RetractoBot Randomized Controlled
       Trial." Abstract, 10th International Congress on Peer Review and Scientific Publication (JAMA
       Network). — **VERIFIED — full abstract including all figures read directly at the Congress record.**
       **The single most decision-relevant source in this file, and it is a null.** 7,958 retracted
       articles randomised to intervention, 7,963 to control; **246,749 deliverable notification emails**
       sent to citing authors, 8 Jan – 7 Feb 2024; follow-up to 7 May 2025. After outlier removal, 7,939
       citations in intervention vs 7,943 in control. **Effect not significant: mean citation rate −0.007,
       95% CI −0.055 to 0.041**, holding across all prespecified sensitivity analyses. Of 15,667 survey
       responses, **80.6% (12,631) of notified authors said they were unaware of *all* the retracted
       citations they were being told about** — i.e. the correction had demonstrably not reached them by
       any prior channel, the notification did reach them, and citation behaviour still did not change at
       one year. Caveat as to status: conference abstract, not yet a full peer-reviewed paper; the authors
       plan secondary analyses at longer follow-up.
    6. **Avenell, A., Bolland, M.J., Gamble, G.D. & Grey, A., 2022/2024.** "A randomized trial alerting
       authors, with or without coauthors or editors, that research they cited in systematic reviews and
       guidelines has been retracted." *Accountability in Research* 31(1): 14–37. — Randomised alerting of
       authors of systematic reviews and guidelines that cited 27 retracted trials, varying whether
       coauthors and editors were also alerted. Reported conclusion: email alerts to authors and editors
       are **inadequate** to correct the impact of retracted publications in citing systematic reviews and
       guidelines. **SECONDARY** — publisher full text was paywalled this session. The widely quoted "89%
       of reviews not corrected one year after notification" figure is **DO-NOT-CITE as verified**.
    7. **Hsiao, T.-K. & Schneider, J., 2021.** "Continued use of retracted papers: Temporal trends in
       citations and (lack of) awareness of retractions shown in citation contexts in biomedicine."
       *Quantitative Science Studies* 2(4): 1144–1169. — 7,813 retracted PubMed papers, ~169,000 citations,
       ~48,000 citation contexts inspected. Of 13,252 post-retraction citation contexts, **722 (5.4%)
       acknowledged the retraction**; the rest cite the paper as though valid. The authors' own summary
       finding is the load-bearing one here: *retraction did not change the way the retracted papers were
       cited.* **SECONDARY** — the primary was unreachable this session (both the MIT Press and PMC copies
       were blocked by a session-level fetch cache and by reCAPTCHA respectively). The 5.4% figure is
       consistent across two independent search summaries and the publisher abstract but was **not read in
       the primary**; treat as SECONDARY, not DO-NOT-CITE.
    8. **Budd, J.M., Sievert, M.E. & Schultz, T.R., 1998.** "Phenomena of retraction: reasons for
       retraction and citations to the publications." *JAMA* 280(3): 296–297. — The founding measurement.
       235 retracted articles were cited 2,034 times *after* the retraction notice; of 299 of those
       citations examined, only 19 noted the retraction, the other 280 treating the retracted article as
       valid. **SECONDARY.** (Note for the register: 14b's queue entry gives the second author as
       "Sizemore"; the correct name is **Sievert**. Corrected here.)
    9. **Schneider, J., Ye, D., Hill, A.M. & Whitehorn, A.S., 2020.** "Continued post-retraction citation
       of a fraudulent clinical trial report, 11 years after it was retracted for falsifying data."
       *Scientometrics* 125(3): 2877–2913. — Case study of the Matsuyama et al. (2005) trial: eleven years
       after retraction it continued to be cited positively and uncritically, without mention of the
       retraction, and the claim propagated onward through the citation network. Directly addresses the
       "half-life" limb: the answer in this case is that there is no observable decay to zero. **SECONDARY.**
    10. **"Living Up to the Recommendations on the Citation of Retracted Articles," 2025** (anaesthesia
       journals audit; PubMed 39851161). — 211 publications retracted 1993–2020 across nine anaesthesia
       journals drew 1,307 post-retraction citations; 78% (164/211) received at least one citation more
       than a year after retraction; 80.2% of those citations affirmed the retracted findings.
       **SECONDARY** — PMC full text blocked by reCAPTCHA this session. All three figures are
       **DO-NOT-CITE as verified**.
    11. **Korpela, K.M., 2010.** "How long does it take for the scientific literature to purge itself of
       fraudulent material?: the Breuning case revisited." *Curr Med Res Opin* 26(4): 843–847. — Read via
       van der Vet & Nijveen's discussion, which reports a case with a **24-year** gap between publication
       and retraction, the paper still being cited at that point. On correction half-life: the tail is
       measured in decades. **SECONDARY** (encountered as a citation in a verified source, not read).
    12. **"The indexation of retracted literature in seven principal scholarly databases," *Scientometrics*
       (2024), DOI 10.1007/s11192-024-05034-y.** — Mechanism limb, source-side. Coverage of retracted
       literature diverges sharply across Dimensions, OpenAlex, PubMed, Scilit, Scopus, The Lens and Web of
       Science, with inaccurate labelling of retracted documents identified in several; the authors
       recommend querying more than one source. Establishes that **flagging at the source record is not
       even reliably *present*, let alone sufficient.** **SECONDARY; author list not confirmed in this
       search — cite by DOI/title only.**

  — LIMB B, engineering analogue: does an advisory reach the dependents? —

    13. **Alfadel, M., Costa, D.E., Shihab, E. & Mkhallalati, M., 2021.** "On the Use of Dependabot Security
       Pull Requests." *2021 IEEE/ACM 18th International Conference on Mining Software Repositories (MSR)*.
       — **VERIFIED — preprint full text read directly.** 15,243 Dependabot security pull requests across
       2,904 active JavaScript GitHub projects. **65.42% are merged, often within a day; 34.58% are not
       merged.** This is the strongest *positive* mechanism evidence in the whole file and the clearest
       contrast with the scholarly case. The difference is structural, not cultural: Dependabot does not
       record a notice and hope — it **computes the dependent set from a machine-readable graph, opens a
       concrete diff against each dependent artefact, and presents it at the point of maintenance.** The
       correction arrives as work already done, in the file that carries the claim. Where the correction
       arrives as a notice (RetractoBot: 246,749 emails, null), it does not land.
    14. Related, for the residual-failure rate: the Empirical Software Engineering line on Dependabot
       (Alfadel et al., "Dependabot and security pull requests: large empirical study," *EMSE* 2024; and
       "Securing dependencies: A comprehensive study of Dependabot's impact on vulnerability mitigation,"
       *EMSE* 2025) — even with automated, diff-level, per-dependent delivery, a substantial minority of
       vulnerable dependents remain unfixed while a fix exists. **SECONDARY**; specific percentages from
       these two are **DO-NOT-CITE as verified**.

  — LIMB B, cognitive floor —

    15. **Walter, N. & Tukachinsky, R., 2019.** "A Meta-Analytic Examination of the Continued Influence of
       Misinformation in the Face of Correction: How Powerful Is It, Why Does It Happen, and How to Stop
       It?" *Communication Research*. — **VERIFIED at abstract level — the abstract of the accepted
       manuscript was read directly at the author's institutional repository record.** 32 studies,
       N = 6,527: **correction does not entirely eliminate the effect of misinformation (r = −.05,
       p = .045)**. Moderators are directly applicable: corrections work better when coherent, consistent
       with the recipient's model, and **delivered by the source of the misinformation itself**; they work
       worse when the original was attributed to a credible source, when the original was **repeated
       multiple times before correction**, and when there is a **time lag between the original and the
       correction**. Read against PRESUMPTION-989: a claim restated across 30 files, corrected days later,
       by a different pass than the one that wrote it, sits on the wrong side of all three moderators. This
       is a floor result — even when the correction demonstrably *reaches* the recipient, residual
       influence persists — so it bounds how much any propagation mechanism can be expected to buy.

  Strength of support: **None** for the claim as written. **Strong** for 14b's assigned direction.

  Summary: The claim as written has no support in any literature searched, and the two randomised trials
    that test it most directly are null or negative. Recording a correction at the source measurably
    reduces *future* uptake by *new* consumers (Furman et al.) — that is the only genuine FOR finding, and
    it is a different proposition from the one filed, because it concerns the flow of new citers rather
    than the stock of artefacts already carrying the claim. On the stock, the measurements are consistent
    and old: 5.4% of post-retraction citation contexts acknowledge the retraction (Hsiao & Schneider);
    Budd et al. found 280 of 299 examined post-retraction citations treating the article as valid; and van
    der Vet & Nijveen, who reconstructed an entire consumer set and read every consumer, found that all but
    two of the directly citing papers showed no awareness of the retraction despite most having been
    published well after it. The half-life limb has no tidy answer: persistence is measured in years to
    decades (11 years in the Matsuyama case, 24 in the Breuning case), and the one careful citation-context
    study reports that retraction did not change *how* the paper was cited at all. On the mechanism limb —
    the one 14b actually needs — the finding is sharper than expected and cuts against the obvious remedy.
    Flagging at the source is necessary but demonstrably insufficient and in practice often absent
    (databases disagree about which papers are retracted; search engines fail to mark them). But active
    notification **at the citing record** — the mechanism van der Vet & Nijveen recommended and the one
    the estate would naturally reach for — was tested at scale by RetractoBot with 246,749 emails against a
    randomised control and produced **no significant reduction in citation** (−0.007, 95% CI −0.055 to
    0.041), even though 80.6% of responding authors confirmed they had been unaware of the retraction until
    the email arrived. Notification reached them; behaviour did not move. The only mechanism in this file
    with a strong positive result is the software analogue, and it differs from notification in a specific,
    transferable way: Dependabot computes the dependent set from a machine-readable graph and delivers the
    correction **as a concrete diff against each dependent artefact at the point of maintenance**, achieving
    65.42% merge, often within a day. The distinction the literature actually supports is therefore not
    "flag at the source vs. flag at the citing record" but **notice vs. patch** — and even patch leaves a
    substantial unfixed minority.

  Caveats:
    - **Polarity.** 14b's assigned FOR direction disconfirms the claim as written. The Recommendation field
      reports the claim; anyone reading only that field will get the opposite of LIMB B's content.
    - **The one real FOR finding is a different proposition.** Furman et al. measures new-citer flow, not
      repair of existing citing documents. It should not be quoted in support of "recording suffices."
    - **RetractoBot's status.** Conference abstract (2025), not yet a full paper; secondary analyses at
      longer follow-up are planned and could change the picture. Its null is also an intention-to-treat
      effect on *aggregate citation rate* — it does not establish that no individual author acted.
    - **Domain transfer is real but imperfect.** The scholarly literature's consumers are independent third
      parties with no obligation to the corrector, no write access to each other's files, and a publication
      cycle measured in months. The estate's consumer set is internal, enumerable by grep, and writable by
      the same agent that issued the correction. That asymmetry makes the scholarly failure rates an *upper
      bound on difficulty*, not a prediction — the estate's case is structurally closer to Dependabot's
      (known dependency graph, write access to dependents) than to PubMed's. This cuts *toward* tractability
      and should be stated when this file is reconciled.
    - **Publication-bias direction.** The post-retraction-citation literature exists because non-propagation
      is a problem; successful, silent propagation generates no papers. The corpus is structurally biased
      toward failure. This is a genuine limit on LIMB B's strength and is named here rather than buried.
    - **Verification.** Only sources 4, 5, 13 (full text) and 15 (abstract of the accepted manuscript) were
      read directly. Sources 1, 6, 7, 8, 9, 10, 11, 12 and 14 are SECONDARY at abstract or summary level.
      Figures marked DO-NOT-CITE in the source list must not be quoted as verified. Three primaries were
      blocked this session (PMC reCAPTCHA ×2; Taylor & Francis paywall ×1) and a session-level fetch cache
      prevented retrieval of the Hsiao & Schneider full text.
    - **The software limb is preliminary.** npm audit adoption, CVE advisory lag, and SBOM/VEX propagation
      were not swept. A fuller pass there is the highest-value extension of this search, because it is the
      limb where the estate's structural situation actually lives.

  Recommendation: **NO-SUPPORT-FOUND** (claim as written)
    Subsidiary: PARTIALLY-SUPPORTED for the weaker restatement "recording a correction at the source
    reduces future uptake by new consumers." SUPPORTED (Strong) for 14b's assigned direction.

NOVELTY-FLAG:
  Item: PRESUMPTION-989
  Searched: Post-retraction citation and citation-context analysis (biomedicine, scientometrics); the two
    randomised mechanism trials (RetractoBot; Avenell et al.); database indexation and reference-manager
    flagging; the continued-influence meta-analytic literature; journalism corrections; and Dependabot /
    dependency-advisory adoption studies.
  Finding: The general claim is **not novel** — it is one of the best-measured failure modes in the
    scientometric literature, and 15a recommends the register record it as covered, not open. One narrow
    limb is a genuine gap: **no located study measures correction propagation in a corpus where the
    corrector and the maintainer of every consuming artefact are the same agent, with full write access and
    an enumerable dependency graph.** Every measured case separates them — independent authors (scholarly),
    independent maintainers (Dependabot), independent readers (continued-influence). The estate's case
    collapses that separation, and the literature has no measurement of what happens when it does.
  Implication: The gap is narrow and does not license waiting. Two findings transfer without needing it
    resolved. First, **notice is not the unit that propagates; a diff is** — RetractoBot sent 246,749
    notifications for no measurable effect, while Dependabot's per-artefact pull requests merge at 65.42%,
    often within a day. Second, **the dependent set must be computed, not remembered** — van der Vet &
    Nijveen's consumer set was only knowable because someone reconstructed the entire citation network, and
    the estate's own item records that its consumer set was believed to be 24 and is in fact 30. Both point
    at the same in-house action already named on three consecutive days and still not run: enumerate the
    consumer set by grep, then emit a per-file edit rather than a prose notice. The literature's contribution
    here is to predict that the prose-notice half of that will not work, and to say why.
  Recommended status: NOT-NOVEL (principal claim — well covered, consistently disconfirmed);
    NOVEL (narrow limb only — single-agent corpora with write access to the full dependent set)
