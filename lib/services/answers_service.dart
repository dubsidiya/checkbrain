import 'dart:io';
import 'package:csv/csv.dart';
import 'package:flutter/services.dart';
import 'package:path/path.dart' as path;

class AnswersService {
  String _getAnswersPath() {
    final currentDir = Directory.current.path;
    return path.join(currentDir, 'desh', 'ege2026kp', 'answers.csv');
  }
  
  Map<int, Map<int, String>>? _answersCache;

  Future<Map<int, Map<int, String>>> loadAnswers() async {
    if (_answersCache != null) {
      return _answersCache!;
    }

    // Сначала пробуем загрузить из assets (приоритет для мобильных устройств)
    try {
      final String data = await rootBundle.loadString('desh/ege2026kp/answers.csv');
      final List<List<dynamic>> csvData = const CsvToListConverter().convert(data);
      _answersCache = _parseAnswers(csvData);
      print('✅ Ответы загружены из assets (${_answersCache!.length} вариантов)');
      return _answersCache!;
    } catch (e) {
      print('⚠️ Ошибка загрузки ответов из assets: $e');
      
      // Fallback: пробуем загрузить из файловой системы (для десктопа)
      try {
        final file = File(_getAnswersPath());
        if (await file.exists()) {
          final String data = await file.readAsString();
          final List<List<dynamic>> csvData = const CsvToListConverter().convert(data);
          _answersCache = _parseAnswers(csvData);
          print('✅ Ответы загружены из файловой системы (${_answersCache!.length} вариантов)');
          return _answersCache!;
        }
      } catch (e2) {
        print('❌ Ошибка загрузки ответов из файловой системы: $e2');
      }
    }

    return {};
  }

  Map<int, Map<int, String>> _parseAnswers(List<List<dynamic>> csvData) {
    final Map<int, Map<int, String>> answers = {};
    
    if (csvData.isEmpty) return answers;

    // Первая строка - заголовки с номерами задач
    final headers = csvData[0];
    final taskNumbers = <int>[];
    
    for (int i = 1; i < headers.length; i++) {
      final header = headers[i].toString().trim();
      if (header.isEmpty) break;
      
      // Извлекаем номер задачи из заголовка (может быть "1", "7-2", "7-v" и т.д.)
      final taskNumStr = header.split('-')[0];
      final taskNum = int.tryParse(taskNumStr);
      if (taskNum != null) {
        taskNumbers.add(taskNum);
      }
    }

    // Остальные строки - варианты с ответами
    for (int rowIndex = 1; rowIndex < csvData.length; rowIndex++) {
      final row = csvData[rowIndex];
      if (row.isEmpty) continue;

      final variantNum = int.tryParse(row[0].toString().trim());
      if (variantNum == null) continue;

      answers[variantNum] = {};
      
      for (int colIndex = 0; colIndex < taskNumbers.length && colIndex + 1 < row.length; colIndex++) {
        final taskNum = taskNumbers[colIndex];
        final answer = row[colIndex + 1].toString().trim();
        
        // Убираем ссылки и лишние символы из ответа
        final cleanAnswer = _cleanAnswer(answer);
        if (cleanAnswer.isNotEmpty) {
          answers[variantNum]![taskNum] = cleanAnswer;
        }
      }
    }

    return answers;
  }

  String _cleanAnswer(String answer) {
    // Убираем ссылки и переносы строк
    return answer
        .split('\n')
        .where((line) => !line.contains('http') && !line.contains('youtu.be') && !line.contains('vk.com'))
        .join(' ')
        .trim();
  }

  String? getAnswer(int variantNumber, int taskNumber) {
    final answer = _answersCache?[variantNumber]?[taskNumber];
    if (answer == null) {
      print('⚠️ Ответ не найден: вариант $variantNumber, задача $taskNumber');
      print('   Доступные варианты в кэше: ${_answersCache?.keys.toList()?.take(10) ?? []}');
      if (_answersCache?[variantNumber] != null) {
        print('   Доступные задачи для варианта $variantNumber: ${_answersCache![variantNumber]!.keys.toList()}');
      }
    }
    return answer;
  }

  /// Извлечь внутренний номер варианта из текста условия
  /// Для задач 8, 17, 23 номер варианта указан в формате "N)" в начале текста
  static int? extractInternalVariantNumber(String? conditionText, int taskNumber) {
    if (conditionText == null || conditionText.isEmpty) return null;
    
    // Для задач 8, 17, 23 ищем паттерн "N)" в начале строки
    if (taskNumber == 8 || taskNumber == 17 || taskNumber == 23) {
      final lines = conditionText.split('\n');
      for (final line in lines) {
        final trimmed = line.trim();
        // Ищем паттерн "N)" где N - число
        final match = RegExp(r'^(\d+)\)').firstMatch(trimmed);
        if (match != null) {
          final variantNum = int.tryParse(match.group(1)!);
          if (variantNum != null) {
            return variantNum;
          }
        }
      }
    }
    
    return null;
  }
}

