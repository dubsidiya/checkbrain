N = 350000
m = 63636
B = 1000000

step = 3

Nmod = N
while (Nmod - m) % step != 0:
  Nmod -= 1
#print( Nmod )

f = [0]*(N+7)
for n in range(Nmod+6, m-step, -step):
  if n > N: f[n] = n**n
  else: f[n] = 3*n + f[n + 2*step] + 2*f[n+step]
  f[n] = f[n] % B

print( f[m] )

#-----------------------------------------------

N = Nmod
f = [(N+step)**(N+step)%B, (N+2*step)**(N+2*step)%B]

n = N
while n >= m:
  f = [(3*n+2*f[0]+f[1]) % B ] + f[:-1]
  n -= step

print( f[0] )

