def f( start, end, trajectory = [] ):
  trajectory = trajectory + [start]
  if start == end:
    return 1 if any( (x+y+z) % 11 == 0
                     for x, y, z in zip(trajectory, trajectory[1:],
                                        trajectory[2:])  )  \
           else 0
  elif start > end: return 0
  else:
    return f(start+2, end, trajectory) + \
           f(start*3, end, trajectory) + \
           f(start*4, end, trajectory)

print( f( 1, 600 ) )


# Автор: И. Гордеев

def f( start, end, tr = [] ):
  tr=tr + [start]
  if start == end:
      for i in range(len(tr)-2):
        if sum(tr[i:i+3])%11==0:
          return 1
      return 0
  elif start > end: return 0
  else:
    return f(start+2, end, tr ) + \
           f(start*3, end, tr ) + \
           f(start*4, end, tr )

print( "Начальное число входит в траекторию:", f( 1, 600 ) )
print( "Начальное число не входит в траекторию:", f( 1+2, 600 )+f(1*3,600)+f(1*4,600) )
