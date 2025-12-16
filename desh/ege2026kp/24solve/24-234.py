s = open('24-234.txt').readline()

def sumDigitsL( n ):
  L = len(n)
  sumL = sum( int(c)**L for c in n )
  return sumL

selected = []
for i in range(10,1000000):
  if sumDigitsL(str(i)) == i:
    selected.append( i )

for num in selected[::-1]:
  if str(num) in s:
    print( num, s.count(str(num)) )

