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
        dict['id'            ] = product['id']
        dict['name'          ] = product['name']
        dict['description'   ] = product['description']
        dict['images'        ] = product['images']

        # Get default price 
        dict['price_default'  ] = { product["default_price"]["id"]: product["default_price"]["unit_amount"]/100}
        
        # Pull all prices 
        all_prices = stripe.Price.list(product=product["id"]).data
        pricedict = {}

        # Save all prices
        for price in all_prices:
            pricedict[price["id"]] = price["unit_amount"] / 100

        dict['prices'] = pricedict
        productdict.append(dict)

    with open(outputFile, "w") as outfile:

        # json.dump({"data": productdict}, outfile)

        products = json.dumps( {"data": productdict}, indent=4, separators=(',', ': ') )        

        outfile.write( products )
        outfile.close()
