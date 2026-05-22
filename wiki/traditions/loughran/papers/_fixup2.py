#!/usr/bin/env python3
"""Round 2: fix remaining failures using gdown properly + alternate gdoc strategies."""
import os, re, urllib.request, subprocess

DEST = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def is_pdf(path):
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-"
    except Exception:
        return False


def gdown_file(file_id, out_path):
    """Use gdown CLI which handles confirmation tokens automatically."""
    if os.path.exists(out_path):
        os.remove(out_path)
    # gdown CLI:  gdown <url> -O <out>
    url = f"https://drive.google.com/uc?id={file_id}"
    r = subprocess.run(["gdown", url, "-O", out_path], capture_output=True, text=True, timeout=120)
    if not is_pdf(out_path):
        # Also try with the file ID form (-> drive.usercontent.google.com)
        r = subprocess.run(["gdown", "--id", file_id, "-O", out_path], capture_output=True, text=True, timeout=120)
    return is_pdf(out_path), r.stderr[-500:] if r.stderr else ""


def export_gdoc_pdf(doc_id, out_path):
    """Fetch the GDoc PDF export. If 401, the doc may require authentication."""
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=pdf"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        if data[:5] == b"%PDF-":
            with open(out_path, "wb") as f:
                f.write(data)
            return True, None
        return False, f"got HTML (size {len(data)})"
    except Exception as e:
        return False, str(e)


def dochub_pdf_v2(view_url, out_path):
    """Retry dochub with broader patterns / curl with referer."""
    # Try alternate viewport URL
    m = re.search(r"dochub\.com/[^/]+/([A-Za-z0-9_-]+)/", view_url + "/")
    if not m:
        return False, "no ID"
    doc_id = m.group(1)
    candidates = [
        f"https://dochub.com/document/{doc_id}.pdf",
        f"https://dochub.com/document/{doc_id}/preview-pdf",
    ]
    for c in candidates:
        try:
            r = subprocess.run(
                ["curl", "-sL", "-A", UA, "-e", view_url, "-o", out_path, c],
                capture_output=True, timeout=60
            )
            if is_pdf(out_path):
                return True, c
        except Exception:
            pass
    # Try fetching page with referer set
    try:
        r = subprocess.run(
            ["curl", "-sL", "-A", UA, "-e", "https://dochub.com", view_url],
            capture_output=True, timeout=60
        )
        html = r.stdout.decode("utf-8", "ignore")
        for pat in [r'"pdf_url"\s*:\s*"([^"]+)"', r'"file_url"\s*:\s*"([^"]+)"', r'"download_url"\s*:\s*"([^"]+)"', r'"original_pdf_url"\s*:\s*"([^"]+)"']:
            mm = re.search(pat, html)
            if mm:
                pdf_url = mm.group(1).replace("\\u0026", "&").replace("\\/", "/")
                r2 = subprocess.run(
                    ["curl", "-sL", "-A", UA, "-e", view_url, "-o", out_path, pdf_url],
                    capture_output=True, timeout=120
                )
                if is_pdf(out_path):
                    return True, pdf_url
    except Exception as e:
        return False, str(e)
    return False, "no patterns matched"


fixups = [
    {"slug": "08_Resanctifying_Human_Life", "type": "drive", "id": "0B2dNYhaliRgQdWFPZHBoVEFaeU0"},
    {"slug": "09b_Self_Esteem_Part_I_II", "type": "drive", "id": "1Q7YsP8ot-_32K-G7D3A0fkk2VqRlHA3z"},
    {"slug": "10_Eulogy_Ann_Catherine_Duwan", "type": "drive", "id": "0B2dNYhaliRgQTS1KWlc1UkpxV2M"},
    {"slug": "17_Trinity_School_Faculty_Note", "type": "drive", "id": "0B2dNYhaliRgQMGQxNDJjMzEtNDliZi00Njc4LTgxN2UtNTVkOWY3MzI4ZDFk"},
    {"slug": "21_INTEGRITY_Proposal", "type": "drive", "id": "1VIH9VAnsV3V013z-l1C72HOxqmAY_fea"},
    {"slug": "22_Scholarly_Interest_Experience_Goals_2006", "type": "gdoc", "id": "1JGmnf4SOtRfnQe5wLmY5HNWxfIsBVgPMBbpJVE5z7L4"},
    {"slug": "23_ISTEM_Community_Precursor_Politics", "type": "dochub", "url": "https://dochub.com/thomasjloughran/275eAYrVoOJ5MXVzXnBNQL/istem-community-as-precursor-to-politics-craft-tradition-pdf"},
]


def main():
    for e in fixups:
        out = os.path.join(DEST, e["slug"] + ".pdf")
        if is_pdf(out):
            print(f"[SKIP] {e['slug']} already PDF")
            continue
        if os.path.exists(out):
            os.remove(out)
        print(f"[FIX] {e['slug']} ({e['type']})")
        ok, info = False, ""
        if e["type"] == "drive":
            ok, info = gdown_file(e["id"], out)
        elif e["type"] == "gdoc":
            ok, info = export_gdoc_pdf(e["id"], out)
        elif e["type"] == "dochub":
            ok, info = dochub_pdf_v2(e["url"], out)
        sz = os.path.getsize(out) if os.path.exists(out) else 0
        print(f"   -> {'OK' if ok else 'FAIL'} {sz} bytes  info: {info[:120] if info else ''}")


if __name__ == "__main__":
    main()
