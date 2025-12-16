#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Re-extract conditions from PDFs in desh/ege2026kp/*.pdf into a clean folder:
  desh/ege2026kp/conditions_regen/<task>/task_<task>_<variant:03d>.txt

This is the "auto-repair" path: it rebuilds all condition files from the source PDFs,
so short/truncated files and inconsistent numbering are eliminated.

Special handling:
  - Tasks 19-21 are extracted from ege1921.pdf (game descriptions). We generate three
    condition files (19/20/21) per variant by combining a standard question template
    with the game description.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple, Dict, Optional

import pdfplumber


BASE = Path("desh/ege2026kp")
OUT = BASE / "conditions_regen"

EXPECTED: Dict[int, int] = {
    1: 195,
    2: 291,
    3: 159,
    4: 95,
    5: 797,
    6: 340,
    7: 186,
    8: 499,
    9: 270,
    10: 329,
    11: 180,
    12: 291,
    13: 250,
    14: 538,
    15: 674,
    16: 298,
    17: 442,
    18: 278,
    19: 151,
    20: 151,
    21: 151,
    22: 210,
    23: 343,
    24: 396,
    25: 375,
    26: 255,
    27: 98,
}


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def extract_lines_from_pdf(pdf_path: Path) -> List[str]:
    lines: List[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            txt = page.extract_text() or ""
            lines.extend(txt.split("\n"))
    return lines


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


def is_variant_start_line(s: str) -> Optional[int]:
    s = s.strip()
    m = re.match(r"^(\d{1,4})\)\s*(.*)$", s)
    if not m:
        return None
    n = int(m.group(1))
    rest = m.group(2)

    # exclude answer-choice lines like "1) 2) 3) 4)"
    if re.match(r"^(?:\d+\)\s*){2,}$", s):
        return None

    # must have some letters, or a long descriptive tail
    if re.search(r"[А-Яа-яA-Za-z]", rest):
        return n
    if len(s) >= 40 and not re.fullmatch(r"[\d\)\(\s\.\,\-–—:;]+", s):
        return n
    return None


def split_variants(lines: List[str]) -> List[Tuple[int, str]]:
    start = find_training_start(lines)
    work = lines[start:]
    starts: List[Tuple[int, int]] = []
    for i, ln in enumerate(work):
        n = is_variant_start_line(ln)
        if n is not None:
            starts.append((n, i))
    # de-dup by first occurrence
    seen = set()
    uniq: List[Tuple[int, int]] = []
    for n, i in starts:
        if n in seen:
            continue
        seen.add(n)
        uniq.append((n, i))
    uniq.sort(key=lambda x: x[1])

    out: List[Tuple[int, str]] = []
    for idx, (n, i0) in enumerate(uniq):
        i1 = uniq[idx + 1][1] if idx + 1 < len(uniq) else len(work)
        chunk = "\n".join(work[i0:i1]).strip()
        if len(chunk) < 50:
            continue
        out.append((n, chunk))
    return out


def write_task_variants(task_num: int, variants: List[Tuple[int, str]]) -> None:
    out_dir = OUT / str(task_num)
    out_dir.mkdir(parents=True, exist_ok=True)
    for v, text in variants:
        fp = out_dir / f"task_{task_num}_{v:03d}.txt"
        fp.write_text(make_header(task_num, v) + text.strip() + "\n", encoding="utf-8")


TASK_19 = (
    "Задание 19.\n"
    "Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.\n"
    "Укажите минимальное значение S, когда такая ситуация возможна.\n"
)
TASK_20 = (
    "Задание 20.\n"
    "Найдите минимальное значение S, при котором у Пети есть выигрышная стратегия, причём\n"
    "одновременно выполняются два условия:\n"
    "− Петя не может выиграть за один ход;\n"
    "− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.\n"
)
TASK_21 = (
    "Задание 21.\n"
    "Найдите два значения S, при которых одновременно выполняются два условия:\n"
    "– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом\n"
    "  при любой игре Пети;\n"
    "– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.\n"
    "Найденные значения запишите в ответе в порядке возрастания.\n"
)


def write_19_21_from_ege1921(pdf_path: Path) -> None:
    lines = extract_lines_from_pdf(pdf_path)
    games = split_variants(lines)
    # games: list of (variant, description)
    for task_num, template in [(19, TASK_19), (20, TASK_20), (21, TASK_21)]:
        out_dir = OUT / str(task_num)
        out_dir.mkdir(parents=True, exist_ok=True)
        for v, game_text in games:
            fp = out_dir / f"task_{task_num}_{v:03d}.txt"
            full = template.strip() + "\n\n" + game_text.strip() + "\n"
            fp.write_text(make_header(task_num, v) + full, encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report_lines: List[str] = []

    # Regular tasks
    for task_num in range(1, 28):
        if task_num in (19, 20, 21):
            continue
        pdf = BASE / f"ege{task_num}.pdf"
        if not pdf.exists():
            report_lines.append(f"{task_num}\tMISSING_PDF\t{pdf}")
            continue
        variants = split_variants(extract_lines_from_pdf(pdf))
        write_task_variants(task_num, variants)
        report_lines.append(f"{task_num}\tEXTRACTED\t{len(variants)}")

    # 19-21
    pdf_1921 = BASE / "ege1921.pdf"
    if pdf_1921.exists():
        lines = extract_lines_from_pdf(pdf_1921)
        games = split_variants(lines)
        report_lines.append(f"1921\tEXTRACTED_GAMES\t{len(games)}")
        write_19_21_from_ege1921(pdf_1921)
    else:
        report_lines.append("1921\tMISSING_PDF\tege1921.pdf")

    # verify counts
    report_lines.append("")
    report_lines.append("VERIFY")
    for task_num, exp in EXPECTED.items():
        d = OUT / str(task_num)
        got = len(list(d.glob("task_*.txt"))) if d.exists() else 0
        status = "OK" if got == exp else "BAD"
        report_lines.append(f"{task_num}\t{status}\tgot={got}\texp={exp}")

    (BASE / "reextract_report.tsv").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    print("Wrote:", BASE / "reextract_report.tsv")


if __name__ == "__main__":
    main()


