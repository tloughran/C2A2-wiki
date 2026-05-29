---
title: Single-Source Participant Registration
pathway_id: participant_registration
status: pinned
created: 2026-05-29
depends_on: []
enables: [universal_search_and_ask, portability_toolkit, apprentice_mode]
isme_critical: no
---

# Pathway 28: Single-Source Participant Registration

## Purpose

Adding a participant to the system — a new thinker/tradition today, a whole new community tomorrow — should be a single declarative act that propagates to every surface automatically, with no per-surface editing and no silent partial states. This pathway names that principle, records where it already holds, and marks where it is still manual or fails quietly.

## The realized mechanism (Sociogram, 2026-05-29)

The Sociogram's entire tradition/structure vocabulary fans out from one Python dict, `COLORS`, in `generate_visualization.py`:

`COLORS` → `tradition_groups` / `structure_groups` (built once, applying `LABEL_OVERRIDES` for friendly spelling) → injected as the JS arrays `TRADITION_GROUPS` / `STRUCTURE_GROUPS` → consumed by **every** group-aware surface:

- node coloring (`get_group()` maps a file's directory to a `COLORS` key);
- the left-panel filter checkboxes and the `groupVisibility` map (`buildFilters()`);
- the focus typeahead (navigation increment 1.5) and `resolveGroupKeys()` label resolution.

The checkboxes and the typeahead are therefore *siblings of one source*, not parent-and-child — they cannot drift apart. Verified this session: the typeahead reads the identical array `buildFilters()` reads.

## What adding a participant costs today

1. **One line in `COLORS`** — e.g. `'traditions/chalmers': '#7E6BA8'`. This is the real registration and is mandatory.
2. **Optional `LABEL_OVERRIDES` entry** when the auto-label (last path segment, title-cased) is wrong — e.g. `arkanihamed` → "Arkani-Hamed", `mcgilchrist` → "McGilchrist".
3. **Vault files under her directory** (`traditions/chalmers/…`) so she has actual nodes; `extract_vault_data.py` derives `node.group` from the directory.
4. **Regen** (`regen_sociogram.sh`) — everything is baked at generation, so both the checkbox and the dropdown pick her up together.

## Why it matters for C2A2 as a whole

The project is an accelerator/detector for *traditions* — new communities are meant to join cheaply and often. A single-registration discipline is the difference between onboarding a tradition being a one-line act versus a multi-surface chore that drifts out of sync. The same principle should govern every config-like taxonomy across the explorer (disciplines, structure groups, PRS axes). It is the registration/provenance counterpart to Pathway 27's retrieval-side `entity_index.json`: Pathway 28 *declares* a participant; Pathway 27 *indexes* her content. The end-state both point to is one participant manifest that every surface reads.

## Current gaps (candidates for follow-up)

- **Silent fallback (Rule 12 violation).** `get_group()` returns `'root'` for any directory whose key is absent from `COLORS`, so a thinker with vault files but no `COLORS` line collapses to grey/root with no warning. This should fail loud — extract or generate should flag traditions present on disk but unregistered (and registered-but-empty traditions, see below).
- **`LABEL_OVERRIDES` is hand-maintained.** Could derive from a participant manifest rather than a second hand-edited dict.
- **No automatic flow into Pathway 27.** Registering a tradition in `COLORS` does not yet add her to `entity_index.json`; the two roster sources should converge.
- **No empty-tradition check.** A registered tradition with zero nodes shows an inert checkbox/suggestion; worth a build-time notice.

## Edges

- **27 Universal Search and Ask** — retrieval-side twin. 28 registers and colors a participant; 27 indexes her entities to origin files. Ideal end-state: both read one participant manifest.
- **26 Research Suggestions per Thinker** — consumes the roster that 28 governs.
- **18 Portability and Toolkit Design** — single-registration onboarding is what makes instantiating the system for a *new* community (not the Karpathi vault) cheap.
- **15 Apprentice Mode** — per-tradition curricula presuppose a clean, complete roster.

## Provenance

Surfaced 2026-05-29 in the sociogram-navigation session, immediately after building navigation increment 1.5 (the friendly-label typeahead). Tom asked whether the dropdowns inherit from the checkboxes such that a newly added thinker would appear "without further ado"; tracing the generator confirmed the single-source fan-out from `COLORS` and prompted pinning the principle as its own pathway. Source dialogue: sociogram navigation, 2026-05-29 (Tom / Cowork).
