from itertools import product

A = "ДГИАШЭ"
G = "ИАЭ"
count = 0
for w in product(A, repeat=5):
   count += (w[0] not in G and w[-1] in G)

print( count )