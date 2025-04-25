import ipaddress
ip=ipaddress.ip_address("192.168.1.1")
print("IP is private:",ip.is_private)
print("IP is global :",ip.is_global)
print("IP is multicast:",ip.is_multicast)