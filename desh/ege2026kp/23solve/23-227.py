
def f( start, end, prog = '' ):
  return 0 if start > end or 'BACA' in prog else \
         1 if start == end else \
         f( start+2, end, prog+'A' ) + \
           f( start*2, end, prog+'B' ) + f( start*4, end, prog+'C' )

print( f(1, 24) )


# Автор: И. Карпачев

trajectory = list()

def f(a, b, way='', command=' '):
    way += command
    if a > b:
        return 0
    if a == b:
        trajectory.append(way[1:])
        way = ''
        return 1
    return f(a + 2, b, way[::], 'A') + f(a * 2, b, way[::], 'B') + f(a * 4, b, way[::], 'C')

print("Всего траекторий:", f(1, 24))
num = 0
print("Список всех команд не содержащих BACA:")
for  e in trajectory:
    if 'BACA' not in e:
        num += 1
        #print(num, '|', e)
print(num)
