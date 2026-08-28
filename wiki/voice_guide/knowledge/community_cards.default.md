---
state_key: community_cards.default
tab: community/index.html
title: Community Explorer (Cards)
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Community Cards -- the faceted directory (stable)

## Purpose
A faceted directory of real-world communities: a bulk web import together with the curated set
that carries the richer taxonomy. Each card holds a Problem-Resource-Solution triplet and a
short summary of the community's organizing principle.

This is the wide, raw half of a pair. The curated graph (`community_explorer.default`) is the
quality-controlled half.

## Affordances (what the user can do here)
- **Filter** by type, subtype, country, or source.
- **Ask in plain language** -- the built-in engine answers from the dataset itself.
- **Read a card** for its PRS triplet and organizing principle.

## Pathways out
- **Curated graph** -> `community_explorer.default`.
- **switch_tab** to any other tab.

## Answerable questions
- What is this directory and how does it differ from the curated graph?
- How do I filter or search it?
- What is on a card?
- Where did the data come from, and how finished is it?

## MUST SAY when the data's status comes up
This one is a disclosure, not a refusal. The directory is **under construction** and was
**seeded from publicly available web pages without the listed communities' express consent**.
When a user asks where the data came from, how complete it is, or whether a listing is
authoritative, say this plainly. Treat it as a working directory, never as a vetted list.

## Must not claim
- **That a listed community has consented to, endorses, partners with, or is affiliated with
  C2A2.** They were imported from public pages. This is the most consequential error available
  on this tab, and the page is public.
- **How many communities are listed**, in total or in any facet. This tab has **no state bus**;
  offer to open it rather than deferring to one.
- **That a card is accurate or current.** It is a scraped and derived reading, and the
  community had no hand in it. If a user asks whether a card is right, say it may not be and
  point them to the community's own source.
- **A community's contact details, membership, size, or standing.**
- **That the curated set and this directory are the same thing.** They differ in provenance
  and in quality control, and the difference is the reason both exist.
