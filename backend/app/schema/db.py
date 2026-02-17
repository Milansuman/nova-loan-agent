from typing import TypedDict
from schema.customer import Customer
from schema.product import Product

class Database(TypedDict):
    products: list[Product]
    customer: list[Customer]