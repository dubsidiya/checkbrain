import 'package:flutter/material.dart';
import '../services/kompege_tasks_service.dart';
import 'task_detail_screen.dart';

/// Сборник задач: список по номерам (1–27), затем список задач выбранного номера.
class TasksCatalogScreen extends StatefulWidget {
  const TasksCatalogScreen({super.key});

  @override
  State<TasksCatalogScreen> createState() => _TasksCatalogScreenState();
}

class _TasksCatalogScreenState extends State<TasksCatalogScreen> {
  final KompegeTasksService _service = KompegeTasksService();
  List<int> _taskNumbers = [];
  Map<int, int> _countByNumber = {};
  bool _loading = true;
  String? _error;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    setState(() {
      _loading = true;
      _error = null;
    });
    try {
      final numbers = await _service.getAvailableTaskNumbers();
      final counts = <int, int>{};
      for (final n in numbers) {
        counts[n] = await _service.getCountForNumber(n);
      }
      setState(() {
        _taskNumbers = numbers;
        _countByNumber = counts;
        _loading = false;
      });
    } catch (e) {
      setState(() {
        _loading = false;
        _error = e.toString();
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Сборник задач'),
        centerTitle: true,
        backgroundColor: Theme.of(context).colorScheme.surface,
        foregroundColor: Theme.of(context).colorScheme.onSurface,
        elevation: 0,
        scrolledUnderElevation: 1,
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : _error != null
              ? _buildError(context)
              : _taskNumbers.isEmpty
                  ? _buildEmpty(context)
                  : RefreshIndicator(
                      onRefresh: _load,
                      child: ListView.builder(
                        padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
                        itemCount: _taskNumbers.length,
                        itemBuilder: (context, index) {
                          final num = _taskNumbers[index];
                          final count = _countByNumber[num] ?? 0;
                          return _buildTaskNumberTile(context, num, count);
                        },
                      ),
                    ),
    );
  }

  Widget _buildError(BuildContext context) {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.error_outline,
              size: 48,
              color: Theme.of(context).colorScheme.error,
            ),
            const SizedBox(height: 16),
            Text(
              'Не удалось загрузить сборник',
              style: Theme.of(context).textTheme.titleMedium,
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 8),
            Text(
              _error!,
              style: Theme.of(context).textTheme.bodySmall,
              textAlign: TextAlign.center,
              maxLines: 3,
              overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: 16),
            FilledButton.icon(
              onPressed: _load,
              icon: const Icon(Icons.refresh),
              label: const Text('Повторить'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildEmpty(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.menu_book_outlined,
            size: 64,
            color: Theme.of(context).colorScheme.onSurfaceVariant,
          ),
          const SizedBox(height: 16),
          Text(
            'Нет задач в сборнике',
            style: Theme.of(context).textTheme.titleMedium,
          ),
          const SizedBox(height: 8),
          Text(
            'Запустите scripts/kompege/extract_all_tasks.js\nи обновите assets/kompege_tasks.json',
            textAlign: TextAlign.center,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
          ),
        ],
      ),
    );
  }

  Widget _buildTaskNumberTile(BuildContext context, int taskNumber, int count) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () => _openTaskNumber(context, taskNumber),
          borderRadius: BorderRadius.circular(16),
          child: Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              border: Border.all(
                color: Theme.of(context)
                    .colorScheme
                    .outlineVariant
                    .withValues(alpha: 0.6),
              ),
              borderRadius: BorderRadius.circular(16),
              color: Theme.of(context).colorScheme.surface,
            ),
            child: Row(
              children: [
                Container(
                  width: 48,
                  height: 48,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: Theme.of(context)
                        .colorScheme
                        .primaryContainer
                        .withValues(alpha: 0.6),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    '$taskNumber',
                    style: Theme.of(context).textTheme.titleLarge?.copyWith(
                          fontWeight: FontWeight.bold,
                          color: Theme.of(context).colorScheme.primary,
                        ),
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Задача $taskNumber',
                        style: Theme.of(context).textTheme.titleMedium?.copyWith(
                              fontWeight: FontWeight.w600,
                            ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        '$count ${_plural(count, 'задача', 'задачи', 'задач')}',
                        style: Theme.of(context).textTheme.bodySmall?.copyWith(
                              color: Theme.of(context).colorScheme.onSurfaceVariant,
                            ),
                      ),
                    ],
                  ),
                ),
                Icon(
                  Icons.chevron_right,
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  String _plural(int n, String one, String few, String many) {
    if (n % 10 == 1 && n % 100 != 11) return one;
    if (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) return few;
    return many;
  }

  void _openTaskNumber(BuildContext context, int taskNumber) {
    Navigator.push(
      context,
      MaterialPageRoute<void>(
        builder: (context) => _TaskNumberListScreen(
          taskNumber: taskNumber,
          service: _service,
        ),
      ),
    );
  }
}

/// Список всех задач по одному номеру (например, все «Задача 3»).
class _TaskNumberListScreen extends StatefulWidget {
  const _TaskNumberListScreen({
    required this.taskNumber,
    required this.service,
  });

  final int taskNumber;
  final KompegeTasksService service;

  @override
  State<_TaskNumberListScreen> createState() => _TaskNumberListScreenState();
}

class _TaskNumberListScreenState extends State<_TaskNumberListScreen> {
  List<KompegeTask> _tasks = [];
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    setState(() => _loading = true);
    final list = await widget.service.getTasksForNumber(widget.taskNumber);
    setState(() {
      _tasks = list;
      _loading = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Задача ${widget.taskNumber}'),
        centerTitle: true,
        backgroundColor: Theme.of(context).colorScheme.surface,
        foregroundColor: Theme.of(context).colorScheme.onSurface,
        elevation: 0,
        scrolledUnderElevation: 1,
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : _tasks.isEmpty
              ? Center(
                  child: Text(
                    'Нет задач с номером ${widget.taskNumber}',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
                  itemCount: _tasks.length,
                  itemBuilder: (context, index) {
                    final task = _tasks[index];
                    return _buildTaskTile(context, task, index + 1);
                  },
                ),
    );
  }

  Widget _buildTaskTile(BuildContext context, KompegeTask task, int index) {
    final preview = _conditionPreview(task.condition);
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute<void>(
                builder: (context) => TaskDetailScreen(task: task),
              ),
            );
          },
          borderRadius: BorderRadius.circular(16),
          child: Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              border: Border.all(
                color: Theme.of(context)
                    .colorScheme
                    .outlineVariant
                    .withValues(alpha: 0.6),
              ),
              borderRadius: BorderRadius.circular(16),
              color: Theme.of(context).colorScheme.surface,
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  width: 36,
                  height: 36,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: Theme.of(context)
                        .colorScheme
                        .surfaceContainerHighest
                        .withValues(alpha: 0.8),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Text(
                    '$index',
                    style: Theme.of(context).textTheme.labelLarge?.copyWith(
                          fontWeight: FontWeight.w600,
                        ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        preview,
                        style: Theme.of(context).textTheme.bodyMedium,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 6),
                      Container(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: Theme.of(context)
                              .colorScheme
                              .primaryContainer
                              .withValues(alpha: 0.5),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          KompegeTasksService.difficultyLabel(task.difficulty),
                          style: Theme.of(context).textTheme.labelSmall?.copyWith(
                                color: Theme.of(context).colorScheme.onPrimaryContainer,
                              ),
                        ),
                      ),
                    ],
                  ),
                ),
                Icon(
                  Icons.chevron_right,
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  String _conditionPreview(String html) {
    String text = html
        .replaceAll(RegExp(r'<[^>]+>'), ' ')
        .replaceAll(RegExp(r'\s+'), ' ')
        .trim();
    if (text.length > 120) text = '${text.substring(0, 117)}...';
    return text.isEmpty ? 'Условие задачи' : text;
  }
}
