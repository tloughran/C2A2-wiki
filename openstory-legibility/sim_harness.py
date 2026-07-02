#!/usr/bin/env python3
"""
sim_harness.py - generate vault-grounded rival-tradition dialogues for the listening
study (see sim_preregistration.md). Two purpose-built interlocutors seeded ONLY from
the C2A2 vault, debating one fixed seam under three conditions.

    python3 sim_harness.py --condition listen  --seeds 0-4 [--backend anthropic|openai]
    python3 sim_harness.py --condition deaf    --seeds 0-4
    python3 sim_harness.py --condition bridge  --seeds 0-4    (retired; result preserved)
    python3 sim_harness.py --condition convene --seeds 0-4    (Amendment 1)

Writes sim/transcripts/<condition>/<seed>.json = {header, turns:[{role,text}]}.
Idempotent: skips a (condition,seed) whose file exists unless --force. Generation needs
ANTHROPIC_API_KEY / OPENAI_API_KEY (absent in the Cowork sandbox -> run on the Mac).

Conditions (sim_preregistration.md s.3):
  listen : C and H each read the full running transcript.
  deaf   : the deaf agent(s) (default H) get the seam + their OWN prior turns only,
           never the partner's turns. --deaf C,H makes it mutually deaf (the strongest
           null: two traditions talking past each other). Default H = the registered
           asymmetric control; mutual is offered as a stronger variant, recorded in the
           header either way.
  bridge : listen + a third whole-corpus interlocutor B translating after each exchange.
  convene: listen + a pass-through convener T (Amendment 1) that, after each C/H exchange,
           sustains a civil register and runs a checking protocol: the OTHER speaker restates
           one speaker's just-made point, and the ORIGINAL speaker certifies or corrects it.
           On a randomized 1/3 of events an UNFAITHFUL (strawman) restatement is injected as
           the anti-rubber-stamp control. Emits a structured cert_events[] array alongside the
           transcript (no text parsing downstream). See sim_preregistration.md Amendment 1.
"""
import json, sys, os, re, time, random, urllib.request, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_VAULT = os.path.expanduser(
    "~/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki")
SEAM = ("Is spacetime fundamental, and what follows for the status of conscious "
        "experience?")
N_EXCHANGES = 16          # ~32 utterances for C/H; bridge adds B per exchange
TEMP = 0.8                # >0 so seeds give independent samples
MAXTOK = 320

def read(p):
    try:
        return open(p, encoding="utf-8").read()
    except Exception:
        return ""

def seed_block(vault, key, cap=6000):
    """Compact tradition seed from the vault: core claim + active questions + triplets."""
    wiki = read(os.path.join(vault, "traditions", key, "wiki.md"))
    prs = read(os.path.join(vault, "traditions", key, "prs_triplets.md"))
    # keep the overview + questions from wiki, and the first chunk of triplets
    wiki = wiki.split("## Solved")[0]
    return (wiki[:cap] + "\n\n--- PRS triplets ---\n" + prs[:cap])[: 2 * cap]

def persona(name, thinker, stance, seed):
    return (
        f"You are {name}, arguing the position of {thinker} in a live philosophical "
        f"debate against a rival tradition. Hold your frame: {stance} Do NOT concede the "
        f"frame cheaply or drift into agreement for politeness — translation across "
        f"incommensurable traditions is hard work, not automatic (MacIntyre). Engage the "
        f"OTHER speaker's last point directly: name it, then press, steelman, concede a "
        f"specific sub-point, or counter. One substantive paragraph, ~120-160 words, no "
        f"lists. Stay grounded in your tradition's actual commitments below.\n\n"
        f"=== YOUR TRADITION (seed) ===\n{seed}")

# --- Convener (Amendment 1) --------------------------------------------------
STRAWMAN_FRACTION = 1.0 / 3.0   # A1.4: 1 in 3 events get an injected unfaithful restatement.

CONVENER_SYS = (
    "You are T, a convener. You do NOT take a side, add substantive content, or judge who is "
    "right. Your two jobs: (1) sustain a civil, mutually respectful register between C and H; "
    "(2) run a checking protocol so each can hear whether the other has grasped their point. In "
    "about 60-90 words, no lists: acknowledge the just-finished exchange in a warm, even-handed "
    "tone, then pose the check aloud - name whose point is now on the table and ask the other to "
    "restate it faithfully enough that its author would certify it. Model civility; introduce no "
    "new claims of your own.")

STRAWMAN_SYS = (
    "You produce a restatement of a philosophical point that sounds superficially plausible and "
    "stays polite in tone, but SUBTLY DISTORTS OR NEGATES its load-bearing claim - so its author "
    "should refuse to certify it. About 70-90 words. Output ONLY the distorted restatement: no "
    "preamble, and no signal that it is distorted.")

def restate_prompt(point):
    return ("A convener asks you to show you have understood your interlocutor. Restate the "
            "following point they made, in your own words and honestly on its own terms, so that "
            "THEY would certify it as what they meant. Do not rebut it and do not add your own "
            "view. About 70-90 words, no preamble.\n\nTheir point:\n" + point)

def certify_prompt(point, restatement):
    return ("A convener relays a restatement of YOUR point and asks you to certify it. Certify "
            "ONLY if it faithfully captures your load-bearing claim on its own terms; refuse if it "
            "distorts or misses it. Reply with EXACTLY the word CERTIFY if faithful, or "
            "'CORRECT: ' followed by one sentence if not.\n\nYour original point:\n" + point
            + "\n\nThe restatement to judge:\n" + restatement)

def parse_verdict(raw):
    """Robustly read CERTIFY/CORRECT from a persona reply that may wrap it in prose. Returns
    (verdict, correction). Unparseable -> conservative 'correct' (a non-certification)."""
    s = (raw or "").strip()
    up = s.upper()
    ic, ik = up.find("CERTIFY"), up.find("CORRECT")
    if ic == -1 and ik == -1:
        return "correct", s
    if ik == -1 or (ic != -1 and ic < ik):
        return "certify", ""
    tail = s[ik:]
    corr = tail.split(":", 1)[1].strip() if ":" in tail else tail[len("CORRECT"):].strip()
    return "correct", corr

def _envkey(name):
    k = os.environ.get(name, "").strip()
    if not k:
        sys.exit(f"{name} is not set in this shell. Export your REAL key first:\n"
                 f'  export {name}="sk-..."\n'
                 f"Verify with:  echo \"len=${{#{name}}} head=${{{name}:0:6}}\"")
    if "REPLACE" in k or k in ("sk-REPLACE",):
        sys.exit(f"{name} still holds the placeholder 'sk-REPLACE'. Export your real key.")
    return k

def _post(url, headers, payload, retries=6):
    body = json.dumps(payload).encode()
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, body, headers)
            return json.load(urllib.request.urlopen(req, timeout=120))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:600]
            transient = e.code in (429, 500, 502, 503, 529)
            if transient and attempt < retries - 1:
                wait = min(4 * (2 ** attempt), 60)        # 4,8,16,32,60,60s
                sys.stderr.write(f"  [{e.code} {e.reason}] retry {attempt+1}/{retries-1} "
                                 f"in {wait}s...\n"); sys.stderr.flush()
                time.sleep(wait); continue
            hint = ""
            if e.code == 401:
                hint = ("\n401 = the API rejected the key. Check it is your REAL key, not "
                        "expired, valid for THIS account.")
            elif e.code == 429:
                hint = ("\n429 = rate-limited / out of credits even after retries. Lower "
                        "load: run fewer --seeds, or wait and re-run (idempotent: finished "
                        "seeds are skipped).")
            sys.exit(f"\nAPI {e.code} {e.reason} from {url}\n{detail}{hint}")
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(5); continue
            sys.exit(f"network error to {url}: {e.reason}")

def _sanitize(history):
    """Make a message list API-valid for the DEAF speaker, whose own turns survive
    filtering with the partner's removed -> consecutive assistant turns ending on
    assistant (which Anthropic rejects: 'must end with a user message'). Merge adjacent
    assistant turns and append a user continuation if it ends on assistant. NO-OP for
    listen/bridge (their histories already alternate and end on the partner's user turn),
    so generation there is byte-identical and conditions stay comparable."""
    out = []
    for m in history:
        if out and out[-1]["role"] == "assistant" and m["role"] == "assistant":
            out[-1] = {"role": "assistant", "content": out[-1]["content"] + "\n\n" + m["content"]}
        else:
            out.append(dict(m))
    if out and out[-1]["role"] == "assistant":
        out.append({"role": "user",
                    "content": "Continue the debate with your next point, in your tradition's voice."})
    return out

def call(backend, system, history, nonce):
    """history: list of {role: 'assistant'|'user', content}. Returns text."""
    history = _sanitize(history)
    if backend == "anthropic":
        key = _envkey("ANTHROPIC_API_KEY")
        r = _post("https://api.anthropic.com/v1/messages",
            {"x-api-key": key, "anthropic-version": "2023-06-01",
             "content-type": "application/json"},
            {"model": "claude-sonnet-4-6", "max_tokens": MAXTOK, "temperature": TEMP,
             "system": system + f"\n\n[variant {nonce}]", "messages": history})
        return r["content"][0]["text"].strip()
    if backend == "openai":
        key = _envkey("OPENAI_API_KEY")
        msgs = [{"role": "system", "content": system + f"\n\n[variant {nonce}]"}] + [
            {"role": ("assistant" if m["role"] == "assistant" else "user"),
             "content": m["content"]} for m in history]
        r = _post("https://api.openai.com/v1/chat/completions",
            {"authorization": f"Bearer {key}", "content-type": "application/json"},
            {"model": "gpt-4o", "temperature": TEMP, "max_tokens": MAXTOK, "messages": msgs})
        return r["choices"][0]["message"]["content"].strip()
    sys.exit(f"unknown backend {backend}")

def visible(turns, speaker, condition, deaf):
    """Build the message history one speaker sees, per condition. Their own turns are
    'assistant'; everyone else's visible turns are 'user' (prefixed with the speaker)."""
    hist = [{"role": "user", "content": f"SEAM: {SEAM}\n\nOpen the debate."}]
    for t in turns:
        if t["role"] == speaker:
            hist.append({"role": "assistant", "content": t["text"]})
        else:
            if condition == "deaf" and speaker in deaf and t["role"] != speaker:
                continue   # deaf speaker never sees the partner
            hist.append({"role": "user", "content": f"[{t['role']}] {t['text']}"})
    return hist

def generate(vault, condition, seed, backend, deaf):
    seedC = seed_block(vault, "carroll"); seedH = seed_block(vault, "hoffman")
    sysC = persona("C", "Sean Carroll (poetic naturalism, Core-Theory completeness, "
                   "Many-Worlds)", "physics is causally complete at the Core Theory; "
                   "consciousness is emergent, not fundamental; spacetime is real.", seedC)
    sysH = persona("H", "Donald Hoffman (interface theory, conscious agents, "
                   "fitness-beats-truth)", "perception is a species-specific interface, "
                   "not truth; spacetime is doomed; consciousness is fundamental.", seedH)
    order = ["C", "H"]
    sysmap = {"C": sysC, "H": sysH}
    if condition == "bridge":
        seedB = seed_block(vault, "carroll")[:1500] + seed_block(vault, "hoffman")[:1500]
        sysmap["B"] = ("You are B, a second-first-language speaker fluent in BOTH "
                       "traditions. After C and H each speak, render each one's last point "
                       "in the OTHER's terms and name the precise locus of disagreement or "
                       "a possible bridge. ~110 words, no lists.\n\n" + seedB)
    if condition == "convene":
        sysmap["T"] = CONVENER_SYS
    rng_sm = random.Random(20260630 + seed)      # reproducible strawman draws, per seed
    cert_events = []
    turns = []
    for ex in range(N_EXCHANGES):
        ex_txt = {}
        for spk in order:
            txt = call(backend, sysmap[spk], visible(turns, spk, condition, deaf), f"{seed}.{ex}")
            turns.append({"role": spk, "text": txt})
            ex_txt[spk] = txt
        if condition == "bridge":
            txt = call(backend, sysmap["B"], visible(turns, "B", "listen", deaf), f"{seed}.{ex}")
            turns.append({"role": "B", "text": txt})
        if condition == "convene":
            # (1) T sustains the civil register and poses the check, visible to C and H.
            t_txt = call(backend, sysmap["T"], visible(turns, "T", "listen", deaf), f"{seed}.{ex}.t")
            turns.append({"role": "T", "text": t_txt})
            # (2) alternate whose point is on the table: even ex -> C's point restated by H
            #     and certified by C; odd ex -> H's point restated by C and certified by H.
            target, restater = ("C", "H") if ex % 2 == 0 else ("H", "C")
            point = ex_txt[target]
            is_straw = rng_sm.random() < STRAWMAN_FRACTION
            if is_straw:
                R = call(backend, STRAWMAN_SYS,
                         [{"role": "user", "content": "Point to distort:\n" + point}],
                         f"{seed}.{ex}.sm")
            else:
                R = call(backend, sysmap[restater],
                         [{"role": "user", "content": restate_prompt(point)}], f"{seed}.{ex}.r")
            # (3) certification is ALWAYS by the original speaker; the convener never certifies.
            vraw = call(backend, sysmap[target],
                        [{"role": "user", "content": certify_prompt(point, R)}], f"{seed}.{ex}.v")
            verdict, correction = parse_verdict(vraw)
            cert_events.append({"exchange": ex, "target": target, "restater": restater,
                                "target_point": point, "restatement": R,
                                "is_strawman": is_straw, "verdict": verdict,
                                "correction": correction})
    rec = {"header": {"condition": condition, "seed": seed, "seam": SEAM,
                      "backend": backend, "deaf": sorted(deaf) if condition == "deaf" else [],
                      "n_exchanges": N_EXCHANGES, "temp": TEMP,
                      "generated": str(datetime.datetime.now())}, "turns": turns}
    if condition == "convene":
        rec["header"]["strawman_fraction"] = STRAWMAN_FRACTION
        rec["cert_events"] = cert_events
    return rec

def parse_seeds(s):
    if "-" in s:
        a, b = s.split("-"); return list(range(int(a), int(b) + 1))
    return [int(x) for x in s.split(",")]

def main():
    a = sys.argv
    g = lambda k, d=None: a[a.index(k) + 1] if k in a else d
    condition = g("--condition", "listen")
    seeds = parse_seeds(g("--seeds", "0-4"))
    backend = g("--backend", "anthropic")
    vault = g("--vault", DEFAULT_VAULT)
    deaf = set((g("--deaf", "H")).split(",")) if condition == "deaf" else set()
    force = "--force" in a
    if "--preflight" in a:
        txt = call(backend, "Reply with the single word: ok.",
                   [{"role": "user", "content": "ping"}], "pf")
        print(f"preflight OK via {backend}: {txt[:40]!r}"); return
    outdir = os.path.join(HERE, "sim", "transcripts", condition)
    os.makedirs(outdir, exist_ok=True)
    for sd in seeds:
        path = os.path.join(outdir, f"{sd}.json")
        if os.path.exists(path) and not force:
            print(f"skip (exists): {path}"); continue
        rec = generate(vault, condition, sd, backend, deaf)
        json.dump(rec, open(path, "w"), indent=1)
        print(f"wrote {path}  ({len(rec['turns'])} turns)")

if __name__ == "__main__":
    main()
