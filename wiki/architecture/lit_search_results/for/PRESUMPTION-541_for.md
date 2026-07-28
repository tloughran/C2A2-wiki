SEARCH-FOR-PRESUMPTION-541:
  Date searched: 2026-07-25
  Original item: PRESUMPTION-541
  Original statement: [inferred] A second connected Chrome extension is presumed neutral-or-helpful (redundancy = resilience), but it broke unattended delivery by adding a selection ambiguity requiring a human prompt — a redundant path reduced availability.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-541
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: surfaced from a redundant client that degraded rather than hardened delivery
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Avizienis, A. & Chen, L. (1977/1995). N-version programming. — Redundant versions do not compose into higher reliability for free; ambiguities/omissions in the specification are a dominant source of COMMON-MODE faults, and the combining/arbitration stage is itself a reliability-critical component. A redundant client without an arbitration rule adds a common-mode ambiguity point.
    2. Perrow, C. (1984). Normal Accidents. — Added redundancy raises interactive complexity and coupling; redundant components create new failure modes (spurious activation, selection ambiguity) that can lower overall availability — the "redundancy can reduce reliability" result.
    3. Sagan, S.D. (2004). "The Problem of Redundancy Problem: Why More Nuclear Security Forces May Produce Less Nuclear Security." Risk Analysis 24(4):935-946. — Documents empirically that adding redundant units can DECREASE system reliability via common-mode failure, overcompensation, and social shirking. Direct support for redundancy ≠ resilience.

  Strength of support: Strong

  Summary: The claim that a redundant path can reduce rather than increase availability is a well-established result, not a one-off. Redundancy improves reliability only under conditions — independence of failure modes and a correct arbitration/selection rule. When two clients present without a rule for which one acts, the redundancy introduces a selection ambiguity that is itself a common-mode failure point (here requiring a human prompt), exactly the mechanism Sagan and the N-version literature describe. The specific instance (a second Chrome extension breaking unattended delivery) is a textbook manifestation.

  Caveats: The general engineering default is that well-arbitrated redundancy DOES improve availability; the supported premise is the corrected one — "redundancy without arbitration can reduce availability" — not "redundancy is bad."

  Recommendation: SUPPORTED
