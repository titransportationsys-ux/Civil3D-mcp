// Headless check of the page: node dashboard/test.cjs   (needs playwright; NODE_PATH=$(npm root -g))
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(), pg = await b.newPage({ viewport: { width: 1280, height: 900 } }), errs = [];
  pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await pg.goto('file://' + path.join(__dirname, 'index.html')); await pg.waitForTimeout(500);
  const r = await pg.evaluate(() => { const c = counts(); return { title: document.title, signs: RES.signs.length, wrong: c.wrong, check: c.check, ok: c.ok, gaps: RES.gaps.length, byFlag: c.byFlag }; });
  console.log(JSON.stringify(r)); console.log('ERRORS', JSON.stringify(errs));
  const expect = { signs: 68, gaps: 14, wrong: 7 }; const bad = Object.keys(expect).filter(k => r[k] !== expect[k]);
  await b.close(); if (bad.length || errs.length) { console.log('FAIL', bad); process.exit(1); } console.log('PASS (Wyte demo: 68 signs, 14 missing numbers, 7 wrong)');
})();
