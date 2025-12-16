# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 20: return s == e
  return f(s - 6, e) + f(s - 1, e) + f(s // 4, e)

print(f(42, 12) * f(12, 10) * f(10, 6))





