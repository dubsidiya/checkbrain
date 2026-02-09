# Скрипты для КЕГЭ (kompege.ru)

Вытягиваем с сайта почти всё: список вариантов, HTML и ответы API по каждому варианту, затем собираем задачи в один объём.

**Не трогаем:** задачи из файлов/папок ege1, ege2, ege3, ege4 и т.п., а также `desh/ege2026kp` — скрипты работают только с `kompege_data/`.

**Важно:** все команды запускать из папки скриптов:

```bash
cd ~/StudioProjects/checkbrain/scripts/kompege
```

После первого раза:

```bash
npm install
npx playwright install
```

---

## Быстрый старт: вытянуть всё подряд

Обновить архив → скачать все варианты → собрать задачи в один объём:

```bash
node pull_everything.js
```

С опциями (например, только 10 вариантов для проверки):

```bash
node pull_everything.js --limit 10
node pull_everything.js --skip-existing   # не перекачивать уже скачанные
```

Результат:
- в корне: `kompege_archive_page.html`, `kompege_variants_list.json`
- `kompege_data/variants/<kim>/` — по каждому варианту: `page.html`, `meta.json`, `responses.json`
- `kompege_data/extracted/` — `variants.json`, `tasks_flat.json`, `api_samples/`

---

## Отдельные шаги

### 1. Обновить список вариантов

Скачивает страницу архива и заново парсит ссылки на варианты:

```bash
node refresh_archive.js
```

Получаешь: `kompege_archive_page.html`, `kompege_variants_list.json` (в корне проекта).

### 2. Скачать данные по всем вариантам

Для каждого варианта из списка открывает страницу и сохраняет HTML и все ответы от kompege.ru:

```bash
node fetch_all_variants.js
node fetch_all_variants.js --limit 5      # только первые 5 (тест)
node fetch_all_variants.js --delay 3000  # пауза 3 сек между запросами
node fetch_all_variants.js --skip-existing
```

Нужен уже созданный `kompege_variants_list.json` (шаг 1 или `parse_archive_html.js`).

Результат: `kompege_data/variants/<kim>/page.html`, `meta.json`, `responses.json`.

### 3. Первая задача с картинкой (HTML по каждому варианту)

Для каждого варианта создаёт `task1.html` — первая задача с отображением картинок (из `text` в API: base64 или ссылки на kompege.ru):

```bash
node export_first_task_html.js
```

Файлы появляются в `kompege_data/variants/<kim>/task1.html`. Открываешь в браузере — видишь условие и ответ.

### 4. Собрать задачи в один объём

Обходит `kompege_data/variants/*`, вытаскивает из `responses.json` структуры с задачами и сводит в общие файлы:

```bash
node extract_all_tasks.js
```

Результат в `kompege_data/extracted/`:
- `variants.json` — по вариантам, с массивом задач
- `tasks_flat.json` — плоский список всех задач (kim, taskNumber, condition, answer, variantTitle)
- `api_samples/` — примеры сырых JSON-ответов API

### 5. Один вариант (отладка)

Скачать только один вариант по `kim`:

```bash
node fetch_variant_data.js 25107025
```

В корне появятся `kompege_variant_25107025.html` и `kompege_variant_25107025_responses.json`.

### 6. Перехват запросов (архив + первый вариант)

Открывает главную → архив → клик по первому варианту, сохраняет HTML и все запросы/ответы:

```bash
node capture.js
```

Файлы: `kompege_archive_page.html`, `kompege_variant_page.html`, `kompege_api_found.json` (в корне).

### 7. Парсинг архива из уже сохранённого HTML

Если архив уже скачан (например через `capture.js` или `refresh_archive.js`), список вариантов можно пересобрать без браузера:

```bash
node parse_archive_html.js
```

Читает `kompege_archive_page.html` в корне, пишет `kompege_variants_list.json`.

---

## Структура после полной выгрузки

```
корень проекта/
  kompege_archive_page.html
  kompege_variants_list.json

  kompege_data/
    variants/
      25107025/
        page.html
        meta.json
        responses.json
      25135392/
        ...
    extracted/
      variants.json
      tasks_flat.json
      api_samples/
        ...
```

---

## Ограничения

- Использование данных КЕГЭ — см. правила сайта и авторские права (задачи К.Ю. Полякова и др.).
- При массовой выгрузке используй `--delay` (например 2500–3000 мс), чтобы не нагружать сервер.
