/**
 * Качает данные вариантов напрямую с API (без браузера):
 *   GET https://kompege.ru/api/v1/variant/kim/<kim>
 * Сохраняет в kompege_data/variants/<kim>/api.json
 *
 * Запуск: node fetch_variants_api.js [--limit N] [--delay MS] [--skip-existing]
 */
import { writeFileSync, readFileSync, mkdirSync, existsSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const rootDir = join(__dirname, '../..');
const variantsDir = join(rootDir, 'kompege_data', 'variants');

const args = process.argv.slice(2);
const limit = args.includes('--limit') ? parseInt(args[args.indexOf('--limit') + 1], 10) : null;
const delayMs = args.includes('--delay') ? parseInt(args[args.indexOf('--delay') + 1], 10) : 800;
const skipExisting = args.includes('--skip-existing');

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function fetchVariant(kim) {
  const url = `https://kompege.ru/api/v1/variant/kim/${kim}`;
  const res = await fetch(url, {
    headers: {
      'Accept': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
      'Referer': 'https://kompege.ru/',
    },
  });
  if (!res.ok) throw new Error(`${res.status}`);
  return res.json();
}

async function main() {
  const listPath = join(rootDir, 'kompege_variants_list.json');
  if (!existsSync(listPath)) {
    console.error('Сначала: node refresh_archive.js');
    process.exit(1);
  }
  let variants = JSON.parse(readFileSync(listPath, 'utf8'));
  if (limit) variants = variants.slice(0, limit);
  console.log('Вариантов: %s, пауза: %s мс', variants.length, delayMs);

  mkdirSync(variantsDir, { recursive: true });
  let ok = 0, skip = 0, err = 0;

  for (let i = 0; i < variants.length; i++) {
    const { kim, title } = variants[i];
    const outDir = join(variantsDir, String(kim));
    const apiPath = join(outDir, 'api.json');
    if (skipExisting && existsSync(apiPath)) {
      skip++;
      process.stdout.write(`\r[${i + 1}/${variants.length}] skip ${kim} ...`);
      await sleep(200);
      continue;
    }
    process.stdout.write(`\r[${i + 1}/${variants.length}] ${kim} ${title.slice(0, 30)}...`);
    try {
      const data = await fetchVariant(kim);
      mkdirSync(outDir, { recursive: true });
      writeFileSync(join(outDir, 'meta.json'), JSON.stringify({ kim, url: `https://kompege.ru/variant?kim=${kim}`, title }, null, 2));
      writeFileSync(apiPath, JSON.stringify(data, null, 2), 'utf8');
      ok++;
    } catch (e) {
      err++;
    }
    await sleep(delayMs);
  }
  console.log('\nГотово. OK: %s, пропущено: %s, ошибок: %s', ok, skip, err);
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
