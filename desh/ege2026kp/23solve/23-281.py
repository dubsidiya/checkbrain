# Автор: М. Ишимов

def f(s, e):
  if s <= e: return s == e
  return f(s - 3, e) + f(s // 3, e) + f(s - 2, e)

print(f(43, 21) * f(21, 15) * f(15, 13))



