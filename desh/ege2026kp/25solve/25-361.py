
for n in range(0,10**10+1,7993):
  s = str(n)
  if s[0] == '4' and s[-1] == '1' and s.find('4736') > 0: # 4*4736*1
    print( n, n//7993 )
