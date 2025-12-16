# Автор: А. Кабанов
# Разбор: https://www.youtube.com/watch?v=DbLCvM4NvMc

with open("26-162.txt") as F:
  N, K = map( int, F.readline().split() )
  data = []
  for _ in range(N):
    size, type = F.readline().strip().split()
    data.append( (int(size), type) )

data.sort()

# массив упакованных подарков
packed = [ (0, 0) for i in range(N) ] # количество вложенных коробок и min вложенная коробка
for i in range(N):
  # максимальное количество вложенных коробок
  m = 0
  minBox = float("inf")
  # проверяем все коробочки меньшего размера
  for j in range(i):
    # если эту коробочку можно вложить в i-ю c ее содержимым
    if data[i][0] - data[j][0] >= K and data[i][1] != data[j][1]:
      if packed[j][0] > m or (packed[j][0] == m and packed[j][1] < minBox):
        m, minBox = packed[j]
  if minBox == float("inf"):
    minBox = data[i][0]
  packed[i] = (m + 1, minBox)

print( max(packed) )




