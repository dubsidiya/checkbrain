/**
 * Полный цикл выгрузки с КЕГЭ:
 * 1) Обновить архив и список вариантов (refresh_archive.js)
 * 2) Скачать данные по всем вариантам (fetch_all_variants.js)
 * 3) Собрать задачи в один объём (extract_all_tasks.js)
 *
 * Запуск:
 *   node pull_everything.js           # полная выгрузка (все варианты, пауза 2.5 с)
 *   node pull_everything.js --limit 5 # только 5 вариантов (для проверки)
 *   node pull_everything.js --skip-existing  # не качать заново уже скачанные
 */
import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const scriptsDir = __dirname;

function run(cmd, args = []) {
  return new Promise((resolve, reject) => {
    const c = spawn(cmd, args, {
      cwd: scriptsDir,
      stdio: 'inherit',
      shell: true,
    });
    c.on('close', code => (code === 0 ? resolve() : reject(new Error(`exit ${code}`))));
  });
}

async function main() {
  const args = process.argv.slice(2);
  console.log('1/3 Обновление архива и списка вариантов...');
  await run('node', ['refresh_archive.js']);

  console.log('\n2/3 Скачивание данных по вариантам...');
  await run('node', ['fetch_all_variants.js', ...args]);

  console.log('\n3/3 Сбор задач в один объём...');
  await run('node', ['extract_all_tasks.js']);

  console.log('\nГотово. Результаты в kompege_data/ и компеге_*.json в корне проекта.');
}

main().catch(e => {
  console.error(e);
  process.exit(1);
});
