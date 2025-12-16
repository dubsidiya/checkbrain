# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 18: return s == e
  return f(s - 1, e) + f(s // 4, e)

print(f(34, 30) * f(30, 27) * f(27, 5))
