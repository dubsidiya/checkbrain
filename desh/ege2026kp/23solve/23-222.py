def f( start, end, prog = "" ):
  return 0 if start > end or (start == end and 'ABA' not in prog) else \
         1 if start == end else \
         f( start*2, end, prog+"A" ) + \
           f( start+3, end, prog+"B" )

print( f( 2, 38 ) )


# Автор: И. Кропачев

trajectory = list()

def f(a, b, way='', command=' '):
    way += command
    if a > b:
        return 0
    if a == b:
        trajectory.append(way[1:])
        way = ''
        return 1
    return f(a * 2, b, way[::], 'A') + f(a + 3, b, way[::], 'B')

print("Всего траекторий:", f(2, 38))
num = 0
print("Список всех команд содержащих ABA:")
for  e in trajectory:
    if 'ABA' in e:
        num += 1
        print(num, '|', e)
