#!/usr/bin/env python3
"""Download all papers listed in _manifest.json into this directory."""
import json, os, re, subprocess, sys, urllib.request, urllib.parse, urllib.error

DEST = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(DEST, "_manifest.json")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"


def follow_redirects(url, max_hops=8):
    """Follow HTTP redirects manually to capture final URL."""
    current = url
    for _ in range(max_hops):
        req = urllib.request.Request(current, method="HEAD", headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                final = resp.geturl()
                if final == current:
                    return final
                current = final
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308):
                current = e.headers.get("Location") or current
            else:
                # Try GET (some servers don't allow HEAD)
                try:
                    req2 = urllib.request.Request(current, headers={"User-Agent": UA})
                    with urllib.request.urlopen(req2, timeout=20) as r2:
                        return r2.geturl()
                except Exception:
                    return current
        except Exception:
            return current
    return current


def gdrive_file_id(url):
    m = re.search(r"/file/d/([A-Za-z0-9_-]+)", url)
    if m:
        return m.group(1)
    m = re.search(r"[?&]id=([A-Za-z0-9_-]+)", url)
    if m:
        return m.group(1)
    return None


def gdoc_id(url):
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", url)
    return m.group(1) if m else None


def download_gdrive_file(file_id, out_path):
    """Download public Drive file. Handles the virus-scan confirm page for big files."""
    base = "https://drive.google.com/uc?export=download&id=" + file_id
    cookies = "/tmp/.gdrive_cookie"
    # First request
    cmd = ["curl", "-sL", "-c", cookies, "-b", cookies, "-A", UA, "-o", out_path, base]
    r = subprocess.run(cmd, capture_output=True, timeout=120)
    # Check if HTML virus-scan page returned (small file)
    if os.path.getsize(out_path) < 200000:
        with open(out_path, "rb") as f:
            head = f.read(2048)
        if b"<html" in head.lower() and b"virus" in head.lower():
            # Need confirmation token
            with open(out_path, "rb") as f:
                content = f.read().decode("utf-8", "ignore")
            m = re.search(r'confirm=([0-9A-Za-z_-]+)', content)
            uuid = re.search(r'name="uuid"\s+value="([^"]+)"', content)
            if m or uuid:
                params = {"export": "download", "id": file_id}
                if m:
                    params["confirm"] = m.group(1)
                if uuid:
                    params["uuid"] = uuid.group(1)
                url = "https://drive.usercontent.google.com/download?" + urllib.parse.urlencode(params)
                cmd2 = ["curl", "-sL", "-c", cookies, "-b", cookies, "-A", UA, "-o", out_path, url]
                subprocess.run(cmd2, capture_output=True, timeout=120)
    return os.path.getsize(out_path)


def download_gdoc_pdf(doc_id, out_path):
    """Export a Google Doc as PDF (public docs only without auth)."""
    url = f"https://docs.google.com/document/d/{doc_id}/export?format=pdf"
    cookies = "/tmp/.gdoc_cookie"
    cmd = ["curl", "-sL", "-c", cookies, "-b", cookies, "-A", UA, "-o", out_path, url]
    subprocess.run(cmd, capture_output=True, timeout=120)
    return os.path.getsize(out_path)


def download_dochub_pdf(url, out_path):
    """Dochub URLs end in -pdf typically; we just fetch the page and look for direct PDF link.
    Many dochub.com pages serve the PDF directly via a 'download' button.
    """
    # Try the page URL first
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as resp:
            ctype = resp.headers.get("Content-Type", "")
            data = resp.read()
        if "pdf" in ctype.lower() or data[:5] == b"%PDF-":
            with open(out_path, "wb") as f:
                f.write(data)
            return os.path.getsize(out_path)
        # Else try the download endpoint
        m = re.search(r"https?://dochub\.com/[^/]+/([A-Za-z0-9_-]+)/", url)
        if m:
            dl_url = f"https://dochub.com/{m.group(0).split('/')[3]}/{m.group(1)}/download"
            # Save the HTML for debugging
            html_path = out_path + ".dochub.html"
            with open(html_path, "wb") as f:
                f.write(data)
            return -1
    except Exception as e:
        with open(out_path + ".err.txt", "w") as f:
            f.write(f"dochub error: {e}\n")
        return -1
    return -1


def download_url(url, out_path):
    """Generic fetch."""
    try:
        cookies = "/tmp/.generic_cookie"
        cmd = ["curl", "-sL", "-c", cookies, "-b", cookies, "-A", UA, "-o", out_path, url]
        r = subprocess.run(cmd, capture_output=True, timeout=120)
        return os.path.getsize(out_path) if os.path.exists(out_path) else 0
    except Exception:
        return 0


def main():
    with open(MANIFEST) as f:
        papers = json.load(f)
    results = []
    for p in papers:
        slug = p["slug"]
        url = p["url"]
        title = p["title"]
        print(f"\n--- #{p['n']} {title}")
        print(f"URL: {url}")
        # Step 1: resolve tinyurl shortcuts
        if "tinyurl.com" in url:
            final = follow_redirects(url)
            print(f"Resolved: {final}")
            url = final
        # Step 2: route by host
        out = None
        if "drive.google.com" in url:
            fid = gdrive_file_id(url)
            if fid:
                out = os.path.join(DEST, slug + ".pdf")
                size = download_gdrive_file(fid, out)
                print(f"Drive file {fid} -> {size} bytes")
        elif "docs.google.com/document" in url:
            did = gdoc_id(url)
            if did:
                out = os.path.join(DEST, slug + ".pdf")
                size = download_gdoc_pdf(did, out)
                print(f"GDoc {did} -> {size} bytes")
        elif "dochub.com" in url:
            out = os.path.join(DEST, slug + ".pdf")
            size = download_dochub_pdf(url, out)
            print(f"Dochub -> {size} bytes")
        else:
            out = os.path.join(DEST, slug + ".pdf")
            size = download_url(url, out)
            print(f"Generic -> {size} bytes")
        results.append({"slug": slug, "url": url, "file": out, "size": os.path.getsize(out) if out and os.path.exists(out) else 0})
    with open(os.path.join(DEST, "_download_log.json"), "w") as f:
        json.dump(results, f, indent=2)
    return results


if __name__ == "__main__":
    main()
