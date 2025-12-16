from ipaddress import ip_network

ip = '135.13.142.29/255.255.255.128'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )