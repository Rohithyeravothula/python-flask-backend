import os


hints = {
    (64, 5840): "Linux (kernel 2.4 and 2.6)",
    (64, 5720): "Google customized Linux",
    (64, 65535): "FreeBSD",
    (128, 65535): "Windows XP",
    (128, 8192): "Windows 7",
    (255, 4128): "Cisco Router",
    (64, 65535):"Apple",
    (64, 32120): "Linux Kernel 2.2",
    (64, 16384): "Open BSD AIX 4.3",
    (128, 16384): "Windows 2000",
    (255, 8760): "Solaris 7",
    (128, 8192): "Windows Vista"
}


{'Linux (kernel 2.4 and 2.6)': 0, 'Google customized Linux': 1, 'Apple': 2, 'Windows XP': 3, 'Windows Vista': 4, 'Cisco Router': 5, 'Linux Kernel 2.2': 6, 'Open BSD AIX 4.3': 7, 'Windows 2000': 8, 'Solaris 7': 9}

hints = {
    (64, 5840): "1",
    (64, 5720): "2",
    (64, 65535): "3",
    (128, 65535): "4",
    (128, 8192): "5",
    (255, 4128): "6",
    (64, 65535):"7",
    (64, 32120): "8",
    (64, 16384): "9",
    (128, 16384): "10",
    (255, 8760): "11",
    (128, 8192): "12"
}

# data_dir = "/home/rohith/Desktop/ISI-Hackathon/exp/data"
#
# all_files = os.listdir(data_dir)
#
# for filename in all_files:
#     resolved_data = []
#     with open(os.path.join(data_dir, filename), 'r') as fp:
#         for line in fp.readlines():
#             ip, ttl, size = line.split("\t")
#             if (int(ttl), int(size)) in hints:
#                 resolved_data.append(",".join([hints[(int(ttl), int(size))], ip, ttl, size]))
#
#     with open("resolved/" + filename+"_resolved.txt", 'w') as fp:
#         fp.write("".join(resolved_data))




data_dir = "/home/rohith/Desktop/ISI-Hackathon/exp/full_data/resolve"


all_files = os.listdir(data_dir)

for filename in all_files:
    associations = {}
    name = os.path.basename(filename)
    if "_data" in name:
        continue
    filename = os.path.join(data_dir, filename)
    with open(filename) as fp:
        # print(filename)
        for line in fp.readlines():
            # print(line)
            (ip, ttl, size) = line.split("\t")
            if (int(ttl), int(size)) in hints:
                associations[ip] = hints[int(ttl), int(size)]

    filename = os.path.join(data_dir, name+"_data.csv")
    resolved_data = []
    count = 0
    # print(associations)
    # print(filename)
    with open(filename) as fp:
        for line in fp.readlines():
            ip = line.split(",")[10][1:-1]
            if ip in associations:
                count += 1
                resolved_data.append(line[:-1] + ",\"" + associations[ip]+"\"")
            # else:
            #     resolved_data.append(line)

    print(count)

    with open("full_data_resolve/" + name+"_resolved.csv", 'w') as fp:
        fp.write("\n".join(resolved_data))







