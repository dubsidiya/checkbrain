# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 2, e) + f(s + 4, e)

print(f(3, 9) * f(9, 61) * f(61, 69))

