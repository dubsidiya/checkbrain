v = 62800
t = 9
W, H = 690, 440
I = v * 9
for i in range(1,20):
  F = (W*H*i + 10*2**13) / 1.25
  if F <= I:
    print( 2**i )

print('----------------------')

V = v * t
I0 = V * 1.25
Idata = I0 - 10*2**13
i = int( Idata / (W*H) )
print( 2**i )