SEARCH-FOR-ASSUMPTION-327:
  Date searched: 2026-06-17
  Original item: ASSUMPTION-327
  Original statement: "A deterministic (reproducible) layout fan is preferable to random jitter for separating co-located 3D nodes."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-327
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the layout-engineering choice — deterministic fan over random jitter
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Layout stability / "mental map" preservation (Misue et al., "Layout Adjustment and the Mental Map") — stable, reproducible layouts across regenerations preserve the viewer's mental map; non-deterministic jitter that moves nodes between runs degrades comparability. Supports determinism for reproducibility.
    2. Reproducibility in scientific visualization — deterministic rendering (fixed seed / fixed rule) is recommended so the same data yields the same picture, enabling diffs, regression tests, and trust. Random jitter defeats reproducibility and validation.
    3. Graphical-perception caution (Cleveland & McGill 1984) — viewers read position as quantitative; both deterministic fans and random jitter risk being over-read, but a deterministic, documented rule at least makes the encoding inspectable and consistent rather than spuriously varying.

  Strength of support: Moderate-Strong

  Summary: Determinism is well-supported for the stated purpose: reproducible layouts preserve the mental map across regenerations (Misue et al.), enable visual diffing/regression testing, and make the separation rule inspectable — all of which random jitter defeats. For merely separating co-located nodes so they are individually resolvable, a deterministic fan is the better-grounded engineering choice. Support is for determinism-over-randomness as a reproducibility/stability property.

  Caveats: Support is for the determinism property, NOT for the assumption that the resulting positions are MEANINGFUL. Both a deterministic fan and random jitter place nodes at locations that carry no data; a stable-but-arbitrary position can be MORE misleading than an obviously-random one because its consistency invites semantic over-reading (couples PRESUMPTION-358: resolvability != fidelity). Recommended companion: mark the fan as incidental/non-semantic.

  Search scope: deterministic vs stochastic layout; mental-map/stability literature; reproducibility in visualization; positional-encoding perception. Comprehensive.

  Recommendation: SUPPORTED
