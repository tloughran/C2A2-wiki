#!/usr/bin/env bash
#
# regen_prs_testcorpus.sh
# Build the Narrative (PRS) Connectome over the DOMINO TEST FIXTURE — twenty landmark
# results, quantum mechanics 1900-1932 against deep learning 2012-2025, encoded as PRS
# triplets from Karpathy's domino image.
#
# WHY THIS EXISTS
#   The live corpus is ~95% recent, so it cannot exercise the axis. This fixture has a
#   125-year baseline and two traditions with disjoint technical vocabularies, which is
#   what surfaced the 2026-09-01 findings: a 33x rate distortion at the shipped tau, six
#   coils rendered as NaN, and zero cross-tradition links from lexical matching.
#   It is a FIXTURE, not vault content — these are not C2A2 research programs and they
#   are deliberately kept out of the live corpus and its counts.
#
# Builds BOTH arms so they can be read side by side:
#   prs_3d_test_tau90.html    the shipped axis (TAU_DAYS = 90)
#   prs_3d_test_linear.html   the control (tau -> infinity), the regression target
#
# Usage:  regen_prs_testcorpus.sh [REPO_ROOT]

set -euo pipefail

REPO="${1:-$(git rev-parse --show-toplevel)}"
WIKI="$REPO/wiki"
S="$WIKI/c2a2-prs-3d/scripts"
TPL="$WIKI/c2a2-prs-3d/template_prs_3d.html"
FIX="$WIKI/c2a2-prs-3d/testcorpus"
OUTDIR="$WIKI/c2a2-prs-3d/testcorpus"

mkdir -p "$OUTDIR"
DATA="$OUTDIR/prs_data_test.json"

echo "=== PRS test-corpus regen — $(date '+%Y-%m-%d %H:%M:%S') ==="

python3 "$S/extract_prs_data.py" "$FIX/vault" --thinker-map "$FIX/thinker_map.json" --out "$DATA"

for arm in tau90:90 linear:linear; do
  name="${arm%%:*}"; tau="${arm##*:}"
  out="$OUTDIR/prs_3d_test_${name}.html"
  echo "--- arm: $name (tau=$tau) ---"
  python3 "$S/generate_prs_3d.py" --tau "$tau" "$DATA" "$TPL" "$out"
  python3 "$S/validate_prs_3d.py" "$out" --source-data "$DATA"
  python3 "$REPO/scripts/prs_axis_max_share.py" "$out" | tail -8
done

cat <<EOF
RESULT: built both arms under $OUTDIR
  prs_3d_test_tau90.html   — shipped axis
  prs_3d_test_linear.html  — control
Serve the folder over HTTP and compare; do NOT open via file:// (the template loads
three.js from a CDN and the coil layer needs a real origin).
EOF
