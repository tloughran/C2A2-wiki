SEARCH-FOR-ASSUMPTION-1213:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1213
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 3 of 14 — Priority Medium
  Original statement: "the citation repairs cost +196 and +216 words, pushing both files past +25% on
    anchoring alone with no new argument added."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1213
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa commentary reviewer (Days 24 and 20) and corroborated against the
        QC sweep's Day 130 escalation ("This is the second time today the clause has fired on
        repair-driven growth, and the tier is not wrong"). Two independent frames, same night, same
        conclusion — recorded as convergence, not as a single report. Status CHALLENGED (of the length
        clause, on internal evidence): the ratio measures words, and words now grow chiefly from
        anchoring; the clause presumes length tracks argument size, three same-day counter-instances
        say it tracks citation density instead. No literature consulted at extraction time.
      15a: Searched for supporting literature
    Current status: CHALLENGED (entering 15a); 15a result SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch unavailable to this run; **all sources
    SNIPPET-ONLY.**
    Queries covered: (a) document length as a proxy for argument quality/size in academic writing;
    (b) journal word-limit policy — specifically whether reference and citation apparatus is counted;
    (c) longitudinal growth in references per paper vs. growth in paper length; (d) Goodhart's law and
    proxy-metric failure, using lines-of-code as the canonical worked case.
    Assessment: **adequate but oblique.** The item's own domain — length control over *structured
    agent-generated commentary* — has, so far as I found, no literature at all. Everything below is
    transferred from scholarly publishing or software metrics. Limbs NOT covered: (i) automatic
    summarisation and text-generation evaluation, where length-normalised metrics and length bias in
    LLM judges are actively studied and would be the nearest technical literature — this is the
    largest uncovered gap and I would prioritise it in any follow-up; (ii) technical-writing and
    documentation-quality research on information density; (iii) legal drafting, where citation
    apparatus is voluminous and page limits are litigated, and where courts have explicit rules on
    whether citations count toward limits.

  Supporting evidence found: Yes

  Sources:
    1. AIP Publishing, Author Instructions. https://publishing.aip.org/resources/researchers/author-instructions/
       — Primary-document evidence for the central supporting point: AIP excludes abstract, title,
       author list, **references** and acknowledgments from the word limit, while *including* figures,
       tables and equations via a space-equivalent calculation. The apparatus is deliberately
       partitioned from the text the limit is meant to govern. SNIPPET-ONLY.
    2. Springer, *Health and Technology*, submission guidelines.
       https://www.springer.com/journal/12553/submission-guidelines
       — Same pattern: abstract, tables, figure legends and references excluded from the 5,000-word
       (review) and 3,500-word (original) limits. SNIPPET-ONLY.
    3. Elsevier, *iLIVER*, Guide for Authors.
       https://www.sciencedirect.com/journal/iliver/publish/guide-for-authors
       — 5,000-word text limit excluding abstract, references, tables and figures. SNIPPET-ONLY.
    4. "Manuscript Word Count Limits & How to Shorten a Submission." CASRAI guide.
       https://casrai.org/guides/manuscript-word-count-limits-how-to-shorten-a-submission
       — Cross-publisher synthesis: "references are almost universally excluded from the main-text
       word count, though many journals cap the *number* of references instead." This is the
       strongest single supporting statement found. It establishes not only that the field separates
       apparatus from argument, but that where apparatus *is* controlled it is controlled by a
       **separate instrument on a different unit** (reference count, not words) — which is precisely
       the remedy 14a's two frames are groping toward. It also records the counter-cases honestly
       (e.g. *Gastroenterology* counts references and legends inside the limit). Practitioner guide,
       not peer-reviewed. SNIPPET-ONLY.
    5. "What all is included in the manuscript word count?" Editage Insights.
       https://www.editage.com/insights/what-all-is-included-in-the-manuscript-word-count
       — Corroborating practitioner statement: "most journals apply the word limit to the main text
       only and exclude the abstract, references, tables and figure legends." Low evidential weight;
       included for corroboration only. SNIPPET-ONLY.
    6. "Growth in the number of references in engineering journal papers during the 1972–2013 period."
       arXiv:1306.4223. [authors unverified] https://arxiv.org/pdf/1306.4223
       — Longitudinal evidence bearing on the mechanism: references per paper have grown ~60% over
       20 years; normalised pages per paper grew ~55% (6.6 → 10.2); and **references per normalised
       page stayed roughly constant** — the absolute number of references grew, not their density.
       Supports the general claim that reference apparatus and text length move together, so a rule
       that measures words is partly measuring apparatus. Note this source is more equivocal than the
       others: constant density over decades is not the same as the *acute* density shift 14a
       observed. Reported honestly. SNIPPET-ONLY.
    7. "Accumulation of Knowledge in Para-Scientific Areas. The Case of Analytic Philosophy."
       arXiv:1802.05941. [authors unverified] https://arxiv.org/pdf/1802.05941
       — Five-fold growth in references per paper in analytic philosophy, 8.8 (1950s) → 44.1 (2000s).
       Included because analytic philosophy is a commentary-style humanities corpus, structurally the
       closest published analogue to C2A2's synthesis files. SNIPPET-ONLY.
    8. "The disruption index suffers from citation inflation and is confounded by shifts in scholarly
       citation practice." arXiv:2406.15311. [authors unverified] https://arxiv.org/pdf/2406.15311
       — Direct methodological analogue to 14a's complaint: a well-established metric is shown to be
       confounded because the underlying citation practice drifted while the metric's definition did
       not. A metric that was valid when apparatus was thin becomes invalid as apparatus thickens.
       This is the closest thing found to a *theoretical grounding* for the length-clause challenge.
       SNIPPET-ONLY.
    9. Fox, C. W., et al. (2016). "Citations increase with manuscript length, author number, and
       references cited in ecology journals." *Ecology and Evolution*. DOI 10.1002/ece3.2505.
       https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.2505
       — Reported against interest. Finds longer papers, with more authors and more references, are
       more cited, and that within journals longer papers are also more positively reviewed. This is
       the main *counter*-consideration to 14a's assumption and is included per the no-cherry-picking
       rule; it supports a rival reading in which length does carry signal. Note however that it
       measures citation *impact*, not argument size, and its own explanation — longer papers contain
       more ideas and more results — concerns content, not apparatus. SNIPPET-ONLY.
   10. "Over-optimization of academic publishing metrics: observing Goodhart's Law in action."
       *GigaScience* 8(6), giz053 (2019). [authors unverified]
       https://academic.oup.com/gigascience/article/8/6/giz053/5506490
       — Theoretical grounding, in the item's own domain: proxy metrics in scholarly publishing
       degrade once they become targets. SNIPPET-ONLY.
   11. Wayne, H. "Goodhart's Law in Software Engineering." Buttondown.
       https://buttondown.com/hillelwayne/archive/goodharts-law-in-software-engineering/
       and "The Measurement Problem in Software Engineering."
       https://maestroai.substack.com/p/the-measurement-problem-in-software
       — The lines-of-code case as the canonical worked example of a size proxy that fails when the
       cheap-to-produce component (boilerplate) grows independently of the valuable component. The
       structural parallel to citation anchoring is exact: 40 idiomatic lines vs. 400 lines of
       redundant boilerplate is +196 words of anchoring vs. +196 words of argument. Practitioner
       sources, not peer-reviewed. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: The assumption's core — that word count is a poor proxy for argument size when growth comes
    from citation apparatus — is supported most directly by an institutional fact rather than a study:
    scholarly publishing has *already solved this problem the way 14a's frames are proposing*.
    References are near-universally excluded from journal word limits, and where the apparatus is
    controlled at all it is controlled by a separate instrument on a different unit — a cap on the
    number of references, not on their word cost (sources 1–5). That convention is a standing,
    field-wide admission that citation apparatus and argument are not commensurable and should not
    share a budget. Theoretical grounding comes from the Goodhart literature, including a case study
    within scholarly publishing itself (10) and the canonical lines-of-code failure in software
    metrics (11), where a size proxy breaks precisely because a cheap-to-produce component can grow
    independently of the valuable one. The disruption-index critique (8) supplies the sharpest
    analogue: a metric confounded because citation practice drifted while the metric's definition did
    not — which is 14a's diagnosis of the length clause, stated about a different metric. Longitudinal
    data confirm apparatus does grow substantially over time (6, 7).

  Caveats: (1) All SNIPPET-ONLY; sources 4, 5 and 11 are practitioner writing, not peer-reviewed.
    (2) **The exclusion convention is narrower than the assumption needs.** Journals exclude the
    *reference list* — a discrete end-matter block. 14a's +196 and +216 words are *in-text anchoring*:
    id citations, source lines and glosses woven into the prose. I found no policy or study that
    treats in-text citation apparatus as excludable, and separating it from argument is genuinely
    harder because anchoring prose is not mechanically detachable. This is the most important
    limitation of the support offered. (3) Source 9 points the other way and is not dismissible:
    within journals, longer papers are both better reviewed and more cited. (4) Source 6 is weaker
    than it first appears — constant references-per-page across four decades is compatible with the
    length clause being fine on average and wrong only in the acute repair case, which is in fact
    exactly what 14a observed (three counter-instances, not a trend). (5) No source addresses
    structured, agent-generated commentary under an automated length-ratio rule; the entire evidence
    base is transferred. (6) The assumption is partly a *measurement claim* about two specific files
    (+196, +216 words, past +25%); no literature can confirm or deny it, and it should be verified
    in-house by diffing the repaired against the pre-repair files.

  Recommendation: SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1213
    Supported sub-claims: (i) that citation apparatus and argument are not commensurable and are
      conventionally budgeted separately — established practice across major publishers; (ii) that
      where apparatus is limited it is limited by count, not by word cost; (iii) that a size proxy
      fails when a cheap-to-produce component grows independently of the valuable one (Goodhart;
      lines of code); (iv) that metrics defined against one citation practice become confounded when
      practice shifts.
    Unaddressed sub-claims: **(a) in-text citation anchoring** — every located exclusion policy
      concerns the detachable reference list, not anchoring woven into prose, and I found no treatment
      of how to length-control text where the apparatus is inline; **(b) length control over
      agent-generated structured commentary**, where the growth is driven by an automated repair loop
      rather than by an author's choices. The second is a genuinely new configuration: the system that
      enforces the length rule and the system that causes the overrun are the same system, which no
      publishing convention has to contend with.
    Implication: the design remedy the literature endorses — budget apparatus separately, cap it by
      count — appears to be directly transferable and is not currently in use here. That is a
      recommendation the literature supports; per remit I record it as a finding, not a proposal.
