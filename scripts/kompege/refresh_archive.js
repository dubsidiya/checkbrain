/**
 * Обновляет список вариантов: загружает страницу архива КЕГЭ и парсит ссылки.
 * Результат: kompege_archive_page.html и kompege_variants_list.json в корне проекта.
 *
 * Запуск: node refresh_archive.js
 */
import { firefox } from 'playwright';
import { writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');

async function main() {
  const browser = await firefox.launch({ headless: true });
  const page = await browser.newPage({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
  });
  try {
    await page.goto('https://kompege.ru/archive', { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);
    const html = await page.content();
    const htmlPath = join(rootDir, 'kompege_archive_page.html');
    writeFileSync(htmlPath, html, 'utf8');
    console.log('Архив сохранён:', htmlPath);

    const re = /<a href="(\/variant\?kim=(\d+))"[^>]*>([^<]+)<\/a>/g;
    const variants = [];
    const seen = new Set();
    let m;
    while ((m = re.exec(html)) !== null) {
      const [, path, kim, title] = m;
      const k = parseInt(kim, 10);
      if (seen.has(k)) continue;
      seen.add(k);
      variants.push({
        kim: k,
        url: `https://kompege.ru${path}`,
        title: title.replace(/\s+/g, ' ').trim(),
      });
    }
    const listPath = join(rootDir, 'kompege_variants_list.json');
    writeFileSync(listPath, JSON.stringify(variants, null, 2), 'utf8');
    console.log('Список вариантов:', listPath, '(%s шт.)', variants.length);
  } finally {
    await browser.close();
  }
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
