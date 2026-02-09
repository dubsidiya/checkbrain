#!/usr/bin/env python3
"""
Скрипт для поиска API КЕГЭ (kompege.ru).
Открывает сайт в браузере, переходит в архив и перехватывает сетевые запросы (XHR/fetch).
Результат: список URL и, по возможности, примеры ответов — в kompege_api_found.json.
"""
import json
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Установите Playwright: pip install playwright && playwright install chromium")
    sys.exit(1)

OUTPUT_FILE = Path(__file__).resolve().parent / "kompege_api_found.json"


def main():
    captured = {
        "requests": [],   # { "url": str, "method": str, "post_data": str|None }
        "responses": [],  # { "url": str, "status": int, "body_preview": str }
    }

    def on_request(request):
        url = request.url
        if any(skip in url for skip in ("google", "yandex", "vk.com", ".js", ".css", ".png", ".woff", "favicon")):
            return
        captured["requests"].append({
            "url": url,
            "method": request.method,
            "post_data": request.post_data if request.post_data else None,
        })

    def on_response(response):
        url = response.url
        if any(skip in url for skip in ("google", "yandex", "vk.com", ".js", ".css", ".png", ".woff", "favicon")):
            return
        try:
            body = response.text()
            preview = body[:2000] if body else ""
            if len(body or "") > 2000:
                preview += "\n... [truncated]"
            captured["responses"].append({
                "url": url,
                "status": response.status,
                "body_preview": preview,
            })
        except Exception as e:
            captured["responses"].append({
                "url": url,
                "status": response.status,
                "body_preview": f"[could not read body: {e}]",
            })

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        )
        context.set_default_timeout(25000)
        page = context.new_page()
        page.on("request", on_request)
        page.on("response", on_response)

        try:
            print("Открываю https://kompege.ru/ ...")
            page.goto("https://kompege.ru/", wait_until="networkidle")
            print("Главная загружена.")

            print("Переход в архив...")
            page.goto("https://kompege.ru/archive", wait_until="networkidle")
            print("Архив загружен.")

            # Ждём появления контента (список вариантов)
            page.wait_for_timeout(3000)

            # Попробуем кликнуть по первому варианту, если есть — поймаем запрос за задачей
            try:
                first_variant = page.locator("a[href*='variant'], a[href*='archive'], [class*='variant'], button").first
                if first_variant.count() > 0:
                    first_variant.click()
                    page.wait_for_timeout(3000)
            except Exception:
                pass

        except Exception as e:
            print(f"Ошибка навигации: {e}")
        finally:
            browser.close()

    # Убираем дубли по URL в responses (оставляем последний)
    seen = set()
    unique_responses = []
    for r in reversed(captured["responses"]):
        key = r["url"]
        if key not in seen:
            seen.add(key)
            unique_responses.append(r)
    captured["responses"] = list(reversed(unique_responses))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(captured, f, ensure_ascii=False, indent=2)

    print(f"\nСохранено в {OUTPUT_FILE}")
    print("\n--- Запросы (без статики) ---")
    for r in captured["requests"]:
        print(r["method"], r["url"][:100])
    print("\n--- Ответы с телом ---")
    for r in captured["responses"]:
        print(r["status"], r["url"][:80])
        if r.get("body_preview") and r["body_preview"] != "[could not read body: ...]":
            print("  preview:", r["body_preview"][:200].replace("\n", " ") + "...")


if __name__ == "__main__":
    main()
