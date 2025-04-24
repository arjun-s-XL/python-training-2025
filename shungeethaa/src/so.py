import re

def parse_interface_output(output: str) -> dict:
    data = {}

    # 1. Interface name, status, and protocol
    match = re.search(r"^(\S+) is (\w+), line protocol is (\w+)", output, re.M)
    if match:
        data["interface_name"] = match.group(1)
        data["interface_status"] = match.group(2)
        data["protocol_status"] = match.group(3)

    # 2. IP Address
    match = re.search(r"Internet address is (\S+)", output)
    if match:
        data["ip_address"] = match.group(1)

    # 3. MAC Address
    match = re.search(r"address is (\S+)", output)
    if match:
        data["mac_address"] = match.group(1)

    # 4. MTU, Bandwidth, Delay
    match = re.search(r"MTU (\d+) bytes, BW (\d+) Kbit/sec, DLY (\d+) usec", output)
    if match:
        data["mtu"] = int(match.group(1))
        data["bandwidth"] = int(match.group(2))
        data["delay"] = int(match.group(3))

    # 5. Input and Output Rate
    match = re.search(r"5 minute input rate (\d+) bits/sec", output)
    if match:
        data["input_rate"] = int(match.group(1))

    match = re.search(r"5 minute output rate (\d+) bits/sec", output)
    if match:
        data["output_rate"] = int(match.group(1))

    # 6. Input and Output Packets
    match = re.search(r"(\d+) packets input", output)
    if match:
        data["input_packets"] = int(match.group(1))

    match = re.search(r"(\d+) packets output", output)
    if match:
        data["output_packets"] = int(match.group(1))

    return data

# Sample output
output = """GigabitEthernet0/0 is up, line protocol is up
  Hardware is iGbE, address is 00a1.b2c3.d4e5 (bia 00a1.b2c3.d4e5)
  Internet address is 192.168.1.1/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec
     5 minute input rate 1000 bits/sec, 2 packets/sec
     5 minute output rate 2000 bits/sec, 3 packets/sec
     12345 packets input, 9876543 bytes
     54321 packets output, 8765432 bytes"""

# Parse and print results
result = parse_interface_output(output)
for key, value in result.items():
    print(f"{key}: {value}")


