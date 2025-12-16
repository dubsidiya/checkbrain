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
  // Ключ: номер задачи, значение: сколько задач этого номера добавить
  Map<int, int> _selectedTaskCounts = {};
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
      if (_selectedTaskCounts.containsKey(taskNumber)) {
        _selectedTaskCounts.remove(taskNumber);
      } else {
        _selectedTaskCounts[taskNumber] = 1;
      }
    });
  }

  void _changeTaskCount(int taskNumber, int delta) {
    final current = _selectedTaskCounts[taskNumber] ?? 0;
    final next = current + delta;
    setState(() {
      if (next <= 0) {
        _selectedTaskCounts.remove(taskNumber);
      } else {
        _selectedTaskCounts[taskNumber] = next;
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
      _selectedTaskCounts.clear();
      for (final topicId in _selectedTopics) {
        final taskNumbers = TaskTopics.getTaskNumbersByTopic(topicId);
        for (final num in taskNumbers) {
          _selectedTaskCounts[num] = 1;
        }
      }
    });
  }

  Future<void> _startVariant() async {
    if (_selectedTaskCounts.isEmpty) {
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
    final taskNumbersList = _selectedTaskCounts.keys.toList()..sort();

    // Для каждого номера берём СЛУЧАЙНУЮ задачу из доступных условий
    // (по количеству, указанному пользователем), но порядок самих номеров задач не перемешиваем.
    for (final taskNum in taskNumbersList) {
      final repeats = _selectedTaskCounts[taskNum] ?? 1;
      for (int i = 0; i < repeats; i++) {
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
    final theme = Theme.of(context);
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
                  child: Card(
                    elevation: 3,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        const SizedBox(height: 12),
                        // Первая строка: номер варианта и кнопка
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: Row(
                            children: [
                              Flexible(
                                child: Row(
                                  children: [
                                    const Flexible(
                                      child: Text('Номер варианта: ', overflow: TextOverflow.ellipsis),
                                    ),
                                    const SizedBox(width: 8),
                                    SizedBox(
                                      width: 70,
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
                                  alignment: Alignment.centerRight,
                                  child: FilledButton.icon(
                                    onPressed: _startVariant,
                                    icon: const Icon(Icons.play_arrow, size: 16),
                                    label: const Text('Начать'),
                                    style: FilledButton.styleFrom(
                                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                                    ),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 14),
                        // Вторая строка: статистика и кнопки
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
                          child: Row(
                            children: [
                              Flexible(
                                child: Wrap(
                                  spacing: 8,
                                  runSpacing: 8,
                                  children: [
                                    Chip(
                                      avatar: const Icon(Icons.list_alt, size: 16),
                                      label: Text(
                                        'Номеров: ${_selectedTaskCounts.length}',
                                        style: theme.textTheme.bodySmall,
                                      ),
                                      padding: const EdgeInsets.symmetric(horizontal: 8),
                                    ),
                                    Chip(
                                      avatar: const Icon(Icons.format_list_numbered, size: 16),
                                      label: Text(
                                        'Всего: ${_selectedTaskCounts.values.fold<int>(0, (p, e) => p + e)}',
                                        style: theme.textTheme.bodySmall,
                                      ),
                                      padding: const EdgeInsets.symmetric(horizontal: 8),
                                    ),
                                  ],
                                ),
                              ),
                              if (_tabController.index == 1)
                                TextButton(
                                  onPressed: () {
                                    setState(() {
                                      if (_selectedTaskCounts.length == _availableTasks.length) {
                                        _selectedTaskCounts.clear();
                                      } else {
                                        _selectedTaskCounts = {
                                          for (final n in _availableTasks) n: 1
                                        };
                                      }
                                    });
                                  },
                                  style: TextButton.styleFrom(
                                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                    minimumSize: Size.zero,
                                    tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                                  ),
                                  child: FittedBox(
                                    fit: BoxFit.scaleDown,
                                    child: Text(
                                      _selectedTaskCounts.length == _availableTasks.length
                                          ? 'Снять все'
                                          : 'Выбрать все',
                                      style: theme.textTheme.bodySmall,
                                    ),
                                  ),
                                ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 12),
                      ],
                    ),
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
                                final inSelection = _selectedTaskCounts.containsKey(num);
                                return Chip(
                                  label: Text('$num'),
                                  backgroundColor: inSelection
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
        : ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: _availableTasks.length,
            itemBuilder: (context, index) {
              final taskNum = _availableTasks[index];
              final count = _selectedTaskCounts[taskNum] ?? 0;
              final isSelected = count > 0;
              final theme = Theme.of(context);
              return Card(
                margin: const EdgeInsets.only(bottom: 12),
                elevation: isSelected ? 4 : 1,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                  side: BorderSide(
                    color: isSelected
                        ? theme.colorScheme.primary
                        : theme.colorScheme.outlineVariant,
                    width: isSelected ? 2 : 1,
                  ),
                ),
                color: isSelected
                    ? theme.colorScheme.primaryContainer
                    : theme.colorScheme.surface,
                child: InkWell(
                  onTap: () => _toggleTaskNumber(taskNum),
                  borderRadius: BorderRadius.circular(12),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 10),
                    child: Row(
                      children: [
                        // Номер задачи в круге
                        Container(
                          width: 40,
                          height: 40,
                          decoration: BoxDecoration(
                            color: isSelected
                                ? theme.colorScheme.primary
                                : theme.colorScheme.surfaceContainerHighest,
                            shape: BoxShape.circle,
                          ),
                          child: Center(
                            child: Text(
                              '$taskNum',
                              style: theme.textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.bold,
                                    color: isSelected
                                        ? theme.colorScheme.onPrimary
                                        : theme.colorScheme.onSurface,
                                  ),
                            ),
                          ),
                        ),
                        const SizedBox(width: 10),
                        // Название задачи
                        Expanded(
                          child: Text(
                            'Задача $taskNum',
                            style: theme.textTheme.bodyLarge?.copyWith(
                                  fontWeight: FontWeight.w600,
                                  color: isSelected
                                      ? theme.colorScheme.onPrimaryContainer
                                      : null,
                                ),
                            overflow: TextOverflow.ellipsis,
                            maxLines: 1,
                          ),
                        ),
                        // Счётчик и кнопки управления
                        if (isSelected)
                          Flexible(
                            child: FittedBox(
                              fit: BoxFit.scaleDown,
                              alignment: Alignment.centerRight,
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Material(
                                    color: Colors.transparent,
                                    child: InkWell(
                                      onTap: () => _changeTaskCount(taskNum, -1),
                                      borderRadius: BorderRadius.circular(16),
                                      child: Padding(
                                        padding: const EdgeInsets.all(4),
                                        child: Icon(
                                          Icons.remove_circle_outline,
                                          size: 20,
                                          color: theme.colorScheme.primary,
                                        ),
                                      ),
                                    ),
                                  ),
                                  Container(
                                    margin: const EdgeInsets.symmetric(horizontal: 4),
                                    padding: const EdgeInsets.symmetric(
                                      horizontal: 6,
                                      vertical: 2,
                                    ),
                                    decoration: BoxDecoration(
                                      color: theme.colorScheme.primary,
                                      borderRadius: BorderRadius.circular(10),
                                    ),
                                    child: Text(
                                      '$count',
                                      style: theme.textTheme.bodySmall?.copyWith(
                                            fontWeight: FontWeight.bold,
                                            color: theme.colorScheme.onPrimary,
                                            fontSize: 12,
                                          ),
                                    ),
                                  ),
                                  Material(
                                    color: Colors.transparent,
                                    child: InkWell(
                                      onTap: () => _changeTaskCount(taskNum, 1),
                                      borderRadius: BorderRadius.circular(16),
                                      child: Padding(
                                        padding: const EdgeInsets.all(4),
                                        child: Icon(
                                          Icons.add_circle_outline,
                                          size: 20,
                                          color: theme.colorScheme.primary,
                                        ),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          )
                        else
                          Icon(
                            Icons.radio_button_unchecked,
                            color: theme.colorScheme.outline,
                            size: 20,
                          ),
                      ],
                    ),
                  ),
                ),
              );
            },
          );
  }
}

