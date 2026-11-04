// Headless test of the Export tab with a mock downloads capability: node dashboard/test_export.cjs
const { chromium } = require('playwright'); const fs = require('fs');
const D = __dirname + '/', O = require('os').tmpdir() + '/ard_export_test/';
(async () => {
  fs.mkdirSync(O, { recursive: true });
  const b = await chromium.launch(), ctx = await b.newContext({ viewport: { width: 1280, height: 900 } }), errs = [];
  await ctx.addInitScript(() => { window.__saves = []; window.claude = { use: async (n) => n === 'downloads' ? { save: async ({ filename, data }) => {
    const ext = filename.split('.').pop(); if (ext === 'dxf') { const e = new Error('ext'); e.code = 'rejected_extension'; throw e; }
    let b64; if (typeof data === 'string') b64 = btoa(unescape(encodeURIComponent(data))); else b64 = await new Promise(r => { const fr = new FileReader(); fr.onload = () => r(fr.result.split(',')[1]); fr.readAsDataURL(data); });
    window.__saves.push({ filename, b64 }); return { status: 'saved' }; } } : null }; });
  const pg = await ctx.newPage(); pg.on('pageerror', e => errs.push('PAGEERR ' + e.message)); pg.on('console', m => { if (m.type() === 'error') errs.push('CONSOLE ' + m.text()); });
  await pg.goto('file://' + D + 'index.html'); await pg.waitForTimeout(500);
  console.log('TABS', await pg.$$eval('#tabs button', bs => bs.map(x => x.dataset.v).join(' ')));
  await pg.screenshot({ path: O + 'header.png', clip: { x: 0, y: 0, width: 1280, height: 330 } });
  await pg.click('[data-v=export]'); await pg.waitForTimeout(300);
  console.log('HAS Save as:', await pg.$('#exSaveAs') !== null, '| formats:', await pg.$$eval('#exFmt option', o => o.map(x => x.value).join(',')));
  await pg.screenshot({ path: O + 'export.png' });
  for (const f of ['csv', 'json', 'md', 'txt', 'dxf', 'png']) { await pg.selectOption('#exFmt', f); await pg.fill('#exName', 'test_' + f); await pg.click('#exSaveAs'); await pg.waitForTimeout(400); console.log(f, '->', await pg.textContent('#exMsg')); }
  for (const f of ['csv', 'dxf', 'txt']) { await pg.click('button[data-ex=' + f + ']'); await pg.waitForTimeout(400); console.log('quick', f, '->', await pg.textContent('#exMsg')); }
  const saves = await pg.evaluate(() => window.__saves); saves.forEach((s, i) => fs.writeFileSync(O + i + '_' + s.filename, Buffer.from(s.b64, 'base64')));
  console.log('SAVED', saves.map(s => s.filename).join(' '));
  // filter respected: hide 'ok' then export count
  await pg.click('[data-v=map]'); await pg.click('#fbMap [data-sev=ok]'); await pg.click('[data-v=export]'); await pg.waitForTimeout(200);
  console.log('NOTE', (await pg.textContent('#v-export p.muted')).slice(0, 80));
  console.log('ERRORS', JSON.stringify(errs)); await b.close();
})();
