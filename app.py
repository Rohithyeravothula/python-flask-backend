from flask import Flask, render_template, request
import json

app = Flask(__name__)

filename = "output.txt"



schema = ['Date', 'Time', 'Source MAC', 'Source IP', 'Source Port', 'Dest MAC', 'Dest IP', 'Dest Port', 'Protocol', 'good_packet', ' allowed']

def read_data():
    indexed_json = {}
    sno = 1
    with open(filename, 'r') as fp:
        for line in fp.readlines():
            cur_json = {}
            data = line.split(",")
            print(data)
            for index, column in enumerate(schema):
                cur_json[column] = data[index]
            indexed_json[sno] = cur_json
            sno+=1
    return indexed_json


def write_data(data):
    csv_data = []
    for key, val in data.keys():
        cur_data = [""]*len(schema)
        for index, col in enumerate(schema):
            cur_data[index] = col[schema[index]]
        csv_data.append(",".join(cur_data))
    with open(filename, 'w') as fp:
        fp.write("\n".join(csv_data))


@app.route("/index")
def index_page():
    data = read_data()
    return json.dumps(data)


@app.route("/change", methods=["POST"])
def change():
    info = json.loads(request.data)
    cur_output = read_data()
    for key, val in info.values():
        cur_output[key] = val
    write_data(cur_output)



if __name__ == '__main__':
    app.run(debug=True)