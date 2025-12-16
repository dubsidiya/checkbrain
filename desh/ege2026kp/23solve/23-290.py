# Автор: М. Ишимов

k = 0

def f(s, e):
  if s <= e or s == 31: return s == e
  return f(s - 3, e) + f(s - 4, e)
k += f(44, 33) * f(33, 19)

def f(s, e):
  if s <= e or s == 33: return s == e
  return f(s - 3, e) + f(s - 4, e)
k += f(44, 31) * f(31, 19)

def f(s, e):
  if s <= e or s == 33 or s == 31: return s == e
  return f(s - 3, e) + f(s - 4, e)
k += f(44, 19)

print(k)



