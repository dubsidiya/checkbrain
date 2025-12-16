#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit (and optionally fix) extracted task conditions under:
  desh/ege2026kp/conditions/<taskNumber>/task_<taskNumber>_<variant>.txt

Checks:
  - directory taskNumber == filename taskNumber
  - header matches filename (task/variant)
  - internal variant marker "<variant>)" appears near the beginning of the body
    (we only consider the first ~40 non-empty lines after the header to avoid
     matching numbered lists inside the condition)

Fix mode:
  - normalizes header to: "Задача №N (вариант V)" + separator + blank line
  - if the body does not start with "<V>)" near the top, inserts a line "V)"
    as the first non-empty body line (after header), preserving the rest.
  - if the body starts with "K)" and K != V, can rename file to match K and
    update header, but ONLY if it doesn't conflict with an existing file.
"""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, List, Tuple, Dict


FNAME_RE = re.compile(r"^task_(\d+)_(\d+)\.txt$")
HEADER_RE = re.compile(r"Задача\s*№\s*(\d+).*?вариант\s*(\d+)", re.IGNORECASE)


def strip_header(text: str) -> Tuple[str, bool]:
    """
    Returns (body, had_header_block)
    Header block formats observed:
      line0: "Задача №N (вариант V)"
      line1: "====...===="
      blank
    """
    lines = text.splitlines()
    if not lines:
        return "", False

    if lines[0].startswith("Задача") and len(lines) >= 2 and set(lines[1].strip()) == {"="}:
        # drop first 2 lines and a following blank line if present
        rest = lines[2:]
        if rest and rest[0].strip() == "":
            rest = rest[1:]
        return "\n".join(rest).rstrip() + "\n", True
    return text, False


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def find_internal_variant_near_top(body: str, max_non_empty_lines: int = 40) -> Optional[int]:
    """
    Look for a line starting with "<digits>)" near the top of the body.
    We only scan the first N non-empty lines to avoid matching numbered lists.
    """
    non_empty_seen = 0
    for line in body.splitlines():
        s = line.strip()
        if not s:
            continue
        non_empty_seen += 1
        # skip separator-like lines
        if set(s) in ({"="}, {"-"}, {"_"}):
            continue
        m = re.match(r"^(\d+)\)\s*", s)
        if m:
            # Accept either:
            #  - a pure marker line like "210)" (inserted by our normalizer), OR
            #  - a real task start line containing letters.
            # This avoids false matches from numbered lists deeper in the text.
            if s == f"{m.group(1)})" or re.search(r"[А-Яа-яA-Za-z]", s):
                return int(m.group(1))
        if non_empty_seen >= max_non_empty_lines:
            break
    return None


@dataclass
class Issue:
    task: int
    file: str
    kind: str
    detail: str = ""


def audit_and_fix(base: Path, fix: bool) -> Tuple[Dict[int, int], List[Issue]]:
    counts: Dict[int, int] = {}
    issues: List[Issue] = []

    for task_dir in sorted([p for p in base.iterdir() if p.is_dir()], key=lambda p: int(p.name)):
        task_num = int(task_dir.name)
        files = sorted(task_dir.glob("*.txt"))
        counts[task_num] = len(files)

        # Build a set of existing filenames to avoid rename collisions
        existing_names = {p.name for p in files}

        for fp in files:
            m = FNAME_RE.match(fp.name)
            if not m:
                issues.append(Issue(task_num, fp.name, "bad_filename"))
                continue
            f_task = int(m.group(1))
            f_var = int(m.group(2))

            if f_task != task_num:
                issues.append(Issue(task_num, fp.name, "filename_task_mismatch", str(f_task)))

            text = fp.read_text(encoding="utf-8", errors="replace")

            # header parse
            header_line = text.splitlines()[0].strip() if text else ""
            hm = HEADER_RE.search(header_line)
            h_task = h_var = None
            if not hm:
                issues.append(Issue(task_num, fp.name, "bad_header", header_line))
            else:
                h_task = int(hm.group(1))
                h_var = int(hm.group(2))
                if h_task != task_num:
                    issues.append(Issue(task_num, fp.name, "header_task_mismatch", str(h_task)))
                if h_var != f_var:
                    issues.append(Issue(task_num, fp.name, "header_variant_mismatch", str(h_var)))

            body, _ = strip_header(text)
            internal = find_internal_variant_near_top(body)

            if internal is None:
                issues.append(Issue(task_num, fp.name, "missing_internal_variant"))
                if fix:
                    # Insert "VVV)" marker as its own line at the top of body.
                    new_body = f"{f_var})\n" + body.lstrip("\n")
                    new_text = make_header(task_num, f_var) + new_body
                    fp.write_text(new_text, encoding="utf-8")
                continue

            if internal != f_var:
                issues.append(Issue(task_num, fp.name, "internal_variant_mismatch", str(internal)))
                if fix:
                    # Prefer renaming file/header to match internal variant if safe.
                    new_name = f"task_{task_num}_{internal:03d}.txt"
                    if new_name not in existing_names:
                        # rewrite header to match internal
                        new_text = make_header(task_num, internal) + body
                        target = fp.with_name(new_name)
                        fp.write_text(new_text, encoding="utf-8")
                        fp.rename(target)
                        existing_names.add(new_name)
                        existing_names.discard(fp.name)
                    else:
                        # conflict: don't rename, but at least fix header to match filename
                        new_text = make_header(task_num, f_var) + body
                        fp.write_text(new_text, encoding="utf-8")

            # If header mismatched, fix header to match filename/internal preference
            if fix:
                # reload (could have been renamed)
                current_fp = fp
                if not current_fp.exists():
                    # it was renamed; skip (next loop iteration doesn't see it)
                    continue
                m2 = FNAME_RE.match(current_fp.name)
                if not m2:
                    continue
                cur_var = int(m2.group(2))
                cur_text = current_fp.read_text(encoding="utf-8", errors="replace")
                cur_body, _ = strip_header(cur_text)
                cur_internal = find_internal_variant_near_top(cur_body)
                # if internal exists and differs from filename, we keep filename (conflict case)
                header_target_var = cur_var
                if cur_internal is not None and cur_internal == cur_var:
                    header_target_var = cur_var
                new_text = make_header(task_num, header_target_var) + cur_body
                if cur_text != new_text:
                    current_fp.write_text(new_text, encoding="utf-8")

    return counts, issues


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="desh/ege2026kp/conditions", help="Base conditions dir")
    ap.add_argument("--fix", action="store_true", help="Apply safe fixes")
    ap.add_argument("--report", default="conditions_audit_report_v2.tsv", help="Report path")
    args = ap.parse_args()

    base = Path(args.base)
    counts, issues = audit_and_fix(base, fix=args.fix)

    out = Path(args.report)
    with out.open("w", encoding="utf-8") as f:
        f.write("COUNTS\n")
        for k in sorted(counts):
            f.write(f"{k}\t{counts[k]}\n")
        f.write("\nISSUES\n")
        f.write("task\tfile\tkind\tdetail\n")
        for it in issues:
            f.write(f"{it.task}\t{it.file}\t{it.kind}\t{it.detail}\n")

    print(f"Report written: {out}")
    print(f"Total issues: {len(issues)} (fix={'on' if args.fix else 'off'})")


if __name__ == "__main__":
    main()


