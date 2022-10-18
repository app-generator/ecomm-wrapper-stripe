from dotenv import load_dotenv
import os
from getstripeproducts import get_products
load_dotenv()

load_dotenv()

get_products(os.getenv('STRIPE_API_KEY'))