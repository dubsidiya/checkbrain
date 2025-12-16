import 'dart:convert';
import 'dart:math';
import 'package:flutter/services.dart';

/// Сервис для загрузки условий задач из JSON файла
class TasksConditionsJsonService {
  static const String _assetsPath = 'assets/tasks_conditions.json';
  Map<String, dynamic>? _cachedData;
  final Random _rng = Random();

  /// Загружает все условия задач из JSON
  Future<Map<String, dynamic>> loadConditions() async {
    if (_cachedData != null) {
      return _cachedData!;
    }

    try {
      final String jsonString = await rootBundle.loadString(_assetsPath);
      _cachedData = json.decode(jsonString) as Map<String, dynamic>;
      return _cachedData!;
    } catch (e) {
      print('Error loading tasks conditions: $e');
      return {};
    }
  }

  /// Получить список условий для конкретного номера задачи
  Future<List<String>> getConditionsForTask(int taskNumber) async {
    final data = await loadConditions();
    final tasks = data['tasks'] as Map<String, dynamic>?;
    if (tasks == null) return [];

    final taskKey = taskNumber.toString();
    final conditions = tasks[taskKey];
    
    if (conditions is List) {
      return conditions.cast<String>();
    }
    
    return [];
  }

  /// Получить случайное условие для номера задачи
  Future<String?> getRandomCondition(int taskNumber) async {
    final conditions = await getConditionsForTask(taskNumber);
    if (conditions.isEmpty) return null;

    // Реальная случайность (чтобы не получать одно и то же при быстрых кликах)
    final index = _rng.nextInt(conditions.length);
    return conditions[index];
  }

  /// Получить количество доступных условий для номера задачи
  Future<int> getConditionCount(int taskNumber) async {
    final conditions = await getConditionsForTask(taskNumber);
    return conditions.length;
  }
}

