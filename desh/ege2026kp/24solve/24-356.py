from re import findall

s = open('24-356.txt').readline()

num14 = '([1-9A-D][0-9A-D]*[02468AC]|[2468AC])'
pattern = f'(?={num14})'
parts = findall( pattern, s )
sMax = max( parts, key=len )
print( len(sMax), sMax )
