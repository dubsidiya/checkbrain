def F( n ):
  return n if n >= 2025 else \
         2*n + F(n+2)

print( F(82) - F(81) )