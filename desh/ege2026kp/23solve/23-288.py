# Автор: М. Ишимов

k = 0

def f(s, e):
  if s <= e or s == 17: return s == e
  return f(s - 3, e) + f(s - 2, e)
k += f(43, 19) * f(19, 7)

def f(s, e):
  if s <= e or s == 19: return s == e
  return f(s - 3, e) + f(s - 2, e)
k += f(43, 17) * f(17, 7)

def f(s, e):
  if s <= e or s == 19 or s == 17: return s == e
  return f(s - 3, e) + f(s - 2, e)
k += f(43, 7)
print(k)



