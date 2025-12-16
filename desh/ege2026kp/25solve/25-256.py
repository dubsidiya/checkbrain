for d1 in '02468':
  for d2 in '13579':
    for d3 in '0123456789':
      n = int( f"12{d1}4{d2}6{d3}8" )
      if n % 92 == 0:
        print( n, n // 92 )