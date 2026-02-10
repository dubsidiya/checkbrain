import 'package:flutter/material.dart';
import '../services/kompege_tasks_service.dart';
import '../widgets/task_condition_content.dart';

/// Экран просмотра одной задачи из сборника (условие + ответ).
class TaskDetailScreen extends StatelessWidget {
  const TaskDetailScreen({super.key, required this.task});

  final KompegeTask task;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Задача ${task.taskNumber}'),
        centerTitle: true,
        backgroundColor: Theme.of(context).colorScheme.surface,
        foregroundColor: Theme.of(context).colorScheme.onSurface,
        elevation: 0,
        scrolledUnderElevation: 1,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            _buildSection(
              context,
              label: 'Условие',
              child: TaskConditionContent(content: task.condition),
            ),
            const SizedBox(height: 20),
            _buildSection(
              context,
              label: 'Ответ',
              child: SelectableText(
                task.answer.isEmpty ? '—' : task.answer,
                style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                      fontWeight: FontWeight.w500,
                    ),
              ),
            ),
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              decoration: BoxDecoration(
                color: Theme.of(context)
                    .colorScheme
                    .surfaceContainerHighest
                    .withValues(alpha: 0.6),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Text(
                KompegeTasksService.difficultyLabel(task.difficulty),
                style: Theme.of(context).textTheme.labelMedium?.copyWith(
                      color: Theme.of(context).colorScheme.onSurfaceVariant,
                    ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSection(
    BuildContext context, {
    required String label,
    required Widget child,
  }) {
    return Card(
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(
          color: Theme.of(context)
              .colorScheme
              .outlineVariant
              .withValues(alpha: 0.6),
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(
                color: Theme.of(context)
                    .colorScheme
                    .primaryContainer
                    .withValues(alpha: 0.6),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Text(
                label,
                style: Theme.of(context).textTheme.titleSmall?.copyWith(
                      fontWeight: FontWeight.w600,
                      color: Theme.of(context).colorScheme.onPrimaryContainer,
                    ),
              ),
            ),
            const SizedBox(height: 12),
            child,
          ],
        ),
      ),
    );
  }
}
