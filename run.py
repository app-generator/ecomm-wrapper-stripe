# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from dotenv import load_dotenv

from stripe_python import get_products

load_dotenv()

if __name__ == "__main__":

    STRIPE_API_KEY = os.getenv('STRIPE_API_KEY', None)

    if STRIPE_API_KEY:
        get_products( STRIPE_API_KEY )
    else:
        print( 'Err: STRIPE_API_KEY not provided in ENV' )
