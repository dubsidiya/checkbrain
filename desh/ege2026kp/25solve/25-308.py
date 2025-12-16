def valid( n ):
  s = sum( map(int, str(n)) )
  return n > 0 and n % s**3 == 0
def gen( L ):
  if L < 1: return []
  fmt = f"%0{L}d"
  v = [ fmt % n for n in range(10**L) if valid(n) ]
  return v

vArr = []
for L in range(7):
  vArr.extend( gen(L) )
for v in vArr:
  n = int('1234' + v)
  if n % 137 == 0:
    print( n, n // 137 )

print('---------------------------')

# Автор: А. Фахуртдинова

for x in range(0, 2*10**9, 137):
    y = str(x)
    n = len(y)
    if n>4 and y[0:4]=='1234':
        s=sum(int(i) for i in y[4:])
        if int(y[4:n])%(s**3)==0:
            print(x, x//137)