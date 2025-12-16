# Автор: Р. Косов

from ipaddress import *
address = '172.95.116.174'
mask = '255.255.192.0'
net = ip_network(f'{address}/{mask}',0)
print(net[1])

print( sum( map(int, str(net[1]).split('.')) ) )
