from customer import *
from product import *

class Store():
    def __init__(self):
        self.products = set()
        self.customers = []

    def add_product(self, product):
        if self.get_product_with_id(product.id) == None:
            self.products.add(product)
    
    def remove_product(self, product):
        try:
            self.products.remove(product)
        except Exception:
            raise Exception("Product not in store")

    def view_products(self):
        return self.products

    def add_new_customer(self):
        self.customers.append(Customer())

    def get_first_customer(self):
        try:
            return self.customers[0]
        except Exception:
            raise Exception("No customers in store")
    
    def get_product_with_id(self, id):
        for item in self.products:
            if item.get_id() == id:
                return item
        return None