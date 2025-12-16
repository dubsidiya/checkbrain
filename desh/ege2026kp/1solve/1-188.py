from itertools import permutations

table = '268 134678 257 27 38 12 234 125'.split()
graph = 'АВ АГ БГ БД ВГ ВЕ ГД ГЕ ГИ ЕЖ ДИ ЖИ'.split()

print( *range(1,9) )

for p in permutations('АБВГДЕЖИ'):
  if all( str(p.index(b)+1) in table[p.index(a)] for a, b in tuple(graph) ):
     print( *p )