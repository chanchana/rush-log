from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import datetime as dt

filename = 'data.log'

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/')
def log():
    addr = str(request.remote_addr)
    datetime = str(dt.datetime.now())
    req = str(request)
    print(dir(request))
    text = addr + ', ' + datetime + ', ' + req + '\n'
    print(text)
    with open(filename, 'a') as f:
        f.write(text)
    return redirect('http://nsc-rush.s3-website-ap-southeast-1.amazonaws.com')

@app.route('/view')
def show():
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line)
    print(data)
    return jsonify({'data': data})

app.run(host='178.128.24.70', port=8080)


