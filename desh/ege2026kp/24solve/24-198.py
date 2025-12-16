# Текстовый файл состоит из символов X, Y и Z.
# Определите максимальное количество идущих подряд троек
# символов X*Y или Z*Y в прилагаемом файле. Здесь *
# обозначает любой символ.

s = open('24-197.txt').readline()
maxLen = curLen = 0
countMax = 0
for i in range(len(s)):
  if s[i] == 'Y': continue # цепочка не начинается с Y
  state = count = 0
  for k in range(i+1, len(s)):
    # if state == 0: все символы разрешены, проходим дальше
    if state == 1: # требуется Y
      if s[k] == 'Y':
        count += 1
        if count > countMax:
           print( s[i:k+1] )
      else: break
    elif state == 2: # требуется X или Z
      if s[k] not in ['X', 'Z']: break
    state = (state + 1) % 3
  countMax = max( countMax, count )

print( countMax )

