#!/usr/bin/env python3
"""PRS created-vs-delivered histogram (WS2 view layer).

Two clocks for the same population of present PRS triplets:
  - Created   = the "Date Added" stamped in traditions/*/prs_triplets.md
                (when the work was done, per the author).
  - Delivered = the git first-seen date from prs_yield_detail.csv
                (when it entered version control / was committed).

Emits a self-contained dark-theme HTML grouped 2-colour histogram with a key.
Pre-2026 "Date Added" values (source-publication dates) are summarised off-scale
rather than stretching the time axis. Read-only; writes one HTML file.
"""
import argparse, csv, glob, json, os, re, sys
from collections import Counter

PRS = re.compile(r"^PRS-(\d+):\s*$")
DA = re.compile(r"^\s*Date Added:\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", re.I)
AXIS_MIN = "2026-03-25"   # main time window; earlier Date-Added values shown off-scale


def date_added_map(wiki):
    out = {}
    for f in glob.glob(os.path.join(wiki, "traditions/*/prs_triplets.md")):
        trad = os.path.basename(os.path.dirname(f))
        cur = None
        for ln in open(f, encoding="utf-8"):
            m = PRS.match(ln)
            if m:
                cur = (trad, int(m.group(1)))
                continue
            if cur:
                d = DA.match(ln)
                if d and cur not in out:
                    out[cur] = d.group(1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--out", default="prs_created_vs_delivered.html")
    args = ap.parse_args()

    wiki = os.path.join(args.repo, "wiki")
    detail = os.path.join(wiki, "architecture/metrics/prs_yield_detail.csv")
    if not os.path.isfile(detail):
        sys.exit("FAIL: %s missing (run prs_yield.py first)" % detail)

    delivered = {}
    for r in csv.DictReader(open(detail, encoding="utf-8")):
        if r.get("present") == "1":
            delivered[(r["tradition"], int(r["prs_id"].replace("PRS-", "")))] = r["first_seen_date"]
    created = date_added_map(wiki)

    # same population: present triplets that have both dates
    keys = [k for k in delivered if k in created]
    both = len(keys)
    no_da = [k for k in delivered if k not in created]

    cre = Counter(created[k] for k in keys)
    dlv = Counter(delivered[k] for k in keys)
    offscale = sum(v for d, v in cre.items() if d < AXIS_MIN)
    cre_in = {d: v for d, v in cre.items() if d >= AXIS_MIN}

    series = {
        "created": sorted([{"date": d, "n": v} for d, v in cre_in.items()], key=lambda x: x["date"]),
        "delivered": sorted([{"date": d, "n": v} for d, v in dlv.items()], key=lambda x: x["date"]),
        "axis_min": AXIS_MIN,
        "n_both": both,
        "offscale_created": offscale,
        "retired_no_da": len(no_da),
        "total_created_days": len(cre),
        "total_delivered_days": len(dlv),
    }

    html = HTML.replace("/*__DATA__*/", json.dumps(series))
    out_path = args.out if os.path.isabs(args.out) else os.path.join(os.getcwd(), args.out)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(html)

    print("present triplets charted (both clocks): %d" % both)
    print("created days: %d (%d off-scale pre-%s)" % (len(cre), offscale, AXIS_MIN[:4]))
    print("delivered days: %d" % len(dlv))
    print("retired (no Date Added, excluded): %d" % len(no_da))
    print("wrote %s" % out_path)


HTML = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>PRS Triplets — Created vs Delivered</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<style>
  body{background:#0a0a0f;color:#d8d8e0;font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;margin:0;padding:24px}
  h1{font-size:18px;margin:0 0 2px} .sub{color:#8a8a98;font-size:12px;margin:0 0 16px;max-width:760px}
  #key{margin:10px 0 4px;font-size:12px}
  .swatch{display:inline-block;width:12px;height:12px;border-radius:2px;vertical-align:-1px;margin-right:5px}
  .axis path,.axis line{stroke:#2a2a3a} .axis text{fill:#9a9aa8;font-size:11px}
  .note{color:#8a8a98;font-size:11px;margin-top:10px}
  .bar-created{fill:#B87D3E} .bar-delivered{fill:#5A8EAF}
  .tip{position:fixed;background:#16161f;border:1px solid #2a2a3a;padding:6px 9px;border-radius:5px;
       font-size:12px;pointer-events:none;opacity:0;transition:opacity .1s}
</style></head><body>
<h1>PRS triplets — when work was done vs when it was delivered</h1>
<p class="sub">Same population of present triplets, two clocks.
<b style="color:#B87D3E">Created</b> = the "Date Added" stamped in the source triplet file (when the work was done).
<b style="color:#5A8EAF">Delivered</b> = the git first-seen date (when it was committed). The lag between the two is the point.</p>
<div id="key">
  <span class="swatch" style="background:#B87D3E"></span>Created (Date Added)&nbsp;&nbsp;
  <span class="swatch" style="background:#5A8EAF"></span>Delivered (git commit)
</div>
<svg id="chart"></svg>
<div class="note" id="note"></div>
<div class="tip" id="tip"></div>
<script>
const DATA = /*__DATA__*/;
const tip = document.getElementById("tip");
function show(html,x,y){tip.innerHTML=html;tip.style.left=(x+12)+"px";tip.style.top=(y+12)+"px";tip.style.opacity=1;}
function hide(){tip.style.opacity=0;}

const M={top:16,right:24,bottom:40,left:44}, W=920, H=380, iW=W-M.left-M.right, iH=H-M.top-M.bottom;
const svg=d3.select("#chart").attr("width",W).attr("height",H);
const g=svg.append("g").attr("transform",`translate(${M.left},${M.top})`);

const parse=d3.timeParse("%Y-%m-%d");
const all=[...DATA.created,...DATA.delivered].map(d=>parse(d.date));
const x=d3.scaleTime().domain([parse(DATA.axis_min), d3.timeDay.offset(d3.max(all),3)]).range([0,iW]);
const yMax=d3.max([...DATA.created,...DATA.delivered],d=>d.n)||1;
const y=d3.scaleLinear().domain([0,yMax]).nice().range([iH,0]);

const bw=7;  // half-width per grouped bar
function draw(arr,cls,off,label){
  g.selectAll("."+cls).data(arr).join("rect").attr("class",cls)
    .attr("x",d=>x(parse(d.date))+off).attr("width",bw)
    .attr("y",d=>y(d.n)).attr("height",d=>iH-y(d.n))
    .on("mousemove",(e,d)=>show(`<b>${d.date}</b><br>${label}: ${d.n}`,e.clientX,e.clientY))
    .on("mouseleave",hide);
}
draw(DATA.created,"bar-created",-bw-0.5,"created");
draw(DATA.delivered,"bar-delivered",0.5,"delivered");

g.append("g").attr("class","axis").attr("transform",`translate(0,${iH})`)
  .call(d3.axisBottom(x).ticks(d3.timeWeek.every(1)).tickFormat(d3.timeFormat("%b %d")));
g.append("g").attr("class","axis").call(d3.axisLeft(y).ticks(6));
g.append("text").attr("transform","rotate(-90)").attr("x",-iH/2).attr("y",-32)
  .attr("text-anchor","middle").attr("fill","#9a9aa8").style("font-size","11px").text("triplets / day");

document.getElementById("note").innerHTML =
  `${DATA.n_both} present triplets charted. `
  + (DATA.offscale_created? `${DATA.offscale_created} created off-scale (Date Added before ${DATA.axis_min}, likely source-publication dates) — not drawn. ` : "")
  + (DATA.retired_no_da? `${DATA.retired_no_da} retired triplet(s) excluded (no current Date Added). ` : "")
  + `Created spans ${DATA.total_created_days} distinct days; delivered batches into ${DATA.total_delivered_days} commit-days — the gap is the create→deliver lag.`;
</script></body></html>
"""

if __name__ == "__main__":
    main()
