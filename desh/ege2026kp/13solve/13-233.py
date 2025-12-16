from ipaddress import ip_network

ip = '132.118.34.161'
nOnes = 13

for i in range(31,15,-1):
  net = ip_network( f'{ip}/{i}', 0 )
  count = sum( f'{ip:b}'.count('1') == nOnes
               for ip in net )
  print( i, net, count )