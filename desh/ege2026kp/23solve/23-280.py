# Автор: М. Ишимов

def f(s, e):
  if s <= e: return s == e
  return f(s - 3, e) + f(s - 2, e) + f(s - 1, e)

print(f(36, 28) * f(28, 26) * f(26, 13))


