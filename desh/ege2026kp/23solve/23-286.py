# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 3, e) + f(s + 4, e)

print(f(17, 27) * f(27, 56) * f(56, 80))



