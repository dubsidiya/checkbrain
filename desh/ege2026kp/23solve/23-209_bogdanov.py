def f(a,b,l=0):
  if a>b: return 0
  if a==b: return l%2
  return f(a+2,b,l+1)+f(a*2,b,l+1) \
    +(0 if a==1 else f(a**2,b,l+1))

print(f(1,100))
