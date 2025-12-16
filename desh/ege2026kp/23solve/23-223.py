def f( start, end, prog = "" ):
  return 0 if start > end or (start == end and 'BCA' not in prog) else \
         1 if start == end else \
         f( start+1, end, prog+"A" ) + \
           f( start*2, end, prog+"B" ) + \
           f( start*3, end, prog+"C" )

print( f( 2, 27 ) )

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
    return f(a + 1, b, way[::], 'A') + f(a * 2, b, way[::], 'B') + f(a * 3, b, way[::], 'C')

print("Всего траекторий:", f(2, 27))
num = 0
print("Список всех команд содержащих BCA:")
for  e in trajectory:
    if 'BCA' in e:
        num += 1
        print(num, '|', e)
