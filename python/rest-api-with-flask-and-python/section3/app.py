from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

stores = [
    {
        'name': 'My Wornderful Store',
        'items': [
            { 
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    store = list(filter(lambda s: s["name"] == name, stores))
    for store in stores:
        if store['name'] == name:
            return jsonify(store), 200
    return jsonify({'message': 'Not Found'}), 404


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            request_data = request.get_json()
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store), 200
    return jsonify({'message': 'Store not found'}), 404


@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']}), 200
    return jsonify({'message': 'Store not found'}), 404


app.run(port=5000)


