import 'package:flutter/material.dart';
import 'screens/task_selection_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'CheckBrain - Подготовка к ЕГЭ по информатике',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const TaskSelectionScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}
