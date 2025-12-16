from re import findall

s0 = open('24-347.txt').readline()

s = s0

num12 = r'([1-9AB][0-9AB]*)'
pattern = fr'(?={num12})'

parts = findall( pattern, s )

full = parts[:]
for p in parts:
  for i in range(1,len(p)):
    full.append( p[:-i] )

parts = [ p for p in full if int(p,12) % 11 == 0 ]

sMax = max( parts, key=lambda x: int(x,12)  )
print( s.find(sMax)+len(sMax)-1, len(sMax), sMax)

