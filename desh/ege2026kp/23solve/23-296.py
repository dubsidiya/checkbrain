# Автор: М. Ишимов

def f(s, e):
  if s >= e or s == 13: return s == e
  return f(s + 3, e) + f(s + 2, e) + f(s ** 2, e)

print(f(9, 55))





