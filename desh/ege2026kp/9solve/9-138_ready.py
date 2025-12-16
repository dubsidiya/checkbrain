p1, p2, p3 = [], [], []
for s in open('9-138.csv'):
   x1, x2, x3, y1, y2, y3 = map( int, s.split(';') )
   p1.append( (x1, y1) )
   p2.append( (x2, y2) )
   p3.append( (x3, y3) )

def isQuater( p, n ):
  x, y = p
  if x > 0 and y > 0: return n == 1
  if x < 0 and y > 0: return n == 2
  if x < 0 and y < 0: return n == 3
  if x > 0 and y < 0: return n == 4
  return False

def theSameQuater( p1, p2 ):
   return p1[0]*p2[0] > 0 and p1[1]*p2[1] > 0


k = [0]*4
k1 = 0
for i in range(len(p1)):
  for q in range(4):
    if isQuater(p1[i],q+1) and isQuater(p2[i],q+1) and isQuater(p3[i],q+1):
      k[q] += 1

  if theSameQuater(p1[i],p2[i]) and theSameQuater(p2[i],p3[i]):
    k1 += 1
    print( i, p1[i], p2[i], p3[i])

print(k, sum(k))
print(k1)