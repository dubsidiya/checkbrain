from ipaddress import ip_network

ip = '193.18.135.201'
nOnes = 19

for i in range(31,15,-1):
  net = ip_network( f'{ip}/{i}', 0 )
  count = sum( f'{ip:b}'.count('1') == nOnes
               for ip in net )
  print( 32-i, net, count )