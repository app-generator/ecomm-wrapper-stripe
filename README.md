# Simple Python Wrapper for Stripe

This minimal library pulls the products from Stripe in [JSON format](https://github.com/app-generator/ecomm-wrapper-stripe/blob/main/products.json) using `STRIPE_API_KEY` as input, loaded from environment.   

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

All products associated with the account are pulled in `products.json`.

<br />

## Standalone Execution

<br />

> **Step 1** - Create `.env` using provided `env.sample`

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
- `price`

<br />

## Credits & Links

- Free [support](https://appseed.us/support) via Email & Discord 
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
**Simple Python Wrapper for Stripe** - Free library provided by [AppSeed](https://appseed.us).
