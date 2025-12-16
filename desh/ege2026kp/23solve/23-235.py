from functools import cache

@cache
def f( start, end, traj = '' ):
   traj += str(start)
   if start > end or '6' in traj: return 0
   if start == end: return 1
   return f( start+1, end, traj ) + f( start+3, end, traj )

print( f(1, 45) )