
digits = '0123456789'
for a in digits:
  for b in digits:
    s = f'12345{a}6{b}8'
    n = int(s)
    if n % 17 == 0:
      print( n, n//17 )
