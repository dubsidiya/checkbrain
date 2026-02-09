# checkbrain

kontrol

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
