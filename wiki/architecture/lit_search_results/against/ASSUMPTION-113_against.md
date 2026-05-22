SEARCH-AGAINST-ASSUMPTION-113:
  Date searched: 2026-05-13
  Original item: ASSUMPTION-113
  Original statement: "Markup-anchor diagnostic for transcript-availability watches (transcript-toggle + timecode + speaker labels) as canonical default method; substring count of 'transcript' produced false positives at 2026-05-05 first check"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-113
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-12 EOD Agent 16 first-resolution-cycle method-fix attribution
      15b: Searched for counter-evidence on speaker-label coverage on non-Carroll-style podcast transcripts; markup-anchor brittleness
    Current status: PARTIALLY-CHALLENGED

  Sources:
    1. Hochheiser & Shneiderman (2001) — UI-control presence is platform-specific; the same canonical observation that supports markup-anchor detection also makes it platform-brittle. Diagnostics that work for YouTube transcripts will not work for Spotify, Apple Podcasts, RSS-feed-hosted transcripts, or podcaster-hosted sites.
    2. Ferreira et al. (2014) "Detecting evolution in web content" — web markup undergoes silent updates; markup-anchor detectors degrade over time without active maintenance.
    3. Many podcasts publish transcripts without speaker labels (interview podcasts vs. monologue podcasts have systematically different transcript-format conventions); the speaker-label requirement is an overfitted feature from the C2A2 thinker corpus (Carroll, Wright, Fredrickson style transcripts).
    4. Wheeler (2000) "Understanding Variation" — generalizing from N=1 (one resolution episode) to "canonical default method" is N-too-low; the marker switch fixed the one observed false positive but generalization to all transcript-availability watches is unsupported.
    5. C2A2-internal: PRESUMPTION-143 (this cycle, paired) — single-instance success conflated with protocol validation; the same conflation operates here for method canonicalness.

  Strength of challenge: Moderate

  Summary: The challenge is moderate. Markup-anchor detection is canonical in principle but platform-brittle in practice; speaker-label requirement is overfitted to the C2A2 thinker corpus and will produce systematic false negatives on monologue podcasts and on platforms that don't markup speakers. The "canonical default method" framing extrapolates from N=1 to method-level claim, which SPC discipline does not support. The method-switch is correct for the one episode but is not validated as default.

  Specific risks: (a) Method canonization based on N=1 episode produces systematic false negatives on platforms outside the diagnostic's scope; (b) Speaker-label requirement excludes monologue podcasts (Lex Fridman solo, Sean Carroll mindscape solo, Donald Hoffman solos) that may publish transcripts without speaker labels by construction; (c) Markup-anchor brittleness: YouTube UI changes silently — the diagnostic must be maintained; (d) Conflating method-correctness with protocol-validation (joint with PRESUMPTION-143).

  Mitigations available: (a) Reframe as "preferred method pending cross-platform validation"; (b) per-platform diagnostic suites (YouTube-specific, Spotify-specific, podcaster-site-specific); (c) explicit fallback chain (markup-anchor → substring-with-context → human-verify); (d) maintenance schedule for markup conventions.

  Recommendation: PARTIALLY-CHALLENGED (Moderate) — method is principled; "canonical default" overstates at N=1 and the speaker-label feature is corpus-specific

  STEELMAN:
    Item: ASSUMPTION-113
    Strongest counterargument: Markup-anchor detection is canonical in web-IR, but the specific three-feature triad (toggle + timecode + speaker-labels) was tested on one episode. Speaker-labels in particular are a podcast-format convention, not a transcript-availability marker — multiple high-value targets in the C2A2 corpus publish transcripts without speaker labels, so the diagnostic will systematically miss them. "Canonical default" elevates a one-episode pattern to method-level commitment; the conservative move is to characterize this as the preferred YouTube-with-multi-speaker pattern pending broader cross-platform validation.
    What would need to be true for C2A2 to be safe: (a) Test the triad on ≥5 distinct platforms / transcript-format combinations; (b) test on monologue podcasts to verify speaker-label fallback; (c) document failure modes for non-triad transcripts.
    How to test: Apply the diagnostic to a sample of 20 transcripts spanning platforms and formats; measure precision and recall.
