/**
 * Обходит kompege_data/variants/*, вытаскивает из responses.json
 * все структуры с задачами (tasks/problems) и собирает в один объём.
 *
 * Источники только kompege_data. Файлы/папки ege1, ege2, ege3, ege4 и desh/ege2026kp не используются.
 *
 * Запуск (из scripts/kompege):
 *   node extract_all_tasks.js
 *
 * Результат в kompege_data/extracted/:
 *   variants.json         — по вариантам: { kim, title, tasks[] }
 *   tasks_flat.json       — плоский список всех задач (с повторами по вариантам)
 *   all_tasks_unique.json — все уникальные задачи без дубликатов (variantKims, variantCount)
 *   api_samples/          — примеры сырых JSON-ответов по типам
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const dataDir = join(rootDir, 'kompege_data');
const variantsDir = join(dataDir, 'variants');
const outDir = join(dataDir, 'extracted');
const samplesDir = join(outDir, 'api_samples');

function extractTaskLike(obj, kim, title) {
  const out = [];
  if (!obj || typeof obj !== 'object') return out;

  const take = (arr, source) => {
    if (!Array.isArray(arr)) return;
    arr.forEach((item, idx) => {
      if (!item || typeof item !== 'object') return;
      const taskNumber = item.taskNumber ?? item.number ?? item.num ?? item.task ?? item.n ?? idx + 1;
      const condition = item.condition ?? item.text ?? item.content ?? item.body ?? item.question ?? item.taskText ?? '';
      const answer = item.answer ?? item.key ?? item.rightAnswer ?? item.correct ?? item.ans ?? item.correctAnswer ?? '';
      const id = item.id ?? item.kim ?? null;
      const taskId = item.taskId ?? null;
      const difficulty = item.difficulty != null ? Math.max(0, parseInt(String(item.difficulty), 10) || 0) : 0;
      out.push({
        kim,
        variantTitle: title,
        taskNumber: typeof taskNumber === 'number' ? taskNumber : parseInt(String(taskNumber), 10) || idx + 1,
        condition: typeof condition === 'string' ? condition : (condition?.text || (condition && JSON.stringify(condition)) || ''),
        answer: typeof answer === 'string' ? answer : String(answer ?? ''),
        rawId: id,
        taskId: taskId != null ? taskId : null,
        difficulty,
      });
    });
  };

  take(obj.tasks, 'tasks');
  take(obj.problems, 'problems');
  take(obj.items, 'items');
  take(obj.exercises, 'exercises');
  take(obj.data?.tasks, 'data.tasks');
  take(obj.data?.problems, 'data.problems');
  if (Array.isArray(obj)) take(obj, 'root');
  if (obj.data && Array.isArray(obj.data)) take(obj.data, 'data');

  // Один объект с полем типа task
  if (obj.taskNumber != null || obj.number != null) {
    const taskNumber = obj.taskNumber ?? obj.number ?? 0;
    const condition = obj.condition ?? obj.text ?? obj.content ?? '';
    const answer = obj.answer ?? obj.key ?? obj.rightAnswer ?? '';
    const difficulty = obj.difficulty != null ? Math.max(0, parseInt(String(obj.difficulty), 10) || 0) : 0;
    out.push({
      kim,
      variantTitle: title,
      taskNumber: typeof taskNumber === 'number' ? taskNumber : parseInt(String(taskNumber), 10),
      condition: typeof condition === 'string' ? condition : JSON.stringify(condition),
      answer: typeof answer === 'string' ? answer : String(answer),
      rawId: obj.id ?? null,
      taskId: obj.taskId ?? null,
      difficulty,
    });
  }
  return out;
}

function tryParseJson(body) {
  if (typeof body !== 'string' || !body.trim()) return null;
  const s = body.replace(/\n\.\.\.\[truncated\]$/, '').trim();
  if ((!s.startsWith('{') && !s.startsWith('[')) || s.length < 10) return null;
  try {
    return JSON.parse(s);
  } catch (_) {
    return null;
  }
}

const IMG_SRC_URL_RE = /<img[^>]+src="(https?:\/\/[^"]+)"/gi;

/** Собирает все уникальные URL картинок из условий. */
function collectImageUrls(tasks) {
  const urls = new Set();
  for (const t of tasks) {
    const html = t.condition || '';
    let m;
    IMG_SRC_URL_RE.lastIndex = 0;
    while ((m = IMG_SRC_URL_RE.exec(html)) !== null) urls.add(m[1]);
  }
  return Array.from(urls);
}

/** Скачивает URL и возвращает data:image/...;base64,... или null при ошибке. */
async function fetchImageAsDataUrl(url) {
  try {
    const res = await fetch(url, { redirect: 'follow' });
    if (!res.ok) return null;
    const buf = await res.arrayBuffer();
    const b64 = Buffer.from(buf).toString('base64');
    const contentType = (res.headers.get('content-type') || 'image/png').split(';')[0].trim();
    return `data:${contentType};base64,${b64}`;
  } catch (e) {
    console.warn('  [img] %s: %s', url.slice(0, 55), e.message);
    return null;
  }
}

/** Заменяет в условиях задач все img src="https://..." на data:...;base64,... */
async function inlineImageUrlsInTasks(tasks) {
  const urls = collectImageUrls(tasks);
  if (urls.length === 0) return tasks;
  console.log('Загрузка изображений по URL (%s уникальных)...', urls.length);
  const urlToData = new Map();
  for (const url of urls) {
    const dataUrl = await fetchImageAsDataUrl(url);
    if (dataUrl) urlToData.set(url, dataUrl);
  }
  console.log('  загружено: %s из %s', urlToData.size, urls.length);
  for (const task of tasks) {
    let html = task.condition || '';
    for (const [url, dataUrl] of urlToData) {
      html = html.split(url).join(dataUrl);
    }
    task.condition = html;
  }
  return tasks;
}

async function main() {
  if (!existsSync(variantsDir)) {
    console.error('Сначала запустите fetch_all_variants.js');
    process.exit(1);
  }

  const dirs = readdirSync(variantsDir).filter(d => {
    const p = join(variantsDir, d);
    return existsSync(join(p, 'api.json')) || existsSync(join(p, 'responses.json'));
  });

  const byVariant = [];
  const tasksFlat = [];
  const sampleByUrl = new Map();

  for (const dir of dirs) {
    const kim = dir;
    const metaPath = join(variantsDir, dir, 'meta.json');
    const apiPath = join(variantsDir, dir, 'api.json');
    const respPath = join(variantsDir, dir, 'responses.json');
    let title = kim;
    if (existsSync(metaPath)) {
      try {
        const meta = JSON.parse(readFileSync(metaPath, 'utf8'));
        title = meta.title || meta.kim || title;
      } catch (_) {}
    }
    const variantTasks = [];

    if (existsSync(apiPath)) {
      try {
        const api = JSON.parse(readFileSync(apiPath, 'utf8'));
        const extracted = extractTaskLike(api, kim, title);
        if (extracted.length) {
          variantTasks.push(...extracted);
          tasksFlat.push(...extracted);
        }
        if (!sampleByUrl.has('api_variant')) sampleByUrl.set('api_variant', { url: '/api/v1/variant/kim/N', body: api });
      } catch (e) {
        console.error('read %s: %s', apiPath, e.message);
      }
    }

    if (existsSync(respPath)) {
      try {
        const responses = JSON.parse(readFileSync(respPath, 'utf8'));
        for (const r of responses) {
          const parsed = tryParseJson(r.body);
          if (!parsed) continue;
          const extracted = extractTaskLike(parsed, kim, title);
          if (extracted.length) {
            variantTasks.push(...extracted);
            tasksFlat.push(...extracted);
            const urlKey = r.url.replace(/\d+/, 'N').slice(0, 80);
            if (!sampleByUrl.has(urlKey)) sampleByUrl.set(urlKey, { url: r.url, body: parsed });
          }
        }
      } catch (e) {
        console.error('read %s: %s', respPath, e.message);
      }
    }

    byVariant.push({
      kim,
      title,
      tasksCount: variantTasks.length,
      tasks: variantTasks,
    });
  }

  mkdirSync(outDir, { recursive: true });
  mkdirSync(samplesDir, { recursive: true });

  writeFileSync(
    join(outDir, 'variants.json'),
    JSON.stringify(byVariant, null, 2),
    'utf8'
  );
  writeFileSync(
    join(outDir, 'tasks_flat.json'),
    JSON.stringify(tasksFlat, null, 2),
    'utf8'
  );

  // Уникальные задачи (дедупликация по taskId или по номеру+условию)
  const uniqueByKey = new Map();
  for (const t of tasksFlat) {
    const key = t.taskId != null
      ? `id:${t.taskId}`
      : `n:${t.taskNumber}:${String(t.condition).trim().slice(0, 400)}`;
    if (!uniqueByKey.has(key)) {
      uniqueByKey.set(key, {
        taskNumber: t.taskNumber,
        condition: t.condition,
        answer: t.answer,
        difficulty: t.difficulty ?? 0,
        taskId: t.taskId ?? undefined,
        rawId: t.rawId ?? undefined,
        variantKims: [t.kim],
        firstVariantTitle: t.variantTitle,
      });
    } else {
      const u = uniqueByKey.get(key);
      if (!u.variantKims.includes(t.kim)) u.variantKims.push(t.kim);
    }
  }
  let allTasksUnique = Array.from(uniqueByKey.values()).map(u => ({
    taskNumber: u.taskNumber,
    condition: u.condition,
    answer: u.answer,
    difficulty: u.difficulty ?? 0,
    ...(u.taskId != null && { taskId: u.taskId }),
    ...(u.rawId && { rawId: u.rawId }),
    variantKims: u.variantKims,
    variantCount: u.variantKims.length,
  }));

  // Подставляем изображения по URL в base64, чтобы в приложении они отображались (нет CORS)
  allTasksUnique = await inlineImageUrlsInTasks(allTasksUnique);

  writeFileSync(
    join(outDir, 'all_tasks_unique.json'),
    JSON.stringify(allTasksUnique, null, 2),
    'utf8'
  );

  // Копия для приложения (assets): один JSON с задачами и сложностью
  const appAssetPath = join(rootDir, 'assets', 'kompege_tasks.json');
  mkdirSync(join(rootDir, 'assets'), { recursive: true });
  writeFileSync(appAssetPath, JSON.stringify(allTasksUnique), 'utf8');
  console.log('Для приложения: %s', appAssetPath);

  let i = 0;
  for (const [urlKey, { url, body }] of sampleByUrl) {
    const safe = urlKey.replace(/[^a-z0-9]/gi, '_').slice(0, 50) + '_' + (i++);
    writeFileSync(
      join(samplesDir, safe + '.json'),
      JSON.stringify(body, null, 2),
      'utf8'
    );
  }

  console.log('Вариантов обработано: %s', byVariant.length);
  console.log('Всего задач (плоский список): %s', tasksFlat.length);
  console.log('Уникальных задач (без дубликатов): %s', allTasksUnique.length);
  console.log('Примеров API сохранено: %s', sampleByUrl.size);
  console.log('Результат: %s', outDir);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
