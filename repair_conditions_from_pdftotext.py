#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fast auto-repair using poppler `pdftotext -layout`.

Why: OCR is slow. `pdftotext` is much faster and often preserves tables better than pdfplumber.

Repairs:
  - For each task T (except 19-21) use desh/ege2026kp/ege{T}.pdf
  - Convert whole PDF to text once (layout mode)
  - Split into variants by lines starting with "NNN)" that contain letters
    (skip answer-choice lines like "1) 2) 3) 4)")
  - Replace condition files whose body is shorter than threshold if we can extract
    a longer chunk for the same variant number.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple, Optional


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"

FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def split_header_and_body(text: str) -> str:
    lines = text.splitlines()
    if len(lines) >= 2 and lines[0].startswith("Задача") and set(lines[1].strip()) == {"="}:
        body = lines[2:]
        if body and body[0].strip() == "":
            body = body[1:]
        return "\n".join(body).rstrip() + "\n"
    return text.rstrip() + "\n"


def normalize_body(body: str, variant: int) -> str:
    lines = body.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    marker = f"{variant})"
    j = i
    while j < len(lines) and lines[j].strip() == marker:
        j += 1
    new_lines = lines[:i] + [marker] + lines[j:]
    return "\n".join(new_lines).rstrip() + "\n"


def is_variant_start_line(s: str) -> Optional[int]:
    s = s.strip()
    m = re.match(r"^(\d{1,4})\)\s*(.*)$", s)
    if not m:
        return None
    n = int(m.group(1))
    rest = m.group(2)
    # skip answer-choice lines "1) 2) 3) 4)"
    if re.match(r"^(?:\d+\)\s*){2,}$", s):
        return None
    # require letters to avoid numeric-only lists
    if re.search(r"[А-Яа-яA-Za-z]", rest):
        return n
    return None


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


def build_variant_chunks(lines: List[str]) -> Dict[int, Tuple[int, int]]:
    start = find_training_start(lines)
    work = lines[start:]
    starts: List[Tuple[int, int]] = []
    for i, ln in enumerate(work):
        n = is_variant_start_line(ln)
        if n is not None:
            starts.append((n, i))
    # keep first occurrence per variant number
    seen = set()
    uniq: List[Tuple[int, int]] = []
    for n, i in sorted(starts, key=lambda x: x[1]):
        if n in seen:
            continue
        seen.add(n)
        uniq.append((n, i))
    uniq.sort(key=lambda x: x[1])
    chunks: Dict[int, Tuple[int, int]] = {}
    for idx, (n, i0) in enumerate(uniq):
        i1 = uniq[idx + 1][1] if idx + 1 < len(uniq) else len(work)
        chunks[n] = (start + i0, start + i1)
    return chunks


def pdftotext_lines(pdf: Path) -> List[str]:
    # output to stdout
    res = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        capture_output=True,
        check=False,
    )
    data = res.stdout
    # try utf-8, fallback to cp1251
    for enc in ("utf-8", "cp1251"):
        try:
            txt = data.decode(enc)
            break
        except Exception:
            txt = None
    if txt is None:
        txt = data.decode("utf-8", errors="replace")
    return txt.splitlines()


def main() -> None:
    THRESHOLD = 220
    replaced = 0
    missing_variant = 0
    skipped = 0
    pdf_missing = 0

    cache: Dict[int, Tuple[List[str], Dict[int, Tuple[int, int]]]] = {}

    for task_dir in sorted([p for p in COND.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        if task_num in (19, 20, 21):
            continue
        pdf = BASE / f"ege{task_num}.pdf"
        if not pdf.exists():
            pdf_missing += 1
            continue
        if task_num not in cache:
            lines = pdftotext_lines(pdf)
            chunks = build_variant_chunks(lines)
            cache[task_num] = (lines, chunks)

        lines, chunks = cache[task_num]

        for fp in task_dir.glob("task_*.txt"):
            m = FNAME_RE.match(fp.name)
            if not m:
                continue
            var = int(m.group(2))
            cur_text = fp.read_text(encoding="utf-8", errors="replace")
            cur_body = split_header_and_body(cur_text)
            cur_len = len(cur_body.strip())
            if cur_len >= THRESHOLD:
                continue
            if var not in chunks:
                missing_variant += 1
                continue
            a, b = chunks[var]
            chunk = "\n".join(lines[a:b]).strip()
            if len(chunk) <= cur_len:
                skipped += 1
                continue
            new_body = normalize_body(chunk, var)
            fp.write_text(make_header(task_num, var) + new_body, encoding="utf-8")
            replaced += 1

    print("=== repair_conditions_from_pdftotext ===")
    print("replaced:", replaced)
    print("skipped_not_better:", skipped)
    print("missing_variants:", missing_variant)
    print("missing_pdfs:", pdf_missing)


if __name__ == "__main__":
    main()


