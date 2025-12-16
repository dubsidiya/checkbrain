import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'dart:io';
import 'package:path/path.dart' as path;
import '../models/task.dart';
import '../services/tasks_service.dart';
import '../services/task_conditions_service.dart';
import '../services/tasks_conditions_json_service.dart';
import '../services/tasks_pool_service.dart';
import 'results_screen.dart';

class TaskSolvingScreen extends StatefulWidget {
  final Variant variant;

  const TaskSolvingScreen({super.key, required this.variant});

  @override
  State<TaskSolvingScreen> createState() => _TaskSolvingScreenState();
}

class _TaskSolvingScreenState extends State<TaskSolvingScreen> {
  final TasksService _tasksService = TasksService();
  final TasksConditionsJsonService _conditionsService = TasksConditionsJsonService();
  final TasksPoolService _tasksPoolService = TasksPoolService();
  final Map<int, TextEditingController> _answerControllers = {};
  final Map<int, TextEditingController> _conditionControllers = {};
  final Map<int, String> _userCodes = {};
  final Map<int, String?> _taskContents = {};
  final Map<int, String?> _dataContents = {};
  final Map<int, List<String>> _taskImages = {}; // Пути к изображениям для каждой задачи
  
  int _currentTaskIndex = 0;
  bool _isLoadingContent = false;
  bool _isEditingCondition = false;

  @override
  void initState() {
    super.initState();
    _initializeControllers();
    _loadTaskContent();
  }

  Future<void> _initializeControllers() async {
    for (final task in widget.variant.tasks) {
      _answerControllers[task.taskNumber] = TextEditingController();
      
      // Используем условие, которое уже сохранено в задаче при создании варианта
      // Это гарантирует стабильность - задача не будет меняться
      String condition = '';
      if (task.solutionCode != null && task.solutionCode!.isNotEmpty) {
        condition = task.solutionCode!;
        // Сохраняем в _taskContents сразу
        _taskContents[task.taskNumber] = condition;
      } else {
        // Fallback: если условие не было сохранено, загружаем из JSON
        try {
          final jsonCondition = await _conditionsService.getRandomCondition(task.taskNumber);
          if (jsonCondition != null && jsonCondition.isNotEmpty) {
            condition = jsonCondition;
            _taskContents[task.taskNumber] = condition;
          }
        } catch (e) {
          print('Error loading condition from JSON: $e');
        }
        
        // Если все еще нет, используем fallback
        if (condition.isEmpty) {
          condition = TaskConditionsService.getTaskConditionWithFallback(task.taskNumber);
        }
      }
      
      _conditionControllers[task.taskNumber] = TextEditingController(text: condition);
    }
  }

  Future<void> _loadTaskContent() async {
    setState(() => _isLoadingContent = true);
    
    final currentTask = widget.variant.tasks[_currentTaskIndex];
    
    // Используем условие, которое уже сохранено в задаче при создании варианта
    // Это гарантирует, что задача не будет меняться при перелистывании
    if (currentTask.solutionCode != null && currentTask.solutionCode!.isNotEmpty) {
      setState(() {
        _taskContents[currentTask.taskNumber] = currentTask.solutionCode;
      });
      // Обновляем контроллер условия
      if (_conditionControllers[currentTask.taskNumber] != null) {
        _conditionControllers[currentTask.taskNumber]!.text = currentTask.solutionCode!;
      }
    } else {
      // Fallback: если условие не было сохранено, загружаем из JSON (но только один раз)
      if (_taskContents[currentTask.taskNumber] == null) {
        try {
          final jsonCondition = await _conditionsService.getRandomCondition(currentTask.taskNumber);
          if (jsonCondition != null && jsonCondition.isNotEmpty) {
            setState(() {
              _taskContents[currentTask.taskNumber] = jsonCondition;
            });
            if (_conditionControllers[currentTask.taskNumber] != null) {
              _conditionControllers[currentTask.taskNumber]!.text = jsonCondition;
            }
          }
        } catch (e) {
          print('Error loading condition from JSON: $e');
        }
      }
      
      // Если все еще нет условия, пробуем загрузить из файлов
      if (_taskContents[currentTask.taskNumber] == null) {
        try {
          final taskFiles = await _tasksService.getTaskFiles(currentTask.taskNumber);
          if (taskFiles.isNotEmpty) {
            final content = await _tasksService.readFileContent(taskFiles.first);
            if (content != null && content.isNotEmpty) {
              setState(() {
                _taskContents[currentTask.taskNumber] = content;
              });
            }
          }
        } catch (e) {
          print('Error loading task content: $e');
        }
      }
    }

    try {
    // Загружаем файлы данных если есть
      final dataFiles = await _tasksService.getDataFiles(currentTask.taskNumber);
      if (dataFiles.isNotEmpty) {
        final content = await _tasksService.readFileContent(dataFiles.first);
        setState(() {
          _dataContents[currentTask.taskNumber] = content;
        });
      }
    } catch (e) {
      print('Error loading data content: $e');
      // Продолжаем работу даже если файл не загрузился
    }

    // Загружаем изображения для задачи (графы и т.д.)
    try {
      if (_taskImages[currentTask.taskNumber] == null) {
        // Пытаемся найти файл условия именно для этого номера и варианта
        final taskFilePath = await _tasksPoolService.getTaskFilePathForVariant(
          currentTask.taskNumber,
          currentTask.variantNumber,
        );
        if (taskFilePath != null) {
          final images = await _tasksPoolService.getImagesForCondition(
            currentTask.taskNumber,
            taskFilePath,
          );
          setState(() {
            _taskImages[currentTask.taskNumber] = images;
          });
        }
      }
    } catch (e) {
      print('Error loading task images: $e');
      // Продолжаем работу даже если изображения не загрузились
    }

    setState(() => _isLoadingContent = false);
  }

  Future<void> _pickCodeFile(int taskNumber) async {
    try {
      FilePickerResult? result = await FilePicker.platform.pickFiles(
        type: FileType.custom,
        allowedExtensions: ['py', 'pas', 'cpp', 'txt', 'kum'],
      );

      if (result != null && result.files.isNotEmpty) {
        final pickedFile = result.files.first;
        String? content;
        
        // В версии 8.x может быть bytes или path
        if (pickedFile.bytes != null) {
          // Читаем из bytes
          content = String.fromCharCodes(pickedFile.bytes!);
        } else if (pickedFile.path != null) {
          // Читаем из файла
          final file = File(pickedFile.path!);
          content = await file.readAsString();
        }
        
        if (content != null && content.isNotEmpty) {
          setState(() {
            _userCodes[taskNumber] = content!;
          });
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Код успешно загружен')),
          );
        }
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Ошибка загрузки файла: $e')),
      );
    }
  }

  void _nextTask() {
    if (_currentTaskIndex < widget.variant.tasks.length - 1) {
      setState(() {
        _currentTaskIndex++;
      });
      _loadTaskContent();
    }
  }

  void _previousTask() {
    if (_currentTaskIndex > 0) {
      setState(() {
        _currentTaskIndex--;
      });
      _loadTaskContent();
    }
  }

  void _finishVariant() {
    // Сохраняем ответы пользователя
    final List<Task> completedTasks = [];
    
    for (final task in widget.variant.tasks) {
      final userAnswer = _answerControllers[task.taskNumber]?.text.trim() ?? '';
      final userCode = _userCodes[task.taskNumber] ?? '';
      
      // Проверяем ответ
      bool? isCorrect;
      if (userAnswer.isNotEmpty && task.answer != null) {
        // Нормализуем ответы для сравнения
        // Учитываем, что пользователь может ввести латиницей вместо кириллицы
        String normalizeText(String text) {
          // Заменяем латинские буквы на кириллические для сравнения
          return text
              .replaceAll('A', 'А')
              .replaceAll('B', 'В')
              .replaceAll('C', 'С')
              .replaceAll('E', 'Е')
              .replaceAll('H', 'Н')
              .replaceAll('K', 'К')
              .replaceAll('M', 'М')
              .replaceAll('O', 'О')
              .replaceAll('P', 'Р')
              .replaceAll('T', 'Т')
              .replaceAll('X', 'Х')
              .replaceAll('Y', 'У')
              .toLowerCase()
              .trim();
        }
        
        final normalizedUserAnswer = normalizeText(userAnswer);
        final normalizedCorrectAnswer = normalizeText(task.answer!);
        isCorrect = normalizedUserAnswer == normalizedCorrectAnswer;
        
        // Отладочный вывод
        print('Задача ${task.taskNumber}:');
        print('  Правильный ответ: "${task.answer}" -> "$normalizedCorrectAnswer"');
        print('  Ответ пользователя: "$userAnswer" -> "$normalizedUserAnswer"');
        print('  Совпадают: $isCorrect');
      } else if (task.answer == null) {
        print('⚠️ Задача ${task.taskNumber}: правильный ответ отсутствует');
      }

      completedTasks.add(task.copyWith(
        userAnswer: userAnswer,
        userCode: userCode,
        isCorrect: isCorrect,
      ));
    }

    final completedVariant = Variant(
      variantNumber: widget.variant.variantNumber,
      tasks: completedTasks,
      startTime: widget.variant.startTime,
      endTime: DateTime.now(),
    );

    // Используем push вместо pushReplacement, чтобы можно было вернуться к варианту
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ResultsScreen(variant: completedVariant),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (widget.variant.tasks.isEmpty) {
      return Scaffold(
        appBar: AppBar(title: const Text('Решение задач')),
        body: const Center(child: Text('Нет задач для решения')),
      );
    }

    final currentTask = widget.variant.tasks[_currentTaskIndex];
    final taskContent = _taskContents[currentTask.taskNumber];
    final dataContent = _dataContents[currentTask.taskNumber];
    final userCode = _userCodes[currentTask.taskNumber];

    return Scaffold(
      appBar: AppBar(
        title: Text('Задача ${currentTask.taskNumber} (${_currentTaskIndex + 1}/${widget.variant.tasks.length})'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: _isLoadingContent
          ? const Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                mainAxisSize: MainAxisSize.min,
                children: [
                  // Прогресс бар
                  LinearProgressIndicator(
                    value: (_currentTaskIndex + 1) / widget.variant.tasks.length,
                  ),
                  const SizedBox(height: 16),
                  
                  // Содержимое задачи
                  Card(
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Условие задачи:',
                            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                  fontWeight: FontWeight.bold,
                                ),
                          ),
                          const SizedBox(height: 8),
                          // Кнопка редактирования условия
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              if (taskContent != null)
                                Chip(
                                  label: const Text('Загружено из файла'),
                                  avatar: const Icon(Icons.check_circle, size: 18),
                                ),
                              IconButton(
                                icon: Icon(_isEditingCondition ? Icons.save : Icons.edit),
                                onPressed: () {
                                  setState(() {
                                    _isEditingCondition = !_isEditingCondition;
                                  });
                                },
                                tooltip: _isEditingCondition ? 'Сохранить' : 'Редактировать условие',
                              ),
                            ],
                          ),
                          const SizedBox(height: 8),
                          if (taskContent != null && !_isEditingCondition) ...[
                            // Показываем загруженное условие из файла
                            SelectableText(
                              taskContent,
                              style: const TextStyle(fontFamily: 'monospace'),
                            ),
                            // Показываем изображения графов, если есть
                            if (_taskImages[currentTask.taskNumber] != null &&
                                _taskImages[currentTask.taskNumber]!.isNotEmpty) ...[
                              const SizedBox(height: 16),
                              Text(
                                'Графы и схемы:',
                                style: Theme.of(context).textTheme.titleSmall?.copyWith(
                                      fontWeight: FontWeight.bold,
                                    ),
                              ),
                              const SizedBox(height: 8),
                              ..._taskImages[currentTask.taskNumber]!.map((imagePath) {
                                return Padding(
                                  padding: const EdgeInsets.only(bottom: 8),
                                  child: Image.file(
                                    File(imagePath),
                                    fit: BoxFit.contain,
                                    errorBuilder: (context, error, stackTrace) {
                                      return Container(
                                        padding: const EdgeInsets.all(8),
                                        color: Theme.of(context).colorScheme.errorContainer,
                                        child: Text(
                                          'Не удалось загрузить изображение: ${path.basename(imagePath)}',
                                          style: TextStyle(
                                            color: Theme.of(context).colorScheme.onErrorContainer,
                                          ),
                                        ),
                                      );
                                    },
                                  ),
                                );
                              }),
                            ],
                          ] else ...[
                            // Показываем условие из сервиса или редактируемое поле
                            ConstrainedBox(
                              constraints: BoxConstraints(
                                maxHeight: MediaQuery.of(context).size.height * 0.4,
                              ),
                              child: TextField(
                                controller: _conditionControllers[currentTask.taskNumber],
                                maxLines: null,
                                minLines: 10,
                                enabled: _isEditingCondition,
                                decoration: InputDecoration(
                                  border: const OutlineInputBorder(),
                                  hintText: 'Введите условие задачи',
                                  filled: !_isEditingCondition,
                                  fillColor: _isEditingCondition 
                                      ? null 
                                      : Theme.of(context).colorScheme.surfaceVariant,
                                ),
                                style: const TextStyle(fontFamily: 'monospace'),
                              ),
                            ),
                            if (!_isEditingCondition) ...[
                              const SizedBox(height: 8),
                              Row(
                                children: [
                                  Icon(
                                    Icons.lightbulb_outline,
                                    size: 16,
                                    color: Theme.of(context).colorScheme.primary,
                                  ),
                                  const SizedBox(width: 4),
                                  Expanded(
                                    child: Text(
                                      'Вы можете отредактировать условие, нажав на кнопку редактирования выше.',
                                      style: Theme.of(context).textTheme.bodySmall?.copyWith(
                                            color: Theme.of(context).colorScheme.primary,
                                          ),
                                    ),
                                  ),
                                ],
                              ),
                            ],
                          ],
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Данные для задачи
                  if (dataContent != null) ...[
                    Card(
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              'Данные для задачи:',
                              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                    fontWeight: FontWeight.bold,
                                  ),
                            ),
                            const SizedBox(height: 8),
                            SelectableText(
                              dataContent,
                              style: const TextStyle(fontFamily: 'monospace'),
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Поле для ввода ответа
                  // ВАЖНО: правильный ответ показываем только в результатах, а не во время решения
                  Card(
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            'Ваш ответ:',
                            style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                  fontWeight: FontWeight.bold,
                                ),
                          ),
                          const SizedBox(height: 8),
                          TextField(
                            controller: _answerControllers[currentTask.taskNumber],
                            decoration: const InputDecoration(
                              border: OutlineInputBorder(),
                              hintText: 'Введите ответ',
                            ),
                            maxLines: 3,
                          ),
                        ],
                      ),
                    ),
                  ),
                  const SizedBox(height: 16),

                  // Прикрепление кода
                  Card(
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                'Код решения:',
                                style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                      fontWeight: FontWeight.bold,
                                    ),
                              ),
                              ElevatedButton.icon(
                                onPressed: () => _pickCodeFile(currentTask.taskNumber),
                                icon: const Icon(Icons.attach_file),
                                label: const Text('Прикрепить файл'),
                              ),
                            ],
                          ),
                          const SizedBox(height: 8),
                          if (userCode != null && userCode.isNotEmpty) ...[
                            ConstrainedBox(
                              constraints: BoxConstraints(
                                maxHeight: MediaQuery.of(context).size.height * 0.3,
                              ),
                              child: SingleChildScrollView(
                                child: Container(
                                  padding: const EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: Theme.of(context).colorScheme.surfaceVariant,
                                    borderRadius: BorderRadius.circular(8),
                                  ),
                                  child: SelectableText(
                                    userCode,
                                    style: const TextStyle(fontFamily: 'monospace', fontSize: 12),
                                  ),
                                ),
                              ),
                            ),
                            const SizedBox(height: 8),
                            TextButton.icon(
                              onPressed: () {
                                setState(() {
                                  _userCodes.remove(currentTask.taskNumber);
                                });
                              },
                              icon: const Icon(Icons.delete),
                              label: const Text('Удалить код'),
                            ),
                          ] else
                            Text(
                              'Код не прикреплен',
                              style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                                    color: Theme.of(context).colorScheme.onSurfaceVariant,
                                  ),
                            ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
      bottomNavigationBar: SafeArea(
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 8),
          child: Row(
            children: [
              SizedBox(
                width: 48,
                child: IconButton(
                  onPressed: _currentTaskIndex > 0 ? _previousTask : null,
                  icon: const Icon(Icons.arrow_back),
                  tooltip: 'Предыдущая задача',
                  padding: EdgeInsets.zero,
                  constraints: const BoxConstraints(),
                ),
              ),
              Expanded(
                child: Text(
                  '${_currentTaskIndex + 1} / ${widget.variant.tasks.length}',
                  style: Theme.of(context).textTheme.titleMedium,
                  textAlign: TextAlign.center,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
              if (_currentTaskIndex < widget.variant.tasks.length - 1)
                SizedBox(
                  width: 48,
                  child: IconButton(
                    onPressed: _nextTask,
                    icon: const Icon(Icons.arrow_forward),
                    tooltip: 'Следующая задача',
                    padding: EdgeInsets.zero,
                    constraints: const BoxConstraints(),
                  ),
                )
              else
                Flexible(
                  child: Padding(
                    padding: const EdgeInsets.only(right: 4),
                    child: ElevatedButton(
                      onPressed: _finishVariant,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Theme.of(context).colorScheme.primary,
                        foregroundColor: Theme.of(context).colorScheme.onPrimary,
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                        minimumSize: Size.zero,
                        tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                      ),
                      child: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.check, size: 18),
                          SizedBox(width: 4),
                          Text('Завершить', style: TextStyle(fontSize: 14)),
                        ],
                      ),
                    ),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }


  @override
  void dispose() {
    for (final controller in _answerControllers.values) {
      controller.dispose();
    }
    for (final controller in _conditionControllers.values) {
      controller.dispose();
    }
    super.dispose();
  }
}

