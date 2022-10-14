
import os, sys

from py_stripe import *

def main():
        
    try:
        
        print(' EXEC -> ' + os.path.basename(__file__)) 

        # Input: Stripe Secrets loaded from .env
        # Output: products.json 
        get_products(None, None)

        # Unix ErrCode
        exit(0)

    except Exception as e:

        print( 'Err: ' + str( e ) )
        exit(1)

if __name__ == '__main__':
    main()
