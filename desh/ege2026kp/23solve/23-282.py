# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 25: return s == e
  return f(s - 2, e) + f(s - 1, e)

print(f(42, 28) * f(28, 17))




