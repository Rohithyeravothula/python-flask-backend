from flask import Flask, render_template, request
import json

app = Flask(__name__)

class_filename = "output.txt"
device_filename = "device_output.txt"


class_schema = ['Date', 'Time', 'Source MAC', 'Source IP', 'Source Port', 'Dest MAC', 'Dest IP',
          'Dest Port', 'Protocol', 'good_packet', 'allowed']

device_schema = ['Mac address', 'IP Address', 'Device Class', 'Device Identification',
                 'Software Identification', 'Software Version', 'Open Ports', 'Communication Ranges and Protocols']

def pprint(collection):
    if isinstance(collection, dict):
        for key, val in collection.items():
            print(key, val)
    else:
        for iter in collection:
            print(iter)


def read_data():
    indexed_json = {}
    sno = 1
    with open(class_filename, 'r') as fp:
        for line in fp.readlines():
            cur_json = {}
            data = line.split(",")
            for index, column in enumerate(class_schema):
                cur_json[column] = data[index].strip()
            indexed_json[sno] = cur_json
            sno+=1
    return indexed_json


def read_device_data():
    indexed_json = {}
    sno = 1
    with open(device_filename, 'r') as fp:
        for line in fp.readlines():
            cur_json = {}
            data = line.split(",")
            for index, column in enumerate(device_schema):
                cur_json[column] = data[index].strip()
            indexed_json[sno] = cur_json
            sno += 1
        return indexed_json



def write_data(data, schema, filename):
    entire_data = []
    for key, val in data.items():
        cur_data = [""]*len(schema)
        for index, col in enumerate(schema):
            cur_data[index] = val[col]
        entire_data.append(",".join(cur_data))
    pprint(entire_data)
    with open(filename, 'w') as fp:
        fp.write("\n".join(entire_data))


@app.route("/index")
def index_page():
    return json.dumps(read_data())

@app.route("/change", methods=["POST"])
def change():
    info = json.loads(request.data)
    cur_output = read_data()
    for key, val in info.items():
        cur_output[int(key)] = val
    write_data(cur_output, class_schema, class_filename)
    return "OK"

@app.route("/device")
def get_device():
    return json.dumps(read_device_data())

@app.route("/device/change", methods=["POST"])
def change_device():
    info = json.loads(request.data)
    cur_output = read_device_data()
    for key, val in info.items():
        cur_output[int(key)] = val
    write_data(cur_output, device_schema, device_filename)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True)