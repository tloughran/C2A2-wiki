SEARCH-AGAINST-ASSUMPTION-451:
  Date searched: 2026-07-13
  Original item: ASSUMPTION-451
  Original statement: "qc_sweep.py's report path keys on the newest pair timestamp and therefore returns 0 across the board — the scripted staleness instrument is fully blind and manual scanning is the sole work source."

  PROVENANCE:
    Origin: 14a
    Chain: 14a -> 15b
    Original item: ASSUMPTION-451
    Item type: ASSUMPTION (stated; QUEUED-EMPIRICAL)
    Transform at each step:
      14a: Extracted from the 2026-07-12 EOD run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. [Vacuity-detection literature (Beer/Ben-David/Eisner/Rodeh lineage; "Robust Vacuity for Branching Temporal Logic," arXiv:1002.4616). — Turned against the claim: the whole point of vacuity DETECTION is that a passing property must be independently interrogated to establish whether the pass was vacuous or genuine. Observing a zero return does not distinguish "the checker is blind" from "there is genuinely nothing stale." The literature supplies the discriminating procedure — a witness/fixture — and C2A2 has not run it.]
    2. [Rothermel, G. & Harrold, M.J. (1997). "A Safe, Efficient Regression Test Selection Technique." ACM TOSEM 6(2). — A claim about which code path a tool takes is settled by reading and exercising the code, not by inferring from its output. The claim is a code-reading claim wearing an empirical costume.]
    3. [Silent-failure literature (Ministry of Testing; observability doctrine) — read against the claim's SECOND clause. — Nothing in this literature supports the leap from "one instrument is blind" to "manual scanning is the SOLE work source." Systems typically have multiple partially-overlapping detection channels, and declaring a single instrument's blindness does not establish the absence of all others. The generalisation is unsupported.]
  Strength of challenge: Moderate
  Summary: The challenge is not to the plausibility of the defect — 15a's hazard-class evidence is strong and I do not dispute it — but to the EVIDENTIAL STATUS of the claim. A staleness scanner returning 0 is consistent with two hypotheses: the instrument is blind, or there is genuinely nothing stale. Observing the 0 cannot discriminate between them, and the vacuity literature's own methodological answer is to construct a WITNESS: feed the checker an input it must flag, and see whether it flags it. C2A2 has asserted blindness without running that fixture. The second clause is weaker still: "manual scanning is the sole work source" is a universal claim inferred from a single instrument's failure, and nothing supports it.
  Specific risks: Low if the claim is true (the fix is a code change). Moderate if the claim is FALSE and acted on: C2A2 would abandon a working instrument in favour of manual scanning, converting an automated detection channel into human labour on the basis of a misdiagnosis — and manual scanning is the channel the operator-absence problem (PRESUMPTION-474 / REVISE-210) has already shown to be unavailable.
  Mitigations available: Run the queued fixture. It is trivial: construct one fresh pair and one deliberately stale pair, invoke the report path, and observe. A single run settles the item permanently in either direction.

  STEELMAN:
    Item: ASSUMPTION-451
    Strongest counterargument: The system has diagnosed an instrument as broken by looking at its readings rather than at its mechanism — which is the same epistemic move it has flagged four times this month under the self-certification family. A 0 return is the reading; the claim is about the cause of the reading; and no amount of staring at 0 distinguishes a blind gauge from a clean process. This matters because the conclusion drawn ("manual scanning is the sole work source") has an operational cost, and it is being paid on the strength of an inference the system's own doctrine forbids.
    What would need to be true for C2A2 to be safe: Either the code has actually been read and the timestamp-keying confirmed at the source level, or a fixture with a known-stale pair has been run and returned 0. Absent one of those, the claim is a hypothesis, not a finding, and should not be labelled a finding.
    How to test: The fixture, exactly as queued: one fresh pair + one stale pair -> invoke report path. Return 0 confirms blindness; return 1 falsifies the claim. Additionally, read the report code path and cite the line. Both are minutes of work.
  Recommendation: PARTIALLY-CHALLENGED
