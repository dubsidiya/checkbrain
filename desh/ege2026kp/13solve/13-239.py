from ipaddress import ip_network

ip = '83.152.68.115/255.255.224.0'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )