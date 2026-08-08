SEARCH-AGAINST-PRESUMPTION-701:
  Date searched: 2026-08-07
  Original item: PRESUMPTION-701
  Original statement: That determinacy of target is sufficient warrant for a vault-wide sweep;
    a bulk repair cleared because "this has one determinate target, so a vault-wide sweep is
    safe," on the same day the same agent family warned that a sweep keyed on a similar
    identifier "would have corrupted one of them."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-701
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Read two same-day rulings from one agent family against each other — one clearing a
        sweep on determinacy grounds, one warning that a sweep on a similar identifier would
        have corrupted a target.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Winters, T., Manshreck, T. and Wright, H. (eds.), 2020. "Software Engineering at Google,"
       Chapter 22, "Large-Scale Changes" (abseil.io/resources/swe-book/html/ch22.html — chapter
       located and read in summary this session; editor list is the standard attribution for the
       volume and was not re-confirmed from the page itself, and the chapter's individual author
       is [UNVERIFIED]). The single most directly relevant source. Google's LSC infrastructure
       (Rosie) does *not* clear a change on the determinacy of its target. It shards the change
       along project and ownership boundaries into units that can be submitted atomically, and
       then puts each shard through an *independent test-mail-submit pipeline* — that is, each
       shard is separately tested, separately reviewed and separately submitted, precisely so
       that a fault in the transformation is contained to one shard rather than landing
       vault-wide. Rosie additionally caps the number of outstanding shards, runs at lower
       priority, and negotiates load with the shared testing infrastructure. Chromium and
       ChromeOS publish equivalent LSC processes (chromium.googlesource.com LSC docs;
       chromium.org ChromeOS developer library LSC guide, both located this session). The
       structural point against PRESUMPTION-701 is stark: the organisation with the most
       experience of vault-wide sweeps in existence treats determinacy of the *specification* as
       the beginning of the safety argument, not the end of it, and its entire apparatus exists
       to cover the gap between a determinate target and a correct execution.
    2. "Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review
       Efficiency." arXiv 2605.30208 (identifier and title confirmed this session; author list,
       year and venue [UNVERIFIED — full text not retrieved]). Meta assigns *risk scores* to
       diffs and only automates review for those scoring low, and the reported policy makes a
       distinction that is exactly on point: deterministic codemods may bypass per-diff review
       entirely, whereas AI-generated codemods require per-diff evaluation, and runbooks are
       governed by per-runbook risk history. So even where automated bulk change is permitted
       without human review, the licence attaches to the *provenance and determinism of the
       transformation*, not to the determinacy of what it is aimed at. A sweep authored by an
       agent falls, on Meta's own taxonomy, in the class that requires per-instance evaluation.
    3. "An Empirical Study on the Potential of LLMs in Automated Software Refactoring." arXiv
       2411.04444 (identifier and title confirmed; authors and venue [UNVERIFIED — full text not
       retrieved, and the figures below are taken from a search-result summary and were not
       verified against the paper). Reported unsafe-solution rates of 6.6% (Gemini) and 7.4%
       (GPT), with 18 of 22 unsafe cases unsafe because the suggested change altered the
       functionality of the code involved. [Treat these numbers as indicative only — I did not
       open the paper.] The relevance is the order of magnitude: an agent-authored bulk
       transformation with a per-site error rate in the several-percent range, applied
       vault-wide, produces a large absolute number of corrupted sites, and none of that risk is
       addressed by the target being determinate.
    4. Practitioner literature on in-place bulk text substitution (LinuxCapable, Linuxize,
       phoenixNAP, thoughtbot and nixCraft guides to `sed`, all located this session; all
       non-peer-reviewed vendor/tutorial material and cited only for the consensus warning they
       carry). The uniform warning is that `sed -i` with a wrong or over-broad pattern silently
       corrupts files, that bulk in-place modification carries a high chance of modifying the
       wrong files, and that the operation is not self-announcing. [NEGATIVE RESULT, stated
       plainly: I searched specifically for a documented public postmortem of a mass-edit
       corruption caused by a false-uniqueness assumption about an identifier and did not find
       one. That is a gap in this file, not evidence that such incidents are rare — internal
       postmortems of this class are typically not published.]
    5. Google's own account of monorepo practice ("Why Google Stores Billions of Lines of Code
       in a Single Repository," Communications of the ACM — title and venue confirmed this
       session; authors and year [UNVERIFIED, commonly attributed to Potvin and Levenberg,
       2016]), which situates the LSC tooling in a codebase where determinate-target sweeps are
       routine and still gated by testing.

  Strength of challenge: Strong

  Summary: The presumption confuses a property of the specification with a property of the
    execution. "This has one determinate target" is a claim about what the change is *aimed at*;
    the safety of a vault-wide sweep depends on whether the matcher used to find that target
    selects it and nothing else, on whether the transformation applied at each match is correct,
    and on whether the blast radius of an error is bounded. Determinacy of target constrains
    none of these. The industrial practice that has had to solve this problem repeatedly does
    not use determinacy as a gate: Google shards LSCs and runs each shard through an independent
    test-and-submit pipeline, and Meta gates automated bulk change on the provenance and
    determinism of the transformation, explicitly excluding AI-generated codemods from
    review-free treatment. The item's own internal evidence is the sharpest source available:
    the same agent family, on the same day, recorded that a sweep keyed on a similar identifier
    would have corrupted a target — which is a demonstrated instance of the belief in uniqueness
    being false. That instance converts the question from theoretical to empirical, and the
    correct inference from it is that uniqueness must be *verified against the corpus* before
    each sweep, not asserted from the shape of the identifier.

  STEELMAN:
    Item: PRESUMPTION-701
    Strongest counterargument: The two same-day rulings may not be inconsistent at all — they
      may be exactly the discrimination the agent family was making. The warning case concerned
      an identifier that *turned out* to be non-unique; the cleared case concerned one that had
      been checked and was determinate. If the determinacy claim was the *output* of a
      verification step rather than an assumption, then "this has one determinate target, so a
      vault-wide sweep is safe" is a correct summary of a correct process, and 14b has read a
      compressed conclusion as though it were the whole reasoning. There is also a real cost on
      the other side. Google's sharding apparatus exists because Google has thousands of
      engineers and owners to consult; C2A2 has one corpus, one authoriser and a version-control
      substrate. If every bulk repair requires a sharded, staged, independently reviewed
      pipeline, the effective outcome is that bulk repairs stop happening, and the vault
      accumulates uncorrected defects — a cost the literature on unfixed-warning backlogs says
      is substantial. Where the operation is fully reversible (a git working tree, a snapshot, a
      dry-run diff retained), the expected cost of a bad sweep is the cost of reverting it, which
      may be genuinely small, and demanding shard-level ceremony for a reversible operation is
      the kind of over-control that produces the approval bottleneck flagged elsewhere in this
      batch.
    What would need to be true for C2A2 to be safe: (a) determinacy is *established by
      enumeration against the actual corpus* immediately before the sweep — the matcher is run
      in report-only mode and the match count is compared to the expected count, so uniqueness
      is a measurement rather than an inference from the identifier's form; (b) a diff is
      produced and reviewed, or at minimum machine-checked for shape, before any write; (c) the
      operation is atomically reversible — a clean version-control state or snapshot exists and
      the revert has been exercised at least once, not merely assumed; (d) the sweep is bounded:
      applied to a subset first, verified, then extended, which is the shard principle scaled
      down to one operator; (e) a post-condition is checked after the sweep, not only a
      pre-condition before it, since the near-miss described in the item was caught by
      inspection rather than by any gate. Condition (a) is decisive and cheap: the same-day
      near-miss would have been caught by it, and its absence is what makes the two rulings
      inconsistent rather than discriminating.
    How to test: Runnable now and largely mechanical. For the specific cleared sweep, re-run its
      matcher in report-only mode over the vault and count matches; if the count exceeds one, the
      presumption is refuted directly on the instance that motivated it. More generally, take the
      last N bulk repairs in the record and, for each, reconstruct the matcher and count matches
      against the corpus as it stood; report the distribution of match counts against the
      intended counts. Any excess is a corrupted site that was not detected. Third test, on
      process: check whether any bulk repair in the record was preceded by a recorded dry-run
      match count. If none was, then determinacy has never been verified in this system and the
      presumption is doing load-bearing work it cannot support.

  Specific risks: If determinacy of target is not sufficient warrant, then (i) the failure mode
    is silent and vault-wide by construction — the whole point of a sweep is that it touches
    everything, so a matcher error is maximally distributed on first execution; (ii) collateral
    edits are far harder to detect than the intended edit is to verify, because the operator's
    attention is on the target and the damage is elsewhere; (iii) the damage is durable in a
    knowledge vault in a way it is not in code, since there is no test suite that fails and no
    compiler that objects — a corrupted wikilink or identifier simply resolves wrongly or not at
    all, and may not surface for months; (iv) the near-miss recorded on the same day establishes
    that the false-uniqueness case is not hypothetical in this system, so the base rate is
    non-zero and unmeasured; (v) the deeper risk is precedent — a rule that cleared one sweep on
    determinacy grounds will clear the next one on the same grounds, and the near-miss did not
    change the rule, which means the system has already demonstrated that this evidence does not
    propagate.

  Mitigations available: (1) Mandatory report-only pass with a match count compared against an
    expected count, as a hard precondition on any vault-wide write — this is the single cheapest
    and highest-value control and directly addresses the demonstrated failure. (2) Diff review
    before commit, even if only a machine check on the shape and count of changed lines. (3)
    Staged application: a subset first, verified, then the remainder — the shard principle at
    C2A2 scale. (4) Guaranteed atomic revert, with the revert path exercised rather than assumed.
    (5) Anchor matchers as tightly as the format permits (whole-token, line-anchored, delimited)
    so that near-identifiers cannot match, which is the specific defect the near-miss exposed.
    (6) Record the match count and the matcher in the run log so that a later auditor can
    reconstruct what was swept and check for collateral damage. (7) Post-condition verification —
    assert an invariant about the vault after the sweep, not only before it.

  Search scope: Comprehensive for industrial large-scale-change practice — Google's LSC/Rosie
    process, Chromium and ChromeOS LSC policy, and Meta's risk-calibrated review automation —
    which is the literature that speaks most directly to the gate this presumption proposes.
    Adequate for automated-refactoring error rates, though the specific figures cited were taken
    from a search summary rather than the paper and are flagged accordingly. Weak on the
    specific question of false-uniqueness in identifier-keyed bulk edits: I searched for
    documented incidents and postmortems of that exact failure and found none, which I record as
    a search limitation rather than as reassurance — this class of incident is typically
    documented internally and not published. Not searched: the database and data-migration
    literature on bulk UPDATE safety and transaction-scoped rollback, and the systematic-review
    literature on mass data correction protocols, either of which would likely add directly
    applicable dry-run and diff-review protocol evidence. Broader search recommended on both.

  Recommendation: CHALLENGED
