#!/usr/bin/env python3
"""
Нормализация папок desh/ege2026kp/conditions/N для задач,
в которых каждая задача в исходном файле имеет собственный
книжный номер вида 'k)' и этот номер должен совпадать с номером варианта.

Для таких задач (например, 8, 17, 23):
  - Берём все существующие task_N_XXX.txt,
  - Находим внутри каждой первый 'k)' в начале строки,
  - Группируем по k (если есть дубликаты – берём первый вариант),
  - Пересоздаём файлы строго как task_N_{k:03d}.txt
    с заголовком 'Задача №N (вариант k)' и телом, начинающимся с строки 'k) ...'.

В результате:
  - количество файлов = количеству уникальных внутренних номеров;
  - имя файла, номер варианта в заголовке и первый номер в условии совпадают.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple

BASE_DIR = Path(__file__).parent / "desh" / "ege2026kp" / "conditions"


def extract_internal_blocks(task_dir: Path) -> Dict[int, str]:
    """
    Читает все task_*.txt в task_dir и вытаскивает:
      - первый номер вида 'k)' в начале строки;
      - текст задачи начиная с этой строки до конца файла.
    Возвращает словарь {k: text}. При конфликте по k берётся первый встретившийся.
    """
    blocks: Dict[int, str] = {}

    for path in sorted(task_dir.glob("task_*.txt")):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  ⚠️  Не удалось прочитать {path}: {e}")
            continue

        lines = text.splitlines()
        internal_num = None
        body_start = 0

        for idx, line in enumerate(lines):
            m = re.match(r"^(\d+)\)\s+", line.strip())
            if m:
                internal_num = int(m.group(1))
                body_start = idx
                break

        if internal_num is None:
            # Нет явного номера — такую задачу пропускаем
            continue

        body = "\n".join(lines[body_start:]).strip()
        if not body:
            continue

        if internal_num not in blocks:
            blocks[inernal_num := internal_num] = body

    return blocks


def normalize_task(task_number: int) -> None:
    task_dir = BASE_DIR / str(task_number)
    if not task_dir.exists():
        print(f"❌ Папка с условиями для задачи №{task_number} не найдена: {task_dir}")
        return

    blocks = extract_internal_blocks(task_dir)
    if not blocks:
        print(f"⚠️  Не удалось найти внутренние номера в задачах №{task_number}")
        return

    internal_nums = sorted(blocks.keys())
    print(
        f"Задача №{task_number}: найдено {len(blocks)} уникальных внутренних номеров "
        f"от {internal_nums[0]} до {internal_nums[-1]}"
    )

    # Пересоздаём файлы: удаляем старые task_*.txt
    for path in task_dir.glob("task_*.txt"):
        try:
            path.unlink()
        except Exception as e:
            print(f"  ⚠️  Не удалось удалить {path}: {e}")

    # Создаём по одному файлу на каждый внутренний номер
    for internal_num in internal_nums:
        body = blocks[internal_num]
        new_path = task_dir / f"task_{task_number}_{internal_num:03d}.txt"
        try:
            with new_path.open("w", encoding="utf-8") as f:
                f.write(f"Задача №{task_number} (вариант {internal_num})\n")
                f.write("=" * 50 + "\n\n")
                f.write(body)
                if not body.endswith("\n"):
                    f.write("\n")
        except Exception as e:
            print(f"  ❌ Ошибка при записи {new_path}: {e}")

    print(f"✅ Задача №{task_number}: файлов пересоздано: {len(internal_nums)}")


def main() -> None:
    # Номера задач, где внутренний номер явно однозначен и должен совпадать с вариантом
    # (по текущему анализу: 8, 17, 23; при необходимости список можно расширить).
    for n in (8, 17, 23):
        print("=" * 60)
        normalize_task(n)


if __name__ == "__main__":
    main()


