# Автор: А. Богданов

s = open('24-221.txt').read()

for c in '23456789':
  s = s.replace(c,' ')

s = s.replace('10','1 0').split()

print(max((len(z) for z in s if '01' in z),default=0))
