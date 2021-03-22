import json
import pandas as pd

catalogue = pd.read_csv("catalogue.csv")

def get_subcategories():
    subcategories = []
    for subcategory in catalogue["subcategory"]:
        if not any(subcategory_dict['name'] ==  subcategory for subcategory_dict in subcategories):
            tags = get_tags_for_subcategory(subcategory)
            subcategory_dict = {
                "name": subcategory,
                "tags": tags
            }
            subcategories.append(subcategory_dict)
    return subcategories

def get_tags_for_subcategory(subcategory):
    tags = []
    subcatalogue = catalogue[catalogue["subcategory"] == subcategory]
    for tag in subcatalogue["tags"]:
        if tag not in tags:
            tags.append(tag)
    return tags

def get_products(tag, subcategory):
    products = []
    subcatalogue = catalogue[(catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag)]
    return subcatalogue.to_dict(orient="records") 

def has_subcategory(subcategory):
    return (catalogue["subcategory"] == subcategory).any()

def has_tag_for_subcategory(tag, subcategory):
    return ((catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag)).any()

