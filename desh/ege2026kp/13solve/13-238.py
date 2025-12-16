from ipaddress import ip_network

ip = '123.215.104.78/255.255.252.0'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )