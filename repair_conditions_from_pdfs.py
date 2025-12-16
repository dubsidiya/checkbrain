#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-repair truncated/too-short condition files by re-extracting the matching variant
from the corresponding source PDF.

For task T (except 19-21), uses:
  desh/ege2026kp/ege{T}.pdf

Strategy:
  - Build a map variant -> (start_line_index, end_line_index) from PDF text,
    using only real variant starts like "187) ..." (must contain letters, not "1) 2) 3) 4)").
  - For each condition file task_T_VVV.txt whose body is shorter than threshold,
    replace its body with the PDF chunk for variant VVV (if found and longer).
  - Always keep header normalized and a single marker line "VVV)" at the top.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import pdfplumber


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
    # exclude answer-choice lines like "1) 2) 3) 4)"
    if re.match(r"^(?:\d+\)\s*){2,}$", s):
        return None
    # must have letters to avoid numeric-only lists
    if re.search(r"[А-Яа-яA-Za-z]", rest):
        return n
    return None


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


def build_variant_chunks(lines: List[str]) -> Dict[int, Tuple[int, int]]:
    start = find_training_start(lines)
    work = lines[start:]
    starts: List[Tuple[int, int]] = []
    for i, ln in enumerate(work):
        n = is_variant_start_line(ln)
        if n is not None:
            starts.append((n, i))
    # Sort by position; keep first occurrence per variant
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


def find_chunk_by_direct_search(lines: List[str], variant: int) -> Optional[str]:
    """
    Fallback extractor: find the first line that starts with f\"{variant})\" and slice
    until the next plausible variant start (any N) that is not an answer-choice line).
    This helps when the start-line heuristic misses some variants.
    """
    pat = re.compile(rf"^\s*{variant}\)\s*")
    start_idx = None
    for i, ln in enumerate(lines):
        if pat.match(ln):
            start_idx = i
            break
    if start_idx is None:
        return None

    next_idx = None
    for j in range(start_idx + 1, len(lines)):
        s = lines[j].strip()
        m = re.match(r"^(\d{1,4})\)\s*.*$", s)
        if not m:
            continue
        if re.match(r"^(?:\d+\)\s*){2,}$", s):
            continue
        n = int(m.group(1))
        if n != variant:
            next_idx = j
            break

    end_idx = next_idx if next_idx is not None else len(lines)
    chunk = "\n".join(lines[start_idx:end_idx]).strip()
    return chunk if len(chunk) >= 50 else None


def main() -> None:
    THRESHOLD = 220
    replaced = 0
    skipped = 0
    missing_pdf = 0
    missing_variant = 0

    pdf_cache: Dict[int, Tuple[List[str], Dict[int, Tuple[int, int]]]] = {}

    for task_dir in sorted([p for p in COND.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        if task_num in (19, 20, 21):
            continue
        pdf_path = BASE / f"ege{task_num}.pdf"
        if not pdf_path.exists():
            missing_pdf += 1
            continue

        for fp in task_dir.glob("task_*.txt"):
            m = FNAME_RE.match(fp.name)
            if not m:
                continue
            var = int(m.group(2))
            text = fp.read_text(encoding="utf-8", errors="replace")
            body = split_header_and_body(text)
            cur_len = len(body.strip())
            if cur_len >= THRESHOLD:
                continue

            if task_num not in pdf_cache:
                lines = extract_lines_from_pdf(pdf_path)
                chunks = build_variant_chunks(lines)
                pdf_cache[task_num] = (lines, chunks)

            lines, chunks = pdf_cache[task_num]
            if var not in chunks:
                # fallback direct search
                chunk_text = find_chunk_by_direct_search(lines, var)
                if not chunk_text:
                    missing_variant += 1
                    continue
            else:
                a, b = chunks[var]
                chunk_text = "\n".join(lines[a:b]).strip()
            if len(chunk_text) <= cur_len:
                skipped += 1
                continue

            new_body = normalize_body(chunk_text, var)
            fp.write_text(make_header(task_num, var) + new_body, encoding="utf-8")
            replaced += 1

    print("=== repair_conditions_from_pdfs ===")
    print("replaced:", replaced)
    print("skipped_not_better:", skipped)
    print("missing_pdf_dirs:", missing_pdf)
    print("missing_variants:", missing_variant)


if __name__ == "__main__":
    main()


