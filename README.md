# checkbrain

kontrol

## Файл задач КЕГЭ (assets/kompege_tasks.json)

Сборник задач генерируется скриптом и весит ~70 MB. GitHub не рекомендует коммитить файлы >50 MB.

**Варианты:**

1. **Не коммитить большой файл**  
   В репозитории держать плейсхолдер (пустой массив). После клонирования запустить:
   ```bash
   cd scripts/kompege && node extract_all_tasks.js
   ```
   Чтобы не запушить 70 MB случайно, перед коммитом откатить файл:
   ```bash
   git checkout -- assets/kompege_tasks.json
   ```

2. **Хранить в Git LFS**  
   [Настройка Git LFS](https://git-lfs.github.com/) для `assets/kompege_tasks.json`, затем закоммитить файл через LFS.

**Чтобы убрать большой файл из истории и держать в репо только плейсхолдер:**
```bash
echo '[]' > assets/kompege_tasks.json
git add assets/kompege_tasks.json
git commit -m "chore: replace kompege_tasks.json with placeholder"
git push
```
После этого приложение соберётся с пустым списком задач; полный список создаётся скриптом `extract_all_tasks.js` локально.

## Деплой на Vercel (Flutter Web)

В репозитории есть `vercel.json`: при подключении проекта к Vercel сборка выполняется на стороне Vercel.

1. Залей проект в GitHub (без папки `build/web` — её можно не коммитить).
2. В [Vercel](https://vercel.com) → **Add New Project** → импортируй репозиторий.
3. Параметры подхватятся из `vercel.json`:
   - **Install:** клонируется Flutter stable, включается web, выполняется `flutter pub get`.
   - **Build:** `flutter build web --release`.
   - **Output:** `build/web`.
4. После каждого пуша в ветку по умолчанию Vercel сам запускает сборку и деплой.

Первый деплой может занять 5–10 минут (установка Flutter). Дальнейшие — быстрее за счёт кэша.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
