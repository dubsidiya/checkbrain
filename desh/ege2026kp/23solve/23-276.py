# Автор: М. Ишимов

def f(s, e):
  if s <= e: return s == e
  return f(s - 3, e) + f(s - 2, e) + f(s // 2, e)

print(f(34, 23) * f(23, 21) * f(21, 19))
