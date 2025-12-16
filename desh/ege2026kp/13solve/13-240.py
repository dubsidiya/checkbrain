from ipaddress import ip_network

ip = '98.112.180.225/255.255.240.0'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )