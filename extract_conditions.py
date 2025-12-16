#!/usr/bin/env python3
"""
Скрипт для извлечения условий задач из Word файлов
"""
import os
import re
from pathlib import Path

try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False
    print("Установите python-docx: pip install python-docx")

def extract_from_docx(file_path):
    """Извлечение текста из .docx файла"""
    try:
        doc = Document(file_path)
        text = []
        for para in doc.paragraphs:
            if para.text.strip():
                text.append(para.text)
        return '\n'.join(text)
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return None

def extract_from_doc_legacy(file_path):
    """Попытка извлечения из старого .doc файла через антиword или textract"""
    try:
        import subprocess
        # Пробуем использовать antiword если установлен
        result = subprocess.run(['antiword', file_path], 
                               capture_output=True, text=True, encoding='utf-8', errors='ignore')
        if result.returncode == 0:
            return result.stdout
    except:
        pass
    
    try:
        import textract
        return textract.process(file_path).decode('utf-8', errors='ignore')
    except:
        pass
    
    return None

def extract_task_conditions(doc_file, output_dir):
    """Извлечение условий задач из Word файла"""
    file_path = Path(doc_file)
    if not file_path.exists():
        print(f"Файл не найден: {doc_file}")
        return
    
    # Определяем номер задачи из имени файла
    match = re.search(r'ege(\d+)', file_path.stem)
    if not match:
        print(f"Не удалось определить номер задачи из {file_path.name}")
        return
    
    task_number = int(match.group(1))
    
    # Извлекаем текст
    text = None
    if file_path.suffix == '.docx':
        text = extract_from_docx(file_path)
    elif file_path.suffix == '.doc':
        text = extract_from_doc_legacy(file_path)
        if not text:
            print(f"Не удалось извлечь текст из {file_path.name}. Установите antiword или textract")
            return
    
    if not text:
        print(f"Не удалось извлечь текст из {file_path.name}")
        return
    
    # Создаем папку для условий
    conditions_dir = Path(output_dir) / 'conditions'
    conditions_dir.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем полный текст
    output_file = conditions_dir / f'task_{task_number}_full.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"Извлечено условие для задачи {task_number} -> {output_file}")
    
    # Пытаемся разбить на отдельные задачи (если в файле несколько)
    # Это зависит от формата файла, может потребоваться ручная настройка
    tasks = split_into_tasks(text, task_number)
    for idx, task_text in enumerate(tasks, 1):
        task_file = conditions_dir / f'task_{task_number}_{idx}.txt'
        with open(task_file, 'w', encoding='utf-8') as f:
            f.write(task_text)
        print(f"  -> Сохранена задача {task_number}-{idx}")

def split_into_tasks(text, task_number):
    """Разбиение текста на отдельные задачи"""
    # Паттерны для поиска начала задач
    patterns = [
        rf'Задача\s+{task_number}',
        rf'Задание\s+{task_number}',
        rf'№\s*{task_number}',
        rf'Задача\s+{task_number}\.',
    ]
    
    tasks = []
    lines = text.split('\n')
    current_task = []
    in_task = False
    
    for line in lines:
        # Проверяем, начинается ли новая задача
        is_new_task = any(re.search(pattern, line, re.IGNORECASE) for pattern in patterns)
        
        if is_new_task and current_task:
            tasks.append('\n'.join(current_task))
            current_task = [line]
            in_task = True
        elif in_task or is_new_task:
            current_task.append(line)
            in_task = True
    
    if current_task:
        tasks.append('\n'.join(current_task))
    
    # Если не удалось разбить, возвращаем весь текст как одну задачу
    if not tasks:
        tasks = [text]
    
    return tasks

def main():
    base_dir = Path(__file__).parent / 'desh' / 'ege2026kp'
    
    if not base_dir.exists():
        print(f"Директория не найдена: {base_dir}")
        return
    
    # Находим все Word файлы
    doc_files = list(base_dir.glob('ege*.doc')) + list(base_dir.glob('ege*.docx'))
    
    print(f"Найдено {len(doc_files)} Word файлов")
    
    for doc_file in sorted(doc_files):
        extract_task_conditions(doc_file, base_dir)

if __name__ == '__main__':
    main()

