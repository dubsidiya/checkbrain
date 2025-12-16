def alg( N ):
  s = f'{N:b}'
  if N % 2 == 0:
    s = '10' + s
  else:
    s = '1' + s + '01'
  return int(s, 2)

end = 1_234_567
results = []
for N in range(end+1):
  R = alg(N)
  if R <= end:
    results.append( R )

print( max(results) )
