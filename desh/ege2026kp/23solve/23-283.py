# Автор: М. Ишимов

def f(s, e):
  if s >= e: return s == e
  return f(s + 3, e) + f(s * 2, e) + f(s + 2, e)

print(f(15, 61) * f(61, 64) * f(64, 80))




