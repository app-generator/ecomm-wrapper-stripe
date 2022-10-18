# Minimal Pythin warpper for Stripe

This minimal library pulls the products from Stripe in `JSON` format. 

<br />

## ✨ Quick Start

<br />

> 👉 **Step 1** - Create `.env` using provided `env.sample`

 Add `.env` file in your projects root directory and add the following credentials

```
STRIPE_API_KEY=<REAL_VALUE_HERE>
```

<br />

> 👉 **Step 1** - Install `dependencies`

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br /> 

> 👉 Pull the products from Stripe dashboard

```bash
$ python run.py
```

The products are saved in `products.json`. Available props: 

- `id`
- `name`
- `description`
- `images`
- `price`

<br />