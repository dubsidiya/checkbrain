# Автор: М. Ишимов

k = 0

def f(s, e):
  if s <= e or s == 20: return s == e
  return f(s - 3, e) + f(s - 1, e) + f(s - 4, e)
k += f(43, 23) * f(23, 17)

def f(s, e):
  if s <= e or s == 23: return s == e
  return f(s - 3, e) + f(s - 1, e) + f(s - 4, e)
k += f(43, 20) * f(20, 17)

def f(s, e):
  if s <= e or s == 23 or s == 20: return s == e
  return f(s - 3, e) + f(s - 1, e) + f(s - 4, e)
k += f(43, 17)
print(k)
