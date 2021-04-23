from flask import jsonify
import pandas as pd
import catalogue_store

product_info = catalogue_store.get_id(1)
if(catalogue_store.has_id(1)):
    print(product_info)
