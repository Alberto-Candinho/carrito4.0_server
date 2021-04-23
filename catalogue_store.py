import json
import pandas as pd

catalogue = pd.read_csv("catalogo_gadis.csv")

def get_categories():
    categories = []
    for category in catalogue["categoria"]:
        if not any(category_dict['nome'] ==  category for category_dict in categories):
            category_dict = {
                "nome": category,
            }
            categories.append(category_dict)
    return categories

def get_products(category):
    subcatalogue = catalogue[catalogue["categoria"] == category]
    return subcatalogue.to_dict(orient="records") 

def get_id(id_number):
    id_info = catalogue[catalogue["id"] == int(id_number)]
    return id_info.to_dict(orient="records") 

def has_category(category):
    return (catalogue["categoria"] == category).any()

def has_id(id_number):
    return (catalogue["id"] == int(id_number)).any()

