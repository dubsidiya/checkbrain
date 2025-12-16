from itertools import permutations

table = '257 17 58 678 137 47 124568 347'.split()
graph = 'АВ АГ БГ БД ВГ ВЕ ГД ГЕ ГИ ЕЖ ДИ ЖИ'.split()

print( *range(1,9) )

for p in permutations('АБВГДЕЖИ'):
  if all( str(p.index(b)+1) in table[p.index(a)] for a, b in tuple(graph) ):
     print( *p )