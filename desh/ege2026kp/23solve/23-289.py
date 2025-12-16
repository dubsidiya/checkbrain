# Автор: М. Ишимов

k = 0

def f(s, e):
  if s >= e or s == 47: return s == e
  return f(s ** 2, e) + f(s + 3, e) + f(s + 4, e)
k += f(10, 49) * f(49, 60)

def f(s, e):
  if s >= e or s == 49: return s == e
  return f(s ** 2, e) + f(s + 3, e) + f(s + 4, e)
k += f(10, 47) * f(47, 60)

def f(s, e):
  if s >= e or s == 47 or s == 49: return s == e
  return f(s ** 2, e) + f(s + 3, e) + f(s + 4, e)
k += f(10, 60)

print(k)



