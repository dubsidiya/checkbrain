#!/usr/bin/env python3
"""
Скрипт для разбиения больших файлов с задачами на отдельные задачи
"""
import re
from pathlib import Path
from typing import List, Tuple

def split_file_into_tasks(file_path: Path) -> List[Tuple[int, str]]:
    """
    Разбивает файл на отдельные задачи
    Ищет паттерны типа: "96)", "(96)", "Задача 96", "96. " и т.д.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    tasks = []
    current_task_lines = []
    current_task_num = None
    
    # Паттерны для поиска начала задачи (в порядке приоритета)
    task_patterns = [
        (r'^\s*(\d+)\)\s*\([А-ЯЁ]\.', 'number_with_paren_author'),  # "96) (Е. Джобс)" или "  96) (А. Иванов)"
        (r'^\s*(\d+)\)\s', 'number_with_paren'),  # "96) " или "  96) "
        (r'^\s*\((\d+)\)\s', 'paren_number'),      # "(96) "
        (r'^\s*(\d+)\.\s', 'number_dot'),          # "96. "
        (r'^Задача\s+(\d+)[\.\s]', 'task_word'),   # "Задача 96"
        (r'^Задание\s+(\d+)[\.\s]', 'task_word2'), # "Задание 96"
    ]
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Пропускаем пустые строки в начале задачи
        if not stripped and not current_task_lines:
            i += 1
            continue
        
        # Проверяем, начинается ли новая задача
        found_task = False
        task_num = None
        
        for pattern, pattern_type in task_patterns:
            match = re.match(pattern, line, re.IGNORECASE)
            if match:
                task_num = int(match.group(1))
                found_task = True
                break
        
        if found_task and task_num is not None:
            # Сохраняем предыдущую задачу
            if current_task_lines and current_task_num is not None:
                task_text = '\n'.join(current_task_lines).strip()
                if len(task_text) > 50:  # Минимальная длина задачи
                    tasks.append((current_task_num, task_text))
            
            # Начинаем новую задачу
            current_task_lines = [line]
            current_task_num = task_num
        else:
            # Продолжаем текущую задачу
            if current_task_lines:
                current_task_lines.append(line)
            # Если еще не начали задачу, но есть текст - начинаем
            elif stripped and not found_task:
                # Возможно, это начало файла без номера задачи
                # Попробуем найти номер в следующих строках
                look_ahead = min(5, len(lines) - i)
                for j in range(i, i + look_ahead):
                    for pattern, _ in task_patterns:
                        match = re.match(pattern, lines[j], re.IGNORECASE)
                        if match:
                            task_num = int(match.group(1))
                            current_task_lines = [line]
                            current_task_num = task_num
                            found_task = True
                            break
                    if found_task:
                        break
        
        i += 1
    
    # Сохраняем последнюю задачу
    if current_task_lines and current_task_num is not None:
        task_text = '\n'.join(current_task_lines).strip()
        if len(task_text) > 50:
            tasks.append((current_task_num, task_text))
    
    return tasks

def process_all_task_files(base_dir: Path):
    """Обрабатывает все файлы задач и разбивает их на отдельные задачи"""
    conditions_dir = base_dir / 'conditions'
    
    if not conditions_dir.exists():
        print(f"❌ Папка conditions не найдена: {conditions_dir}")
        return
    
    total_tasks = 0
    total_files = 0
    
    # Проходим по всем папкам с номерами задач
    for task_dir in sorted(conditions_dir.iterdir()):
        if not task_dir.is_dir():
            continue
        
        try:
            task_number = int(task_dir.name)
        except ValueError:
            continue
        
        print(f"\n📋 Обработка задачи №{task_number}")
        
        # Обрабатываем все файлы в папке
        task_files = sorted(task_dir.glob('task_*.txt'))
        
        for task_file in task_files:
            print(f"  📄 {task_file.name}")
            
            # Разбиваем на отдельные задачи
            tasks = split_file_into_tasks(task_file)
            
            if len(tasks) == 0:
                print(f"    ⚠️  Не удалось разбить на задачи")
                continue
            
            print(f"    ✅ Найдено {len(tasks)} задач")
            
            # Удаляем старый файл
            task_file.unlink()
            
            # Сохраняем каждую задачу отдельно
            for task_num, task_text in tasks:
                new_file = task_dir / f'task_{task_number}_{task_num:03d}.txt'
                with open(new_file, 'w', encoding='utf-8') as f:
                    f.write(f"Задача №{task_number} (вариант {task_num})\n")
                    f.write("=" * 60 + "\n\n")
                    f.write(task_text)
                
                print(f"    💾 Сохранена задача {task_num} ({len(task_text)} символов)")
                total_tasks += 1
            
            total_files += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Обработано файлов: {total_files}")
    print(f"✅ Создано отдельных задач: {total_tasks}")

def main():
    base_dir = Path(__file__).parent / 'desh' / 'ege2026kp'
    
    if not base_dir.exists():
        print(f"❌ Директория не найдена: {base_dir}")
        return
    
    process_all_task_files(base_dir)
    
    print("\n💡 Теперь запустите create_tasks_json.py для обновления JSON файла")

if __name__ == '__main__':
    main()

