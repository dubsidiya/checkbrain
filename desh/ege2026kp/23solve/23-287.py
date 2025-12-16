# Автор: М. Ишимов

def f(s, e):
  if s >= e or s == 17: return s == e
  return f(s * 4, e) + f(s + 3, e) + f(s + 2, e)

print(f(7, 38) * f(38, 40) * f(40, 56))



