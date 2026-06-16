SEARCH-AGAINST-PRESUMPTION-351:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-351
  Original statement: "[inferred] A visible gap-marker is an understood gap (visibility = comprehension)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-351
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated comprehension premise beneath ASSUMPTION-320
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Graphical-perception / encoding-comprehension literature (Cleveland & McGill 1984; time-series viz review arXiv:2507.14920). — Comprehension depends on whether the encoding maps to a learned/perceptual operation; a NOVEL or custom gap encoding is not self-explanatory. Visibility (the marker is on screen) and comprehension (the viewer infers "no data here, and why") are distinct; the review explicitly warns gaps can "bring more noise than signal," i.e., be seen but misread.
    2. Legend/convention discoverability (information-visualization usability). — Bespoke conventions require a legend or annotation to be decoded; without it, viewers default to familiar readings (a gap looks like zero, or like the end of the series, or like a rendering glitch). The marker's mere presence does not carry its meaning.
    3. C2A2 trace-vs-substance family (project-internal pattern; couples PRESUMPTION-322/345). — This is the same failure class the project has repeatedly flagged: the existence of an artifact (here, a gap-marker) is presumed to deliver the function (here, understanding), when the artifact's presence and its effect are separate facts that must be separately verified.

  Strength of challenge: Moderate-Strong

  Summary: The presumption is challenged: a visible gap-marker is not self-interpreting. Graphical-perception research ties comprehension to learned encodings, and a custom gap convention has no such learning behind it; without a legend/annotation, viewers commonly misread a gap as zero, as series-end, or as a glitch. This is a specific instance of the project's recurring trace-vs-substance error — presence of the marker presumed to equal delivery of understanding. As a PRESUMPTION, "visibility = comprehension" is an unexamined leap that the visualization literature directly denies.

  Specific risks: The Metabolism view's honest gaps (correctly preferred per ASSUMPTION-320) are misread — a capture-artifact gap (PRESUMPTION-352) read as "I did nothing," or a true-inactivity gap read as a glitch — so the integrity gained by showing the gap is lost at the comprehension step. The user draws wrong conclusions from a technically-honest chart.

  Mitigations available: Annotate gaps with their reason (inline label or tooltip: "no capture — instrumentation gap" vs "no activity"); include a legend defining the gap convention; comprehension-test the convention on a naive viewer; where the gap's cause is known (artifact vs real), encode the two differently so they are not conflated (couples PRESUMPTION-352).

  STEELMAN:
    Strongest counterargument: The audience is a single expert user (the builder) who already knows the convention, so for THIS dashboard visibility may effectively equal comprehension — the comprehension gap is real for general audiences but near-zero for a sole, informed viewer. Demanding legends/comprehension tests for a personal tool may be over-engineering.
    What would need to be true for C2A2 to be safe: Either the sole viewer reliably remembers the convention's meaning (including months later, and including the artifact-vs-real distinction), or the gaps carry an inline reason so comprehension does not depend on recall. Given PRESUMPTION-352's open artifact-vs-real ambiguity, even the expert viewer cannot read cause from a bare gap.
    How to test: Show the builder their own chart after a delay and ask them to state, per gap, whether it is a capture artifact or real inactivity; inability to do so from the marker alone confirms visibility ≠ comprehension even for the expert.

  Search scope: Graphical-perception comprehension, encoding/legend discoverability, trace-vs-substance pattern. Comprehensive.

  Recommendation: CHALLENGED
