# Автор: М. Ишимов

def f(s, e):
  if s <= e: return s == e
  return f(s - 3, e) + f(s - 5, e)

print(f(49, 15))





