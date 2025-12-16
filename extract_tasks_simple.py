#!/usr/bin/env python3
"""
Упрощенный скрипт для извлечения задач из Word файлов
Использует python-docx для .docx и предлагает конвертировать .doc в .docx
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
    print("❌ Установите python-docx: pip install python-docx")
    exit(1)

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
        print(f"  ❌ Ошибка при чтении: {e}")
        return ""

def split_into_tasks(text: str, task_number: int) -> List[Tuple[int, str]]:
    """Разбиение текста на отдельные задачи"""
    tasks = []
    lines = text.split('\n')
    current_task = []
    task_num = 1
    
    # Паттерны для поиска начала задач
    task_patterns = [
        rf'^Задача\s+{task_number}[\.\s]',
        rf'^Задание\s+{task_number}[\.\s]',
        rf'^№\s*{task_number}[\.\s]',
    ]
    
    # Также ищем любые задачи с номерами
    any_task_pattern = re.compile(r'^Задача\s+(\d+)[\.\s]', re.IGNORECASE)
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Проверяем, начинается ли новая задача
        is_new_task = any(re.search(p, line, re.IGNORECASE) for p in task_patterns)
        
        # Или это задача с другим номером (но того же типа)
        match = any_task_pattern.match(line)
        if match and not is_new_task:
            found_num = int(match.group(1))
            # Если это задача нужного номера или следующая после нужной
            if found_num == task_number or (current_task and found_num > task_number):
                is_new_task = True
        
        if is_new_task and current_task:
            # Сохраняем предыдущую задачу
            task_text = '\n'.join(current_task).strip()
            if len(task_text) > 100:  # Минимальная длина задачи
                tasks.append((task_num, task_text))
                task_num += 1
            current_task = []
        
        if is_new_task or current_task:
            current_task.append(lines[i])
        
        i += 1
    
    # Сохраняем последнюю задачу
    if current_task:
        task_text = '\n'.join(current_task).strip()
        if len(task_text) > 100:
            tasks.append((task_num, task_text))
    
    # Если не удалось разбить, возвращаем весь текст
    if not tasks:
        tasks = [(1, text.strip())]
    
    return tasks

def process_file(file_path: Path, output_base_dir: Path):
    """Обработка одного файла"""
    print(f"\n📄 {file_path.name}")
    
    # Определяем номер задачи
    match = re.search(r'ege(\d+)', file_path.stem)
    if not match:
        print(f"  ⚠️  Не удалось определить номер задачи")
        return
    
    task_number = int(match.group(1))
    print(f"  📋 Задача №{task_number}")
    
    # Извлекаем текст
    if file_path.suffix == '.docx':
        text = extract_text_from_docx(file_path)
    elif file_path.suffix == '.doc':
        print(f"  ⚠️  .doc файлы требуют конвертации в .docx")
        print(f"     Используйте: libreoffice --headless --convert-to docx {file_path.name}")
        return
    else:
        print(f"  ⚠️  Неподдерживаемый формат: {file_path.suffix}")
        return
    
    if not text or len(text.strip()) < 50:
        print(f"  ⚠️  Не удалось извлечь текст")
        return
    
    print(f"  ✅ Извлечено {len(text)} символов")
    
    # Разбиваем на задачи
    tasks = split_into_tasks(text, task_number)
    print(f"  📝 Найдено задач: {len(tasks)}")
    
    # Создаем папку
    task_dir = output_base_dir / 'conditions' / str(task_number)
    task_dir.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем каждую задачу
    for task_idx, task_text in tasks:
        task_file = task_dir / f'task_{task_number}_{task_idx:03d}.txt'
        with open(task_file, 'w', encoding='utf-8') as f:
            f.write(f"Задача №{task_number} (вариант {task_idx})\n")
            f.write("=" * 60 + "\n\n")
            f.write(task_text)
        print(f"  💾 {task_file.name} ({len(task_text)} символов)")

def main():
    base_dir = Path(__file__).parent / 'desh' / 'ege2026kp'
    
    if not base_dir.exists():
        print(f"❌ Директория не найдена: {base_dir}")
        return
    
    # Ищем только .docx файлы (или конвертированные)
    docx_files = sorted(list(base_dir.glob('ege*.docx')))
    
    if not docx_files:
        print(f"⚠️  .docx файлы не найдены")
        print(f"💡 Для .doc файлов используйте конвертацию:")
        print(f"   libreoffice --headless --convert-to docx *.doc")
        return
    
    print(f"📚 Найдено {len(docx_files)} .docx файлов")
    print("=" * 60)
    
    processed = 0
    for docx_file in docx_files:
        try:
            process_file(docx_file, base_dir)
            processed += 1
        except Exception as e:
            print(f"  ❌ Ошибка: {e}")
    
    print("\n" + "=" * 60)
    print(f"✅ Обработано: {processed}/{len(docx_files)}")
    print(f"📁 Условия в: {base_dir / 'conditions'}")

if __name__ == '__main__':
    main()

