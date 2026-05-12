#!/usr/bin/env python3
"""
Validate generated HTML files for common template/embedding bugs.
Usage: python validate_html.py <html_file> [--source-data <json_file>]

Exit codes:
  0 = all checks pass
  1 = validation failures found
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def extract_inline_scripts(html: str) -> str:
    """Extract all inline JavaScript from <script> tags (skip external src= tags)."""
    scripts = []
    # Match <script> tags without src= attribute
    # Use negative lookahead to skip <script src=...>
    for match in re.finditer(r'<script>(.+?)</script>', html, re.DOTALL):
        scripts.append(match.group(1))
    return '\n'.join(scripts)


def check_js_syntax(html: str) -> list:
    """Check 1: Extract JS and validate with node --check."""
    errors = []
    js = extract_inline_scripts(html)
    if not js.strip():
        errors.append("WARNING: No inline JavaScript found in HTML")
        return errors

    tmp = Path('/tmp/_validate_html_js.js')
    tmp.write_text(js)

    result = subprocess.run(
        ['node', '--check', str(tmp)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        # Extract the specific error line
        stderr = result.stderr.strip()
        errors.append(f"FAIL: JavaScript syntax error\n{stderr}")
    else:
        print("  [PASS] JavaScript syntax valid")

    return errors


def check_double_braces(html: str) -> list:
    """Check 2: Detect {{ or }} in CSS and JS (outside JSON data)."""
    errors = []

    # Check CSS
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    if style_match:
        css = style_match.group(1)
        double_opens = [m.start() for m in re.finditer(r'\{\{', css)]
        double_closes = [m.start() for m in re.finditer(r'\}\}', css)]
        if double_opens or double_closes:
            errors.append(
                f"FAIL: CSS contains double braces "
                f"({{ x{len(double_opens)}, }} x{len(double_closes)}). "
                f"This breaks all CSS rules."
            )
        else:
            print("  [PASS] No double braces in CSS")

    # Check JS (excluding JSON data assignments like `const X = {...}`)
    js = extract_inline_scripts(html)
    if js:
        # Remove JSON data lines (const VAR = [...]  or const VAR = {...})
        # These legitimately contain }}
        js_no_data = re.sub(
            r'const \w+ = [\[\{].*?[\]\}];',
            '',
            js,
            flags=re.DOTALL
        )
        double_in_js = list(re.finditer(r'\$?\{\{|\}\}', js_no_data))
        if double_in_js:
            samples = []
            for m in double_in_js[:3]:
                pos = m.start()
                ctx = js_no_data[max(0, pos-20):pos+20].replace('\n', ' ')
                samples.append(f"  ...{ctx}...")
            errors.append(
                f"FAIL: JS code contains {len(double_in_js)} double-brace pattern(s) "
                f"outside data declarations:\n" + '\n'.join(samples)
            )
        else:
            print("  [PASS] No double braces in JS code")

    return errors


def check_css_braces(html: str) -> list:
    """Check 4: CSS brace balance."""
    errors = []
    style_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    if style_match:
        css = style_match.group(1)
        opens = css.count('{')
        closes = css.count('}')
        if opens != closes:
            errors.append(
                f"FAIL: CSS brace mismatch: {opens} open, {closes} close"
            )
        else:
            print(f"  [PASS] CSS braces balanced ({opens} pairs)")
    return errors


def check_data_integrity(html: str, source_path: str) -> list:
    """Check 3: Compare embedded data counts against source JSON."""
    errors = []

    with open(source_path) as f:
        data = json.load(f)

    # Extract stats from HTML
    html_stats = dict(re.findall(r'<span>(\d+) (\w+)</span>', html))

    # Build expected counts from source
    expected = {}
    files = data.get('files', [])
    expected['files'] = data.get('metadata', {}).get('total_files', len(files))
    expected['findings'] = len(data.get('findings', []))
    expected['decisions'] = len(data.get('decisions', []))

    for label, expected_count in expected.items():
        html_count = int(html_stats.get(label, -1))
        if html_count == -1:
            continue  # Label not in HTML, skip
        if html_count == 0 and expected_count > 0:
            errors.append(
                f"FAIL: HTML shows 0 {label} but source has {expected_count}"
            )
        elif html_count != expected_count:
            errors.append(
                f"WARNING: HTML shows {html_count} {label}, "
                f"source has {expected_count}"
            )
        else:
            print(f"  [PASS] {label}: {html_count} matches source")

    return errors


def main():
    parser = argparse.ArgumentParser(description='Validate generated HTML')
    parser.add_argument('html_file', help='Path to the HTML file to validate')
    parser.add_argument('--source-data', help='Path to source JSON for data integrity check')
    args = parser.parse_args()

    html_path = Path(args.html_file)
    if not html_path.exists():
        print(f"ERROR: {html_path} not found")
        sys.exit(1)

    html = html_path.read_text()
    all_errors = []

    print(f"Validating: {html_path}")
    print(f"  Size: {len(html):,} chars, {html.count(chr(10)):,} lines")
    print()

    print("Check 1: JavaScript syntax")
    all_errors.extend(check_js_syntax(html))

    print("\nCheck 2: Double-brace detection")
    all_errors.extend(check_double_braces(html))

    print("\nCheck 3: CSS brace balance")
    all_errors.extend(check_css_braces(html))

    if args.source_data:
        print("\nCheck 4: Data integrity")
        all_errors.extend(check_data_integrity(html, args.source_data))

    print("\n" + "=" * 50)
    failures = [e for e in all_errors if e.startswith("FAIL")]
    warnings = [e for e in all_errors if e.startswith("WARNING")]

    if failures:
        print(f"VALIDATION FAILED: {len(failures)} error(s), {len(warnings)} warning(s)")
        for e in failures + warnings:
            print(f"\n  {e}")
        sys.exit(1)
    elif warnings:
        print(f"PASSED with {len(warnings)} warning(s)")
        for w in warnings:
            print(f"\n  {w}")
    else:
        print("ALL CHECKS PASSED")


if __name__ == '__main__':
    main()
