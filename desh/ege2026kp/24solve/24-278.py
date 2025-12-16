s = open( '24-278.txt' ). readline()

for c in 'KNL':
  s = s.replace( c, 'F' )

maxLenF = 0
sF = ''
for i, c in enumerate(s):
  if c in '02468':
    if len(sF) > max(1,maxLenF) and sF[0] == c:
      print( len(sF)-1, sF+c )
      maxLenF = max( len(sF)-1, maxLenF )
    sF = c
  elif c == 'F':
    if sF: sF += c
  else:
    sF = ''

print( maxLenF )
print( any( c+maxLenF*'F'+c in s for c in '02468' ) )

# Вариант 2: метод грубой силы

maxLenF = 0
for border in '02468':
  countF = 1
  while border + countF*'F' in s:
    if border + countF*'F' + border in s:
      maxLenF = max( countF, maxLenF )
    countF += 1

print( maxLenF )