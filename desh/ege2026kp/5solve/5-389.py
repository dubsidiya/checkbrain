def alg( N ):
  s = f'{N:b}'
  return int( f"{s.count('0'):b}{s.count('1'):b}", 2)

R = 214
s = f'{R:b}'

results = []
for i, c in enumerate(s):
  if i > 0 and c == '1':
    count0 = int( s[:i], 2 )
    count1 = int( s[i:], 2 )
    Nbin = '1' + '0'*count0 + '1'*(count1-1)
    N = int(Nbin, 2)
    print( N, Nbin, alg(N) )
    results.append( N )

print( min(results) )