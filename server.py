from flask import Flask, render_template, jsonify, request, abort
import json
# from corsdecorator import crossdomain
import time
from drone_delivery import get_delivery_order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True


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