SEARCH-FOR-PRESUMPTION-262:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-262
  Original statement: [inferred] The 2026-05-18 truncation diagnosis was complete; today's recurrence = "fix-unimplemented" rather than "diagnostic-incomplete"; alternative reading (multi-causal-path bug; one patched, another active) not separately considered.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-262
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from "diagnosis stands" framing without re-investigation.
      15a: Searched for supporting literature on when "recurrence = fix-absence" framing is the right first reading.
    Current status: PARTIALLY-SUPPORTED (Weak)

  Supporting evidence found: Yes (weak)

  Sources:
    1. Allspaw (2012) "Blameless PostMortems" — when a fix is documented but unimplemented, recurrence is straightforwardly attributable to the unimplemented fix; this is a common case in incident triage.
    2. Beyer et al. (2016) SRE — single-cause attribution is the dominant first-pass diagnostic stance in low-complexity systems; only escalated to multi-cause investigation under specific triggers.
    3. Cockburn (2006) Agile Software Development — pragmatic stance: "the simplest explanation that fits the evidence" supports starting with the unimplemented-fix hypothesis when no contradicting evidence is present.
    4. C2A2-internal: 2026-05-18 diagnosis remains coherent with the 2026-05-27 recurrence pattern; no contradicting evidence has been collected.

  Strength of support: Weak

  Summary: The "recurrence = fix-absence" framing IS the right FIRST reading in incident-response literature when (a) the diagnosis is documented, (b) the fix is documented as unimplemented, and (c) the recurrence pattern matches the original diagnosis. The C2A2 case meets all three. However, the support is "right first reading" — not "right complete reading."

  Caveats: (a) Literature explicitly recommends second-look re-investigation on recurrence even when the unimplemented-fix hypothesis fits; (b) the support is for single-cause-as-first-pass, not single-cause-as-complete; (c) Cook & Woods (1994) "second story" framing warns that simple single-cause framings can obscure multi-causal patterns; (d) the presumption is specifically about NOT separately considering the multi-cause alternative — this absence is what 15b will challenge.

  Recommendation: PARTIALLY-SUPPORTED (Weak) — first-reading is defensible; complete-reading framing is not.
