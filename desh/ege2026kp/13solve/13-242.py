from ipaddress import ip_network

ip = '143.168.72.213/255.255.255.240'
net = ip_network( f'{ip}', 0 )
print( net.broadcast_address - 1 )