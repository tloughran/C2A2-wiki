SEARCH-AGAINST-PRESUMPTION-865:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-865
  Queue ref: LIT-QUEUE-2026-08-24-009
  Original statement: Reducing collection breadth is low-cost when the collected items are not being
    consumed.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-865
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from the asymmetry between the stated cost (queue depth) and the unstated
           cost (coverage)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Search scope: HONEST LIMITATION — no WebSearch query was executed specifically for this item. The
    session WebSearch budget (200/200) was exhausted before I reached it; my two planned queries
    (adaptive-sampling bias / unknown inclusion probability; systematic-review search-strategy
    narrowing and coverage bias) both returned budget-exhausted errors. The evidence below comes from
    documents surfaced by the PRESUMPTION-875 searches and then fetched and read directly, which
    turned out to contain a formalisation of the exact cost asymmetry at issue. Venues reached:
    arXiv (cs.CR). Date range: 2026, with one secondary citation to 2019. This search is
    PRELIMINARY, and specifically it does NOT cover: the statistics literature on adaptive/sequential
    sampling and inverse-probability weighting; the systematic-review methodology literature on
    database-coverage bias; the file-drawer / publication-bias literature at the level of what was
    never searched. All three of those would likely strengthen or sharpen the challenge, and this
    item should be re-queued for a budgeted search.

  Challenging evidence found: Partial

  Sources:
    1. [Authors not captured.] 2026. "AI-Driven Security Alert Screening and Alert Fatigue Mitigation
       in Security Operations Centers: A Comprehensive Survey." arXiv:2605.08316, §3.1.
       https://arxiv.org/html/2605.08316v1 — The central challenging source. It formalises exactly
       the asymmetry 14b inferred, and reaches the opposite conclusion from the presumption: "The
       asymmetric cost structure (where a suppressed true positive (missed threat) incurs unbounded
       organizational damage while a passed false positive merely consumes analyst time) drives the
       optimization toward extreme conservatism at the decision threshold." And: "The design question
       is not 'maximize accuracy' but 'maximize suppression rate subject to a tolerable FNR budget',
       typically FNR < 2% in production systems." Two things follow. First, the cost of reduced
       breadth is treated as *unbounded*, not low. Second — and this is the sharper point — the cost
       of the retained-but-unconsumed item is explicitly "merely consumes analyst time," i.e. the
       field's own framing is that queue depth is the *cheap* side of the trade. The presumption
       inverts the literature's cost ordering. FULL-TEXT (§3.1 read verbatim via fetch; later
       sections truncated by fetch size limits).
    2. Same source, §3.1 continued — Note that the survey draws a distinction directly relevant here:
       filtering "operates on already-generated alerts and makes no modifications to the detection
       layer itself," as opposed to "upstream IDS tuning (which reduces the alert generation rate at
       the source by adjusting detection thresholds)." Reducing *collection breadth* is the upstream
       operation. The survey's remedies (cost-sensitive formulation, uncertainty quantification,
       conservative operating-point selection, explicit FNR budget) are all applied to the downstream
       filter, where the suppressed item still exists and could in principle be recovered. Nothing
       analogous protects the upstream case, where the item is never generated. FULL-TEXT.
    3. Pendlebury et al. — cited within arXiv:2605.08316 [ref 112]: "ignoring temporal ordering in
       splits inflates reported performance." CITED-WITHIN; I did not retrieve the primary source and
       the full citation is unverified. Relevant as the closest thing I found to the "non-uniform
       coverage is not recoverable later" question: an evaluation built on a corpus collected under a
       policy that varied over time will overstate its own performance, and the inflation is not
       correctable after the fact without knowing the policy.
    4. Same source, §4.3 — "alert distributions are non-stationary, so trained models drift; explicit
       drift-detection methods (ADWIN, Page-Hinkley, DDM) monitor prediction-stream statistics and
       trigger retraining." Bears on recoverability: if the underlying distribution moves while
       collection breadth is narrowed, the gap in the corpus is not a random hole but a hole aligned
       with a particular period and a particular policy — the worst case for later correction.
       FULL-TEXT.
    5. Same source, table of contents, §10 "C3: Label scarcity, noise, and temporal drift" and §12
       "Selection bias (internal)" — the survey names both as open research challenges and threats to
       validity. I could not read the bodies of these sections (truncated by fetch size limit), so I
       flag them as pointers rather than evidence. SNIPPET-ONLY.

  Strength of challenge: Moderate

  Summary: I found one source that formalises the exact trade-off and orders the two costs in the
  opposite direction from the presumption: in mature alert-screening practice the retained-but-
  unreviewed item "merely consumes analyst time" while the never-collected true positive "incurs
  unbounded organizational damage," and production systems accordingly hold themselves to a false-
  negative budget under 2%. That is a direct challenge to "reducing collection breadth is low-cost."
  The specific sub-claim — that reduced breadth is low-cost *because* items are unconsumed — is
  weakened further by two considerations in the same source: a suppressed-but-generated item is at
  least recoverable, whereas a never-collected item is not, so the upstream operation is strictly
  more destructive than the downstream one the literature is careful about; and under non-stationary
  distributions the resulting gap is policy-aligned and time-aligned rather than random, which is the
  hardest kind to correct after the fact. The challenge is rated Moderate rather than Strong because
  the evidence is analogical (security alert triage, not literature search), because I reached only
  one substantive source, and because I could not execute any query targeted at this item — the
  statistics and systematic-review literatures that bear on recoverability were not searched at all.

  Specific risks: If reduced breadth is not low-cost, C2A2 has silently traded an unmeasured quantity
  (coverage) for a measured one (queue depth), and the trade is invisible in the artefacts because
  the only thing recorded is what was collected. Concretely: (a) the missing items leave no trace —
  there is no "not searched" entry anywhere, so no downstream reviewer can even estimate the gap;
  (b) if the narrowing policy correlates with anything substantive (a channel, a topic, a period),
  the surviving corpus is biased rather than merely smaller, and every aggregate statement computed
  over it inherits that bias; (c) recoverability is asymmetric in time — sources go dark, queues
  expire, context is lost — so a decision to narrow *now* forecloses options *later* in a way that
  keeping items does not; (d) the justification is circular in a dangerous way: items are unconsumed
  because the review gate is not serviced (PRESUMPTION-875), and breadth is cut because items are
  unconsumed, so a failure of the review gate silently propagates upstream into a permanent coverage
  loss; (e) the pipeline's own null results become uninterpretable — a NO-CHALLENGE-FOUND from an
  unknown fraction of the intended search space is not evidence of absence, and this file is itself an
  example, since two of my five items were searched under a degraded budget.

  Mitigations available:
    - Set an explicit false-negative budget for any narrowing decision rather than narrowing
      opportunistically — the production practice is FNR < 2% (arXiv:2605.08316 §3.1). Even a
      declared-but-loose budget converts an invisible cost into a stated one.
    - Prefer downstream filtering over upstream collection reduction, since the filtered item still
      exists and remains recoverable (arXiv:2605.08316 §3.1's own distinction).
    - Record the narrowing policy itself as a first-class artefact — which channels, which period,
      which threshold — so that later re-weighting is at least possible. This is the minimum
      condition for the coverage gap to be recoverable at all, and it is nearly free.
    - Drift detection over the collection stream so that policy-aligned gaps are flagged when the
      underlying distribution moves (arXiv:2605.08316 §4.3, citing ADWIN / Page-Hinkley / DDM).
    - Log null results per channel, not just per item, so that "searched and found nothing" is
      distinguishable from "did not search."

  STEELMAN:
    Item: PRESUMPTION-865
    Strongest counterargument: The alert-screening analogy imports an assumption that does not
    obviously hold here — that undetected items carry unbounded downside. In a SOC, a missed true
    positive is an intrusion; in a literature-review pipeline, a missed source is a source that
    someone can find later, and the corpus of scholarly literature is persistent, indexed and
    re-searchable in a way an ephemeral alert stream is not. If the items being collected are drawn
    from a stable, permanently addressable population, then narrowing collection is genuinely
    reversible: you re-run the search later with a wider net and recover exactly what you skipped.
    Under that condition the cost of reduced breadth really is close to the cost of the delay alone,
    and paying storage and queue-depth cost now for items nobody will read is straightforwardly
    wasteful. The presumption may be sloppily stated but substantially right for this domain.
    What would need to be true for C2A2 to be safe: (i) the sources being narrowed away must be
    persistent and re-addressable — permanent identifiers, stable venues, no rate-limited or
    expiring channels; (ii) the narrowing policy must be recorded, so a later wider search knows what
    it is filling in; (iii) no aggregate or null-result claim may be made over the narrowed corpus
    without disclosing the narrowing — otherwise the bias is laundered into a finding; (iv) the
    narrowing must not be correlated with the substance of what is being sought, which is hard to
    guarantee when the narrowing criterion is "reduce volume" and volume correlates with topic
    popularity; (v) the delay before re-broadening must be bounded, which reintroduces dependence on
    the review gate (PRESUMPTION-875).
    How to test: Yes, and cheaply, via a back-fill experiment. Pick a past period where breadth was
    reduced, re-run the wider collection policy retrospectively, and measure (a) what fraction of the
    skipped items are still retrievable — this tests recoverability directly, and (b) what fraction of
    the recovered items would have changed a downstream conclusion — this tests materiality. A high
    retrievability rate and a near-zero materiality rate would substantially vindicate the
    presumption; either being poor would confirm the challenge. A second, cheaper test: check whether
    any existing artefact states a conclusion over a corpus collected under a narrowing policy without
    disclosing it. If so, condition (iii) has already failed.

  Recommendation: PARTIALLY-CHALLENGED
