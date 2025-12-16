def coprime(a, b):
   while b:
      a, b = b, a % b
   return a == 1

pairs = set()

NUM_CMD = 5
def Landysh( a, b, n = 0 ):
  global pairs
  if n == NUM_CMD:
    if coprime(a, b):
      pairs.add( (a, b) if a < b else (b, a) )
    return
  Landysh( a + 3, b, n + 1 )
  Landysh( a * 4, b, n + 1 )
  Landysh( a, b + 5, n + 1 )
  Landysh( a, b * 2, n + 1 )

Landysh(2, 3)

print( len(pairs) )
