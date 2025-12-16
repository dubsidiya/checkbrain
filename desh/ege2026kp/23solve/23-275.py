# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 32: return s == e
  return f(s - 1, e) + f(s - 2, e) + f(s - 4, e)

print(f(37, 22) * f(22, 16) * f(16, 8))
