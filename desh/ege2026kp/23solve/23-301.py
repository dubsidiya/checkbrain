# Автор: М. Ишимов

def f(s, e):
  if s <= e or s == 27: return s == e
  return f(s - 1, e) + f(s - 5, e)

print(f(32, 26) * f(26, 24) * f(24, 17))







