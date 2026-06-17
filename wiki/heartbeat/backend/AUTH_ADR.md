# ADR — Heartbeat sign-in + per-user preferences (Phase 2b)

*Status: ACCEPTED + APPLIED 2026-06-17. Sign-in method chosen: **magic link (email
OTP)**. The `user_preferences` migration is applied; `auth.js` + `heartbeat-config.js`
are wired into the tab. Remaining manual step: configure Supabase Auth redirect URLs
(see "Remaining" below).*

## Context

The immediate goal is to make the Heartbeat **useful to others besides the author**,
which requires sign-in and per-user preferences before any federation. The public
tab is otherwise static / GitHub-Pages-safe; accounts are the first thing that needs
a backend.

A backend already exists: the **`C2A2-wiki` Supabase project** (ref
`akhcocmgfwybdovqeovd`, active), currently hosting the cc-broker rate-limit tables.
**Supabase Auth is provisioned but has 0 users.**

## Decision

Use **Supabase Auth** for sign-in and a single **`public.user_preferences`** table
(jsonb, RLS, owner-only) for storage, reusing the existing project. Rationale:

- **No new infrastructure / no new cost surface.** The project, Postgres, and the
  Auth service already run. Adding one table is additive and does not touch broker
  tables (verified: `device_usage`, `global_meter`, `device_byo_keys`, `ip_hits`
  remain untouched).
- **RLS does the permission work.** `auth.uid() = user_id` policies mean a user can
  only ever read/write their own lens — the §3 "local ownership / role-based access"
  invariant enforced at the database, not in app code.
- **One schema, two stores.** `data/preferences.schema.json` already backs the
  client-side localStorage lens. The account row stores the *same* document, so the
  local lens upgrades to a synced lens at sign-in with no UI change.
- **Pages stays static.** The public read surface is unchanged; only signed-in
  writes hit Supabase, via the JS client + anon key (safe to expose; RLS is the
  guard).

### Sign-in method — the one decision needed from Tom

| Option | Friction | Notes |
|---|---|---|
| **Magic link (email OTP)** *(recommended default)* | Lowest; no passwords | Supabase sends a sign-in link; good for a broad community audience. Needs email sending configured (Supabase default SMTP for low volume, or your own SMTP later). |
| **Google / GitHub OAuth** | One click for users with those accounts | Requires registering an OAuth app + redirect URL per provider. |
| **Email + password** | Familiar; you manage resets | More surface (password rules, reset flow). |

Federated identity / SSO is explicitly out of scope for Phase 2b.

## Consequences

- **Consent/role model ships first.** Per §3 of `ARCHITECTURE.md`, the consent
  booleans live in the preference schema (all default false) and gate every future
  write/contribution path. No stars/comments/shared-graph writes in this phase.
- **Anon key in client.** Acceptable: it is a publishable key; RLS is the real
  boundary. The service-role key is never shipped to the browser.
- **Redirect URLs.** The site origin(s) — GitHub Pages URL and any localhost used
  for review — must be added to the project's allowed redirect URLs.

## Done (2026-06-17)

1. Sign-in method chosen: **magic link**.
2. `0001_user_preferences.sql` applied via `apply_migration` (verified: table, RLS,
   3 policies, 1 trigger).
3. `auth.js` + `heartbeat-config.js` wired into `index.html`: sign-in bar above the
   Pulse signals; account tier reads `user_preferences` on sign-in (seeds from the
   local lens on first sign-in) and upserts on every change. Graceful no-op when the
   SDK/config aren't present (file://), so the per-device lens always works.

## Remaining (manual, in Supabase dashboard — Auth → URL Configuration)

- Set **Site URL** and add **Redirect URLs** for every origin the tab is served from:
  the GitHub Pages URL (e.g. `https://<user>.github.io/C2A2-wiki/wiki/heartbeat/`)
  and any localhost used for review (e.g. `http://localhost:8080/heartbeat/`). The
  magic link only returns to allow-listed URLs. Email provider is on by default;
  default SMTP is fine for low volume (add your own SMTP before high volume).
- The Heartbeat tab also runs inside the Explorer iframe; for that path, sign-in is
  simplest from the standalone `heartbeat/index.html` page (same origin → shared
  session). Iframe-embedded magic-link return can be hardened later if needed.
