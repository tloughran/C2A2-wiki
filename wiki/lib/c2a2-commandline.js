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
    return { byVerb: byVerb, dimensions: verbsJson.dimensions, verbs: verbsJson.verbs };
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

    const spec = grammar.byVerb[verb];
    if (!spec) { return err('unknown_verb', echo, { verb: verb }); }

    switch (spec.args) {

      case 'none': {
        if (rest) { return err('too_many_args', echo, { verb: verb }); }
        // const-valued verbs (fit/read/stop) carry their fixed value as the arg
        const args = Object.prototype.hasOwnProperty.call(spec, 'const') ? [spec['const']] : [];
        return ok(spec, args, echo);
      }

      case 'one': {
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        if (rest.indexOf(' ') !== -1) { return err('too_many_args', echo, { verb: verb }); }
        if (spec.enum && spec.enum.indexOf(rest) === -1) {
          return err('bad_enum', echo, { verb: verb, allowed: spec.enum });
        }
        return ok(spec, [rest], echo);
      }

      case 'text': {
        if (!rest) { return err('missing_arg', echo, { verb: verb }); }
        return ok(spec, [rest], echo);  // whole remainder = one free-text arg
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

  function low(s) { return String(s == null ? '' : s).toLowerCase().trim(); }
  function leaf(key) { const i = key.lastIndexOf('/'); return i === -1 ? key : key.slice(i + 1); }

  // term -> group key(s). A term naming a whole SECTION (e.g. 'traditions')
  // expands to every key under it, so "hide traditions" is one symmetric op.
  function resolveGroups(term, roster) {
    const t = low(term);
    if (!t) { return { ok: false, error: 'unresolved', term: term }; }
    roster = roster || [];

    const section = roster.filter(function (k) { return low(k).indexOf(t + '/') === 0; });
    if (section.length) { return { ok: true, keys: section, section: true, term: term }; }

    const exact = roster.filter(function (k) { return low(k) === t || low(leaf(k)) === t; });
    if (exact.length) { return { ok: true, keys: exact, term: term }; }

    const prefix = roster.filter(function (k) { return low(leaf(k)).indexOf(t) === 0; });
    if (prefix.length === 1) { return { ok: true, keys: prefix, term: term }; }
    if (prefix.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: prefix.slice(0, CAND_CAP) }; }

    const sub = roster.filter(function (k) { return low(leaf(k)).indexOf(t) !== -1; });
    if (sub.length === 1) { return { ok: true, keys: sub, term: term }; }
    if (sub.length > 1) { return { ok: false, error: 'ambiguous', term: term, candidates: sub.slice(0, CAND_CAP) }; }

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
  const SOCIOGRAM_CAPS = [
    'go', 'back',
    'show', 'hide', 'only', 'all', 'none',
    'open', 'close',
    'find', 'clear', 'focus',
    'fit',
    'undo', 'redo', 'reset', 'restore',
    'what', 'where', 'help',
  ];

  function unsupported(op, caps) {
    return { ok: false, error: 'unsupported_here', verb: op.verb, supported: caps.slice().sort() };
  }

  // Resolve every term of a multi-term filter/focus op against the roster.
  // Ambiguity in ANY term stops execution (the guide asks); unresolved terms
  // are reported but do not block the resolved subset.
  function resolveTerms(args, roster) {
    const keys = [];
    const unresolved = [];
    for (const term of args) {
      const r = resolveGroups(term, roster);
      if (r.ok) { for (const k of r.keys) { if (keys.indexOf(k) === -1) { keys.push(k); } } }
      else if (r.error === 'ambiguous') { return { ambiguous: r }; }
      else { unresolved.push(term); }
    }
    return { keys: keys, unresolved: unresolved };
  }

  function plan(op, ctx) {
    ctx = ctx || {};
    const caps = ctx.caps || SOCIOGRAM_CAPS;
    if (!op || op.ok !== true) { return op; }                 // pass parse errors through
    if (caps.indexOf(op.verb) === -1) { return unsupported(op, caps); }

    switch (op.verb) {
      case 'go': {
        const r = resolveTab(op.args[0], ctx.tabs);
        if (!r.ok) { return r; }
        return { ok: true, kind: 'shell', action: 'switchTab', tab: r.id, label: r.label, journal: { dim: 'tab' } };
      }
      case 'back':
        return { ok: true, kind: 'shell', action: 'back', journal: { dim: 'tab' } };

      case 'show': case 'hide': case 'only': {
        const action = op.op; // 'union' | 'diff' | 'set'
        const res = resolveTerms(op.args, ctx.roster);
        if (res.ambiguous) { return res.ambiguous; }
        if (!res.keys.length) { return { ok: false, error: 'unresolved', term: op.args.join(' ') }; }
        return { ok: true, kind: 'filters', action: action, keys: res.keys, unresolved: res.unresolved, journal: { dim: 'filters' } };
      }
      case 'all':
        return { ok: true, kind: 'filters', action: 'all', journal: { dim: 'filters' } };
      case 'none':
        return { ok: true, kind: 'filters', action: 'none', journal: { dim: 'filters' } };

      case 'open': {
        const r = resolveNode(op.args[0], ctx.nodes);
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
        let spec = null;
        for (let i = 0; i < knobs.length; i++) { if (low(knobs[i].id) === low(op.knob)) { spec = knobs[i]; break; } }
        if (!spec) { return { ok: false, error: 'unknown_knob', knob: op.knob, supported: knobs.map(function (k) { return k.id; }) }; }
        const rv = resolveKnobValue(op.args[0], spec);
        if (!rv.ok) { return rv; }
        return { ok: true, kind: 'knob', knob: spec.id, value: rv.value, bind: spec.bind, journal: { dim: 'knob:' + spec.id } };
      }

      case 'fit':
        return { ok: true, kind: 'camera', action: 'fit', journal: { dim: 'camera' } };

      case 'undo': case 'redo': case 'reset': case 'restore':
        return { ok: true, kind: 'journal', action: op.verb };

      case 'what': case 'where': case 'help':
        return { ok: true, kind: 'read', action: op.verb };

      default:
        return unsupported(op, caps);
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
    auditCoverage: auditCoverage,
    createJournal: createJournal,
    plan: plan,
    SOCIOGRAM_CAPS: SOCIOGRAM_CAPS,
  };
});
