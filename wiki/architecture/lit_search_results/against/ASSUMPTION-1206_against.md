SEARCH-AGAINST-ASSUMPTION-1206:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1206
  Queue ref: LIT-QUEUE — 2026-08-25 (14a + 14b end-of-day intake cohort), Priority Critical
  Original statement: "Verified 307 synthesis files (Days 001–307, the complete series) against the live
    C2A2 wiki... **zero dead citations**: all 979 attributable PRS references, 9 distinct FLAG ids,
    47 distinct CROSS ids, and every cited tradition-wiki path resolve." — reported as the
    corpus-wide citation-health headline for the first complete pass over the finished series.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1206
    Item type: ASSUMPTION (stated — quoted verbatim)
    Transform at each step:
      14a: Extracted from the Summa 2026 nightly verification (22:00), then checked against the same
           day's Summa commentary reviewer and QC sweep transcripts. CHALLENGED on
           register-vs-register evidence within one day.
      15b: Searched for challenging literature. Six WebSearch queries executed covering citation- and
           quotation-error rates, the limits of automated reference verification, link/reference rot,
           and the citation-error/quotation-error taxonomy.
    Current status: CHALLENGED

  Search scope: Six WebSearch queries, executed 2026-08-26. Coverage reached: the medical and general
    science citation-accuracy literature (multiple systematic reviews and meta-analyses), the
    scientometric literature on reference errors, the 2024–2026 arXiv literature on automated and
    LLM-based citation verification, and the library/web-archiving literature on link and reference
    rot. Date range of sources reached: 1965 (Kaplan, via secondary report) to 2026. All sources were
    read as search-result snippets and titles only — **no full text or abstract was fetched for any
    source in this search**, so every citation below is marked SNIPPET-ONLY and quantitative figures
    are reported as the search engine rendered them, not as verified from the paper. NOT COVERED:
    (a) the humanities and philosophy citation-accuracy literature, which is the closest disciplinary
    analogue to a wiki of contemplative and scientific traditions and which the medical literature
    does not stand in for; (b) any study that measures the *joint* distribution — i.e. of references
    that resolve, what fraction are also semantically accurate — which is the exact quantity this item
    asks about and which I did not find a direct measurement of; (c) the software-engineering
    literature on test-coverage-as-quality-proxy, which would supply the structural analogue
    (a passing test suite is not a correct program); (d) the Karpathy/C2A2 corpus itself, which I did
    not read. The evidence below is therefore strong on the *general* point and indirect on the
    *specific* one.

  Challenging evidence found: Yes

  Sources:
    1. [authors unverified] 2017. "Accuracy of cited 'facts' in medical research articles: A review of
       study methodology and recalculation of quotation error rate." PLOS ONE.
       https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0184727 (also
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5599002/) — Recalculates the quotation error rate
       in the medical literature at 14.5% (95% CI 10.5–18.6%). A quotation error is by definition an
       error in a reference that *exists and resolves*; the reference is present and correct as a
       pointer, and wrong as a warrant. This is the defect class that a resolution check cannot see,
       measured. SNIPPET-ONLY.
    2. [authors unverified] 2025/2026. "Systematic review and meta-analysis of quotation inaccuracy in
       medicine." https://pmc.ncbi.nlm.nih.gov/articles/PMC12285159/ — Pooled 46 studies covering
       ~32,000 quotations; 16.9% of quotations incorrect, roughly half of them major (8.0%). Major
       errors are defined as cases where the cited source "fails to substantiate, is unrelated to, or
       contradicts the assertion." Critically for this item: meta-regression showed **no significant
       improvement in quotation accuracy over time**, i.e. the digitisation and reference-manager era
       that eliminated most *citation* (pointer) errors did not touch *quotation* (warrant) errors.
       That is the sharpest available statement that the two defect classes are independent.
       SNIPPET-ONLY.
    3. [authors unverified] 2020. "Quotation errors in general science journals." Proceedings of the
       Royal Society A 476(2242): 20200538.
       https://royalsocietypublishing.org/rspa/article/476/2242/20200538/80897/Quotation-errors-in-general-science
       — Reported by Times Higher Education as finding that ~25% of sampled references in Science,
       Science Advances, Nature, Nature Communications and PNAS "were deemed not to substantiate the
       points raised by authors."
       https://www.timeshighereducation.com/news/quarter-citations-top-journals-wrong-or-misleading —
       Directly relevant boundary: this is the highest-quality-control corpus in existence, with
       essentially zero dead references, and a quarter of its citations still fail on accuracy. The
       maximal version of ASSUMPTION-1206's check, applied to the world's best-edited corpora, yields
       no information about the quarter that is wrong. SNIPPET-ONLY (figure via THE's report of the
       paper, not read in the paper).
    4. [authors unverified] 2025. "SemanticCite: Citation Verification with AI-Powered Full-Text
       Analysis and Evidence-Based Reasoning." arXiv:2511.16198.
       https://arxiv.org/html/2511.16198v1 — States the architectural point explicitly: existing
       automated verification systems "validate citations against authority databases (Web of
       Science, PubMed, CrossRef), detecting incorrect metadata or non-existent references, but cannot
       verify whether citation claims accurately reflect source document content. A reference may
       exist with correct metadata whilst the citing author mischaracterises the source's actual
       findings." This is the C2A2 nightly check described in the third person. SNIPPET-ONLY.
    5. [authors unverified] 2024. "Detecting Reference Errors in Scientific Literature with Large
       Language Models." arXiv:2411.06101. https://arxiv.org/abs/2411.06101 — Supplies the taxonomy
       that makes the challenge precise: *citation errors* are typographical/bibliographic (wrong
       author, title, year, arrangement) and have "become less common in the era of digitization and
       citation managers"; *quotation errors* are where "a reference fails to support the statement
       for which it is cited" and are "difficult to detect for humans." The class the C2A2 check
       measures is the class that technology already fixed; the class that remains is the one it
       cannot address. SNIPPET-ONLY.
    6. [authors unverified] 2024. "Assessing citation integrity in biomedical publications: corpus
       annotation and NLP models." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11231046/ — Exists as
       a corpus-annotation effort precisely because citation integrity is not readable off reference
       resolution; the need for hand-annotated ground truth is itself evidence that no resolution-based
       proxy was available. SNIPPET-ONLY (title and framing only).
    7. Wakeling, S., et al. [remaining authors unverified] 2025. "How do authors perceive the way their
       work is cited? Findings from a large-scale survey on quotation accuracy." Journal of the
       Association for Information Science and Technology.
       https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.70000 — Independent methodology: asks
       cited authors whether their own work was characterised correctly. Reached by title only; I did
       not obtain the headline figure. Recorded because it is a non-medical, non-adjudicator method of
       measuring the same gap. SNIPPET-ONLY — figure NOT captured, do not quote a number from this.
    8. First-party corroboration, counted as such: the item's own day. The nightly verification
       reported zero dead citations over 979 references; the same day, two hand-reading frames found
       five citation defects across five days of material, and per the register **every one of the
       five resolves**. That is a within-system demonstration that the two defect classes are
       disjoint, at a hand-reading rate of roughly one pair per twenty minutes. FIRST-PARTY (from
       assumptions.md ASSUMPTION-1206 status note and presumptions.md PRESUMPTION-877 evidence line).

  Strength of challenge: Strong

  Summary: The literature contradicts the inferential step, not the measurement. Nobody disputes that
  979 references resolved; the challenge is to reading that as the corpus's citation result. Three
  independent bodies of evidence converge. First, the defect class that resolution checking cannot see
  is large and measured: 14.5% to 16.9% of quotations wrong in pooled medical samples, ~8% of them
  major, and ~25% of sampled references in the top general-science journals judged not to substantiate
  the claim made from them. Second, the two classes are demonstrably independent — the meta-regression
  finding of *no improvement in quotation accuracy over time*, in exactly the decades when reference
  managers and DOIs largely eliminated pointer errors, is the cleanest available evidence that fixing
  one does nothing for the other. Third, the verification literature states the limitation in its own
  words: authority-database validation "cannot verify whether citation claims accurately reflect source
  document content." The C2A2 case is stronger than the general one, because the day's own hand-reading
  found five defects of which all five resolve — so the check did not merely fail to catch them in
  principle, it failed to catch them in fact, on the same corpus, on the same day. Rated Strong rather
  than Moderate because the challenge does not depend on any single source and because the internal
  replication is available. The one thing I could not find is a direct measurement of the conditional
  quantity — given that a reference resolves, what is the probability it is accurate — so the size of
  the gap in *this* corpus remains unmeasured.

  Specific risks: (a) The claim as phrased is the strongest evidential statement the wiki makes about
  itself and is the one most likely to be quoted forward without its scope; every downstream
  confidence in the citation layer is then borrowed against an instrument that cannot fail in the way
  the corpus actually fails. (b) A "zero" result on an insensitive instrument is worse than no result,
  because it terminates inquiry: the register acquires a headline that discourages the hand-reading
  that is currently the only thing finding defects. (c) If the general rates transfer even
  approximately, 979 attributable PRS references carry on the order of 100–250 quotation-level defects,
  of which roughly half would be major; the day's five found by hand is consistent with that estimate
  and with the corpus being essentially unread rather than essentially clean. (d) The check defines the
  vocabulary — "dead citation" — so the larger class has no name in the register and cannot be counted,
  tracked or trended even after it is noticed. (e) Compounds with ASSUMPTION-1211: if the generator
  produces attributions that are plausible *and* resolvable, the check is not merely silent on the
  defect, it is systematically silent on the specific defect this generator makes.

  Mitigations available:
    - Restate the headline in its true scope: "zero unresolvable references" rather than "zero dead
      citations," and never as "citation health." This costs nothing and removes the inference.
    - Report the two classes side by side and always together: N references resolving, and M
      hand-verified for accuracy out of N. The second number is currently near zero and should be
      stated as near zero.
    - Sample rather than sweep. The quotation-accuracy literature's own method is a random sample of
      cited assertions checked against sources by a reader. A sample of 30–50 of the 979 would give a
      first interval on the corpus's real error rate at a cost of hours, not weeks.
    - Automated content-level verification is now a live research area (arXiv:2511.16198,
      arXiv:2411.06101, arXiv:2606.08589) and reports non-trivial detection with limited context. This
      is a candidate check that would actually address the class — unlike a further resolution check.
      I did not verify any performance figures and cannot vouch for readiness.
    - Track the *found-by-hand* rate as a leading indicator. Five defects in one day of partial reading
      is an estimate of density, not a tally of incidents, and should be recorded as such.

  STEELMAN:
    Item: ASSUMPTION-1206
    Strongest counterargument: The quotation-error literature measures a fundamentally different
    object. Its corpora are papers in which one author characterises another author's *findings* — an
    interpretive act with wide latitude, where reasonable readers disagree, and where a large share of
    the reported "errors" are adjudicator judgements about emphasis rather than factual mismatches.
    C2A2's PRS references are not that: they point at short, structured, machine-readable records in a
    corpus the same system wrote, where the referent is a field, not an argument. In that setting
    resolution is a much better proxy than it is in medicine, because there is far less distance
    between "the record exists" and "the record says what is claimed." Moreover the verification run
    never claimed accuracy — it reported resolution and named exactly what it checked. The inference
    to citation health may be the register's, not the run's, in which case the assumption under test is
    a reading error rather than a measurement error, and the fix is editorial.
    What would need to be true for C2A2 to be safe: (i) the referents must be short and unambiguous
    enough that resolution nearly determines accuracy — but the day's own five defects include "Rohr
    PRS-03 cited for a claim it does not make (twice)" and "Levin PRS-03 carrying a half-correct
    gloss," which are precisely accuracy failures on short structured records, so this condition is
    already known to be violated at least five times; (ii) the headline must never be restated outside
    the run that produced it, since the scope qualifier is what carries the meaning and quotation
    strips it; (iii) the hand-reading that currently finds the defects must continue at a rate
    sufficient to cover the corpus — at one pair per twenty minutes over 307 days, it does not; (iv)
    there must be no downstream consumer that treats "zero dead citations" as licence to skip
    verification.
    How to test: Draw a random sample of 40 of the 979 attributable PRS references. For each, open the
    cited record and score the claim made from it as substantiated / partially substantiated / not
    substantiated, using the major/minor split from the medical literature so the result is comparable.
    Report the proportion not substantiated with a binomial interval. The check's sensitivity is then
    directly estimable: every defect in the sample that nonetheless resolved is an instance the nightly
    verification would have scored as clean. If that proportion is materially above zero, the
    assumption is refuted on the corpus's own evidence, and the size of the gap is known rather than
    argued.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: ASSUMPTION-1206, ASSUMPTION-1213, PRESUMPTION-877 (and adjacent: ASSUMPTION-1211)
    Common vulnerability: **Construct-validity failure in automated proxies — the register measures
    what is cheap to compute and reports it as the construct it wanted.** In 1206/877 an id resolves
    and is reported as citation health. In 1213 a word is counted and reported as argument size. In
    both cases the proxy is perfectly reliable and measures the wrong thing, and in both cases the
    proxy's vocabulary has colonised the register: "dead citation" and "length ratio" are the terms
    available, so the constructs they miss — semantic accuracy, argumentative content — have no name
    and cannot be tracked. The failure signature is identical and it is the classic one: a measure
    that has become a target ceases to be a good measure (Goodhart), and a proxy that omits
    goal-relevant features permits arbitrarily large degradation of those features for small gains in
    the proxy (arXiv:2510.02840).
    Literature basis: PMC12285159 (no improvement in quotation accuracy across the decades that
    eliminated pointer errors); arXiv:2511.16198 (authority-database validation cannot verify semantic
    accuracy); Proc. R. Soc. A 476:20200538 (~25% non-substantiating references in the best-edited
    corpora); arXiv:2605.07409 "The Proxy Presumption: From Semantic Embeddings to Valid Social
    Measures" (title/framing only, SNIPPET-ONLY); Goodhart 1975 / Strathern 1997 formulation
    [primary sources not retrieved in this search].
    Risk level: High
    Recommendation: Treat every automated figure in the nightly register as a measurement of its
    proxy, named as such, and require that any figure promoted to a headline carry an explicit
    statement of the defect class it cannot detect. Where no such statement can be written, the figure
    should not be a headline.

  Recommendation: CHALLENGED
