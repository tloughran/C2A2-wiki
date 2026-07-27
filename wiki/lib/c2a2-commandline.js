'use strict';

// c2a2-commandline.js
// The CCL (C2A2 Command Line) engine. v1 increment 1 ships the PARSER only:
// a pure function that turns one terse command string into a canonical op
// {dim, op, args, ...} against the grammar in wiki/voice_guide/verbs.json.
// Resolver (fuzzy names -> group keys / node ids), journal (absolute-vector
// undo/redo/restore), and per-tab dispatcher land in later increments; their
// sections are intentionally NOT stubbed here (Rule 2: no speculative code).
//
// Design: wiki/architecture/voice_guide_redesign.md (sections 3, 4, 5, 9).
//
// The grammar is passed IN, never fetched here, so parse/compileGrammar stay
// pure and node/jsdom-testable (redesign section 9). In the browser the shell
// fetches verbs.json once, calls compileGrammar, and holds the result; in node
// the test loads verbs.json from disk and does the same. One source of truth.
//
// API (attached to window.CommandLine in a browser; module.exports in node):
//   - VERSION                       "1"
//   - compileGrammar(verbsJson)     -> grammar {byVerb, dimensions, verbs}
//                                      throws on a malformed grammar
//   - parse(text, grammar)          -> op | error   (see shapes below)
//
// Success op:
//   { ok:true, verb, dim, op, args:[...], kind,
//     mode?, knob?, const?, spend?:bool, gated?:bool, echo }
// Error:
//   { ok:false, error:<code>, echo, ... }   codes:
//     'empty' | 'unknown_verb' | 'missing_arg' | 'too_many_args' |
//     'bad_enum' | 'focus_needs_two'

(function (root, factory) {
  const api = factory();
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; }
  if (typeof window !== 'undefined') { window.CommandLine = api; }
})(this, function () {

  const VERSION = '1';

  // ---- grammar compilation -------------------------------------------------

  function compileGrammar(verbsJson) {
    if (!verbsJson || !Array.isArray(verbsJson.verbs) || !verbsJson.dimensions) {
      throw new Error('CCL grammar malformed: need {dimensions, verbs[]}');
    }
    const byVerb = Object.create(null);
    for (const spec of verbsJson.verbs) {
      if (!spec.verb) { throw new Error('CCL grammar: verb spec missing "verb"'); }
      if (byVerb[spec.verb]) { throw new Error('CCL grammar: duplicate verb "' + spec.verb + '"'); }
      byVerb[spec.verb] = spec;
    }
    const filler = Array.isArray(verbsJson.filler) ? verbsJson.filler : [];
    const aliases = Array.isArray(verbsJson.aliases) ? verbsJson.aliases : [];

    // Two invariants, enforced HERE so a bad declaration dies at load with a
    // named reason rather than quietly changing what a command means.
    for (const w of filler) {
      // A filler word that is also an enum value would delete the argument it
      // is part of: put "out" in the list and `zoom out` becomes missing_arg.
      for (const spec of verbsJson.verbs) {
        if (spec.enum && spec.enum.indexOf(w) !== -1) {
          throw new Error('CCL grammar: filler "' + w + '" is also a value of ' + spec.verb + ' -- it would eat the argument');
        }
      }
    }
    for (const a of aliases) {
      if (!a || !a.say || !a.means) { throw new Error('CCL grammar: alias needs {say, means}'); }
      if (!byVerb[a.means]) { throw new Error('CCL grammar: alias "' + a.say + '" points at unknown verb "' + a.means + '"'); }
      // An alias that shadows a real verb silently redefines it. Allowed ONLY
      // when argument shape tells the two apart (`open first` vs `open levin`).
      if (byVerb[a.say] && !Array.isArray(a.when_arg_in)) {
        throw new Error('CCL grammar: alias "' + a.say + '" shadows the verb of the same name; give it when_arg_in or drop it');
      }
      if (Array.isArray(a.when_arg_in) && !a.when_arg_in.length) {
        throw new Error('CCL grammar: alias "' + a.say + '" has an empty when_arg_in, so it can never fire');
      }
    }
    return {
      byVerb: byVerb, dimensions: verbsJson.dimensions, verbs: verbsJson.verbs,
      filler: filler, aliases: aliases
    };
  }

  // ---- helpers -------------------------------------------------------------

  // Collapse internal runs of whitespace to single spaces and trim the ends.
  function normalize(text) {
    return String(text == null ? '' : text).replace(/\s+/g, ' ').trim();
  }

  function ok(spec, args, echo, extra) {
    const out = {
      ok: true,
      verb: spec.verb,
      dim: spec.dim,
      op: spec.op,
      args: args,
      kind: spec.kind,
      echo: echo,
    };
    if (spec.mode) { out.mode = spec.mode; }
    if (Object.prototype.hasOwnProperty.call(spec, 'const')) { out.const = spec['const']; }
    if (spec.spend) { out.spend = true; }
    if (spec.gated) { out.gated = true; }
    if (extra) { for (const k in extra) { out[k] = extra[k]; } }
    return out;
  }

  // VOICE TOLERANCE, applied only where a parse has ALREADY failed on arity.
  //
  // People put the noun back in ("pick first section", "pick first card") and
  // use a copula ("what is this"). Each of those returned too_many_args --
  // rejected one redundant word away from a command that works, which is what
  // made Start Here's sections feel unreachable while a bare `pick first` had
  // been working all along. The redundant noun carries NO information the
  // grammar lacks, so this is normalization, not a guess: it is silent, and
  // nothing is narrated back. (Contrast the resolver's "taking X as Y", which
  // narrates because it really did choose between live candidates.)
  //
  // Narrow by construction: the caller only reaches this on the arity-error
  // branch of `none` / `opt` / `one`. `text` and `many` verbs never call it, so
  // a search string, a tab name, or a group list cannot be silently eaten.
  function stripFiller(rest, grammar) {
    const filler = grammar && grammar.filler;
    if (!filler || !filler.length || !rest) { return rest; }
    return rest.split(' ').filter(function (w) { return filler.indexOf(w) === -1; }).join(' ').trim();
  }

  // Pick / select / choose / open are one intent in ordinary speech, and a
  // guide that accepts only the blessed word is not conversational -- it is a
  // command line with a microphone. The mapping is DATA (verbs.json aliases)
  // and deterministic, so the common phrasings cannot fail on a model's bad
  // day; the model's own latitude handles what is genuinely novel, on top of
  // this rather than instead of it.
  //
  // `strippedRest` is the argument AFTER filler removal, because shape is what
  // separates the two senses of a shadowing alias: `open first` is a cursor
  // move, `open levin` opens that node's article. Anything not listed in
  // when_arg_in keeps the original verb untouched.
  function resolveAlias(verb, strippedRest, grammar) {
    const aliases = grammar && grammar.aliases;
    if (!aliases || !aliases.length) { return verb; }
    for (const a of aliases) {
      if (a.say !== verb) { continue; }
      if (Array.isArray(a.when_arg_in) && a.when_arg_in.indexOf(strippedRest) === -1) { continue; }
      return a.means;
    }
    return verb;
  }

  function err(code, echo, extra) {
    const out = { ok: false, error: code, echo: echo };
    if (extra) { for (const k in extra) { out[k] = extra[k]; } }
    return out;
  }

  // ---- the parser ----------------------------------------------------------

  // parse("only levin friston", grammar)
  //   -> {ok:true, verb:'only', dim:'filters', op:'set', args:['levin','friston'], ...}
  // One command per call (redesign section 4). Names/values are NOT resolved
  // here -- fuzzy resolution against the live roster / node index is the
  // resolver's job at execution time.
  function parse(text, grammar) {
    const echo = normalize(text);
    if (!echo) { return err('empty', echo); }

    const sp = echo.indexOf(' ');
    const verb = (sp === -1 ? echo : echo.slice(0, sp)).toLowerCase();
    const rest = sp === -1 ? '' : echo.slice(sp + 1).trim();

    // Synonyms resolve before anything else, so every check below sees the one
    // canonical verb. A shadowing alias (`open`) fires only when the argument
    // shape says so, which is why the stripped form is computed first.
    const stripped = stripFiller(rest, grammar);
    const spec = grammar.byVerb[resolveAlias(verb, stripped, grammar)];
    if (!spec) { return err('unknown_verb', echo, { verb: verb }); }

    // Free-text and list verbs keep every word the user said: a search string,
    // a tab name and a group list must never have a token quietly removed.
    const bare = (spec.args === 'text' || spec.args === 'many') ? rest : stripped;

    switch (spec.args) {

      case 'none': {
        if (rest && bare) { return err('too_many_args', echo, { verb: verb }); }
        // const-valued verbs (fit/read/stop) carry their fixed value as the arg
        const args = Object.prototype.hasOwnProperty.call(spec, 'const') ? [spec['const']] : [];
        return ok(spec, args, echo);
      }

      // 0 or 1 token: `all` means every group, `all tags` every member of that
      // family. One verb, two scopes, no new vocabulary to learn.
      case 'opt': {
        if (!bare) {
          var dflt = Object.prototype.hasOwnProperty.call(spec, 'const') ? [spec['const']] : [];
          return ok(spec, dflt, echo);
        }
        if (bare.indexOf(' ') !== -1) { return err('too_many_args', echo, { verb: verb }); }
        return ok(spec, [bare], echo);
      }

      case 'one': {
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        if (!bare) { return err('missing_arg', echo, { verb: verb }); }
        if (bare.indexOf(' ') !== -1) { return err('too_many_args', echo, { verb: verb }); }
        if (spec.enum && spec.enum.indexOf(bare) === -1) {
          return err('bad_enum', echo, { verb: verb, allowed: spec.enum });
        }
        return ok(spec, [bare], echo);
      }

      case 'text': {
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        return ok(spec, [rest], echo);  // whole remainder = one free-text arg
      }

      // Free text that MAY be omitted. `open` earns this: on a tab that walks a
      // roster, "pick first ... open" is the ordinary shape -- you go to a thing
      // and then open the thing you are on -- and requiring the name back would
      // make the user say what the guide just said to them. Whether a bare
      // `open` is meaningful is not the parser's call, so it passes an empty
      // arg list along and plan() decides: a tab whose items declare how they
      // open reads it as "the one under the cursor", and the graph still
      // answers missing_arg exactly as before.
      case 'text-opt': {
        return ok(spec, rest ? [rest] : [], echo);
      }

      case 'many': {
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        return ok(spec, rest.split(' '), echo);
      }

      case 'nary': {
        // focus a ~ b [~ c ...]  -- n-ary via '~' (redesign section 4)
        const terms = rest.split('~').map(function (t) { return t.trim(); }).filter(Boolean);
        if (terms.length < 2) { return err('focus_needs_two', echo, { verb: verb }); }
        return ok(spec, terms, echo);
      }

      case 'knob-value': {
        // set <knob> <value...>
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        const kSp = rest.indexOf(' ');
        if (kSp === -1) { return err('missing_arg', echo, { verb: verb, need: 'value' }); }
        const knob = rest.slice(0, kSp);
        const value = rest.slice(kSp + 1).trim();
        if (!value) { return err('missing_arg', echo, { verb: verb, need: 'value' }); }
        return ok(spec, [value], echo, { knob: knob });
      }

      default:
        return err('unknown_verb', echo, { verb: verb, note: 'unhandled args kind ' + spec.args });
    }
  }

  // ---- the resolver --------------------------------------------------------
  //
  // Fuzzy term -> concrete target, run at execution time against LIVE sources:
  //   - resolveGroups: filter group keys. Roster is read live from the iframe
  //     checkbox DOM (the salvaged filterRoster trick) -- nothing to keep in
  //     sync. Keys look like 'traditions/levin' or a bare structure name
  //     ('architecture'). Tests inject a static roster; the shell injects the
  //     live one.
  //   - resolveTab / resolveNode: match the generated destinations index
  //     (wiki/voice_guide/destinations.json). NODES is a top-level const in the
  //     regen artifact, not a window property, so it cannot be read live -- the
  //     index MUST be generated (redesign section 4, F12).
  //
  // Every resolver returns one of:
  //   { ok:true,  ... }                         exactly one target
  //   { ok:false, error:'ambiguous', term, candidates:[...] }
  //   { ok:false, error:'unresolved', term }
  // Ambiguity candidates ride in the result so disambiguation needs no model
  // memory (redesign section 5).

  const CAND_CAP = 8;

  // Guess, act, and SAY it was a guess -- rather than handing the question back.
  //
  // Returning `ambiguous` for every multi-match turned the guide into a machine
  // for answering questions with questions, which is intolerable in a voice-only
  // tool: the user cannot see the candidate list you are asking them about. So
  // when the matches rank cleanly (one is a closer match than the rest), take
  // the winner, mark it low-confidence, and carry the alternatives so the shell
  // can say "taking X to mean Y". Only a genuine TIE is worth a question.
  //
  // The safety of this rests on two things that already hold: every command
  // reports what actually happened (a wrong guess is visible, not hidden), and
  // `undo` is one word away. Hedge the INTERPRETATION, never the outcome.
  function rankOrAsk(candidates, term) {
    const scored = candidates.slice().sort(function (a, b) {
      const la = leaf(a).length, lb = leaf(b).length;
      if (la !== lb) { return la - lb; }          // closer match = less left over
      return low(a) < low(b) ? -1 : 1;            // deterministic tie-break
    });
    const tied = leaf(scored[0]).length === leaf(scored[1]).length;
    if (tied) { return { ok: false, error: 'ambiguous', term: term, candidates: scored.slice(0, CAND_CAP) }; }
    return {
      ok: true, keys: [scored[0]], term: term,
      confidence: 'low', alternatives: scored.slice(1, CAND_CAP)
    };
  }

  function low(s) { return String(s == null ? '' : s).toLowerCase().trim(); }
  function leaf(key) { const i = key.lastIndexOf('/'); return i === -1 ? key : key.slice(i + 1); }

  // term -> group key(s). A term naming a whole SECTION (e.g. 'traditions')
  // expands to every key under it, so "hide traditions" is one symmetric op.
  function resolveGroups(term, roster) {
    const t = low(term);
    if (!t) { return { ok: false, error: 'unresolved', term: term }; }
    roster = roster || [];

    const section = roster.filter(function (k) { return low(k).indexOf(t + '/') === 0; });
    const exact = roster.filter(function (k) { return low(k) === t || low(leaf(k)) === t; });

    // A key can be BOTH a group and a section parent: 'architecture' holds the
    // architecture files AND owns 'architecture/changelog'. Returning only the
    // children silently dropped the parent, so "show architecture" turned on
    // the changelog, reported a groups-on count that sounded like success, and
    // rendered zero architecture nodes. A term naming both means both.
    if (section.length) {
      const keys = exact.concat(section.filter(function (k) { return exact.indexOf(k) === -1; }));
      return { ok: true, keys: keys, section: true, term: term };
    }
    if (exact.length) { return { ok: true, keys: exact, term: term }; }

    const prefix = roster.filter(function (k) { return low(leaf(k)).indexOf(t) === 0; });
    if (prefix.length === 1) { return { ok: true, keys: prefix, term: term }; }
    if (prefix.length > 1) { return rankOrAsk(prefix, term); }

    const sub = roster.filter(function (k) { return low(leaf(k)).indexOf(t) !== -1; });
    if (sub.length === 1) { return { ok: true, keys: sub, term: term }; }
    if (sub.length > 1) { return rankOrAsk(sub, term); }

    return { ok: false, error: 'unresolved', term: term };
  }

  // term -> tab id, against the destinations `tabs` list ({id,label,aka[]}).
  function resolveTab(term, tabs) {
    const t = low(term);
    if (!t) { return { ok: false, error: 'unresolved', term: term }; }
    tabs = tabs || [];

    const hit = function (tab) {
      if (low(tab.id) === t || low(tab.label) === t) { return true; }
      return (tab.aka || []).some(function (a) { return low(a) === t; });
    };
    const exact = tabs.filter(hit);
    if (exact.length === 1) { return { ok: true, id: exact[0].id, label: exact[0].label, term: term }; }
    if (exact.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: exact.map(function (x) { return x.id; }).slice(0, CAND_CAP) }; }

    const has = function (tab) {
      if (low(tab.id).indexOf(t) !== -1 || low(tab.label).indexOf(t) !== -1) { return true; }
      return (tab.aka || []).some(function (a) { return low(a).indexOf(t) !== -1; });
    };
    const sub = tabs.filter(has);
    if (sub.length === 1) { return { ok: true, id: sub[0].id, label: sub[0].label, term: term }; }
    if (sub.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: sub.map(function (x) { return x.id; }).slice(0, CAND_CAP) }; }

    return { ok: false, error: 'unresolved', term: term };
  }

  // term -> node id, against the destinations `nodes` list ({id,label,group}).
  // Matches label first (what a user says), then id (the filename). Many nodes
  // share the label 'Untitled', so ambiguity is common and expected -- the
  // candidates carry the group so the guide can disambiguate out loud.
  function resolveNode(term, nodes) {
    const t = low(term);
    if (!t) { return { ok: false, error: 'unresolved', term: term }; }
    nodes = nodes || [];

    const idBase = function (n) { return low(n.id).replace(/\.md$/, ''); };
    const asCand = function (n) { return { id: n.id, label: n.label, group: n.group }; };

    const labelExact = nodes.filter(function (n) { return low(n.label) === t; });
    const idExact = nodes.filter(function (n) { return idBase(n) === t; });
    const exact = labelExact.length ? labelExact : idExact;
    if (exact.length === 1) { return { ok: true, id: exact[0].id, label: exact[0].label, group: exact[0].group, term: term }; }
    if (exact.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: exact.slice(0, CAND_CAP).map(asCand) }; }

    const sub = nodes.filter(function (n) { return low(n.label).indexOf(t) !== -1 || idBase(n).indexOf(t) !== -1; });
    if (sub.length === 1) { return { ok: true, id: sub[0].id, label: sub[0].label, group: sub[0].group, term: term }; }
    if (sub.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: sub.slice(0, CAND_CAP).map(asCand) }; }

    return { ok: false, error: 'unresolved', term: term };
  }

  // term -> a knob's concrete option value, against a knob spec's declared
  // values ({v, aka[]}). Fuzzy like resolveGroups because a user says the
  // spoken label ("waveform"), not the DOM option value ("wave"). v1 knob
  // tabs are T1 selects/checkboxes (redesign section 8); the shell writes
  // `value` into the bound control. Same result contract as the other
  // resolvers so ambiguity rides in the result (no model memory needed).
  function resolveKnobValue(term, knobSpec) {
    const t = low(term);
    const vals = (knobSpec && knobSpec.values) || [];
    const allowed = vals.map(function (x) { return x.v; });
    if (!t) { return { ok: false, error: 'unresolved_value', term: term, knob: knobSpec && knobSpec.id, allowed: allowed }; }

    const byV = vals.filter(function (x) { return low(x.v) === t; });
    if (byV.length === 1) { return { ok: true, value: byV[0].v, term: term }; }

    const byAka = vals.filter(function (x) { return (x.aka || []).some(function (a) { return low(a) === t; }); });
    if (byAka.length === 1) { return { ok: true, value: byAka[0].v, term: term }; }
    if (byAka.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: byAka.map(function (x) { return x.v; }).slice(0, CAND_CAP) }; }

    const sub = vals.filter(function (x) {
      return low(x.v).indexOf(t) !== -1 || (x.aka || []).some(function (a) { return low(a).indexOf(t) !== -1; });
    });
    if (sub.length === 1) { return { ok: true, value: sub[0].v, term: term }; }
    if (sub.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: sub.map(function (x) { return x.v; }).slice(0, CAND_CAP) }; }

    return { ok: false, error: 'unresolved_value', term: term, knob: knobSpec && knobSpec.id, allowed: allowed };
  }

  // term -> a knob SPEC, against the active tab's declared knobs. Same fuzzy
  // contract as resolveKnobValue, and for the same reason: the user says the
  // word printed on the control, which is not always the knob id. metabolism's
  // metric select is labelled "Amplitude" on screen -- "set amplitude output"
  // must work, or voice cannot reach a control the user is looking straight at.
  // Matches id, then `label`, then `aka`, then substring.
  //
  // NOTE: the parser takes the knob as the FIRST TOKEN of `set <knob> <value>`,
  // so knob names and their aliases must be single words -- a two-word alias is
  // unparseable, not merely unmatched. verbs.json's grammar check enforces the
  // shape; keep aliases single-token when authoring a manifest.
  function resolveKnob(term, knobs) {
    const t = low(term);
    knobs = knobs || [];
    const ids = knobs.map(function (k) { return k.id; });
    if (!t) { return { ok: false, error: 'unknown_knob', knob: term, supported: ids }; }

    const byId = knobs.filter(function (k) { return low(k.id) === t; });
    if (byId.length === 1) { return { ok: true, spec: byId[0], term: term }; }

    const byLabel = knobs.filter(function (k) { return low(k.label) === t; });
    if (byLabel.length === 1) { return { ok: true, spec: byLabel[0], term: term }; }

    const byAka = knobs.filter(function (k) { return (k.aka || []).some(function (a) { return low(a) === t; }); });
    if (byAka.length === 1) { return { ok: true, spec: byAka[0], term: term }; }
    if (byAka.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: byAka.map(function (k) { return k.id; }).slice(0, CAND_CAP) }; }

    const sub = knobs.filter(function (k) {
      return low(k.id).indexOf(t) !== -1 || low(k.label).indexOf(t) !== -1 ||
             (k.aka || []).some(function (a) { return low(a).indexOf(t) !== -1; });
    });
    if (sub.length === 1) { return { ok: true, spec: sub[0], term: term }; }
    if (sub.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: sub.map(function (k) { return k.id; }).slice(0, CAND_CAP) }; }

    return { ok: false, error: 'unknown_knob', knob: term, supported: ids };
  }

  // A FAMILY is a second filter dimension on the same tab: edge types, layers,
  // content tags. They are addressed by qualifier -- "hide edges mention" --
  // so the verb set stays fixed while the number of dimensions grows, which is
  // the whole point of assignments-over-dimensions. Without this they were
  // simply unreachable: `filters` is defined as groupVisibility (a NODE-group
  // map), so nothing in the grammar could ever name an edge.
  function resolveFamily(term, families) {
    const t = low(term);
    families = families || [];
    for (let i = 0; i < families.length; i++) {
      const f = families[i];
      if (low(f.id) === t || (f.aka || []).some(function (a) { return low(a) === t; })) { return f; }
    }
    return null;
  }
  // Terms -> concrete member keys of one family. Same fuzzy contract as the
  // group resolver, and unresolved terms ride back so the caller can say which
  // words it could not place rather than silently dropping them.
  function resolveFamilyValues(terms, family) {
    const keys = [], unresolved = [];
    const vals = (family && family.values) || [];
    for (const term of terms) {
      const t = low(term);
      let hit = vals.filter(function (v) { return low(v.v) === t; })[0];
      if (!hit) { hit = vals.filter(function (v) { return (v.aka || []).some(function (a) { return low(a) === t; }); })[0]; }
      if (!hit) { hit = vals.filter(function (v) { return low(v.v).indexOf(t) !== -1; })[0]; }
      if (hit) { if (keys.indexOf(hit.v) === -1) { keys.push(hit.v); } }
      else { unresolved.push(term); }
    }
    return { keys: keys, unresolved: unresolved };
  }

  // ---- the coverage audit (pure core; redesign section 9) ------------------
  //
  // The north star made checkable: every control a user can operate on a tab
  // must be a bound knob or an explicit exclusion, else voice cannot reach it.
  // This is the PURE diff; the browser enumerates the tab's LIVE interactive
  // element ids (the Sociogram's 29 filter checkboxes exist only as runtime
  // innerHTML -- static HTML parsing is provably blind, so enumeration must be
  // runtime) and feeds them in. Tests inject a static id list.
  //   declaredBindIds  ids the manifest's knobs bind (['view','metric',...])
  //   liveControlIds   ids of the tab's live interactive controls
  //   excluded         ids intentionally outside the voice surface (with reason, elsewhere)
  // Returns ok:false (loud) when a live control is neither bound nor excluded.
  function auditCoverage(declaredBindIds, liveControlIds, excluded) {
    declaredBindIds = declaredBindIds || [];
    liveControlIds = liveControlIds || [];
    excluded = excluded || [];
    const has = function (arr, id) { return arr.indexOf(id) !== -1; };
    const unbound = liveControlIds.filter(function (id) { return !has(declaredBindIds, id) && !has(excluded, id); });
    const missing = declaredBindIds.filter(function (id) { return !has(liveControlIds, id); });
    return { ok: unbound.length === 0, unbound: unbound, missing: missing };
  }

  // Gestures: the half of the surface the DOM sweep is structurally blind to.
  //
  // Zoom, pan, node-drag and hover are things a user DOES to the graph with no
  // control element behind them, so auditCoverage -- which enumerates live
  // elements -- reported "0 uncovered" on the Sociogram while an entire
  // interaction modality was unreachable by voice (2026-07-25, Tom asked to
  // zoom and center and there was nothing to call). Gestures cannot be
  // discovered at runtime; they can only be DECLARED. So the gate's job is to
  // verify the declaration is honest rather than to find them:
  //   - every gesture carries a status (covered | deferred | excluded)
  //   - `covered` must name verbs the tab ACTUALLY has in caps -- claiming
  //     coverage by a verb that does not exist is the exact failure this
  //     catches, and is invisible to any other check
  //   - `deferred` must name the increment that closes it; `excluded` a reason
  //   - a tab with NO declaration fails: silence is not a claim of completeness
  const GESTURE_STATUS = ['covered', 'deferred', 'excluded'];

  function auditGestures(gestures, caps) {
    caps = caps || [];
    const problems = [];
    if (!gestures || !gestures.length) {
      return { ok: false, problems: ['no gestures declared -- a tab must state its non-DOM surface, even if only to say there is none'], counts: {} };
    }
    const counts = { covered: 0, deferred: 0, excluded: 0 };
    gestures.forEach(function (g) {
      const id = (g && g.id) || '(unnamed)';
      if (!g || GESTURE_STATUS.indexOf(g.status) === -1) {
        problems.push(id + ': status must be one of ' + GESTURE_STATUS.join('/'));
        return;
      }
      counts[g.status]++;
      if (g.status === 'covered') {
        const by = g.by || [];
        if (!by.length) { problems.push(id + ': marked covered but names no verb'); }
        by.forEach(function (v) {
          if (caps.indexOf(v) === -1) { problems.push(id + ': claims verb "' + v + '" which this tab does not support'); }
        });
      }
      if (g.status === 'deferred' && !g.planned) { problems.push(id + ': deferred with no increment named'); }
      if (g.status === 'excluded' && !g.reason) { problems.push(id + ': excluded with no reason'); }
    });
    return { ok: problems.length === 0, problems: problems, counts: counts };
  }

  // ---- the journal ---------------------------------------------------------
  //
  // Per-tab undo/redo over ABSOLUTE vectors {dim, before, after} (redesign
  // section 7). Absolute (not delta) so replay is deterministic and immune to
  // the single-writer delusion: `before` is captured by the dispatcher as
  // read() AT COMMAND TIME, so a mouse change between commands is already
  // reflected. The journal is value-opaque -- it never inspects before/after,
  // it just stores and hands them back -- which is exactly why it is pure and
  // testable without a DOM.
  //
  //   record(tab, {dim, before, after})  push; clears the redo stack; caps
  //   undo(tab)  -> {dim, value:before} to write, or null if nothing to undo
  //   redo(tab)  -> {dim, value:after}  to write, or null
  //
  // reset (-> boot-captured defaults) and restore (-> cross-tab snapshot) are
  // shell-orchestrated snapshot writes, NOT journal-stack ops, so they live in
  // the dispatcher; the grammar routes them to @journal but the shell owns the
  // snapshots (section 7). Tab navigation undo likewise goes through restore,
  // not this stack.
  function createJournal(opts) {
    const cap = (opts && opts.cap) || 20;
    const undoStacks = Object.create(null);  // tab -> [entry...]
    const redoStacks = Object.create(null);

    const undoOf = function (tab) { return (undoStacks[tab] || (undoStacks[tab] = [])); };
    const redoOf = function (tab) { return (redoStacks[tab] || (redoStacks[tab] = [])); };

    return {
      record: function (tab, entry) {
        if (!entry || entry.dim == null) { throw new Error('journal.record needs {dim, before, after}'); }
        const u = undoOf(tab);
        u.push({ dim: entry.dim, before: entry.before, after: entry.after });
        while (u.length > cap) { u.shift(); }   // drop oldest beyond the cap
        redoStacks[tab] = [];                    // a fresh action invalidates redo
        return this;
      },
      undo: function (tab) {
        const u = undoOf(tab);
        if (!u.length) { return null; }
        const e = u.pop();
        redoOf(tab).push(e);
        return { dim: e.dim, value: e.before };
      },
      redo: function (tab) {
        const r = redoOf(tab);
        if (!r.length) { return null; }
        const e = r.pop();
        undoOf(tab).push(e);
        return { dim: e.dim, value: e.after };
      },
      canUndo: function (tab) { return undoOf(tab).length > 0; },
      canRedo: function (tab) { return redoOf(tab).length > 0; },
      depth: function (tab) { return undoOf(tab).length; },
    };
  }

  // ---- the dispatcher: pure planner ----------------------------------------
  //
  // plan(op, ctx) turns a parsed op + live context into an execution INTENT for
  // the active tab -- or an early error (ambiguous / unresolved / unsupported)
  // that the adapter speaks without touching the DOM (redesign section 5, 8).
  // It is pure: name resolution runs against injected indexes; the actual
  // before/after reads and global calls happen in the browser adapter, which
  // consumes this plan. Splitting it this way keeps the hard logic testable
  // headless and leaves the adapter a thin, per-tab shim (section 8, T2/T3).
  //
  //   ctx = { caps:[verb...], roster:[groupKey...], tabs:[...], nodes:[...] }
  //   caps is the tab's supported-verb list -- the unsupported_here `supported`
  //   array is derived FROM it, so it can never be stale prose (section 5, F1).
  //
  // Intent kinds: 'shell' | 'filters' | 'selection' | 'highlight' | 'camera' |
  //               'journal' | 'read'. Each carries a `journal` {dim} when the
  //               adapter should record an absolute vector around it.

  // v1 Sociogram support set. zoom/set/read/ask are deliberately absent -- they
  // resolve to unsupported_here (spoken plainly) until a later increment or
  // Tom's gate promotes them (section 10, 13, 16). Promote by adding here.
  // What a view with no manifest can honestly do: move and be asked about.
  // The shell used to fall back to SOCIOGRAM_CAPS on an unmapped page, so a
  // chapter page advertised filtering it cannot perform -- the same class of
  // dishonesty as reporting state the screen does not support.
  const SHELL_CAPS = ['go', 'back', 'what', 'where', 'help'];

  const SOCIOGRAM_CAPS = [
    'go', 'back',
    'show', 'hide', 'only', 'all', 'none',
    'open', 'close',
    'find', 'clear', 'focus',
    'fit', 'zoom', 'pan',
    'pick', 'next', 'previous',
    'read', 'stop',
    'undo', 'redo', 'reset', 'restore',
    'what', 'where', 'help',
  ];

  // A verb that means something HERE under another name is worth naming, once.
  // "open the first card" on a content tab is not a confused request -- picking
  // an item IS opening it -- but it used to come back as a ten-verb word list,
  // which on a voice-only surface is close to no answer at all. Data, not a
  // branch: a verb declares `near`, and it is offered only when the near verb
  // is actually supported on this view.
  function unsupported(op, caps, grammar) {
    // Carry the ARGUMENT through. A rejected verb is not always a rejected
    // request: "Prima Pars, Question 18, Article 1" came back as "that kind of
    // search isn't supported here" because the guide chose `find` for what was
    // an ADDRESS, and the words the user actually said were dropped at the door
    // (Tom, 2026-07-27). The shell can only offer a better reading if it still
    // has them.
    const out = { ok: false, error: 'unsupported_here', verb: op.verb, supported: caps.slice().sort(),
                  term: (op.args && op.args.length === 1 && typeof op.args[0] === 'string') ? op.args[0] : null };
    const spec = grammar && grammar.byVerb ? grammar.byVerb[op.verb] : null;
    if (spec && spec.near && caps.indexOf(spec.near) !== -1) { out.near = spec.near; }
    return out;
  }

  // Resolve every term of a multi-term filter/focus op against the roster.
  // Ambiguity in ANY term stops execution (the guide asks); unresolved terms
  // are reported but do not block the resolved subset.
  function resolveTerms(args, roster) {
    const keys = [];
    const unresolved = [], guesses = [];
    for (const term of args) {
      const r = resolveGroups(term, roster);
      if (r.ok) {
        for (const k of r.keys) { if (keys.indexOf(k) === -1) { keys.push(k); } }
        // A low-confidence hit rides back so the spoken answer can own it.
        if (r.confidence === 'low') { guesses.push({ term: r.term, chose: r.keys[0], alternatives: r.alternatives || [] }); }
      }
      else if (r.error === 'ambiguous') { return { ambiguous: r }; }
      else { unresolved.push(term); }
    }
    return { keys: keys, unresolved: unresolved, guesses: guesses };
  }

  function plan(op, ctx) {
    ctx = ctx || {};
    const caps = ctx.caps || SOCIOGRAM_CAPS;
    if (!op || op.ok !== true) { return op; }                 // pass parse errors through
    if (caps.indexOf(op.verb) === -1) { return unsupported(op, caps, ctx.grammar); }

    switch (op.verb) {
      case 'go': {
        // Ordering rides on the verb we already have. The tabs ARE arranged
        // left-to-right on screen and a voice user cannot see that, so it has
        // to be sayable: "go next" walks the row in its visible order.
        const step = low(op.args[0]);
        if (step === 'next' || step === 'previous' || step === 'first' || step === 'last') {
          return { ok: true, kind: 'shell', action: 'stepTab', dir: step, journal: { dim: 'tab' } };
        }
        const r = resolveTab(op.args[0], ctx.tabs);
        // Carry the verb so the shell can answer "which tabs, then?" -- an
        // unknown tab fails in the RESOLVER, never reaching the dispatcher.
        if (!r.ok) { r.verb = 'go'; return r; }
        // Carry the RAW term alongside the resolved tab. A tab always wins here
        // -- destinations.json is authoritative and sub-views resolve only on
        // `unresolved` -- so a sub-view whose name is also a tab name ("the Agent
        // Map's sociogram view") could never be reached: `go sociogram` matched
        // the Sociogram TAB every time and the user was thrown across the app
        // (Tom, 2026-07-26). The shell needs the original words to notice that
        // the user is standing on a tab whose own view they just named.
        return { ok: true, kind: 'shell', action: 'switchTab', tab: r.id, label: r.label, term: op.args[0], journal: { dim: 'tab' } };
      }
      case 'back':
        return { ok: true, kind: 'shell', action: 'back', journal: { dim: 'tab' } };

      case 'show': case 'hide': case 'only': {
        const action = op.op; // 'union' | 'diff' | 'set'
        const fam = resolveFamily(op.args[0], ctx.families);
        if (fam) {
          const rest = op.args.slice(1);
          if (!rest.length) { return { ok: false, error: 'missing_arg', verb: op.verb, note: 'name which ' + fam.id + ' -- or say "all ' + fam.id + '"' }; }
          const rv = resolveFamilyValues(rest, fam);
          if (!rv.keys.length) { return { ok: false, error: 'unresolved_value', term: rest.join(' '), knob: fam.id, allowed: fam.values.map(function (v) { return v.v; }) }; }
          return { ok: true, kind: 'family', family: fam.id, state: fam.state, action: action, keys: rv.keys, unresolved: rv.unresolved, journal: { dim: 'family:' + fam.id } };
        }
        const res = resolveTerms(op.args, ctx.roster);
        if (res.ambiguous) { return res.ambiguous; }
        if (!res.keys.length) { return { ok: false, error: 'unresolved', term: op.args.join(' ') }; }
        return { ok: true, kind: 'filters', action: action, keys: res.keys, unresolved: res.unresolved,
                 guesses: res.guesses, journal: { dim: 'filters' } };
      }
      case 'all': case 'none': {
        const famAll = resolveFamily(op.args[0], ctx.families);
        if (famAll) {
          return { ok: true, kind: 'family', family: famAll.id, state: famAll.state, action: op.verb,
                   keys: famAll.values.map(function (v) { return v.v; }), unresolved: [], journal: { dim: 'family:' + famAll.id } };
        }
        return { ok: true, kind: 'filters', action: op.verb, journal: { dim: 'filters' } };
      }

      case 'open': {
        const term = op.args.length ? op.args[0] : '';
        // A tab whose items declare how they OPEN resolves the name against
        // what is ON SCREEN, not against the vault index: a Summa question is
        // not a node, so resolving it there could only ever fail ("Could not
        // find the nature and extent of sacred doctrine"). The matching itself
        // stays in the shell, which is the only side that can see the rows and
        // already reports ambiguity honestly -- two matchers would drift.
        if (ctx.activates) { return { ok: true, kind: 'selection', action: 'open', label: term, journal: { dim: 'selection' } }; }
        if (!term) { return { ok: false, error: 'missing_arg', verb: 'open' }; }
        const r = resolveNode(term, ctx.nodes);
        if (!r.ok) { return r; }
        return { ok: true, kind: 'selection', action: 'open', id: r.id, label: r.label, group: r.group, journal: { dim: 'selection' } };
      }
      case 'close':
        return { ok: true, kind: 'selection', action: 'close', journal: { dim: 'selection' } };

      case 'find':
        return { ok: true, kind: 'highlight', action: 'find', text: op.args[0], journal: { dim: 'highlight' } };
      case 'clear':
        return { ok: true, kind: 'highlight', action: 'clear', journal: { dim: 'highlight' } };
      case 'focus': {
        const res = resolveTerms(op.args, ctx.roster);
        if (res.ambiguous) { return res.ambiguous; }
        if (res.keys.length < 2) { return { ok: false, error: 'unresolved', term: op.args.join(' ~ '), note: 'focus needs two resolvable groups' }; }
        return { ok: true, kind: 'highlight', action: 'focus', keys: res.keys, unresolved: res.unresolved, journal: { dim: 'highlight' } };
      }

      case 'set': {
        // set <knob> <value> -- validate against THIS tab's declared knobs
        // (ctx.knobs from the per-tab manifest). T1 tabs bind a select/checkbox;
        // the shell writes `value` into `bind` (redesign sections 3, 8).
        const knobs = ctx.knobs || [];
        const rk = resolveKnob(op.knob, knobs);
        if (!rk.ok) { return rk; }
        const spec = rk.spec;
        const rv = resolveKnobValue(op.args[0], spec);
        if (!rv.ok) { return rv; }
        return { ok: true, kind: 'knob', knob: spec.id, value: rv.value, bind: spec.bind, journal: { dim: 'knob:' + spec.id } };
      }

      // The CURSOR walks the currently revealed set: pick random/first/last,
      // then next/previous. Voice-only exploration needs a way to reach ONE
      // node out of a reveal without a mouse, and the random pick belongs in
      // code rather than in the model (deterministic plumbing is not a
      // judgement call). Scope is whatever is revealed, which auto-framing
      // already defines precisely.
      case 'pick':
        return { ok: true, kind: 'cursor', action: 'pick', mode: op.args[0], journal: { dim: 'selection' } };
      case 'next': case 'previous':
        return { ok: true, kind: 'cursor', action: 'step', dir: op.verb, journal: { dim: 'selection' } };

      // Playback drives the PAGE's own TTS, never the realtime audio channel:
      // verbatim, interruptible, cheap, and stoppable (redesign section 14.7).
      case 'read': case 'stop':
        // `read` bare reads the prose; `read details` reads the provenance the
        // speech script holds back (see the shell's speechScript).
        var scope = low(op.args[0]);
        return { ok: true, kind: 'playback', action: op.verb,
                 mode: (scope && scope !== op.verb) ? scope : 'prose', journal: { dim: 'playback' } };

      case 'fit':
        return { ok: true, kind: 'camera', action: 'fit', journal: { dim: 'camera' } };

      // zoom in|out -- the grammar declared this verb from the start; it simply
      // had no plan case or dispatcher, so "zoom in so I can see them" hit a
      // model with nothing to call and it narrated instead of acting. Discrete
      // steps only: the semantic tier holds, and camera stays out of the
      // journal (section 14.4 bars HASHING continuous fields, not reaching them).
      case 'zoom':
        return { ok: true, kind: 'camera', action: 'zoom', dir: op.args[0], journal: { dim: 'camera' } };

      // pan left|right|up|down -- VIEW-relative: "pan left" shows what lies to
      // the left. Together with zoom in/out and fit the camera dimension is now
      // symmetric, which is the bar this design sets for every dimension.
      case 'pan':
        return { ok: true, kind: 'camera', action: 'pan', dir: op.args[0], journal: { dim: 'camera' } };

      case 'undo': case 'redo': case 'reset': case 'restore':
        return { ok: true, kind: 'journal', action: op.verb };

      case 'what': case 'where': case 'help':
        return { ok: true, kind: 'read', action: op.verb };

      default:
        return unsupported(op, caps, ctx.grammar);
    }
  }

  return {
    VERSION: VERSION,
    compileGrammar: compileGrammar,
    parse: parse,
    normalize: normalize,
    resolveGroups: resolveGroups,
    resolveTab: resolveTab,
    resolveNode: resolveNode,
    resolveKnobValue: resolveKnobValue,
    resolveKnob: resolveKnob,
    resolveFamily: resolveFamily,
    resolveFamilyValues: resolveFamilyValues,
    auditCoverage: auditCoverage,
    auditGestures: auditGestures,
    createJournal: createJournal,
    plan: plan,
    SOCIOGRAM_CAPS: SOCIOGRAM_CAPS,
    SHELL_CAPS: SHELL_CAPS,
  };
});
