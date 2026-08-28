SEARCH-FOR-ASSUMPTION-1231:
  Date searched: 2026-08-28
  Original item: ASSUMPTION-1231
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority Medium)
  Original statement: A queue cleared by hand will refill, because the arrival rate is unchanged and the
    server is an intermittently available human. Pinned to measured baseline pending=0 at 2026-08-27,
    scoreable 2026-09-10.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1231
    Item type: ASSUMPTION (stated prediction)
    Transform at each step:
      14a: Extracted verbatim and pinned to a measured baseline with a scoring date.
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-28, one dedicated query on Little's law, backlog clearance and WIP
    limits. Literature reached: Kanban Tool's queuing-theory guide, Kanban Zone and Businessmap on Little's
    law, two arXiv queueing papers (1206.0720 fluid/diffusion limits; 1811.09576 finite-pool heavy traffic).
    NOT COVERED and material: the queueing-with-vacations literature, which is the exact formal model for an
    intermittently absent server and which the queue entry gestures at; and Little & Graves in primary form.
    All sources SNIPPET-ONLY. Search confidence: MODERATE.

  Supporting evidence found: Yes

  Sources:
    1. Kanban Tool, "Queuing Theory & Kanban" [SNIPPET-ONLY]
       https://kanbantool.com/kanban-guide/queuing-theory ; Businessmap, "What Is Little's Law?"
       [SNIPPET-ONLY] https://businessmap.io/continuous-flow/littles-law —
       Give the relation L = λW and the operative consequence: where arrival rate exceeds service rate a
       queue forms, and a correctly chosen WIP limit is what binds the system. Clearing L without touching
       λ or the service process leaves the relation that generated L intact.
    2. Kanban Zone, "Little's Law" [SNIPPET-ONLY] https://kanbanzone.com/resources/lean/littles-law/ —
       States the steady-state precondition explicitly, which is the honest boundary on the prediction.
    3. Anon., "An alternative approach to heavy-traffic limits for finite-pool queues" (arXiv:1811.09576)
       [SNIPPET-ONLY; authors unverified] — Cited only to record that heavy-traffic behaviour of queues with
       a bounded population is a studied regime; not used as evidence for the prediction.

  Strength of support: Moderate

  Summary: The prediction follows from the most standard result in queueing, and the literature states it in
    the form the assumption needs: work-in-progress is determined by arrival rate and time-in-system, so
    emptying the queue by hand changes the instantaneous count and nothing that produced it. Practitioner
    Kanban guidance makes the same point as its central argument for WIP limits over periodic clean-ups. The
    support is theoretical rather than empirical — no study of a hand-cleared review queue with an
    intermittent human server was located — and the same sources supply the precondition (steady state) that
    the against direction will press on.

  Caveats: All sources are practitioner-facing explainers of a textbook result; none measures this regime.
    The prediction is dated and falsifiable in-house on 2026-09-10, which is a better test than anything
    this search can supply.

  Recommendation: SUPPORTED
