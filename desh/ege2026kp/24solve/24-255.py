from string import ascii_uppercase

L = []
for s in open('24-164.txt'):
  D = {}
  for i in range(len(s)-1):
    if s[i] == 'X':
      D[s[i+1]] = D.get(s[i+1], 0) + 1
  M = max( D.values() )
  L.extend( [ c for c in D if D[c] == M ] )

print( max( L.count(c) for c in ascii_uppercase ) )