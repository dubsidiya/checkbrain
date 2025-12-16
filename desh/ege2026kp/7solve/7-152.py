from math import ceil, log2

K = 1

R1 = 200
R2 = 300
mu1 = 50
V1c = 8
V2c = 12

V1 = V1c / (1 - mu1/100)
V2 = V1*(R2/R1)**2

# V2 = V2c / (1 - mu2/100)

mu2 = (1 - (V2c/V2))* 100

print( round(mu2)  )

