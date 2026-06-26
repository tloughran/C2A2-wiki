SEARCH-AGAINST-PRESUMPTION-403:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-403
  Original statement: "That OpenStory capturing its own repair session live is artifact-free observation (no reflexivity in self-logging)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-403
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: self-capture presumed artifact-free
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Hawthorne effect / participant reactivity (NN/G "Hawthorne Effect or Observer Bias"; reactivity meta-analyses). - Observation/measurement changes the observed behavior; a system whose operation is being captured (especially self-captured) is subject to reactivity, so the record is not neutral.
    2. Reflexivity in self-referential measurement. - When the observer and observed are the same system, capturing a repair session injects meta-work into the very corpus it is building - a composition artifact.
    3. Selection/over-representation bias. - A live-captured repair session over-weights maintenance/meta episodes relative to ordinary use.

  Strength of challenge: Moderate

  Summary: "Artifact-free" is contradicted by reactivity and reflexivity findings. Even granting that automated logging is less reactive than overt human observation, self-capture is not neutral: it changes what gets recorded (meta-work over-representation) and, where the act of capturing influences the session, the behavior itself. The corpus built this way is biased toward self-referential repair episodes. The effect is a real but bounded composition artifact, not a fatal flaw - it should be tagged and corrected for, not ignored.

  Specific risks: Corpus over-represents meta/maintenance work; downstream analyses trained/derived from it inherit the skew; self-referential episodes treated as representative.

  Mitigations available: Tag self-referential/meta sessions; weight or exclude them in corpus analyses; track the meta-vs-substantive ratio; prefer capturing ordinary sessions for representativeness.

  STEELMAN:
    Item: PRESUMPTION-403
    Strongest counterargument: Self-logging a repair-of-itself session is doubly non-neutral - reactivity (being captured can shape the session) plus reflexive composition bias (the corpus fills with meta-work) - so "artifact-free" is exactly backwards; the cleanest signal is the one this method least produces.
    What would need to be true for C2A2 to be safe: Self-referential/meta sessions are tagged and de-biased, and representativeness is monitored.
    How to test: Compare meta-work proportion in self-captured vs externally-captured sessions; a gap quantifies the artifact.

  Search scope: Hawthorne/reactivity; reflexivity; selection bias. Comprehensive.

  Recommendation: CHALLENGED
