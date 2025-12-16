N = 130000
m = 33122
B = 10000000

f = [0] * (N+5)
for n in range(N+4, m-2, -2):
  if n > N: f[n] = n**n
  else: f[n] = n + f[n + 4] - f[n+2]
  f[n] = f[n] % B

print( f[m] )

#-----------------------------------------------

f = [(N+2)**(N+2)%B, (N+4)**(N+4)%B]

n = N
while n >= m:
  f = [(n-f[0]+f[1]) % B ] + f[:-1]
  n -= 2

print( f[0] )

