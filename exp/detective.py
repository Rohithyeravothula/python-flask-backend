import pandas as pd

filename = "/home/rohith/Desktop/DatasetF123.csv"

data = pd.read_csv(filename)


# ['Date', 'Time/Seq', 'SMAC', 'SIP', 'Sport', 'DMAC', 'DIP', 'Dport', 'Protocol', 'GoodBad', 'AllowBlock', 'Comments']

# print(data.groupby("SIP")["DIP"].unique())
print(data.groupby(["SIP", "DIP"])["DIP", "SIP"].filter(lambda x: len(x) <= 1))