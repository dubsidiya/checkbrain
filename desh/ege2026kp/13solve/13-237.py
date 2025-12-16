from ipaddress import ip_network

ip = '218.194.82.148/255.255.255.192'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )