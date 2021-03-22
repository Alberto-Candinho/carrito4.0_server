from flask import Flask
from flask import request
from flask import jsonify
import catalogue_store
import json 
import codecs

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def get_subcategories():
    return jsonify(
            status=200,
            categories=catalogue_store.get_subcategories()
    )


@app.route('/<subcategory>/<tag>', methods = ['GET'])
def get_products(tag, subcategory):
    if(catalogue_store.has_tag_for_subcategory(tag, subcategory)):
        return jsonify(
            status=200,
            products=catalogue_store.get_products(tag, subcategory)
        )
    elif(catalogue_store.has_subcategory(subcategory)):
        return jsonify(
            status=404,
            products='Tag ' + str(tag) + ' not present in subcategory ' + str(subcategory)
        )
    else:
        return jsonify(
            status=404,
            products='Subcategory ' + str(subcategory) + ' not found'
        )

app.run(host='192.168.8.106', port= 8090)
