SEARCH-AGAINST-PRESUMPTION-476:
  Date searched: 2026-07-13
  Original item: PRESUMPTION-476
  Original statement: "An in-run self-caught, self-fixed tool defect needs no independent confirmation — the erring run certifies its own fix and the exoneration of all prior output."

  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-476
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from the 2026-07-12 resolver-defect episode
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Fagan, M. (1976). "Design and code inspections to reduce errors in program development." IBM Systems Journal 15(3). — Formal inspection separates the AUTHOR from independent inspectors precisely because reviewers surface defects the author cannot see; IBM reported 80-90% defect detection. Author-blindness is the founding empirical premise of the entire inspection tradition.]
    2. [Basili, V. & Selby, R. (1987). "Comparing the Effectiveness of Software Testing Strategies." IEEE TSE SE-13(12):1278-1296. — With 32 professionals: code reading by an INDEPENDENT reader detected more faults, at a higher rate, than the author's own functional or structural testing. Direct empirical rebuttal of self-verification adequacy.]
    3. [SLSA v1.0 Build Levels (OpenSSF) and NIST SP 800-218 (SSDF). — The canonical codification that SELF-ATTESTATION IS THE WEAKEST EVIDENCE TIER: SLSA L1 provenance may be self-generated and unsigned and is explicitly described as "trivial to forge"; only L2+ requires provenance signed by a hosted build platform the tenant cannot modify. The software supply-chain community has already had this argument and settled it against the presumption.]
    4. [Metrological traceability: ISO/IEC 17025:2017 cl. 6.5 and the Eurachem-CITAC Guide (2019). — A result is trustworthy only through a documented, unbroken chain of calibrations to an INDEPENDENT reference. An instrument certifying itself has no traceability. This is the presumption's exact anti-pattern, named and prohibited in the measurement standard C2A2's own census work implicitly appeals to.]
    5. [Rothermel, G. & Harrold, M.J. (1997). "A Safe, Efficient Regression Test Selection Technique." ACM TOSEM 6(2):173-210. — SAFETY requires re-running all modification-traversing tests. A fix's correctness says NOTHING about outputs already produced under the defective version; establishing that requires re-executing the corrected tool over the prior inputs. This is the clean logical gap at the heart of the presumption.]
  Strength of challenge: Strong
  Summary: Four independent evidentiary traditions — code inspection, supply-chain attestation, metrology, and regression testing — converge without exception on a single rule: THE ENTITY THAT ERRED CANNOT BE THE SOLE WITNESS TO THE SCOPE OF ITS OWN ERROR. The presumption also silently conflates two distinct propositions: (i) the fix is correct, and (ii) prior output was unaffected. Proposition (ii) does not follow from (i) under any doctrine found in any of these literatures; it is an empirical question, and the only method that answers it is re-execution of the corrected tool over the prior inputs. That C2A2's run caught its own defect is genuinely creditable and should be preserved as a practice. That the same run then certified its own fix and retroactively exonerated all its prior output is a different act entirely, and it has no support anywhere.
  Specific risks: This is the FIFTH member of the self-certifying family (after ASSUMPTION-442, ASSUMPTION-445, PRESUMPTION-471, PRESUMPTION-473) and it operates at the TOOLING layer, beneath all of them — meaning it can silently invalidate the evidence the other four are argued from. If the resolver defect predates the 07-12 run, the entire connectivity series is affected, and the run that would have detected this instead closed the question.
  Mitigations available: Replay the corrected tool over every prior input and diff against the emitted outputs. If diffs are empty, prior output is exonerated BY RE-EXECUTION rather than by assertion. If replay is impossible, prior output must be marked PROVISIONAL, not clean. Additionally: check the resolver's version-control history to date the defect — nearly free, and potentially decisive on its own.

  STEELMAN:
    Item: PRESUMPTION-476
    Strongest counterargument: The presumption survives if and only if (a) the defect's blast radius is provably bounded and mechanically computable — a deterministic tool, a pure function, a clean input/output log — and (b) the self-check that caught it is a genuinely INDEPENDENT ORACLE: an assertion or invariant authored separately from the code path it guards. That distinction is the whole ballgame. An independent invariant catching a bug is not self-review; it is a second, cheaper implementation disagreeing with the first, and the assertion-density literature (Kudrjavets et al. 2006) shows it works. But if the "self-catch" was the same reasoning process noticing its own slip, it is self-review, and Fagan and Basili-Selby say it will miss what it is blind to — which is, definitionally, what it is blind to.
    What would need to be true for C2A2 to be safe: The catch must have come from an independent invariant, AND prior output must be re-derived by replay rather than assumed clean.
    How to test: Replay the corrected tool over every prior input from the affected runs and diff against the emitted outputs. Empty diff = exonerated by re-execution. Non-empty diff = back-correction required. If replay is infeasible, mark prior output provisional and say so in every downstream artifact that consumes it.
  Recommendation: CHALLENGED
