def sumdiv( n ):
  return sum( i for i in range(1,n+1)
                if n % i == 0 )

def F( start, end ):
  return 1 if start == end else \
         0 if start > end else \
         F(start+1, end) + F(sumdiv(start), end)

print( F(2,24) )

#------------------------------------
# Автор: М. Шагитов

lst = [0]*100
lst[2] = 1
for i in range(2,24):
  lst[i+1] += lst[i]
  lst[sumdiv(i)] += lst[i]

print( lst[24] )