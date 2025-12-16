from itertools import permutations

table = '26 134678 27 257 48 128 234 256'.split()
graph = 'АВ АГ БГ БД ВГ ВЕ ГД ГЕ ГИ ЕЖ ДИ ЖИ'.split()

print( *range(1,9) )

for p in permutations('АБВГДЕЖИ'):
  if all( str(p.index(b)+1) in table[p.index(a)] for a, b in tuple(graph) ):
     print( *p )