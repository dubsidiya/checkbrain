k = 1
t = 1
while True:
  Iimage = 1920*1080 * 20 * 16 * t
  Isound = 44000*16*t*k
  IMb = (Iimage+Isound) / 1024**2 / 8
  if IMb > 3123: break
  t += 1

print( t-1 )