SEARCH-AGAINST-ASSUMPTION-474:
  Date searched: 2026-07-20
  Original item: ASSUMPTION-474
  Original statement: The vault census measures machine-dump volume rather than knowledge-graph health; the week-over-week delta mixes ~+145 real growth with ~+80 definitional difference, and the series needs a break-marker or a re-derivation.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-474
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-07-19 sewing weekly and bootstrap audit transcripts
      15b: Searched for challenging literature (index break conventions in official statistics, Goodhart effects on proxy metrics, reconciliation of definitional vs real change)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Eurostat, *Backcasting manual — 2025 edition* (KS-01-25-030) and Eurostat, "EU labour force survey — correction for breaks in time series" (Statistics Explained, retrieved 2026-07-20). Official-statistics practice when a definition changes is to **backcast and correct the historical series**, not to leave a marker on a discontinuous one. Challenges the item's "break-marker **or** re-derivation" as a false equivalence: the two options are not of comparable quality, and the cheaper one preserves the incomparability it flags.
    2. Eurostat, "Guidance on time-series treatment in the context of COVID-19" (retrieved 2026-07-20). Confirms that flagging a break is a fallback used when correction is infeasible, and that flagged series remain unusable for the trend analysis they were kept for.
    3. Splunk, "What is Goodhart's Law?" and Psych Safety, "Goodhart's Law, Campbell's Law, and the Cobra Effect" (retrieved 2026-07-20). The standard remedy in this literature is **multiple measures triangulating the goal**, not the replacement of one proxy by another. Challenges the implied move from "file count is a bad proxy" to "connectivity is the right one" — connectivity is subject to the identical argument once it is targeted.
    4. Monte Carlo, "The Comprehensive Guide To Data Reconciliation" and Tricentis, "What is data reconciliation?" (retrieved 2026-07-20). Mismatches between two systems commonly stem from definitional differences — aggregation level, inclusion window, processing delay — and "not all differences represent actual errors requiring correction." Supports the item's diagnosis but challenges the precision of the ~+145 / ~+80 split, which is a partition asserted before the frozen-snapshot dual-resolver run that would establish it.

  Strength of challenge: Moderate

  Summary: The core observation — that a file count measures dump volume and that a resolver change contaminated the week-over-week delta — is not contradicted by anything retrieved. Two things are challenged. First, the remedy menu: official-statistics practice treats break-marking as the fallback when correction is infeasible, and re-derivation as the standard; offering them as alternatives understates the cost of the cheap one, because a marked-but-uncorrected series still cannot answer the question the series exists to answer. Second, the numbers: the ~+145/~+80 decomposition is presented as a finding but is an estimate that the item's own proposed test has not yet produced, and the reconciliation literature is explicit that separating definitional from real change requires running both definitions over one frozen snapshot before the split is quotable. Third and more structurally, the Goodhart framing does not license substituting connectivity for file count — connectivity becomes a target the moment it is adopted, and the literature's actual recommendation is a small panel of measures, none load-bearing alone.

  Specific risks: If the break-marker path is taken because it is cheaper, C2A2 acquires a permanently discontinuous health series that is nominally documented and practically unusable, and the discontinuity will be re-discovered at some later audit. If the ~+80 figure circulates before the frozen-snapshot test, a provisional estimate hardens into a cited fact — the same mechanism PRESUMPTION-501 describes. If connectivity replaces file count as the single health metric, the same Goodhart failure recurs one metric later, and this time against a metric agents can directly optimize by adding wikilinks.

  Mitigations available: Run the dual-resolver frozen-snapshot test first and quote the definitional component only after it is measured. Prefer re-derivation over marking; if marking is chosen, record it as a known-deficient fallback with a scheduled re-derivation date rather than as a resolution. Adopt a small panel (count, orphan rate, connectivity, edit recency) with an explicit rule that no single member is a target, per the Goodhart literature's own recommendation.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-474
  Strongest counterargument: The item correctly identifies a contaminated series and then offers, as equal options, the one action that fixes it and the one action that documents that it is broken. Official statistics does not treat these as equivalent: Eurostat's backcasting manual exists precisely because a flagged discontinuity leaves the series unable to support trend inference, which is the only reason a weekly census is maintained. Meanwhile the numbers that would justify either action — the ~+145/~+80 partition — have not been measured; they are an inference from the size of the resolver change, offered in the same register as an observation. And the framing that motivates the whole item, "this measures dumps not graph health," implies a replacement metric that is subject to the identical Goodhart argument the moment it is adopted, with the added hazard that connectivity is directly writable by the agents being measured. The item is right that something is wrong and has not yet earned any of its three next steps.
  What would need to be true for C2A2 to be safe: The definitional component must be measured, not estimated, before it is quoted; re-derivation must be attempted before marking is accepted; and whatever replaces the raw count must be a panel no member of which is separately targeted.
  How to test: Freeze one vault snapshot. Run the old and new resolvers over it and record the exact difference — that number, not an estimate, is the definitional component; the residual is real growth. Then re-derive the prior weeks under the new definition and check whether the connectivity trend reverses sign, which is the item's own stated discriminator. Separately, log whether any agent's edit behaviour changes in the two weeks after connectivity is announced as a health metric.

  Search scope: Preliminary — four targeted searches. Broader search recommended on knowledge-graph health metrics specifically; the retrieved material on that sub-target was thin.
