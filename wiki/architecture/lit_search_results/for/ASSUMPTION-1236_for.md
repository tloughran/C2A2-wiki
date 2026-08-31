SEARCH-FOR-ASSUMPTION-1236:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1236
  Original statement: "A structurally identical ~300 KB file is clutter, not measurement." (i.e.
    re-running an unchanged method over an unchanged corpus produces no information.)
  Generalizable limb searched: Does repeating a deterministic measurement over an unchanged input
    yield information, and is retaining the duplicate output a net cost?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: UNDER-SEARCHED. Snippet-level results only; 2 queries run (Priority Medium, so no
    Pass 2 query); no full-text reads. Neither query found literature addressing the specific claim.
    The support recorded below is analogical, drawn from the monitoring/alerting literature rather
    than from anything testing the proposition itself.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-1236
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from critique of a repeated artifact produced by an unchanged method over an
           unchanged corpus
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Datadog Engineering, n.d. "Alert Fatigue: What It Is and How to Prevent It." — Practitioner
       source. Defines alert fatigue as arising when a monitoring system produces excessive or
       irrelevant output, diminishing the ability to see critical issues. Supports the "clutter"
       half of the claim: undifferentiated repeated output carries a real attention cost.
    2. Encardio Rite, n.d. "Solving Alert Fatigue in Infrastructure Monitoring." — Snippet gives
       the mechanism concretely: uncoordinated streams overlap and duplicate signals, producing
       multiple alarms for one event; the recommended remedy is consolidation so the system "does
       not send multiple notifications when nothing has changed." That last clause is close to a
       direct statement of the assumption in the monitoring domain.
    3. Cloud monitoring alert-fatigue study, 2024. "Mitigating Alert Fatigue in Cloud Monitoring
       Systems: A Machine Learning Perspective." ScienceDirect (S138912862400375X). — Seen at
       snippet depth only; establishes alert redundancy as a studied problem with measurable
       operational cost rather than a matter of taste.
    4. Information-theoretic literature on redundancy, e.g. Ince and colleagues' line of work on
       partial information decomposition (arXiv:1711.11408, "The identity of information: how
       deterministic dependencies constrain information synergy and redundancy"). — Found, but on
       inspection of the snippet it addresses redundancy *between sources about a target*, not the
       information content of a repeated deterministic observation. NOT usable as support; recorded
       here so that it is not mistaken for support later.

  Strength of support: Weak

  Summary: No literature was found that tests the specific proposition. What exists is a strong and
    well-established analogy in operational monitoring: repeated, non-varying output is treated
    across that literature as a cost rather than a benefit, and the standard remedy — deduplicate,
    consolidate, suppress notifications when nothing has changed — encodes exactly the judgement the
    assumption makes. The formal information-theoretic framing that would settle the matter cleanly
    is trivially true and unhelpful: a deterministic function of unchanged input has zero conditional
    entropy given the previous output, so re-running it transmits no new information *about the
    corpus*. The searches did not find anyone bothering to state this, which is itself weak evidence
    that it is regarded as obvious. The assumption is therefore best described as supported by
    analogy and by an uncontroversial formal point, not by direct evidence.

  Caveats: (a) Under-searched — 2 queries, Medium priority, and neither hit the claim directly.
    (b) The claim is only true under a load-bearing condition it states but does not verify: that
    the method and corpus really were unchanged. A rerun that *establishes* identity is not
    information-free; it is a determinacy check. It transmits nothing about the corpus but something
    about the pipeline. (c) This is precisely where the internal tension with ASSUMPTION-1237 sits,
    and the tension is real rather than apparent. 1237 licenses its deltas by pointing to exact
    reproduction of five hub counts — that is, it treats a null result from an unchanged method as
    evidentially valuable. 1236 treats the same kind of null result as clutter. Both can be held
    only by distinguishing the *fact* of reproduction (informative, cheap, a few numbers) from the
    *artifact* of reproduction (uninformative, ~300 KB retained). The monitoring literature supports
    exactly that resolution: consolidation removes duplicate notifications, it does not stop running
    the check. Recommend the pair be reconciled on those terms rather than one being retracted.
    (d) "Clutter" is a claim about storage and attention cost that no source found here quantifies
    at the ~300 KB scale.

  Recommendation: PARTIALLY-SUPPORTED

  NOVELTY-FLAG:
    Item: ASSUMPTION-1236
    Searched scope: informational value of repeated measurement under an unchanged method;
      replication vs. redundancy in monitoring regimes; information-theoretic treatment of
      deterministic re-observation.
    Finding: No source was located that addresses the proposition directly. The nearest matches are
      (i) operational alert-fatigue guidance, which is about notification volume rather than the
      information content of a repeated measurement, and (ii) partial-information-decomposition
      work, which uses "redundancy" in an unrelated technical sense. The distinction the item
      actually needs — between the informational value of the *fact* of reproduction and the
      disvalue of *retaining* the reproduced artifact — was not found stated anywhere.
    Implication: The item may be locally novel as framed. It is more likely that it is a
      near-tautology in information terms that nobody writes down, dressed as an empirical claim
      about artifact management. Recommend it be restated as the artifact-retention claim it really
      is, which is testable, rather than the information claim, which is trivially true.
    Recommended status: NOVEL (framing-level; low confidence given the under-searched grade)
