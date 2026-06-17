-- C2A2 Heartbeat — Phase 2b: per-account preference storage
-- Target project: C2A2-wiki (ref akhcocmgfwybdovqeovd)
--
-- STATUS: APPLIED 2026-06-17 (migration `heartbeat_user_preferences`). Additive
-- only — created one new table in `public`; broker tables (device_usage,
-- global_meter, device_byo_keys, ip_hits) untouched. Verified: RLS on, 3 policies,
-- 1 trigger. Kept here as the source-of-record for the schema. See AUTH_ADR.md.
--
-- Stores the SAME document defined by data/preferences.schema.json, one row per
-- authenticated user, protected by row-level security so a user can read/write
-- only their own row.

create table if not exists public.user_preferences (
  user_id     uuid primary key references auth.users (id) on delete cascade,
  prefs       jsonb not null default '{}'::jsonb,
  schema_ver  integer not null default 1,
  updated_at  timestamptz not null default now()
);

comment on table public.user_preferences is
  'C2A2 Heartbeat per-user lens. prefs conforms to wiki/heartbeat/data/preferences.schema.json (v1). One row per auth user; RLS restricts access to the owner.';

alter table public.user_preferences enable row level security;

-- Owner-only access. auth.uid() is the signed-in user's id.
drop policy if exists "own prefs - select" on public.user_preferences;
create policy "own prefs - select" on public.user_preferences
  for select using (auth.uid() = user_id);

drop policy if exists "own prefs - insert" on public.user_preferences;
create policy "own prefs - insert" on public.user_preferences
  for insert with check (auth.uid() = user_id);

drop policy if exists "own prefs - update" on public.user_preferences;
create policy "own prefs - update" on public.user_preferences
  for update using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- keep updated_at fresh
create or replace function public.touch_user_preferences()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists trg_touch_user_preferences on public.user_preferences;
create trigger trg_touch_user_preferences
  before update on public.user_preferences
  for each row execute function public.touch_user_preferences();
