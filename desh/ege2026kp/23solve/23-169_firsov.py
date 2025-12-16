# Автор: М. Фирсов

# формирование возможных маршрутов
С = 5 # вместо 5 можно взять любое число
a = [[С]]; k = 9
for _ in range(k):
    b = []
    for i in a:
        b.append(i + [i[-1] + 3])
        b.append(i + [i[-1] - 1])
    a = b[:]

#ways будет принимать возможные циклические программы, где С встречается более 1 раза.
ways = [];
for way in a:
  if way.count(С) >= 2: ways.append(way)

#Подсчет подходящих программ. Вывод их количества.
cnt = 0
for way in ways:
  pos2 = 1 + way[1:].index(way[0])
  for i in range(pos2, len(way)):
    if way[i] != way[i-pos2]:
      break
  else:
    print( way )
    cnt += 1
print(cnt)

