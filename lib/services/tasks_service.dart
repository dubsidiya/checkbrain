import 'dart:io';
import 'package:flutter/services.dart';
import 'package:path/path.dart' as path;

class TasksService {
  // Предопределенный список номеров задач ЕГЭ по информатике
  static const List<int> _knownTaskNumbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18,
    19, 20, 21, 22, 23, 24, 25, 26, 27
  ];

  // Используем абсолютный путь или путь относительно рабочей директории
  String _getBasePath() {
    // Пробуем найти папку desh относительно текущей рабочей директории
    final currentDir = Directory.current.path;
    final basePath = path.join(currentDir, 'desh', 'ege2026kp');
    return basePath;
  }

  Future<List<int>> getAvailableTaskNumbers() async {
    // На мобильных устройствах Directory.current не работает корректно
    // Возвращаем предопределенный список задач ЕГЭ
    return List<int>.from(_knownTaskNumbers);
  }

  Future<List<String>> getTaskFiles(int taskNumber) async {
    final List<String> files = [];
    final solveDir = path.join(_getBasePath(), '${taskNumber}solve');
    
    try {
      final dir = Directory(solveDir);
      if (await dir.exists()) {
        await for (final entity in dir.list()) {
          if (entity is File) {
            files.add(entity.path);
          }
        }
      }
    } catch (e) {
      print('Error getting task files: $e');
    }

    return files;
  }

  Future<List<String>> getDataFiles(int taskNumber) async {
    final List<String> files = [];
    final dataDir = path.join(_getBasePath(), '${taskNumber}data');
    
    try {
      final dir = Directory(dataDir);
      if (await dir.exists()) {
        await for (final entity in dir.list()) {
          if (entity is File) {
            files.add(entity.path);
          }
        }
      }
    } catch (e) {
      print('Error getting data files: $e');
    }

    return files;
  }

  Future<String?> readFileContent(String filePath) async {
    try {
      final file = File(filePath);
      if (await file.exists()) {
        return await file.readAsString();
      }
    } catch (e) {
      print('Error reading file $filePath: $e');
    }
    return null;
  }

  Future<String?> readAssetFile(String assetPath) async {
    try {
      return await rootBundle.loadString(assetPath);
    } catch (e) {
      print('Error reading asset $assetPath: $e');
      return null;
    }
  }
}

