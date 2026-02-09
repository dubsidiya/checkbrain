import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter_widget_from_html/flutter_widget_from_html.dart';

/// Отображает условие задачи: HTML (КЕГЭ) — рендерится красиво, иначе — обычный текст.
class TaskConditionContent extends StatelessWidget {
  const TaskConditionContent({
    super.key,
    required this.content,
    this.textStyle,
    this.selectable = true,
  });

  final String content;
  final TextStyle? textStyle;
  final bool selectable;

  static bool _looksLikeHtml(String text) {
    final t = text.trim();
    if (t.isEmpty) return false;
    if (t.startsWith('<') && t.contains('>')) return true;
    if (t.contains('</p>') || t.contains('</table>') || t.contains('<img')) {
      return true;
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    final style = textStyle ??
        Theme.of(context).textTheme.bodyLarge?.copyWith(
              height: 1.5,
              fontSize: 16,
            );
    final color = Theme.of(context).colorScheme.onSurface;

    if (!_looksLikeHtml(content)) {
      return SelectableText(
        content,
        style: style?.copyWith(fontFamily: 'monospace'),
      );
    }

    return HtmlWidget(
      content,
      textStyle: style?.copyWith(color: color),
      customStylesBuilder: (element) {
        if (element.localName == 'table') {
          return {
            'border-collapse': 'collapse',
            'width': '100%',
            'margin': '8px 0',
          };
        }
        if (element.localName == 'td' || element.localName == 'th') {
          return {
            'border': '1px solid',
            'padding': '6px 8px',
          };
        }
        if (element.localName == 'p') {
          return {'margin': '0 0 8px 0'};
        }
        if (element.localName == 'img') {
          return {'max-width': '100%', 'height': 'auto'};
        }
        return null;
      },
      customWidgetBuilder: (element) {
        if (element.localName == 'img') {
          final src = element.attributes['src'];
          if (src != null && src.isNotEmpty) {
            return _buildImage(context, src);
          }
        }
        return null;
      },
    );
  }

  Widget _buildImage(BuildContext context, String src) {
    const padding = EdgeInsets.symmetric(vertical: 8);

    // data:image/png;base64,... — декодируем и показываем через Image.memory
    if (src.startsWith('data:image')) {
      final base64 = _parseDataImageBase64(src);
      if (base64 != null && base64.isNotEmpty) {
        try {
          final bytes = base64Decode(base64);
          return Padding(
            padding: padding,
            child: Image.memory(
              bytes,
              fit: BoxFit.contain,
              errorBuilder: (context, error, stackTrace) =>
                  _buildImagePlaceholder(context),
            ),
          );
        } catch (_) {
          return Padding(
            padding: padding,
            child: _buildImagePlaceholder(context),
          );
        }
      }
    }

    // Сетевые изображения
    return Padding(
      padding: padding,
      child: Image.network(
        src,
        fit: BoxFit.contain,
        loadingBuilder: (context, child, loadingProgress) {
          if (loadingProgress == null) return child;
          return SizedBox(
            height: 100,
            child: Center(
              child: CircularProgressIndicator(
                value: loadingProgress.expectedTotalBytes != null
                    ? loadingProgress.cumulativeBytesLoaded /
                        (loadingProgress.expectedTotalBytes ?? 1)
                    : null,
              ),
            ),
          );
        },
        errorBuilder: (context, error, stackTrace) =>
            _buildImagePlaceholder(context),
      ),
    );
  }

  /// Из data:image/png;base64,XXXX возвращает XXXX (без префикса).
  static String? _parseDataImageBase64(String dataUrl) {
    final comma = dataUrl.indexOf(',');
    if (comma < 0) return null;
    return dataUrl.substring(comma + 1).trim();
  }

  /// Нейтральный плейсхолдер при ошибке загрузки (без красного блока).
  Widget _buildImagePlaceholder(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 16),
      decoration: BoxDecoration(
        color: Theme.of(context)
            .colorScheme
            .surfaceContainerHighest
            .withValues(alpha: 0.5),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.image_not_supported_outlined,
            size: 20,
            color: Theme.of(context).colorScheme.onSurfaceVariant,
          ),
          const SizedBox(width: 8),
          Text(
            'Изображение',
            style: Theme.of(context).textTheme.bodySmall?.copyWith(
                  color: Theme.of(context).colorScheme.onSurfaceVariant,
                ),
          ),
        ],
      ),
    );
  }
}
