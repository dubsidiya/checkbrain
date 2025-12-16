# Автор: М. Ишимов

def f(s, e):
  if s <= e: return s == e
  return f(s - 3, e) + f(s - 4, e) + f(s // 2, e)

print(f(28, 13))
