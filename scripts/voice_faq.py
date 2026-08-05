#!/usr/bin/env python3
"""
voice_faq.py — Feature-FAQ generator for the C2A2 Explorer voice guide.

The "Talk to the Wiki" voice guide (in wiki/explorer.html) loads
wiki/voice_guide_faq.json at session start and uses it as its first-pass
resource for answering vocalized questions. This script owns the DETERMINISTIC
half of keeping that FAQ fresh (Rule 5: if code can answer, code answers):

  scan   Read every knowledge/ affordance-state file, hash each, and diff
         against voice_faq/state.json. Prints JSON: which features (per
         state_key) are new, changed, unchanged, or removed. No network, no key.

  merge  Take LLM-authored Q&A for the new/changed features, retain existing
         Q&A for unchanged features, validate the schema, and write
         wiki/voice_guide_faq.json + voice_faq/report.md + update state.json.

The GENERATIVE half (authoring natural Q&A for new/changed features) is done by
the weekly scheduled Claude agent, which runs `scan`, writes a qa JSON, then
runs `merge`. This split keeps generation smart and everything else reliable.

Per the repo's no-blind-push rule, this script never pushes. It writes the FAQ
and a report; a human reviews and publishes.

The FAQ deepens over time toward TARGET_TOTAL (100) questions: `merge` is
ADDITIVE — provided Q&A is appended to each feature (deduped by question), never
overwriting. Author questions high-level first, working down to detail. Once the
target is reached the agent adds ~1/week and keeps scanning for feature changes.

Usage:
    python3 voice_faq.py scan                       # feature diff as JSON
    python3 voice_faq.py scan --pretty              # human-readable diff
    python3 voice_faq.py status                      # coverage, phase, thinnest features
    python3 voice_faq.py merge <qa.json>            # append Q&A + write FAQ + report
    python3 voice_faq.py merge <qa.json> --dry-run  # validate + preview; no writes

qa.json shape (any subset of state_keys; pairs are appended, dupes skipped):
    { "sociogram.graph.default": [ {"q": "...", "a": "..."}, ... ], ... }
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "wiki" / "voice_guide" / "knowledge"   # canonical source of truth
FAQ_OUT = ROOT / "wiki" / "voice_guide_faq.json"
STATE_DIR = ROOT / "voice_faq"                # outside wiki/ so Obsidian ignores it
STATE_FILE = STATE_DIR / "state.json"
REPORT_FILE = STATE_DIR / "report.md"

MIN_QA_PER_FEATURE = 3        # floor for a brand-new feature's first seed
TARGET_TOTAL = 100            # ramp target; once reached, the agent adds ~1/week


# ── feature inventory ────────────────────────────────────────────────────────
# Source of truth is the canonical knowledge/ directory (voice_guide_state_bus.md
# "canonical-source rule"), NOT the descriptions map inside explorer.html. Each
# knowledge file is one FAQ feature keyed by its `state_key` — i.e. per
# affordance-state (finer than per-tab). The explorer's own help text is DERIVED
# from knowledge/ by scripts/derive_tab_help.py, so it is not a second source.


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a knowledge markdown file into (frontmatter dict, body).

    Frontmatter is the block between the first two `---` lines; values are simple
    `key: value` scalars (no nested YAML needed here)."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.split("#", 1)[0].strip()
    return fm, m.group(2)


def build_inventory() -> list[dict]:
    """One record per knowledge affordance-state: key (state_key), title, body.

    Order = sorted by filename for determinism."""
    inv: list[dict] = []
    if not KNOWLEDGE_DIR.is_dir():
        return inv
    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        fm, body = _parse_frontmatter(path.read_text(encoding="utf-8"))
        key = fm.get("state_key") or path.stem
        inv.append({
            "key": key,
            "title": fm.get("title") or key,
            "label": fm.get("title") or key,
            "body": body.strip(),
        })
    return inv


def _hash_feature(rec: dict) -> str:
    return hashlib.sha1((rec["title"] + "\x1e" + rec["body"]).encode("utf-8")).hexdigest()[:12]


def _norm_q(q: str) -> str:
    """Normalize a question for dedupe (case/punctuation/whitespace-insensitive)."""
    return re.sub(r"[^a-z0-9]+", " ", (q or "").lower()).strip()


# ── state ────────────────────────────────────────────────────────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"features": {}, "last_run": None}


def diff_inventory(inv: list[dict], state: dict) -> dict:
    prev = state.get("features", {})
    new, changed, unchanged = [], [], []
    inv_keys = set()
    for rec in inv:
        inv_keys.add(rec["key"])
        h = _hash_feature(rec)
        if rec["key"] not in prev:
            new.append(rec)
        elif prev[rec["key"]].get("hash") != h:
            changed.append(rec)
        else:
            unchanged.append(rec["key"])
    removed = [k for k in prev if k not in inv_keys]
    return {"new": new, "changed": changed, "unchanged": unchanged, "removed": removed}


# ── commands ─────────────────────────────────────────────────────────────────

def cmd_scan(args) -> int:
    inv = build_inventory()
    diff = diff_inventory(inv, load_state())
    if args.pretty:
        print(f"Knowledge features: {len(inv)}")
        print(f"  new:       {len(diff['new'])}  " +
              ", ".join(r["key"] for r in diff["new"]))
        print(f"  changed:   {len(diff['changed'])}  " +
              ", ".join(r["key"] for r in diff["changed"]))
        print(f"  unchanged: {len(diff['unchanged'])}")
        print(f"  removed:   {len(diff['removed'])}  " + ", ".join(diff["removed"]))
        need = diff["new"] + diff["changed"]
        if need:
            print("\nNeeds Q&A authored for:")
            for r in need:
                print(f"\n### {r['key']}  ({r['title']})")
                print(r["body"][:600])
    else:
        print(json.dumps(diff, indent=2))
    return 0


def _validate_qa(qa_map: dict, need_keys: set, all_keys: set,
                 existing_keys: set) -> list[str]:
    """Merge is additive, so deepening may add as few as one pair. Only a
    brand-new feature (no existing Q&A) must arrive with the seed floor."""
    errs: list[str] = []
    for key in need_keys:
        if key not in qa_map and key not in existing_keys:
            errs.append(f"missing Q&A for new/changed feature: {key}")
    for key, pairs in qa_map.items():
        if key not in all_keys:
            errs.append(f"Q&A provided for unknown feature key: {key}")
            continue
        if not isinstance(pairs, list) or len(pairs) < 1:
            errs.append(f"{key}: expected a non-empty list of Q&A pairs")
            continue
        is_new = key not in existing_keys
        if is_new and len(pairs) < MIN_QA_PER_FEATURE:
            errs.append(f"{key}: new feature needs >= {MIN_QA_PER_FEATURE} "
                        f"seed pairs, got {len(pairs)}")
        for i, p in enumerate(pairs):
            if not isinstance(p, dict) or not p.get("q") or not p.get("a"):
                errs.append(f"{key}[{i}]: each pair needs non-empty 'q' and 'a'")
    return errs


def cmd_merge(args) -> int:
    inv = build_inventory()
    inv_by_key = {r["key"]: r for r in inv}
    all_keys = set(inv_by_key)
    state = load_state()
    diff = diff_inventory(inv, state)
    need_keys = {r["key"] for r in diff["new"]} | {r["key"] for r in diff["changed"]}

    qa_map = json.loads(Path(args.qa).read_text(encoding="utf-8"))

    existing_faq = {}
    if FAQ_OUT.exists():
        try:
            for f in json.loads(FAQ_OUT.read_text(encoding="utf-8")).get("features", []):
                existing_faq[f["key"]] = f.get("qa", [])
        except Exception:
            pass

    errs = _validate_qa(qa_map, need_keys, all_keys, set(existing_faq))
    if errs:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        return 1

    # The additive merge below is additive WITHIN a key. The output file is not:
    # `features` is rebuilt by iterating the inventory, so a key holding Q&A that
    # is no longer in the inventory is simply never emitted, and its pairs vanish
    # from the published file. That is correct exactly once -- at the END of a key
    # migration, after the pairs have been re-homed under the new keys -- and is
    # silent data loss at every other moment.
    #
    # It is not hypothetical: the 2026-07-22 move to knowledge/ as canonical source
    # (bd33ef7) re-keyed features from per-tab filenames to per-affordance-state
    # `state_key`s and ported only the Sociogram slice, leaving 102 pairs under 14
    # keys the inventory no longer names. Nothing has overwritten them yet only
    # because still_missing below refuses first. Seed the four new keys to clear
    # that, and this path opens.
    dropped = sorted(k for k, pairs in existing_faq.items()
                     if pairs and k not in all_keys)
    if dropped and not args.allow_drop:
        lost = sum(len(existing_faq[k]) for k in dropped)
        print(f"REFUSING: {len(dropped)} feature(s) hold Q&A but are no longer in "
              f"the inventory. Merging would drop {lost} pair(s):", file=sys.stderr)
        for k in dropped:
            print(f"  - {k} ({len(existing_faq[k])} pair(s))", file=sys.stderr)
        print("  Re-home them under current keys first, or pass --allow-drop if "
              "you already have.", file=sys.stderr)
        return 1

    # ADDITIVE merge: existing Q&A is kept; provided pairs are appended, deduped
    # by normalized question. This lets the agent DEEPEN a feature (add pairs)
    # rather than overwrite it. Order within a feature = high-level first, then
    # whatever the agent appends over time (detail).
    merged = {k: list(v) for k, v in existing_faq.items()}
    added, skipped_dupes = 0, 0
    for key, pairs in qa_map.items():
        seen = {_norm_q(p["q"]) for p in merged.get(key, [])}
        for p in pairs:
            nq = _norm_q(p["q"])
            if nq in seen:
                skipped_dupes += 1
                continue
            merged.setdefault(key, []).append({"q": p["q"], "a": p["a"]})
            seen.add(nq)
            added += 1

    features, still_missing = [], []
    for rec in inv:
        key = rec["key"]
        if merged.get(key):
            features.append({"key": key, "title": rec["title"], "qa": merged[key]})
        else:
            still_missing.append(key)
    if still_missing:
        print("VALIDATION FAILED: no Q&A (existing or authored) for: "
              + ", ".join(still_missing), file=sys.stderr)
        return 1

    total = sum(len(f["qa"]) for f in features)
    phase = "ramp" if total < TARGET_TOTAL else "steady"
    deficit = max(0, TARGET_TOTAL - total)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    faq = {"generated_at": now,
           "feature_count": len(features),
           "qa_count": total,
           "target_total": TARGET_TOTAL,
           "features": features}

    if args.dry_run:
        print(f"[dry-run] +{added} added, {skipped_dupes} dupes skipped -> "
              f"{total} total ({phase}, {deficit} to target).")
        return 0

    STATE_DIR.mkdir(exist_ok=True)
    FAQ_OUT.write_text(json.dumps(faq, indent=2, ensure_ascii=False), encoding="utf-8")

    state["features"] = {r["key"]: {"hash": _hash_feature(r), "title": r["title"]}
                         for r in inv}
    state["last_run"] = now
    state["qa_total"] = total
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

    thin = sorted(((len(f["qa"]), f["title"], f["key"]) for f in features))[:5]
    lines = [
        "# Voice-guide FAQ — refresh report", "",
        f"Generated: {now}", "",
        f"- Total Q&A pairs: **{total}** / target {TARGET_TOTAL}  ·  phase: **{phase}**",
        f"- Added this run: **{added}**  ·  duplicate questions skipped: {skipped_dupes}",
        f"- Features covered: **{len(features)}**",
        f"- New features: {len(diff['new'])}  ·  Changed: {len(diff['changed'])}  "
        f"·  Removed from state: {len(diff['removed'])}", "",
        "## Thinnest features (deepen these next)",
        *[f"- {c} Q&A — {title} (`{key}`)" for c, title, key in thin], "",
    ]
    if diff["new"]:
        lines += ["## New features", *[f"- `{r['key']}` — {r['title']}" for r in diff["new"]], ""]
    if diff["changed"]:
        lines += ["## Changed features (help text changed — review answers for staleness)",
                  *[f"- `{r['key']}` — {r['title']}" for r in diff["changed"]], ""]
    if diff["removed"]:
        lines += ["## Removed from explorer", *[f"- `{k}`" for k in diff["removed"]], ""]
    # Only reachable with --allow-drop. Named here as well as on stderr: the report
    # is the durable artifact, and a permitted drop still has to be legible later.
    if dropped:
        lines += ["## Dropped from the published FAQ (--allow-drop was passed)",
                  *[f"- `{k}` — {len(existing_faq[k])} pair(s) no longer published"
                    for k in dropped], ""]
    lines += ["---",
              "Review `wiki/voice_guide_faq.json`, then commit + push it with the",
              "rest of the wiki (no auto-push, per the repo's no-blind-push rule)."]
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {FAQ_OUT.relative_to(ROOT)} — {total} Q&A across {len(features)} "
          f"features (+{added} this run, {phase}, {deficit} to target).")
    print(f"Report: {REPORT_FILE.relative_to(ROOT)}")
    return 0


def cmd_status(args) -> int:
    """Report current coverage and where to deepen next — for the agent."""
    inv = build_inventory()
    existing = {}
    if FAQ_OUT.exists():
        try:
            for f in json.loads(FAQ_OUT.read_text(encoding="utf-8")).get("features", []):
                existing[f["key"]] = len(f.get("qa", []))
        except Exception:
            pass
    counts = [(existing.get(r["key"], 0), r["title"], r["key"]) for r in inv]
    total = sum(c for c, _, _ in counts)
    phase = "ramp" if total < TARGET_TOTAL else "steady"
    out = {"total": total, "target": TARGET_TOTAL,
           "deficit": max(0, TARGET_TOTAL - total), "phase": phase,
           "per_feature": [{"key": k, "title": t, "count": c}
                           for c, t, k in sorted(counts)]}
    print(json.dumps(out, indent=2))
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="C2A2 voice-guide FAQ generator")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="diff explorer features against state")
    s.add_argument("--pretty", action="store_true")
    s.set_defaults(func=cmd_scan)
    m = sub.add_parser("merge", help="append authored Q&A into the FAQ (additive)")
    m.add_argument("qa", help="path to authored qa.json")
    m.add_argument("--dry-run", action="store_true")
    m.add_argument("--allow-drop", action="store_true",
                   help="permit dropping Q&A held under keys the inventory no "
                        "longer names (only after re-homing them)")
    m.set_defaults(func=cmd_merge)
    st = sub.add_parser("status", help="coverage + phase + thinnest features (JSON)")
    st.set_defaults(func=cmd_status)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
