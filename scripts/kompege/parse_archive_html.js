/**
 * Парсит сохранённый HTML архива КЕГЭ (kompege_archive_page.html)
 * и вытаскивает все варианты: kim, название, ссылка.
 * Результат: kompege_variants_list.json в корне проекта.
 */
import { readFileSync, writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const htmlPath = join(rootDir, 'kompege_archive_page.html');
const outputPath = join(rootDir, 'kompege_variants_list.json');

const html = readFileSync(htmlPath, 'utf8');

// Ссылки на варианты: /variant?kim=25107025, текст — название
const re = /<a href="(\/variant\?kim=(\d+))"[^>]*>([^<]+)<\/a>/g;
const variants = [];
let m;
while ((m = re.exec(html)) !== null) {
  const [, url, kim, title] = m;
  const cleanTitle = title.replace(/\s+/g, ' ').trim();
  if (cleanTitle && !cleanTitle.startsWith('http')) {
    variants.push({
      kim: parseInt(kim, 10),
      url: `https://kompege.ru${url}`,
      title: cleanTitle,
    });
  }
}

// Убираем дубли по kim (оставляем первое вхождение)
const byKim = new Map();
for (const v of variants) {
  if (!byKim.has(v.kim)) byKim.set(v.kim, v);
}
const unique = [...byKim.values()];

writeFileSync(outputPath, JSON.stringify(unique, null, 2), 'utf8');
console.log(`Сохранено ${unique.length} вариантов в ${outputPath}`);
console.log('Примеры:', unique.slice(0, 5));
