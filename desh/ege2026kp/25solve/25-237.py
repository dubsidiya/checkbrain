D = 103

results = []
def rec( s = '' ):
  n = int(s) if s else -1
  if n % D == 0:
     results.append( n )
     return
  lastDigit = 0 if not s else int(s[-1])
  for nextDigit in range(lastDigit+1, 10):
    rec( s + str(nextDigit) )

rec()
for n in sorted(results):
  print( n, n // D )
