import pandas as pd
from random import randint, choice

filename = "../dataset.csv"

data = pd.read_csv(filename)

unique_source = data["Source"].unique()
unique_destination = data["Destination"].unique()

all_ips = list(set(list(unique_source) + list(unique_destination)))

mac_extension = "ignore"

mac_addresses = ["00012A", "000393", "000502", "000A27"]
software_identification = ["Mac OS X", "Time Machine", "Unix", "The Shell Terminal", "Ubuntu",
                    "Simplified Linux Setup", "BeOS", "64-Bit Journaling File System", "IRIX SGI Dogfight",
                    "NeXTSTEP", "MS-DOS"]
# software_identification = ["Linux 4.13.0-38-generic", "Linux 2.13.0-47-apple", "3.0-38-mac"]
software_version = ["v1", "v2", "v3", "v4", "v5"]
device_class = ["Camera", "Mobile", "Laptop", "Coffee Machine", "Desktop"]
device_identification = ["Apple", "Lenovo", "Lenovo thinkpad", "MBP", ""]
protocols = ["http", "tcp", "udp", "generic"]
ports = ['22-500', '80-484', '443-677', '8080-9000', '4000-5676', '8972-32000', '27000-60000']



device_data = []

for ip_addr in all_ips:
    line = []
    line.append(ip_addr)
    line.append(choice(mac_addresses) + mac_extension)
    line.append(choice(software_identification))
    line.append(choice(software_version))
    line.append(choice(ports))
    line.append(choice(device_class))
    line.append(choice(device_identification))
    line.append(choice(protocols))
    device_data.append(",".join(list(map(lambda x: str(x), line))))


with open("device_information.txt", 'w') as fp:
    fp.write("\n".join(device_data))



"""
IP Address,Mac address,Software Identification,Software Version,Device Class,Device Identification,,Open Ports,Communication Ranges and Protocols
"""