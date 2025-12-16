class Task {
  final int taskNumber;
  final int variantNumber;
  final String? answer;
  final String? solutionCode;
  final String? userAnswer;
  final String? userCode;
  final bool? isCorrect;

  Task({
    required this.taskNumber,
    required this.variantNumber,
    this.answer,
    this.solutionCode,
    this.userAnswer,
    this.userCode,
    this.isCorrect,
  });

  Task copyWith({
    int? taskNumber,
    int? variantNumber,
    String? answer,
    String? solutionCode,
    String? userAnswer,
    String? userCode,
    bool? isCorrect,
  }) {
    return Task(
      taskNumber: taskNumber ?? this.taskNumber,
      variantNumber: variantNumber ?? this.variantNumber,
      answer: answer ?? this.answer,
      solutionCode: solutionCode ?? this.solutionCode,
      userAnswer: userAnswer ?? this.userAnswer,
      userCode: userCode ?? this.userCode,
      isCorrect: isCorrect ?? this.isCorrect,
    );
  }
}

class Variant {
  final int variantNumber;
  final List<Task> tasks;
  final DateTime? startTime;
  final DateTime? endTime;

  Variant({
    required this.variantNumber,
    required this.tasks,
    this.startTime,
    this.endTime,
  });

  int get correctCount => tasks.where((t) => t.isCorrect == true).length;
  int get incorrectCount => tasks.where((t) => t.isCorrect == false).length;
  int get totalCount => tasks.length;
}

