from math import ceil, log2

K = 1

R1 = 150
R2 = 300
mu1 = 30
V1c = 10
V2c = 15

V1 = V1c / (1 - mu1/100)
V2 = V1*(R2/R1)**2

# V2 = V2c / (1 - mu2/100)

mu2 = (1 - (V2c/V2))* 100

print( round(mu2)  )

