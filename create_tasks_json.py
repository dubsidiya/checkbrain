#!/usr/bin/env python3
"""
Скрипт для создания JSON файла с условиями задач из извлеченных файлов
"""
import json
import re
from pathlib import Path
from typing import Dict, List

def load_task_conditions(base_dir: Path) -> Dict[int, List[str]]:
    """Загружает все условия задач из папок conditions/"""
    conditions_dir = base_dir / 'conditions'
    tasks_dict: Dict[int, List[str]] = {}
    
    if not conditions_dir.exists():
        print(f"❌ Папка conditions не найдена: {conditions_dir}")
        return tasks_dict
    
    # Проходим по всем папкам с номерами задач
    for task_dir in sorted(conditions_dir.iterdir()):
        if not task_dir.is_dir():
            continue
        
        # Извлекаем номер задачи из имени папки
        try:
            task_number = int(task_dir.name)
        except ValueError:
            continue
        
        # Читаем все файлы задач в этой папке
        task_files = sorted(task_dir.glob('task_*.txt'))
        tasks_dict[task_number] = []
        
        for task_file in task_files:
            try:
                with open(task_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Убираем заголовок, если есть
                    lines = content.split('\n')
                    # Пропускаем первые 2-3 строки (заголовок и разделитель)
                    if len(lines) > 3 and '=' in lines[1]:
                        content = '\n'.join(lines[3:]).strip()
                    tasks_dict[task_number].append(content)
                    print(f"  ✅ Загружена задача {task_number} из {task_file.name} ({len(content)} символов)")
            except Exception as e:
                print(f"  ⚠️  Ошибка при чтении {task_file}: {e}")
    
    return tasks_dict

def create_tasks_json(base_dir: Path, output_file: Path):
    """Создает JSON файл с условиями задач"""
    print("📚 Загрузка условий задач...")
    tasks_dict = load_task_conditions(base_dir)
    
    if not tasks_dict:
        print("❌ Не найдено ни одной задачи")
        return
    
    total_tasks = sum(len(tasks) for tasks in tasks_dict.values())
    print(f"\n✅ Загружено {total_tasks} задач из {len(tasks_dict)} номеров")
    
    # Создаем структуру для JSON
    json_data = {
        "version": "1.0",
        "tasks": {}
    }
    
    for task_number, conditions in sorted(tasks_dict.items()):
        json_data["tasks"][str(task_number)] = conditions
    
    # Сохраняем JSON
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    
    file_size = output_file.stat().st_size / 1024 / 1024  # MB
    print(f"\n💾 JSON файл создан: {output_file}")
    print(f"   Размер: {file_size:.2f} MB")
    print(f"   Задач: {total_tasks}")
    print(f"   Номеров: {len(tasks_dict)}")

def main():
    base_dir = Path(__file__).parent / 'desh' / 'ege2026kp'
    output_file = Path(__file__).parent / 'assets' / 'tasks_conditions.json'
    
    if not base_dir.exists():
        print(f"❌ Директория не найдена: {base_dir}")
        return
    
    create_tasks_json(base_dir, output_file)
    
    print("\n" + "=" * 60)
    print("📝 Не забудьте добавить в pubspec.yaml:")
    print("   assets:")
    print("     - assets/tasks_conditions.json")

if __name__ == '__main__':
    main()

