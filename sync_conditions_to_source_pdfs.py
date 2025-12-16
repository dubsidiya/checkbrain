#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sync conditions/* to what's actually present in source PDFs.

Problem: after various extractions/renames, some tasks now contain variants that
do not exist in the corresponding source PDF (e.g. task 5 > 412).
This script:
  - parses each ege{task}.pdf to detect which variant numbers exist
  - moves condition files whose variant is NOT present in the PDF into
    desh/ege2026kp/conditions_out_of_source/<task>/
  - (optional) can regenerate missing variants from the PDF later (not implemented here)

Heuristic for detecting a variant start line in PDF text:
  - line starts with N) (N is 1..4 digits)
  - NOT a multiple-choice options line (lines with many occurrences of '\\d+)' in one line)
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pdfplumber


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"
OUT = BASE / "conditions_out_of_source"

FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")


def extract_lines(pdf: Path) -> List[str]:
    lines: List[str] = []
    with pdfplumber.open(str(pdf)) as doc:
        for page in doc.pages:
            txt = page.extract_text() or ""
            lines.extend(txt.split("\n"))
    return lines


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


def is_variant_start_line(line: str) -> Optional[int]:
    s = line.strip()
    m = re.match(r"^(\d{1,4})\)\s*(.*)$", s)
    if not m:
        return None
    n = int(m.group(1))
    rest = m.group(2)

    # Exclude typical answer-choice lines: "1) ... 2) ... 3) ... 4) ..."
    # Count how many markers like 'number)' exist in the same line.
    markers = re.findall(r"\b\d{1,4}\)", s)
    if len(markers) >= 3:
        return None

    # Must contain letters in the remainder to be a real statement line
    if not re.search(r"[А-Яа-яA-Za-z]", rest):
        return None

    return n


def variants_in_pdf(task_num: int) -> Set[int]:
    pdf = BASE / (f"ege{task_num}.pdf" if task_num not in (19, 20, 21) else "ege1921.pdf")
    if not pdf.exists():
        return set()
    lines = extract_lines(pdf)
    start = find_training_start(lines)
    seen: Set[int] = set()
    for ln in lines[start:]:
        n = is_variant_start_line(ln)
        if n is not None:
            seen.add(n)
    return seen


def main() -> None:
    moved = 0
    scanned = 0
    per_task: Dict[int, Tuple[int, int]] = {}  # task -> (seen_count, moved_count)

    for task_dir in sorted([p for p in COND.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        seen = variants_in_pdf(task_num)
        if not seen:
            continue

        moved_task = 0
        for fp in task_dir.glob("task_*.txt"):
            m = FNAME_RE.match(fp.name)
            if not m:
                continue
            scanned += 1
            v = int(m.group(2))
            if v not in seen:
                out_dir = OUT / str(task_num)
                out_dir.mkdir(parents=True, exist_ok=True)
                target = out_dir / fp.name
                k = 1
                while target.exists():
                    target = out_dir / f"{fp.stem}.x{k}{fp.suffix}"
                    k += 1
                shutil.move(str(fp), str(target))
                moved += 1
                moved_task += 1

        per_task[task_num] = (len(seen), moved_task)

    print("=== sync_conditions_to_source_pdfs ===")
    print("files_scanned:", scanned)
    print("moved_out_of_source:", moved)
    for t in sorted(per_task):
        seen_cnt, moved_cnt = per_task[t]
        if moved_cnt:
            print(f"task {t}: pdf_variants={seen_cnt} moved={moved_cnt}")


if __name__ == "__main__":
    main()


