import json
import pandas as pd

catalogue = pd.read_csv("catalogue.csv")

def get_subcategories():
    subcategories = []
    for subcategory in catalogue["subcategory"]:
        if subcategory not in subcategories:
            subcategories.append(subcategory)
    return subcategories

def get_tags_for_subcategory(subcategory):
    tags = []
    subcatalogue = catalogue[catalogue["subcategory"] == subcategory]
    for tag in subcatalogue["tags"]:
        if tag not in tags:
            tags.append(tag)
    return tags

def get_brands_for_tag_in_subcategory(tag, subcategory):
    brands = []
    subcatalogue = catalogue[(catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag)]
    for brand in subcatalogue["prod_brand"]:
        if brand not in brands:
            brands.append(brand)
    return brands

def get_products(brand, tag, subcategory):
    products = []
    subcatalogue = catalogue[(catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag) & (catalogue["prod_brand"] == brand)]
    return subcatalogue.values.tolist() 


def has_subcategory(subcategory):
    return (catalogue["subcategory"] == subcategory).any()

def has_tag_for_subcategory(tag, subcategory):
    return ((catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag)).any()

def has_brand_for_tag_in_subcategory(brand, tag, subcategory):
    return ((catalogue["subcategory"] == subcategory) & (catalogue["tags"] == tag) & (catalogue["prod_brand"] == brand)).any()

