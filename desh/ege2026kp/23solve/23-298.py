# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 32: return s == e
  return f(s // 4, e) + f(s - 1, e) + f(s - 5, e)

print(f(43, 39) * f(39, 17))







