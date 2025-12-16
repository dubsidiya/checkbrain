# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 24: return s == e
  return f(s - 2, e) + f(s - 4, e)

print(f(34, 28) * f(28, 12))




