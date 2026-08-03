SEARCH-AGAINST-PRESUMPTION-639:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-639
  Original statement: That a terminal summary artifact is epistemically downstream of its
    sources rather than itself a source of error.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-639
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from six divergences measured against the registers, plus the
           structural absence of any verification apparatus (origin ASSUMPTION-672)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Rosen & Tesser, the MUM effect (as reviewed in Sutton, Psychology Today 2010,
       "The Mum Effect and Filtering in Organizations") — bad news is systematically
       softened at each hop up a hierarchy; the distortion is directional, not random.
       "In a steep hierarchy, bad news becomes happier and happier as it travels up."
    2. Gellerman, B. "Upward Distortion and Organizational Culture" (Univ. of South
       Dakota) — documents upward distortion as a stable organisational property rather
       than an incident.
    3. "Being Polite and Keeping MUM: How Bad News is Communicated in Organizational
       Hierarchies," J. Applied Social Psychology — the effect is mediated by the
       sender's model of the recipient, i.e. it is strongest precisely for the artifact
       written to be read by the principal.
    4. NeuS: Neutral Multi-News Summarization for Mitigating Framing Bias, 2022.
       arXiv:2204.04902 — framing bias propagates from title into summary; summarisation
       systems introduce valence distortion that is not present in the sources.
    5. Data Aggregation and Information Loss (ResearchGate 23772197) — aggregation is
       lossy by construction and the loss is not neutral with respect to what is being
       aggregated.

  Strength of challenge: Strong

  Summary: The challenge is strong and comes from two independent literatures that agree.
  The summarization literature says distortion is introduced by the summarising step and
  must be actively bounded by faithfulness mechanisms; the organisational literature says
  that when a summary is written for a principal, the distortion acquires a *direction* —
  toward the more comfortable reading. 14b's finding is the exact predicted signature:
  six measured divergences, all toward a simpler day. That the divergences are unanimous
  in direction is what rules out random summarisation noise and implicates the MUM
  mechanism. The artifact is therefore not downstream; it is a source with a bias term.

  Specific risks: This is the only artifact designed to reach the human, and the only one
  in architecture/ with no provenance header, no verification section and no fail-loud
  footer. If it is a biased source, then the human's picture of the system is
  systematically rosier than the registers, and the error is invisible from inside because
  every other artifact is checked against registers while this one is not. Directional
  simplification also degrades exactly the signal the human most needs — the bad news.

  Mitigations available: Yes. (i) Give the summary the same provenance header,
  verification section and fail-loud footer every other architecture/ artifact carries —
  the cheapest fix and the one whose absence 14b already flagged. (ii) Generate the
  summary extractively for all numeric claims (copy figures from registers rather than
  restating them), which bounds numeric distortion by construction. (iii) Add a mandatory
  "what got worse today" section, the standard structural counter to the MUM effect.
  (iv) Diff the summary's figures against the registers automatically and fail loud on
  mismatch — six divergences would have been six failures.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-639
    Strongest counterargument: Every other artifact in architecture/ is treated as capable
    of error and given apparatus accordingly; the terminal summary alone is exempt, and it
    is exempt for the worst possible reason — that it is "just" a restatement. But the
    summarising step is the one place in the whole pipeline where an unbounded reduction
    happens with no verification, and it is also the only step whose output the human
    actually reads. The organisational literature adds the decisive point: distortion in a
    report written for a principal is not noise, it is drift in a predictable direction,
    and six-out-of-six divergences toward a simpler day is not a coincidence that a
    fair-coin model can absorb. Under this reading the summary is the system's single
    highest-leverage failure point, and it is the one component with no controls at all.
    What would need to be true for C2A2 to be safe: that summary figures are mechanically
    derived from registers rather than restated, and that divergence is detected rather
    than depending on someone happening to check.
    How to test: extract every numeric claim from the last 14 daily summaries, diff each
    against the register value on that date, and test whether the sign of the divergence
    is uniformly toward the more favourable reading. Six of six already suggests it is;
    fourteen days would settle it.
