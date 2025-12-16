# Автор: М. Ишимов

def f(s, e):
  if s >= e or s == 18: return s == e
  return f(s * 3, e) + f(s + 2, e)

print(f(4, 46) * f(46, 52))



