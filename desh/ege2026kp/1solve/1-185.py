from itertools import permutations

table = '47 345 27 1267 268 458 134 56'.split()
graph = 'АБ АВ АГ БГ ВЕ ГЕ ГД ДЖ ДИ ЕЖ ЖИ'.split()

print( *range(1,10) )

for p in permutations('АБВГДЕЖИ'):
  if all( str(p.index(b)+1) in table[p.index(a)] for a, b in tuple(graph) ):
     print( *p )