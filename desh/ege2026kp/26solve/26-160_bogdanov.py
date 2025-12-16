# Автор А. Богданов

(n,), *a = ( tuple(map(int, s.split()))
             for s in open('26-160.txt') )

a.sort( key=lambda x: x[1] )
s = [[0, 0, 0, -1]] # cost,time,cnt,tend
for t0, t1, cost in a:
  mx_cost, total_time, cnt = max( v for *v, t in s if t < t0)
  s += [[mx_cost+cost, total_time+(t1-t0+1), cnt+1, t1]]

print( *max(s)[:3] )