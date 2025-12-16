#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild tasks 19/20/21 conditions directly from the source PDF: desh/ege2026kp/ege1921.pdf

Important nuance:
  The PDF groups several "game statements" (variants like 46), and then *after them*
  there is one shared questions block:
      "Вопросы 19-21 к следующим задачам:" + "Задание 19/20/21 ..."
  That questions block applies to ALL game variants since the previous questions block.

So we:
  - parse all variant statements (V) from the PDF
  - parse all questions blocks (Q)
  - assign each Q to all variants collected since the last Q
  - for each variant: produce 3 files (19/20/21) with:
      statement(V) + only its question block (from Q)

Output:
  desh/ege2026kp/conditions/19/task_19_VVV.txt
  desh/ege2026kp/conditions/20/task_20_VVV.txt
  desh/ege2026kp/conditions/21/task_21_VVV.txt

We overwrite an existing file only if:
  - it misses its question label, OR
  - the new text is longer.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pdfplumber


BASE = Path("desh/ege2026kp")
PDF = BASE / "ege1921.pdf"
COND = BASE / "conditions"


def make_header(task_num: int, variant: int) -> str:
    return f"Задача №{task_num} (вариант {variant})\n" + ("=" * 50) + "\n\n"


def is_footer_or_noise(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if "http://kpolyakov" in s or "kpolyakov" in s:
        return True
    if s.startswith("©"):
        return True
    # page header like "9 http://..." sometimes prefixed with page num
    if re.match(r"^\d+\s+http", s):
        return True
    # standalone page number
    if re.match(r"^\d{1,3}$", s):
        return True
    return False


def is_variant_start(line: str) -> Optional[int]:
    s = line.strip()
    m = re.match(r"^(\d{1,4})\)\s*(.*)$", s)
    if not m:
        return None
    n = int(m.group(1))
    rest = m.group(2)
    # exclude multi-choice-like lines with many markers
    if len(re.findall(r"\b\d{1,4}\)", s)) >= 3:
        return None
    # must have letters after marker
    if not re.search(r"[А-Яа-яA-Za-z]", rest):
        return None
    return n


def is_questions_header(line: str) -> bool:
    # The PDF uses this header in multiple forms:
    # - "Вопросы 19-21 к следующим задачам:"
    # - "Вопросы 19-21 к задаче 11 и следующим задачам следующие:"
    return "Вопросы 19-21" in line


def extract_pdf_lines() -> List[str]:
    lines: List[str] = []
    with pdfplumber.open(str(PDF)) as doc:
        for page in doc.pages:
            txt = page.extract_text() or ""
            lines.extend(txt.split("\n"))
    return lines


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


def split_question_block(q_lines: List[str]) -> Optional[Dict[int, List[str]]]:
    """
    Split a questions block into three parts by labels 'Задание 19/20/21'.
    Returns dict {19,20,21} -> lines (including label line).
    """
    text = "\n".join(q_lines)
    if not (
        re.search(r"\bЗадание\s*19\b", text, re.IGNORECASE)
        and re.search(r"\bЗадание\s*20\b", text, re.IGNORECASE)
        and re.search(r"\bЗадание\s*21\b", text, re.IGNORECASE)
    ):
        return None

    def find_idx(pat: str) -> Optional[int]:
        rx = re.compile(pat, re.IGNORECASE)
        for i, ln in enumerate(q_lines):
            if rx.search(ln):
                return i
        return None

    i19 = find_idx(r"\bЗадание\s*19\b")
    i20 = find_idx(r"\bЗадание\s*20\b")
    i21 = find_idx(r"\bЗадание\s*21\b")
    if i19 is None or i20 is None or i21 is None:
        return None

    # keep optional header "Вопросы 19-21..." if it exists above
    prefix = q_lines[:i19]
    p19 = prefix + q_lines[i19:i20]
    p20 = prefix + q_lines[i20:i21]
    p21 = prefix + q_lines[i21:]
    return {19: p19, 20: p20, 21: p21}


def extract_embedded_questions_from_statement(statement_lines: List[str]) -> Optional[Tuple[List[str], List[str]]]:
    """
    Some variants include the 19/20/21 questions right inside the variant block
    (no separate 'Вопросы 19-21 ...' section). In that case we split:
      statement_only = lines before the first 'Задание 19'
      q_lines        = lines starting from 'Задание 19' (and below)
    Returns (statement_only, q_lines) or None.
    """
    idx19 = None
    for i, ln in enumerate(statement_lines):
        if re.search(r"\bЗадание\s*19\b", ln, re.IGNORECASE):
            idx19 = i
            break
    if idx19 is None:
        return None
    # Require also 20 and 21 somewhere after to be considered a full embedded block
    tail = "\n".join(statement_lines[idx19:])
    if not (
        re.search(r"\bЗадание\s*20\b", tail, re.IGNORECASE)
        and re.search(r"\bЗадание\s*21\b", tail, re.IGNORECASE)
    ):
        return None
    return statement_lines[:idx19], statement_lines[idx19:]


def should_overwrite(existing_text: str, task_num: int, new_text: str) -> bool:
    if not re.search(rf"\bЗадание\s*{task_num}\b", existing_text, re.IGNORECASE):
        return True
    return len(new_text.strip()) > len(existing_text.strip())


def write_condition(task_num: int, variant: int, statement: List[str], q_part: List[str], dry_run: bool) -> bool:
    out_dir = COND / str(task_num)
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"task_{task_num}_{variant:03d}.txt"
    body_lines = [ln for ln in statement if not is_footer_or_noise(ln)]
    body_lines.append("")  # separator
    body_lines.extend([ln for ln in q_part if not is_footer_or_noise(ln)])
    new_text = make_header(task_num, variant) + ("\n".join(body_lines).rstrip() + "\n")

    if out.exists():
        old = out.read_text(encoding="utf-8", errors="replace")
        if not should_overwrite(old, task_num, new_text):
            return False
    if not dry_run:
        out.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-variant", type=int, default=None, help="Limit rebuild to variants <= N")
    args = ap.parse_args()

    if not PDF.exists():
        raise SystemExit(f"PDF not found: {PDF}")

    lines = extract_pdf_lines()
    start = find_training_start(lines)
    lines = lines[start:]

    statements: Dict[int, List[str]] = {}
    questions_blocks: List[List[str]] = []

    current_variant: Optional[int] = None
    current_statement: List[str] = []
    current_questions: Optional[List[str]] = None
    pending_variants: List[int] = []
    assigned_questions: Dict[int, List[str]] = {}
    active_questions_for_future: Optional[List[str]] = None
    last_good_questions_block: Optional[List[str]] = None
    last_variant_seen: Optional[int] = None

    def finalize_statement() -> None:
        nonlocal current_variant, current_statement, active_questions_for_future
        if current_variant is None:
            return
        if args.max_variant is not None and current_variant > args.max_variant:
            current_variant = None
            current_statement = []
            return
        st_lines = current_statement[:]
        # If this variant already contains embedded 19/20/21 questions, extract them and do NOT
        # wait for the external question block.
        embedded = extract_embedded_questions_from_statement(st_lines)
        if embedded is not None:
            st_only, q_lines = embedded
            statements[current_variant] = st_only
            assigned_questions[current_variant] = q_lines
        else:
            statements[current_variant] = st_lines
            pending_variants.append(current_variant)
            # If we have a questions block that applies to future variants,
            # assign it immediately when a variant statement finishes.
            if active_questions_for_future is not None:
                assigned_questions[current_variant] = active_questions_for_future[:]
        current_variant = None
        current_statement = []

    def finalize_questions() -> None:
        nonlocal current_questions, pending_variants, active_questions_for_future, last_good_questions_block, last_variant_seen
        if not current_questions:
            return
        # Track the last "good" questions block (the one that can be split into 19/20/21).
        if split_question_block(current_questions) is not None:
            last_good_questions_block = current_questions[:]

        # If we have pending variants since the previous questions block,
        # this questions block applies to those variants (like 46-48).
        # Otherwise, it acts as a template for the upcoming variants.
        if pending_variants:
            # Heuristic: if pending variants are "close" to the current position,
            # we attach backwards. If the gap is large (e.g. pending ended at 84,
            # but we are already at 94), this block is a new template for future variants,
            # and the pending ones should use the previous template.
            max_pending = max(pending_variants)
            gap = (last_variant_seen - max_pending) if last_variant_seen is not None else 999
            backward_window = 3
            if gap <= backward_window:
                for v in pending_variants:
                    assigned_questions[v] = current_questions[:]
                pending_variants = []
                active_questions_for_future = None
            else:
                # Use previous known-good block for pending (if available)
                if last_good_questions_block is not None:
                    for v in pending_variants:
                        assigned_questions[v] = last_good_questions_block[:]
                    pending_variants = []
                # And treat current as template for future variants
                active_questions_for_future = current_questions[:]
        else:
            active_questions_for_future = current_questions[:]
        current_questions = None

    for ln in lines:
        if is_footer_or_noise(ln):
            continue

        vstart = is_variant_start(ln)
        if vstart is not None:
            last_variant_seen = vstart
            # starting a new variant statement closes any open questions block
            if current_questions is not None:
                finalize_questions()
            # closes previous statement
            if current_variant is not None:
                finalize_statement()
            current_variant = vstart
            current_statement = [ln]
            continue

        if is_questions_header(ln):
            # close last statement and begin questions
            if current_variant is not None:
                finalize_statement()
            if current_questions is not None:
                finalize_questions()
            current_questions = [ln]
            continue

        # continuation line
        if current_questions is not None:
            current_questions.append(ln)
        elif current_variant is not None:
            current_statement.append(ln)
        else:
            # outside blocks (ignore)
            continue

    # finalize tail
    if current_variant is not None:
        finalize_statement()
    if current_questions is not None:
        finalize_questions()

    updated = 0
    missing_q = 0
    bad_q = 0

    for v in sorted(statements.keys()):
        q = assigned_questions.get(v)
        if not q:
            missing_q += 1
            continue
        parts = split_question_block(q)
        if not parts:
            bad_q += 1
            continue
        st = statements[v]
        for t in (19, 20, 21):
            if write_condition(t, v, st, parts[t], args.dry_run):
                updated += 1

    print("=== rebuild_1921_from_pdf ===")
    print("variants_statements:", len(statements))
    print("variants_with_questions:", len(assigned_questions))
    print("missing_questions_for_variants:", missing_q)
    print("bad_question_blocks:", bad_q)
    print("files_updated:", updated)


if __name__ == "__main__":
    main()


