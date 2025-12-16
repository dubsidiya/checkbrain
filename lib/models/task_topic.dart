class TaskTopic {
  final String id;
  final String name;
  final String description;
  final List<int> taskNumbers;

  TaskTopic({
    required this.id,
    required this.name,
    required this.description,
    required this.taskNumbers,
  });
}

// Темы задач ЕГЭ по информатике
class TaskTopics {
  static final List<TaskTopic> topics = [
    TaskTopic(
      id: 'coding',
      name: 'Кодирование информации',
      description: 'Кодирование и декодирование информации, определение количества информации',
      taskNumbers: [1, 5, 7, 10],
    ),
    TaskTopic(
      id: 'logic',
      name: 'Логика и таблицы истинности',
      description: 'Таблицы истинности, логические выражения, преобразование логических формул',
      taskNumbers: [2, 15, 23],
    ),
    TaskTopic(
      id: 'models',
      name: 'Информационные модели',
      description: 'Графы, схемы, таблицы, информационные модели',
      taskNumbers: [3, 4, 9, 18, 22],
    ),
    TaskTopic(
      id: 'databases',
      name: 'Базы данных',
      description: 'Базы данных, поиск информации в таблицах',
      taskNumbers: [4],
    ),
    TaskTopic(
      id: 'executors',
      name: 'Исполнители и алгоритмы',
      description: 'Алгоритмы для исполнителей, исполнители',
      taskNumbers: [6, 8, 11, 16, 19, 20, 21],
    ),
    TaskTopic(
      id: 'spreadsheets',
      name: 'Электронные таблицы',
      description: 'Электронные таблицы, формулы и функции, диаграммы',
      taskNumbers: [9, 18],
    ),
    TaskTopic(
      id: 'networks',
      name: 'Сети и адресация',
      description: 'IP-адреса, адресация в сетях, определение объёма информации',
      taskNumbers: [12, 13],
    ),
    TaskTopic(
      id: 'number_systems',
      name: 'Системы счисления',
      description: 'Позиционные системы счисления, преобразование чисел',
      taskNumbers: [14],
    ),
    TaskTopic(
      id: 'programming',
      name: 'Программирование',
      description: 'Обработка данных, массивы, строки, последовательности',
      taskNumbers: [17, 19, 24, 25, 26, 27],
    ),
    TaskTopic(
      id: 'analysis',
      name: 'Анализ программ',
      description: 'Анализ программ, поиск ошибок, определение результата работы программы',
      taskNumbers: [22],
    ),
  ];

  // Получить тему по номеру задачи
  static TaskTopic? getTopicByTaskNumber(int taskNumber) {
    for (final topic in topics) {
      if (topic.taskNumbers.contains(taskNumber)) {
        return topic;
      }
    }
    return null;
  }

  // Получить все темы, содержащие задачу
  static List<TaskTopic> getTopicsByTaskNumber(int taskNumber) {
    return topics.where((topic) => topic.taskNumbers.contains(taskNumber)).toList();
  }

  // Получить все номера задач по теме
  static List<int> getTaskNumbersByTopic(String topicId) {
    final topic = topics.firstWhere(
      (t) => t.id == topicId,
      orElse: () => topics.first,
    );
    return topic.taskNumbers;
  }
}

