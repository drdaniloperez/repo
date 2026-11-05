const { chromium } = require('playwright');
(async () => {
  const [html] = process.argv.slice(2);
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 2 });
  await pg.goto('file://' + html);
  await pg.screenshot({ path: html.replace('.html', '.png'), fullPage: true });
  const h = await pg.evaluate('document.body.scrollHeight');
  await pg.pdf({ path: html.replace('.html', '.pdf'), width: '1600px', height: (h + 2) + 'px', printBackground: true });
  await b.close();
})();
