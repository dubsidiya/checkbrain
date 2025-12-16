#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild tasks 19/20/21 conditions so that each variant produces:
  - task_19_V.txt: common game statement + ONLY question block "Задание 19"
  - task_20_V.txt: common game statement + ONLY question block "Задание 20"
  - task_21_V.txt: common game statement + ONLY question block "Задание 21"

Why: some extracted files contain only the statement (or only a part) and are missing
their own question block. The true structure is one game description + 3 questions.

Sources:
  - desh/ege2026kp/conditions/{19,20,21}/*.txt
  - desh/ege2026kp/conditions_dups/{19,20,21}/*.txt (used as extra sources)

We search for "combined" sources that contain ALL three question labels (19/20/21),
pick the longest per variant, split it, then write results into conditions/19..21.
We only overwrite an existing output file if:
  - it is missing its label, OR
  - the newly generated content is longer.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"
DUPS = BASE / "conditions_dups"

FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")
HEADER_RE = re.compile(r"Задача\\s*№\\s*(\\d+).*?вариант\\s*(\\d+)", re.IGNORECASE)


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\\n" + ("=" * 50) + "\\n\\n"


def split_header_and_body(text: str) -> List[str]:
    lines = text.splitlines()
    if len(lines) >= 2 and lines[0].startswith("Задача") and set(lines[1].strip()) == {"="}:
        body = lines[2:]
        if body and body[0].strip() == "":
            body = body[1:]
        return body
    return lines


def marker_line_variant(line: str) -> Optional[Tuple[int, str]]:
    s = line.strip()
    m = re.match(r"^(\\d{1,4})\\)\\s*(.*)$", s)
    if not m:
        return None
    return int(m.group(1)), m.group(2)


def is_meaningful_marker(rest: str) -> bool:
    return bool(re.search(r"[А-Яа-яA-Za-z]", rest))


def first_meaningful_marker(body_lines: List[str], max_scan: int = 120) -> Optional[Tuple[int, int]]:
    non_empty = 0
    for idx, ln in enumerate(body_lines):
        s = ln.strip()
        if not s:
            continue
        non_empty += 1
        if set(s) in ({"="}, {"-"}, {"_"}):
            continue
        mv = marker_line_variant(s)
        if mv:
            v, rest = mv
            if len(re.findall(r"\\b\\d{1,4}\\)", s)) >= 3:
                continue
            if is_meaningful_marker(rest):
                return idx, v
        if non_empty >= max_scan:
            break
    return None


def contains_all_labels(text: str) -> bool:
    return (
        re.search(r"\\bЗадание\\s*19\\b", text, re.IGNORECASE)
        and re.search(r"\\bЗадание\\s*20\\b", text, re.IGNORECASE)
        and re.search(r"\\bЗадание\\s*21\\b", text, re.IGNORECASE)
    )


def split_1921(body_lines: List[str]) -> Optional[Tuple[int, Dict[int, List[str]]]]:
    txt = "\\n".join(body_lines)
    if not contains_all_labels(txt):
        return None

    rv = first_meaningful_marker(body_lines)
    if rv is None:
        return None
    start_idx, variant = rv

    def find_idx(pat: str) -> Optional[int]:
        rx = re.compile(pat, re.IGNORECASE)
        for i, ln in enumerate(body_lines):
            if rx.search(ln):
                return i
        return None

    i19 = find_idx(r"\\bЗадание\\s*19\\b")
    i20 = find_idx(r"\\bЗадание\\s*20\\b")
    i21 = find_idx(r"\\bЗадание\\s*21\\b")
    if i19 is None or i20 is None or i21 is None:
        return None

    # common statement from real marker to just before 'Задание 19'
    statement = body_lines[start_idx:i19]
    block19 = body_lines[i19:i20]
    block20 = body_lines[i20:i21]
    block21 = body_lines[i21:]

    return variant, {19: statement + block19, 20: statement + block20, 21: statement + block21}


@dataclass
class CombinedSource:
    path: Path
    variant: int
    body_lines: List[str]
    body_len: int


def iter_sources() -> List[Path]:
    srcs: List[Path] = []
    for root in (COND, DUPS):
        for t in (19, 20, 21):
            d = root / str(t)
            if d.exists():
                srcs.extend(sorted(d.glob("task_*.txt")))
    return srcs


def parse_variant_from_filename(fp: Path) -> Optional[int]:
    m = FNAME_RE.match(fp.name)
    if not m:
        return None
    return int(m.group(2))


def best_combined_sources() -> Dict[int, CombinedSource]:
    best: Dict[int, CombinedSource] = {}
    for fp in iter_sources():
        txt = fp.read_text(encoding="utf-8", errors="replace")
        body_lines = split_header_and_body(txt)
        split = split_1921(body_lines)
        if not split:
            continue
        variant, _ = split
        blen = len("\\n".join(body_lines).strip())
        cur = best.get(variant)
        if cur is None or blen > cur.body_len:
            best[variant] = CombinedSource(fp, variant, body_lines, blen)
    return best


def output_needs_update(out_fp: Path, task_num: int, new_text: str) -> bool:
    if not out_fp.exists():
        return True
    old = out_fp.read_text(encoding="utf-8", errors="replace")
    # must contain its label
    if not re.search(rf"\\bЗадание\\s*{task_num}\\b", old, re.IGNORECASE):
        return True
    return len(new_text.strip()) > len(old.strip())


def write_out(task_num: int, variant: int, body_lines: List[str], dry_run: bool) -> bool:
    out_dir = COND / str(task_num)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_fp = out_dir / f"task_{task_num}_{variant:03d}.txt"
    new_text = make_header(task_num, variant) + ("\\n".join(body_lines).rstrip() + "\\n")
    if output_needs_update(out_fp, task_num, new_text):
        if not dry_run:
            out_fp.write_text(new_text, encoding="utf-8")
        return True
    return False


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    best = best_combined_sources()
    updated = 0
    missing = 0

    for variant, src in sorted(best.items(), key=lambda kv: kv[0]):
        split = split_1921(src.body_lines)
        if not split:
            missing += 1
            continue
        v2, parts = split
        if v2 != variant:
            # should not happen, but be safe
            variant = v2
        for t in (19, 20, 21):
            if write_out(t, variant, parts[t], args.dry_run):
                updated += 1

    print("=== rebuild_1921_conditions ===")
    print("combined_variants_found:", len(best))
    print("files_updated:", updated)
    print("split_failed:", missing)


if __name__ == "__main__":
    main()


