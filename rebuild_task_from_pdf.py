#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild a task's conditions from its source PDF.

Fixes two issues:
  - variants glued into a single txt file
  - missing variants (incomplete extraction)

Also supports [pic] placeholders:
  - if extracted text contains '[pic]' for a variant, we render the PDF page where that
    placeholder appears to PNG and save it alongside the condition file with the same basename.
    Example: conditions/14/task_14_082.png
The app can then show the image below the text.

Usage:
  python3 rebuild_task_from_pdf.py --task 14 --pdf desh/ege2026kp/ege14.pdf --wipe
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pdfplumber


BASE = Path("desh/ege2026kp")


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
    if re.match(r"^\d+\s+http", s):
        return True
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
    # avoid multi-marker option lines
    if len(re.findall(r"\b\d{1,4}\)", s)) >= 3:
        return None
    # must have letters after marker (real statement)
    if not re.search(r"[А-Яа-яA-Za-z]", rest):
        return None
    return n


def find_training_start(lines: List[str]) -> int:
    for i, ln in enumerate(lines):
        if "Задачи для тренировки" in ln:
            return i + 1
    return 0


@dataclass
class Line:
    page: int
    text: str


@dataclass
class VariantBlock:
    variant: int
    lines: List[Line]

    def plain_lines(self) -> List[str]:
        return [ln.text for ln in self.lines if not is_footer_or_noise(ln.text)]

    def pages_with_pic(self) -> List[int]:
        pages: List[int] = []
        for ln in self.lines:
            if "[pic]" in ln.text:
                pages.append(ln.page)
        # unique preserving order
        out = []
        for p in pages:
            if p not in out:
                out.append(p)
        return out

    def pages_with_missing_equation_picture(self) -> List[int]:
        """
        pdfplumber may drop equation images completely, leaving lines like:
          '82) Решите уравнение .'
        Treat that as a picture placeholder and render the page.
        """
        pages: List[int] = []
        for ln in self.lines:
            s = ln.text.strip()
            if re.search(r"Решите\s+уравнение\s*\.\s*$", s, flags=re.IGNORECASE):
                pages.append(ln.page)
        out: List[int] = []
        for p in pages:
            if p not in out:
                out.append(p)
        return out


def extract_pdf_lines(pdf: Path) -> List[Line]:
    out: List[Line] = []
    with pdfplumber.open(str(pdf)) as doc:
        for page_idx, page in enumerate(doc.pages, start=1):
            txt = page.extract_text() or ""
            for ln in txt.split("\n"):
                out.append(Line(page=page_idx, text=ln))
    return out


def split_variants(lines: List[Line]) -> List[VariantBlock]:
    # work with plain strings for start detection, but keep page numbers
    raw_text = [ln.text for ln in lines]
    start = find_training_start(raw_text)
    lines = lines[start:]

    blocks: List[VariantBlock] = []
    cur_v: Optional[int] = None
    cur_lines: List[Line] = []

    def flush() -> None:
        nonlocal cur_v, cur_lines
        if cur_v is None:
            return
        blocks.append(VariantBlock(cur_v, cur_lines[:]))
        cur_v = None
        cur_lines = []

    for ln in lines:
        if is_footer_or_noise(ln.text):
            continue
        v = is_variant_start(ln.text)
        if v is not None:
            flush()
            cur_v = v
            cur_lines = [ln]
        else:
            if cur_v is not None:
                cur_lines.append(ln)

    flush()
    return blocks


def render_page_png(pdf: Path, page: int, out_png: Path, dpi: int = 200) -> None:
    """
    Render a single PDF page to PNG using pdftoppm (fast and reliable on mac).
    """
    out_png.parent.mkdir(parents=True, exist_ok=True)
    prefix = out_png.with_suffix("")  # pdftoppm adds .png
    cmd = [
        "pdftoppm",
        "-png",
        "-r",
        str(dpi),
        "-f",
        str(page),
        "-l",
        str(page),
        "-singlefile",
        str(pdf),
        str(prefix),
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    produced = prefix.with_suffix(".png")
    if produced != out_png:
        if out_png.exists():
            out_png.unlink()
        produced.rename(out_png)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", type=int, required=True)
    ap.add_argument("--pdf", type=str, required=True)
    ap.add_argument("--wipe", action="store_true", help="Move existing conditions/<task> to a backup folder first")
    ap.add_argument("--no-images", action="store_true", help="Do not render PNGs for [pic]")
    ap.add_argument("--dpi", type=int, default=200)
    args = ap.parse_args()

    task = args.task
    pdf = Path(args.pdf)
    if not pdf.exists():
        raise SystemExit(f"PDF not found: {pdf}")

    out_dir = BASE / "conditions" / str(task)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.wipe:
        backup = BASE / "conditions_backup" / str(task)
        backup.mkdir(parents=True, exist_ok=True)
        for fp in out_dir.glob("*"):
            shutil.move(str(fp), str(backup / fp.name))

    lines = extract_pdf_lines(pdf)
    blocks = split_variants(lines)

    written = 0
    pics = 0
    for b in blocks:
        body = "\n".join(b.plain_lines()).rstrip() + "\n"
        out_txt = out_dir / f"task_{task}_{b.variant:03d}.txt"
        out_txt.write_text(make_header(task, b.variant) + body, encoding="utf-8")
        written += 1

        if not args.no_images:
            pages = b.pages_with_pic() + b.pages_with_missing_equation_picture()
            if pages:
                out_png = out_dir / f"task_{task}_{b.variant:03d}.png"
                try:
                    render_page_png(pdf, pages[0], out_png, dpi=args.dpi)
                    pics += 1
                except Exception:
                    # keep going even if rendering fails
                    pass

    print("=== rebuild_task_from_pdf ===")
    print("task:", task)
    print("variants_written:", written)
    print("variants_with_pic_png:", pics)


if __name__ == "__main__":
    main()


