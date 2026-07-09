SEARCH-FOR-ASSUMPTION-414:
  Date searched: 2026-07-06
  Original item: ASSUMPTION-414
  Original statement: "Shipping the modal with a known minor defect is acceptable for ISME."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-414
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted stated assumption that a known minor defect in the modal does not block the ISME-deadline release
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Yourdon, E., 1995. "When Good Enough Software Is Best." IEEE Software 12(3). — Canonical argument that rationally balancing quality against schedule/cost/functionality is legitimate; "great software today is often preferable to perfect software tomorrow." Directly supports shipping with known rough edges when stakeholders judge benefits outweigh negatives.
    2. Bach, J., 1997. "Good Enough Quality: Beyond the Buzzword." IEEE Computer 30(8). — Frames shipping with bugs as acceptable "as long as you ship with the right bugs"; quality defined as positive consequences acceptably outweighing negatives in stakeholder judgment. Direct support for severity-triaged known-defect releases.
    3. Okumoto, K. & Goel, A.L., 1979/1980. "Optimum release time for software systems based on reliability and cost criteria." Journal of Systems and Software. — Founding paper of the optimal-release-policy literature: release timing is a cost-reliability tradeoff; zero remaining defects is never the optimum stopping criterion. Theoretical grounding that releasing with residual defects is economically rational.
    4. Hunt, A. & Thomas, D., 1999. "Good-Enough Software," The Pragmatic Programmer. Addison-Wesley. — Standard practitioner doctrine: involve users in the tradeoff; ship when quality is good enough for the stakes.
    5. Industry defect-triage practice (e.g., severity-weighted release gates: tens of high-priority defects block release, hundreds of low-priority defects may not; documented "known limitations" with workarounds). — Empirical precedent that severity-classified minor defects routinely ride along in production releases.

  Strength of support: Strong

  Summary: The claim sits on one of the best-established norms in software engineering economics. The "good enough software" literature (Yourdon, Bach, Hunt & Thomas) and the optimal-release-policy literature (Okumoto & Goel and its large successor family) both hold that releasing with known residual defects is rational and normal when defects are severity-triaged and the deadline/benefit side of the ledger dominates. Industry practice institutionalizes this via severity-weighted release gates and published "known limitations" lists. A cosmetic/minor modal defect for a conference demo artifact is squarely inside the class of defects this literature treats as acceptable to ship.

  Caveats: Support presumes (a) the defect really is minor — the severity classification itself was done deliberately, not under deadline-induced optimism (time-pressure studies, e.g., PLOS ONE 2021 laboratory experiment on time pressure and software quality, show triage quality degrades under deadline pressure); (b) key stakeholders (Tom) knowingly accepted the tradeoff; (c) the artifact is not safety- or evidence-critical in the defective region. If the "minor" defect touches the evidential content of the visualization rather than cosmetics, the good-enough framework itself would reclassify it.

  Recommendation: SUPPORTED
