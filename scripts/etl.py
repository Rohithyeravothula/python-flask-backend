import pandas as pd
import csv
import os

data_dir = "/home/rohith/Desktop/ISI-Hackathon/UN_dataset"
outputfilename = "/home/rohith/Desktop/ISI-Hackathon/cleandata.csv"
column_names = ['srcip', 'sport', 'dstip', 'dsport', 'proto', 'state', 'dur', 'sbytes', 'dbytes',
                'sttl', 'dttl', 'sloss', 'dloss', 'service', 'Sload', 'Dload', 'Spkts', 'Dpkts',
                'swin', 'dwin', 'stcpb', 'dtcpb', 'smeansz', 'dmeansz', 'trans_depth',
                'res_bdy_len', 'Sjit', 'Djit', 'Stime', 'Ltime', 'Sintpkt', 'Dintpkt', 'tcprtt',
                'synack', 'ackdat', 'is_sm_ips_ports', 'ct_state_ttl', 'ct_flw_http_mthd',
                'is_ftp_login', 'ct_ftp_cmd', 'ct_srv_src', 'ct_srv_dst', 'ct_dst_ltm',
                'ct_src_ ltm', 'ct_src_dport_ltm', 'ct_dst_sport_ltm', 'ct_dst_src_ltm',
                'attack_cat', 'Label']
useful_columns = ["srcip", "sport", "dstip", "dsport", "proto", "service", "Stime", "Label"]
usefule_column_indices = [0, 1, 2, 3, 4, 13, 28, 48]



clean_data = []
all_files = os.listdir(data_dir)
print(all_files)


for filename in all_files:
    with open(os.path.join(data_dir, filename), 'r') as fp:
        data = csv.reader(fp, delimiter='\t')
        for line in data:
            clean_line = []
            for i in usefule_column_indices:
                try:
                    clean_line.append(line[i])
                except:
                    print(line)
                    break
            clean_data.append("\t".join(clean_line))


with open(outputfilename, 'w') as fp:
    fp.write("\n".join(clean_data))




