#!/usr/bin/env python3
"""Generate the Distill-layer long summaries via the cc-broker (Pathway 00).

This is the MODEL step of the summary pipeline. It is incremental and additive:
for each signal in digest.json whose URL is NOT already in long_summaries.json,
it asks the broker (action=enrich) for a faithful ~150-word summary grounded in
the source text the runtime fetched, then writes the result back into the sidecar
with {model, generated, kind} provenance. Already-cached entries are never
touched (so hand-written or prior summaries are preserved), making the whole step
idempotent and cheap to re-run.

The deterministic merge into digest.json still happens in enrich_summaries.py —
this script only populates the sidecar. Pipeline order:
    export_digest.py  →  generate_summaries.py  →  enrich_summaries.py

Broker contract (mirrors wiki/lib/c2a2-search.js, verified against the function
source): POST <broker>/  with headers Content-Type, X-CC-Device:<uuid>, and an
allowed Origin; body {action:"enrich", system, user, model?}. 200 →
{text, source, model, freeRemaining}. 402 → free_limit_reached (cap). 429 →
ip_rate_limited. The broker holds the OpenRouter key server-side and meters a
daily cap; this script sends NO secret.

Stdlib only. Runs wherever the refresh runs (Mac next to the runtime, or cron).

Usage:
  python3 generate_summaries.py --data-dir data
  python3 generate_summaries.py --data-dir data --max-new 12
  python3 generate_summaries.py --self-test          # one broker call, writes nothing
"""

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

DEFAULT_BROKER = "https://akhcocmgfwybdovqeovd.supabase.co/functions/v1/cc-broker"
DEFAULT_ORIGIN = "https://tloughran.github.io"   # must be in the broker's ALLOWED_ORIGINS

SYSTEM_PROMPT = (
    "You write faithful, grounded summaries of AI-developments items for a "
    "community AI-education 'Heartbeat'. Rules: (1) Use ONLY the provided source "
    "text — never add facts, names, numbers, or claims not present in it. "
    "(2) Aim for about 150 words in a single paragraph; if the source text is "
    "thin, write a SHORTER proportionate summary rather than padding, and say it "
    "is based on a brief source. (3) End with one sentence on why this matters for "
    "a community keeping up with AI, clearly framed as relevance — not a new fact. "
    "(4) Plain prose only: no markdown, headings, lists, or preamble like 'This "
    "summary'. Begin directly with the content."
)


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def load_json(p: Path, default):
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def sidecar_entries(sidecar: dict) -> dict:
    # Accept {"entries": {...}} or a bare {url: {...}} mapping.
    if isinstance(sidecar, dict) and "entries" in sidecar and isinstance(sidecar["entries"], dict):
        return sidecar["entries"]
    return sidecar if isinstance(sidecar, dict) else {}


def get_device_id(data_dir: Path) -> str:
    f = data_dir / ".broker_device_id"
    try:
        if f.exists():
            v = f.read_text(encoding="utf-8").strip()
            if v:
                return v
    except Exception:
        pass
    v = str(uuid.uuid4())
    try:
        f.write_text(v + "\n", encoding="utf-8")
    except Exception:
        pass
    return v


def call_broker(broker_url, origin, device_id, system, user, model, timeout):
    payload = {"action": "enrich", "system": system, "user": user}
    if model:
        payload["model"] = model
    req = Request(
        broker_url,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "X-CC-Device": device_id,
            "Origin": origin,
        },
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        try:
            body = json.loads(e.read().decode("utf-8"))
        except Exception:
            body = {"error": "http_" + str(e.code)}
        return e.code, body
    except URLError as e:
        return 0, {"error": "unreachable", "detail": str(e.reason)}


def build_user_prompt(sig: dict) -> str:
    return (
        "Title: " + str(sig.get("title", "")) + "\n"
        "Source: " + str(sig.get("source", "")) + "\n"
        "Tags: " + ", ".join(sig.get("tags") or []) + "\n\n"
        "Source text (this is all that was fetched; summarize only this):\n"
        + str(sig.get("summary", "")).strip()
    )


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--data-dir", default=str(Path(__file__).resolve().parent.parent / "data"))
    p.add_argument("--broker-url", default=DEFAULT_BROKER)
    p.add_argument("--origin", default=DEFAULT_ORIGIN, help="must be in broker ALLOWED_ORIGINS")
    p.add_argument("--model", default=None, help="OpenRouter model id; default = broker default (gpt-4o-mini)")
    p.add_argument("--max-new", type=int, default=12, help="cap items generated this run (cost bound)")
    p.add_argument("--timeout", type=float, default=60.0)
    p.add_argument("--self-test", action="store_true", help="one broker call, print result, write nothing")
    args = p.parse_args(argv)

    data_dir = Path(args.data_dir)
    device_id = get_device_id(data_dir)

    if args.self_test:
        st, body = call_broker(
            args.broker_url, args.origin, device_id,
            "Reply with exactly the word: ok", "ping", args.model, args.timeout,
        )
        print("broker status:", st)
        print("broker body:", json.dumps(body)[:400])
        ok = st == 200 and isinstance(body, dict) and body.get("text")
        print("SELF-TEST", "PASS" if ok else "FAIL")
        return 0 if ok else 1

    digest = load_json(data_dir / "digest.json", None)
    if not digest or "signals" not in digest:
        raise SystemExit("error: no digest.json with signals at " + str(data_dir))

    sidecar_raw = load_json(data_dir / "long_summaries.json", {"entries": {}})
    entries = sidecar_entries(sidecar_raw)
    # Normalize to the {"_about", "entries"} envelope on write.
    about = sidecar_raw.get("_about") if isinstance(sidecar_raw, dict) else None

    missing = [s for s in digest["signals"] if s.get("url") and s["url"] not in entries]
    print("signals: {0} | cached: {1} | missing: {2} | will attempt: {3}".format(
        len(digest["signals"]), len(entries), len(missing), min(len(missing), args.max_new)))

    made = 0
    for sig in missing[: args.max_new]:
        st, body = call_broker(
            args.broker_url, args.origin, device_id,
            SYSTEM_PROMPT, build_user_prompt(sig), args.model, args.timeout,
        )
        if st == 200 and isinstance(body, dict) and body.get("text"):
            entries[sig["url"]] = {
                "long_summary": body["text"].strip(),
                "model": body.get("model", "via cc-broker"),
                "generated": today(),
                "kind": "machine-generated",
            }
            made += 1
            print("  + {0}  ({1})".format(sig.get("title", "")[:60], body.get("model", "")))
        elif st in (402, 429):
            # Cap or rate-limit hit — stop cleanly, keep what we have.
            print("  ! cap/limit hit ({0}: {1}) — stopping; remaining left for next run".format(
                st, (body or {}).get("error", "")))
            break
        else:
            # Transient/provider error — skip this item, continue.
            print("  ~ skip ({0}: {1}) {2}".format(st, (body or {}).get("error", ""), sig.get("title", "")[:50]))

    if made:
        out = {"_about": about or "Sidecar of machine-generated long summaries; merged by enrich_summaries.py.",
               "entries": entries}
        (data_dir / "long_summaries.json").write_text(
            json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("done: {0} new summary(ies) written; sidecar now holds {1}".format(made, len(entries)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
