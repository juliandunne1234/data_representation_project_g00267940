from flask import Flask, jsonify, request, redirect, abort, jsonify
from werkzeug.datastructures import ContentSecurityPolicy
from cryptoDAO import cryptoDAO
import requests

app = Flask(__name__,
            static_url_path='', 
            static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

@app.route('/cryptos')
def getAll():
    return jsonify(cryptoDAO.getAll())

@app.route('/cryptos/<string:cryptocurrency>')
def findById(id):
    return jsonify(cryptoDAO.findById(id))

@app.route('/cryptos', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    crypto = {
        "id":  request.json['id'],
        "cryptocurrency": request.json['cryptocurrency'],
        "USD_price":request.json['USD_price']
    }
    return jsonify(cryptoDAO.create(crypto))

@app.route('/cryptos/<string:id>', methods =['PUT'])
def update(id):
    foundCrypto = cryptoDAO.findById(id)
    if foundCrypto == {}:
        return jsonify({}), 404
    currentCrypto = foundCrypto
    if 'USD_price' in request.json:
        currentCrypto['USD_price'] = request.json['USD_price']
    cryptoDAO.update(currentCrypto)

    return jsonify(currentCrypto)

@app.route('/cryptos/<string:cryptocurrency>', methods =['DELETE'])
def delete(cryptocurrency):
    cryptoDAO.delete(cryptocurrency)
    return  jsonify( {'done':True })

if __name__ == '__main__' :
    app.run(debug= True)

