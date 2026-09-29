SEARCH-AGAINST-ASSUMPTION-1682:
  Date searched: 2026-09-29
  Original item: ASSUMPTION-1682
  Original statement: A finding counts as a proper null hypothesis when the same instrument could observe either outcome.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1682
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run bc6bea9e (FINDING-091 rationale).
      15b: Searched for challenging literature (scheduled run 2026-09-29; sources marked 'search-result level' were not read in full)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Strength: Moderate

  Sources:
    1. Duhem-Quine underdetermination (Quine 1951; Stanford Encyclopedia 'Underdetermination of Scientific Theory'): an instrument 'observing either outcome' does not isolate the hypothesis from auxiliary assumptions, so a null may indict the instrument. (Background knowledge; SERP surfaced secondary summaries only, e.g. philarchive SFECOF-2.)
    2. Lakens et al. 2018 (same source as 15a used, read independently here): 'could observe either outcome' is necessary but not sufficient — an underpowered instrument can 'observe' an effect and still not detect it; absence of evidence is not evidence of absence without power/bounds.

  STEELMAN: the condition is a necessary symmetry test, not a definition. A proper null needs (i) power/sensitivity to a stated smallest effect of interest and (ii) auxiliary assumptions checked. The 'same instrument' wording invites treating any instrument that is capable in principle as adequate in practice.

  SYSTEMIC-RISK: see run note in for_lit_search.md (2026-09-29).

---
SUPPLEMENT — second 15b pass, same date (concurrent-writer collision; appended, nothing above
removed). A separate 15b process wrote the block above while this pass was in progress, and it
overwrote this pass's original file. This pass did NOT read anything in lit_search_results/for/.
Note: the block above says Lakens was the "same source as 15a used", which implies that writer
saw 15a's result. The orchestrator should check that for independence.

SEARCH-AGAINST-ASSUMPTION-1682 (supplement):
  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-1682
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run bc6bea9e (FINDING-091 rationale).
      15b: Searched for challenging literature (lane: falsifiability; severe testing; null-hypothesis design)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Mayo, D. G. (2018). Statistical Inference as Severe Testing. Cambridge University Press.
       [Not fetched; severity definition confirmed via search results (NDPR review,
       philsci-archive notes).] A pass counts as evidence only if it would have been very
       improbable were the hypothesis false. An instrument that can show either result but
       nearly always shows "null" is not a severe test.
    2. Lakens, D. (2017). "Equivalence Tests: A Practical Primer for t Tests, Correlations, and
       Meta-Analyses." Social Psychological and Personality Science 8(4). [Fetched; grep-level read.]
       Without a stated smallest effect of interest and adequate power, a non-significant result
       cannot be read as support for the null. It cites Morey & Lakens (2017, manuscript), "Why most
       of psychology is statistically unfalsifiable".
    3. Duhem–Quine (unverified, background knowledge). A null may reflect a failed auxiliary
       (instrument misconfigured or not run). A positive control is needed.

  Strength of challenge: Moderate

  Summary: "The instrument can register both outcomes" is necessary but not sufficient. A proper
  null also needs (a) adequate sensitivity to a pre-stated effect size, and (b) a demonstration,
  via a positive control, that the instrument does flag the effect when it is present. Without
  these, "null" confounds the effect being absent, too small, or missed through instrument
  failure.

  Specific risks: FINDING-091-type nulls may be logged as properly tested when the instrument had low
    sensitivity or failed silently, and absence of detection is then read as evidence of absence.

  Mitigations available: Positive control per null; stated smallest effect of interest; report "not
    detected at sensitivity X" rather than "absent".

  Search scope: Preliminary: 2 searches, 2 fetch attempts (PMC Bayesian-severity paper blocked by
    reCAPTCHA; not cited).

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1682
  Strongest counterargument: The criterion rules out rigged tests but does not make a null
    informative. On Mayo's severity criterion, a null counts only if the instrument would probably
    have shown the effect had it been there. A two-outcome instrument with 10% sensitivity yields
    "proper nulls" that are 90% likely to be misses.
  What would need to be true for C2A2 to be safe: Instruments behind the relevant nulls have
    flagged a known-positive case, and nulls are stated relative to a detection threshold.
  How to test: Run the FINDING-091 instrument on a seeded positive case. If it misses, reclassify
    the null as "inconclusive".
