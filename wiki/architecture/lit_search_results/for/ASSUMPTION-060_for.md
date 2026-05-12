SEARCH-FOR-ASSUMPTION-060:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-060
  Original statement: "Read-only observation of still-running specialist sessions is the correct default (natural-termination precedent from 2026-04-19 Levin-Friston)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-060
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from evening sync autonomous-choices note citing Levin-Friston precedent
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Non-intervention / observational-first literature (Beyer 2016 SRE "incident response" on gather-then-act; medical-ethics non-maleficence patterns): observation before intervention is a recognized safety principle. "Read-only first" avoids creating cascading failures that an intervention might cause.
    2. Natural-termination design patterns (long-running-process literature; Unix process-management traditions on "let it exit cleanly"): processes with no external blocking dependencies often terminate on their own trajectory; premature intervention discards work-in-progress and creates restart costs.
    3. Precedent-based decision-making in operational settings (Schön 1983 "The Reflective Practitioner"): applying prior-case precedent when facing a new instance is a legitimate heuristic for novel situations. The Monday Levin-Friston precedent is a data point, even if only one.
    4. Non-interference literature in multi-agent systems (Russell & Norvig 2020 AI textbook on cooperative agents): one agent intervening on another's execution without clear authority creates coordination hazards. Read-only observation preserves the coordination contract.

  Strength of support: Weak-to-Moderate

  Summary: The "observe before intervene" stance has general support from incident-response practice, Unix process-management traditions, and multi-agent coordination literature. Single-precedent application in novel operational situations is a recognized (if imperfect) heuristic. Read-only observation avoids coordination hazards and preserves work-in-progress. However, support is weaker for elevating a single precedent to a default policy — the literature endorses caution, not precedent-canonization.

  Caveats: (a) Single-precedent generalization is methodologically fragile — one successful natural-termination does not establish that natural-termination generally works; (b) the stance is in direct tension with candidate DECISION-024 (turn-cap default = 20) drafted the same day — two different stances on the same question; (c) "read-only" is compatible with escalation and signaling; the claim does not preclude those.

  Recommendation: PARTIALLY-SUPPORTED (general pattern endorsed; single-precedent elevation to default is weakly supported; internal tension with candidate DECISION-024)
