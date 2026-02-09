/**
 * Открывает КЕГЭ (kompege.ru), переходит в архив и перехватывает XHR/fetch.
 * Результат: kompege_api_found.json в корне проекта.
 */
import { firefox } from 'playwright';
import { writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const outputPath = join(rootDir, 'kompege_api_found.json');

const captured = { requests: [], responses: [] };

function shouldSkip(url) {
  const skip = ['google', 'yandex', 'vk.com', '.js', '.css', '.png', '.woff', 'favicon', 'analytics'];
  return skip.some(s => url.includes(s));
}

async function main() {
  const browser = await firefox.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  });
  context.setDefaultTimeout(25000);

  const page = await context.newPage();

  page.on('request', req => {
    if (shouldSkip(req.url())) return;
    captured.requests.push({ url: req.url(), method: req.method(), postData: req.postData() || null });
  });

  page.on('response', async res => {
    if (shouldSkip(res.url())) return;
    let bodyPreview = '';
    try {
      const body = await res.text();
      bodyPreview = body.length > 2000 ? body.slice(0, 2000) + '\n... [truncated]' : body;
    } catch (e) {
      bodyPreview = `[could not read: ${e.message}]`;
    }
    captured.responses.push({
      url: res.url(),
      status: res.status(),
      bodyPreview,
    });
  });

  try {
    console.log('Открываю https://kompege.ru/ ...');
    await page.goto('https://kompege.ru/', { waitUntil: 'networkidle' });
    console.log('Главная загружена.');

    console.log('Переход в архив...');
    await page.goto('https://kompege.ru/archive', { waitUntil: 'networkidle' });
    console.log('Архив загружен.');

    await page.waitForTimeout(3000);

    // Сохраняем HTML архива — возможно, данные встроены в страницу (SSR)
    const archiveHtml = await page.content();
    const htmlPath = join(rootDir, 'kompege_archive_page.html');
    writeFileSync(htmlPath, archiveHtml, 'utf8');
    console.log('HTML архива сохранён в', htmlPath);

    // Клик по первой ссылке на вариант (только внутренние /variant?kim=...)
    try {
      const link = page.locator('a[href^="/variant?kim="]').first;
      await link.click({ timeout: 5000 });
      console.log('Переход на страницу варианта...');
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(3000);

      // Сохраняем HTML страницы варианта (могут быть встроенные данные)
      const variantHtml = await page.content();
      const variantHtmlPath = join(rootDir, 'kompege_variant_page.html');
      writeFileSync(variantHtmlPath, variantHtml, 'utf8');
      console.log('HTML варианта сохранён в', variantHtmlPath);
    } catch (e) {
      console.log('Клик по варианту:', e.message);
    }

  } catch (e) {
    console.error('Ошибка:', e.message);
  } finally {
    await browser.close();
  }

  // Уникальные ответы по URL (последний)
  const byUrl = new Map();
  for (const r of captured.responses) byUrl.set(r.url, r);
  captured.responses = [...byUrl.values()];

  writeFileSync(outputPath, JSON.stringify(captured, null, 2), 'utf8');
  console.log('\nСохранено в', outputPath);
  console.log('\n--- Запросы (без статики) ---');
  for (const r of captured.requests) console.log(r.method, r.url.slice(0, 100));
  console.log('\n--- Ответы ---');
  for (const r of captured.responses) {
    console.log(r.status, r.url.slice(0, 80));
    if (r.bodyPreview && !r.bodyPreview.startsWith('[')) console.log('  preview:', r.bodyPreview.slice(0, 150).replace(/\n/g, ' ') + '...');
  }
}

main();
