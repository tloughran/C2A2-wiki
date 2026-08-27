SEARCH-AGAINST-ASSUMPTION-1176:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1176
  Original statement: "`N>=3` licenses only R>=0.464 at 90% confidence; R>=0.80 needs n=11. **The threshold that item waited five cycles to reach would not have settled it.**"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1176
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim from the pipeline's disposition note. [stated]
      15b: Searched for challenging literature; independently recomputed the stated bounds
    Current status: PARTIALLY-CHALLENGED

  Search scope: Comprehensive on the arithmetic (recomputed from first principles, shown below);
    comprehensive on the two literatures that bear on it — (i) zero-failure binomial reliability
    demonstration and its independence assumption, (ii) the methodological critique of evidence
    thresholds expressed as raw counts of studies (vote counting). Queries via WebSearch ("rule of
    three" zero-failure reliability confidence bound; vote counting invalid in evidence synthesis
    Hedges & Olkin; confidence intervals for correlation at very small n). Bibliographic details for
    every citation below verified against the Crossref REST API or the arXiv Atom API on 2026-08-25.
    Date range 1934-2026.
    GAPS: (a) The stated claim does not name its own statistical model, so the reconstruction below is
    an inference from the numbers — a very well-determined inference (two independent exact matches to
    four significant figures), but an inference. (b) The WebSearch budget was exhausted during this
    assignment; the vote-counting critique was verified bibliographically but full texts were not
    retrieved. (c) I did not locate any source that treats "N corroborating sources" in an
    AI-assisted literature pipeline as a formal reliability demonstration — the mapping the claim
    performs appears to be novel and therefore un-peer-reviewed.

  Challenging evidence found: Partial

  MY OWN ARITHMETIC (this is the required verification):

    Reconstruction of the model. The two numbers are only jointly consistent with one standard
    formula: the one-sided lower confidence bound on reliability from a zero-failure binomial
    demonstration test. This is the Clopper-Pearson exact lower limit specialised to the case x = n
    (all n trials succeed):

        R_L = (1 - C)^(1/n)          where C is the confidence level

    Check 1 — the N>=3 figure. With n = 3, C = 0.90:
        R_L = (1 - 0.90)^(1/3) = 0.10^(1/3) = 0.464158883...
             = 0.4642 to 4 s.f.
      The claim states 0.464. EXACT MATCH.

    Check 2 — the n = 11 figure. Solve (1 - C)^(1/n) >= 0.80 for n at C = 0.90:
        n >= ln(0.10) / ln(0.80) = (-2.302585093) / (-0.223143551) = 10.31885...
      so the smallest integer n is 11.
      Verifying by direct evaluation:
        n = 10:  0.10^(1/10) = 0.794328...   < 0.80   (insufficient)
        n = 11:  0.10^(1/11) = 0.811130...  >= 0.80   (sufficient)
      The claim states n = 11. EXACT MATCH.

    Full table at C = 0.90, for reference:
        n :  1      2      3      4      5      6      7      8      9      10     11     12
        R_L: 0.100  0.316  0.464  0.562  0.631  0.681  0.720  0.750  0.774  0.794  0.811  0.825

    VERDICT ON THE ARITHMETIC: **The stated bounds are correct.** Both figures reproduce exactly under
    the standard zero-failure reliability-demonstration formula at 90% one-sided confidence. I could
    not break either number. This is a legitimate confirmation and is recorded as such.

    WHAT THE ARITHMETIC IS NOT. Two things follow that the claim's wording obscures.

    (a) The symbol R here is a *reliability* (a Bernoulli success probability), not a correlation
        coefficient. The item's own testability note says "confidence bounds on correlation/reliability
        estimates at small n," collapsing two different parameters. They are not interchangeable, and
        the numbers belong unambiguously to the reliability reading. For contrast, on the correlation
        reading the corresponding quantity is not merely weak but undefined: the Fisher z-transform
        standard error is 1/sqrt(n - 3), which at n = 3 divides by zero, so the conventional 90%
        interval for a Pearson r at n = 3 is the entire admissible range [-1, +1]. If any downstream
        C2A2 text reads "R>=0.464" as a correlation floor, it is reading a number that the derivation
        does not license.

    (b) The formula assumes n *statistically independent* trials with *zero observed failures*. Both
        assumptions are doing heavy lifting when the "trials" are corroborating sources found by a
        search, and both are challenged by the literature below. Independence failure makes the bound
        anti-conservative (Salako & Zhao 2022); the zero-failure condition is not established by a
        search that was looking for confirmations, because unfound disconfirmations are not observed
        failures — they are unobserved trials.

    An illustrative consequence of (b), flagged as illustrative and not derived: Bugaud (2026, cited in
    ASSUMPTION-1175) finds that family-correlated errors reduce 17 nominally distinct models to an
    effective 2.5-3.6 independent voters. Applying an effective-to-nominal ratio of that order to
    n = 3 gives n_eff near 1, and 0.10^(1/1) = 0.10. The claim's own conclusion — that N>=3 is too
    weak — is, if anything, understated.

  Sources:
    1. Clopper, C. J., & Pearson, E. S. 1934. "The use of confidence or fiducial limits illustrated in
       the case of the binomial." Biometrika, 26(4):404-413. DOI 10.1093/biomet/26.4.404. — The origin
       of the exact interval whose x=n special case is the formula reproduced above. Establishes that
       the stated bounds are correctly derived, and that they are *exact* rather than approximate, so
       the claim cannot be attacked as an approximation artefact. METADATA-ONLY (Crossref).
    2. Salako, K., & Zhao, X. 2022. "Demonstrating Software Reliability using Possibly Correlated
       Tests: Insights from a Conservative Bayesian Approach." arXiv:2208.07935; accepted by Quality
       and Reliability Engineering International. — The central challenge to the *applicability* of the
       claim. Formalises "doubting" that executions are independent and shows "the extent to which
       independence assumptions can undermine conservatism in assessments." Two of their findings bear
       directly: that there is a confidence level an assessor must already possess before testing is
       informative at all ("otherwise, such testing is futile — favourable operational testing evidence
       will eventually decrease one's confidence"), and that "in some scenarios, observing a system
       operate without failure gives less confidence in the system than if some failures had been
       observed." Both attack the zero-failure logic that N>=3 corroborating sources implicitly invokes.
       ABSTRACT-ONLY (arXiv API).
    3. Hedges, L. V., & Olkin, I. 1980. "Vote-counting methods in research synthesis." Psychological
       Bulletin, 88(2):359-369. DOI 10.1037/0033-2909.88.2.359. — The canonical demonstration that
       evidence thresholds expressed as counts of studies are statistically defective. Vote counting
       has extremely low power at realistic effect and sample sizes, and — the celebrated
       counter-intuitive result — its power *decreases* as the number of studies reviewed increases.
       This challenges the claim's remedy rather than its arithmetic: raising the count from 3 to 11
       does not repair a count-based gate, because the defect is in counting, not in the count.
       SNIPPET-ONLY (metadata verified via Crossref; abstract via search snippet).
    4. Combs, J. G., Ketchen Jr., D. J., Crook, T. R., & Roth, P. L. 2011. "Assessing Cumulative
       Evidence within 'Macro' Research: Why Meta-Analysis Should be Preferred Over Vote Counting."
       Journal of Management Studies, 48(1):178-197. DOI 10.1111/j.1467-6486.2009.00899.x. — Restates
       the Hedges-Olkin result for a management-research audience and makes the precision point:
       vote counting gives each study one vote regardless of sample size or quality. Relevant because
       C2A2's sources are radically heterogeneous in weight. METADATA-ONLY (Crossref).
    5. Grainger, M. J., Stewart, G. B., & Haddaway, N. R. 2022. "Why 'vote-counting' is never
       acceptable in evidence synthesis." OSF preprint. DOI 10.31219/osf.io/c49uh. — Recent and
       maximally strong statement of the same position; title states the thesis. Note: preprint, not
       peer-reviewed at the version located. METADATA-ONLY (Crossref).
    6. Bugaud, Z. 2026. "Hidden Clones: Exposing and Fixing Family Bias in Vision-Language Model
       Ensembles." arXiv:2603.17111. — Supplies the effective-versus-nominal-n quantity used in the
       illustrative calculation above: correlated errors reduce 17 nominally independent models to
       2.5-3.6 effective independent voters, and produce a tier where correlated majority error takes
       accuracy to 0%. ABSTRACT-ONLY (arXiv API).

  Strength of challenge: Weak (against the arithmetic — the arithmetic is confirmed)
                         Moderate (against the construct: what R denotes, and whether the
                         independence and zero-failure conditions that make the formula valid are met)

  Summary: I recomputed both figures independently and both are exactly right: 0.10^(1/3) = 0.4642 and
    the least n with 0.10^(1/n) >= 0.80 is 11. The claim's arithmetic survives. What does not survive
    unqualified is the construct it is attached to. The formula is the Clopper-Pearson zero-failure
    reliability bound, which presumes independent trials and genuinely observed non-failures; a
    literature search that returns three supporting sources satisfies neither condition, since sources
    within a field are correlated and unfound disconfirmations are unobserved rather than absent.
    Salako & Zhao (2022) show that dropping independence removes the conservatism the bound is prized
    for, and that zero-failure evidence can in some regimes be *less* informative than evidence
    containing failures. Separately, the classical synthesis literature (Hedges & Olkin 1980; Combs et
    al. 2011; Grainger et al. 2022) holds that count-based evidence thresholds are defective in kind
    and cannot be repaired by raising the count — which means the claim's implied remedy (use n=11) is
    the wrong repair even though its diagnosis (n=3 is too weak) is right. The item also conflates
    "reliability" with "correlation" in its own testability note; at n=3 the correlation reading is not
    weak but undefined, since the Fisher-z standard error 1/sqrt(n-3) divides by zero.

  Specific risks: If the claim is taken at face value and C2A2 responds by raising its gates from N>=3
    to N>=11, it will incur roughly four times the search cost for a threshold that is still
    statistically invalid in kind, still assumes source independence it does not have, and still counts
    a blog post and a Biometrika paper as one vote each. The more serious risk is the opposite one: if
    the R symbol propagates into the vault read as a correlation, downstream entries will inherit a
    number that its derivation does not support. And because the independence assumption is
    unwarranted, the true situation is worse than 0.464, not better — so any decision that treats
    0.464 as a floor is optimistic.

  Mitigations available:
    - Replace count gates with weight-and-quality-sensitive synthesis. This is the standing
      recommendation of the whole vote-counting literature (Hedges & Olkin 1980; Combs et al. 2011;
      Grainger et al. 2022): grade sources by design, directness and independence rather than tally
      them.
    - If a count gate must be retained for tractability, discount nominal n to an effective n before
      applying the bound, and state the discount. Bugaud (2026) gives a defensible order of magnitude.
    - Adopt conservative-Bayesian bounds that price in doubt about independence rather than assuming it
      away (Salako & Zhao 2022) — these are designed for exactly the situation where you cannot
      certify that your trials were independent.
    - Record disconfirmations as observed failures. The zero-failure formula only applies if you
      actually looked for failures; the for/against split in this very pipeline is the mechanism that
      would make the zero-failure condition earned rather than assumed. That is a genuine architectural
      strength of C2A2 and should be cited when the bound is invoked.
    - Rename the symbol. Use R_rel or p_success, never bare R, to prevent the correlation misreading.

  STEELMAN:
    Item: ASSUMPTION-1176
    Strongest counterargument: The claim is arithmetically flawless and its rhetorical target — a
      self-imposed threshold that could not have licensed its own conclusion — is a real and useful
      finding. But the claim quietly imports a reliability-engineering model into an evidence-synthesis
      setting where its two enabling assumptions fail. Zero-failure demonstration testing earns its
      strong bound by running n pre-specified independent trials and observing that none failed; a
      literature search that stops at three confirmations has run an unknown number of trials, observed
      an unknown number of failures, and drawn its sources from a correlated population. Under those
      conditions the 0.464 figure is not a floor but an upper-optimistic estimate, and the natural
      reading of the claim — "so use 11 instead" — reproduces the defect at higher cost, because
      Hedges and Olkin showed in 1980 that the power of count-based gates can fall rather than rise as
      the count increases.
    What would need to be true for C2A2 to be safe: (a) the number is used only as a rhetorical
      demonstration that small-N gates are weak, never as a live parameter in a decision rule; (b) if it
      is used as a parameter, source independence is argued for rather than assumed, and disconfirming
      searches are actually run so that "zero failures" is an observation rather than an artefact of
      one-sided searching — which is exactly what the 15a/15b architecture provides; (c) the symbol R is
      never read as a correlation anywhere downstream. Under (a)-(c) the claim is a correct and
      salutary warning and nothing breaks.
    How to test: Two checks, both cheap. First, the arithmetic — already done above and confirmed;
      anyone can reproduce it with `0.10**(1/3)` and `log(0.10)/log(0.80)`. Second, and more
      informative, the independence assumption: take a set of C2A2 claims that reached N>=3 and, for
      each, record whether the corroborating sources share authors, institutions, a common primary
      source, or a common upstream review. The proportion sharing at least one such link estimates the
      correlation the formula assumes to be zero. If that proportion is materially above zero — which
      for a vault built around fourteen named thinkers it almost certainly is — the effective n is below
      3 and the 0.464 bound is anti-conservative, in which case the claim's conclusion holds a fortiori.

  Recommendation: PARTIALLY-CHALLENGED
