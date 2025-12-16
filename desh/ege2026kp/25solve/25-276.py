from fnmatch import fnmatch

def valid( n ):
   s = str(n)
   sOdd = sum( int(x) for x in s if x in '13579' )
   return fnmatch( s, "124*5*79" ) and \
          sOdd > 0 and n % sOdd == 0

nums = []
for n in range(124579, 12495979+1):
   if valid(n):
      print( n, sum(map(int, str(n))) )



