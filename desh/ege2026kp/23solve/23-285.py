# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 3, e) + f(s + 2, e) + f(s ** 2, e)

print(f(13, 25) * f(25, 75) * f(75, 89))



