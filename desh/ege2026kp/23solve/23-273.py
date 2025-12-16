# Автор: М. Ишимов

k = 0
def f(s, e):
  if s <= e or s == 8: return s == e
  return f(s - 4, e) + f(s // 2, e)
k += f(39, 23) * f(23, 4)

def f(s, e):
  if s <= e or s == 23: return s == e
  return f(s - 4, e) + f(s // 2, e)
k += f(39, 8) * f(8, 4)

def f(s, e):
  if s <= e or s == 23 or s == 8: return s == e
  return f(s - 4, e) + f(s // 2, e)
k += f(39, 4)

print(k)
