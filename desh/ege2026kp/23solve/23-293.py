# Автор: М. Ишимов

def f(s, e):
  if s >= e or s == 19: return s == e
  return f(s * 4, e) + f(s + 2, e) + f(s + 4, e)

print(f(8, 24) * f(24, 36))





