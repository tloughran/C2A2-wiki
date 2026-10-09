SEARCH-AGAINST-PRESUMPTION-539 (RE-TRIGGER cycle 1):
  Date searched: 2026-10-09
  Original item: PRESUMPTION-539
  Original statement: [inferred] More self-diagnostic output is presumed self-evidently good ("the
    pipeline is now studying its own pathology"), though per PREMISE-123 that self-knowledge cannot
    reach any executor.
  Under test this cycle (MONITOR-477): the current disposition — "keep producing diagnosis; value it by
    ACTUATION, not volume"; self-diagnostic output is surrogation unless actuated; in-house test =
    acted-on/produced ratio. I searched for challenges to that disposition: value without a separate
    actuator, aggregate/corpus value, and boundary conditions on surrogation.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today. Both fetches this item succeeded and were
    not deduplicated against another agent.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (re-trigger cycle 1)]
    Original item: PRESUMPTION-539
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-07-23): Inferred normative "more self-knowledge = better" from headline framing of
        self-directed premises.
      15a (cycle 0): SUPPORTED (Strong) — surrogation (Choi/Hecht/Tayler), Muller 2018, Goodhart.
      15b (cycle 0, 2026-07-24): PARTIALLY-CHALLENGED (Weak-Moderate) — option value, basic-research
        analogy, corpus-for-detection; NO citations (argument only).
      15c: DISPOSITION-525 → MONITOR-477 (Medium; subordinate to PREMISE-105 & PREMISE-123).
      15d (2026-08-02): Re-triggered, cycle 1.
      15b (re-trigger cycle 1, 2026-10-09): 3 searches (measurement reactivity; surrogation boundary
        conditions; near-miss/incident reporting aggregate value); 2 fetches (BMJ Open 2015, full
        text; Sieberichs & Kluge 2021, abstract).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One full-text empirical paper; one abstract; remainder search-result.
    First cycle in which 15b's challenge to this item carries citations.

  Challenging evidence found: Partial

  Sources:
    1. PECARN investigators (contributor initials include RMR; author list/order NOT verified) 2015. Near-miss and unsafe-condition incident reports from 18
       paediatric EDs. BMJ Open 5(9): e007541. [fetched, full text] 487 near-miss/unsafe-condition
       reports over one year, analysed in aggregate; "Based on review of these incident reports, some
       hospitals in our network have modified their processes for recording patient weights, for
       delivering medications to the bedside, and for labelling laboratory specimens"; near misses
       are valuable "because these are not only more common than serious safety events, but also
       provide useful insight into factors that may lead to serious events." Bearing: in the best-
       developed analogue (safety reporting), the value of diagnostic reports is realised at the
       CORPUS level, by later aggregate analysis, mostly not by actuation of individual reports. A
       per-finding acted-on/produced ratio near zero is the normal profile of a working reporting
       system and does not by itself indicate surrogation. HONEST COUNTER IN THE SAME SOURCE: IR
       systems "often in themselves are not granular enough to derive better safety outcomes because
       of lack of how each was followed up" — the corpus pays only when someone eventually analyses it.
    2. Sieberichs, S. & Kluge, A. 2021/2022. "Why learning opportunities from aviation incidents are
       lacking." Aviation Psychology and Applied Human Factors 11(1): 33–47. doi:10.1027/2192-0923/
       a000204. [fetched, abstract] 2,208 voluntary pilot reports; confidential reports "contained
       more information about latent failures"; latent failures identified as risk factors for
       specific unsafe acts. Bearing: value of self-report depends on CONTENT (latent-condition
       information) not on per-report actuation; a volume-vs-actuation metric misses the dimension
       that matters.
    3. Measurement-reactivity literature: Kazdin 1974 (as cited in reviews); smartphone EMA snacking
       study (Maastricht, n=136); daily-diary substance-use RCT (n=307); Miles et al. 2018 (LSHTM)
       on measurement-reaction bias. [search-result] Being monitored, or self-monitoring, changes
       behaviour with no separate intervention; effects are real but often short-lived (accommodation
       within ~1 week) and behaviour-specific. Bearing: diagnosis can BE its own actuator when the
       diagnosed party reads it — "surrogation unless actuated" presumes actuation must be a separate
       downstream step. Transfer to LLM agents reading their own wiki is untested.
    4. Choi, Hecht & Tayler 2012 (Accounting Review) and 2013 (Journal of Accounting Research);
       Wikipedia "Surrogation". [search-result] Surrogation is strongest when agents are compensated on
       a SINGLE measure, weaker with multiple measures, and mitigated when managers participate in
       strategy selection; it persists without incentives (attribute substitution). Bearing: the
       surrogation finding that grounds MONITOR-477 is conditioned on a single incentivised measure
       of a strategic construct; C2A2's self-diagnostic output is not a compensated KPI. The
       transfer is by analogy, and the analogy's boundary conditions are not obviously met.
    COUNTERWEIGHT reported for honesty (search-result, healthcare incident-reporting review): reductions
       in incidents "were often assumed rather than shown" — supports MONITOR-477's caution that
       corpus value is frequently asserted, not demonstrated.

  Strength of challenge: Moderate (up from Weak-Moderate; now cited)

  Summary: The literature does not support "more self-diagnosis is self-evidently good" — the
    original presumption stays refuted. But it does challenge the disposition's measuring rule.
    Safety-reporting systems derive their value from aggregate analysis of reports most of which are
    never individually acted on, so a low per-finding actuation ratio is expected even in systems that
    work. Measurement reactivity shows that diagnosis read by the diagnosed party can change behaviour
    without any separate executor. And surrogation's documented conditions (single incentivised
    measure) are not clearly present. The defensible rule is that self-diagnosis earns its keep if
    some aggregate analysis consumes the corpus and produces changes — not if each finding is actuated.

  Specific risks: (i) the in-house acted-on/produced ratio would read near zero for a healthy
    corpus-type system and trigger suppression of the very corpus SYSTEMIC-RISK detection draws on;
    (ii) conversely, corpus value is often assumed, not shown — absent a scheduled aggregate consumer
    the corpus is surrogation by another name.

  Mitigations available: replace the per-finding ratio with a corpus-level test — over a window, how
    many system changes cite ≥2 self-diagnostic findings jointly (aggregate actuation); name the
    aggregate consumer (13 pattern detector / 15b SYSTEMIC-RISK pass) and check it actually reads the
    corpus; monitor content quality (latent-condition information) rather than volume.

  Recommendation: PARTIALLY-CHALLENGED — challenges the actuation-per-finding valuation rule; does
    not rehabilitate "more is better."

STEELMAN:
  Item: PRESUMPTION-539 / MONITOR-477 disposition
  Strongest counterargument: Aviation and hospital reporting systems are the most successful
    self-diagnostic institutions we have, and almost none of their individual reports are acted on;
    their value comes from someone later reading hundreds together and seeing the latent condition.
    Judging C2A2's self-diagnosis by whether each finding was actuated would condemn those systems
    too. Meanwhile the surrogation evidence comes from managers paid on a single metric — a condition
    C2A2's diagnostic output does not meet — and the measurement-reactivity literature shows that a
    party that reads its own diagnosis can change without any executor at all.
  What would need to be true for C2A2 to be safe: a named aggregate consumer reads the self-diagnostic
    corpus on a schedule and its outputs demonstrably cite multiple findings.
  How to test: count system changes (spec edits, premise changes) in the last 60 days that cite two or
    more self-diagnostic findings; compare with per-finding actuation. High aggregate / low
    per-finding = corpus value real; both near zero = surrogation confirmed.
