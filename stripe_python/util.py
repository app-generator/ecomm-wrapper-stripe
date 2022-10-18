# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import stripe
import json

def get_products( stripeApiKEY, outputFile='products.json'):

    stripe.api_key = stripeApiKEY
    products       = stripe.Product.list(expand = ['data.default_price'])

    productdict = []
    for product in products:
        dict= {}
        dict['id'          ] = product['id']
        dict['Name'        ] = product['name']
        dict['Description' ] = product['description']
        dict['Images'      ] = product['images']
        dict['Price_Default'       ] = { product["default_price"]["id"]: product["default_price"]["unit_amount"]/100}
        all_prices = stripe.Price.list(product=product["id"]).data
        pricedict = {}

        for price in all_prices:
            pricedict[price["id"]] = price["unit_amount"] / 100

        dict['Prices'] = pricedict
        productdict.append(dict)

    with open(outputFile, "w") as outfile:
        json.dump({"data": productdict}, outfile)

