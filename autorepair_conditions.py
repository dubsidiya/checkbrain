#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-repair extracted conditions after aggressive normalization:

Goal (per user's rule):
  - The file name variant, header variant, and the *first marker line* in the body
    must match, for ALL tasks.

What we do:
  1) Merge files back from desh/ege2026kp/conditions_dups/<task>/ into
     desh/ege2026kp/conditions/<task>/ by filename variant.
     - If destination is missing -> move back.
     - If destination exists -> keep the 'better' file (longer body), move the other to dups.
  2) For every file in conditions/<task>/:
     - rewrite header to "Задача №N (вариант V)" + separator
     - ensure exactly ONE marker line "V)" at the beginning of the body (after header)
       (remove duplicates if multiple)

This restores counts and fixes the "looks like missing text" cases where a short
placeholder stayed in main while the full text was moved to conditions_dups.
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Optional, Dict, List


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"
DUPS = BASE / "conditions_dups"

FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")
HEADER_RE = re.compile(r"Задача\s*№\s*(\d+).*?вариант\s*(\d+)", re.IGNORECASE)

# User-provided expected counts (unique variants per task)
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


def split_header_and_body(text: str) -> Tuple[str, str]:
    lines = text.splitlines()
    if len(lines) >= 2 and lines[0].startswith("Задача") and set(lines[1].strip()) == {"="}:
        body_lines = lines[2:]
        if body_lines and body_lines[0].strip() == "":
            body_lines = body_lines[1:]
        return "\n".join(lines[:2]) + "\n", "\n".join(body_lines).rstrip() + "\n"
    return "", text.rstrip() + "\n"


def body_len(text: str) -> int:
    _, body = split_header_and_body(text)
    return len(body.strip())


def normalize_body(body: str, variant: int) -> str:
    """Ensure exactly one marker line 'V)' at top of body (after trimming leading blanks)."""
    lines = body.splitlines()

    # remove leading blank lines
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    marker = f"{variant})"

    # count consecutive marker lines
    j = i
    while j < len(lines) and lines[j].strip() == marker:
        j += 1
    marker_count = j - i

    new_lines = lines[:i]
    new_lines.append(marker)
    # skip all existing marker duplicates
    new_lines.extend(lines[j:])

    return "\n".join(new_lines).rstrip() + "\n"


def rewrite_file(fp: Path, task_num: int, variant: int) -> None:
    text = fp.read_text(encoding="utf-8", errors="replace")
    _, body = split_header_and_body(text)
    body = normalize_body(body, variant)
    fp.write_text(make_header(task_num, variant) + body, encoding="utf-8")


def move_to_dups(fp: Path, task_num: int) -> Path:
    target_dir = DUPS / str(task_num)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / fp.name
    k = 1
    while target.exists():
        target = target_dir / f"{fp.stem}.bak{k}{fp.suffix}"
        k += 1
    shutil.move(str(fp), str(target))
    return target


@dataclass
class Candidate:
    path: Path
    task: int
    variant: int
    body_len: int


def parse_task_variant_from_any_name(fp: Path) -> Optional[Tuple[int, int]]:
    """
    Accept names like:
      task_1_019.txt
      task_1_019.old.txt
      task_1_019.bak2.txt
    """
    m = re.match(r"^task_(\d+)_(\d+)(?:\..+)?\.txt$", fp.name)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def parse_variant_from_content(fp: Path) -> Optional[Tuple[int, int]]:
    """
    Fallback: read header 'Задача №N (вариант V)'.
    """
    try:
        first = fp.open("r", encoding="utf-8", errors="replace").readline().strip()
    except Exception:
        return None
    m = HEADER_RE.search(first)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def index_dups_candidates() -> Dict[Tuple[int, int], List[Candidate]]:
    idx: Dict[Tuple[int, int], List[Candidate]] = {}
    if not DUPS.exists():
        return idx
    for fp in DUPS.rglob("*.txt"):
        tv = parse_task_variant_from_any_name(fp) or parse_variant_from_content(fp)
        if not tv:
            continue
        t, v = tv
        txt = fp.read_text(encoding="utf-8", errors="replace")
        idx.setdefault((t, v), []).append(Candidate(fp, t, v, body_len(txt)))
    # sort best-first
    for k in idx:
        idx[k].sort(key=lambda c: c.body_len, reverse=True)
    return idx


def main() -> None:
    moved_back = 0
    replaced = 0
    kept_existing = 0
    rewritten = 0

    # Build candidates index from dups (including *.old/*.bak)
    dups_idx = index_dups_candidates()

    # 1) restore expected set by filename variants 1..EXPECTED[task]
    for task_num, expected_cnt in EXPECTED.items():
        dest_dir = COND / str(task_num)
        dest_dir.mkdir(parents=True, exist_ok=True)
        for v in range(1, expected_cnt + 1):
            dest = dest_dir / f"task_{task_num}_{v:03d}.txt"
            if dest.exists():
                continue
            cands = dups_idx.get((task_num, v), [])
            if not cands:
                continue
            # copy best candidate back (keep dups as backup)
            shutil.copy2(cands[0].path, dest)
            moved_back += 1

    # 1b) improve short files using dups
    MIN_BODY = 220
    for task_num, expected_cnt in EXPECTED.items():
        dest_dir = COND / str(task_num)
        for v in range(1, expected_cnt + 1):
            dest = dest_dir / f"task_{task_num}_{v:03d}.txt"
            if not dest.exists():
                continue
            txt = dest.read_text(encoding="utf-8", errors="replace")
            cur_len = body_len(txt)
            if cur_len >= MIN_BODY:
                continue
            cands = dups_idx.get((task_num, v), [])
            if cands and cands[0].body_len > cur_len:
                # move current to dups, replace with best
                old_tmp = dest_dir / f"{dest.stem}.old{dest.suffix}"
                shutil.move(str(dest), str(old_tmp))
                move_to_dups(old_tmp, task_num)
                shutil.copy2(cands[0].path, dest)
                replaced += 1

    # 2) rewrite all main files to guarantee header + single marker
    for task_dir in sorted([p for p in COND.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        for fp in sorted(task_dir.glob("task_*.txt")):
            m = re.match(r"^task_(\d+)_(\d+)\.txt$", fp.name)
            if not m:
                continue
            v = int(m.group(2))
            rewrite_file(fp, task_num, v)
            rewritten += 1

    print("=== autorepair_conditions ===")
    print("moved_back_from_dups:", moved_back)
    print("replaced_with_better_from_dups:", replaced)
    print("kept_existing_over_dups:", kept_existing)
    print("rewritten_main_files:", rewritten)


if __name__ == "__main__":
    main()


