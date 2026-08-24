SEARCH-FOR-PRESUMPTION-838:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-838
  Original statement: That a workaround for a missing capability inherits the safety properties of the
    capability it replaces. Three runs substituted host access for an absent mount; all three died there.
    The one run that declined the substitution completed.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that
  workarounds are commonly assumed to inherit the safety properties of what they replace, and that this
  assumption is documented to fail. It is NOT read as support for the presumption being true.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-838
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by sorting the day's mount-affected runs by whether they substituted a host-access
        route, and finding the substitution — not the mount — predicted the outcome. Refines
        PRESUMPTION-834, INCORPORATED by 15c today.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Workarounds Emerging From Electronic Health Record System Usage: Consequences for Patient Safety,
       Effectiveness of Care, and Efficiency of Care." JMIR Human Factors, 2017;4(4):e27. (author list not
       verified) — Peer-reviewed study of EHR workarounds and their consequences, explicitly framed around
       patient-safety outcomes. Establishes workarounds as a studied category with measured negative
       safety consequences, not merely an anecdotal concern.
    2. "Persisting workarounds in Electronic Health Record System use: types, risks and benefits."
       PMC8186102. (author list not verified) — Typology of persisting workarounds with both risks and
       benefits enumerated. Supports the item's specific structure: the workaround is chosen for its local
       benefit while its risk profile differs from the sanctioned path.
    3. Pennsylvania Patient Safety Advisory (2017), "Workarounds: Trash or Treasure?"
       patientsafety.pa.gov. [practitioner safety authority] — States that workarounds used to overcome an
       intentional barrier may bypass "a purposeful and appropriate safety intervention, creating a
       hazardous situation," and that long-term hazards develop when a workaround manages an immediate
       problem without addressing its source. This is close to a verbatim statement of the presumption 14b
       named: the substitute is treated as equivalent when it is not.
    4. Vaughan, D. (1996). *The Challenger Launch Decision*. [established-work] — Normalisation of
       deviance: repeated successful departure from the sanctioned procedure converts the departure into
       the norm without its risk ever having been re-assessed. Theoretical grounding for why the
       substitution persists across runs.
    5. Perrow, C. (1984). *Normal Accidents*. [established-work] — Tight coupling and interactive
       complexity as the conditions under which a locally reasonable substitution propagates into system
       failure. Theoretical grounding for the "all three died there" observation.

  Strength of support: Moderate-to-Strong

  Summary: The healthcare human-factors literature is the best-developed body on exactly this presumption,
  and it supports 14b's diagnosis directly. Workarounds are documented to bypass safety interventions that
  were deliberately placed, to shift rather than remove risk, and to create hazards for parties beyond the
  person performing them; they are also documented to persist because they solve the immediate problem.
  The Pennsylvania Patient Safety Advisory formulation — a workaround overcoming an *intentional* barrier
  and thereby bypassing a purposeful safety intervention — is the same claim as "the substitute does not
  inherit the safety properties of what it replaces." Vaughan and Perrow supply the standing theoretical
  account of why such substitutions persist and why they fail systemically rather than locally. The
  privilege-escalation-as-fallback limb of the search angle is supported only by analogy: the safety
  literature covers barrier bypass generally, not host-access substitution specifically.

  Caveats: The strongest sources are from clinical settings with human operators, embodied barriers and
  regulatory context; transfer to agent runs substituting host access for an absent mount is by analogy.
  The healthcare literature also reports *benefits* of workarounds and treats them as signals of flawed
  process design rather than as operator error — which cuts against a purely prohibitive reading of this
  presumption. The item's own evidence base is n=4 runs (3 failed, 1 succeeded); no source supports
  inferring a rate from that, and the correlation could be confounded (runs that attempted the
  substitution may have differed in other ways). Search scope: moderate — covered healthcare workarounds
  and classic safety theory; did NOT cover the security literature on privilege escalation as an
  operational fallback, which is the most direct analogue and remains unsearched.

  Recommendation: SUPPORTED
