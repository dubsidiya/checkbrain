s = open( '24-277.txt' ). readline()

for c in 'EIOUY':
  s = s.replace( c, 'A' )

maxLenA = 0
sA = ''
for i, c in enumerate(s):
  if c in '13579':
    if len(sA) > max(1,maxLenA) and sA[0] == c:
      print( len(sA)-1, sA+c )
      maxLenA = max( len(sA)-1, maxLenA )
    sA = c
  elif c == 'A':
    if sA: sA += c
  else:
    sA = ''

print( maxLenA )
print( any( c+maxLenA*'A'+c in s for c in '13579' ) )

# Вариант 2: метод грубой силы

maxLenA = 0
for border in '13579':
  countA = 1
  while border + countA*'A' in s:
    if border + countA*'A' + border in s:
      maxLenA = max( countA, maxLenA )
    countA += 1

print( maxLenA )