
def f( start, end, prog = '' ):
  return 0 if start > end or 'BBA' in prog else \
         1 if start == end else \
         f( start*2, end, prog+'A' ) + \
           f( start+2, end, prog+'B' )

print( f(4, 42) )


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
    return f(a * 2, b, way[::], 'A') + f(a + 2, b, way[::], 'B')

print("Всего траекторий:", f(4, 42))
num = 0
print("Список всех программ, не содержащих BBA:")
for  e in trajectory:
    if 'BBA' not in e:
        num += 1
        print(num, '|', e)
