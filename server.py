from flask import Flask, render_template, jsonify, request, abort
import json
# from corsdecorator import crossdomain
import time
from drone_delivery import get_delivery_order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True


p0 = {'name': 'p0', 'latlon': (-33.891413, 151.268683)}
p1 = {'name': 'p1', 'latlon': (-33.891338, 151.274032)}
p2 = {'name': 'p2', 'latlon': (-33.889167, 151.270709)}
p3 = {'name': 'p3', 'latlon': (-33.891867, 151.272004)}
p4 = {'name': 'p4', 'latlon': (-33.894699, 151.268533)}
p5 = {'name': 'p5', 'latlon': (-32.894699, 151.238533)}
p6 = {'name': 'p6', 'latlon': (-31.894699, 151.268433)}
p7 = {'name': 'p7', 'latlon': (-33.895699, 151.258533)}
p8 = {'name': 'p8', 'latlon': (-33.893699, 151.298533)}
p9 = {'name': 'p9', 'latlon': (-32.894699, 151.268533)}
p10 = {'name': 'p10', 'latlon': (-30.894699, 150.268533)}
points = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/delivery_order', methods=['POST'])
def get_ordered_delivery_points():
    payload = request.get_json()
    print(payload)
    
    return jsonify(get_delivery_order(payload['delivery_points']))


if __name__ == '__main__':
    app.run(port=8000)