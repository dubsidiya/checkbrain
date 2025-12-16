#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix condition files where filename/header variant does NOT match the real internal variant.

Typical broken pattern (after aggressive "autorepair"):
  Header says variant 159, then body starts with:
    159)
    176) (Author) ... real condition text ...
So "159)" is just a placeholder marker line, but the real variant is 176.

This script:
  1) For every desh/ege2026kp/conditions/<task>/task_<task>_<v>.txt:
     - detects the first *meaningful* internal marker "N)" (line with letters after marker)
     - if there is a leading placeholder marker line equal to filename/header variant, removes it
     - renames file + rewrites header to use the real variant (N)
     - handles collisions by moving losers to conditions_dups/<task>/

  2) Special-case for tasks 19/20/21:
     If a condition contains "Задание 19/20/21" blocks, it is a combined statement.
     We split into 3 separate files:
       - task 19: statement + block "Задание 19"
       - task 20: statement + block "Задание 20"
       - task 21: statement + block "Задание 21"
     All with the same variant number.

Safe-ish: destructive renames/moves. Use git to review if needed.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple


BASE = Path("desh/ege2026kp")
COND = BASE / "conditions"
DUPS = BASE / "conditions_dups"

FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")
HEADER_RE = re.compile(r"Задача\s*№\s*(\d+).*?вариант\s*(\d+)", re.IGNORECASE)


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def split_header_and_body(text: str) -> Tuple[str, List[str]]:
    lines = text.splitlines()
    if len(lines) >= 2 and lines[0].startswith("Задача") and set(lines[1].strip()) == {"="}:
        body = lines[2:]
        if body and body[0].strip() == "":
            body = body[1:]
        return "\n".join(lines[:2]) + "\n", body
    return "", lines


def parse_filename(fp: Path) -> Optional[Tuple[int, int]]:
    m = FNAME_RE.match(fp.name)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def parse_header_variant(text: str) -> Optional[Tuple[int, int]]:
    first_line = text.splitlines()[0] if text.splitlines() else ""
    m = HEADER_RE.search(first_line)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))


def marker_line_variant(line: str) -> Optional[Tuple[int, str]]:
    s = line.strip()
    m = re.match(r"^(\d{1,4})\)\s*(.*)$", s)
    if not m:
        return None
    return int(m.group(1)), m.group(2)


def is_meaningful_marker(rest: str) -> bool:
    # "159)" alone is NOT meaningful; "176) (Автор) ..." is meaningful.
    return bool(re.search(r"[А-Яа-яA-Za-z]", rest))


def find_real_variant(body_lines: List[str], max_scan: int = 80) -> Optional[int]:
    non_empty = 0
    for ln in body_lines:
        s = ln.strip()
        if not s:
            continue
        non_empty += 1
        # skip separators
        if set(s) in ({"="}, {"-"}, {"_"}):
            continue
        mv = marker_line_variant(s)
        if mv:
            v, rest = mv
            # ignore multi-choice option lines: "1) ... 2) ... 3) ..." (many markers)
            if len(re.findall(r"\b\d{1,4}\)", s)) >= 3:
                continue
            if is_meaningful_marker(rest):
                return v
        if non_empty >= max_scan:
            break
    return None


def find_real_variant_with_index(body_lines: List[str], max_scan: int = 80) -> Optional[Tuple[int, int]]:
    """
    Return (index, variant) for the first meaningful marker line "N)" near the top.
    """
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
            if len(re.findall(r"\b\d{1,4}\)", s)) >= 3:
                continue
            if is_meaningful_marker(rest):
                return idx, v
        if non_empty >= max_scan:
            break
    return None


def remove_leading_placeholder(body_lines: List[str], placeholder_variant: int) -> List[str]:
    # Remove leading blanks, then remove ONE placeholder line if it is exactly "V)"
    i = 0
    while i < len(body_lines) and body_lines[i].strip() == "":
        i += 1
    if i < len(body_lines) and body_lines[i].strip() == f"{placeholder_variant})":
        return body_lines[:i] + body_lines[i + 1 :]
    return body_lines


def move_to_dups(fp: Path, task_num: int) -> Path:
    target_dir = DUPS / str(task_num)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / fp.name
    k = 1
    while target.exists():
        target = target_dir / f"{fp.stem}.fix{k}{fp.suffix}"
        k += 1
    shutil.move(str(fp), str(target))
    return target


def write_file(fp: Path, task_num: int, variant: int, body_lines: List[str]) -> None:
    body = "\n".join(body_lines).rstrip() + "\n"
    fp.write_text(make_header(task_num, variant) + body, encoding="utf-8")


def split_1921_blocks(body_lines: List[str]) -> Optional[Dict[int, List[str]]]:
    """
    If body contains "Задание 19/20/21" blocks, return mapping {19,20,21} -> body_lines.
    Each body is: (variant marker line + statement + that task's block)
    """
    text = "\n".join(body_lines)
    if not ("Задание 19" in text and "Задание 20" in text and "Задание 21" in text):
        return None

    # Identify real start line: first meaningful "V) <text...>"
    rv = find_real_variant_with_index(body_lines, max_scan=120)
    if rv is None:
        return None
    v_line_idx, v = rv

    # Find blocks by lines "Задание 19.", "Задание 20.", "Задание 21" (dot optional)
    def find_idx(pat: str) -> Optional[int]:
        rx = re.compile(pat, re.IGNORECASE)
        for i, ln in enumerate(body_lines):
            if rx.search(ln):
                return i
        return None

    i19 = find_idx(r"\bЗадание\s*19\b")
    i20 = find_idx(r"\bЗадание\s*20\b")
    i21 = find_idx(r"\bЗадание\s*21\b")
    if i19 is None or i20 is None or i21 is None:
        return None

    # Statement: from real variant line up to just before "Задание 19"
    statement = body_lines[v_line_idx:i19]
    # blocks: from label to before next label (keep label line)
    block19 = body_lines[i19:i20]
    block20 = body_lines[i20:i21]
    block21 = body_lines[i21:]

    return {
        19: statement + block19,
        20: statement + block20,
        21: statement + block21,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=str(COND), help="Conditions base directory")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only-task", type=int, default=None)
    ap.add_argument(
        "--include-dups-1921",
        action="store_true",
        help="For tasks 19/20/21 also scan conditions_dups as sources to split combined statements",
    )
    args = ap.parse_args()

    base = Path(args.base)
    renamed = 0
    rewritten = 0
    moved_dups = 0
    split_1921 = 0

    for task_dir in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        if args.only_task is not None and task_num != args.only_task:
            continue

        # Primary sources: conditions/<task>/*.txt
        sources = list(sorted(task_dir.glob("task_*.txt")))
        # Additional sources for 19-21: conditions_dups/<task>/*.txt (read-only source)
        if task_num in (19, 20, 21) and args.include_dups_1921:
            dups_dir = DUPS / str(task_num)
            if dups_dir.exists():
                sources += list(sorted(dups_dir.glob("task_*.txt")))

        for fp in sources:
            tv = parse_filename(fp)
            if not tv:
                continue
            fn_task, fn_var = tv
            if fn_task != task_num:
                continue

            text = fp.read_text(encoding="utf-8", errors="replace")
            header, body_lines = split_header_and_body(text)

            hv = None
            hv_parsed = parse_header_variant(text)
            if hv_parsed:
                _, hv = hv_parsed

            real = find_real_variant(body_lines)
            if real is None:
                continue

            # remove placeholder (prefer header variant if present, else filename variant)
            placeholder = hv if hv is not None else fn_var
            if placeholder != real:
                body_lines2 = remove_leading_placeholder(body_lines, placeholder)
            else:
                body_lines2 = body_lines

            # split 19-21 blocks if present (only for task 19/20/21 dirs)
            if task_num in (19, 20, 21):
                parts = split_1921_blocks(body_lines2)
                if parts:
                    # Write for each of 19/20/21 into their folders using same real variant
                    for t in (19, 20, 21):
                        dest_dir = base / str(t)
                        dest_dir.mkdir(parents=True, exist_ok=True)
                        dest = dest_dir / f"task_{t}_{real:03d}.txt"
                        # If collision: keep longer body (more complete condition)
                        new_body_text = "\n".join(parts[t]).rstrip() + "\n"
                        if dest.exists():
                            old_text = dest.read_text(encoding="utf-8", errors="replace")
                            _, old_body_lines = split_header_and_body(old_text)
                            old_body_text = "\n".join(old_body_lines).rstrip() + "\n"
                            if len(new_body_text.strip()) > len(old_body_text.strip()):
                                if not args.dry_run:
                                    move_to_dups(dest, t)
                                moved_dups += 1
                            else:
                                # existing is better; skip writing
                                continue
                        if not args.dry_run:
                            write_file(dest, t, real, parts[t])
                        rewritten += 1
                    split_1921 += 1

            # Rename file if needed
            desired = fp.with_name(f"task_{task_num}_{real:03d}.txt")
            cur = fp
            # Never rename/move sources that live in conditions_dups (they are only sources)
            is_dups_source = str(fp).find(str(DUPS)) != -1
            if (not is_dups_source) and desired.name != fp.name:
                if desired.exists():
                    # Collision: keep longer body
                    existing_text = desired.read_text(encoding="utf-8", errors="replace")
                    _, existing_body_lines = split_header_and_body(existing_text)
                    existing_body = "\n".join(existing_body_lines).rstrip()
                    current_body = "\n".join(body_lines2).rstrip()
                    if len(current_body.strip()) > len(existing_body.strip()):
                        if not args.dry_run:
                            move_to_dups(desired, task_num)
                            cur.rename(desired)
                        moved_dups += 1
                        cur = desired
                        renamed += 1
                    else:
                        if not args.dry_run:
                            move_to_dups(cur, task_num)
                        moved_dups += 1
                        continue
                else:
                    if not args.dry_run:
                        cur.rename(desired)
                    cur = desired
                    renamed += 1

            # Rewrite header + keep body (after placeholder removal)
            new_text = make_header(task_num, real) + ("\n".join(body_lines2).rstrip() + "\n")
            if (not args.dry_run) and (not is_dups_source):
                cur.write_text(new_text, encoding="utf-8")
            rewritten += 1

    print("=== fix_conditions_variant_mismatches ===")
    print("renamed:", renamed)
    print("rewritten:", rewritten)
    print("moved_to_dups:", moved_dups)
    print("split_19_21_sets:", split_1921)


if __name__ == "__main__":
    main()


