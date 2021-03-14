from flask import Flask
from flask import request
from flask import jsonify
import catalogue_store
import json 
import codecs

app = Flask(__name__)

@app.route('/subcategories', methods = ['GET'])
def get_subcategories():
    return jsonify(
            status=200,
            data=catalogue_store.get_subcategories()
    )

@app.route('/subcategories/<subcategory>', methods = ['GET'])
def get_tags_for_subcategory(subcategory):
    #if(subcategory in catalogue_store.get_subcategories()):
    if(catalogue_store.has_subcategory(subcategory)):
        return jsonify(
                status=200,
                data=catalogue_store.get_tags_for_subcategory(subcategory)
        )
    else:
        return jsonify(
                status=404,
                data='Subcategory ' + str(subcategory) + ' not found'
                )

@app.route('/subcategories/<subcategory>/<tag>', methods = ['GET'])
def get_brands_for_tag_in_subcategory(tag, subcategory):
    #if(subcategory in catalogue_store.get_subcategories()):
    #    if(tag in catalogue_store.get_tags_for_subcategory(subcategory)):
    #        return jsonify(
    #                status=200,
    #                data=catalogue_store.get_brands_for_tag_in_subcategory(tag, subcategory)
    #                )
    #    else:
    #        return jsonify(
    #            status=404,
    #            data='Tag ' + str(tag) + ' not present in subcategory ' + str(subcategory)
    #        )
    #else:
    #    return jsonify(
    #            status=404,
    #            data='Subcategory ' + str(subcategory) + ' not found'
    #            )
    if(catalogue_store.has_tag_for_subcategory(tag, subcategory)):
        return jsonify(
            status=200,
            data=catalogue_store.get_brands_for_tag_in_subcategory(tag, subcategory)
        )
    elif(catalogue_store.has_subcategory(subcategory)):
        return jsonify(
            status=404,
            data='Tag ' + str(tag) + ' not present in subcategory ' + str(subcategory)
        )
    else:
        return jsonify(
            status=404,
            data='Subcategory ' + str(subcategory) + ' not found'
        )
                
@app.route('/subcategories/<subcategory>/<tag>/<brand>', methods = ['GET'])
def get_products(brand, tag, subcategory):
    #if(subcategory in catalogue_store.get_subcategories()):
    #    if(tag in catalogue_store.get_tags_for_subcategory(subcategory)):
    #        return jsonify(
    #                status=200,
    #                data=catalogue_store.get_products_for_tag_in_subcategory(tag, subcategory)
    #                )
    #    else:
    #        return jsonify(
    #            status=404,
    #            data='Tag ' + str(tag) + ' not present in subcategory ' + str(subcategory)
    #        )
    #else:
    #    return jsonify(
    #            status=404,
    #            data='Subcategory ' + str(subcategory) + ' not found'
    #            )
    if(catalogue_store.has_brand_for_tag_in_subcategory(brand, tag, subcategory)):
        return jsonify(
            status=200,
            data=catalogue_store.get_products(brand, tag, subcategory)
        )
    elif(catalogue_store.has_tag_for_subcategory(tag, subcategory)):
        return jsonify(
            status=404,
            data='Brand ' + str(brand) + ' not present for ' + str(tag) + ' in ' + str(subcategory)
        )
    elif(catalogue_store.has_subcategory(subcategory)):
        return jsonify(
            status=404,
            data='Tag ' + str(tag) + ' not present in subcategory ' + str(subcategory)
        )
    else:
        return jsonify(
            status=404,
            data='Subcategory ' + str(subcategory) + ' not found'
        )


app.run(host='192.168.8.106', port= 8090)
