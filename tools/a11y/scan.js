// Accessibility scan for the built site. Run it with "make a11y" (which builds
// _site, serves it, and points this at it).
//
// Three passes:
//   1. axe-core, WCAG 2.0/2.1 A + AA rules, every page, in four states
//      (desktop, 320px = 400% zoom, mobile with the menu open, reduced motion)
//   2. criteria axe does not decide: focus order and focus visibility walked
//      with real Tab presses, link purpose, heading structure, alt quality,
//      page titles, 1.4.12 text spacing, the accessibility tree a screen
//      reader is handed
//   3. behaviour: the slideshow's pause button, the keyboard path through the
//      "pick your professor" matrix, the mobile menu, the campus map
//
// Exit code is non-zero if anything fails, so CI can gate on it.
const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer-core');

const BASE = process.env.A11Y_BASE || 'http://127.0.0.1:4100';
const AXE = fs.readFileSync(path.join(__dirname, 'node_modules/axe-core/axe.min.js'), 'utf8');
const CHROME = [
  process.env.CHROME_PATH,
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome',
].find(p => p && fs.existsSync(p));

const PAGES = ['/', '/ai.html', '/alumni.html', '/compliance.html', '/contact.html', '/directory.html',
  '/faculty.html', '/internships.html', '/keynotes.html', '/lessons.html', '/pick.html', '/pubs.html',
  '/raleigh.html', '/student-life.html', '/students.html'];
const TAGS = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'];
const SPACING = `* { line-height: 1.5 !important; letter-spacing: 0.12em !important;
  word-spacing: 0.16em !important; }
 p, li, td, th, figcaption { margin-bottom: 2em !important; }`;

const fails = [];
const note = (where, what) => { fails.push(`${where}: ${what}`); console.log(`  FAIL ${where}: ${what}`); };

async function launch(tries) {
  for (let i = 1; ; i++) {
    try {
      return await puppeteer.launch({
        executablePath: CHROME, headless: true, timeout: 90000,
        args: ['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu'],
      });
    } catch (e) {
      if (i >= tries) throw e;
      console.log(`  chrome did not start (attempt ${i}): ${e.message.split('\n')[0]}`);
    }
  }
}

async function axeRun(page) {
  await page.evaluate(AXE);
  return page.evaluate(async (tags) => (await axe.run(document, {
    runOnly: { type: 'tag', values: tags }, resultTypes: ['violations'],
  })).violations.map(v => `${v.impact} ${v.id} x${v.nodes.length} [${v.nodes[0].target}]`), TAGS);
}

(async () => {
  if (!CHROME) { console.error('no Chrome found'); process.exit(2); }
  // CI runners occasionally fail to hand back the devtools endpoint inside the
  // default 30s. --disable-dev-shm-usage keeps Chrome off the runner's tiny
  // /dev/shm (the usual cause); the retry covers the rest.
  const browser = await launch(2);

  // ---------- 1. axe, four states ----------
  const STATES = [
    { name: 'desktop 1280px', vp: { width: 1280, height: 900 } },
    { name: '320px (400% zoom)', vp: { width: 320, height: 640 } },
    { name: 'mobile, menu open', vp: { width: 320, height: 640 }, menu: true },
    { name: 'reduced motion', vp: { width: 1280, height: 900 }, calm: true },
  ];
  for (const st of STATES) {
    let n = 0;
    for (const p of PAGES) {
      const page = await browser.newPage();
      if (st.calm) await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
      await page.setViewport(st.vp);
      await page.goto(BASE + p, { waitUntil: 'networkidle2' });
      if (st.menu) { await page.click('#menu-button'); await new Promise(r => setTimeout(r, 250)); }
      const v = await axeRun(page);
      v.forEach(x => note(`axe ${st.name} ${p}`, x));
      n += v.length;
      await page.close();
    }
    console.log(`axe ${st.name}: ${n} violations over ${PAGES.length} pages`);
  }

  // ---------- 2. what axe leaves to a human ----------
  for (const p of PAGES) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1280, height: 900 });
    await page.goto(BASE + p, { waitUntil: 'networkidle2' });

    const stat = await page.evaluate(() => {
      const out = { title: document.title, lang: document.documentElement.lang || null, bad: [] };
      if (!out.lang) out.bad.push('no lang on <html>');
      if (!out.title) out.bad.push('no page title');
      if (document.querySelector('meta[http-equiv="refresh"]')) out.bad.push('meta refresh (2.2.1/2.2.4)');
      if (!document.querySelector('main')) out.bad.push('no main landmark');
      const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(h => h.offsetParent !== null).map(h => +h.tagName[1]);
      if (hs.filter(l => l === 1).length !== 1) out.bad.push(`h1 count = ${hs.filter(l => l === 1).length}`);
      for (let i = 1; i < hs.length; i++) if (hs[i] - hs[i - 1] > 1) out.bad.push(`heading skip h${hs[i - 1]} -> h${hs[i]}`);
      const vague = /^(here|click here|read more|more|link|this|details)\b/i;
      const byName = new Map();
      for (const a of document.querySelectorAll('a[href]')) {
        if (a.offsetParent === null) continue;
        const txt = (a.getAttribute('aria-label') || a.textContent || '').trim().replace(/\s+/g, ' ');
        if (vague.test(txt)) out.bad.push(`vague link "${txt}" (2.4.4)`);
        if (txt && byName.has(txt.toLowerCase()) && byName.get(txt.toLowerCase()) !== a.href)
          out.bad.push(`link text "${txt}" points at two places (2.4.4)`);
        if (txt) byName.set(txt.toLowerCase(), a.href);
      }
      for (const img of document.querySelectorAll('img')) {
        const alt = img.getAttribute('alt');
        if (alt === null) out.bad.push(`img with no alt: ${img.getAttribute('src')}`);
        else if (alt && (/\.(jpg|jpeg|png|gif|svg)$/i.test(alt) || /^(image|photo|picture|img)[\s_\-0-9]*$/i.test(alt)))
          out.bad.push(`generic alt "${alt}"`);
      }
      for (const c of document.querySelectorAll('input:not([type=hidden]),select,textarea')) {
        const lbl = c.id && document.querySelector(`label[for="${CSS.escape(c.id)}"]`);
        if (!(lbl || c.getAttribute('aria-label') || c.getAttribute('aria-labelledby') || c.title))
          out.bad.push(`control with no label: ${c.outerHTML.slice(0, 80)}`);
      }
      return out;
    });
    stat.bad.forEach(b => note(`structure ${p}`, b));

    // 2.4.3 / 2.4.7: walk the tab ring with real Tab presses
    const order = [], seen = new Set();
    for (let i = 0; i < 120; i++) {
      await page.keyboard.press('Tab');
      const info = await page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return null;
        const cs = getComputedStyle(el), r = el.getBoundingClientRect();
        const name = (el.getAttribute('aria-label') || el.textContent || el.value || '').trim().replace(/\s+/g, ' ').slice(0, 40);
        return {
          tag: el.tagName.toLowerCase(), name,
          lit: (cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) > 0) || cs.boxShadow !== 'none',
          offscreen: r.width === 0 || r.height === 0,
          key: el.tagName + name + Math.round(r.top + scrollY) + Math.round(r.left),
        };
      });
      if (!info || seen.has(info.key)) break;
      seen.add(info.key);
      order.push(info);
    }
    order.filter(o => !o.lit && !o.offscreen).forEach(o => note(`focus ${p}`, `no visible focus on ${o.tag} "${o.name}" (2.4.7)`));
    if (!order.length) note(`focus ${p}`, 'nothing focusable');

    // 4.1.2 via the accessibility tree: every widget needs a name
    const flat = [];
    (function walk(n) { if (!n) return; flat.push(n); (n.children || []).forEach(walk); })(await page.accessibility.snapshot({ interestingOnly: true }));
    flat.filter(n => /button|link|checkbox|textbox|combobox|menuitem/.test(n.role) && !n.name)
      .forEach(n => note(`a11y tree ${p}`, `${n.role} with no accessible name (4.1.2)`));

    // 1.4.12 text spacing
    await page.addStyleTag({ content: SPACING });
    await new Promise(r => setTimeout(r, 250));
    const spacing = await page.evaluate(() => {
      const bad = [];
      if (document.documentElement.scrollWidth > document.documentElement.clientWidth + 2) bad.push('page scrolls sideways under the 1.4.12 spacing override');
      document.querySelectorAll('p,li,td,th,h1,h2,h3,figcaption').forEach(el => {
        const cs = getComputedStyle(el);
        if (el.scrollHeight > el.clientHeight + 4 && /hidden|clip/.test(cs.overflowY)) bad.push(`text clipped: "${el.textContent.trim().slice(0, 30)}"`);
      });
      return bad.slice(0, 5);
    });
    spacing.forEach(s => note(`text spacing ${p}`, s));
    await page.close();
  }

  // ---------- 3. does the thing actually work ----------
  let page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto(BASE + '/', { waitUntil: 'networkidle2' });
  const frame = () => page.evaluate(() => [...document.querySelectorAll('.marquee figure')].findIndex(f => f.classList.contains('on')));
  const btn = await page.evaluate(() => { const b = document.querySelector('.marquee-pause'); b.focus(); const ok = document.activeElement === b; b.click(); return ok; });
  if (!btn) note('marquee', 'pause button is not keyboard focusable (2.1.1)');
  const f0 = await frame();
  await new Promise(r => setTimeout(r, 11000));
  if (await frame() !== f0) note('marquee', 'slideshow keeps advancing while paused (2.2.2)');
  await page.evaluate(() => document.querySelector('.marquee-pause').click());
  await new Promise(r => setTimeout(r, 6000));
  if (await frame() === f0) note('marquee', 'play does not resume the slideshow');
  await page.close();

  page = await browser.newPage();
  await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto(BASE + '/', { waitUntil: 'networkidle2' });
  const r0 = await page.evaluate(() => [...document.querySelectorAll('.marquee figure')].findIndex(f => f.classList.contains('on')));
  await new Promise(r => setTimeout(r, 11000));
  const rm = await page.evaluate(() => ({ idx: [...document.querySelectorAll('.marquee figure')].findIndex(f => f.classList.contains('on')), anim: getComputedStyle(document.querySelector('a.hiring')).animationName }));
  if (rm.idx !== r0) note('reduced motion', 'slideshow rotates even though the reader asked for less motion');
  if (rm.anim !== 'none') note('reduced motion', `hiring badge still animates (${rm.anim})`);
  await page.close();

  page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto(BASE + '/pick.html', { waitUntil: 'networkidle2' });
  const kb = await page.evaluate(() => {
    const th = document.querySelector('th.p');
    th.focus();
    const focused = document.activeElement === th;
    th.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
    return { focused, pressed: th.getAttribute('aria-pressed') === 'true', card: !!document.querySelector('#pick-card .nm') };
  });
  if (!kb.focused) note('pick matrix', 'column heads are not focusable (2.1.1)');
  if (!kb.pressed || !kb.card) note('pick matrix', 'Enter does not select a professor (2.1.1)');
  await page.close();

  page = await browser.newPage();
  await page.setViewport({ width: 320, height: 640 });
  await page.goto(BASE + '/', { waitUntil: 'networkidle2' });
  await page.evaluate(() => document.getElementById('menu-button').focus());
  await page.keyboard.press('Enter');
  await new Promise(r => setTimeout(r, 250));
  const menu = await page.evaluate(() => ({ pressed: document.getElementById('menu-button').getAttribute('aria-pressed'), open: document.getElementById('site-nav').getBoundingClientRect().height > 50 }));
  if (menu.pressed !== 'true' || !menu.open) note('mobile menu', 'Enter does not open the menu (2.1.1)');
  await page.close();

  page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  await page.goto(BASE + '/contact.html', { waitUntil: 'networkidle2' });
  const before = await page.evaluate(() => { document.getElementById('campus-map').focus(); return document.querySelector('#campus-map .leaflet-map-pane').style.transform; });
  await page.keyboard.press('ArrowRight');
  await new Promise(r => setTimeout(r, 500));
  const after = await page.evaluate(() => document.querySelector('#campus-map .leaflet-map-pane').style.transform);
  if (before === after) note('campus map', 'arrow keys do not pan the map (2.1.1)');
  await page.close();

  await browser.close();
  console.log(fails.length ? `\n${fails.length} FAILURES` : '\nall checks pass');
  process.exit(fails.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(2); });
