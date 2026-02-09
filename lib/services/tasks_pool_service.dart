import 'kompege_tasks_service.dart';

/// Пул задач: только КЕГЭ (kompege_tasks.json).
/// Старые источники (ege1, ege2, ege3, desh/ege2026kp, tasks_conditions.json) удалены.
class TasksPoolService {
  final KompegeTasksService _kompegeService = KompegeTasksService();

  /// Есть ли задачи из КЕГЭ.
  Future<bool> hasKompegeTasks() async {
    return _kompegeService.hasTasks();
  }

  /// Случайное условие + ответ. [difficulty] — фильтр по сложности КЕГЭ (0–3).
  /// Возвращает null, если для номера нет задач (или нет после фильтра по сложности).
  Future<Map<String, dynamic>?> getRandomTaskConditionWithVariant(
    int taskNumber, {
    int? difficulty,
  }) async {
    final kompegeTask = await _kompegeService.getRandomTask(
      taskNumber,
      difficulty: difficulty,
    );
    if (kompegeTask == null) return null;
    return {
      'condition': kompegeTask.condition,
      'variant': null,
      'path': 'kompege',
      'answer': kompegeTask.answer,
    };
  }

  /// Список номеров задач, для которых есть хотя бы одна задача (только КЕГЭ).
  Future<List<int>> getAvailableTaskNumbers() async {
    if (!await hasKompegeTasks()) return [];
    return _kompegeService.getAvailableTaskNumbers();
  }

  /// Количество задач по номеру (только КЕГЭ). Для UI.
  Future<int> getTaskCountForNumber(int taskNumber, {int? difficulty}) async {
    return _kompegeService.getCountForNumber(taskNumber, difficulty: difficulty);
  }

  /// Условие случайной задачи по номеру (удобство).
  Future<String?> getRandomTaskCondition(int taskNumber, {int? difficulty}) async {
    final data = await getRandomTaskConditionWithVariant(
      taskNumber,
      difficulty: difficulty,
    );
    return data?['condition'] as String?;
  }
}
