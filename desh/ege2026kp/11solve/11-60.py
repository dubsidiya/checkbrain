from math import ceil, log2

part1 = ceil(log2(10*10))
part2 = ceil(log2(10*10*10))
print( ceil(24*(part1+part2)/8) )
