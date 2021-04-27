import json
import pandas as pd

catalogue = pd.read_csv("catalogo_gadis.csv")

def get_categories():
    categories = []
    categories.append({
            "nome": "Ofertas",
    })
    for category in catalogue["categoria"]:
        if not any(category_dict['nome'] ==  category for category_dict in categories):
            category_dict = {
                "nome": category,
            }
            categories.append(category_dict)
    return categories

def get_products(category):
    if(category != "Ofertas"):
        subcatalogue = catalogue[catalogue["categoria"] == category]
        subcatalogue = subcatalogue.sort_values(by=["desconto"], ascending=False)
        return subcatalogue.to_dict(orient="records") 
    else:
        subcatalogue = catalogue[catalogue["desconto"] != 0]
        subcatalogue = subcatalogue.sort_values(by=["desconto"], ascending=False)
        return subcatalogue.to_dict(orient="records")

def get_id(id_number):
    id_info = catalogue[catalogue["id"] == int(id_number)]
    return id_info.to_dict(orient="records") 

def has_category(category):
    if(category != "Ofertas"):
        return (catalogue["categoria"] == category).any()
    else:
        return True

def has_id(id_number):
    return (catalogue["id"] == int(id_number)).any()

