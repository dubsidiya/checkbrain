def tr(n):
    if n == 0: return '0'
    s = ''
    while n > 0:
        s = str(n%3)+s
        n //= 3
    return s

ans = []
for n in range(1, 10000):
    n3 = tr(n)
    if n in [11,12]:
      print( n, n3 )
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        n3 += tr( (n % 3 - 1)*3 )
    R = int(n3, 3)
    if n in [11,12]:
      print( n, n3, R )
    if R <= 200:
      ans.append(R)
print( max(ans) )

