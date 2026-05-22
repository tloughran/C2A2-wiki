#!/usr/bin/env python3
"""Retry failed downloads using gdown + dochub-specific logic."""
import json, os, re, subprocess, sys, urllib.request, urllib.parse, time

DEST = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def is_pdf(path):
    if not os.path.exists(path):
        return False
    try:
        with open(path, "rb") as f:
            return f.read(5) == b"%PDF-"
    except Exception:
        return False


def gdown_file(file_id, out_path):
    """Use gdown library to download from Google Drive."""
    import gdown
    url = f"https://drive.google.com/uc?id={file_id}"
    try:
        gdown.download(url, out_path, quiet=True, fuzzy=True)
        return is_pdf(out_path)
    except Exception as e:
        print(f"gdown error: {e}")
        return False


def dochub_pdf(view_url, out_path):
    """Fetch dochub page and extract the actual PDF download URL.

    Pattern: dochub.com/{user}/{id}/{slug}
    Their PDF download URL pattern (best-effort): https://dochub.com/document/{id}.pdf or similar.
    Falls back to scraping the page's initial payload.
    """
    m = re.search(r"dochub\.com/[^/]+/([A-Za-z0-9_-]+)/", view_url + "/")
    if not m:
        print("Couldn't extract dochub ID")
        return False
    doc_id = m.group(1)
    # Strategy 1: direct PDF endpoint
    candidates = [
        f"https://dochub.com/document/{doc_id}.pdf",
        f"https://dochub.com/document/{doc_id}/preview-pdf",
        f"https://dochub.com/api/documents/{doc_id}.pdf",
    ]
    for c in candidates:
        try:
            req = urllib.request.Request(c, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            if data[:5] == b"%PDF-":
                with open(out_path, "wb") as f:
                    f.write(data)
                return True
        except Exception:
            pass
    # Strategy 2: fetch the view page, look for embed/PDF URL in HTML
    try:
        req = urllib.request.Request(view_url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", "ignore")
        # Look for the PDF URL in the JS payload — common keys: pdf_url, file_url, url
        patterns = [
            r'"pdf_url"\s*:\s*"([^"]+\.pdf[^"]*)"',
            r'"file_url"\s*:\s*"([^"]+\.pdf[^"]*)"',
            r'"original_pdf_url"\s*:\s*"([^"]+)"',
            r'"download_url"\s*:\s*"([^"]+)"',
            r'https://dochub\.com/[^"\\\s]+\.pdf',
        ]
        for pat in patterns:
            mm = re.search(pat, html)
            if mm:
                pdf_url = mm.group(1) if mm.lastindex else mm.group(0)
                pdf_url = pdf_url.replace("\\u0026", "&").replace("\\/", "/")
                print(f"   Found PDF URL: {pdf_url[:120]}")
                try:
                    req2 = urllib.request.Request(pdf_url, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req2, timeout=60) as r2:
                        d = r2.read()
                    if d[:5] == b"%PDF-":
                        with open(out_path, "wb") as f:
                            f.write(d)
                        return True
                except Exception as e:
                    print(f"   fetch failed: {e}")
    except Exception as e:
        print(f"   page fetch failed: {e}")
    return False


def gdoc_pdf(doc_id, out_path):
    """Re-try Google Doc export."""
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=pdf"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        if data[:5] == b"%PDF-":
            with open(out_path, "wb") as f:
                f.write(data)
            return True
        # If still HTML, try drive.usercontent fallback
    except Exception as e:
        print(f"gdoc export failed: {e}")
    return False


# Map of files that need fixing
fixups = [
    {"slug": "08_Resanctifying_Human_Life", "type": "drive", "id": "0B2dNYhaliRgQdWFPZHBoVEFaeU0"},
    {"slug": "09b_Self_Esteem_Part_I_II", "type": "drive", "id": "1Q7YsP8ot-_32K-G7D3A0fkk2VqRlHA3z"},
    {"slug": "10_Eulogy_Ann_Catherine_Duwan", "type": "drive", "id": "0B2dNYhaliRgQTS1KWlc1UkpxV2M"},
    {"slug": "17_Trinity_School_Faculty_Note", "type": "drive", "id": "0B2dNYhaliRgQMGQxNDJjMzEtNDliZi00Njc4LTgxN2UtNTVkOWY3MzI4ZDFk"},
    {"slug": "21_INTEGRITY_Proposal", "type": "drive", "id": "1VIH9VAnsV3V013z-l1C72HOxqmAY_fea"},
    {"slug": "22_Scholarly_Interest_Experience_Goals_2006", "type": "gdoc", "id": "1JGmnf4SOtRfnQe5wLmY5HNWxfIsBVgPMBbpJVE5z7L4"},
    {"slug": "14_Latifas_Story_BOSCO_Wikispaces", "type": "dochub", "url": "https://dochub.com/drthomasjloughrantom/0YkWQ4BwYWvE1eJKpl7A8q/bosco-latifah-wikispaces-blog-guest-post-pdf"},
    {"slug": "16_Education_Tradition_Core_Curriculum", "type": "dochub", "url": "https://dochub.com/drthomasjloughrantom/oGZeMNnwXYYLG0YRQvbrYd/education-tradition-core-curricula-pdf"},
    {"slug": "18_NDeRC_2011_1Page_Progress_Report", "type": "dochub", "url": "https://dochub.com/drthomasjloughrantom/gzdnE7NwJM7z6E1VQyW3BJ/nderc-1-page-report-end-2011-pdf"},
    {"slug": "20_STEM_Forum_2014_Press_Release", "type": "dochub", "url": "https://dochub.com/thomasjloughran/pqb0g5YRqyo95ODRJ2nx67/2014-forum-collaboration-forum-plants-seeds-for-stem-growth-news-college-of-scien"},
    {"slug": "23_ISTEM_Community_Precursor_Politics", "type": "dochub", "url": "https://dochub.com/thomasjloughran/275eAYrVoOJ5MXVzXnBNQL/istem-community-as-precursor-to-politics-craft-tradition-pdf"},
]


def main():
    for entry in fixups:
        out = os.path.join(DEST, entry["slug"] + ".pdf")
        # Skip if already valid
        if is_pdf(out):
            print(f"[OK already] {entry['slug']}")
            continue
        if os.path.exists(out):
            os.remove(out)
        print(f"[FIX] {entry['slug']}  type={entry['type']}")
        ok = False
        if entry["type"] == "drive":
            ok = gdown_file(entry["id"], out)
        elif entry["type"] == "gdoc":
            ok = gdoc_pdf(entry["id"], out)
        elif entry["type"] == "dochub":
            ok = dochub_pdf(entry["url"], out)
        print(f"    -> {'OK' if ok else 'FAIL'} {os.path.getsize(out) if os.path.exists(out) else 0} bytes")


if __name__ == "__main__":
    main()
