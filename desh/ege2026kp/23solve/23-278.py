# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 3, e) + f(s * 3, e) + f(s + 4, e)

print(f(16, 96) * f(96, 99) * f(99, 105))
