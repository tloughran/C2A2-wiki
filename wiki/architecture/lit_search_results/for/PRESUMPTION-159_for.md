SEARCH-FOR-PRESUMPTION-159:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-159
  Original statement: "'7-day delivery drought broken' presumes sign-in fix is durable root cause; credential-layer workaround framed as architectural-layer fix"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-159
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-126 sign-in-restoration-as-fix without durability audit
      15a: Searched for credential-layer-vs-architectural-layer durability taxonomy in sync failure recovery
    Current status: SUPPORTED

  Sources:
    1. Rasmussen (1997) accident-causation hierarchy / Reason (1990) "Human Error" Swiss-cheese model — distinguishing immediate fixes (credential-layer) from systemic fixes (architectural-layer) is canonical incident-analysis practice.
    2. Allspaw & Robbins (2010) "Web Operations" — credential refresh as a symptomatic fix that masks an underlying architectural fragility is a recognized post-incident-analysis pattern.
    3. Beyer et al. (2016) Google SRE — root-cause-vs-mitigation distinction is enforced in postmortem culture.
    4. C2A2-internal: 7-day drought pattern + PRESUMPTION-134 substrate-decomposition gap.

  Strength of support: Strong

  Summary: Credential-layer-as-architectural-layer-fix confusion is a recognized post-incident-analysis anti-pattern. The presumption correctly identifies that ASSUMPTION-126's "drought broken" claim does not distinguish symptomatic-fix from root-cause-fix. The 7-day duration of the drought is itself a tell that the failure mode is recurrent and substrate-level. Strong support for the inference.

  Caveats: (a) Credential refresh is a legitimate first-line fix; the presumption's concern is durability framing, not the fix itself; (b) Multi-data-point durability test would resolve the question; (c) PRESUMPTION-134 substrate-decomposition is the load-bearing dependency.

  Recommendation: SUPPORTED — credential-vs-architectural distinction is canonical; inference is correct
