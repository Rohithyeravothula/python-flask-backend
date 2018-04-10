import random
import time
import datetime
import socket
import struct

generic = ["Laptop", "Macbook Pro"]
iot_devices = ["Amazon Alexa", "Amazon Echo", "Google Home"]
sensors = ["Thermostat", "Light"]


generic_ips = ["192.168.1.108", "192.168.1.103", "192.168.1.113"]
iot_ips = ["192.168.1.21", "192.168.1.91", "192.168.1.93"]



iot_devices_allowed_ips = ["205.251.242.103", "172.217.14.110", "192.30.255.112", "104.192.143.7"]

generic_blocked_ips = ["91.121.149.203", "111.222.333.44", "555.444.333.22"]
iot_devices_blocked_ips = ["66.211.162.12", "31.13.70.36", "191.239.213.197"]


protocol_ports = [("http", "80"), ("https", "443"), ("ftp", "20"), ("ftp", "21"), ("snmp", "88"),
                  ("ssh", "22"), ("tftp", "69"), ("gopher", "70"), ("dhcpv6", "546"), ("dhcp", "67"),
                  ("echo", "7"), ("whois", "42"), ("hostname", "101"), ("snmp", "161"), ("bgp", "179"),
                  ("rip", "520"), ("telnet", "23"), ("sftp", "115")]

def get_random_ip():
    return str(socket.inet_ntoa(struct.pack('>I', random.randint(3221225472, 0xffffffff))))

def get_random_port():
    return random.ranint(0, 2)

def get_random_time():
    return str(time.time() + random.randint(0, 1000))

def get_random_date():
    return str(datetime.date(2018, 5, random.randint(1, 5)))

def get_lan_ip():
    return

data = []
good_packets = 100







# good data
while good_packets > 0:
    good_packets -= 1
    flip = random.randint(0,1)
    if flip:
        device_ip = random.choice(generic_ips)
        device = random.choice(generic)
        device_port = get_random_port()
        dest_ip = get_random_ip()
        protocol, dest_port = random.choice(protocol_ports)
        timestamp = get_random_time()
        data.append(",".join([timestamp, device_ip, device_port, dest_ip, dest_port, protocol, '1']))
    else:
        iot_ip = random.choice(iot_ips)
        device = random.choice(iot_devices)
        device_port = get_random_port()
        dest_ip = random.choice(iot_devices_allowed_ips)
        protocol, dest_port = random.choice(protocol_ports)
        timestamp = get_random_time()
        data.append(",".join([timestamp, iot_ip, device_port, dest_ip, dest_port, protocol, '1']))


bad_packets = 10

# good data
while bad_packets > 0:
    bad_packets -= 1
    flip = random.randint(0,1)
    if flip:
        device_ip = random.choice(generic_ips)
        device = random.choice(generic)
        device_port = get_random_port()
        dest_ip = random.choice(generic_blocked_ips)
        protocol, dest_port = random.choice(protocol_ports)
        timestamp = get_random_time()
        data.append(",".join([timestamp, device_ip, device_port, dest_ip, dest_port, protocol, '0']))
    else:
        iot_ip = random.choice(iot_ips)
        device = random.choice(iot_devices)
        device_port = get_random_port()
        dest_ip = random.choice(iot_devices_blocked_ips)
        protocol, dest_port = random.choice(protocol_ports)
        timestamp = get_random_time()
        data.append(",".join([timestamp, iot_ip, device_port, dest_ip, dest_port, protocol, '0']))


for line in data:
    print(line)