with open( "9-191.csv" ) as F:
  count = 0
  for s in F:
    row = list( map(int, s.split(';')) )
    doubles = [ x for x in row if row.count(x) > 1 ]
    singles = [ x for x in row if row.count(x) == 1 ]
    if singles and doubles:
       if sum(singles)*len(doubles) == sum(doubles)*len(singles):
         count += 1

print( count )
