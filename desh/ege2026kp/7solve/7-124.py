from math import pi
D = 40
cmInInch = 2.54
ppi = 300
R = D / 2
S = 4*pi*R**2
print( f"S = {S}" )
a = cmInInch # S**0.5
print( f"a = {a}" )
aInch = a / cmInInch
print( f"ai = {aInch}'" )

b = S / a
print( f"b = {b}" )
bInch = b / cmInInch
print( f"bi = {bInch}'" )

from math import ceil
w, h = ceil(aInch*ppi), ceil(bInch*ppi)
I = w*h*24 / 2**23
print( f"I = {I} Mb'" )
print( f"I = {ceil(I)} Mb'" )


