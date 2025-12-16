"""
Повтори 7 [
  Повтори 2 [ Вперед 3 ]
  Закрасить
  Назад 4
  Закрасить ]
Сколько клеток будет закрашено?
"""
x = 0

painted = set()
for _ in range(7):
  for _ in range(2):
     # Вперед 3
     x += 3
  # Закрасить
  painted.add( x )
  # Назад 4
  x -= 4
  # Закрасить
  painted.add( x )

print( len(painted) )