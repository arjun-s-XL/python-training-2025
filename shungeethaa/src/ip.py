
import ipaddress

# ip = ipaddress.ip_address('192.168.1.1')
# print(ip)
# print(type(ip))

# ipv6 = ipaddress.ip_address('2001:0db8::1')
# print(ipv6)
# print(type(ipv6))

# network = ipaddress.ip_network('192.168.1.0/24')
# print(network)
# print("All hosts in network:")
# for host in network.hosts():
#     print(host)


ip = ipaddress.ip_address('192.168.1.10')
network = ipaddress.ip_network('192.168.1.0/24')

print(ip in network)  # True
