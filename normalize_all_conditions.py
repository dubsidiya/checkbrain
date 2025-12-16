#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Normalize all extracted condition files so that:
  - directory task number == filename task number
  - header "Задача №N (вариант V)" matches filename V
  - the first internal marker "V)" near the top of the body matches V

If an internal variant near the top is detected and differs from filename:
  - rename file to match internal variant (task_N_internal.txt)
  - rewrite header to match internal

If no internal marker is found near the top:
  - insert "<filename_variant>)" as the first non-empty body line
  - rewrite header to match filename

If renaming causes collisions (two files claim the same internal variant):
  - keep ONE canonical file for that internal variant
  - move the rest to: desh/ege2026kp/conditions_dups/<taskNumber>/
    (this folder is NOT included in pubspec assets, so the app won't see them)

This is a destructive operation (renames/moves files). Use git to review.
"""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, List, Tuple


FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")
HEADER_RE = re.compile(r"Задача\s*№\s*(\d+).*?вариант\s*(\d+)", re.IGNORECASE)


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def strip_header(text: str) -> str:
    lines = text.splitlines()
    if not lines:
        return ""
    if lines[0].startswith("Задача") and len(lines) >= 2 and set(lines[1].strip()) == {"="}:
        rest = lines[2:]
        if rest and rest[0].strip() == "":
            rest = rest[1:]
        return "\n".join(rest).rstrip() + "\n"
    return text.rstrip() + "\n"


def find_internal_variant_near_top(body: str, max_non_empty_lines: int = 40) -> Optional[int]:
    non_empty = 0
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        non_empty += 1
        # skip pure separators
        if set(s) in ({"="}, {"-"}, {"_"}):
            continue
        m = re.match(r"^(\d+)\)\s*", s)
        if m:
            # Must have letters to be a task start (avoid matching "1) 2) 3)" lists)
            if re.search(r"[А-Яа-яA-Za-z]", s):
                return int(m.group(1))
        if non_empty >= max_non_empty_lines:
            break
    return None


@dataclass
class FileInfo:
    path: Path
    task: int
    filename_variant: int
    internal_variant: Optional[int]
    body: str


def load_file_info(fp: Path, task_dir_num: int) -> Optional[FileInfo]:
    m = FNAME_RE.match(fp.name)
    if not m:
        return None
    task = int(m.group(1))
    var = int(m.group(2))
    text = fp.read_text(encoding="utf-8", errors="replace")
    body = strip_header(text)
    internal = find_internal_variant_near_top(body)
    return FileInfo(path=fp, task=task, filename_variant=var, internal_variant=internal, body=body)


def ensure_internal_marker(body: str, variant: int) -> str:
    # If already has variant marker near top, keep.
    internal = find_internal_variant_near_top(body)
    if internal == variant:
        return body
    # Insert marker as its own line at top (after trimming leading blanks)
    return f"{variant})\n" + body.lstrip("\n")


def write_normalized(fp: Path, task_num: int, variant: int, body: str) -> None:
    fp.write_text(make_header(task_num, variant) + body, encoding="utf-8")


def move_to_dups(fp: Path, dups_root: Path, task_num: int) -> Path:
    target_dir = dups_root / str(task_num)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / fp.name
    i = 1
    while target.exists():
        target = target_dir / f"{fp.stem}.dup{i}{fp.suffix}"
        i += 1
    shutil.move(str(fp), str(target))
    return target


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="desh/ege2026kp/conditions", help="Base conditions dir")
    ap.add_argument("--dups", default="desh/ege2026kp/conditions_dups", help="Where to move duplicates")
    ap.add_argument("--dry-run", action="store_true", help="No writes, just report")
    args = ap.parse_args()

    base = Path(args.base)
    dups_root = Path(args.dups)

    total_files = 0
    fixed_headers = 0
    inserted_markers = 0
    renamed = 0
    moved_dups = 0
    bad_names = 0
    bad_taskdir = 0
    dup_sets: List[Tuple[int, int, List[str]]] = []

    for task_dir in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_dir_num = int(task_dir.name)
        infos: List[FileInfo] = []
        for fp in sorted(task_dir.glob("*.txt")):
            info = load_file_info(fp, task_dir_num)
            if info is None:
                bad_names += 1
                continue
            total_files += 1
            if info.task != task_dir_num:
                bad_taskdir += 1
            infos.append(info)

        # Decide target variant per file:
        # - if internal exists -> internal wins
        # - else -> filename variant wins (and we will insert marker)
        by_target: Dict[int, List[FileInfo]] = {}
        for info in infos:
            target_var = info.internal_variant if info.internal_variant is not None else info.filename_variant
            by_target.setdefault(target_var, []).append(info)

        # Resolve duplicates (multiple files target same variant)
        for target_var, group in sorted(by_target.items(), key=lambda kv: kv[0]):
            if len(group) <= 1:
                continue
            # Choose canonical:
            # 1) file whose filename variant already equals target
            # 2) otherwise smallest filename
            canonical = None
            for g in group:
                if g.filename_variant == target_var:
                    canonical = g
                    break
            if canonical is None:
                canonical = sorted(group, key=lambda x: x.path.name)[0]
            others = [g for g in group if g.path != canonical.path]
            dup_sets.append((task_dir_num, target_var, [o.path.name for o in others]))

            # Move others away
            for o in others:
                if args.dry_run:
                    continue
                move_to_dups(o.path, dups_root, task_dir_num)
                moved_dups += 1

        # Re-scan current dir after moving dups
        current_files = sorted(task_dir.glob("*.txt"))
        for fp in current_files:
            info = load_file_info(fp, task_dir_num)
            if info is None:
                continue

            target_var = info.internal_variant if info.internal_variant is not None else info.filename_variant
            body = info.body
            # ensure marker
            if info.internal_variant is None:
                new_body = ensure_internal_marker(body, target_var)
                if new_body != body:
                    inserted_markers += 1
                body = new_body

            # rename if needed
            desired_name = f"task_{task_dir_num}_{target_var:03d}.txt"
            desired_path = fp.with_name(desired_name)
            if fp.name != desired_name:
                if args.dry_run:
                    pass
                else:
                    if desired_path.exists():
                        # collision still exists -> move this file to dups
                        move_to_dups(fp, dups_root, task_dir_num)
                        moved_dups += 1
                        continue
                    fp.rename(desired_path)
                    fp = desired_path
                renamed += 1

            # rewrite header always (canonical)
            new_text = make_header(task_dir_num, target_var) + body
            if args.dry_run:
                continue
            old_text = fp.read_text(encoding="utf-8", errors="replace")
            if old_text != new_text:
                fp.write_text(new_text, encoding="utf-8")
                fixed_headers += 1

    print("=== normalize_all_conditions ===")
    print("files_total:", total_files)
    print("bad_names:", bad_names)
    print("taskdir_task_mismatch:", bad_taskdir)
    print("renamed:", renamed)
    print("inserted_markers:", inserted_markers)
    print("rewrote_headers:", fixed_headers)
    print("moved_duplicates:", moved_dups)
    print("dup_sets:", len(dup_sets))
    if dup_sets:
        print("sample dup sets (up to 10):")
        for t, v, others in dup_sets[:10]:
            print(f"  task {t} variant {v}: moved {len(others)} files, e.g. {others[:3]}")


if __name__ == "__main__":
    main()


