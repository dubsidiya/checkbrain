#!/usr/bin/env python3
"""
Скрипт для анализа найденных и пропущенных задач в файле ege1.doc
"""
import subprocess
import re
from pathlib import Path

def analyze_tasks():
    """Анализ задач в файле ege1.doc"""
    
    # Читаем файл
    result = subprocess.run(['antiword', 'desh/ege2026kp/ege1.doc'], 
                           capture_output=True, text=True, encoding='utf-8', errors='ignore')
    text = result.stdout
    lines = text.split('\n')
    
    # Находим "Задачи для тренировки"
    training_start = None
    for i, line in enumerate(lines):
        if 'Задачи для тренировки' in line:
            training_start = i
            break
    
    if training_start is None:
        print("❌ Фраза 'Задачи для тренировки' не найдена!")
        return
    
    print(f"✅ Найдена фраза 'Задачи для тренировки' на строке {training_start+1}")
    print(f"📊 Всего строк после этой фразы: {len(lines) - training_start - 1}")
    print("=" * 80)
    
    # Находим все потенциальные начала задач
    all_potential_starts = []
    
    for i in range(training_start + 1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        prev_line_empty = i == 0 or not lines[i-1].strip()
        task_type = None
        confidence = "low"
        
        # 1. Строки с "число)"
        match = re.match(r'^(\d+)\)\s+', line)
        if match:
            found_num = int(match.group(1))
            is_time_only = bool(re.match(r'^\d+\)\s+\d+[:\.]\d+', line))
            is_short_answer = bool(re.match(r'^\d+\)\s+\d+\s+\d+\)', line))
            is_city_route = bool(re.match(r'^\d+\)\s+[А-Я]+(?:\s*–\s*[А-Я]+)+$', line))
            
            if prev_line_empty and len(line) > 25:
                if not (is_time_only or is_short_answer or is_city_route):
                    task_type = f"число) {found_num}"
                    confidence = "high"
            elif len(line) > 40 and found_num >= 10 and not (is_time_only or is_short_answer):
                task_type = f"число) {found_num}"
                confidence = "medium"
        
        # 2. Строки с метками
        if re.search(r'\([А-Яа-яA-ZЕГКР]+-?\d{4}\)', line):
            task_type = "метка"
            confidence = "high"
        
        # 3. Строки, начинающиеся с "На рисунке"
        if (line.startswith('На рисунке') or line.startswith('На рисунке справа')) and len(line) > 40:
            if prev_line_empty or len(line) > 50:
                if task_type is None:
                    task_type = "На рисунке"
                    confidence = "medium"
        
        # 4. Другие паттерны начала задач
        if task_type is None:
            if line.startswith('Определите') and len(line) > 30 and not line.startswith('Определите самое раннее время'):
                task_type = "Определите"
                confidence = "low"
            elif line.startswith('В таблице') and len(line) > 30:
                task_type = "В таблице"
                confidence = "low"
            elif line.startswith('Между') and len(line) > 40:
                task_type = "Между"
                confidence = "low"
            elif line.startswith('Путешественник') and len(line) > 40:
                task_type = "Путешественник"
                confidence = "low"
            elif line.startswith('Транспортная фирма') and len(line) > 40:
                task_type = "Транспортная фирма"
                confidence = "low"
            elif (line.startswith('Турист') or line.startswith('Турист-паломник')) and len(line) > 40:
                task_type = "Турист"
                confidence = "low"
            elif 'Каждому населённому пункту' in line and len(line) > 40:
                task_type = "Каждому населённому пункту"
                confidence = "low"
        
        if task_type:
            all_potential_starts.append((i+1, task_type, confidence, prev_line_empty, line[:60]))
    
    print(f"\n📋 Найдено потенциальных начал задач: {len(all_potential_starts)}")
    
    # Группируем по типу
    by_type = {}
    by_confidence = {"high": 0, "medium": 0, "low": 0}
    
    for line_num, task_type, confidence, prev_empty, text in all_potential_starts:
        if task_type not in by_type:
            by_type[task_type] = []
        by_type[task_type].append((line_num, confidence, prev_empty, text))
        by_confidence[confidence] += 1
    
    print(f"\n📊 По уверенности:")
    print(f"  Высокая: {by_confidence['high']}")
    print(f"  Средняя: {by_confidence['medium']}")
    print(f"  Низкая: {by_confidence['low']}")
    
    print(f"\n📊 По типам:")
    for task_type, items in sorted(by_type.items()):
        print(f"  {task_type:30s}: {len(items)} задач")
    
    # Проверяем, какие задачи уже извлечены
    conditions_dir = Path('desh/ege2026kp/conditions/1')
    extracted_count = 0
    if conditions_dir.exists():
        extracted_count = len(list(conditions_dir.glob('task_1_*.txt')))
    
    print(f"\n✅ Уже извлечено задач: {extracted_count}")
    print(f"🎯 Ожидается: 195")
    print(f"❌ Пропущено: {195 - extracted_count}")
    
    # Показываем примеры задач с низкой уверенностью (могут быть пропущены)
    print(f"\n⚠️  Примеры задач с низкой уверенностью (могут быть пропущены):")
    low_confidence = [item for item in all_potential_starts if item[2] == "low"]
    for line_num, task_type, confidence, prev_empty, text in low_confidence[:10]:
        empty_mark = "✓" if prev_empty else "✗"
        print(f"  Строка {line_num:4d} [{task_type:20s}] Пустая={empty_mark}: {text}")
    
    if len(low_confidence) > 10:
        print(f"  ... и еще {len(low_confidence) - 10} задач с низкой уверенностью")
    
    # Показываем последние найденные задачи
    print(f"\n📝 Последние 20 найденных задач:")
    for line_num, task_type, confidence, prev_empty, text in all_potential_starts[-20:]:
        conf_mark = "✓" if confidence == "high" else "?" if confidence == "medium" else "⚠"
        empty_mark = "✓" if prev_empty else "✗"
        print(f"  {conf_mark} Строка {line_num:4d} [{task_type:20s}] Пустая={empty_mark}: {text}")
    
    # Сохраняем полный список в файл
    output_file = Path('task_analysis.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Анализ задач из ege1.doc\n")
        f.write(f"=" * 80 + "\n\n")
        f.write(f"Найдено потенциальных начал задач: {len(all_potential_starts)}\n")
        f.write(f"Уже извлечено: {extracted_count}\n")
        f.write(f"Ожидается: 195\n")
        f.write(f"Пропущено: {195 - extracted_count}\n\n")
        f.write(f"Полный список:\n")
        f.write(f"-" * 80 + "\n")
        for line_num, task_type, confidence, prev_empty, text in all_potential_starts:
            conf_mark = "✓" if confidence == "high" else "?" if confidence == "medium" else "⚠"
            empty_mark = "✓" if prev_empty else "✗"
            f.write(f"{conf_mark} Строка {line_num:4d} [{task_type:20s}] Пустая={empty_mark}: {text}\n")
    
    print(f"\n💾 Полный анализ сохранен в файл: {output_file}")

if __name__ == '__main__':
    analyze_tasks()

