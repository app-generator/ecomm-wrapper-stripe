# ecomm-wrapper-stripe

## Install package and run project

Create virtual envirnoment
```
virtualenv --python=python3 venv
```
activate virtual envirnoment
```
source venv/bin/activate (linux/mac)
```

install stripe-wraper and other required packages
```
pip install getstripeproducts-0.0.1-py3-none-any.whl
pip install python-dotenv
```

create .env file and add STRIPE_API_KEY variable init.

.env
```
STRIPE_API_KEY=stripeapikey
```

run script testproduct.py
 ```
python testproduct.py
```
