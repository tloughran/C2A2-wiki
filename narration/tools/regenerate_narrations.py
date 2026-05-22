#!/usr/bin/env python3
"""Regenerate brief/deep/voice narrations for each date using an LLM.

Input for each date YYYY-MM-DD:
  1. wiki/architecture/changelog/YYYY-MM-DD_changes.md (if present) — primary source
  2. Node labels from narration/data/nodes.json for that date — fallback / supplement
  3. A fixed project-context header that tells the LLM what C2A2 is

Output: rewrites data/narrations.json with clean prose that NEVER contains:
  - Raw CHANGE-YYYY-MM-DD-NNN ids
  - wiki/... or traditions/... file paths
  - "Added N files." or "Explored X traditions with N files." openers
  - IDs like FINDING-011a spoken as-is (rewritten as "the eleven-a finding",
    or simply paraphrased out).

Three variants per date:
  - brief (~60 words):  tight summary for a reviewer skimming
  - deep (~200 words):  one coherent paragraph — significance, not inventory
  - voice (~180 words): deep, rewritten for speech — no symbols, no acronyms
    spoken as letters, natural sentence rhythm

Providers:
  - anthropic (default): requires ANTHROPIC_API_KEY env var or --api-key
  - openai:              requires OPENAI_API_KEY env var or --api-key

Usage:
    python3 tools/regenerate_narrations.py                    # all dates
    python3 tools/regenerate_narrations.py --dates 2026-04-15
    python3 tools/regenerate_narrations.py --provider openai
    python3 tools/regenerate_narrations.py --dry-run          # print, don't write
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import sys
import time
from pathlib import Path

try:
    import urllib.request as _u
    import urllib.error as _ue
except ImportError:
    print("Need urllib (stdlib) — Python 3 required.", file=sys.stderr)
    sys.exit(1)


# ---- Fixed context the LLM always sees ----------------------------------

PROJECT_CONTEXT = """\
You are writing narration for a visualization of the C2A2 research project.

C2A2 is a system that treats eleven research traditions — each developed over
decades by a single thinker — as autonomous cognitive agents that can read,
reason about, and eventually respond to one another's work. The eleven:
Friston (active inference / free energy), Kastrup (analytic idealism),
Levin (bioelectric morphogenesis), Hoffman (interface theory), McGilchrist
(hemispheric cognition), Fredrickson (positive psychology / broaden-and-build),
Hawkins (Thousand Brains / Monty architecture), Stump (philosophical theology),
Carroll (naturalist physics), Arkani-Hamed (amplitudes), Wolfram (computational
reducibility). The target audience for this narration is a general reviewer —
intelligent, unfamiliar with the project, evaluating whether the system
produces anything of substance.

The visualization is a force-directed graph: every node is a wiki file;
categories are agents (purple), traditions (blue), architecture (orange),
findings/flags (red), decisions (green), review (yellow), master (teal),
inbox/deferred (grey). The graph reveals chronologically; your narration
plays over each day's reveal.

Eleven formal artifacts define the system:
  - FINDING-001 through FINDING-017: hypotheses the system surfaced
    (structural homology; explanatory bridge; observer-dependent boundary;
    etc.). FINDING-011 is the "triangular evidence" hypothesis linking
    Hoffman, Friston, and Kastrup; FINDING-011a extends it to a multi-vertex
    convergence including Levin and Hawkins.
  - DECISIONS documented in wiki/architecture/decisions.md.
  - PROPOSALS: papers, talks, or podcasts flagged by specialist agents for
    ingestion into the wiki; cleared from a queue by individual review or
    batch approval.
  - An automated pipeline (stages 14a → 14b → 15a → 15b → 15c) that surfaces,
    researches, and dispositions premises underlying the system's own claims.

Write for speech, not for documentation. No file paths, no raw IDs, no
"added N files" openers.
"""


# ---- Voice-mode style anchor --------------------------------------------
# Gold-standard example of voice narration, hand-authored for 2026-04-15.
# Every voice regeneration sees this as a cadence/register target.

VOICE_ANCHOR = """\
--- Voice anchor (gold-standard example for voice mode) ---

The following is the target voice for a day with strong conceptual content
(2026-04-15). Match its cadence, register, and willingness to name thinkers
and claims directly. Move from concrete (what happened) to conceptual (what
it meant). Do NOT reuse its sentences; do NOT force its conceptual material
onto days that don't have it. For quiet days, use the same voice to describe
infrastructure, housekeeping, or backlog clearing.

[begin anchor]
April fifteenth was a landmark session. A great many technical tasks were
accomplished. But the day's center of gravity was a larger pattern that had
been lurking under earlier work and finally came into focus. The original
triangle had three thinkers. Hoffman and Kastrup met along a philosophical
edge. Friston and Kastrup met along a structural edge, where the free energy
principle names the boundary condition of any complex system and Kastrup's
dissociative boundary between an alter and the universal mind names the same
cut. Hoffman and Friston met along a mathematical edge, where the trace logic
of interface theory meets the formal grammar of Markov blankets. Three pairs,
three independent paths to one claim.

Then the triangle widened. Levin's cognitive light cone, the reach of a
cluster whose cells are reprogrammed to read the same bioelectric goal as
their own, anchored the boundary condition in living biology. A limb cell
cluster sees the limb's target shape but not the frog's, and that difference
is where the self begins. Hawkins' thousand brains, where roughly a thousand
cortical columns are active in parallel, each a whole that processes the
whole, each with its own cognitive light cone, voting through the hemisphere
and ultimately the paired brain, anchored the same architecture in cognition.
That same architecture has now been implemented in a working artificial
intelligence called Monty. The boundary is a cognitive light cone at every
scale, and which scale counts as the agent depends on where the observer
sets their grip. Across all eleven traditions, the overarching research
program is the same. Show that the entire system points at a monism that
takes mind as the primitive.
[end anchor]
"""


# ---- Per-date source assembly -------------------------------------------

def load_changelog(repo_root: Path, date: str) -> str | None:
    p = repo_root / "wiki" / "architecture" / "changelog" / f"{date}_changes.md"
    if p.exists():
        return p.read_text(encoding="utf-8")
    return None


def load_proposals_for_date(repo_root: Path, date: str) -> list[tuple[str, str]]:
    inbox = repo_root / "wiki" / "inbox"
    results = []
    for f in sorted(inbox.glob(f"{date}_*.md")):
        label = f.stem[len(date) + 1:]  # strip date prefix + underscore
        text = f.read_text(encoding="utf-8")
        snippet = text.strip()[:400]
        results.append((label, snippet))
    return results


def load_decisions_for_date(repo_root: Path, date: str) -> list[str]:
    p = repo_root / "wiki" / "architecture" / "decisions.md"
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    blocks = []
    current: list[str] = []
    in_block = False
    for line in text.splitlines():
        if line.startswith("DECISION-"):
            if current and in_block:
                blocks.append("\n".join(current))
            current = [line]
            in_block = True
        elif in_block:
            current.append(line)
    if current and in_block:
        blocks.append("\n".join(current))
    return [b for b in blocks if f"  Date: {date}" in b]


def load_findings_for_date(repo_root: Path, date: str) -> list[str]:
    p = repo_root / "wiki" / "flags" / "pattern_detector_findings.md"
    if not p.exists():
        return []
    text = p.read_text(encoding="utf-8")
    blocks = []
    current: list[str] = []
    in_block = False
    for line in text.splitlines():
        if line.startswith("FINDING-"):
            if current and in_block:
                blocks.append("\n".join(current))
            current = [line]
            in_block = True
        elif in_block:
            current.append(line)
    if current and in_block:
        blocks.append("\n".join(current))
    return [b for b in blocks if f"Date evaluated: {date}" in b]


def load_cross_signals_for_date(repo_root: Path, date: str) -> list[tuple[str, str]]:
    flags = repo_root / "wiki" / "flags"
    results = []
    for f in sorted(flags.glob(f"cross_signals_{date}_*.md")):
        content = f.read_text(encoding="utf-8")
        results.append((f.name, content))
    return results


def per_date_extras(repo_root: Path, date: str) -> str:
    proposals = load_proposals_for_date(repo_root, date)
    decisions = load_decisions_for_date(repo_root, date)
    findings = load_findings_for_date(repo_root, date)
    cross_signals = load_cross_signals_for_date(repo_root, date)

    if not proposals and not decisions and not findings and not cross_signals:
        return "(no proposals, decisions, findings, or cross-signals dated to this day)"

    parts = []

    cap = min(len(proposals), 10)
    parts.append(f"PROPOSALS filed this day ({cap}):")
    if proposals:
        for label, snippet in proposals[:10]:
            first_line = snippet.splitlines()[0].strip() if snippet else ""
            parts.append(f"  {label}: {first_line[:120]}")
    else:
        parts.append("  (none)")

    parts.append(f"\nDECISIONS recorded this day ({len(decisions)}):")
    if decisions:
        for b in decisions:
            parts.append(b)
            parts.append("")
    else:
        parts.append("  (none)")

    parts.append(f"\nPATTERN-DETECTOR FINDINGS evaluated this day ({len(findings)}):")
    if findings:
        for b in findings:
            parts.append(b)
            parts.append("")
    else:
        parts.append("  (none)")

    parts.append(f"\nCROSS-SIGNAL ROLLUPS created this day ({len(cross_signals)}):")
    if cross_signals:
        for fname, content in cross_signals:
            parts.append(f"  [{fname}]")
            parts.append(content[:800])
            parts.append("")
    else:
        parts.append("  (none)")

    return "\n".join(parts)


def node_summary_for_date(nodes_path: Path, date: str) -> str:
    """Group that date's new files by top-level directory; return a human list."""
    nodes = json.loads(nodes_path.read_text())
    by_dir: dict[str, list[str]] = collections.defaultdict(list)
    for n in nodes:
        if n.get("date") != date:
            continue
        d = n.get("directory", "root")
        # Use first two path segments for grouping (e.g. traditions/friston)
        parts = d.split("/")
        top = "/".join(parts[:2]) if parts[0] == "traditions" else parts[0]
        by_dir[top].append(n.get("label") or n.get("id") or "(unlabelled)")
    if not by_dir:
        return "(no new files recorded for this date)"
    lines = []
    for d, labs in sorted(by_dir.items()):
        if len(labs) <= 5:
            lines.append(f"  {d}: {', '.join(labs)}")
        else:
            head = ", ".join(labs[:4])
            lines.append(f"  {d}: {head}, and {len(labs) - 4} more")
    return "\n".join(lines)


# ---- LLM prompt ----------------------------------------------------------

USER_PROMPT_TEMPLATE = """\
Generate narration for date: {date}

{project_context}

--- Source material for {date} ---

Changelog file ({changelog_status}):
{changelog_block}

New files added this day, grouped by area:
{node_block}

Additional source material for {date}:
{date_extras}

--- Your task ---

Produce a JSON object (and nothing else) with keys "brief", "deep", "voice".

brief (40-70 words, prose, one short paragraph):
  The reviewer hears this in ~20 seconds. What MATTERS about this day?
  If it was a quiet / seeding day, say so plainly.

deep (150-220 words, prose, one paragraph, maybe two):
  The reviewer hears this in ~90 seconds. Name the significance, not the
  inventory. If a finding was recorded, what is it a finding OF? If a
  decision was made, what question did it answer? If the day was
  infrastructure or backlog clearing, say so and explain why it mattered
  for what came next. Write in past tense.

voice (same content as deep, adapted for speech):
  Rewrite "deep" with no hyphens, no em-dashes, no parentheticals, no
  file paths, no raw IDs. Spell out anything the TTS would mangle:
  "FEP" → "free energy principle"; "FINDING-011a" → "the eleven-a finding"
  or just "the finding"; arrows "→" → "to"; slashes → "and". Sentences
  should be shorter than in "deep" — the listener has no backtracking.

{voice_anchor}

Do NOT include CHANGE-YYYY-MM-DD-NNN codes.
Do NOT include wiki/... paths.
Do NOT open with "Added N files" or "Explored X traditions".
Do NOT use raw IDs (DECISION-NNN, FINDING-NNN, PROPOSAL-NNN) in the text —
  paraphrase them into plain language.
Do include: named thinkers, the character of the work, and — where present
  — a concrete intellectual result.

Return ONLY the JSON object, no prose around it.
"""


def build_user_prompt(date: str, changelog: str | None, node_summary: str, repo_root: Path) -> str:
    changelog_status = "present" if changelog else "NOT PRESENT for this date"
    changelog_block = (
        changelog.strip() if changelog
        else "(no changelog for this date — rely on node list and infer the day's character)"
    )
    return USER_PROMPT_TEMPLATE.format(
        date=date,
        project_context=PROJECT_CONTEXT,
        changelog_status=changelog_status,
        changelog_block=changelog_block,
        node_block=node_summary,
        date_extras=per_date_extras(repo_root, date),
        voice_anchor=VOICE_ANCHOR,
    )


# ---- Provider adapters ---------------------------------------------------

def call_anthropic(prompt: str, api_key: str, model: str = "claude-opus-4-7") -> str:
    body = {
        "model": model,
        "max_tokens": 1500,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = _u.Request(
        "https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        method="POST",
    )
    try:
        with _u.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except _ue.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {err_body[:1000]}") from None
    # content is a list of blocks; concatenate any text blocks
    return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def call_openai(prompt: str, api_key: str, model: str = "gpt-4o") -> str:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.4,
        "response_format": {"type": "json_object"},
    }
    req = _u.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with _u.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


# ---- JSON extraction (robust to stray prose) ----------------------------

def extract_json(text: str) -> dict:
    """Pull the first {...} block out of the LLM response."""
    text = text.strip()
    # strip code fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        if text.endswith("```"):
            text = text.rsplit("```", 1)[0]
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object found in response:\n{text[:300]}")
    return json.loads(text[start : end + 1])


# ---- Main ----------------------------------------------------------------

def main():
    here = Path(__file__).resolve().parent.parent  # narration/
    repo_root = here.parent
    nodes_path = here / "data" / "nodes.json"
    narrations_path = here / "data" / "narrations.json"

    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["anthropic", "openai"], default="anthropic")
    ap.add_argument("--api-key", default=None)
    ap.add_argument("--model", default=None,
                    help="override model (default: claude-opus-4-6 / gpt-4o)")
    ap.add_argument("--dates", nargs="*", default=None,
                    help="only regenerate these dates (default: all in narrations.json)")
    ap.add_argument("--dry-run", action="store_true", help="print, don't write")
    ap.add_argument("--sleep", type=float, default=0.5,
                    help="pause between calls (seconds)")
    args = ap.parse_args()

    api_key = args.api_key or os.environ.get(
        "ANTHROPIC_API_KEY" if args.provider == "anthropic" else "OPENAI_API_KEY"
    )
    if not api_key:
        env = "ANTHROPIC_API_KEY" if args.provider == "anthropic" else "OPENAI_API_KEY"
        print(f"error: no API key. set ${env} or pass --api-key", file=sys.stderr)
        sys.exit(2)

    narrations = json.loads(narrations_path.read_text())
    dates = args.dates or sorted(narrations.keys())

    model = args.model or ("claude-opus-4-7" if args.provider == "anthropic" else "gpt-4o")
    call = call_anthropic if args.provider == "anthropic" else call_openai

    print(f"regenerating {len(dates)} dates via {args.provider}:{model}")
    for i, date in enumerate(dates, 1):
        changelog = load_changelog(repo_root, date)
        node_sum = node_summary_for_date(nodes_path, date)
        prompt = build_user_prompt(date, changelog, node_sum, repo_root)
        print(f"[{i}/{len(dates)}] {date}  changelog={'Y' if changelog else 'N'}"
              f"  prompt={len(prompt)}ch  ... ", end="", flush=True)
        try:
            raw = call(prompt, api_key, model)
            parsed = extract_json(raw)
        except Exception as e:
            print(f"FAIL: {e}")
            continue
        for k in ("brief", "deep", "voice"):
            if k not in parsed:
                print(f"WARN: missing key {k!r}")
                parsed[k] = parsed.get("deep", "")
        wc = len(parsed.get("voice", "").split())
        print(f"ok ({wc}w voice)")
        narrations[date] = {
            "brief": parsed["brief"].strip(),
            "deep": parsed["deep"].strip(),
            "voice": parsed["voice"].strip(),
        }
        if args.sleep:
            time.sleep(args.sleep)

    if args.dry_run:
        print("\n--- dry run, not writing ---")
        for d in dates:
            print(f"\n=== {d} ===")
            print(json.dumps(narrations[d], indent=2))
        return

    narrations_path.write_text(json.dumps(narrations, indent=2, ensure_ascii=False) + "\n")
    print(f"\nwrote {narrations_path}")


if __name__ == "__main__":
    main()
