from basket import *

class Customer():
    def __init__(self):
        self.basket = Basket()

    def view_basket(self):
        return self.basket.view_products_in_basket()

    def get_basket(self):
        return self.basket