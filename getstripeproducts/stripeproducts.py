import stripe
import json

def get_products(apikey):
    stripe.api_key = apikey
    products = stripe.Product.list(expand = ['data.default_price'])
    productdict = []
    for product in products:
        dict= {}
        dict['id'] = product['id']
        dict['Name'] = product['name']
        dict['Description'] = product['description']
        dict['Images'] = product['images']
        dict['Price'] = product["default_price"]["unit_amount"]/100
        productdict.append(dict)

    with open("stripeproductlist.json", "w") as outfile:
        json.dump({"data": productdict}, outfile)

