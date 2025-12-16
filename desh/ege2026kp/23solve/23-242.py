from functools import cache

cost = [
[int(x) for x in "0 3	3	3	1	3	2	3	2	1	4	5	4	5	2	3	3".split()],
[int(x) for x in "0 1	4	2	7	2	1	2	3	2	3	4	3	4	3	2	4".split()]
]

minTotal = 10**10
@cache
def f( start, end, total = 0, n1 = 0 ):
   global minTotal
   if start > end: return 10**10
   if start == end:
     if total < minTotal:
        print( total, '->', n1 )
        minTotal = total
     return total
   return min( f( start+1, end, total+cost[0][start], n1+1 ) ,
               f( start*2, end, total+cost[1][start], n1 )   )

print( f(1, 16) )