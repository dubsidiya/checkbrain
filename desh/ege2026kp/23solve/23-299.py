# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 3, e) + f(s * 4, e) + f(s + 4, e)

print(f(11, 20) * f(20, 55))







