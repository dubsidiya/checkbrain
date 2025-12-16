# Вариант 1

V = (1000000 * 60 - 12*1024*8) * 1.35
N = 44000 * 60 * 2
print( int(V / N) )

# Вариант 2

for i in range(1,100):
  I = i * 44000 * 60 * 2
  Ifull = I / 1.35 + 12*1024*8
  if Ifull > 1000000*60: break
  iMax = i

print( iMax )
