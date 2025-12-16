# Извлечение условий задач из Word файлов

## Установка зависимостей

Для извлечения условий из Word файлов нужно установить Python библиотеки:

```bash
pip install python-docx
```

Для старых .doc файлов (опционально):
```bash
# macOS
brew install antiword

# Или используйте textract
pip install textract
```

## Запуск скрипта

```bash
cd /Users/vladkharin/StudioProjects/checkbrain
python3 extract_conditions.py
```

Скрипт:
1. Найдет все файлы ege*.doc и ege*.docx в папке desh/ege2026kp/
2. Извлечет текст из каждого файла
3. Сохранит условия в папку desh/ege2026kp/conditions/
4. Каждое условие будет сохранено как task_<номер>_<индекс>.txt

## Структура файлов

После выполнения скрипта структура будет такой:
```
desh/ege2026kp/
  conditions/
    task_1_1.txt
    task_1_2.txt
    task_2_1.txt
    ...
```

## Примечание

Если скрипт не может извлечь текст из .doc файлов, установите antiword или textract.
Для .docx файлов достаточно python-docx.

