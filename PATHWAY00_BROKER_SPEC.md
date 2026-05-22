# Pathway-00 Broker — Build Spec (free tier → add-your-own brokered key)

**Date:** 2026-05-22 · **Owner:** Tom Loughran · **Status:** Approved direction; build not started.
**Target:** working pilot **before ISME (July 8–10, 2026)**. Pilot surface = the Community Explorer tab only; roll to the other AI tabs after ISME.
**Resume cue:** open a Cowork thread and say *"build the Pathway-00 broker per the spec"* (or paste this file).

---

## 1. Purpose — what the broker is FOR

Pathway 00 settled that **public C2A2 pages must never hold a client-side API key**. The broker is the server-side seam that makes that real: the browser calls *the broker*, never a model provider, and holds no secret. The broker decides whose money pays and which provider answers.

The scheme Tom wants, in one line:

> **An up-front free allowance on Tom's dime, then "add your own key" — but brokered** (the user's key is stored server-side, used only for their calls, never exposed on the page).

Two payoffs: (a) anyone can try the AI features with zero setup; (b) Tom's spend is capped and watched ("close watch on ask-scope"), and heavy users bring their own funding without ever touching a raw key in the page.

This is the **Pathway-00 substrate** the other AI tabs (Sociogram TTS, Connectome search) will later route through. We pilot it on the Community Explorer because it was deliberately built as the **first broker-ready tab** — all its key/LLM access already funnels through one `callLLM()` seam.

---

## 2. Locked decisions (2026-05-22)

| Decision | Choice | Why |
|---|---|---|
| Free-tier metering | **Per-browser/day, anonymous** — keyed to a localStorage device UUID; default **10 asks/day** (config knob) | Fastest to ship for July; no login friction; acceptable for a research preview. Defeatable by clearing storage → backstopped by IP rate-limit + a global daily $ ceiling. |
| July scope | **Community Explorer pilot only** | Designated first broker-ready tab; prove the free→BYO flow end to end before widening surface area. |
| Broker substrate | **Supabase Edge Function (Deno/TS) + Postgres** | Already in Tom's toolset; serverless/low-ops for a non-developer; keys live server-side; Postgres for metering + encrypted key storage. |
| Upstream | **OpenRouter** (one provider-agnostic endpoint, 300+ models, model-swappable by config) | Keeps provider choice *inside* the broker, exactly as the broker-only direction intended; one billing surface for Tom's free pool. |
| BYO key format | **An OpenRouter key** (one format, provider-agnostic for the user too) | One code path; the user also gets multi-provider without us writing a provider registry. |
| Default model | cheap/fast tier via OpenRouter, **config value `DEFAULT_MODEL`** (e.g. `openai/gpt-4o-mini` or `google/gemini-2.0-flash`) | Ranking task is ~1K tokens/call → a fraction of a cent on any cheap-tier model; the point is it's one line to change. |

Term note — **"AI gateway / broker":** a single server endpoint that holds the real key(s) and forwards to a model. **"BYO key, brokered":** the user supplies their own key but it is stored and used *server-side*; it never appears in page JavaScript.

---

## 3. Architecture & request flow

```
Browser (Community Explorer)                Supabase Edge Function "cc-broker"        OpenRouter
  callLLM({system,user})  ──POST /enrich──▶  1. check origin + device id + size
  X-CC-Device: <uuid>                        2. IP rate-limit backstop
  (no secret)                                3. today's count for device?
                                             4a. under free limit & under global cap
                                                 → use OPENROUTER_FREE_KEY (Tom)  ──▶  model
                                                    ++device count, ++global meter
                                             4b. over limit & device has BYO key
                                                 → decrypt BYO key, use it        ──▶  model
                                             4c. over limit & no BYO key
                                                 → 402 free_limit_reached
  ◀── {text, source, model, freeRemaining} ──  return text only (never a key)
```

Postgres holds: per-device daily counters, the global daily meter (circuit breaker), and each device's **encrypted** BYO key. Tom's free-pool key lives only as a function **secret**.

---

## 4. Broker contract (so the client swap is a one-liner)

Base URL: `BROKER_URL` = the deployed Edge Function URL. All requests send `X-CC-Device: <uuid>` and **no secret**. CORS is locked to the Pages origin.

**`POST /enrich`** — the only call the AI features make.
- Body: `{ "system": string, "user": string, "maxTokens"?: number, "model"?: string }`
- `200` → `{ "text": string, "source": "free" | "byo", "model": string, "usage": {prompt_tokens, completion_tokens}, "freeRemaining": number }`
- `402` → `{ "error": "free_limit_reached", "freeRemaining": 0 }` — UI prompts "add your key"
- `429` → `{ "error": "rate_limited" }`
- `4xx/5xx` → `{ "error": string }` — client falls back to the deterministic engine

**`GET /status`** → `{ "freeRemaining": number, "hasByoKey": boolean, "model": string }` — drives the Ask-panel pill.

**`POST /key`** — body `{ "key": string }` → stores it **encrypted**, returns `{ "ok": true, "masked": "sk-or-…XXXX" }`. Never echoes the full key.

**`DELETE /key`** → `{ "ok": true }` — user removes their stored key.

---

## 5. Data model (Postgres)

```sql
-- per-device daily free-tier counter
create table cc_usage (
  device_id  text not null,
  usage_date date not null default current_date,
  count      int  not null default 0,
  primary key (device_id, usage_date)
);

-- one encrypted BYO key per device (encryption via Supabase Vault / pgsodium)
create table cc_byo_key (
  device_id      text primary key,
  key_ciphertext bytea not null,        -- encrypted at rest; decrypt only in function memory
  masked         text not null,         -- e.g. "sk-or-…7f2a" for UI display
  created_at     timestamptz not null default now()
);

-- global daily circuit breaker protecting Tom's dime
create table cc_global_meter (
  usage_date  date primary key default current_date,
  spend_cents int  not null default 0
);

-- optional: lightweight event log (no payloads, no keys)
create table cc_event (
  id serial primary key, ts timestamptz default now(),
  device_id text, kind text, model text, est_cents int
);
```

Encryption: use **Supabase Vault** (or `pgsodium`) so `cc_byo_key.key_ciphertext` is never readable from the DB alone; the function decrypts in memory only at call time.

---

## 6. Free-tier algorithm (server, fully deterministic — code answers, not the model)

1. **Gate:** verify `Origin` is in the allowlist; require `X-CC-Device`; reject bodies over a size cap (e.g. 8 KB).
2. **IP backstop:** rate-limit per IP (e.g. **30 req/min**) regardless of device id.
3. **Look up** today's `count` for the device and today's global `spend_cents`.
4. **Free path** — if `count < FREE_LIMIT` **and** `spend_cents < GLOBAL_DAILY_CAP_CENTS`: call OpenRouter with `OPENROUTER_FREE_KEY`; on success `count++` and add the call's estimated cost to the global meter; return `source:"free"`, `freeRemaining = FREE_LIMIT - count`.
5. **BYO path** — else if the device has a stored key: decrypt it, call OpenRouter with it; **do not** touch the free counter or global meter; return `source:"byo"`.
6. **Wall** — else return `402 free_limit_reached`.
7. **Always** clamp `max_tokens` server-side to ≤ `MAX_TOKENS` (600) no matter what the client sends.

Config knobs (env): `FREE_LIMIT=10`, `GLOBAL_DAILY_CAP_CENTS=500` ($5/day default), `DEFAULT_MODEL`, `MAX_TOKENS=600`, `IP_RATE=30/min`, `ALLOWED_ORIGIN`.

---

## 7. Client changes (Community Explorer — reuse the existing seam)

The whole point of the `getKey()/callLLM()` seam (`wiki/community/app.js`, ~lines 49–79) is that this is a localized change:

- **Rewrite `callLLM()`** to `POST {BROKER_URL}/enrich` with `X-CC-Device` and `{system, user, maxTokens}` — **no key**. Map `402` to a thrown `'free-limit'` so `enrichWithLLM()` falls back to the deterministic engine *and* the UI shows the add-key prompt. Keep `callLLM()` the single network entrypoint (the single-seam property).
- **Retire `getKey()` / `tts_api_key`** in this tab. Store only an anonymous `cc_device_id` UUID in localStorage. (Resolves the long-standing `tts_api_key` misnomer for this tab.)
- **Ask-panel UI:** replace the transport pill with broker state from `GET /status`:
  - *"Brokered · N free asks left today"* (free path), or
  - *"Your key · •••XXXX"* (BYO path), with a **Remove key** action.
  - When `/enrich` returns `402`: inline prompt *"You've used today's free asks. Paste your OpenRouter key to keep going — it's stored securely server-side, never in this page."* → `POST /key` → pill flips to "Your key".
- **No other tab changes** for the pilot. `prs_3d.html` (Connectome) and the Sociogram keep their current BYO-in-localStorage until the post-ISME rollout reuses this exact seam.

---

## 8. Security & "watch the ask-scope"

- **Keys never reach the client.** Tom's free-pool key is a function secret; BYO keys are encrypted at rest and decrypted only in function memory; responses return text + a **masked** key only.
- **CORS locked** to the Pages origin; reject all others. No secrets in URLs, query strings, or logs.
- **Three nested caps** (the leash Tom asked for): per-call `max_tokens` (600), per-device/day `FREE_LIMIT` (10), and a **global daily $ ceiling** that halts the free pool even if many fresh devices appear. As a hard outer backstop, **set a spend limit on the OpenRouter account itself**.
- **Honesty layer:** the add-key copy states the key is stored server-side and is deletable; `DELETE /key` actually removes it.
- **Known limitation (accepted for preview):** an anonymous device id resets when storage is cleared, so the free tier is not abuse-proof — the IP limit + global cap + OpenRouter account limit are what actually protect the dime.

---

## 9. Who does what (safety boundary)

**Tom must do himself** (account/secret actions Claude must not take): create the Supabase project; create an OpenRouter account and generate the **free-pool** OpenRouter key; set the Edge Function secrets (`OPENROUTER_FREE_KEY`, encryption secret, `ALLOWED_ORIGIN`); set a hard **spend limit** on the OpenRouter account.

**Claude / Cowork can build:** the SQL migrations, the `cc-broker` Edge Function (Deno/TS), the client `callLLM()` swap + Ask-panel UI, and the tests. Deployment can use the Supabase MCP (`apply_migration`, `deploy_edge_function`) **with Tom confirming cost** — but only after local review and Tom's sign-off, per the constitutional no-blind-push rule.

---

## 10. Build sequence (ordered, for July)

1. **Tom:** provision Supabase project + OpenRouter free-pool key + account spend limit. Hand the project ref + `BROKER_URL` placeholder to the build.
2. Migrations: create the four tables (§5) + Vault/pgsodium encryption helpers.
3. `cc-broker` Edge Function: `/enrich`, `/status`, `/key` (POST/DELETE) implementing §6, with CORS + IP limit + caps.
4. Local test the function (curl): free path, free-limit boundary (call 10 then 11 → 402), BYO path, `/key` store + mask + delete, CORS rejection, oversize-body rejection.
5. Client swap in `wiki/community/`: rewrite `callLLM()`, retire `getKey()`/`tts_api_key`, add device UUID, add the Ask-panel free-count/add-key UI.
6. Wire `BROKER_URL` (config constant) and verify the Community Explorer end to end against the deployed function.
7. **Constitutional review:** serve `wiki/` locally, review `http://localhost:8080/explorer.html` → Community Explorer; confirm free asks count down, 402 prompts for a key, BYO path works, deterministic fallback on broker error. Report observations → Tom signs off → **Tom pushes from the Mac.**

---

## 11. Testing / acceptance

- **Free boundary:** with `FREE_LIMIT=10`, the 11th same-day ask on a fresh device returns `402` and the UI prompts for a key.
- **BYO:** after `POST /key`, over-limit asks succeed with `source:"byo"` and do **not** change `freeRemaining`.
- **Leash:** with `GLOBAL_DAILY_CAP_CENTS` set low, the free pool halts even across new devices; OpenRouter account limit is the final wall.
- **No key leak:** no response, log, or URL ever contains a full key; `/status` and `/key` return only masked values.
- **Fallback:** any broker error degrades gracefully to the deterministic `ai-query-core.js` engine — the tab never hard-fails.

---

## 12. Deferred (post-pilot / dev track)

- **User-pays beyond BYO:** layer **Stripe AI token billing** (set a developer margin) so a community can fund its own usage and Tom takes a small fee — Stripe's token-billing/margin feature is new in 2026 and was in private preview as of this writing.
- **Cross-tab rollout:** point Sociogram TTS + Connectome `callLLM()` at the same broker; standardize/retire the `tts_api_key` name with a migration.
- **Sturdier identity:** optional magic-link login if anonymous metering proves too leaky.
- **Provider registry inside the broker** if we ever want non-OpenRouter upstreams.

---

## 13. Constraints carried from project standing rules

- **No blind pushes.** Local HTTP review of `explorer.html` + Tom's sign-off before any push; the sandbox cannot push — Tom pushes from the Mac.
- **Repo is public** (`github.com/tloughran/C2A2-wiki`) → triple-check no secret ever lands in committed files; `BROKER_URL` is public (fine), keys are not (server-side only).
- **Obsidian caution:** edits to `wiki/**` while Obsidian is open can revert — reload-without-saving and verify from disk.
