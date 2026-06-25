SEARCH-AGAINST-ASSUMPTION-353:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-353
  Original statement: "Usefulness != productivity; the test must be asymmetric - FAIL strong/clean, PASS only necessary-condition-met (provisional)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-353
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a firewall against productivity-ism/Goodhart; discharges REVISE-105
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: Partial

  Sources:
    1. Biagioli & Lippman (eds.) 2020, 'Gaming the Metrics.' - Meta-gaming: even well-designed asymmetric tests can be gamed at the level of the test itself, so asymmetry is not a complete firewall.
    2. Manheim & Garrabrant 2018. 'Categorizing Variants of Goodhart's Law.' - Several Goodhart mechanisms (adversarial, regressional) survive asymmetric/necessary-condition framing.

  Strength of challenge: Weak

  Summary: No challenge to the core distinction (usefulness != productivity) or to the value of asymmetric testing was found; both are well supported. The only qualification is that asymmetry is not a COMPLETE firewall against Goodhart: necessary conditions can be satisfied vacuously and the test design itself can be meta-gamed. This narrows the claim's scope rather than refuting it.

  Specific risks: Treating the asymmetric test as a complete anti-Goodhart firewall could let vacuous necessary-condition PASSes or meta-gaming slip through.

  Mitigations available: Periodically red-team the test itself; vary/secret-hold thresholds; treat necessary-condition PASS as provisional (as the assumption already does).

  STEELMAN:
    Item: ASSUMPTION-353
    Strongest counterargument: Asymmetric necessary-condition testing blunts but does not eliminate Goodhart; an adversary can satisfy the necessary condition without delivering usefulness, so the firewall framing risks overconfidence.
    What would need to be true for C2A2 to be safe: The necessary conditions are tight enough that satisfying them genuinely entails (not merely permits) usefulness, and the test is periodically red-teamed.
    How to test: Attempt to PASS the test while contributing no real usefulness; if achievable, tighten the necessary conditions.

  Search scope: Goodhart variants; meta-gaming. Adequate.

  Recommendation: NO-CHALLENGE-FOUND
