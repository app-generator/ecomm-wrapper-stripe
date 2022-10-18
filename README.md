# Simple Python Wrapper for Stripe

Simple **Python** library that pulls the products from **Stripe** dashboard in `JSON format` using only **STRIPE_API_KEY** as input. 

> Actively supported by [AppSeed](https://appseed.us/) via `Email` and `Discord`. Available items:

- `Product` Meta Information:
  - ID, name, description
- `All Images`
- `All Prices` 
- The `default price` 
  - separate node for quick access

<br />

## Quick Start

<br />

> **Install the package** via `PIP` 

```bash
$ pip install python-stripe
```

<br />

> **Usage in code**

```python

from stripe_python import get_products

STRIPE_KEY  = 'YOUR_key_here' # mandatory parameter  
OUTPUT_FILE = 'products.json' # optional   

get_products( STRIPE_KEY, OUTPUT_FILE ) 
```

All products associated with the account are pulled in `products.json`. Here is a sample output using an account with one product (multiple prices): 

```json
{
    "data": [
        {
            "id": "prod_L3QBiEdGWquAHl",
            "name": "Django Datta Able PRO",
            "description": "Premium Django Seed project",
            "images": [
                "https://files.stripe.com/links/MDB8YWNjdF8xSGxXdEdHTExkMVgwN1ZVfGZsX3Rlc3RfZjNtOGxwZTRFdGp1MGp1N2ZUeFlENU9Q008T4Zyl6Z"
            ],
            "price_dfault": {
                "price_1KNJKmGLLd1X07VUqu1kDHO2": 99.0
            },
            "prices": {
                "price_1LuEz0GLLd1X07VUpsvuNCT8": 119.0,
                "price_1KNJKmGLLd1X07VUqu1kDHO2": 99.0
            }
        }
    ]
}
```

<br />

> `Product Image` pulled from **Stripe**

![Django Datta Able PRO - Stripe Image](https://files.stripe.com/links/MDB8YWNjdF8xSGxXdEdHTExkMVgwN1ZVfGZsX3Rlc3RfZjNtOGxwZTRFdGp1MGp1N2ZUeFlENU9Q008T4Zyl6Z)

<br />

## Standalone Execution

<br />

> **Step 1** - Clone the sources from [public repository](https://github.com/app-generator/ecomm-wrapper-stripe)

```bash
$ git clone https://github.com/app-generator/ecomm-wrapper-stripe.git
$ cd ecomm-wrapper-stripe
```

<br />

> **Step 2** - Create `.env` using provided `env.sample`

 Add `.env` file in your projects root directory and add the following credentials

```
STRIPE_API_KEY=<REAL_VALUE_HERE>
```

<br />

> **Step 2** - Install `dependencies`

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br /> 

> **Step 3** - Pull the products from Stripe dashboard

```bash
$ python run.py
```

The products are saved in `products.json` (current working directory). Available props: 

- `id`
- `name`
- `description`
- `images`
- `price` (all)

<br />

## Credits & Links

- Free [support](https://appseed.us/support) via Email & Discord 
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
**Simple Python Wrapper for Stripe** - Free library provided by [AppSeed](https://appseed.us).
