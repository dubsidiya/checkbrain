fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 55]

results = set()
for c in [''] + list('9876543210'):
  for f1 in fib:
    for f2 in fib:
      n = int( '73' + c + '5' + str(f1) + '486' + str(f2) )
      if n < 1000000000 and n % 43 == 0:
        results.add( n )

results = sorted( list(results) )
for r in results:
  print( r, r // 43 )