SEARCH-AGAINST-PRESUMPTION-334:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-334
  Original statement: When direct observation is blocked, structural code-path identity is an acceptable substitute for behavioral verification.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-334
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference as the unstated general rule behind ASSUMPTION-301's specific verification claim
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Industry consensus surveys on static vs dynamic verification (e.g., Heicon, "Static analysis and dynamic testing: strengths and weaknesses"; Qt, "Static vs. Dynamic Code Analysis"). — Uniform position: structural/static evidence "has no proof of functional correctness"; runtime behavior (leaks, races, load effects, environment interactions) is only observable dynamically; the two are complements, never substitutes.
    2. Leveson & Turner, 1993. "An Investigation of the Therac-25 Accidents." IEEE Computer. — The defining case study of structural-reuse reasoning standing in for behavioral verification: identical software, new operational context, fatal latent defects that structural identity arguments could not surface.
    3. Lions et al., 1996. "Ariane 5 Flight 501 Inquiry Board Report." ESA. — Code verified in one behavioral envelope was accepted by structural identity into another; the report's core lesson is that verification is a property of code-plus-operational-conditions, not of code alone.
    4. Dijkstra, 1972. "The Humble Programmer." CACM. — "Testing shows the presence, not the absence of bugs"; a fortiori, NOT testing (structural argument only) shows neither — the presumption substitutes an even weaker evidence class for an already-weak one.
  Strength of challenge: Strong
  Summary: As a general epistemic rule (which is what the presumption is — the generalization beneath ASSUMPTION-301), this is directly contradicted by both safety-engineering canon and routine testing practice: behavior is a function of code AND state, inputs, timing, load, and environment, so identity of code underdetermines identity of behavior. The accident literature exists largely because organizations accepted structural-identity arguments when observation was expensive or blocked. The legitimate version of the move — equivalence-class reasoning in test design — explicitly requires demonstrating that the new usage falls inside the verified input/state envelope; the presumption as stated skips that demonstration. "Observation is blocked" lowers the available evidence; it does not raise the evidential value of what remains.
  Specific risks: A norm forms in C2A2 practice where any blocked observation is closable by a structural argument, systematically converting "unverified" into "verified" in the architecture record; verification debt accumulates invisibly precisely in the high-load/unusual-state conditions where observation tends to be blocked and where behavior most differs.
  Mitigations available: Record such items as "structurally argued, behaviorally unverified" (a distinct status, never "verified"); require an envelope-containment argument (inputs/state/load of new context vs verified context) before accepting any equivalence claim; create degraded observation paths (subsampling, logging-based invariant checks, offline recomputation) so "blocked" rarely means "no behavioral evidence at all."
  STEELMAN:
    Strongest counterargument: All practical verification rests on equivalence classes — nobody re-tests every caller of a shared function — and when observation is genuinely blocked, a careful structural argument (pure function, identical types, contained envelope) is the best available evidence and far better than nothing. Refusing to act until direct observation is possible would stall the project; rational practice is graded belief, and the presumption only claims acceptability, not certainty.
    What would need to be true for C2A2 to be safe: Structural arguments are accepted only with explicit envelope-containment reasoning; the path is stateless/pure; acceptance is recorded as provisional and revisited when observation unblocks.
    How to test: Maintain a ledger of structurally-verified claims; when observation later becomes possible, audit the hit rate — any miss calibrates how much trust the rule deserves.
  Search scope: 1 WebSearch ("static analysis cannot replace dynamic testing behavioral verification structural similarity insufficient runtime behavior differs"); plus safety-engineering canon.
  Recommendation: CHALLENGED
