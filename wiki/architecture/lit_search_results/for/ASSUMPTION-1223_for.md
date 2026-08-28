SEARCH-FOR-ASSUMPTION-1223:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1223
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High)
  Original statement: A keyword-triggered escalation filter can invert — systematically holding the
    highest-value items — because item value and the trigger token co-occur. Precision reported as 1-of-17.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1223
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim; the 1-of-17 precision figure carried as stated, not independently recounted.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-28, one dedicated query on keyword triage precision/recall and
    escalation-classifier false negatives. Literature reached: scikit-learn's precision-recall
    documentation for the threshold trade-off; two arXiv papers on customer-support escalation prediction
    (Montgomery et al. line of work at IBM); one arXiv paper on alarm-burden metrics; one 2026 arXiv
    paper defining a Triage Efficiency Score. NOT COVERED and material: (i) the information-retrieval
    literature on Boolean/keyword query failure, which is the closest match to the mechanism claimed;
    (ii) any study that measures the specific inversion — correlation between item value and trigger-token
    presence — which is the actual content of the assumption and which I did not find addressed anywhere.
    All sources SNIPPET-ONLY. Search confidence: MODERATE on the surrounding trade-off, LOW on the
    inversion mechanism.

  Supporting evidence found: Partial

  Sources:
    1. scikit-learn developers, "Precision-Recall" (v1.9.0 documentation) [SNIPPET-ONLY]
       https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html —
       Establishes the threshold trade-off: raising the bar for a positive prediction raises precision and
       lowers recall. A filter tuned to fire rarely will hold items it should pass.
    2. Montgomery, L. et al., "Customer Support Ticket Escalation Prediction using Feature Engineering"
       (arXiv:2010.06145) and "Escalation Prediction using Feature Engineering: Addressing Support Ticket
       Escalations within IBM's Ecosystem" (arXiv:2010.06390) [SNIPPET-ONLY; authors partially unverified] —
       Reports that industrial stakeholders explicitly prefer high recall in escalation settings: missing a
       critical case is costlier than over-attending a benign one. Supports the assumption's implicit claim
       that a precision-optimised escalation filter is mis-specified for the objective.
    3. Anon., "ALTIS: Automated Loss Triage and Impact Scoring…" (arXiv:2603.13803) [SNIPPET-ONLY;
       authors unverified] — Defines a Triage Efficiency Score that jointly rewards inspection reduction
       and *recall of high-severity items*, penalising false-positive dispatch. Documented recognition that
       triage must be scored against severity, not volume.

  Strength of support: Moderate

  Summary: The surrounding claim is well supported: escalation triage is a recall-dominant problem, the
    precision/recall trade-off is monotone in the trigger threshold, and the practice literature has moved
    toward severity-weighted triage scores precisely because volume-weighted ones misprice the rare
    important case. What is *not* supported by anything found is the assumption's distinctive content —
    that value and the trigger token co-occur, producing a systematic inversion rather than ordinary
    imprecision. No study addressing that mechanism was located. The supportive verdict is therefore for
    the frame, not the finding.

  Caveats: Two of three sources are unreviewed arXiv preprints with unverified author lists. The 1-of-17
    figure was neither recounted nor evaluated by this direction.

  Recommendation: PARTIALLY-SUPPORTED
