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
    if (src.startsWith('data:image')) {
      // data URL — не поддерживаем отображение напрямую в Image.network
      return const SizedBox.shrink();
    }
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Image.network(
        src,
        fit: BoxFit.contain,
        loadingBuilder: (context, child, loadingProgress) {
          if (loadingProgress == null) return child;
          return SizedBox(
            height: 120,
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
        errorBuilder: (context, error, stackTrace) {
          return Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Theme.of(context).colorScheme.errorContainer,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Row(
              children: [
                Icon(
                  Icons.broken_image_outlined,
                  color: Theme.of(context).colorScheme.onErrorContainer,
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    'Не удалось загрузить изображение',
                    style: TextStyle(
                      color: Theme.of(context).colorScheme.onErrorContainer,
                      fontSize: 12,
                    ),
                  ),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
