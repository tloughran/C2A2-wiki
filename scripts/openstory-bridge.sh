#!/usr/bin/env bash
# openstory-bridge.sh — flatten Cowork + Claude Code session transcripts into the
# watch_dir/{project}/{session}.jsonl shape OpenStory's paths.rs expects.
#
# Why: OpenStory's path parser (rs/core/src/paths.rs) derives the project from the
# IMMEDIATE child of watch_dir and the session from the file stem. Cowork nests its
# transcripts as {uuid}/.claude/projects/{project}/{session}.jsonl (two levels too
# deep), so pointing watch_dir at the store directly mis-derives every id. This
# bridge symlinks each transcript into a flat {project}/{session}.jsonl root.
# The watcher's backfill uses WalkDir::follow_links(true), so symlinks are honored.
#
# Idempotent: re-running only adds/repairs links. Safe alongside a live instance
# (it never writes into the source stores; it only creates symlinks under WATCH_ROOT).
#
# Overridable via env (defaults target the real machine):
#   OPENSTORY_WATCH_ROOT  flat output root            (default ~/openstory-watch)
#   COWORK_ROOT           Cowork session store         (default ~/Library/.../local-agent-mode-sessions)
#   CC_ROOT               Claude Code projects root    (default ~/.claude/projects)
set -euo pipefail

WATCH_ROOT="${OPENSTORY_WATCH_ROOT:-$HOME/openstory-watch}"
COWORK_ROOT="${COWORK_ROOT:-$HOME/Library/Application Support/Claude/local-agent-mode-sessions}"
CC_ROOT="${CC_ROOT:-$HOME/.claude/projects}"

mkdir -p "$WATCH_ROOT"

linked=0; skipped=0; collisions=0

link_one() {
  # $1 = source .jsonl absolute path; $2 = project name; $3 = relative path within project
  local src="$1" proj="$2" rel="$3"
  local dst="$WATCH_ROOT/$proj/$rel"
  if [ -L "$dst" ] && [ -e "$dst" ]; then
    # An existing, resolvable link wins (first-wins, deterministic via sorted input).
    # Re-running therefore changes nothing. A different source for the same
    # project/session is a true collision (≈never, since session UUIDs are unique).
    [ "$(readlink "$dst")" = "$src" ] || collisions=$((collisions+1))
    skipped=$((skipped+1)); return
  fi
  # New, or a broken link to a moved/removed source — (re)create it.
  mkdir -p "$(dirname "$dst")"
  ln -sfn "$src" "$dst"
  linked=$((linked+1))
}

# Flatten every *.jsonl under a "{project}/..." base into WATCH_ROOT, preserving the
# in-project remainder (so {session}/subagents/agent-*.jsonl is carried verbatim).
process_base() {
  local base="$1"
  [ -d "$base" ] || return 0
  while IFS= read -r -d '' f; do
    local rel="${f#"$base"/}"   # project/.../session.jsonl
    case "$rel" in */*) ;; *) continue ;; esac   # skip files directly in base (no project)
    local proj="${rel%%/*}"     # first path segment
    local rest="${rel#*/}"      # remainder after "project/"
    link_one "$f" "$proj" "$rest"
  done < <(find "$base" -type f -name '*.jsonl' -print0 | sort -z)
}

# Source 1: Claude Code (~/.claude/projects/{project}/{session}.jsonl)
process_base "$CC_ROOT"

# Source 2: Cowork store. Each session nests its own projects root at
# {uuid1}/{uuid2}/local_{id}/.claude/projects (~depth 5), so don't bound depth —
# enumerate every .claude/projects base wherever it appears and flatten each.
if [ -d "$COWORK_ROOT" ]; then
  while IFS= read -r -d '' ccp; do
    process_base "$ccp"
  done < <(find "$COWORK_ROOT" -type d -path '*/.claude/projects' -print0 | sort -z)
fi

echo "bridge: linked=$linked skipped=$skipped collisions=$collisions root=$WATCH_ROOT"
