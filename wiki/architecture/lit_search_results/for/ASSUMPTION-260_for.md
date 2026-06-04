SEARCH-FOR-ASSUMPTION-260:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-260
  Original statement: Adding a participant is a single-source operation: one COLORS line + vault files + regen.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-260
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15a: Searched low-friction / plugin-style registration patterns.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Plugin-registry / convention-over-configuration literature (e.g., Fowler on registries) — a single registration entry plus convention-located files is a recognized low-friction extension pattern.
    2. DRY/SSOT (Pragmatic Programmer) — one declaration site for a new entity minimizes the change surface.
    3. C2A2-internal: the documented workflow (extract -> generate -> validate) already supports add-by-regen.

  Strength of support: Moderate

  Summary: One declaration line plus convention-located vault files plus a regen is a clean, low-friction registration pattern in line with registry/DRY practice. For current N it is genuinely a near-single-source operation.

  Caveats: 'Single-source' holds at current scale and assumes the regen and grouping always succeed loudly.

  Recommendation: SUPPORTED
