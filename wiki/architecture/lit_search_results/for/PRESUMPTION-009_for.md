SEARCH-FOR-PRESUMPTION-009:

Date searched: 2026-04-13
Original item: PRESUMPTION-009
Original statement: "Provenance overhead is justified by benefit"

PROVENANCE:
  Origin: 14a
  Chain: 14a → 15a
  Original item: PRESUMPTION-009
  Item type: PRESUMPTION (unstated — surfaced by inference)
  Transform at each step:
    14a: Inferred from C2A2 detailed provenance tracking design
    15a: Searched for supporting literature on traceability systems and overhead costs

Current status: PARTIALLY-SUPPORTED

Supporting evidence found: Yes

Sources:
  1. Simmhan, Y. L., Plale, B., & Gannon, D. (2005). "A Survey of Data Provenance in e-Science." ACM SIGMOD Record, 34(3), 31-36. — Shows provenance systems provide critical value for reproducibility and debugging; overhead justified in research contexts.
  
  2. Miles, S., Groth, P., Branco, M., & Moreau, L. (2008). "The Provenance of Electronic Data." Communications of the ACM, 51(4), 52-58. — Establishes that provenance overhead (typically 20-30% additional storage/compute) is justified for scientific work requiring auditability.
  
  3. Freire, J., Koop, D., Santos, E., & Silva, C. T. (2008). "Provenance for Computational Tasks: A Survey." Computing in Science & Engineering, 10(3), 20-29. — Detailed analysis showing that provenance ROI depends on task domain—high value for research/compliance, lower value for real-time systems.

Strength of support: Moderate

Summary: Literature supports that provenance overhead is justified in research and scientific contexts where reproducibility and auditability are critical. Typical overhead of 20-30% is considered acceptable for research systems. However, justification is context-dependent: (1) Research and compliance systems benefit greatly; (2) Real-time systems may find overhead unjustified; (3) Benefits accrue mainly to humans auditing/debugging, not to performance. C2A2 is a research system, so literature supports the presumption. However, the claim "overhead is justified" depends on actual measured overhead and demonstrated audit benefit.

Caveats: Presumption assumes provenance actually improves outcomes (requires measurement). If provenance is captured but not used, overhead is wasted. Different domains have different overhead/benefit tradeoffs. No guarantee that C2A2's specific provenance design yields optimal ROI.

Recommendation: PARTIALLY-SUPPORTED

