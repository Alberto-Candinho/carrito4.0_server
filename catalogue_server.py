from flask import Flask
from flask import request
from flask import jsonify
import catalogue_store
import json 
import codecs

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_categories():
    return jsonify(
            status=200,
            categories=catalogue_store.get_categories()
    )


@app.route('/<category>', methods = ['GET'])
def get_products(category):
    if(catalogue_store.has_category(category)):
        return jsonify(
            status=200,
            products=catalogue_store.get_products(category)
        )
    else:
        return jsonify(
            status=404,
            products='Category ' + str(category) + ' not found'
        )

@app.route('/id/<id_number>', methods = ['GET'])
def get_id(id_number):
    if(catalogue_store.has_id(id_number)):
        return jsonify(
            status=200,
            info=catalogue_store.get_id(id_number)
        )
    else:
        return jsonify(
            status=404,
            info='There is no element with id ' + str(id_number)
        )

#app.run(host='172.20.10.13', port= 8090)
app.run(host='192.168.1.145', port= 8090)
