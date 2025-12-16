# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 19: return s == e
  return f(s - 2, e) + f(s - 1, e) + f(s // 2, e)

print(f(36, 16) * f(16, 15) * f(15, 12))



