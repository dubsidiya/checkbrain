#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR-based auto-repair for remaining short conditions.

Input: conditions_short_remaining.tsv (generated earlier)
Output: overwrites corresponding files in desh/ege2026kp/conditions/<task>/task_<task>_<variant:03d>.txt
        when OCR extraction produces a longer body.

Approach:
  - Use pdfplumber to get page count for ege{task}.pdf
  - Predict page ~ page_count * (variant / expected_count)
  - OCR a small window around predicted page (default +/-10) using:
      pdftoppm -f N -l N -png PDF outprefix
      tesseract out.png stdout -l rus+eng --psm 6
  - Find line starting with "{variant})" and extract until next variant start on same page.
  - Replace file if extracted chunk is longer than current body.

This avoids OCR scanning the whole PDF for tasks with hundreds of variants.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import subprocess
import time
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"
SHORT_LIST = Path("conditions_short_remaining.tsv")
TMP = Path(".tmp_ocr_pages")

EXPECTED: Dict[int, int] = {
    1: 195, 2: 291, 3: 159, 4: 95, 5: 797, 6: 340, 7: 186, 8: 499, 9: 270,
    10: 329, 11: 180, 12: 291, 13: 250, 14: 538, 15: 674, 16: 298, 17: 442, 18: 278,
    19: 151, 20: 151, 21: 151, 22: 210, 23: 343, 24: 396, 25: 375, 26: 255, 27: 98,
}

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


def ocr_page(pdf: Path, page_1based: int) -> str:
    TMP.mkdir(parents=True, exist_ok=True)
    prefix = TMP / "p"
    # pdftoppm outputs p-XX.png
    subprocess.run(
        ["pdftoppm", "-f", str(page_1based), "-l", str(page_1based), "-png", str(pdf), str(prefix)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    img = TMP / f"p-{page_1based:02d}.png"
    if not img.exists():
        # poppler sometimes pads with 3 digits for large docs; try glob
        matches = sorted(TMP.glob(f"p-{page_1based:02d}*.png"))
        if matches:
            img = matches[0]
    res = subprocess.run(
        ["tesseract", str(img), "stdout", "-l", "rus+eng", "--psm", "6"],
        capture_output=True,
        text=True,
        check=False,
    )
    return res.stdout or ""


def extract_variant_chunk_from_ocr(ocr_text: str, variant: int) -> Optional[str]:
    lines = ocr_text.splitlines()
    start = None
    pat = re.compile(rf"^\s*{variant}\)\s*")
    for i, ln in enumerate(lines):
        if pat.match(ln):
            start = i
            break
    if start is None:
        return None
    end = None
    for j in range(start + 1, len(lines)):
        n = is_variant_start_line(lines[j])
        if n is not None and n != variant:
            end = j
            break
    chunk = "\n".join(lines[start:end]).strip()
    if len(chunk) < 80:
        return None
    return chunk


def predicted_page(page_count: int, variant: int, expected_cnt: int) -> int:
    # 1..page_count
    if expected_cnt <= 0:
        return max(1, min(page_count, 1))
    frac = max(0.0, min(1.0, variant / float(expected_cnt)))
    p = int(round(frac * page_count))
    return max(1, min(page_count, p))


def read_short_list() -> Dict[int, Set[int]]:
    tasks: Dict[int, Set[int]] = {}
    with SHORT_LIST.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            t = int(row["task"])
            name = row["file"]
            m = FNAME_RE.match(name)
            if not m:
                continue
            v = int(m.group(2))
            tasks.setdefault(t, set()).add(v)
    return tasks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max", type=int, default=0, help="Max variants to process (0 = all)")
    ap.add_argument("--task", type=int, default=0, help="Only process one task number (0 = all)")
    ap.add_argument("--min-body", type=int, default=220, help="Only try to repair files with body shorter than this")
    ap.add_argument("--window", type=int, default=10, help="Initial +/- page window around predicted page")
    ap.add_argument("--steps", type=int, default=4, help="How many times to expand the window (window doubles each step)")
    ap.add_argument("--sleep", type=float, default=0.0, help="Optional sleep between OCR pages (seconds)")
    args = ap.parse_args()

    if not SHORT_LIST.exists():
        raise SystemExit(f"Missing {SHORT_LIST}")

    tasks = read_short_list()
    if args.task:
        tasks = {args.task: tasks.get(args.task, set())}

    total_targets = sum(len(vs) for vs in tasks.values())
    print("targets:", total_targets, "tasks:", len(tasks), "filter_task:", args.task or "ALL")

    replaced = 0
    not_found = 0
    errors = 0
    processed = 0

    # Cache OCR text per (pdf, page) so we never OCR the same page twice in one run
    ocr_cache: "OrderedDict[Tuple[str,int], str]" = OrderedDict()
    OCR_CACHE_LIMIT = 120  # pages

    for task_num, variants in sorted(tasks.items()):
        if task_num in (19, 20, 21):
            continue
        pdf = BASE / f"ege{task_num}.pdf"
        if not pdf.exists():
            print("missing pdf for task", task_num)
            continue

        expected_cnt = EXPECTED.get(task_num, 0)
        # cheap page count via pdfinfo-like call would be faster, but keep it simple:
        import pdfplumber
        with pdfplumber.open(str(pdf)) as pdfdoc:
            page_count = len(pdfdoc.pages)

        # Process each variant independently (but using predicted window)
        for v in sorted(variants):
            if args.max and processed >= args.max:
                break
            fp = COND / str(task_num) / f"task_{task_num}_{v:03d}.txt"
            if not fp.exists():
                continue
            cur_text = fp.read_text(encoding="utf-8", errors="replace")
            cur_body = split_header_and_body(cur_text)
            cur_len = len(cur_body.strip())

            if cur_len >= args.min_body:
                continue

            center = predicted_page(page_count, v, expected_cnt)
            window = args.window
            found_chunk = None

            # Expand window a few times
            for step in range(args.steps):
                p0 = max(1, center - window)
                p1 = min(page_count, center + window)
                for page in range(p0, p1 + 1):
                    try:
                        key = (str(pdf), page)
                        if key in ocr_cache:
                            ocr_text = ocr_cache[key]
                            # touch
                            ocr_cache.move_to_end(key)
                        else:
                            ocr_text = ocr_page(pdf, page)
                            ocr_cache[key] = ocr_text
                            if len(ocr_cache) > OCR_CACHE_LIMIT:
                                ocr_cache.popitem(last=False)
                    except Exception:
                        errors += 1
                        continue
                    chunk = extract_variant_chunk_from_ocr(ocr_text, v)
                    if chunk:
                        found_chunk = chunk
                        break
                    if args.sleep:
                        time.sleep(args.sleep)
                if found_chunk:
                    break
                window *= 2

            if not found_chunk:
                not_found += 1
                processed += 1
                continue

            new_body = normalize_body(found_chunk, v)
            if len(new_body.strip()) <= cur_len:
                processed += 1
                continue
            fp.write_text(make_header(task_num, v) + new_body, encoding="utf-8")
            replaced += 1
            processed += 1
            if processed % 25 == 0:
                print(f"progress processed={processed} replaced={replaced} not_found={not_found} errors={errors}", flush=True)

        # cleanup images to keep workspace small
        if TMP.exists():
            for img in TMP.glob("*.png"):
                try:
                    img.unlink()
                except Exception:
                    pass

        if args.max and processed >= args.max:
            break

    print("=== ocr_repair_remaining_conditions ===")
    print("replaced:", replaced)
    print("not_found:", not_found)
    print("errors:", errors)
    print("processed:", processed)


if __name__ == "__main__":
    main()


