/**
 * Открывает страницу одного варианта КЕГЭ и вытаскивает все данные:
 * - HTML страницы варианта
 * - Все ответы от kompege.ru (в т.ч. JSON с задачами)
 *
 * Запуск: node fetch_variant_data.js [kim]
 * Пример: node fetch_variant_data.js 25107025
 */
import { firefox } from 'playwright';
import { writeFileSync, readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');

const kim = process.argv[2] || '25107025';
const variantUrl = `https://kompege.ru/variant?kim=${kim}`;

const kompegeResponses = []; // { url, status, body }

function shouldSkip(url) {
  const skip = ['google', 'yandex', 'vk.com', '.js', '.css', '.png', '.woff', 'favicon', 'analytics', 'mail.ru'];
  return skip.some(s => url.includes(s));
}

async function main() {
  const browser = await firefox.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  });
  context.setDefaultTimeout(30000);

  const page = await context.newPage();

  page.on('response', async res => {
    const url = res.url();
    if (shouldSkip(url) || !url.includes('kompege.ru')) return;
    let body = '';
    try {
      body = await res.text();
    } catch (e) {
      body = `[error: ${e.message}]`;
    }
    kompegeResponses.push({
      url,
      status: res.status(),
      contentType: res.headers()['content-type'] || '',
      body: body.length > 500000 ? body.slice(0, 500000) + '\n...[truncated]' : body,
    });
  });

  try {
    console.log('Открываю вариант kim=%s ...', kim);
    await page.goto(variantUrl, { waitUntil: 'networkidle' });
    await page.waitForTimeout(4000);

    const html = await page.content();
    const htmlPath = join(rootDir, `kompege_variant_${kim}.html`);
    writeFileSync(htmlPath, html, 'utf8');
    console.log('HTML сохранён:', htmlPath);
  } catch (e) {
    console.error('Ошибка:', e.message);
  } finally {
    await browser.close();
  }

  // Сохраняем все ответы от kompege.ru
  const dataPath = join(rootDir, `kompege_variant_${kim}_responses.json`);
  writeFileSync(dataPath, JSON.stringify(kompegeResponses, null, 2), 'utf8');
  console.log('Ответы сохранены:', dataPath, `(${kompegeResponses.length} записей)`);

  // Если есть JSON-ответ с задачами — сохраняем отдельно для удобства
  for (const r of kompegeResponses) {
    if (r.body.startsWith('{') || r.body.startsWith('[')) {
      try {
        const parsed = JSON.parse(r.body.replace(/\n...[truncated]$/, ''));
        const shortName = r.url.replace(/https?:\/\/kompege\.ru\/?/, '').replace(/[^a-z0-9]/gi, '_').slice(0, 40);
        const jsonPath = join(rootDir, `kompege_variant_${kim}_${shortName}.json`);
        writeFileSync(jsonPath, JSON.stringify(parsed, null, 2), 'utf8');
        console.log('JSON сохранён:', jsonPath);
      } catch (_) {}
    }
  }
}

main();
