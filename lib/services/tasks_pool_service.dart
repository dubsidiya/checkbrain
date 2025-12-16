import 'dart:convert';
import 'dart:io';
import 'dart:math';
import 'package:flutter/services.dart';
import 'package:path/path.dart' as path;
import 'tasks_conditions_json_service.dart';

/// Сервис для работы с пулом задач (как на kompege.ru)
/// Хранит все доступные задачи по номерам и позволяет выбирать случайные
class TasksPoolService {
  final TasksConditionsJsonService _jsonService = TasksConditionsJsonService();
  final Random _rng = Random();
  Map<int, List<String>>? _assetTaskFilesCache;
  Map<String, dynamic>? _assetManifestCache;

  String _getBasePath() {
    final currentDir = Directory.current.path;
    return path.join(currentDir, 'desh', 'ege2026kp');
  }

  /// Загрузить условие задачи из assets по номеру задачи и варианта.
  /// Путь в assets: desh/ege2026kp/conditions/<taskNumber>/task_<taskNumber>_<variant>.txt
  Future<String?> _loadConditionFromAssets(
    int taskNumber,
    int variantNumber,
  ) async {
    final assetPath =
        'desh/ege2026kp/conditions/$taskNumber/task_${taskNumber}_${variantNumber.toString().padLeft(3, '0')}.txt';
    try {
      final data = await rootBundle.loadString(assetPath);
      if (data.isNotEmpty) {
        print(
          '✅ Загружено условие из assets: $assetPath (${data.length} символов)',
        );
        return data;
      }
      print('⚠️ Файл в assets пустой: $assetPath');
    } catch (e) {
      // Пробуем альтернативные пути (на случай, если структура assets отличается)
      final altPaths = [
        'desh/ege2026kp/conditions/$taskNumber/task_${taskNumber}_${variantNumber}.txt',
        'packages/checkbrain/desh/ege2026kp/conditions/$taskNumber/task_${taskNumber}_${variantNumber.toString().padLeft(3, '0')}.txt',
      ];
      for (final altPath in altPaths) {
        try {
          final data = await rootBundle.loadString(altPath);
          if (data.isNotEmpty) {
            print('✅ Загружено условие из альтернативного пути: $altPath');
            return data;
          }
        } catch (_) {
          continue;
        }
      }
      print('❌ Ошибка загрузки из assets: $assetPath - $e');
      print('   Пробовали альтернативные пути: ${altPaths.join(", ")}');
    }
    return null;
  }

  Future<Map<String, dynamic>> _loadAssetManifest() async {
    if (_assetManifestCache != null) return _assetManifestCache!;
    final jsonStr = await rootBundle.loadString('AssetManifest.json');
    _assetManifestCache = (jsonDecode(jsonStr) as Map).cast<String, dynamic>();
    return _assetManifestCache!;
  }

  /// Получить список файлов условий для номера задачи из assets (мобилка).
  Future<List<String>> _getAssetTaskFilesForNumber(int taskNumber) async {
    _assetTaskFilesCache ??= {};
    if (_assetTaskFilesCache!.containsKey(taskNumber)) {
      return _assetTaskFilesCache![taskNumber]!;
    }

    try {
      final manifest = await _loadAssetManifest();
      final prefix = 'desh/ege2026kp/conditions/$taskNumber/';
      final files =
          manifest.keys
              .where((k) => k.startsWith(prefix) && k.endsWith('.txt'))
              .toList()
            ..sort();
      _assetTaskFilesCache![taskNumber] = files;
      return files;
    } catch (e) {
      print('❌ Не удалось прочитать AssetManifest.json: $e');
      _assetTaskFilesCache![taskNumber] = const [];
      return const [];
    }
  }

  int? _extractVariantFromTaskFileName(String assetOrFilePath, int taskNumber) {
    final base = path.basenameWithoutExtension(assetOrFilePath);
    final m = RegExp(r'^task_(\d+)_(\d+)$').firstMatch(base);
    if (m == null) return null;
    final tn = int.tryParse(m.group(1)!);
    final vn = int.tryParse(m.group(2)!);
    if (tn == taskNumber && vn != null) return vn;
    return null;
  }

  /// Случайное условие + номер варианта условия (для правильного ответа из CSV).
  /// Работает на Android/iOS через assets, на десктопе — через файловую систему.
  Future<Map<String, dynamic>?> getRandomTaskConditionWithVariant(
    int taskNumber,
  ) async {
    // 1) На мобильных: пробуем выбрать случайный asset-файл из AssetManifest
    try {
      final assetFiles = await _getAssetTaskFilesForNumber(taskNumber);
      if (assetFiles.isNotEmpty) {
        final picked = assetFiles[_rng.nextInt(assetFiles.length)];
        final condition = await rootBundle.loadString(picked);
        final variant = _extractVariantFromTaskFileName(picked, taskNumber);
        return {'condition': condition, 'variant': variant, 'path': picked};
      }
    } catch (e) {
      print('Error getting random condition from assets: $e');
    }

    // 2) На десктопе/CLI: случайный файл из файловой системы
    final files = await getTaskFilesForNumber(taskNumber);
    if (files.isNotEmpty) {
      final picked = files[_rng.nextInt(files.length)];
      final condition = await getTaskCondition(picked);
      if (condition != null) {
        final variant = _extractVariantFromTaskFileName(picked, taskNumber);
        return {'condition': condition, 'variant': variant, 'path': picked};
      }
    }

    // 3) Fallback: JSON (если вдруг есть)
    final jsonCond = await _jsonService.getRandomCondition(taskNumber);
    if (jsonCond != null) {
      return {'condition': jsonCond, 'variant': null, 'path': null};
    }
    return null;
  }

  /// Получить список всех доступных задач по номеру
  Future<List<String>> getTaskFilesForNumber(int taskNumber) async {
    final List<String> files = [];

    // Ищем условия в папке conditions/<номер_задачи>/
    final conditionsDir = path.join(
      _getBasePath(),
      'conditions',
      taskNumber.toString(),
    );
    try {
      final dir = Directory(conditionsDir);
      if (await dir.exists()) {
        await for (final entity in dir.list()) {
          if (entity is File) {
            final ext = path.extension(entity.path).toLowerCase();
            // Ищем все текстовые файлы с условиями
            if (ext == '.txt') {
              files.add(entity.path);
            }
          }
        }
      }
    } catch (e) {
      print('Error reading conditions dir: $e');
    }

    // Если не нашли в новой структуре, ищем в старой
    if (files.isEmpty) {
      final oldConditionsDir = path.join(_getBasePath(), 'conditions');
      try {
        final dir = Directory(oldConditionsDir);
        if (await dir.exists()) {
          await for (final entity in dir.list()) {
            if (entity is File) {
              final name = path.basenameWithoutExtension(entity.path);
              if (name.startsWith('task_${taskNumber}_')) {
                files.add(entity.path);
              }
            }
          }
        }
      } catch (e) {
        print('Error reading old conditions dir: $e');
      }
    }

    // Ищем решения в папке solve (как дополнительный источник условий)
    // Для задачи №1 могут быть условия в других форматах
    final solveDir = path.join(_getBasePath(), '${taskNumber}solve');
    try {
      final dir = Directory(solveDir);
      if (await dir.exists()) {
        await for (final entity in dir.list()) {
          if (entity is File) {
            final ext = path.extension(entity.path).toLowerCase();
            // Добавляем текстовые файлы из solve папки тоже
            if (ext == '.txt' || ['.py', '.pas', '.cpp'].contains(ext)) {
              // Добавляем только если нет условий в conditions
              if (files.isEmpty || ext == '.txt') {
                files.add(entity.path);
              }
            }
          }
        }
      }
    } catch (e) {
      print('Error reading solve dir: $e');
    }

    return files;
  }

  /// Получить путь к файлу задачи по номеру и номеру варианта (ТОЛЬКО для файловой системы, не для assets)
  /// Ожидается структура вида desh/ege2026kp/conditions/<taskNumber>/task_<taskNumber>_<variant>.txt
  Future<String?> getTaskFilePathForVariant(
    int taskNumber,
    int variantNumber,
  ) async {
    final conditionsDir = path.join(
      _getBasePath(),
      'conditions',
      taskNumber.toString(),
    );
    final dir = Directory(conditionsDir);
    if (!await dir.exists()) {
      // На Android/iOS эта папка, скорее всего, отсутствует — в этом случае работаем только через assets
      print(
        '⚠️ Папка conditions/$taskNumber не существует в файловой системе: $conditionsDir',
      );
      return null;
    }

    final fileName =
        'task_${taskNumber}_${variantNumber.toString().padLeft(3, '0')}.txt';
    final fullPath = path.join(conditionsDir, fileName);
    final file = File(fullPath);
    if (await file.exists()) {
      print('✅ Найден файл условия в файловой системе: $fullPath');
      return fullPath;
    }
    print('⚠️ Файл условия не найден в файловой системе: $fullPath');
    return null;
  }

  /// Получить изображения для задачи (графы и т.д.)
  /// Ищет изображения в папке conditions/<номер_задачи>/ с тем же базовым именем, что и файл условия
  Future<List<String>> getImagesForCondition(
    int taskNumber,
    String conditionFilePath,
  ) async {
    final List<String> images = [];
    // 1) If condition path looks like an asset path, find matching image assets via AssetManifest
    if (conditionFilePath.startsWith('desh/') ||
        conditionFilePath.startsWith('packages/')) {
      try {
        final manifest = await _loadAssetManifest();
        final prefix = path.dirname(conditionFilePath) + '/';
        final baseName = path.basenameWithoutExtension(conditionFilePath);
        final assetImages = manifest.keys.where((k) {
          if (!k.startsWith(prefix)) return false;
          final ext = path.extension(k).toLowerCase();
          if (![
            '.png',
            '.jpg',
            '.jpeg',
            '.gif',
            '.svg',
            '.webp',
          ].contains(ext)) {
            return false;
          }
          return path.basenameWithoutExtension(k) == baseName;
        }).toList()..sort();
        images.addAll(assetImages.cast<String>());
        return images;
      } catch (e) {
        print('Error reading image assets for condition: $e');
        // Fall through to filesystem attempt
      }
    }

    try {
      final conditionsDir = path.join(
        _getBasePath(),
        'conditions',
        taskNumber.toString(),
      );
      final baseName = path.basenameWithoutExtension(conditionFilePath);

      final dir = Directory(conditionsDir);
      if (await dir.exists()) {
        await for (final entity in dir.list()) {
          if (entity is File) {
            final ext = path.extension(entity.path).toLowerCase();
            final fileBaseName = path.basenameWithoutExtension(entity.path);

            // Ищем изображения с тем же базовым именем
            if (['.png', '.jpg', '.jpeg', '.gif', '.svg'].contains(ext) &&
                fileBaseName == baseName) {
              images.add(entity.path);
            }
          }
        }
      }
    } catch (e) {
      print('Error reading images for condition: $e');
    }
    return images;
  }

  Future<bool> _assetExists(String assetPath) async {
    try {
      final manifest = await _loadAssetManifest();
      return manifest.containsKey(assetPath);
    } catch (_) {
      return false;
    }
  }

  /// Get images referenced inside the condition text (e.g. "[pic]").
  ///
  /// This handles cases like task 14 where a single variant contains multiple sub-items:
  ///   82) ... [pic]
  ///   83) ... [pic]
  /// and the images are stored as:
  ///   conditions/14/task_14_082.png
  ///   conditions/14/task_14_083.png
  ///
  /// Also keeps the old behavior: include images that share the same base name as the condition file.
  Future<List<String>> getImagesForTaskContent(
    int taskNumber,
    String taskContent, {
    String? conditionPath,
    int? variantNumber,
  }) async {
    final exts = const ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'];
    final List<String> ordered = [];
    final Set<String> seen = {};

    Future<void> addImagePath(String p) async {
      if (seen.add(p)) ordered.add(p);
    }

    // 1) Images with the same base name as the condition file.
    if (conditionPath != null && conditionPath.isNotEmpty) {
      final baseImages = await getImagesForCondition(taskNumber, conditionPath);
      for (final img in baseImages) {
        await addImagePath(img);
      }
    }

    // 2) Images referenced as "[pic]" (extract leading marker number in the same line).
    final picRegex = RegExp(
      r'^\s*(\d{1,4})\)\s*.*?\[pic\]',
      caseSensitive: false,
      multiLine: true,
    );
    final matches = picRegex.allMatches(taskContent).toList();
    for (final m in matches) {
      final n = int.tryParse(m.group(1) ?? '');
      if (n == null) continue;
      final base = 'task_${taskNumber}_${n.toString().padLeft(3, '0')}';
      // Prefer assets if available, else filesystem.
      for (final ext in exts) {
        final assetPath = 'desh/ege2026kp/conditions/$taskNumber/$base$ext';
        if (await _assetExists(assetPath)) {
          await addImagePath(assetPath);
          break;
        }
        // filesystem fallback
        final fsPath = path.join(
          _getBasePath(),
          'conditions',
          taskNumber.toString(),
          '$base$ext',
        );
        if (await File(fsPath).exists()) {
          await addImagePath(fsPath);
          break;
        }
      }
    }

    // 3) If there is a "[pic]" without a leading number, fall back to current variant number.
    if (taskContent.toLowerCase().contains('[pic]') &&
        matches.isEmpty &&
        variantNumber != null) {
      final base =
          'task_${taskNumber}_${variantNumber.toString().padLeft(3, '0')}';
      for (final ext in exts) {
        final assetPath = 'desh/ege2026kp/conditions/$taskNumber/$base$ext';
        if (await _assetExists(assetPath)) {
          await addImagePath(assetPath);
          break;
        }
        final fsPath = path.join(
          _getBasePath(),
          'conditions',
          taskNumber.toString(),
          '$base$ext',
        );
        if (await File(fsPath).exists()) {
          await addImagePath(fsPath);
          break;
        }
      }
    }

    return ordered;
  }

  /// Asset path to a condition file for a specific variant.
  /// Example: desh/ege2026kp/conditions/14/task_14_081.txt
  String getTaskAssetPathForVariant(int taskNumber, int variantNumber) {
    return 'desh/ege2026kp/conditions/$taskNumber/'
        'task_${taskNumber}_${variantNumber.toString().padLeft(3, '0')}.txt';
  }

  /// Получить количество доступных задач по номеру
  /// Считает задачи из всех источников.
  /// Источник истины:
  ///  1) assets (если есть — это то, что реально попадёт в APK/IPA)
  ///  2) файловая система (десктоп/CLI)
  ///  3) JSON (fallback, если нет файлов)
  Future<int> getTaskCountForNumber(int taskNumber) async {
    // 1) assets (мобилка/универсально)
    final assetFiles = await _getAssetTaskFilesForNumber(taskNumber);
    if (assetFiles.isNotEmpty) return assetFiles.length;

    // 2) файловая система (десктоп)
    final files = await getTaskFilesForNumber(taskNumber);
    if (files.isNotEmpty) return files.length;

    // 3) JSON fallback
    try {
      final jsonCount = await _jsonService.getConditionCount(taskNumber);
      return jsonCount;
    } catch (e) {
      print('Error getting count from JSON: $e');
      return 0;
    }
  }

  /// Получить случайную задачу по номеру
  Future<String?> getRandomTaskForNumber(int taskNumber) async {
    // ВАЖНО: здесь возвращаем только ПУТЬ к файлу (файловая система).
    // На Android/iOS файловой системы с assets нет — используйте getRandomTaskConditionWithVariant().
    final files = await getTaskFilesForNumber(taskNumber);
    if (files.isEmpty) return null;

    return files[_rng.nextInt(files.length)];
  }

  /// Получить условие задачи из файла
  Future<String?> getTaskCondition(String filePath) async {
    try {
      final file = File(filePath);
      if (await file.exists()) {
        return await file.readAsString();
      }
    } catch (e) {
      print('Error reading task condition: $e');
    }
    return null;
  }

  /// Получить условие случайной задачи по номеру
  /// Возвращает содержимое условия
  Future<String?> getRandomTaskCondition(int taskNumber) async {
    final data = await getRandomTaskConditionWithVariant(taskNumber);
    return (data == null) ? null : (data['condition'] as String?);
  }

  /// Получить условие задачи по номеру и номеру варианта.
  /// Приоритет:
  ///  1) assets (desh/ege2026kp/conditions/...)
  ///  2) файловая система (для десктопа/CLI)
  ///  3) fallback на старую логику случайной задачи
  Future<String?> getTaskConditionForVariant(
    int taskNumber,
    int variantNumber,
  ) async {
    // 1) Пробуем загрузить из assets (этот вариант работает и на Android/iOS)
    final assetCondition = await _loadConditionFromAssets(
      taskNumber,
      variantNumber,
    );
    if (assetCondition != null && assetCondition.isNotEmpty) {
      return assetCondition;
    }

    // 2) Пробуем из файловой системы (актуально для десктопа / запуска из CLI)
    final filePath = await getTaskFilePathForVariant(taskNumber, variantNumber);
    if (filePath != null) {
      final condition = await getTaskCondition(filePath);
      if (condition != null && condition.isNotEmpty) {
        return condition;
      }
      print('⚠️ Файл найден, но содержимое пустое: $filePath');
    }

    // 3) Fallback: если файла нет (например, ещё не извлечены условия) — пробуем как раньше
    print(
      '⚠️ Используем fallback для задачи $taskNumber, варианта $variantNumber',
    );
    return await getRandomTaskCondition(taskNumber);
  }

  /// Получить путь к файлу случайной задачи по номеру
  /// Используется для поиска связанных изображений
  Future<String?> getRandomTaskFilePath(int taskNumber) async {
    // Для JSON нет файла, возвращаем null
    try {
      final condition = await _jsonService.getRandomCondition(taskNumber);
      if (condition != null && condition.isNotEmpty) {
        return null; // JSON не имеет файла
      }
    } catch (e) {
      // Игнорируем ошибку
    }

    // Fallback на файлы
    final files = await getTaskFilesForNumber(taskNumber);
    if (files.isEmpty) return null;

    return files[_rng.nextInt(files.length)];
  }
}
