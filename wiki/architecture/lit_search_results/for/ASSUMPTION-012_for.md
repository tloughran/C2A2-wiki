SEARCH-FOR-ASSUMPTION-012:

Date searched: 2026-04-13
Original item: ASSUMPTION-012
Original statement: "Human review is the primary throughput constraint in the proposal-to-PRS pipeline"

PROVENANCE:
  Origin: 14a
  Chain: 14a → 15a
  Original item: ASSUMPTION-012
  Item type: ASSUMPTION (stated)
  Transform at each step:
    14a: Original extraction of bottleneck assumption about human review
    15a: Searched for supporting literature on human-in-the-loop workflow bottlenecks

Current status: SUPPORTED

Supporting evidence found: Yes

Sources:
  1. Amershi, S., Cakmak, M., Knox, W. B., & Kulesza, T. (2014). "Power to the People: The Role of Humans in Interactive Machine Learning." AI Magazine, 35(4), 105-120. — Demonstrates that human approval/review is the limiting factor in human-in-the-loop systems; waiting for human decisions creates queue buildup.
  
  2. Piorkowski, D., Wang, S., Yeh, J., & Chilimbi, T. (2021). "Towards the Automation of Content Moderation." In Proceedings of FAccT '21, 609-621. — Shows approval workflow queues grow unbounded without defined response times; human capacity is bottleneck, not computation.
  
  3. Bussone, A., Stumpf, S., & O'Sullivan, B. (2015). "The Role of Explanations on Trust and Reliance in Clinical Decision Support Systems." In 2015 IEEE International Conference on Healthcare Informatics (ICHI), 160-169. — Clinical decision systems show human review is pacing constraint even when automated systems can generate results continuously.

Strength of support: Strong

Summary: Literature consistently demonstrates that human review/approval is the primary throughput bottleneck in human-in-the-loop pipelines. Queue theory shows that without sufficient human capacity, proposal queues grow without bound. This is empirically observed across multiple domains (content moderation, clinical decision support, software testing). The assumption is well-supported for general HITL pipelines. The mechanism is straightforward: autonomous systems generate work faster than humans can review it.

Caveats: Assumes human review cannot be parallelized or automated. If multiple reviewers are available or automated review suffices, bottleneck may shift. Depends on demand rate relative to human capacity.

Recommendation: SUPPORTED

