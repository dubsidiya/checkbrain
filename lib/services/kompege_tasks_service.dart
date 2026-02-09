import 'dart:convert';
import 'dart:math';
import 'package:flutter/services.dart';

/// Задача из КЕГЭ (kompege): условие, ответ, сложность.
class KompegeTask {
  final int taskNumber;
  final String condition;
  final String answer;
  final int difficulty;

  KompegeTask({
    required this.taskNumber,
    required this.condition,
    required this.answer,
    required this.difficulty,
  });

  static KompegeTask fromJson(Map<String, dynamic> json) {
    return KompegeTask(
      taskNumber: (json['taskNumber'] as num).toInt(),
      condition: json['condition'] as String? ?? '',
      answer: json['answer'] as String? ?? '',
      difficulty: (json['difficulty'] as num?)?.toInt() ?? 0,
    );
  }
}

/// Сервис загрузки задач КЕГЭ из assets (компеге), с разбивкой по сложности.
class KompegeTasksService {
  static const String _assetPath = 'assets/kompege_tasks.json';
  List<KompegeTask>? _tasks;
  Map<int, List<int>>? _byTaskNumber; // taskNumber -> indices in _tasks
  Map<int, List<int>>? _byDifficulty; // difficulty -> indices in _tasks
  final Random _rng = Random();

  Future<List<KompegeTask>> _load() async {
    if (_tasks != null) return _tasks!;
    try {
      final String jsonString = await rootBundle.loadString(_assetPath);
      final List<dynamic> list = json.decode(jsonString) as List<dynamic>? ?? [];
      _tasks = list
          .map((e) => KompegeTask.fromJson(e as Map<String, dynamic>))
          .toList();

      _byTaskNumber = {};
      _byDifficulty = {};
      for (int i = 0; i < _tasks!.length; i++) {
        final t = _tasks![i];
        _byTaskNumber!.putIfAbsent(t.taskNumber, () => []).add(i);
        _byDifficulty!.putIfAbsent(t.difficulty, () => []).add(i);
      }
      return _tasks!;
    } catch (e) {
      print('KompegeTasksService: error loading $_assetPath: $e');
      _tasks = [];
      _byTaskNumber = {};
      _byDifficulty = {};
      return _tasks!;
    }
  }

  /// Есть ли вообще задачи (файл загружен и не пустой).
  Future<bool> hasTasks() async {
    final list = await _load();
    return list.isNotEmpty;
  }

  /// Список задач по номеру (1–27). Опционально фильтр по сложности.
  Future<List<KompegeTask>> getTasksForNumber(
    int taskNumber, {
    int? difficulty,
  }) async {
    await _load();
    final indices = _byTaskNumber?[taskNumber];
    if (indices == null || indices.isEmpty) return [];
    if (difficulty != null) {
      return indices
          .map((i) => _tasks![i])
          .where((t) => t.difficulty == difficulty)
          .toList();
    }
    return indices.map((i) => _tasks![i]).toList();
  }

  /// Случайная задача по номеру. Если задана [difficulty], только такие.
  Future<KompegeTask?> getRandomTask(
    int taskNumber, {
    int? difficulty,
  }) async {
    final list = await getTasksForNumber(taskNumber, difficulty: difficulty);
    if (list.isEmpty) return null;
    return list[_rng.nextInt(list.length)];
  }

  /// Количество задач по номеру (с опциональным фильтром по сложности).
  Future<int> getCountForNumber(int taskNumber, {int? difficulty}) async {
    final list = await getTasksForNumber(taskNumber, difficulty: difficulty);
    return list.length;
  }

  /// Уникальные уровни сложности в данных (0, 1, 2, 3).
  Future<List<int>> getDifficultyLevels() async {
    await _load();
    final levels = _byDifficulty?.keys.toList() ?? [];
    levels.sort();
    return levels;
  }

  /// Подписи для сложности (как на КЕГЭ).
  static String difficultyLabel(int d) {
    switch (d) {
      case 0:
        return 'Базовый';
      case 1:
        return 'Повышенный';
      case 2:
        return 'Высокий';
      case 3:
        return 'Очень высокий';
      default:
        return 'Уровень $d';
    }
  }
}
