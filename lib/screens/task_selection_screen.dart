import 'package:flutter/material.dart';
import '../models/task.dart';
import '../models/task_topic.dart';
import '../services/tasks_pool_service.dart';
import 'task_solving_screen.dart';

class TaskSelectionScreen extends StatefulWidget {
  const TaskSelectionScreen({super.key});

  @override
  State<TaskSelectionScreen> createState() => _TaskSelectionScreenState();
}

class _TaskSelectionScreenState extends State<TaskSelectionScreen> with SingleTickerProviderStateMixin {
  final TasksPoolService _tasksPoolService = TasksPoolService();
  
  List<int> _availableTasks = [];
  // Ключ: номер задачи, значение: сколько задач этого номера добавить
  Map<int, int> _selectedTaskCounts = {};
  Set<String> _selectedTopics = {};
  bool _isLoading = true;
  final TextEditingController _variantController = TextEditingController(text: '1');
  late TabController _tabController;
  /// Фильтр по сложности КЕГЭ: null = любая, 0–3 = уровень
  int? _selectedDifficulty;
  bool _kompegeAvailable = false;

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
      final kompege = await _tasksPoolService.hasKompegeTasks();
      final tasks = kompege
          ? await _tasksPoolService.getAvailableTaskNumbers()
          : <int>[];
      setState(() {
        _kompegeAvailable = kompege;
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

    // Создаем список задач для варианта (только из КЕГЭ)
    final List<Task> tasks = [];
    final taskNumbersList = _selectedTaskCounts.keys.toList()..sort();

    for (final taskNum in taskNumbersList) {
      final repeats = _selectedTaskCounts[taskNum] ?? 1;
      for (int i = 0; i < repeats; i++) {
        final picked = await _tasksPoolService.getRandomTaskConditionWithVariant(
          taskNum,
          difficulty: _selectedDifficulty,
        );
        if (picked == null) continue;
        final taskCondition = (picked['condition'] as String?) ?? '';
        final answer = picked['answer'] as String?;

        tasks.add(Task(
          taskNumber: taskNum,
          variantNumber: variantNum,
          answer: answer,
          solutionCode: taskCondition,
        ));
      }
    }

    if (tasks.isEmpty) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(content: Text('Не удалось загрузить задачи. Проверьте assets/kompege_tasks.json')),
        );
      }
      return;
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
        title: const Text('Выбор задач'),
        centerTitle: true,
        backgroundColor: Theme.of(context).colorScheme.surface,
        foregroundColor: Theme.of(context).colorScheme.onSurface,
        elevation: 0,
        scrolledUnderElevation: 1,
        bottom: TabBar(
          controller: _tabController,
          tabs: const [
            Tab(text: 'По темам', icon: Icon(Icons.category_outlined)),
            Tab(text: 'По номерам', icon: Icon(Icons.numbers)),
          ],
        ),
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : Column(
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                  child: Column(
                    children: [
                      // Номер варианта и кнопка «Начать»
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Text(
                            'Вариант',
                            style: Theme.of(context).textTheme.titleSmall?.copyWith(
                                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                                ),
                          ),
                          const SizedBox(width: 10),
                          SizedBox(
                            width: 72,
                            child: TextField(
                              controller: _variantController,
                              keyboardType: TextInputType.number,
                              textAlign: TextAlign.center,
                              decoration: InputDecoration(
                                border: OutlineInputBorder(
                                  borderRadius: BorderRadius.circular(12),
                                ),
                                contentPadding: const EdgeInsets.symmetric(
                                    horizontal: 12, vertical: 10),
                                isDense: true,
                                filled: true,
                                fillColor: Theme.of(context)
                                    .colorScheme
                                    .surfaceContainerHighest
                                    .withValues(alpha: 0.5),
                              ),
                            ),
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: FilledButton.icon(
                              onPressed: _startVariant,
                              icon: const Icon(Icons.play_arrow_rounded, size: 22),
                              label: const Text('Начать вариант'),
                              style: FilledButton.styleFrom(
                                padding: const EdgeInsets.symmetric(vertical: 14),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(12),
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                      if (_kompegeAvailable) ...[
                        const SizedBox(height: 14),
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 14, vertical: 10),
                          decoration: BoxDecoration(
                            color: Theme.of(context)
                                .colorScheme
                                .primaryContainer
                                .withValues(alpha: 0.4),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: Row(
                            children: [
                              Icon(
                                Icons.bar_chart_rounded,
                                size: 20,
                                color: Theme.of(context).colorScheme.primary,
                              ),
                              const SizedBox(width: 10),
                              Text(
                                'Сложность (КЕГЭ):',
                                style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                                      fontWeight: FontWeight.w500,
                                    ),
                              ),
                              const SizedBox(width: 10),
                              DropdownButton<int?>(
                                value: _selectedDifficulty,
                                isDense: true,
                                isExpanded: false,
                                hint: const Text('Любая'),
                                borderRadius: BorderRadius.circular(12),
                                underline: const SizedBox(),
                                items: const [
                                  DropdownMenuItem<int?>(value: null, child: Text('Любая')),
                                  DropdownMenuItem<int?>(value: 0, child: Text('Базовый')),
                                  DropdownMenuItem<int?>(value: 1, child: Text('Повышенный')),
                                  DropdownMenuItem<int?>(value: 2, child: Text('Высокий')),
                                  DropdownMenuItem<int?>(value: 3, child: Text('Очень высокий')),
                                ],
                                onChanged: (v) {
                                  setState(() => _selectedDifficulty = v);
                                },
                              ),
                            ],
                          ),
                        ),
                      ],
                      const SizedBox(height: 14),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 12, vertical: 6),
                            decoration: BoxDecoration(
                              color: Theme.of(context)
                                  .colorScheme
                                  .surfaceContainerHighest
                                  .withValues(alpha: 0.6),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: Text(
                              'Задач: ${_selectedTaskCounts.values.fold<int>(0, (p, e) => p + e)}',
                              style: Theme.of(context).textTheme.titleSmall?.copyWith(
                                    fontWeight: FontWeight.w600,
                                  ),
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
                              child: Text(
                                _selectedTaskCounts.length == _availableTasks.length
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
      padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          ...TaskTopics.topics.map((topic) {
            final isSelected = _selectedTopics.contains(topic.id);
            return Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: Material(
                color: Colors.transparent,
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
                  borderRadius: BorderRadius.circular(16),
                  child: Container(
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(
                      border: Border.all(
                        color: isSelected
                            ? Theme.of(context).colorScheme.primary.withValues(alpha: 0.6)
                            : Theme.of(context).colorScheme.outlineVariant.withValues(alpha: 0.6),
                        width: isSelected ? 2 : 1,
                      ),
                      borderRadius: BorderRadius.circular(16),
                      color: isSelected
                          ? Theme.of(context).colorScheme.primaryContainer.withValues(alpha: 0.35)
                          : Theme.of(context).colorScheme.surface,
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Checkbox(
                          value: isSelected,
                          onChanged: (value) {
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
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(6),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                topic.name,
                                style: Theme.of(context).textTheme.titleMedium?.copyWith(
                                      fontWeight: FontWeight.w600,
                                    ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                topic.description,
                                style: Theme.of(context).textTheme.bodySmall?.copyWith(
                                      color: Theme.of(context).colorScheme.onSurfaceVariant,
                                    ),
                              ),
                              const SizedBox(height: 10),
                              Wrap(
                                spacing: 6,
                                runSpacing: 6,
                                children: topic.taskNumbers.map((num) {
                                  final inSelection = _selectedTaskCounts.containsKey(num);
                                  return Container(
                                    padding: const EdgeInsets.symmetric(
                                        horizontal: 8, vertical: 4),
                                    decoration: BoxDecoration(
                                      color: inSelection
                                          ? Theme.of(context).colorScheme.primaryContainer
                                          : Theme.of(context)
                                              .colorScheme
                                              .surfaceContainerHighest
                                              .withValues(alpha: 0.7),
                                      borderRadius: BorderRadius.circular(8),
                                    ),
                                    child: Text(
                                      '$num',
                                      style: Theme.of(context).textTheme.labelMedium?.copyWith(
                                            fontWeight: FontWeight.w500,
                                          ),
                                    ),
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
                  'Загрузите задачи КЕГЭ: выполните\nscripts/kompege/extract_all_tasks.js\nи обновите assets/kompege_tasks.json',
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
            padding: const EdgeInsets.fromLTRB(20, 8, 20, 24),
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 4,
              crossAxisSpacing: 12,
              mainAxisSpacing: 12,
              childAspectRatio: 1.4,
            ),
            itemCount: _availableTasks.length,
            itemBuilder: (context, index) {
              final taskNum = _availableTasks[index];
              final count = _selectedTaskCounts[taskNum] ?? 0;
              final isSelected = count > 0;
              return Material(
                color: Colors.transparent,
                child: InkWell(
                  onTap: () => _toggleTaskNumber(taskNum),
                  borderRadius: BorderRadius.circular(14),
                  child: Container(
                    decoration: BoxDecoration(
                      color: isSelected
                          ? Theme.of(context).colorScheme.primaryContainer.withValues(alpha: 0.6)
                          : Theme.of(context).colorScheme.surfaceContainerHighest.withValues(alpha: 0.4),
                      border: Border.all(
                        color: isSelected
                            ? Theme.of(context).colorScheme.primary.withValues(alpha: 0.7)
                            : Theme.of(context).colorScheme.outlineVariant.withValues(alpha: 0.5),
                        width: isSelected ? 2 : 1,
                      ),
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(10),
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Text(
                            'Задача',
                            style: Theme.of(context).textTheme.labelSmall?.copyWith(
                                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                                ),
                            overflow: TextOverflow.ellipsis,
                            maxLines: 1,
                          ),
                          const SizedBox(height: 4),
                          Text(
                            '$taskNum',
                            style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                                  fontWeight: FontWeight.bold,
                                  color: isSelected
                                      ? Theme.of(context).colorScheme.primary
                                      : Theme.of(context).colorScheme.onSurface,
                                ),
                            overflow: TextOverflow.ellipsis,
                            maxLines: 1,
                          ),
                          if (isSelected) ...[
                            const SizedBox(height: 8),
                            Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                IconButton(
                                  icon: const Icon(Icons.remove_rounded, size: 20),
                                  padding: EdgeInsets.zero,
                                  visualDensity: VisualDensity.compact,
                                  onPressed: () => _changeTaskCount(taskNum, -1),
                                  tooltip: 'Уменьшить',
                                  style: IconButton.styleFrom(
                                    foregroundColor: Theme.of(context).colorScheme.primary,
                                  ),
                                ),
                                Text(
                                  '$count',
                                  style: Theme.of(context).textTheme.titleSmall?.copyWith(
                                        fontWeight: FontWeight.w700,
                                      ),
                                ),
                                IconButton(
                                  icon: const Icon(Icons.add_rounded, size: 20),
                                  padding: EdgeInsets.zero,
                                  visualDensity: VisualDensity.compact,
                                  onPressed: () => _changeTaskCount(taskNum, 1),
                                  tooltip: 'Добавить',
                                  style: IconButton.styleFrom(
                                    foregroundColor: Theme.of(context).colorScheme.primary,
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ],
                      ),
                    ),
                  ),
                ),
              );
            },
          );
  }
}

