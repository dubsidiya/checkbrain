# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 28: return s == e
  return f(s - 3, e) + f(s - 5, e) + f(s // 3, e)

print(f(41, 12))






