#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Second-stage auto-repair: if PDF text extraction is still too short (tables/images),
try extracting from the original .doc files using antiword, and replace the condition
if we can get a longer chunk for the same variant number.
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
    if re.match(r"^(?:\d+\)\s*){2,}$", s):
        return None
    if re.search(r"[А-Яа-яA-Za-z]", rest):
        return n
    return None


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


def extract_lines_from_doc(doc_path: Path) -> List[str]:
    # antiword outputs cp1251-ish sometimes; we decode permissively
    res = subprocess.run(
        ["antiword", str(doc_path)],
        capture_output=True,
        check=False,
    )
    data = res.stdout
    # try utf-8 then cp1251
    for enc in ("utf-8", "cp1251"):
        try:
            text = data.decode(enc)
            break
        except Exception:
            text = None
    if text is None:
        text = data.decode("utf-8", errors="replace")
    return text.splitlines()


def build_variant_chunks(lines: List[str]) -> Dict[int, Tuple[int, int]]:
    start = find_training_start(lines)
    work = lines[start:]
    starts: List[Tuple[int, int]] = []
    for i, ln in enumerate(work):
        n = is_variant_start_line(ln)
        if n is not None:
            starts.append((n, i))
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


def main() -> None:
    THRESHOLD = 220
    replaced = 0
    missing_doc = 0
    missing_variant = 0
    skipped = 0

    cache: Dict[int, Tuple[List[str], Dict[int, Tuple[int, int]]]] = {}

    for task_dir in sorted([p for p in COND.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        doc_path = BASE / (f"ege{task_num}.doc" if task_num not in (19, 20, 21) else "ege1921.doc")
        if not doc_path.exists():
            missing_doc += 1
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

            if task_num not in cache:
                lines = extract_lines_from_doc(doc_path)
                chunks = build_variant_chunks(lines)
                cache[task_num] = (lines, chunks)

            lines, chunks = cache[task_num]
            if var not in chunks:
                missing_variant += 1
                continue
            a, b = chunks[var]
            chunk_text = "\n".join(lines[a:b]).strip()
            if len(chunk_text) <= cur_len:
                skipped += 1
                continue

            new_body = normalize_body(chunk_text, var)
            fp.write_text(make_header(task_num, var) + new_body, encoding="utf-8")
            replaced += 1

    print("=== repair_conditions_from_docs ===")
    print("replaced:", replaced)
    print("skipped_not_better:", skipped)
    print("missing_doc_dirs:", missing_doc)
    print("missing_variants:", missing_variant)


if __name__ == "__main__":
    main()


