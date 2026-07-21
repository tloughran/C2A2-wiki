#!/usr/bin/env python3
"""
janitor.py — Weekly polish-and-surface pass over the C2A2 wiki vault.

Catches imperfections in a working system (broken wikilinks, sync drift,
stale WIP, undated nodes, etc.), auto-fixes a tiny safelist of safe categories
(trailing whitespace, .DS_Store), and reports everything else to a markdown
findings file for triage. Designed to fold into morning-system-health.

Design rules:
  - Baseline-then-deltas: first run snapshots all findings as accepted noise;
    subsequent weeks flag only deltas.
  - Auto-fix is whitelisted explicitly. Categories promote one at a time after
    clean runs. Any destructive category is permanently notify-only.
  - Sewing-agent owns orphan/sparse detection (wiki/architecture/metrics/
    connectivity_log.csv) — janitor does not duplicate it.

Usage:
    python3 janitor.py                    # run with current state
    python3 janitor.py --baseline         # force a fresh baseline snapshot
    python3 janitor.py --dry-run          # report only; skip auto-fix writes
    python3 janitor.py --promote <check>  # promote a check to auto-fix safelist
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

# --- Configuration -----------------------------------------------------------
# Paths auto-detect between the real Mac filesystem and the sandbox mount, so
# the same script runs from both the scheduled task (Mac paths) and dry-runs
# inside a Cowork session (sandbox mounts).

_MAC_ROOT     = Path("/Users/tomloughran/Documents/Claude/Projects")

def _detect_sandbox_root() -> Path:
    # Auto-detect the live Cowork session mount instead of hardcoding a session
    # id (which goes stale every new session). Pick the mount that actually
    # contains this project.
    if Path("/sessions").exists():
        for mnt in sorted(Path("/sessions").glob("*/mnt")):
            if (mnt / "RC Karpathy Wiki Project").exists():
                return mnt
    return _MAC_ROOT

_SANDBOX_ROOT = _detect_sandbox_root()
_ROOT = _MAC_ROOT if _MAC_ROOT.exists() else _SANDBOX_ROOT

PROJECT_ROOT = _ROOT / "RC Karpathy Wiki Project"
VAULT_DIR    = PROJECT_ROOT / "wiki"
SUMMA_SRC    = _ROOT / "Summa 2026 in a Year" / "vault"
SUMMA_PUB    = VAULT_DIR / "vault"
JANITOR_DIR  = PROJECT_ROOT / "janitor"
STATE_PATH   = JANITOR_DIR / "state.json"
FINDINGS_MD  = JANITOR_DIR / "findings.md"

# Auto-fix safelist (severity=safe). New categories MUST start as report-only
# and be promoted via --promote after at least one clean run.
DEFAULT_AUTO_FIX = {"trailing_whitespace", "ds_store"}

# Any check that deletes content is destructive — permanent notify-only.
DESTRUCTIVE_CHECKS = {"empty_section", "dead_end_wikilink"}

# How old (days) an uncommitted file must be to count as "stale WIP".
WIP_STALE_DAYS = 14

# Files / dirs to skip when walking the vault.
SKIP_DIRS = {".git", ".obsidian", "__pycache__", "node_modules", ".trash"}
SKIP_FILE_GLOBS = {"_fs_probe_test.tmp"}

WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:[#|][^\]]*)?\]\]")
H1_RE       = re.compile(r"^\#\s+(.+)$", re.MULTILINE)

# --- Drift detection config (fact_inventory.md R5) ---------------------------
# Machine-readable allowlist of INTENTIONAL variance (hazard H1). Without it the
# drift checks would flag deliberate differences (e.g. MacIntyre's intentional
# exclusion) as bugs. See scripts/drift_allowlist.json.
DRIFT_ALLOWLIST_PATH = PROJECT_ROOT / "scripts" / "drift_allowlist.json"

# The three hand-maintained tradition palettes (fact_inventory.md Family 3).
# Each pipeline stores its color map in a DIFFERENT shape, so each gets a
# structure-scoped extractor rather than a blanket `#hex` grep — several of these
# files embed HTML/CSS templates whose colors would otherwise be swept in.
_HEX = r"(#[0-9A-Fa-f]{6})"

def _palette_gen_viz(text):
    # generate_visualization.py:  'traditions/<name>': '#RRGGBB',
    return {n.lower(): h.upper() for n, h in
            re.findall(r"'traditions/([a-z-]+)'\s*:\s*'" + _HEX + r"'", text)}

def _palette_prs3d(text):
    # extract_prs_data.py:  THINKER_COLORS = { "<name>": "#RRGGBB", ... }
    blk = re.search(r"THINKER_COLORS\s*=\s*\{(.*?)\}", text, re.DOTALL)
    if not blk:
        return {}
    return {n.lower(): h.upper() for n, h in
            re.findall(r'"([a-z-]+)"\s*:\s*"' + _HEX + r'"', blk.group(1))}

def _palette_bundle(text):
    # build_bundle.py:  ("<name>", [...aliases...], [...], "#RRGGBB"),
    return {n.lower(): h.upper() for n, h in
            re.findall(r'\(\s*"([a-z-]+)"\s*,.*?"' + _HEX + r'"\s*\)', text)}

# (pipeline id, path relative to PROJECT_ROOT, extractor). The id is what the
# allowlist's `absent_from` refers to.
PALETTE_PIPELINES = [
    ("gen_viz", "wiki/c2a2-wiki-narration/scripts/generate_visualization.py", _palette_gen_viz),
    ("prs3d",   "wiki/c2a2-prs-3d/scripts/extract_prs_data.py",               _palette_prs3d),
    ("bundle",  "wiki/commentary-explorer/scripts/build_bundle.py",           _palette_bundle),
]

# 'master' is the central synthesis node, not a per-tradition tint; pipelines
# legitimately differ on whether they carry it, so it is outside the palette
# agreement universe (not an allowlist case — it is categorically not a tradition).
_PALETTE_NON_TRADITIONS = {"master"}

# --- Roster drift config (fact_inventory.md Family 1 / R5) -------------------
# Four published surfaces describe "the agents", and they measure DIFFERENT
# universes, so raw count-equality across all four is NOT a valid invariant
# (hazard H2 — the two-scheduling-worlds finding):
#   * agents_tab.html AGENTS array = the full DISPLAY roster (OpenStory + launchd
#     + Cowork agents) that the schedule animation draws.
#   * agent_map.json = the OpenStory-only CANONICAL roster; it is the telemetry
#     join's declared source of truth (extract_openstory_agent_data.py:13).
#   * FRIENDLY_NAMES = a display-name lookup WITH a code fallback (fname()), so it
#     may legitimately omit an agent.
#   * TELEMETRY.roster_size = generated as len(agent_map) at telemetry-build time
#     (extract_openstory_agent_data.py:337), so it shares agent_map's universe.
# This check asserts only invariants that hold WITHIN a shared universe, and
# treats display-only agents (launchd/Cowork, no OpenStory sessions) as
# allowlistable via drift_allowlist.json['roster_display_only'] rather than bugs.
AGENTS_TAB_PATH = PROJECT_ROOT / "wiki" / "agents_tab.html"
AGENT_MAP_PATH  = PROJECT_ROOT / "wiki" / "agents" / "openstory" / "agent_map.json"

# taskIds are normal kebab ids OR reverse-DNS launchd labels (dots + mixed case),
# e.g. com.tomloughran.openstory.watchdog — the charset must admit both.
_TASKID = r"[A-Za-z0-9._-]+"


def _extract_agents_taskids(html):
    """Ordered taskId list from the `const AGENTS = [ ... ];` array. Order and
    duplicates are preserved so a duplicated entry surfaces. Returns None if the
    array cannot be located (structure changed under the extractor)."""
    m = re.search(r"const AGENTS\s*=\s*\[(.*?)\n\];", html, re.DOTALL)
    if not m:
        return None
    return re.findall(r"taskId\s*:\s*[\"'](" + _TASKID + r")[\"']", m.group(1))


def _extract_friendly_keys(html):
    """Keys of the `const FRIENDLY_NAMES = { ... };` display-name map (both quote
    styles are used in the file). None if the map cannot be located."""
    m = re.search(r"const FRIENDLY_NAMES\s*=\s*\{(.*?)\n\};", html, re.DOTALL)
    if not m:
        return None
    return re.findall(r"[\"'](" + _TASKID + r")[\"']\s*:", m.group(1))


def _extract_telemetry_alias(html):
    """The page's own display-taskId -> telemetry-taskId map (TELEMETRY_ALIAS),
    which papers over the c2a2-/c282- daily-run name drift. Read from source so
    the detector normalizes roster membership EXACTLY the way the page does,
    rather than duplicating the mapping. Empty dict if absent."""
    m = re.search(r"const TELEMETRY_ALIAS\s*=\s*\{(.*?)\}", html, re.DOTALL)
    if not m:
        return {}
    return dict(re.findall(
        r"[\"'](" + _TASKID + r")[\"']\s*:\s*[\"'](" + _TASKID + r")[\"']",
        m.group(1)))


def _extract_roster_size(html):
    """The published TELEMETRY blob's `_meta.roster_size`. Anchored on the
    TELEMETRY_DATA_END marker (the blob has nested braces, so a non-greedy `}`
    match would truncate). None if absent/unparseable."""
    m = re.search(
        r"const TELEMETRY\s*=\s*(\{.*\});\s*\n\s*/\* TELEMETRY_DATA_END \*/",
        html, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(1))["_meta"]["roster_size"]
    except (json.JSONDecodeError, KeyError, TypeError):
        return None


# --- Utilities ---------------------------------------------------------------

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {
        "version": 1,
        "first_run_at": None,
        "last_run_at": None,
        "last_read_at": None,
        "baseline_ids": [],
        "auto_fix_promoted": sorted(DEFAULT_AUTO_FIX),
        "fix_history": [],
        "run_counter": 0,
    }


def save_state(state: dict) -> None:
    JANITOR_DIR.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True))


def load_drift_allowlist() -> dict:
    """Load the intentional-variance allowlist (H1). Missing/unparseable file is
    treated as an empty allowlist — a drift check must still run and report, just
    without any suppressions, rather than crash."""
    try:
        return json.loads(DRIFT_ALLOWLIST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def walk_md(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn in SKIP_FILE_GLOBS:
                continue
            if fn.endswith(".md"):
                yield Path(dirpath) / fn


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(p)


# --- Finding type ------------------------------------------------------------

class Finding:
    __slots__ = ("check", "scope", "detail", "severity", "note")

    def __init__(self, check: str, scope: str, detail: str,
                 severity: str = "info", note: str = ""):
        self.check = check
        self.scope = scope
        self.detail = detail
        self.severity = severity
        self.note = note

    @property
    def fid(self) -> str:
        return f"{self.check}::{self.scope}::{self.detail}"

    def to_dict(self) -> dict:
        return {
            "check": self.check, "scope": self.scope, "detail": self.detail,
            "severity": self.severity, "note": self.note, "fid": self.fid,
        }


# --- Checks: auto-fix safelist ----------------------------------------------

def check_trailing_whitespace(apply_fix: bool):
    """Trim trailing whitespace from .md files in the vault."""
    findings, fixes = [], []
    for path in walk_md(VAULT_DIR):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        new_lines, touched = [], False
        for line in text.splitlines(keepends=False):
            stripped = line.rstrip()
            if stripped != line:
                touched = True
            new_lines.append(stripped)
        if touched:
            findings.append(Finding(
                "trailing_whitespace", rel(path),
                "trailing whitespace on one or more lines", "safe",
            ))
            if apply_fix:
                new_text = "\n".join(new_lines)
                if text.endswith("\n"):
                    new_text += "\n"
                path.write_text(new_text, encoding="utf-8")
                fixes.append((path, "trimmed"))
    return findings, fixes


def check_ds_store(apply_fix: bool):
    """Remove stray .DS_Store files anywhere under the vault."""
    findings, fixes = [], []
    for dirpath, _dirnames, filenames in os.walk(VAULT_DIR):
        for fn in filenames:
            if fn == ".DS_Store":
                p = Path(dirpath) / fn
                findings.append(Finding(
                    "ds_store", rel(p), "stray .DS_Store", "safe",
                ))
                if apply_fix:
                    try:
                        p.unlink()
                        fixes.append((p, "deleted"))
                    except OSError as e:
                        fixes.append((p, f"unlink-failed:{e}"))
    return findings, fixes


# --- Checks: report-only -----------------------------------------------------

def check_reindexer_freshness():
    """
    Synthesis files for Days that aren't yet marked available=true in
    refs/summa_index.json. Surfaces "Day-NNN written but reindexer hasn't run."
    """
    findings = []
    syn_dir = SUMMA_SRC / "synthesis"
    idx_path = SUMMA_SRC / "refs" / "summa_index.json"
    if not syn_dir.exists() or not idx_path.exists():
        return findings
    try:
        idx = json.loads(idx_path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        findings.append(Finding(
            "reindexer_freshness", rel(idx_path), f"index unreadable: {e}", "warn"
        ))
        return findings
    available_days = set()
    # summa_index.json is a dict keyed by article id (e.g. "I.Q1.A1"); iterate values, not keys.
    for entry in idx.values():
        if entry.get("available") and entry.get("day") is not None:
            available_days.add(int(entry["day"]))
    day_pat = re.compile(r"^Day-(\d{3})")
    syn_days = set()
    for p in syn_dir.glob("Day-*.md"):
        m = day_pat.match(p.name)
        if m:
            syn_days.add(int(m.group(1)))
    missing = sorted(syn_days - available_days)
    for d in missing:
        findings.append(Finding(
            "reindexer_freshness", "Summa 2026 in a Year/vault/refs/summa_index.json",
            f"Day-{d:03d} synthesis exists but not in index", "warn",
            note="rebuild via build_index.py (canonical) or run sync_vault.sh",
        ))
    return findings


def check_src_pub_refs_sync():
    """Files in source vault's refs/ that aren't in the published wiki/vault/refs/."""
    findings = []
    src = SUMMA_SRC / "refs"
    pub = SUMMA_PUB / "refs"
    if not src.exists() or not pub.exists():
        return findings
    src_files = {p.name for p in src.iterdir() if p.is_file()}
    pub_files = {p.name for p in pub.iterdir() if p.is_file()}
    for fn in sorted(src_files - pub_files):
        findings.append(Finding(
            "src_pub_refs_drift", "wiki/vault/refs/",
            f"missing {fn} (present in SRC)", "warn",
            note="sync_vault.sh only rsyncs transcripts/+synthesis/",
        ))
    return findings


def check_stale_wip():
    """Uncommitted files in the project older than WIP_STALE_DAYS."""
    findings = []
    try:
        out = subprocess.run(
            ["git", "-C", str(PROJECT_ROOT), "status", "--porcelain=v1"],
            capture_output=True, text=True, check=True, timeout=20,
        ).stdout
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired,
            FileNotFoundError):
        return findings
    now = datetime.now().timestamp()
    cutoff = WIP_STALE_DAYS * 86400
    seen = set()
    for line in out.splitlines():
        # porcelain v1: XY <path>  ; deletions / renames have different shape
        if len(line) < 4:
            continue
        path_part = line[3:].split(" -> ")[-1].strip().strip('"')
        if path_part in seen:
            continue
        seen.add(path_part)
        fp = PROJECT_ROOT / path_part
        if not fp.exists():
            continue
        try:
            age = now - fp.stat().st_mtime
        except OSError:
            continue
        if age > cutoff:
            days = int(age / 86400)
            findings.append(Finding(
                "stale_wip", path_part,
                f"uncommitted, mtime {days}d old", "info",
            ))
    return findings


def check_undated_refs_nodes():
    """Summa refs/* synthesis-style nodes that won't appear on the date slider."""
    findings = []
    refs_dir = SUMMA_PUB / "refs"
    if not refs_dir.exists():
        return findings
    skip_names = {"summa_index.json", "playlist.json", "missing_days.md"}
    for p in refs_dir.iterdir():
        if not p.is_file():
            continue
        if p.name in skip_names:
            continue
        if not p.name.endswith(".md"):
            continue
        findings.append(Finding(
            "undated_refs_node", rel(p),
            "no Gregorian date → invisible when date slider moves", "info",
            note="design call: opt into mtime, or treat empty-date as always-visible",
        ))
    return findings


def _build_name_index():
    """Map lowercased basename(stem) -> [actual_stems...] for the whole vault."""
    idx = defaultdict(list)
    for p in walk_md(VAULT_DIR):
        idx[p.stem.lower()].append(p.stem)
    return idx


def check_broken_wikilinks(name_index):
    """[[Target]] where Target doesn't resolve to any .md stem (case-insensitive)."""
    findings = []
    for path in walk_md(VAULT_DIR):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target or target.startswith("http"):
                continue
            # Tail of a path-style link
            tail = target.rsplit("/", 1)[-1]
            if tail.lower() not in name_index:
                findings.append(Finding(
                    "broken_wikilink", rel(path),
                    f"[[{target}]] has no matching file", "warn",
                ))
    return findings


def check_wikilink_case_mismatch(name_index):
    """[[Target]] that resolves only with case adjustment."""
    findings = []
    for path in walk_md(VAULT_DIR):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if not target or target.startswith("http"):
                continue
            tail = target.rsplit("/", 1)[-1]
            actual = name_index.get(tail.lower())
            if not actual:
                continue
            if tail not in actual:
                findings.append(Finding(
                    "wikilink_case_mismatch", rel(path),
                    f"[[{target}]] → should be one of {actual}", "warn",
                ))
    return findings


def check_duplicate_h1():
    """Same H1 title across multiple files. Surfaces accidental copies / divergence."""
    findings = []
    by_title = defaultdict(list)
    for path in walk_md(VAULT_DIR):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        m = H1_RE.search(text)
        if not m:
            continue
        title = m.group(1).strip()
        if title:
            by_title[title].append(path)
    for title, paths in by_title.items():
        if len(paths) > 1:
            paths_str = ", ".join(rel(p) for p in sorted(paths))
            findings.append(Finding(
                "duplicate_h1", f"H1: {title}",
                f"{len(paths)} files share this title: {paths_str}", "info",
            ))
    return findings


# --- Checks: drift detection (fact_inventory.md R5) --------------------------

def check_palette_drift():
    """Cross-pipeline tradition-color agreement (fact_inventory.md Family 3).

    Three pipelines hand-maintain the same tradition palette. Two of them
    assigning DIFFERENT hexes to one tradition is a real hand-copy bug (Class B
    drift) -> `palette_hex_mismatch` (warn), never allowlistable. A tradition
    defined in some pipelines but missing from another -> `palette_hex_absent`
    (info), suppressed when declared intentional in
    drift_allowlist.json['palette_absence'] (H1). Read-only; no writes, no git,
    so it is idempotent and lock-safe (H6).
    """
    findings = []
    maps = {}
    for pid, relpath, extractor in PALETTE_PIPELINES:
        try:
            text = (PROJECT_ROOT / relpath).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            findings.append(Finding(
                "palette_drift", relpath,
                "palette pipeline file missing/unreadable — moved or renamed?",
                "warn"))
            continue
        m = extractor(text)
        if not m:
            findings.append(Finding(
                "palette_drift", relpath,
                "no tradition palette extracted — the file's structure may have "
                "changed out from under the extractor", "warn",
                note="update the matching _palette_* extractor in janitor.py"))
        maps[pid] = m

    if len(maps) < 2:
        return findings  # need at least two pipelines to compare

    allow = load_drift_allowlist()
    absent_ok = {(e.get("tradition", "").lower(), e.get("absent_from", ""))
                 for e in allow.get("palette_absence", [])}

    traditions = set().union(*maps.values()) - _PALETTE_NON_TRADITIONS
    for trad in sorted(traditions):
        present = {pid: m[trad] for pid, m in maps.items() if trad in m}
        # Mismatch: the pipelines that DO define it disagree on the hex.
        distinct = sorted(set(present.values()))
        if len(distinct) > 1:
            where = ", ".join(f"{pid}={present[pid]}" for pid in sorted(present))
            findings.append(Finding(
                "palette_hex_mismatch", f"tradition:{trad}",
                f"{len(distinct)} hexes for one tradition across pipelines: {where}",
                "warn",
                note="hand-copied palette drift (Class B) — pick the canonical hex "
                     "and reconcile the sources (color choice is Tom's call)"))
        # Absence: defined somewhere, missing elsewhere, unless allowlisted.
        for pid in (p for p in maps if trad not in maps[p]):
            if (trad, pid) in absent_ok:
                continue
            deftext = ", ".join(f"{p}={present[p]}" for p in sorted(present))
            findings.append(Finding(
                "palette_hex_absent", f"tradition:{trad}",
                f"absent from pipeline '{pid}' but defined in: {deftext}", "info",
                note="if deliberate, declare it in "
                     "scripts/drift_allowlist.json['palette_absence']"))
    return findings


def _roster_findings(agents, friendly, roster_size, alias, map_ids, allow):
    """Pure roster-drift logic (no file/git I/O) so every branch is directly
    unit-testable. See the roster-drift config block for why cross-universe
    count-equality is deliberately NOT asserted.

    agents      -- ordered list of AGENTS taskIds (duplicates preserved)
    friendly    -- iterable of FRIENDLY_NAMES keys
    roster_size -- published TELEMETRY roster_size (int) or None
    alias       -- {display_id: telemetry_id} from TELEMETRY_ALIAS
    map_ids     -- iterable of agent_map.json taskIds (OpenStory canonical roster)
    allow       -- parsed drift_allowlist.json
    """
    findings = []
    agents_set = set(agents)
    friendly_set = set(friendly)
    map_set = set(map_ids)
    display_only = {e.get("taskId") for e in allow.get("roster_display_only", [])}

    # 1. Duplicate taskId inside AGENTS — never intentional.
    from collections import Counter
    for tid, n in sorted(Counter(agents).items()):
        if n > 1:
            findings.append(Finding(
                "roster_duplicate_taskid", f"agent:{tid}",
                f"taskId appears {n}x in the AGENTS array (must be unique)",
                "warn"))

    # 2. FRIENDLY_NAMES entry for a taskId not in AGENTS — a display name for an
    #    agent that no longer exists (stale/renamed). The reverse (an AGENT with
    #    no friendly name) is fine: fname() falls back, so it is not flagged.
    for tid in sorted(friendly_set - agents_set):
        findings.append(Finding(
            "roster_friendly_orphan", f"agent:{tid}",
            "FRIENDLY_NAMES defines a display name for a taskId not in AGENTS "
            "(stale entry, or the agent was renamed/removed)", "warn"))

    # 3. Published roster_size vs the canonical map size. Same universe:
    #    roster_size is generated as len(agent_map), so inequality means the
    #    injected TELEMETRY blob predates the current agent_map.
    if roster_size is not None and roster_size != len(map_set):
        findings.append(Finding(
            "roster_size_stale", "telemetry:roster_size",
            f"TELEMETRY roster_size={roster_size} but agent_map.json has "
            f"{len(map_set)} agents", "warn",
            note="roster_size is generated as len(agent_map); divergence means "
                 "agents_tab.html's injected TELEMETRY block is stale — "
                 "regenerate it (extract_openstory_agent_data.py + "
                 "inject_telemetry.py)"))

    # Normalize between the display universe and the telemetry/map universe
    # exactly the way the page does (TELEMETRY_ALIAS is display -> telemetry).
    rev_alias = {v: k for k, v in alias.items()}
    def display_id(tid):  # telemetry/map id -> the id used in AGENTS
        return rev_alias.get(tid, tid)
    def canon_id(tid):    # AGENTS id -> the id used in agent_map/telemetry
        return alias.get(tid, tid)

    # 4. Canonical map agent not present in the display roster (after alias
    #    normalization) — a tracked agent invisible in the animation. Real bug;
    #    the allowlist can never suppress this direction.
    for tid in sorted(map_set):
        if display_id(tid) not in agents_set:
            findings.append(Finding(
                "roster_map_not_displayed", f"agent:{tid}",
                "in the canonical agent_map.json roster but absent from the "
                "AGENTS display array (after TELEMETRY_ALIAS normalization)",
                "warn"))

    # 5. Display agent not in the OpenStory canonical map — EXPECTED for
    #    launchd/Cowork agents (they run no OpenStory sessions), so info +
    #    allowlistable rather than a bug. An un-allowlisted one still surfaces,
    #    because it may instead mean agent_map is stale.
    for tid in sorted(agents_set):
        if canon_id(tid) in map_set or tid in display_only:
            continue
        findings.append(Finding(
            "roster_display_extra", f"agent:{tid}",
            "in the AGENTS display roster but not in agent_map.json (the "
            "OpenStory canonical roster)", "info",
            note="if this agent is intentionally display-only (e.g. a launchd "
                 "job with no OpenStory sessions), declare it in "
                 "scripts/drift_allowlist.json['roster_display_only']; "
                 "otherwise agent_map.json may be stale"))
    return findings


def check_roster_drift():
    """Agent-roster agreement across agents_tab.html (the AGENTS array,
    FRIENDLY_NAMES, the injected TELEMETRY blob, and TELEMETRY_ALIAS) and
    agent_map.json (fact_inventory.md Family 1). Read-only; no writes, no git, so
    it is idempotent and lock-safe (H6).

    Only WITHIN-universe invariants are asserted; cross-universe count-equality is
    deliberately not one, because the display roster is a superset of the
    OpenStory canonical roster (hazard H2 — the two scheduling worlds).
    """
    findings = []
    try:
        html = AGENTS_TAB_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return [Finding(
            "roster_drift", rel(AGENTS_TAB_PATH),
            "agents_tab.html missing/unreadable — moved or renamed?", "warn")]

    agents = _extract_agents_taskids(html)
    friendly = _extract_friendly_keys(html)
    if agents is None:
        findings.append(Finding(
            "roster_drift", rel(AGENTS_TAB_PATH),
            "AGENTS array not found — the file's structure may have changed out "
            "from under the extractor", "warn",
            note="update _extract_agents_taskids in janitor.py"))
        return findings  # nothing else is comparable without the roster
    if friendly is None:
        findings.append(Finding(
            "roster_drift", rel(AGENTS_TAB_PATH),
            "FRIENDLY_NAMES map not found — structure may have changed", "warn",
            note="update _extract_friendly_keys in janitor.py"))

    alias = _extract_telemetry_alias(html)
    roster_size = _extract_roster_size(html)
    try:
        amap = json.loads(AGENT_MAP_PATH.read_text(encoding="utf-8"))
        map_ids = [a["taskId"] for a in amap.get("agents", [])]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError,
            TypeError):
        findings.append(Finding(
            "roster_drift", rel(AGENT_MAP_PATH),
            "agent_map.json missing/unreadable — cannot reconcile the roster",
            "warn", note="expected at wiki/agents/openstory/agent_map.json"))
        return findings

    allow = load_drift_allowlist()
    findings.extend(_roster_findings(
        agents, friendly or [], roster_size, alias, map_ids, allow))
    return findings


# --- Orchestration -----------------------------------------------------------

ALL_CHECKS = [
    # (name, function, takes_apply_fix_arg, takes_name_index_arg)
    ("trailing_whitespace",     check_trailing_whitespace,   True,  False),
    ("ds_store",                check_ds_store,              True,  False),
    ("reindexer_freshness",     check_reindexer_freshness,   False, False),
    ("src_pub_refs_drift",      check_src_pub_refs_sync,     False, False),
    ("stale_wip",               check_stale_wip,             False, False),
    ("undated_refs_node",       check_undated_refs_nodes,    False, False),
    ("broken_wikilink",         check_broken_wikilinks,      False, True),
    ("wikilink_case_mismatch",  check_wikilink_case_mismatch, False, True),
    ("duplicate_h1",            check_duplicate_h1,          False, False),
    ("palette_drift",           check_palette_drift,         False, False),
    ("roster_drift",            check_roster_drift,          False, False),
]


def run_checks(state: dict, apply_fix_for: set, dry_run: bool):
    name_index = _build_name_index()
    all_findings = []
    fix_log = []  # (check, path, action)
    for name, fn, takes_fix, takes_idx in ALL_CHECKS:
        do_fix = (name in apply_fix_for) and not dry_run
        try:
            if takes_fix and takes_idx:
                fnd, fixes = fn(do_fix, name_index)
            elif takes_fix:
                fnd, fixes = fn(do_fix)
            elif takes_idx:
                fnd = fn(name_index)
                fixes = []
            else:
                fnd = fn()
                fixes = []
        except Exception as e:
            fnd = [Finding(name, "<check-error>", str(e), "error")]
            fixes = []
        all_findings.extend(fnd)
        for p, action in fixes:
            fix_log.append((name, rel(p), action))
    return all_findings, fix_log


def categorize(findings: list, baseline_ids: set):
    """Split findings into (baseline_still_open, new_since_baseline, fixed_this_run_eligible)."""
    open_now = {f.fid: f for f in findings}
    baseline = set(baseline_ids) & set(open_now)
    new      = set(open_now) - set(baseline_ids)
    return {fid: open_now[fid] for fid in baseline}, {fid: open_now[fid] for fid in new}


# --- Findings renderer -------------------------------------------------------

def render_findings(state, fixed_this_run, new_findings, baseline_open,
                    auto_fix_promoted, dry_run, is_baseline_run):
    lines = []
    lines.append("# C2A2 Wiki Janitor — Findings")
    lines.append("")
    lines.append(f"Last run: {state['last_run_at']}  ")
    lines.append(f"Run #: {state['run_counter']}  ")
    lines.append(f"Auto-fix categories: {', '.join(sorted(auto_fix_promoted)) or '(none)'}")
    if dry_run:
        lines.append("  ")
        lines.append("**DRY RUN** — no files written.")
    if is_baseline_run:
        lines.append("  ")
        lines.append("**BASELINE RUN** — all open findings recorded as accepted noise; "
                     "next run will flag only deltas.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Fixed this run
    lines.append("## Fixed this run")
    lines.append("")
    if fixed_this_run:
        by_check = defaultdict(list)
        for check, path, action in fixed_this_run:
            by_check[check].append((path, action))
        for check in sorted(by_check):
            lines.append(f"### {check}  ({len(by_check[check])} fixes)")
            for path, action in by_check[check][:50]:
                lines.append(f"- `{path}` — {action}")
            if len(by_check[check]) > 50:
                lines.append(f"- … and {len(by_check[check]) - 50} more")
            lines.append("")
    else:
        lines.append("_(nothing fixed this run)_")
        lines.append("")

    # New since last week — the section morning-system-health should ingest.
    lines.append("## New since last week")
    lines.append("<!-- morning-system-health: read this section -->")
    lines.append("")
    if new_findings:
        by_check = defaultdict(list)
        for f in new_findings.values():
            by_check[f.check].append(f)
        for check in sorted(by_check):
            sev_label = "destructive" if check in DESTRUCTIVE_CHECKS else (
                "auto-fix" if check in auto_fix_promoted else "report-only"
            )
            lines.append(f"### {check}  ({len(by_check[check])} new, {sev_label})")
            for f in by_check[check][:30]:
                note = f"  _({f.note})_" if f.note else ""
                lines.append(f"- `{f.scope}` — {f.detail}{note}")
            if len(by_check[check]) > 30:
                lines.append(f"- … and {len(by_check[check]) - 30} more")
            lines.append("")
    else:
        lines.append("_(no new findings since last week — clean delta)_")
        lines.append("")

    # All open (rolled up)
    lines.append("## All open findings (rollup)")
    lines.append("")
    all_open = {**baseline_open, **new_findings}
    if all_open:
        by_check = defaultdict(int)
        for f in all_open.values():
            by_check[f.check] += 1
        lines.append("| Check | Count | Mode |")
        lines.append("|---|---|---|")
        for check in sorted(by_check):
            mode = ("destructive (notify-only)" if check in DESTRUCTIVE_CHECKS
                    else "auto-fix" if check in auto_fix_promoted
                    else "report-only")
            lines.append(f"| `{check}` | {by_check[check]} | {mode} |")
        lines.append("")
    else:
        lines.append("_(no open findings — pristine)_")
        lines.append("")

    # Baseline (just a count — too noisy to list)
    lines.append(f"## Baseline (pre-existing, accepted noise): {len(baseline_open)} findings")
    lines.append("")
    lines.append("These were present on the first run and aren't re-listed each week. "
                 "They're carried forward until they go away or are intentionally addressed.")
    lines.append("")

    # Promotion record
    lines.append("---")
    lines.append("## Promotion log")
    lines.append("")
    lines.append("Promote a category to auto-fix:  ")
    lines.append("`python3 scripts/janitor.py --promote <check_name>`")
    lines.append("")
    lines.append("Currently promoted: " + ", ".join(sorted(auto_fix_promoted)))
    lines.append("")
    lines.append(f"Permanent notify-only (destructive): "
                 f"{', '.join(sorted(DESTRUCTIVE_CHECKS))}")

    return "\n".join(lines) + "\n"


# --- Main --------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", action="store_true",
                    help="Reset baseline_ids to current open findings.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Report only; do not perform any auto-fixes.")
    ap.add_argument("--promote", metavar="CHECK",
                    help="Add a check to the auto-fix safelist and exit.")
    args = ap.parse_args(argv)

    state = load_state()

    # --promote: mutate state, save, exit.
    if args.promote:
        check = args.promote
        if check in DESTRUCTIVE_CHECKS:
            print(f"refuse: {check} is permanently notify-only (destructive)",
                  file=sys.stderr)
            return 2
        valid = {name for name, *_ in ALL_CHECKS}
        if check not in valid:
            print(f"unknown check: {check}. known: {sorted(valid)}",
                  file=sys.stderr)
            return 2
        promoted = set(state.get("auto_fix_promoted", []))
        promoted.add(check)
        state["auto_fix_promoted"] = sorted(promoted)
        save_state(state)
        print(f"promoted: {check}. auto-fix now covers: "
              f"{', '.join(state['auto_fix_promoted'])}")
        return 0

    JANITOR_DIR.mkdir(parents=True, exist_ok=True)
    state["run_counter"] = state.get("run_counter", 0) + 1
    state["last_run_at"] = now_iso()
    if state.get("first_run_at") is None:
        state["first_run_at"] = state["last_run_at"]

    auto_fix_promoted = set(state.get("auto_fix_promoted", []) or DEFAULT_AUTO_FIX)

    findings, fix_log = run_checks(state, auto_fix_promoted, args.dry_run)

    # Baseline-then-deltas accounting.
    is_baseline_run = args.baseline or not state.get("baseline_ids")
    if is_baseline_run:
        state["baseline_ids"] = sorted({f.fid for f in findings})
        baseline_open = {f.fid: f for f in findings}
        new_findings = {}
    else:
        baseline_open, new_findings = categorize(findings, set(state["baseline_ids"]))

    md = render_findings(
        state=state,
        fixed_this_run=fix_log,
        new_findings=new_findings,
        baseline_open=baseline_open,
        auto_fix_promoted=auto_fix_promoted,
        dry_run=args.dry_run,
        is_baseline_run=is_baseline_run,
    )
    FINDINGS_MD.write_text(md, encoding="utf-8")

    # Append fix history (cap to last 200 entries).
    for check, path, action in fix_log:
        state.setdefault("fix_history", []).append({
            "run_at": state["last_run_at"], "check": check,
            "path": path, "action": action,
        })
    state["fix_history"] = state["fix_history"][-200:]
    save_state(state)

    print(f"janitor: {len(findings)} open findings, "
          f"{len(new_findings)} new since baseline, "
          f"{len(fix_log)} auto-fixes "
          f"({'dry-run' if args.dry_run else 'applied'}).")
    print(f"findings: {FINDINGS_MD}")
    print(f"state:    {STATE_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
