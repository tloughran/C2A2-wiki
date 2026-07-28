SEARCH-AGAINST-PRESUMPTION-561:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-561
  Original statement: [inferred] Applying Little's Law to the monitor register presumes it IS a queue with a service requirement and an obligatory consumer; if it is a log or watch-list, zero drain is correct and "instability" is a category error whose remedy is retention policy, not consumption.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-561
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a formalism applied to a register whose purpose was assumed rather than specified
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Little, J. D. C. & Graves, S. C. 2008. "Little's Law." In Chhajed, D. & Lowe, T. J. (eds.), Building Intuition: Insights from Basic Operations Management Models and Principles. Springer. — States explicitly that SERVICE is nowhere required or mentioned in Little's Law; the law needs only arrivals, departures and waiting time in a well-defined system. This directly refutes the presumption's premise. L = lambda*W applies to any bounded system with a defined boundary and finite long-run averages, including a log or a watch-list; no service process and no obligatory consumer are presupposed.
    2. Little, J. D. C. 2011. "Little's Law as Viewed on Its 50th Anniversary." Operations Research 59(3): 536-549. — Confirms the generality: the result is independent of arrival and service distributions, number of servers, and queue discipline, and follows from conservation of flow in a stable system. The corollary is the sharp one for C2A2: if departures are zero and arrivals are positive, the system is by definition NOT stable, so L is unbounded and W is infinite. That conclusion is a consequence of the definitions, not an assumption about the register's purpose - so "instability" is not a category error, it is exactly what the law says about a zero-departure register.
    3. EEMUA Publication 191 (Alarm Systems: A Guide to Design, Management and Procurement, 3rd edn.); IEC 62682:2023 / ANSI-ISA-18.2. — The standards governing monitoring registers whose items are precisely watch-items impose per-operator rate limits (EEMUA: ~150 alarms/day likely acceptable, 300/day manageable but demanding) and define alarm flood/overload as more alarms than a single console operator can physically address. In other words: a watch-list DOES have a service requirement, derived from the finite attention of its reader, and unbounded growth degrades it to unusability via alarm fatigue and desensitisation. Reclassifying the register as "a watch-list, not a queue" does not exempt it from a drain requirement; it just relocates the requirement into the reader's capacity.
    4. Kreps, J. / Kleppmann, M. 2015. "Kafka, Samza and the Unix Philosophy of Distributed Data." IEEE Data Engineering Bulletin 38(4); Confluent, "Log Compaction" (Kafka design docs). — Even for the paradigm case of an append-only log, unbounded growth is treated as a defect to be managed, not a design property: retention.ms/retention.bytes and compaction exist precisely because uncontrolled log growth degrades performance and eventually causes failure. So even granting the presumption's reclassification, "zero drain is correct" does not follow - log semantics come with mandatory retention machinery, and the located register has none.

  Strength of challenge: Strong

  Summary: The presumption's central premise is factually wrong: Little's Law does not presuppose a service process or an obligatory consumer. Little & Graves state that service is nowhere required, and Little's 50th-anniversary review confirms the result depends only on conservation of flow in a stable system. Given that, a register with positive arrivals and zero departures is unstable by definition, and calling it unstable is a correct application, not a category error. The reclassification to "log or watch-list" also fails to deliver the exemption it promises: alarm-management standards (EEMUA 191, IEC 62682) impose explicit throughput limits on exactly this kind of monitoring register because operator attention is finite, and the append-only-log literature treats unbounded growth as a defect requiring retention or compaction. The presumption's constructive point - that a terminal state and a consumer should be specified - remains valuable, but its argument for "zero drain is correct" does not survive.

  Specific risks: If C2A2 adopts this presumption, it retires a valid stability metric on a false technical premise and replaces a drain obligation with a retention policy, which would let the register grow while formally compliant. The concrete failure mode is the one the alarm literature names: the register becomes larger than any reader can address, and desensitisation means the items that mattered are never actioned - the register keeps its form and loses its function. The ~174-item backlog with zero consumption since 07-08 (ASSUMPTION-542) is already inside the EEMUA-style overload regime for a single reader.

  Mitigations available: Specify both, not either: (a) a terminal state and a consumer for register items, per the presumption's constructive half; and (b) a rate/size limit and review cadence in the EEMUA/IEC 62682 style, so the register is scored against reader capacity rather than against zero. Report L and W (register size, item age) explicitly - they are computable now and their divergence is the alarm. If genuinely no consumer is intended, then apply log semantics honestly, i.e. add retention/compaction AND stop routing items there that require action.

  STEELMAN:
    Item: PRESUMPTION-561
    Strongest counterargument (against the presumption): Little's Law makes no reference to service at all - Little & Graves say so in the canonical exposition - so the presumption attacks a requirement the formalism does not impose. All the law needs is a system boundary, arrivals and departures; with arrivals positive and departures zero the system is non-stable and residence time diverges, which is precisely the reported instability. Nor does the log/watch-list reclassification rescue "zero drain," because the standards for monitoring registers (EEMUA 191, IEC 62682) set explicit per-operator rate limits on the grounds that reader attention is the service capacity, and even Kafka-style append-only logs require retention or compaction because unbounded growth is a defect. The category error runs the other way: treating an action-bearing register as a log is what licenses unbounded growth.
    What would need to be true for the PRESUMPTION to hold: the register's charter states that items have no terminal state, no reader is expected to act on them, AND a retention or compaction policy bounds its size. Absent all three, the queue reading is the correct one.
    How to test: read 15d's charter and the monitor_queue.md preamble for (i) a named consumer, (ii) a defined terminal state, (iii) any retention rule. Then compute L (current size) and W (median item age since 07-08). If no consumer, no terminal state and no retention rule exist, the register is an unbounded action-bearing list, which both queueing theory and the alarm standards classify as a defect.

  Recommendation: CHALLENGED
