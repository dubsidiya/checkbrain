import 'package:flutter/material.dart';
import '../models/task.dart';

class ResultsScreen extends StatelessWidget {
  final Variant variant;

  const ResultsScreen({super.key, required this.variant});

  @override
  Widget build(BuildContext context) {
    final correctCount = variant.correctCount;
    final incorrectCount = variant.incorrectCount;
    final totalCount = variant.totalCount;
    final percentage = totalCount > 0 ? (correctCount / totalCount * 100).round() : 0;

    final duration = variant.endTime != null && variant.startTime != null
        ? variant.endTime!.difference(variant.startTime!)
        : null;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Результаты варианта'),
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Общая статистика
            Card(
              color: Theme.of(context).colorScheme.primaryContainer,
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  children: [
                    Text(
                      'Вариант ${variant.variantNumber}',
                      style: Theme.of(context).textTheme.headlineSmall?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                    const SizedBox(height: 24),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _buildStatCard(
                          context,
                          'Правильно',
                          correctCount.toString(),
                          Colors.green,
                        ),
                        _buildStatCard(
                          context,
                          'Неправильно',
                          incorrectCount.toString(),
                          Colors.red,
                        ),
                        _buildStatCard(
                          context,
                          'Всего',
                          totalCount.toString(),
                          Theme.of(context).colorScheme.primary,
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),
                    Text(
                      'Процент правильных ответов: $percentage%',
                      style: Theme.of(context).textTheme.titleLarge?.copyWith(
                            fontWeight: FontWeight.bold,
                          ),
                    ),
                    if (duration != null) ...[
                      const SizedBox(height: 16),
                      Text(
                        'Время выполнения: ${_formatDuration(duration)}',
                        style: Theme.of(context).textTheme.bodyLarge,
                      ),
                    ],
                  ],
                ),
              ),
            ),
            const SizedBox(height: 24),

            // Детали по задачам
            Text(
              'Детали по задачам:',
              style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
            ),
            const SizedBox(height: 16),
            ...variant.tasks.map((task) => _buildTaskResultCard(context, task)),
          ],
        ),
      ),
      floatingActionButton: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          FloatingActionButton.extended(
            heroTag: "back_to_variant",
            onPressed: () {
              // Возвращаемся к варианту для повторной проверки
              Navigator.pop(context);
            },
            icon: const Icon(Icons.arrow_back),
            label: const Text('Вернуться к варианту'),
            backgroundColor: Theme.of(context).colorScheme.secondary,
          ),
          const SizedBox(height: 8),
          FloatingActionButton.extended(
            heroTag: "go_home",
            onPressed: () {
              Navigator.of(context).popUntil((route) => route.isFirst);
            },
            icon: const Icon(Icons.home),
            label: const Text('На главную'),
          ),
        ],
      ),
    );
  }

  Widget _buildStatCard(BuildContext context, String label, String value, Color color) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: color.withOpacity(0.2),
            shape: BoxShape.circle,
          ),
          child: Text(
            value,
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: color,
            ),
          ),
        ),
        const SizedBox(height: 8),
        Text(
          label,
          style: Theme.of(context).textTheme.bodyMedium,
        ),
      ],
    );
  }

  Widget _buildTaskResultCard(BuildContext context, Task task) {
    final isCorrect = task.isCorrect;
    final hasAnswer = task.userAnswer != null && task.userAnswer!.isNotEmpty;

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      color: isCorrect == true
          ? Colors.green.withOpacity(0.1)
          : isCorrect == false
              ? Colors.red.withOpacity(0.1)
              : null,
      child: ExpansionTile(
        leading: Icon(
          isCorrect == true
              ? Icons.check_circle
              : isCorrect == false
                  ? Icons.cancel
                  : Icons.help_outline,
          color: isCorrect == true
              ? Colors.green
              : isCorrect == false
                  ? Colors.red
                  : Colors.grey,
        ),
        title: Text('Задача ${task.taskNumber}'),
        subtitle: Text(
          isCorrect == true
              ? 'Правильно'
              : isCorrect == false
                  ? 'Неправильно'
                  : hasAnswer
                      ? 'Ответ не проверен'
                      : 'Ответ не дан',
        ),
        children: [
          Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Всегда показываем правильный ответ, даже если он null
                _buildAnswerRow(
                  context,
                  'Правильный ответ:',
                  task.answer ?? 'Не найден',
                  task.answer != null ? Colors.green : Colors.grey,
                ),
                const SizedBox(height: 12),
                if (hasAnswer) ...[
                  _buildAnswerRow(
                    context,
                    'Ваш ответ:',
                    task.userAnswer!,
                    isCorrect == true ? Colors.green : Colors.red,
                  ),
                  const SizedBox(height: 12),
                ],
                if (task.userCode != null && task.userCode!.isNotEmpty) ...[
                  Text(
                    'Ваш код:',
                    style: Theme.of(context).textTheme.titleSmall?.copyWith(
                          fontWeight: FontWeight.bold,
                        ),
                  ),
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Theme.of(context).colorScheme.surfaceVariant,
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: SelectableText(
                      task.userCode!,
                      style: const TextStyle(fontFamily: 'monospace', fontSize: 12),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildAnswerRow(BuildContext context, String label, String value, Color color) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        SizedBox(
          width: 150,
          child: Text(
            label,
            style: Theme.of(context).textTheme.titleSmall?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
          ),
        ),
        Expanded(
          child: Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: color.withOpacity(0.1),
              borderRadius: BorderRadius.circular(4),
              border: Border.all(color: color.withOpacity(0.3)),
            ),
            child: SelectableText(
              value,
              style: TextStyle(color: color, fontWeight: FontWeight.w500),
            ),
          ),
        ),
      ],
    );
  }

  String _formatDuration(Duration duration) {
    final hours = duration.inHours;
    final minutes = duration.inMinutes.remainder(60);
    final seconds = duration.inSeconds.remainder(60);

    if (hours > 0) {
      return '${hours}ч ${minutes}м ${seconds}с';
    } else if (minutes > 0) {
      return '${minutes}м ${seconds}с';
    } else {
      return '${seconds}с';
    }
  }
}

