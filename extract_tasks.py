#!/usr/bin/env python3
"""
Скрипт для извлечения задач из Word файлов и сохранения каждой задачи в отдельный файл
"""
import os
import re
from pathlib import Path
from typing import List, Tuple

try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False
    print("Установите python-docx: pip install python-docx")

try:
    import pdfplumber
    HAS_PDF = True
except ImportError:
    HAS_PDF = False
    print("Установите pdfplumber: pip install pdfplumber")

def extract_text_from_docx(file_path: Path) -> str:
    """Извлечение текста из .docx файла"""
    try:
        doc = Document(file_path)
        text_parts = []
        for para in doc.paragraphs:
            if para.text.strip():
                text_parts.append(para.text)
        return '\n'.join(text_parts)
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return ""

def split_tasks_from_pdf(pdf_path: Path) -> List[Tuple[int, str]]:
    """Разбиваем задачи из PDF (используем, если antiword даёт неполный результат)"""
    tasks: List[Tuple[int, str]] = []
    if not HAS_PDF:
        return tasks
    if not pdf_path.exists():
        return tasks

    try:
        lines: List[str] = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                lines.extend(page_text.split("\n"))
    except Exception as e:
        print(f"Ошибка чтения PDF {pdf_path}: {e}")
        return tasks

    # Ищем фразу "Задачи для тренировки"
    training_start = None
    for i, line in enumerate(lines):
        if "Задачи для тренировки" in line:
            training_start = i
            break
    if training_start is None:
        training_start = 0

    variant_starts: List[int] = []

    for i in range(training_start + 1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        prev_empty = i == 0 or not lines[i - 1].strip()

        # 1) число) ... — принимаем как старт, если не выглядит как короткий ответ
        num_match = re.match(r"^(\d+)\)\s+", line)
        if num_match and len(line) > 20:
            is_time_only = bool(re.match(r"^\d+\)\s+\d+[:\.]\d+", line))
            is_short_answer = bool(re.match(r"^\d+\)\s+\d+\s+\d+\)", line))
            if not is_time_only and not is_short_answer:
                variant_starts.append(i)
                continue

        # 2) Определите... — всегда считаем началом задачи
        if line.startswith("Определите") and len(line) > 30:
            variant_starts.append(i)
            continue

        # 3) Путешественник оказался...
        if line.startswith("Путешественник оказался") and len(line) > 30:
            variant_starts.append(i)
            continue

        # 4) Метки/рисунки
        if re.search(r"\([А-Яа-яA-ZЕГКР]+-?\d{4}\)", line):
            variant_starts.append(i)
            continue
        # Не добавляем строки "На рисунке..." как начало задач — они часто идут внутри условия

    variant_starts = sorted(set(variant_starts))

    for idx, start in enumerate(variant_starts):
        end = variant_starts[idx + 1] if idx + 1 < len(variant_starts) else len(lines)
        task_text = "\n".join(lines[start:end]).strip()
        if len(task_text) > 50:
            tasks.append((idx + 1, task_text))

    return tasks

def extract_text_from_doc(file_path: Path) -> str:
    """Попытка извлечения из старого .doc файла"""
    # Пробуем antiword
    try:
        import subprocess
        result = subprocess.run(
            ['antiword', str(file_path)],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore',
            timeout=30
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
    except Exception as e:
        print(f"antiword не сработал: {e}")
    
    # Пробуем textract
    try:
        import textract
        text = textract.process(str(file_path)).decode('utf-8', errors='ignore')
        if text.strip():
            return text
    except Exception as e:
        print(f"textract не сработал: {e}")
    
    return ""

def split_into_tasks(text: str, task_number: int) -> List[Tuple[int, str]]:
    """
    Разбиение текста на отдельные задачи
    Возвращает список кортежей (номер_задачи_в_файле, текст_задачи)
    """
    tasks = []
    lines = text.split('\n')
    
    # Ищем фразу "Задачи для тренировки" - после неё начинаются задачи
    training_start = None
    for i, line in enumerate(lines):
        if 'Задачи для тренировки' in line:
            training_start = i
            break
    
    # Если не нашли, ищем альтернативные варианты
    if training_start is None:
        for i, line in enumerate(lines):
            if 'тренировки' in line.lower() or 'тренировочные' in line.lower():
                training_start = i
                break
    
    # Если нашли начало тренировочных задач, ищем все задачи после этой строки
    variant_starts = []
    
    if training_start is not None:
        # После фразы "Задачи для тренировки" ищем ВСЕ задачи:
        # 1. Строки с "число)" после пустой строки (основные задачи)
        # 2. Строки с метками типа "(ЕГЭ-2022)", "(ЕГКР-2025)", "(Апробация-2025)"
        # 3. Строки, начинающиеся с "На рисунке справа схема дорог..."
        
        for i in range(training_start + 1, len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            # Ищем паттерн "число) текст"
            prev_line_empty = i == 0 or not lines[i-1].strip()
            match = re.match(r'^(\d+)\)\s+', line)
            
            if match:
                found_num = int(match.group(1))
                
                # Проверяем, что это не просто вариант ответа
                is_time_only = bool(re.match(r'^\d+\)\s+\d+[:\.]\d+', line))
                is_short_answer = bool(re.match(r'^\d+\)\s+\d+\s+\d+\)', line))
                is_city_route = bool(re.match(r'^\d+\)\s+[А-Я]+(?:\s*–\s*[А-Я]+)+$', line))
                
                # Вариант задачи должен:
                # 1. Идти после пустой строки (или быть в начале)
                # 2. Быть достаточно длинным (не просто "1) 16:15")
                # 3. Не быть вариантом ответа
                if prev_line_empty and len(line) > 25:
                    if not (is_time_only or is_short_answer or is_city_route):
                        variant_starts.append(i)
                # Также проверяем длинные строки даже без пустой строки перед ними
                elif len(line) > 40 and not (is_time_only or is_short_answer):
                    # Но только если номер >= 10 (чтобы не захватить варианты ответов)
                    if found_num >= 10:
                        variant_starts.append(i)
            
            # Также ищем задачи с метками типа "(ЕГЭ-2022)", "(ЕГКР-2025)" и т.д.
            if re.search(r'\([А-Яа-яA-ZЕГКР]+-?\d{4}\)', line):
                # Проверяем, что это не просто упоминание в тексте
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "Определите" (часто начало задачи)
            if line.startswith('Определите') and len(line) > 30:
                # Принимаем все "Определите..." (включая "самое раннее время"), т.к. это отдельные задачи
                # Нередко идут без пустой строки после предыдущей задачи, поэтому не требуем пустую строку
                if i not in variant_starts:
                    variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "В таблице" (начало задачи с таблицей)
            if line.startswith('В таблице') and len(line) > 30:
                if prev_line_empty or len(line) > 40:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "Между" (часто начало задачи про графы)
            if line.startswith('Между') and len(line) > 40:
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "Путешественник" (задачи про расписание)
            if line.startswith('Путешественник') and len(line) > 40:
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки "Путешественник оказался" (начало новой задачи)
            if line.startswith('Путешественник оказался') and len(line) > 30:
                if prev_line_empty or len(line) > 40:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "Транспортная фирма"
            if line.startswith('Транспортная фирма') and len(line) > 40:
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки, начинающиеся с "Турист" или "Турист-паломник"
            if (line.startswith('Турист') or line.startswith('Турист-паломник')) and len(line) > 40:
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
            
            # Ищем строки с "Каждому населённому пункту" (часто начало задачи)
            if 'Каждому населённому пункту' in line and len(line) > 40:
                if prev_line_empty or len(line) > 50:
                    if i not in variant_starts:
                        variant_starts.append(i)
    
    # Если не нашли через "Задачи для тренировки", используем старую логику
    if not variant_starts:
        # Паттерны для поиска начала задач
        patterns = [
            rf'Задача\s+{task_number}[\.\s]',
            rf'Задание\s+{task_number}[\.\s]',
            rf'№\s*{task_number}[\.\s]',
            rf'Задача\s+{task_number}\.',
            rf'^Задача\s+{task_number}\s',
            rf'^Задание\s+{task_number}\s',
            rf'Задача\s+{task_number}[\)\:]',
            rf'Задание\s+{task_number}[\)\:]',
        ]
        
        # Сначала проверяем стандартные паттерны
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            is_standard_pattern = any(re.search(p, line, re.IGNORECASE) for p in patterns)
            if is_standard_pattern:
                variant_starts.append(i)
    
    # Затем ищем все строки, начинающиеся с числа и скобки после пустой строки
    # Это могут быть варианты задач
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        prev_line_empty = not lines[i-1].strip()
        
        # Ищем паттерн "число) текст"
        match = re.match(r'^(\d+)\)\s+', line)
        if match:
            found_num = int(match.group(1))
            
            # Вариант задачи должен:
            # 1. Идти после пустой строки
            # 2. Иметь длину > 25 символов (не просто вариант ответа типа "1) 16:15")
            if prev_line_empty and len(line) > 25:
                # Проверяем, что это не просто вариант ответа (только время/числа)
                is_time_only = bool(re.match(r'^\d+\)\s+\d+[:\.]\d+', line))
                is_short_answer = bool(re.match(r'^\d+\)\s+\d+\s+\d+\)', line))  # "1) 16:15   2) 18:15"
                
                if not is_time_only and not is_short_answer:
                    # Это похоже на вариант задачи
                    variant_starts.append(i)
            # Также проверяем номера >= 10 даже без пустой строки, если строка длинная
            elif found_num >= 10 and len(line) > 40:
                variant_starts.append(i)
            # В начале файла может быть описание задачи
            elif i < 50 and found_num == task_number and len(line) > 30:
                variant_starts.append(i)
    
    # Убираем дубликаты и сортируем
    variant_starts = sorted(set(variant_starts))
    
    # Если нашли мало вариантов, пробуем более агрессивный поиск
    # Ищем все строки с номерами после пустой строки
    if len(variant_starts) < 100:
        for i in range(1, len(lines)):
            line = lines[i].strip()
            if not line:
                continue
            
            prev_line_empty = not lines[i-1].strip()
            
            # Ищем любую строку с номером и скобкой после пустой строки
            match = re.match(r'^(\d+)\)\s+', line)
            if match:
                found_num = int(match.group(1))
                
                # Проверяем условия для варианта задачи
                if prev_line_empty and len(line) > 25:
                    # Проверяем, что это не просто вариант ответа
                    is_time_only = bool(re.match(r'^\d+\)\s+\d+[:\.]\d+', line))
                    is_short_answer = bool(re.match(r'^\d+\)\s+\d+\s+\d+\)', line))
                    # Варианты ответов обычно короткие и содержат только числа/время
                    is_answer_variant = len(line) < 40 and (is_time_only or is_short_answer or 
                                                           bool(re.match(r'^\d+\)\s+\d+', line)))
                    
                    if not is_answer_variant:
                        if i not in variant_starts:
                            variant_starts.append(i)
                # Также проверяем номера >= 10 даже без пустой строки, если строка длинная
                elif found_num >= 10 and len(line) > 40:
                    if i not in variant_starts:
                        variant_starts.append(i)
        
        variant_starts = sorted(set(variant_starts))
    
    # Разбиваем текст на задачи по найденным началам
    if variant_starts:
        for idx, start_line in enumerate(variant_starts):
            end_line = variant_starts[idx + 1] if idx + 1 < len(variant_starts) else len(lines)
            task_lines = lines[start_line:end_line]
            task_text = '\n'.join(task_lines).strip()
            
            if task_text and len(task_text) > 50:  # Минимальная длина задачи
                tasks.append((idx + 1, task_text))
    else:
        # Если не нашли варианты, возвращаем весь текст как одну задачу
        tasks = [(1, text.strip())]

    # Дополнительное разбиение внутри одной задачи по строкам вида "1) ...", "2) ..." и т.д.
    def split_inner_numbered(task_text: str) -> List[str]:
        inner_lines = task_text.split('\n')
        inner_starts: List[int] = []
        for i, ln in enumerate(inner_lines):
            s = ln.strip()
            m = re.match(r'^(\d+)\)\s+', s)
            if not m:
                continue
            # пропускаем совсем короткие строки без текста
            if len(s) < 30:
                continue
            # должны быть буквы (а не только числа/время)
            if not re.search(r'[А-Яа-яA-Za-z]', s):
                continue
            inner_starts.append(i)
        if len(inner_starts) <= 1:
            return [task_text]
        parts: List[str] = []
        for idx, st in enumerate(inner_starts):
            end = inner_starts[idx + 1] if idx + 1 < len(inner_starts) else len(inner_lines)
            sub = '\n'.join(inner_lines[st:end]).strip()
            if len(sub) > 30:
                parts.append(sub)
        return parts or [task_text]

    # Применяем внутреннее разбиение только для некоторых номеров задач,
    # где в одном блоке реально лежит несколько самостоятельных условий,
    # помеченных 1), 2), 3) ...
    # 8 — перебор слов; 17 — перебор чисел; 23 — калькулятор.
    if task_number in (8, 17, 23):
        final_tasks: List[Tuple[int, str]] = []
        counter = 1
        for _, t_text in tasks:
            subs = split_inner_numbered(t_text)
            for sub in subs:
                final_tasks.append((counter, sub))
                counter += 1
        return final_tasks

    # Для остальных номеров возвращаем задачи как есть
    return tasks

def process_word_file(file_path: Path, output_base_dir: Path):
    """Обработка одного Word файла"""
    print(f"\nОбработка: {file_path.name}")
    
    # Определяем номера задач из имени файла
    # Специальная обработка для ege1921.doc (задачи 19, 20, 21)
    task_numbers = []
    if '1921' in file_path.stem or '19-21' in file_path.stem:
        task_numbers = [19, 20, 21]
        print(f"  📋 Задачи №19, 20, 21 (из одного файла)")
    else:
        match = re.search(r'ege(\d+)', file_path.stem)
        if not match:
            print(f"  ⚠️  Не удалось определить номер задачи из {file_path.name}")
            return
        task_numbers = [int(match.group(1))]
        print(f"  📋 Задача №{task_numbers[0]}")
    
    # Извлекаем текст
    text = ""
    if file_path.suffix == '.docx':
        if not HAS_DOCX:
            print(f"  ❌ python-docx не установлен. Установите: pip install python-docx")
            return
        text = extract_text_from_docx(file_path)
    elif file_path.suffix == '.doc':
        text = extract_text_from_doc(file_path)
    
    if not text or len(text.strip()) < 50:
        print(f"  ⚠️  Не удалось извлечь текст или текст слишком короткий")
        return
    
    print(f"  ✅ Извлечено {len(text)} символов")
    
    # Обрабатываем каждую задачу из списка
    for task_number in task_numbers:
        # Разбиваем на отдельные задачи
        tasks = split_into_tasks(text, task_number)

        # Для задачи №1 пробуем разбиение из PDF (если оно даёт больше вариантов)
        if task_number == 1:
            pdf_path = file_path.with_suffix(".pdf")
            pdf_tasks = split_tasks_from_pdf(pdf_path) if HAS_PDF else []
            if pdf_tasks:
                # Добавляем уникальные задачи из PDF, которых нет в antiword-разбиении
                sig = lambda t: (t[1][:120].strip().lower())
                existing = {sig(t) for t in tasks}
                added = 0
                for _, txt in pdf_tasks:
                    if len(tasks) >= 195:
                        break
                    sig_txt = sig((0, txt))
                    if sig_txt not in existing:
                        tasks.append((len(tasks) + 1, txt))
                        existing.add(sig_txt)
                        added += 1
                if len(tasks) > 195:
                    tasks = tasks[:195]
                if added:
                    print(f"  🔄 Добавили из PDF: +{added} (итого {len(tasks)})")
        print(f"  📝 Задача №{task_number}: найдено {len(tasks)} вариантов")
        
        # Создаем папку для этого номера задачи
        task_dir = output_base_dir / 'conditions' / str(task_number)
        task_dir.mkdir(parents=True, exist_ok=True)
        
        # Сохраняем каждую задачу в отдельный файл
        for task_idx, task_text in tasks:
            task_file = task_dir / f'task_{task_number}_{task_idx:03d}.txt'
            
            with open(task_file, 'w', encoding='utf-8') as f:
                f.write(f"Задача №{task_number} (вариант {task_idx})\n")
                f.write("=" * 50 + "\n\n")
                f.write(task_text)
            
            print(f"  💾 Сохранено: {task_file.name} ({len(task_text)} символов)")

def main():
    base_dir = Path(__file__).parent / 'desh' / 'ege2026kp'
    
    if not base_dir.exists():
        print(f"❌ Директория не найдена: {base_dir}")
        return
    
    # Находим все Word файлы
    doc_files = sorted(list(base_dir.glob('ege*.doc')) + list(base_dir.glob('ege*.docx')))
    
    if not doc_files:
        print(f"❌ Word файлы не найдены в {base_dir}")
        return
    
    print(f"📚 Найдено {len(doc_files)} Word файлов")
    print("=" * 60)
    
    # Создаем папку для условий
    output_dir = base_dir / 'conditions'
    output_dir.mkdir(exist_ok=True)
    
    # Обрабатываем каждый файл
    processed = 0
    for doc_file in doc_files:
        try:
            process_word_file(doc_file, base_dir)
            processed += 1
        except Exception as e:
            print(f"  ❌ Ошибка при обработке {doc_file.name}: {e}")
    
    print("\n" + "=" * 60)
    print(f"✅ Обработано файлов: {processed}/{len(doc_files)}")
    print(f"📁 Условия сохранены в: {output_dir}")

if __name__ == '__main__':
    main()

