/**
 * Для каждого варианта в kompege_data/variants/ создаёт task1.html —
 * первая задача с картинками (HTML из API, картинки base64 или с kompege.ru).
 *
 * Запуск: node export_first_task_html.js
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const variantsDir = join(rootDir, 'kompege_data', 'variants');

const PAGE_TEMPLATE = (title, taskHtml, taskNumber, answer) => `<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Задача ${taskNumber} — ${escapeHtml(title)}</title>
  <style>
    body { font-family: sans-serif; max-width: 800px; margin: 1rem auto; padding: 0 1rem; }
    .task { line-height: 1.5; }
    .task img { max-width: 100%; height: auto; }
    .answer { margin-top: 1rem; padding: 0.5rem; background: #eee; border-radius: 4px; }
    h1 { font-size: 1.2rem; }
  </style>
</head>
<body>
  <h1>Задача ${taskNumber}</h1>
  <div class="task">${taskHtml}</div>
  <div class="answer"><strong>Ответ:</strong> ${escapeHtml(answer || '—')}</div>
</body>
</html>`;

function escapeHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function main() {
  if (!existsSync(variantsDir)) {
    console.error('Нет папки kompege_data/variants. Сначала запустите fetch_variants_api.js');
    process.exit(1);
  }

  const dirs = readdirSync(variantsDir).filter(d => {
    return existsSync(join(variantsDir, d, 'api.json'));
  });

  let count = 0;
  for (const dir of dirs) {
    const apiPath = join(variantsDir, dir, 'api.json');
    const metaPath = join(variantsDir, dir, 'meta.json');
    let title = dir;
    try {
      const meta = JSON.parse(readFileSync(metaPath, 'utf8'));
      title = meta.title || title;
    } catch (_) {}

    const api = JSON.parse(readFileSync(apiPath, 'utf8'));
    const tasks = api.tasks;
    if (!tasks || tasks.length === 0) continue;

    const first = tasks[0];
    const taskNumber = first.number ?? 1;
    const text = first.text ?? '';
    const answer = first.key ?? '';

    // Делаем ссылки на картинки kompege.ru абсолютными (на случай если были относительные)
    const taskHtml = text
      .replace(/src="\/images\//g, 'src="https://kompege.ru/images/');

    const html = PAGE_TEMPLATE(title, taskHtml, taskNumber, answer);
    const outPath = join(variantsDir, dir, 'task1.html');
    writeFileSync(outPath, html, 'utf8');
    count++;
  }

  console.log('Создано task1.html для %s вариантов в %s', count, variantsDir);
}

main();
