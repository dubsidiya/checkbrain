def allDivs( n ):
    a = set()
    for i in range(1,int(n**0.5)+1):
        if n % i == 0: a.update([i,n//i])
    return sorted(a)

def check( n ):
  divs = allDivs(n)
  specDivs = [ d for d in divs[:-1]
                 if d % 100 in [29, 51, 78] and d not in [29, 51, 78] ]
  return (specDivs, divs[-2])

count = 0
for n in range(6_700_001,10**10):
    specDivs, maxDiv = check( n )
    if len(specDivs) == 5:
        print( n, maxDiv ) #, specDivs )
        count += 1
        if count == 5: break
