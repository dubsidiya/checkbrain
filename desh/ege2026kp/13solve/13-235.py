from ipaddress import ip_network

ip1 = '113.188.14.51'
ip2 = '113.188.6.86'
nOnes = 17

for i in range(31,15,-1):
  net1 = ip_network( f'{ip1}/{i}', 0 )
  net2 = ip_network( f'{ip2}/{i}', 0 )
  if net1 == net2:
    count = sum( f'{ip:b}'.count('1') == nOnes
               for ip in net1 )
    print( i, net1, count )