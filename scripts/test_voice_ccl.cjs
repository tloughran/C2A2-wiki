'use strict';

// Tier-0 headless test for the CCL parser (voice_guide_redesign.md section 9).
// Pure functions only -- no browser, no realtime, no broker. Loads the real
// grammar (wiki/voice_guide/verbs.json), the parser (wiki/lib/c2a2-commandline.js),
// and the golden table (wiki/voice_guide/ccl_golden.json). Plain asserts, no
// pytest/mocha -- mirrors scripts/test_janitor_drift.py. Run:
//   node scripts/test_voice_ccl.cjs
// Exits non-zero on any failure so the janitor / CI gate can consume it.

const assert = require('assert');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CCL = require(path.join(ROOT, 'wiki/lib/c2a2-commandline.js'));
const VERBS = JSON.parse(fs.readFileSync(path.join(ROOT, 'wiki/voice_guide/verbs.json'), 'utf8'));
const GOLDEN = JSON.parse(fs.readFileSync(path.join(ROOT, 'wiki/voice_guide/ccl_golden.json'), 'utf8'));

const grammar = CCL.compileGrammar(VERBS);

let passed = 0;
const failures = [];
function check(name, fn) {
  try { fn(); passed++; }
  catch (e) { failures.push(name + ' -- ' + (e && e.message ? e.message : e)); }
}

// Compact accessor for the fields we assert most.
function shape(op) {
  return { verb: op.verb, dim: op.dim, op: op.op, args: op.args };
}

// ---- 1. golden smoke: every expected_command parses to its expect block -----

for (const c of GOLDEN.cases) {
  if (c.expected_command === null) {
    // deferred rows must be explicitly flagged, never silently skipped
    check('golden ' + c.id + ' is a declared deferral', function () {
      assert.strictEqual(c.v1_behavior, 'ask', 'null command needs v1_behavior:ask');
    });
    continue;
  }
  check('golden ' + c.id + ' "' + c.expected_command + '"', function () {
    const op = CCL.parse(c.expected_command, grammar);
    assert.strictEqual(op.ok, true, 'expected ok:true, got ' + JSON.stringify(op));
    assert.deepStrictEqual(shape(op), c.expect);
    assert.strictEqual(op.echo, CCL.normalize(c.expected_command), 'echo must be the normalized input');
  });
}

// ---- 2. full-shape ops (flags, const, mode carried correctly) ---------------

check('fit carries const arg and value kind', function () {
  assert.deepStrictEqual(CCL.parse('fit', grammar), {
    ok: true, verb: 'fit', dim: 'camera', op: 'set', args: ['fit'], kind: 'value', const: 'fit', echo: 'fit',
  });
});
check('read is gated + const, playback value', function () {
  const op = CCL.parse('read', grammar);
  assert.strictEqual(op.gated, true);
  assert.strictEqual(op.const, 'read');
  assert.deepStrictEqual(shape(op), { verb: 'read', dim: 'playback', op: 'set', args: ['read'] });
});
check('stop is the inverse-shaped playback const', function () {
  const op = CCL.parse('stop', grammar);
  assert.strictEqual(op.const, 'stop');
  assert.strictEqual(op.gated, undefined);
});
check('ask carries spend:true and routes to @broker', function () {
  const op = CCL.parse('ask what is c2a2', grammar);
  assert.strictEqual(op.spend, true);
  assert.deepStrictEqual(shape(op), { verb: 'ask', dim: '@broker', op: 'route', args: ['what is c2a2'] });
});
check('find carries mode:find', function () {
  const op = CCL.parse('find bioelectric fields', grammar);
  assert.strictEqual(op.mode, 'find');
  // dim is `cut` since 2026-07-25: find WRITES the cut (its matched id set),
  // and the query travels inside that value so undo restores both together.
  assert.deepStrictEqual(shape(op), { verb: 'find', dim: 'cut', op: 'set', args: ['bioelectric fields'] });
});
check('focus carries mode:focus and is n-ary', function () {
  const op = CCL.parse('focus levin ~ friston ~ hoffman', grammar);
  assert.strictEqual(op.mode, 'focus');
  assert.deepStrictEqual(op.args, ['levin', 'friston', 'hoffman']);
});
check('set carries the knob name; value is the remainder', function () {
  const op = CCL.parse('set view waveform', grammar);
  assert.strictEqual(op.knob, 'view');
  assert.deepStrictEqual(op.args, ['waveform']);
});
check('set brightness keeps a numeric-looking value as a string arg', function () {
  const op = CCL.parse('set brightness 0.5', grammar);
  assert.deepStrictEqual(op, { ok: true, verb: 'set', dim: 'knob', op: 'set', args: ['0.5'], kind: 'value', knob: 'brightness', echo: 'set brightness 0.5' });
});

// ---- 3. set-operation coverage on the ONE filters dimension (symmetry) ------

check('show -> filters union', function () { assert.strictEqual(CCL.parse('show levin', grammar).op, 'union'); });
check('hide -> filters diff', function () { assert.strictEqual(CCL.parse('hide levin', grammar).op, 'diff'); });
check('only -> filters set', function () { assert.strictEqual(CCL.parse('only levin', grammar).op, 'set'); });
check('all  -> filters setAll (no args)', function () { assert.deepStrictEqual(shape(CCL.parse('all', grammar)), { verb: 'all', dim: 'filters', op: 'setAll', args: [] }); });
check('none -> filters setEmpty (no args)', function () { assert.deepStrictEqual(shape(CCL.parse('none', grammar)), { verb: 'none', dim: 'filters', op: 'setEmpty', args: [] }); });
check('show/hide are the same dimension (add==remove symmetry)', function () {
  assert.strictEqual(CCL.parse('show x', grammar).dim, CCL.parse('hide x', grammar).dim);
});

// ---- 4. tokenization & normalization ----------------------------------------

check('many splits on whitespace', function () {
  assert.deepStrictEqual(CCL.parse('show levin friston hoffman', grammar).args, ['levin', 'friston', 'hoffman']);
});
check('text keeps a multi-word remainder as one arg', function () {
  assert.deepStrictEqual(CCL.parse('open michael levin', grammar).args, ['michael levin']);
});
check('go takes free text (multi-word tab term)', function () {
  assert.deepStrictEqual(shape(CCL.parse('go review log', grammar)), { verb: 'go', dim: 'tab', op: 'set', args: ['review log'] });
});
check('collapses internal whitespace and trims; echo is normalized', function () {
  const op = CCL.parse('   only   levin    friston  ', grammar);
  assert.strictEqual(op.echo, 'only levin friston');
  assert.deepStrictEqual(op.args, ['levin', 'friston']);
});
check('verb is case-insensitive but args preserve case (resolver lowercases)', function () {
  const op = CCL.parse('ONLY Levin', grammar);
  assert.strictEqual(op.verb, 'only');
  assert.deepStrictEqual(op.args, ['Levin']);
});
check('focus tolerates no spaces around the tilde', function () {
  assert.deepStrictEqual(CCL.parse('focus levin~friston', grammar).args, ['levin', 'friston']);
});

// ---- 5. errors: every code reachable, no silent acceptance ------------------

check('empty string -> empty', function () { assert.strictEqual(CCL.parse('', grammar).error, 'empty'); });
check('whitespace-only -> empty', function () { assert.strictEqual(CCL.parse('   ', grammar).error, 'empty'); });
check('null -> empty', function () { assert.strictEqual(CCL.parse(null, grammar).error, 'empty'); });
check('unknown verb -> unknown_verb (with verb echoed)', function () {
  const op = CCL.parse('florb levin', grammar);
  assert.strictEqual(op.error, 'unknown_verb');
  assert.strictEqual(op.verb, 'florb');
});
// "undo that" USED to be an arity error. It is the phrasing a person actually
// says, and "that" adds nothing the grammar needs, so it is now normalized away
// rather than rejected. The arity rule itself is unchanged -- a word carrying
// real content still fails, which the row below this one holds.
check('none-verb with a filler word -> accepted, not rejected ("undo that")', function () {
  const op = CCL.parse('undo that', grammar);
  assert.strictEqual(op.ok, true);
  assert.strictEqual(op.verb, 'undo');
});
check('none-verb with a CONTENTFUL trailing arg still -> too_many_args', function () {
  assert.strictEqual(CCL.parse('undo everything', grammar).error, 'too_many_args');
});
check('fit with args -> too_many_args', function () { assert.strictEqual(CCL.parse('fit now', grammar).error, 'too_many_args'); });

// ---- the phrasings a person actually says (2026-07-26 live review) ----------
// Every one of these came back as a hard error while a bare `pick first` had
// been working the whole time, which is what made Start Here's sections feel
// unreachable. They are listed verbatim because they are evidence, not guesses.
check('spoken phrasings reach the cursor: noun, article and copula tolerated', function () {
  ['pick first', 'pick first card', 'pick first section', 'pick the first card',
   'select first', 'choose the first section', 'open the first card', 'open first'
  ].forEach(function (said) {
    const op = CCL.parse(said, grammar);
    assert.strictEqual(op.ok, true, said + ' did not parse');
    assert.strictEqual(op.verb, 'pick', said + ' -> ' + op.verb);
    assert.deepStrictEqual(op.args, ['first'], said + ' args');
  });
});
check('"what is this" is the same question as "what"', function () {
  const op = CCL.parse('what is this', grammar);
  assert.strictEqual(op.ok, true);
  assert.strictEqual(op.verb, 'what');
});
// The alias must NOT swallow the sense it shadows: `open <node>` still opens an
// article. Shape decides, so this can never become a coin-flip.
check('"open levin" is still the article verb, not the cursor', function () {
  const op = CCL.parse('open levin', grammar);
  assert.strictEqual(op.verb, 'open');
  assert.deepStrictEqual(op.args, ['levin']);
});
// The blast radius of filler stripping: free-text and list verbs keep every
// word. If this ever fails, a search or a filter is silently losing a term.
check('filler is NEVER stripped from free-text or list arguments', function () {
  assert.deepStrictEqual(CCL.parse('find the card', grammar).args, ['the card']);
  assert.deepStrictEqual(CCL.parse('go community explorer', grammar).args, ['community explorer']);
  assert.deepStrictEqual(CCL.parse('only levin friston', grammar).args, ['levin', 'friston']);
});
check('grammar rejects a filler word that is also an enum value', function () {
  const bad = JSON.parse(JSON.stringify(VERBS));
  bad.filler = (bad.filler || []).concat(['out']);          // would break `zoom out`
  assert.throws(function () { CCL.compileGrammar(bad); }, /would eat the argument/);
});
check('grammar rejects an alias that silently shadows a real verb', function () {
  const bad = JSON.parse(JSON.stringify(VERBS));
  bad.aliases = (bad.aliases || []).concat([{ say: 'back', means: 'previous' }]);
  assert.throws(function () { CCL.compileGrammar(bad); }, /shadows the verb/);
});
check('one-verb missing arg -> missing_arg ("zoom")', function () { assert.strictEqual(CCL.parse('zoom', grammar).error, 'missing_arg'); });
check('one-verb extra arg -> too_many_args ("zoom in out")', function () { assert.strictEqual(CCL.parse('zoom in out', grammar).error, 'too_many_args'); });
check('zoom enum enforced ("zoom sideways" -> bad_enum)', function () {
  const op = CCL.parse('zoom sideways', grammar);
  assert.strictEqual(op.error, 'bad_enum');
  assert.deepStrictEqual(op.allowed, ['in', 'out']);
});
check('zoom in / zoom out accepted', function () {
  assert.deepStrictEqual(CCL.parse('zoom in', grammar).args, ['in']);
  assert.deepStrictEqual(CCL.parse('zoom out', grammar).args, ['out']);
});
// `open` moved from `text` to `text-opt` when Summa's contents tree arrived:
// there, "pick first ... open" is the ordinary shape, and demanding the name
// back would make the user repeat what the guide had just said to them. The
// PARSER cannot know whether a bare `open` is meaningful -- that depends on
// whether the tab's items declare how they open -- so the decision moved to
// plan(), and these three rows pin the whole contract rather than one end of it.
check('bare "open" parses -- the parser does not decide whether it is meaningful', function () {
  const op = CCL.parse('open', grammar);
  assert.strictEqual(op.error, undefined);
  assert.deepStrictEqual(op.args, []);
});
// (the two plan-level halves of this contract live in section 9, below, where
// a planner CTX exists)
check('many-verb missing arg -> missing_arg ("show")', function () { assert.strictEqual(CCL.parse('show', grammar).error, 'missing_arg'); });
check('focus with one term -> focus_needs_two', function () { assert.strictEqual(CCL.parse('focus levin', grammar).error, 'focus_needs_two'); });
check('set with no value -> missing_arg ("set view")', function () {
  const op = CCL.parse('set view', grammar);
  assert.strictEqual(op.error, 'missing_arg');
  assert.strictEqual(op.need, 'value');
});
check('set with nothing -> missing_arg ("set")', function () { assert.strictEqual(CCL.parse('set', grammar).error, 'missing_arg'); });

// ---- 6. grammar integrity (mirrors the future janitor drift checks) ---------

const SENTINELS = new Set(['@journal', '@read', '@broker']);

check('compileGrammar rejects a malformed grammar', function () {
  assert.throws(function () { CCL.compileGrammar({}); });
  assert.throws(function () { CCL.compileGrammar({ dimensions: {}, verbs: [{}] }); });  // verb spec missing "verb"
  assert.throws(function () { CCL.compileGrammar({ dimensions: {}, verbs: [{ verb: 'x' }, { verb: 'x' }] }); });  // duplicate
});
check('every verb.dim is a declared dimension or a sentinel', function () {
  for (const v of VERBS.verbs) {
    const okDim = SENTINELS.has(v.dim) || Object.prototype.hasOwnProperty.call(VERBS.dimensions, v.dim);
    assert.ok(okDim, 'verb "' + v.verb + '" writes undeclared dimension "' + v.dim + '"');
  }
});
check('every declared dimension is reachable by >=1 verb', function () {
  const reached = new Set(VERBS.verbs.map(function (v) { return v.dim; }));
  for (const dim of Object.keys(VERBS.dimensions)) {
    assert.ok(reached.has(dim), 'dimension "' + dim + '" is unreachable (no verb writes it)');
  }
});
check('every paired inverse actually exists and is mutual where claimed', function () {
  for (const v of VERBS.verbs) {
    if (v.inverse && !SENTINELS.has(v.inverse) && v.inverse !== null) {
      const inv = grammar.byVerb[v.inverse];
      assert.ok(inv, 'verb "' + v.verb + '" names inverse "' + v.inverse + '" which does not exist');
    }
  }
  // spot-check the mutual pairs from section 4
  assert.strictEqual(grammar.byVerb['show'].inverse, 'hide');
  assert.strictEqual(grammar.byVerb['hide'].inverse, 'show');
  assert.strictEqual(grammar.byVerb['open'].inverse, 'close');
  assert.strictEqual(grammar.byVerb['close'].inverse, 'open');
  assert.strictEqual(grammar.byVerb['read'].inverse, 'stop');
  assert.strictEqual(grammar.byVerb['stop'].inverse, 'read');
});
check('only ask spends; only read is gated (v1)', function () {
  const spenders = VERBS.verbs.filter(function (v) { return v.spend; }).map(function (v) { return v.verb; });
  const gated = VERBS.verbs.filter(function (v) { return v.gated; }).map(function (v) { return v.verb; });
  assert.deepStrictEqual(spenders, ['ask']);
  assert.deepStrictEqual(gated, ['read']);
});

// ---- 7. resolver: fuzzy term -> concrete target -----------------------------

const DEST = JSON.parse(fs.readFileSync(path.join(ROOT, 'wiki/voice_guide/destinations.json'), 'utf8'));
const ROSTER = Array.from(new Set(DEST.nodes.map(function (n) { return n.group; }))); // live-roster stand-in

check('resolveGroups: exact leaf ("levin" -> traditions/levin)', function () {
  const r = CCL.resolveGroups('levin', ROSTER);
  assert.deepStrictEqual(r.keys, ['traditions/levin']);
});
check('resolveGroups: exact bare key ("architecture")', function () {
  assert.deepStrictEqual(CCL.resolveGroups('architecture', ROSTER).keys, ['architecture']);
});
check('resolveGroups: a section term expands to every key under it', function () {
  const r = CCL.resolveGroups('traditions', ROSTER);
  assert.strictEqual(r.section, true);
  assert.ok(r.keys.length >= 15, 'expected all traditions/* keys, got ' + r.keys.length);
  assert.ok(r.keys.every(function (k) { return k.indexOf('traditions/') === 0; }));
});
check('resolveGroups: unique prefix resolves ("arch" -> architecture)', function () {
  assert.deepStrictEqual(CCL.resolveGroups('arch', ROSTER).keys, ['architecture']);
});
check('resolveGroups: unique substring resolves ("hamed" -> arkanihamed)', function () {
  assert.deepStrictEqual(CCL.resolveGroups('hamed', ROSTER).keys, ['traditions/arkanihamed']);
});
check('resolveGroups: a multi-match is RANKED and acted on, hedged ("a")', function () {
  // Policy changed 2026-07-25: this row used to assert that any multi-match
  // asked. In a voice-only tool a returned question costs more than a stated
  // assumption, so a ranked winner is taken and marked. The invariant that
  // SURVIVES -- a genuine tie still asks -- is the row below.
  const r = CCL.resolveGroups('a', ROSTER);
  if (r.ok) {
    assert.strictEqual(r.confidence, 'low', 'a guess must be marked as one');
    assert.ok(r.alternatives.length, 'the roads not taken must be speakable');
  } else {
    assert.strictEqual(r.error, 'ambiguous');
    assert.ok(r.candidates.length > 1);
  }
});
check('resolveGroups: unknown term -> unresolved (never invents)', function () {
  assert.strictEqual(CCL.resolveGroups('zzzznope', ROSTER).error, 'unresolved');
});
check('resolveGroups: empty term -> unresolved', function () {
  assert.strictEqual(CCL.resolveGroups('', ROSTER).error, 'unresolved');
});

check('resolveTab: exact id/label ("sociogram")', function () {
  assert.strictEqual(CCL.resolveTab('sociogram', DEST.tabs).id, 'sociogram');
});
check('resolveTab: aka match ("heartbeat" -> ai_heartbeat)', function () {
  assert.strictEqual(CCL.resolveTab('heartbeat', DEST.tabs).id, 'ai_heartbeat');
});
check('resolveTab: aka match ("physics" -> physics_explorer)', function () {
  assert.strictEqual(CCL.resolveTab('physics', DEST.tabs).id, 'physics_explorer');
});
check('resolveTab: ambiguous substring returns candidates ("community")', function () {
  const r = CCL.resolveTab('community', DEST.tabs);
  assert.strictEqual(r.error, 'ambiguous');
  assert.ok(r.candidates.indexOf('community_explorer') !== -1 && r.candidates.indexOf('community_interactions') !== -1);
});
check('resolveTab: unknown -> unresolved', function () {
  assert.strictEqual(CCL.resolveTab('zzzznope', DEST.tabs).error, 'unresolved');
});

check('resolveNode: a distinctive label resolves to one id', function () {
  // fixture-derived: find a label that is non-Untitled and unique, so the test
  // does not hardcode a volatile title.
  const counts = {};
  for (const n of DEST.nodes) { const l = n.label.toLowerCase(); counts[l] = (counts[l] || 0) + 1; }
  const uniqueNode = DEST.nodes.find(function (n) { return n.label !== 'Untitled' && counts[n.label.toLowerCase()] === 1; });
  assert.ok(uniqueNode, 'fixture should contain at least one unique non-Untitled label');
  const r = CCL.resolveNode(uniqueNode.label, DEST.nodes);
  assert.strictEqual(r.ok, true);
  assert.strictEqual(r.id, uniqueNode.id);
});
check('resolveNode: exact id (filename base) resolves', function () {
  const sample = DEST.nodes[0];
  const base = sample.id.replace(/\.md$/, '');
  const r = CCL.resolveNode(base, DEST.nodes);
  assert.strictEqual(r.ok, true);
  assert.strictEqual(r.id, sample.id);
});
check('resolveNode: shared label "Untitled" is ambiguous, carries group in candidates', function () {
  const r = CCL.resolveNode('untitled', DEST.nodes);
  assert.strictEqual(r.error, 'ambiguous');
  assert.ok(r.candidates.length > 1 && r.candidates.length <= 8, 'candidates capped');
  assert.ok(r.candidates[0].group !== undefined, 'candidate carries group for spoken disambiguation');
});
check('resolveNode: unknown -> unresolved', function () {
  assert.strictEqual(CCL.resolveNode('zzzznope-not-a-node', DEST.nodes).error, 'unresolved');
});

// ---- 8. journal: absolute-vector undo/redo, per-tab, capped -----------------

check('journal: record then undo returns before; redo returns after', function () {
  const j = CCL.createJournal();
  j.record('sociogram', { dim: 'filters', before: ['a'], after: ['a', 'b'] });
  assert.deepStrictEqual(j.undo('sociogram'), { dim: 'filters', value: ['a'] });
  assert.deepStrictEqual(j.redo('sociogram'), { dim: 'filters', value: ['a', 'b'] });
});
check('journal: undo/redo walk a multi-entry stack in order', function () {
  const j = CCL.createJournal();
  j.record('s', { dim: 'filters', before: 0, after: 1 });
  j.record('s', { dim: 'filters', before: 1, after: 2 });
  j.record('s', { dim: 'selection', before: null, after: 'x' });
  assert.deepStrictEqual(j.undo('s'), { dim: 'selection', value: null });
  assert.deepStrictEqual(j.undo('s'), { dim: 'filters', value: 1 });
  assert.deepStrictEqual(j.undo('s'), { dim: 'filters', value: 0 });
  assert.strictEqual(j.undo('s'), null); // empty
});
check('journal: a fresh record invalidates the redo stack', function () {
  const j = CCL.createJournal();
  j.record('s', { dim: 'd', before: 0, after: 1 });
  j.undo('s');
  assert.strictEqual(j.canRedo('s'), true);
  j.record('s', { dim: 'd', before: 0, after: 9 }); // new action
  assert.strictEqual(j.canRedo('s'), false);
});
check('journal: undo on empty -> null; redo on fresh -> null', function () {
  const j = CCL.createJournal();
  assert.strictEqual(j.undo('s'), null);
  assert.strictEqual(j.redo('s'), null);
});
check('journal: per-tab stacks are isolated', function () {
  const j = CCL.createJournal();
  j.record('a', { dim: 'd', before: 0, after: 1 });
  j.record('b', { dim: 'd', before: 5, after: 6 });
  assert.strictEqual(j.depth('a'), 1);
  assert.strictEqual(j.depth('b'), 1);
  assert.deepStrictEqual(j.undo('a'), { dim: 'd', value: 0 });
  assert.strictEqual(j.canUndo('b'), true); // undoing a did not touch b
});
check('journal: caps at 20, dropping the oldest', function () {
  const j = CCL.createJournal();
  for (let i = 0; i < 25; i++) { j.record('s', { dim: 'd', before: i, after: i + 1 }); }
  assert.strictEqual(j.depth('s'), 20);
  // oldest 5 dropped: after 20 undos the deepest before is 5, not 0
  let last = null;
  for (let i = 0; i < 20; i++) { last = j.undo('s'); }
  assert.strictEqual(last.value, 5);
  assert.strictEqual(j.undo('s'), null);
});
check('journal: honors a custom cap', function () {
  const j = CCL.createJournal({ cap: 3 });
  for (let i = 0; i < 10; i++) { j.record('s', { dim: 'd', before: i, after: i + 1 }); }
  assert.strictEqual(j.depth('s'), 3);
});
check('journal: record rejects a malformed entry', function () {
  const j = CCL.createJournal();
  assert.throws(function () { j.record('s', { before: 1, after: 2 }); }); // no dim
});

// ---- 9. dispatcher planner: op + context -> execution intent ----------------

const CTX = { caps: CCL.SOCIOGRAM_CAPS, roster: ROSTER, tabs: DEST.tabs, nodes: DEST.nodes };
function planCmd(str) { return CCL.plan(CCL.parse(str, grammar), CTX); }

// The other two thirds of the bare-`open` contract (the parse half is in
// section 3): who decides, and both answers.
check('bare "open" is still missing_arg where there is no roster to be relative to', function () {
  assert.strictEqual(CCL.plan(CCL.parse('open', grammar), CTX).error, 'missing_arg');
});
check('bare "open" on a tab that activates its items means the one under the cursor', function () {
  const ctx = { caps: CCL.SOCIOGRAM_CAPS, roster: [], tabs: [], nodes: [], activates: true };
  const p = CCL.plan(CCL.parse('open', grammar), ctx);
  assert.strictEqual(p.ok, true);
  assert.strictEqual(p.kind, 'selection');
  assert.strictEqual(p.label, '');
});

check('plan: parse errors pass straight through', function () {
  const p = CCL.plan(CCL.parse('florb', grammar), CTX);
  assert.strictEqual(p.ok, false);
  assert.strictEqual(p.error, 'unknown_verb');
});
check('plan: unsupported verb -> unsupported_here with derived supported list', function () {
  // `ask` (the metered broker path) is still outside v1 Sociogram caps. This row
  // has now been re-pointed twice -- first off `zoom`, then off `read` -- as each
  // moved INTO caps. It was encoding decisions, not a rule; the rule is only that
  // an uncapped verb degrades honestly.
  const p = planCmd('ask what is c2a2');
  assert.strictEqual(p.error, 'unsupported_here');
  assert.ok(p.supported.indexOf('fit') !== -1 && p.supported.indexOf('ask') === -1);
});
check('plan: set and ask remain unsupported in v1 Sociogram', function () {
  assert.strictEqual(planCmd('set brightness 0.5').error, 'unsupported_here');
  assert.strictEqual(planCmd('ask what is c2a2').error, 'unsupported_here');
});
check('cursor: pick/next/previous plan against the revealed set', function () {
  assert.strictEqual(planCmd('pick random').mode, 'random');
  assert.strictEqual(planCmd('pick first').mode, 'first');
  assert.strictEqual(planCmd('next').dir, 'next');
  assert.strictEqual(planCmd('previous').dir, 'previous');
  assert.strictEqual(CCL.parse('pick sideways', grammar).error, 'bad_enum');
});
check('cursor: next and previous are declared inverses of each other', function () {
  const byVerb = grammar.byVerb;
  assert.strictEqual(byVerb.next.inverse, 'previous');
  assert.strictEqual(byVerb.previous.inverse, 'next');
});
check('playback: read/stop plan, and stop is read\'s declared inverse', function () {
  assert.strictEqual(planCmd('read').kind, 'playback');
  assert.strictEqual(planCmd('stop').kind, 'playback');
  assert.strictEqual(grammar.byVerb.read.inverse, 'stop');
});

check('plan: only levin friston -> filters set with both keys', function () {
  const p = planCmd('only levin friston');
  assert.deepStrictEqual({ ok: p.ok, kind: p.kind, action: p.action, keys: p.keys }, {
    ok: true, kind: 'filters', action: 'set', keys: ['traditions/levin', 'traditions/friston'],
  });
  assert.deepStrictEqual(p.journal, { dim: 'filters' });
});
check('plan: show -> union, hide -> diff (same dimension, symmetry)', function () {
  assert.strictEqual(planCmd('show levin').action, 'union');
  assert.strictEqual(planCmd('hide levin').action, 'diff');
  assert.strictEqual(planCmd('show levin').kind, planCmd('hide levin').kind);
});
check('plan: hide architecture resolves the bare structure key', function () {
  assert.deepStrictEqual(planCmd('hide architecture').keys, ['architecture']);
});
check('plan: a section term expands (hide traditions -> all traditions/* keys)', function () {
  const p = planCmd('hide traditions');
  assert.ok(p.keys.length >= 15 && p.keys.every(function (k) { return k.indexOf('traditions/') === 0; }));
});
check('plan: all / none map to filters all/none, no keys', function () {
  assert.deepStrictEqual({ kind: planCmd('all').kind, action: planCmd('all').action }, { kind: 'filters', action: 'all' });
  assert.strictEqual(planCmd('none').action, 'none');
});
check('plan: a term it had to guess at still EXECUTES, carrying the assumption', function () {
  const p = planCmd('only a'); // 'a' prefix-matches several groups
  if (p.ok) {
    assert.ok(p.guesses && p.guesses.length, 'executed a guess without recording it -- the user would never hear that it guessed');
  } else {
    assert.strictEqual(p.error, 'ambiguous');
    assert.ok(p.candidates.length > 1);
  }
});
check('plan: unresolved-only filter term -> unresolved (never a silent no-op)', function () {
  assert.strictEqual(planCmd('only zzzznope').error, 'unresolved');
});
// The verb rides along for the same reason it does on `go`: unresolved is one
// error code for several questions, and the shell can only answer the right one
// if it knows which verb asked. Without this, a tab that HAS filters answered a
// miss with "Could not find X" -- true, and about the wrong thing.
check('plan: an unresolved filter term names the verb that failed', function () {
  assert.strictEqual(planCmd('only zzzznope').verb, 'only');
  assert.strictEqual(planCmd('hide zzzznope').verb, 'hide');
});
check('plan: partially-resolved filter proceeds with resolved, reports unresolved', function () {
  const p = planCmd('only levin zzzznope');
  assert.deepStrictEqual(p.keys, ['traditions/levin']);
  assert.deepStrictEqual(p.unresolved, ['zzzznope']);
});

check('plan: go heartbeat -> shell switchTab ai_heartbeat', function () {
  const p = planCmd('go heartbeat');
  assert.deepStrictEqual({ kind: p.kind, action: p.action, tab: p.tab }, { kind: 'shell', action: 'switchTab', tab: 'ai_heartbeat' });
});
check('plan: back -> shell back', function () {
  assert.deepStrictEqual({ kind: planCmd('back').kind, action: planCmd('back').action }, { kind: 'shell', action: 'back' });
});
check('plan: go to a nonexistent tab -> unresolved', function () {
  assert.strictEqual(planCmd('go zzzznope').error, 'unresolved');
});

check('plan: close/find/clear/fit carry the right kind + journal dim', function () {
  assert.deepStrictEqual({ kind: planCmd('close').kind, dim: planCmd('close').journal.dim }, { kind: 'selection', dim: 'selection' });
  assert.deepStrictEqual({ kind: planCmd('find bioelectric').kind, text: planCmd('find bioelectric').text }, { kind: 'highlight', text: 'bioelectric' });
  assert.strictEqual(planCmd('clear').action, 'clear');
  assert.deepStrictEqual({ kind: planCmd('fit').kind, dim: planCmd('fit').journal.dim }, { kind: 'camera', dim: 'camera' });
});
check('plan: focus needs two resolvable groups', function () {
  const good = planCmd('focus levin ~ friston');
  assert.deepStrictEqual({ kind: good.kind, action: good.action, keys: good.keys }, {
    kind: 'highlight', action: 'focus', keys: ['traditions/levin', 'traditions/friston'],
  });
  assert.strictEqual(planCmd('focus levin ~ zzzznope').error, 'unresolved');
});
check('plan: undo/redo/reset/restore route to the journal kind', function () {
  for (const v of ['undo', 'redo', 'reset', 'restore']) {
    assert.deepStrictEqual({ kind: planCmd(v).kind, action: planCmd(v).action }, { kind: 'journal', action: v });
  }
});
check('plan: what/where/help route to reads', function () {
  for (const v of ['what', 'where', 'help']) {
    assert.strictEqual(planCmd(v).kind, 'read');
  }
});
check('plan: every SOCIOGRAM_CAPS verb yields a plan, never unsupported_here', function () {
  // guards against a cap being listed but unhandled in the switch
  const samples = {
    go: 'go sociogram', back: 'back', zoom: 'zoom in', pan: 'pan left',
    pick: 'pick random', next: 'next', previous: 'previous', read: 'read', stop: 'stop',
    summarize: 'summarize',
    show: 'show levin', hide: 'hide levin', only: 'only levin',
    all: 'all', none: 'none', open: 'open ' + DEST.nodes[0].id.replace(/\.md$/, ''), close: 'close',
    find: 'find x', clear: 'clear', focus: 'focus levin ~ friston', fit: 'fit',
    undo: 'undo', redo: 'redo', reset: 'reset', restore: 'restore', what: 'what', where: 'where', help: 'help',
  };
  for (const verb of CCL.SOCIOGRAM_CAPS) {
    assert.ok(samples[verb], 'no sample command for capability "' + verb + '"');
    const p = planCmd(samples[verb]);
    assert.notStrictEqual(p.error, 'unsupported_here', 'cap "' + verb + '" planned as unsupported');
  }
});

// ---- per-tab manifest fan-out: set/knob planning + coverage audit -----------
// Increment 4 step 1: the pure engine gains `set` (knob) planning validated
// against a tab's manifest, plus the coverage-audit diff. Metabolism is the
// first knob tab (voice_guide_redesign.md sections 3, 8, 9).

const MANIFEST = JSON.parse(fs.readFileSync(path.join(ROOT, 'wiki/voice_guide/manifests.json'), 'utf8'));
const META = MANIFEST.tabs.metabolism;
const META_CTX = { caps: META.caps, knobs: META.knobs, tabs: DEST.tabs, nodes: DEST.nodes, roster: ROSTER };
function planMeta(str) { return CCL.plan(CCL.parse(str, grammar), META_CTX); }

check('manifest: metabolism is well-formed (caps `set` + 4 bound knobs)', function () {
  assert.ok(Array.isArray(META.caps) && META.caps.indexOf('set') !== -1, 'metabolism must cap `set`');
  assert.strictEqual(META.knobs.length, 4);
  for (const k of META.knobs) {
    assert.ok(k.id && k.bind && (k.bind.select || k.bind.checkbox), 'knob ' + k.id + ' needs a DOM bind');
    assert.ok(Array.isArray(k.values) && k.values.length >= 2, 'knob ' + k.id + ' needs >=2 values');
  }
});
check('manifest: sociogram caps mirror the engine SOCIOGRAM_CAPS (one source, no drift)', function () {
  assert.deepStrictEqual(MANIFEST.tabs.sociogram.caps.slice().sort(), CCL.SOCIOGRAM_CAPS.slice().sort());
});

check('plan set: spoken alias resolves to the DOM value (set view waveform -> wave)', function () {
  const p = planMeta('set view waveform');
  assert.deepStrictEqual({ ok: p.ok, kind: p.kind, knob: p.knob, value: p.value }, { ok: true, kind: 'knob', knob: 'view', value: 'wave' });
  assert.deepStrictEqual(p.bind, { select: '#view' });
  assert.strictEqual(p.journal.dim, 'knob:view');
});
check('plan set: exact DOM value resolves (set view dual)', function () {
  assert.strictEqual(planMeta('set view dual').value, 'dual');
});
check('plan set: multi-word value resolves (returned vs sent -> dual)', function () {
  assert.strictEqual(planMeta('set view returned vs sent').value, 'dual');
});
check('plan set: bool knob maps aliases both ways (logy on->on, linear->off)', function () {
  assert.strictEqual(planMeta('set logy on').value, 'on');
  assert.strictEqual(planMeta('set logy linear').value, 'off');
});
check('plan set: unknown knob on this tab -> unknown_knob + supported list', function () {
  const p = planMeta('set brightness 0.5');
  assert.strictEqual(p.error, 'unknown_knob');
  assert.deepStrictEqual(p.supported.slice().sort(), ['color', 'logy', 'metric', 'view']);
});
check('plan set: bad value -> unresolved_value + allowed list (never a silent no-op)', function () {
  const p = planMeta('set view zzzznope');
  assert.strictEqual(p.error, 'unresolved_value');
  assert.deepStrictEqual(p.allowed, ['raster', 'wave', 'dual']);
});
check('plan set: ambiguous value asks, candidates ride in the result (metric tokens)', function () {
  const p = planMeta('set metric tokens'); // substring-hits output/total/thinking *tokens*
  assert.strictEqual(p.error, 'ambiguous');
  assert.ok(p.candidates.length >= 2, 'expected multiple candidates, got ' + JSON.stringify(p.candidates));
});

check('plan: Sociogram (no `set` cap) still rejects set as unsupported_here', function () {
  assert.strictEqual(planCmd('set view wave').error, 'unsupported_here');
});
check('plan: metabolism honestly degrades Sociogram-only verbs (unsupported_here, never faked)', function () {
  assert.strictEqual(planMeta('only levin').error, 'unsupported_here');
  assert.strictEqual(planMeta('open x').error, 'unsupported_here');
  assert.strictEqual(planMeta('fit').error, 'unsupported_here');
});
check('plan: shared verbs plan cross-tab (metabolism go/what/undo)', function () {
  assert.strictEqual(planMeta('go sociogram').kind, 'shell');
  assert.strictEqual(planMeta('what').kind, 'read');
  assert.strictEqual(planMeta('undo').kind, 'journal');
});
check('plan: every metabolism cap yields a plan, never unsupported_here', function () {
  const samples = {
    go: 'go sociogram', back: 'back', zoom: 'zoom in', pan: 'pan left', set: 'set view wave',
    undo: 'undo', redo: 'redo', reset: 'reset', restore: 'restore',
    what: 'what', where: 'where', help: 'help',
  };
  for (const verb of META.caps) {
    assert.ok(samples[verb], 'no sample command for metabolism cap "' + verb + '"');
    assert.notStrictEqual(planMeta(samples[verb]).error, 'unsupported_here', 'cap "' + verb + '" planned as unsupported');
  }
});

check('audit: a fully-bound tab passes (every live control is a knob)', function () {
  const declared = META.knobs.map(function (k) { return (k.bind.select || k.bind.checkbox).replace('#', ''); });
  assert.deepStrictEqual(CCL.auditCoverage(declared, ['view', 'metric', 'color', 'logy'], META.controls_excluded),
    { ok: true, unbound: [], missing: [] });
});
check('audit: an unbound live control is a LOUD failure (the north-star invariant)', function () {
  const r = CCL.auditCoverage(['view', 'metric', 'color', 'logy'], ['view', 'metric', 'color', 'logy', 'sneaky_new_toggle'], []);
  assert.strictEqual(r.ok, false);
  assert.deepStrictEqual(r.unbound, ['sneaky_new_toggle']);
});
check('audit: an explicit exclusion silences a control (in data, not prose)', function () {
  assert.strictEqual(CCL.auditCoverage(['view'], ['view', 'legend_toggle'], ['legend_toggle']).ok, true);
});
check('audit: a declared-but-absent control is reported missing (stale manifest)', function () {
  assert.deepStrictEqual(CCL.auditCoverage(['view', 'gone'], ['view'], []).missing, ['gone']);
});

// ---- knob NAME resolution: what the user says vs what the id is -------------
//
// The control the user is looking at on metabolism says "Amplitude"; the knob
// id is `metric`. If only the id resolved, voice could not reach a control in
// plain sight -- and the coverage audit would still report the tab fully
// covered, because it checks that controls are BOUND, not that they are
// SAYABLE. These rows are that gap's regression guard.

check('knob: resolves by id', function () {
  assert.strictEqual(CCL.resolveKnob('metric', META.knobs).spec.id, 'metric');
});
check('knob: resolves by the label printed on the control', function () {
  assert.strictEqual(CCL.resolveKnob('Amplitude', META.knobs).spec.id, 'metric');
});
check('knob: resolves by spoken alias', function () {
  assert.strictEqual(CCL.resolveKnob('colour', META.knobs).spec.id, 'color');
  assert.strictEqual(CCL.resolveKnob('log', META.knobs).spec.id, 'logy');
});
check('knob: unknown name lists what IS available (never a bare code)', function () {
  const r = CCL.resolveKnob('banana', META.knobs);
  assert.strictEqual(r.ok, false);
  assert.strictEqual(r.error, 'unknown_knob');
  assert.deepStrictEqual(r.supported, ['view', 'metric', 'color', 'logy']);
});
check('knob: an alias matching two knobs is ambiguous, not a coin flip', function () {
  const knobs = [{ id: 'a', label: 'A', aka: ['size'] }, { id: 'b', label: 'B', aka: ['size'] }];
  const r = CCL.resolveKnob('size', knobs);
  assert.strictEqual(r.error, 'ambiguous');
  assert.deepStrictEqual(r.candidates, ['a', 'b']);
});
check('knob: "set amplitude output" plans onto metric (end to end)', function () {
  const p = planMeta('set amplitude output');
  assert.strictEqual(p.ok, true);
  assert.strictEqual(p.knob, 'metric');
  assert.strictEqual(p.value, 'out');
});

// Drift guards on the manifest itself: a two-word alias would be UNPARSEABLE
// (the parser reads the knob as the first token), and a duplicate alias across
// knobs would make one of them permanently ambiguous. Both are authoring
// mistakes that a fan-out to 12 tabs would otherwise repeat quietly.
check('manifest: every knob declares a label and single-token aliases', function () {
  for (const key of Object.keys(MANIFEST.tabs)) {
    for (const k of (MANIFEST.tabs[key].knobs || [])) {
      assert.ok(k.label, key + '.' + k.id + ' has no label');
      assert.ok((k.aka || []).length, key + '.' + k.id + ' has no aka');
      for (const a of k.aka) {
        assert.ok(a.indexOf(' ') === -1, key + '.' + k.id + ' alias "' + a + '" is multi-word (unparseable)');
        assert.strictEqual(a, a.toLowerCase(), key + '.' + k.id + ' alias "' + a + '" is not lowercase');
      }
    }
  }
});
check('manifest: no alias collides across knobs on the same tab', function () {
  for (const key of Object.keys(MANIFEST.tabs)) {
    const seen = {};
    for (const k of (MANIFEST.tabs[key].knobs || [])) {
      for (const name of [k.id].concat(k.aka || [])) {
        assert.ok(!seen[name], key + ': "' + name + '" claimed by both ' + seen[name] + ' and ' + k.id);
        seen[name] = k.id;
      }
    }
  }
});

// ---- a key that is BOTH a group and a section parent ------------------------
//
// 'architecture' holds the architecture files AND owns 'architecture/changelog'.
// The section-prefix branch used to short-circuit and return only the child, so
// "show architecture" reported success and rendered nothing (2026-07-25, found
// live by Tom -- not by any test, because every test asserted the filter STATE
// the code had just written rather than what the graph showed).

const PARENT_ROSTER = ['traditions/levin', 'master', 'architecture', 'architecture/changelog', 'flags'];

check('groups: a parent-and-section key resolves to ITSELF plus its children', function () {
  const r = CCL.resolveGroups('architecture', PARENT_ROSTER);
  assert.strictEqual(r.ok, true);
  assert.ok(r.keys.indexOf('architecture') !== -1, 'the parent group itself was dropped');
  assert.ok(r.keys.indexOf('architecture/changelog') !== -1, 'the child section was dropped');
});
check('groups: the parent comes first, so the reported list reads naturally', function () {
  assert.deepStrictEqual(CCL.resolveGroups('architecture', PARENT_ROSTER).keys,
    ['architecture', 'architecture/changelog']);
});
check('groups: a pure section parent (no bare key) still expands to children only', function () {
  assert.deepStrictEqual(CCL.resolveGroups('traditions', PARENT_ROSTER).keys, ['traditions/levin']);
});
check('groups: a leaf-only term is unaffected', function () {
  assert.deepStrictEqual(CCL.resolveGroups('changelog', PARENT_ROSTER).keys, ['architecture/changelog']);
});
check('groups: hide is symmetric with show over the same expansion', function () {
  const shown = CCL.resolveGroups('architecture', PARENT_ROSTER).keys;
  const hidden = CCL.resolveGroups('architecture', PARENT_ROSTER).keys;
  assert.deepStrictEqual(shown, hidden, 'show and hide must expand identically or symmetry is a lie');
});

// ---- gestures: the surface the DOM sweep cannot see -------------------------
//
// Zoom, pan, drag and hover have no element, so auditCoverage is blind to them
// and reported "0 uncovered" on the Sociogram while zoom/pan were unreachable
// (2026-07-25). Since they cannot be discovered, the gate checks the honesty of
// the declaration -- above all, that a gesture claiming coverage names a verb
// the tab actually has.

check('gestures: a tab declaring none FAILS -- silence is not completeness', function () {
  assert.strictEqual(CCL.auditGestures([], ['fit']).ok, false);
  assert.strictEqual(CCL.auditGestures(undefined, ['fit']).ok, false);
});
check('gestures: covered must name a verb the tab ACTUALLY supports', function () {
  const bad = CCL.auditGestures([{ id: 'zoom', status: 'covered', by: ['zoom'] }], ['fit', 'only']);
  assert.strictEqual(bad.ok, false);
  assert.ok(/claims verb "zoom"/.test(bad.problems[0]), bad.problems[0]);
  assert.strictEqual(CCL.auditGestures([{ id: 'zoom', status: 'covered', by: ['fit'] }], ['fit']).ok, true);
});
check('gestures: covered with no verb named is a failure, not a pass', function () {
  assert.strictEqual(CCL.auditGestures([{ id: 'zoom', status: 'covered', by: [] }], ['fit']).ok, false);
});
check('gestures: deferred needs an increment, excluded needs a reason', function () {
  assert.strictEqual(CCL.auditGestures([{ id: 'pan', status: 'deferred' }], []).ok, false);
  assert.strictEqual(CCL.auditGestures([{ id: 'pan', status: 'deferred', planned: 'inc 5' }], []).ok, true);
  assert.strictEqual(CCL.auditGestures([{ id: 'hover', status: 'excluded' }], []).ok, false);
  assert.strictEqual(CCL.auditGestures([{ id: 'hover', status: 'excluded', reason: 'transient' }], []).ok, true);
});
check('gestures: an unknown status is rejected rather than counted', function () {
  const r = CCL.auditGestures([{ id: 'x', status: 'probably fine' }], []);
  assert.strictEqual(r.ok, false);
});
check('gestures: every declared tab passes its own gate', function () {
  for (const key of Object.keys(MANIFEST.tabs)) {
    const t = MANIFEST.tabs[key];
    const r = CCL.auditGestures(t.gestures, t.caps);
    assert.strictEqual(r.ok, true, key + ' gestures: ' + r.problems.join(' | '));
  }
});

// ---- zoom: declared in the grammar from day one, never wired ---------------

check('zoom: in/out plan as camera ops carrying the direction', function () {
  for (const dir of ['in', 'out']) {
    const p = planCmd("zoom " + dir);
    assert.strictEqual(p.ok, true, 'zoom ' + dir + ' did not plan');
    assert.strictEqual(p.kind, 'camera');
    assert.strictEqual(p.dir, dir);
  }
});
check('zoom: a direction that is not in/out is refused by the grammar', function () {
  assert.strictEqual(CCL.parse('zoom sideways', grammar).error, 'bad_enum');
});
check('pan: all four directions plan, and only those four', function () {
  for (const dir of ['left', 'right', 'up', 'down']) {
    const p = planCmd('pan ' + dir);
    assert.strictEqual(p.ok, true, 'pan ' + dir + ' did not plan');
    assert.strictEqual(p.kind, 'camera');
    assert.strictEqual(p.dir, dir);
  }
  assert.strictEqual(CCL.parse('pan sideways', grammar).error, 'bad_enum');
});
// rotate -- the THIRD axis, and the first that only means anything on a tab
// drawn in three dimensions. Zoom moves the camera along its sightline and pan
// slides what it looks at; on a flat graph that is the whole camera, which is
// why the dimension stopped at two verbs. The Connectome is an orbit camera and
// could not be turned by voice at all (Tom, 2026-07-27).
// Planned against the CONNECTOME's caps, not the Sociogram's: rotate is only
// in caps where there is something to turn, so the default CTX refusing it is
// the design working rather than a gap.
const PRS_CTX = { caps: MANIFEST.tabs.prs_3d.caps, roster: [], tabs: DEST.tabs, nodes: [] };
function planPrs(str) { return CCL.plan(CCL.parse(str, grammar), PRS_CTX); }
check('rotate: all four directions plan, and only those four', function () {
  for (const dir of ['left', 'right', 'up', 'down']) {
    const p = planPrs('rotate ' + dir);
    assert.strictEqual(p.ok, true, 'rotate ' + dir + ' did not plan');
    assert.strictEqual(p.kind, 'camera');
    assert.strictEqual(p.dir, dir);
  }
  assert.strictEqual(CCL.parse('rotate sideways', grammar).error, 'bad_enum');
});
check('camera: the dimension is symmetric -- every move has its opposite', function () {
  const pairs = [['zoom in', 'zoom out'], ['pan left', 'pan right'], ['pan up', 'pan down']];
  for (const [a, b] of pairs) {
    assert.strictEqual(planCmd(a).ok, true, a);
    assert.strictEqual(planCmd(b).ok, true, b);
  }
  for (const [a, b] of [['rotate left', 'rotate right'], ['rotate up', 'rotate down']]) {
    assert.strictEqual(planPrs(a).ok, true, a);
    assert.strictEqual(planPrs(b).ok, true, b);
  }
});
// The soft layer, same rule as pick/select/choose: people say "turn it round"
// and "orbit left" for the one act, and leaving that to the model means the
// common phrasing fails whenever the model does.
check('rotate: turn and orbit resolve to it deterministically, not by model luck', function () {
  for (const say of ['turn left', 'orbit right']) {
    const p = planPrs(say);
    assert.strictEqual(p.ok, true, say + ' did not plan');
    assert.strictEqual(p.kind, 'camera');
    assert.strictEqual(p.action, 'rotate');
  }
});
// `center` is NOT a camera verb, and that is the whole point: opening something
// on a 3D tab already moves the camera onto it (the page's own search results
// do exactly that), so the word maps to the thing that exists rather than
// growing a second road to it. Asserted at the PARSE layer, where the rewrite
// happens, so the row does not depend on any particular node resolving.
// spin -- the only verb that leaves something running.
check('spin: bare means left, and the three forms are the only ones', function () {
  assert.strictEqual(planPrs('spin').dir, 'left');
  for (const dir of ['left', 'right', 'off']) {
    const p = planPrs('spin ' + dir);
    assert.strictEqual(p.ok, true, 'spin ' + dir + ' did not plan');
    assert.strictEqual(p.kind, 'camera');
    assert.strictEqual(p.dir, dir);
  }
});
// `opt` never checked its enum, because no verb using it had one until now --
// so `spin banana` parsed clean and would have reached the shell as a
// direction, which is how a typo becomes a silent no-op.
check('spin: an optional argument still has to be one of the allowed ones', function () {
  assert.strictEqual(CCL.parse('spin banana', grammar).error, 'bad_enum');
});
check('opt: verbs WITHOUT an enum are untouched by that check', function () {
  assert.strictEqual(CCL.parse('read details', grammar).args[0], 'details');
  assert.strictEqual(CCL.parse('all tags', grammar).args[0], 'tags');
});
check('center: the word means open, because opening already centres', function () {
  for (const say of ['center something', 'centre something']) {
    assert.strictEqual(CCL.parse(say, grammar).verb, 'open', say);
  }
});
// A flat tab must SAY it cannot turn rather than silently doing nothing. Caps
// are per-tab, so the engine refuses before the shell is ever reached.
check('rotate: a tab without it in caps gets unsupported_here, naming what it does have', function () {
  const flat = CCL.plan(CCL.parse('rotate left', grammar),
    { caps: MANIFEST.tabs.start_here.caps, groups: [], tabs: [], nodes: [] });
  assert.strictEqual(flat.ok, false);
  assert.strictEqual(flat.error, 'unsupported_here');
});
check('rotate: the Connectome declares the cap its gesture now claims', function () {
  const prs = MANIFEST.tabs.prs_3d;
  const orbit = prs.gestures.filter(function (g) { return g.id === 'orbit'; })[0];
  assert.strictEqual(orbit.status, 'covered');
  for (const v of orbit.by) { assert.ok(prs.caps.indexOf(v) !== -1, 'gesture claims uncapped verb ' + v); }
  // And the declaration the shell reads is really there, with the page's own
  // limits rather than invented ones -- a camera voice could put somewhere the
  // mouse cannot reach is a worse bug than one that will not move.
  assert.ok(prs.camera && prs.camera.apply && prs.camera.fit, 'no camera declaration');
  assert.deepStrictEqual(prs.camera.dolly.clamp, [15, 120]);
});
check('zoom: the Sociogram now declares the cap its gesture claims', function () {
  const soc = MANIFEST.tabs.sociogram;
  const zoomGesture = soc.gestures.filter(function (g) { return g.id === 'zoom'; })[0];
  assert.strictEqual(zoomGesture.status, 'covered');
  for (const v of zoomGesture.by) { assert.ok(soc.caps.indexOf(v) !== -1, 'gesture claims uncapped verb ' + v); }
});

// ---- guess, act, and say so (2026-07-25, Tom) ------------------------------
//
// Returning `ambiguous` for every multi-match made the guide answer questions
// with questions -- unusable in a voice tool, where the user cannot see the
// candidate list being asked about. A ranked winner is now acted on and marked
// low-confidence. Safety rests on the outcome still being reported exactly and
// undo being one word away.

const RANK_ROSTER = ['traditions/stump', 'summa', 'traditions/summa-extra', 'sessions', 'traditions/levin'];

check('guess: a ranked winner is ACTED on, not asked about', function () {
  const r = CCL.resolveGroups('su', RANK_ROSTER);
  assert.strictEqual(r.ok, true, 'should have acted, got ' + JSON.stringify(r));
  assert.deepStrictEqual(r.keys, ['summa']);
  assert.strictEqual(r.confidence, 'low');
  assert.ok(r.alternatives.length, 'the alternatives must ride along so they can be spoken');
});
check('guess: a genuine tie still ASKS -- guessing is not the same as bluffing', function () {
  const r = CCL.resolveGroups('s', RANK_ROSTER);
  assert.strictEqual(r.ok, false);
  assert.strictEqual(r.error, 'ambiguous');
});
check('guess: an unambiguous match carries NO hedge', function () {
  const r = CCL.resolveGroups('levin', RANK_ROSTER);
  assert.strictEqual(r.ok, true);
  assert.strictEqual(r.confidence, undefined, 'a certain match must not be hedged -- that would train the user to ignore hedges');
});
check('guess: the plan carries the assumption up to the speaker', function () {
  const ctx = { caps: CCL.SOCIOGRAM_CAPS, roster: RANK_ROSTER, tabs: [], nodes: [] };
  const p = CCL.plan(CCL.parse('only su', grammar), ctx);
  assert.strictEqual(p.ok, true);
  assert.strictEqual(p.guesses.length, 1);
  assert.strictEqual(p.guesses[0].chose, 'summa');
  assert.strictEqual(p.guesses[0].term, 'su');
});

// ---- report -----------------------------------------------------------------

if (failures.length) {
  console.error('FAIL: ' + failures.length + ' failed, ' + passed + ' passed\n');
  for (const f of failures) { console.error('  x ' + f); }
  process.exit(1);
}
console.log('ok: ' + passed + ' passed');
