SEARCH-FOR-PRESUMPTION-1101 (RE-TRIGGER — 15d 2026-10-11, MONITOR-636, cycle 1; High):
  Date searched: 2026-10-12
  Original item: PRESUMPTION-1101
  Original statement: [inferred] Normative: deferring to the designer is the safe default even when the
    designer is absent. The system assumes escalation is cheap and that the reviewer is live. Refined form
    (15a cycle 0): escalation-to-human designs need a policy for reviewer absence (expiry, default action or
    batching); otherwise queues grow without bound.
  Owed (per 15d block): peer-reviewed or measured evidence on HITL queue behaviour under reviewer absence; or
    in-house backlog data showing growth without a policy (INCORPORATE the refined form).
  Cycle: 1 (RE-TRIGGER by 15d 2026-10-11; processed 2026-10-12)

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-1101
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 2026-09-30 sessions (c2274f26, e5156b86, 496689c2, 9e53c0d9; OPEN-259)
      15a (cycle 0, 2026-10-01): SUPPORTED (Moderate). The sources were practitioner and vendor material
        (TianPan 2026, the SRE book ch. 6, AWS, Cloudflare). No peer-reviewed primary study was found.
      15b (cycle 0): independent; not read by this agent.
      15c: DISPOSITION-1019 -> MONITOR-636 (High; CONTESTED/INDIRECT-EVIDENCE)
      15d: re-triggered 2026-10-11 without evaluating evidence
      15a (cycle 1, 2026-10-12): 3 web searches; 2 fetch attempts (1 abstract read in full, 1 FAILED). This
        cycle targets the peer-reviewed limb only.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: (a) clinical EHR in-basket coverage during physician absence (the closest measured analogue
    of a human review queue whose reviewer is away); (b) audit-log measurement of physician EHR work on paid
    time off; (c) learning-to-defer under expert capacity and availability constraints (ML deferral
    literature). The in-house backlog limb was not examined. That is the 15c/empirical lane.

  Supporting evidence found: Partial. There is peer-reviewed analogous evidence. Nothing directly measures
    an AI-agent escalation queue.

  Sources:
    1. Sinsky, C.A., Trockel, M.T., Dyrbye, L.N., Wang, H., Carlasare, L.E., West, C.P. & Shanafelt, T.D.,
       2024. "Vacation Days Taken, Work during Vacation, and Burnout among US Physicians." JAMA Network Open
       7(1):e2351635. doi:10.1001/jamanetworkopen.2023.51635. [read: full structured abstract via Mayo
       Clinic Pure; full text NOT read; jamanetwork.com fetch FAILED at a captcha]
       Findings:
       - Cross-sectional survey, n=3024.
       - Only 49.1% (1468/2991) had full EHR inbox coverage while on vacation.
       - 70.4% did patient-care tasks on vacation, and 33.1% worked 30 minutes or more per vacation day.
       - Concern about coverage reduced the likelihood of taking more than 3 weeks of vacation (OR 0.30–0.48).
       - Full inbox coverage was associated with lower burnout (OR 0.74).
       Relevance: this is peer-reviewed, measured evidence. Where a reviewer's queue has no absence policy
       (no coverage), the queue does not pause. The work is absorbed by the absent reviewer, or, by
       implication, it waits. That supports the presumption's claim that escalation is not cheap when the
       reviewer is away. Limits: it measures coverage and reviewer load, not queue length or item ageing.
    2. Obermiller et al., 2025. Research letter, JAMA Network Open (EHR audit logs, n=56 primary care
       physicians, Jan 2022–Jul 2023). [search snippet only] Median 16.1 minutes of EHR time per paid-time-
       off day. Activity clustered on the first (57%) and last (63.5%) days of time off. Inbox tasks were
       the largest share (median 39.5%). This is measured, log-based evidence that inbox work queues up
       around reviewer absence and is cleared at its edges. Not verified against the paper.
    3. AMA survey, reported by AMA News ("How one physician group cut its primary care in-basket by 25%").
       [search snippet only] 75% of physicians said the inbox volume waiting on return was a barrier to
       taking time off. Survey only, not a primary measurement.
    4. Alves, J.V., et al., 2024. "Cost-Sensitive Learning to Defer to Multiple Experts with Workload
       Constraints." TMLR 2024 / arXiv:2403.06906. [search snippet and abstract excerpts only] The authors
       state that expert availability changes in real HAIC deployments. They say classical classifier-
       rejector deferral "fails to consider the existence of human work-capacity limitations", and they
       impose capacity constraints at inference time.
       Companion work, also snippets only:
       - FiFAR dataset (arXiv:2312.13218) models an explicit expert "absence rate" per batch.
       - "Online Learning-to-Defer with Varying Experts" (AISTATS 2026) handles experts whose availability
         varies over time.
       Relevance: theoretical and benchmark grounding from the human-AI deferral field. The field treats
       reviewer absence and capacity as first-class design constraints that a deferral policy must handle.
       That is the refined form of the presumption.

  Strength of support: Moderate.
    - Peer-reviewed measured analogue: source 1 (abstract read) and source 2 (snippet).
    - Formal ML literature that names absence and capacity as policy variables: source 4.
    - Queueing theory (arrival rate > service rate implies unbounded queue growth; standard result, cited
      from background knowledge, not fetched) remains the theoretical spine.

  Summary: Cycle 0 relied on practitioner sources. This cycle adds peer-reviewed analogues from two
    directions. Clinical studies measure what happens to a human-review inbox when the reviewer is absent
    and no coverage policy exists: about half of physicians lack coverage, the work is absorbed during or
    around the absence, and coverage is associated with better outcomes. The learning-to-defer literature
    has moved from assuming an always-available expert to modelling capacity limits and expert absence
    explicitly. Both support the refined presumption: an escalation design without an absence policy relies
    on a reviewer who is not reliably there.

  Owed condition: PARTIALLY met. Peer-reviewed, measured evidence was found, but only for analogous human
    queues (clinical inboxes), not for an agent-to-human escalation queue. None of the sources measures
    queue LENGTH growing without bound; they measure coverage gaps and displaced work. The in-house backlog
    limb was not examined.

  Caveats:
    - In clinical inboxes, patient safety pressure forces the absent physician to keep working. C2A2's
      reviewer may simply not engage, which makes unbounded growth more likely than the clinical data shows.
    - Sources 2–4 were read as snippets.
    - The Sinsky associations are cross-sectional.
    - The ML deferral papers use synthetic experts (fraud analysts).

  Recommendation: PARTIALLY-SUPPORTED (Moderate). This adds peer-reviewed analogous support to cycle 0's
    practitioner support. The direct agent-queue measurement is still absent, and the in-house backlog count
    remains the cheapest decisive test.
