# Автор: Р. Косов

from ipaddress import *

address = '192.168.12.207'
mask = '255.192.0.0'
net = ip_network(f'{address}/{mask}',0)
res = []
for ip in net:
    dv = bin(int(ip))[2:].zfill(32)
    if dv.count('1') == dv.count('0'):
        res.append(ip)

print( str(res[-1]).replace('.','') )
