import 'package:flutter/material.dart';
import '../models/task.dart';
import '../models/task_topic.dart';
import '../services/answers_service.dart';
import '../services/tasks_service.dart';
import '../services/tasks_pool_service.dart';
import 'task_solving_screen.dart';

class TaskSelectionScreen extends StatefulWidget {
  const TaskSelectionScreen({super.key});

  @override
  State<TaskSelectionScreen> createState() => _TaskSelectionScreenState();
}

class _TaskSelectionScreenState extends State<TaskSelectionScreen> with SingleTickerProviderStateMixin {
  final AnswersService _answersService = AnswersService();
  final TasksService _tasksService = TasksService();
  final TasksPoolService _tasksPoolService = TasksPoolService();
  
  List<int> _availableTasks = [];
  Set<int> _selectedTaskNumbers = {}; // Номера задач для включения в вариант
  Set<String> _selectedTopics = {};
  bool _isLoading = true;
  final TextEditingController _variantController = TextEditingController(text: '1');
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    // Оставляем только две вкладки: "По темам" и "По номерам"
    _tabController = TabController(length: 2, vsync: this);
    _loadTasks();
  }

  @override
  void dispose() {
    _tabController.dispose();
    _variantController.dispose();
    super.dispose();
  }

  Future<void> _loadTasks() async {
    setState(() => _isLoading = true);
    try {
      final tasks = await _tasksService.getAvailableTaskNumbers();
      setState(() {
        _availableTasks = tasks;
        _isLoading = false;
      });
    } catch (e) {
      setState(() => _isLoading = false);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Ошибка загрузки задач: $e')),
        );
      }
    }
  }

  void _toggleTaskNumber(int taskNumber) {
    setState(() {
      if (_selectedTaskNumbers.contains(taskNumber)) {
        _selectedTaskNumbers.remove(taskNumber);
      } else {
        _selectedTaskNumbers.add(taskNumber);
      }
    });
  }

  void _selectTasksByTopics() {
    if (_selectedTopics.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Выберите хотя бы одну тему')),
      );
      return;
    }

    setState(() {
      _selectedTaskNumbers.clear();
      for (final topicId in _selectedTopics) {
        final taskNumbers = TaskTopics.getTaskNumbersByTopic(topicId);
        _selectedTaskNumbers.addAll(taskNumbers);
      }
    });
  }

  Future<void> _startVariant() async {
    if (_selectedTaskNumbers.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Выберите хотя бы один номер задачи')),
      );
      return;
    }

    final variantNum = int.tryParse(_variantController.text);
    if (variantNum == null || variantNum < 1) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Введите корректный номер варианта')),
      );
      return;
    }

    // Загружаем ответы
    await _answersService.loadAnswers();

    // Создаем список задач для варианта
    final List<Task> tasks = [];
    final taskNumbersList = _selectedTaskNumbers.toList()..sort();
    
    // Для каждого номера берём СЛУЧАЙНУЮ задачу из доступных условий,
    // но порядок самих номеров задач не перемешиваем.
    for (final taskNum in taskNumbersList) {
      final picked = await _tasksPoolService.getRandomTaskConditionWithVariant(taskNum);
      final taskCondition = (picked?['condition'] as String?) ?? '';
      final conditionVariantNum = picked?['variant'] as int?;

      // В answers.csv ответы привязаны к номеру варианта УСЛОВИЯ (из имени файла task_N_VVV.txt).
      // Если вариант не удалось определить — считаем, что ответа нет.
      final answer = conditionVariantNum != null
          ? _answersService.getAnswer(conditionVariantNum, taskNum)
          : null;

      tasks.add(Task(
        taskNumber: taskNum,
        // task.variantNumber используем как номер варианта конкретного условия
        variantNumber: conditionVariantNum ?? variantNum,
        answer: answer,
        solutionCode: taskCondition, // Текст условия
      ));
    }

    // Задачи остаются в порядке по номерам (не перемешиваем)

    // Переходим на экран решения задач
    if (mounted) {
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => TaskSolvingScreen(
            variant: Variant(
              variantNumber: variantNum,
              tasks: tasks,
              startTime: DateTime.now(),
            ),
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Выбор задач для варианта'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        bottom: TabBar(
          controller: _tabController,
          tabs: const [
            Tab(text: 'По темам', icon: Icon(Icons.category)),
            Tab(text: 'По номерам', icon: Icon(Icons.numbers)),
          ],
        ),
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : Column(
              children: [
                Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      // Первая строка: номер варианта и кнопка
                      Row(
                        children: [
                          Flexible(
                            child: Row(
                              children: [
                                const Flexible(
                                  child: Text('Номер варианта: ', overflow: TextOverflow.ellipsis),
                                ),
                                const SizedBox(width: 8),
                                SizedBox(
                                  width: 80,
                                  child: TextField(
                                    controller: _variantController,
                                    keyboardType: TextInputType.number,
                                    decoration: const InputDecoration(
                                      border: OutlineInputBorder(),
                                      contentPadding: EdgeInsets.symmetric(horizontal: 8, vertical: 8),
                                      isDense: true,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 8),
                          Flexible(
                            child: FittedBox(
                              fit: BoxFit.scaleDown,
                              child: ElevatedButton.icon(
                                onPressed: _startVariant,
                                icon: const Icon(Icons.play_arrow, size: 18),
                                label: const Text('Начать вариант', style: TextStyle(fontSize: 14)),
                                style: ElevatedButton.styleFrom(
                                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                                  minimumSize: Size.zero,
                                  tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                      // Вторая строка: статистика и кнопки
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Выбрано номеров: ${_selectedTaskNumbers.length}',
                            style: Theme.of(context).textTheme.titleMedium,
                          ),
                          if (_tabController.index == 1)
                            TextButton(
                              onPressed: () {
                                setState(() {
                                  if (_selectedTaskNumbers.length == _availableTasks.length) {
                                    _selectedTaskNumbers.clear();
                                  } else {
                                    _selectedTaskNumbers = _availableTasks.toSet();
                                  }
                                });
                              },
                              child: Text(
                                _selectedTaskNumbers.length == _availableTasks.length
                                    ? 'Снять все'
                                    : 'Выбрать все',
                              ),
                            ),
                        ],
                      ),
                    ],
                  ),
                ),
                // Контент вкладок: "По темам" и "По номерам"
                Expanded(
                  child: TabBarView(
                    controller: _tabController,
                    children: [
                      // Вкладка "По темам"
                      _buildTopicsTab(context),
                      // Вкладка "По номерам"
                      _buildTasksTab(context),
                    ],
                  ),
                ),
              ],
            ),
    );
  }

  Widget _buildTopicsTab(BuildContext context) {
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Список тем
          ...TaskTopics.topics.map((topic) {
            final isSelected = _selectedTopics.contains(topic.id);
            return Card(
              margin: const EdgeInsets.only(bottom: 12),
              child: InkWell(
                onTap: () {
                  setState(() {
                    if (isSelected) {
                      _selectedTopics.remove(topic.id);
                    } else {
                      _selectedTopics.add(topic.id);
                    }
                  });
                  _selectTasksByTopics();
                },
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Row(
                    children: [
                        Checkbox(
                          value: isSelected,
                          onChanged: (value) {
                            // onChanged уже обрабатывается через onTap InkWell,
                            // но оставляем для прямого клика на Checkbox
                            if (value != isSelected) {
                              setState(() {
                                if (value == true) {
                                  _selectedTopics.add(topic.id);
                                } else {
                                  _selectedTopics.remove(topic.id);
                                }
                              });
                              _selectTasksByTopics();
                            }
                          },
                        ),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              topic.name,
                              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                    fontWeight: FontWeight.bold,
                                  ),
                            ),
                            const SizedBox(height: 4),
                            Text(
                              topic.description,
                              style: Theme.of(context).textTheme.bodySmall,
                            ),
                            const SizedBox(height: 8),
                            Wrap(
                              spacing: 4,
                              children: topic.taskNumbers.map((num) {
                                return Chip(
                                  label: Text('$num'),
                                  backgroundColor: _selectedTaskNumbers.contains(num)
                                      ? Theme.of(context).colorScheme.primaryContainer
                                      : null,
                                );
                              }).toList(),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            );
          }),
        ],
      ),
    );
  }

  Widget _buildTasksTab(BuildContext context) {
    return _availableTasks.isEmpty
        ? Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.info_outline,
                  size: 64,
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
                const SizedBox(height: 16),
                Text(
                  'Задачи не найдены',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                const SizedBox(height: 8),
                Text(
                  'Убедитесь, что папка desh/ege2026kp существует\nи содержит папки с задачами (1solve, 2solve, и т.д.)',
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Theme.of(context).colorScheme.onSurfaceVariant,
                      ),
                ),
                const SizedBox(height: 16),
                ElevatedButton.icon(
                  onPressed: _loadTasks,
                  icon: const Icon(Icons.refresh),
                  label: const Text('Обновить'),
                ),
              ],
            ),
          )
        : GridView.builder(
            padding: const EdgeInsets.all(16),
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 4,
              crossAxisSpacing: 8,
              mainAxisSpacing: 8,
              childAspectRatio: 1.5,
            ),
            itemCount: _availableTasks.length,
            itemBuilder: (context, index) {
              final taskNum = _availableTasks[index];
              final isSelected = _selectedTaskNumbers.contains(taskNum);
              return InkWell(
                onTap: () => _toggleTaskNumber(taskNum),
                borderRadius: BorderRadius.circular(8),
                child: Container(
                  decoration: BoxDecoration(
                    color: isSelected
                        ? Theme.of(context).colorScheme.primaryContainer
                        : Theme.of(context).colorScheme.surface,
                    border: Border.all(
                      color: isSelected
                          ? Theme.of(context).colorScheme.primary
                          : Theme.of(context).colorScheme.outline,
                      width: isSelected ? 2 : 1,
                    ),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(8),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Flexible(
                          child: Text(
                            'Задача',
                            style: Theme.of(context).textTheme.labelSmall,
                            overflow: TextOverflow.ellipsis,
                            maxLines: 1,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Flexible(
                          child: Text(
                            '$taskNum',
                            style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: isSelected
                                      ? Theme.of(context).colorScheme.primary
                                      : null,
                                ),
                            overflow: TextOverflow.ellipsis,
                            maxLines: 1,
                          ),
                        ),
                        if (isSelected) ...[
                          const SizedBox(height: 2),
                          Icon(
                            Icons.check_circle,
                            color: Theme.of(context).colorScheme.primary,
                            size: 18,
                          ),
                        ],
                      ],
                    ),
                  ),
                ),
              );
            },
          );
  }
}

