def sumdiv( n ):
  return sum( i for i in range(1,n+1)
                if n % i == 0 )

def F( start, end ):
  return 1 if start == end else \
         0 if start > end else \
         F(start+1, end) + F(start+sumdiv(start), end)

print( F(2,62) )

#------------------------------------
# Автор: М. Шагитов

lst = [0] * 300
lst[2] = 1
for i in range(2, 62):
    lst[i + 1] += lst[i]
    lst[i + sumdiv(i)] += lst[i]
print(lst[62])
