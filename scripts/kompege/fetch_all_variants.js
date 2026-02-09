/**
 * Вытягивает данные по всем вариантам из kompege_variants_list.json.
 * Для каждого варианта: HTML страницы + все ответы от kompege.ru.
 *
 * Запуск (из scripts/kompege):
 *   node fetch_all_variants.js              # все варианты
 *   node fetch_all_variants.js --limit 10   # первые 10 (тест)
 *   node fetch_all_variants.js --delay 3000 # пауза 3 сек между вариантами
 *   node fetch_all_variants.js --skip-existing  # не перезаписывать уже скачанные
 */
import { firefox } from 'playwright';
import { writeFileSync, readFileSync, mkdirSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const dataDir = join(rootDir, 'kompege_data');
const variantsDir = join(dataDir, 'variants');

const args = process.argv.slice(2);
const limitIndex = args.indexOf('--limit');
const limit = limitIndex >= 0 && args[limitIndex + 1] ? parseInt(args[limitIndex + 1], 10) : null;
const delayIndex = args.indexOf('--delay');
const delayMs = delayIndex >= 0 && args[delayIndex + 1] ? parseInt(args[delayIndex + 1], 10) : 2500;
const skipExisting = args.includes('--skip-existing');

function shouldSkip(url) {
  const skip = ['google', 'yandex', 'vk.com', '.js', '.css', '.png', '.woff', 'favicon', 'analytics', 'mail.ru'];
  return skip.some(s => url.includes(s));
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function fetchOneVariant(page, variant, outDir) {
  const { kim, url, title } = variant;
  const responses = [];

  const onResponse = async (res) => {
    const u = res.url();
    if (shouldSkip(u) || !u.includes('kompege.ru')) return;
    let body = '';
    try {
      body = await res.text();
    } catch (e) {
      body = `[error: ${e.message}]`;
    }
    if (body.length > 800000) body = body.slice(0, 800000) + '\n...[truncated]';
    responses.push({
      url: u,
      status: res.status(),
      contentType: res.headers()['content-type'] || '',
      body,
    });
  };

  page.on('response', onResponse);
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(2000);
  } catch (e) {
    console.error(`  ошибка: ${e.message}`);
    page.off('response', onResponse);
    return { ok: false, error: e.message };
  }
  page.off('response', onResponse);

  const html = await page.content();
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, 'page.html'), html, 'utf8');
  writeFileSync(join(outDir, 'meta.json'), JSON.stringify({ kim, url, title }, null, 2), 'utf8');
  writeFileSync(join(outDir, 'responses.json'), JSON.stringify(responses, null, 2), 'utf8');
  return { ok: true, responsesCount: responses.length };
}

async function main() {
  const listPath = join(rootDir, 'kompege_variants_list.json');
  if (!existsSync(listPath)) {
    console.error('Сначала создайте список вариантов: node parse_archive_html.js');
    process.exit(1);
  }
  let variants = JSON.parse(readFileSync(listPath, 'utf8'));
  if (limit != null) {
    variants = variants.slice(0, limit);
    console.log('Ограничение: первые %s вариантов', limit);
  }
  console.log('Вариантов к выгрузке: %s, пауза между запросами: %s мс', variants.length, delayMs);
  if (skipExisting) console.log('Режим: пропуск уже скачанных');

  mkdirSync(variantsDir, { recursive: true });

  const browser = await firefox.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  });
  context.setDefaultTimeout(35000);
  const page = await context.newPage();

  let done = 0;
  let skipped = 0;
  let failed = 0;

  for (let i = 0; i < variants.length; i++) {
    const v = variants[i];
    const outDir = join(variantsDir, String(v.kim));
    if (skipExisting && existsSync(join(outDir, 'responses.json'))) {
      skipped++;
      process.stdout.write(`\r[${i + 1}/${variants.length}] skip ${v.kim} ${v.title.slice(0, 30)}...`);
      await sleep(500);
      continue;
    }
    process.stdout.write(`\r[${i + 1}/${variants.length}] ${v.kim} ${v.title.slice(0, 35)}...`);
    const result = await fetchOneVariant(page, v, outDir);
    if (result.ok) done++; else failed++;
    await sleep(delayMs);
  }

  await browser.close();
  console.log('\nГотово. Скачано: %s, пропущено: %s, ошибок: %s', done, skipped, failed);
  console.log('Данные в %s', variantsDir);
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
