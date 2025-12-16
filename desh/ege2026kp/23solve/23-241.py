from functools import cache

cost = [
[int(x) for x in "0 3	3	3	1	3	2	3	2	1	4	5	4	5	2	3	3".split()],
[int(x) for x in "0 1	2	1	2	3	2	1	2	3	2	3	2	1	1	3	1".split()],
[int(x) for x in "0 1	4	2	2	2	1	2	3	2	3	4	3	4	3	2	4".split()]
]

@cache
def f( start, end, total = 0 ):
   if start > end: return 10**10
   if start == end: return total
   return min( f( start+1, end, total+cost[0][start] ) ,
               f( start+2, end, total+cost[1][start] ),
               f( start*2, end, total+cost[2][start] )   )

print( f(1, 16) )